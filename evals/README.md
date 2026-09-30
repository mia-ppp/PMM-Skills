# Evals

Zero-dependency harness for the skills in `skills/`. Reads each skill's existing `evals/evals.json`. Python 3.9+ only.

## Commands

| Command | What it answers | API cost |
|---|---|---|
| `lint` | Which skills lack evals, and how many assertions only check format | Free |
| `route` | Does the right skill get picked when every skill competes? | One short call per eval prompt per trial |
| `run` | Does loading the skill beat no skill on the same prompt? | ~2 x cases x trials, plus judge calls |
| `report` | Pass rate, lift vs baseline, variance, dead assertions, calibration rubric scores | Free |
| `calibrate` | Blind outputs for hand-grading the rubrics in `rubrics/` | 30 calls by default |
| `agree` | Does the rubric judge agree with the hand grades? Leave-one-out: each output is judged with its own anchor hidden | One call per graded output |

```bash
export PMM_EVALS_API_KEY=sk-...
python evals/harness.py lint
python evals/harness.py route --trials 1
python evals/harness.py run --skills page-cro,copywriting --trials 3
python evals/harness.py report
python evals/harness.py calibrate
```

Add `--mock` to any command to test the pipeline without a key. Mock results go to `evals/results/mock/` so they never mix with real runs.

## Local regression checks and interpretation

```bash
bash validate-skills.sh
python3 evals/harness.py lint
python3 evals/check_references.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s evals/tests -v
git diff --check
```

- **Structural validation:** skill frontmatter, eval fields/IDs, fixture paths,
  shared references, explicit handoff targets, and README catalog/links. Lint
  exits nonzero on invalid fixtures, missing shared files, or invalid handoffs.
- **Regression/unit validation:** deterministic tests of prompt assembly,
  repository boundaries, failure reporting, isolation, calibration inputs,
  judge inputs, and fixture-sensitive reuse. These never call an API.
- **Mock pipeline validation:** fake generation/routing and random mock grades
  exercise orchestration and result persistence. Mock scores are not evidence
  that a skill makes correct PMM decisions.
- **Real model evaluation:** generation and grading through the configured API.
  Requires authorization for any spend. Historical results describe their own
  samples and revisions, not later additions.

### Fixture convention

Each eval may declare `files` as a list of UTF-8 input paths. Omitted `files` and
`files: []` leave the user prompt unchanged. Paths can be relative to that
skill's `evals/` directory (`fixtures/sample.md`) or the repository root
(`skills/skill-name/evals/fixtures/sample.md`). Reference only the inputs needed
by the case. A verifier case may also name the originating `SKILL.md` and its
required standards. Do not include expected answers as input evidence.

`run` and `calibrate` append exactly the named inputs, in order, to both loaded
and baseline prompts. Fixture cases provide the same assembled evidence to
assertion and rubric judges. The scoring rules, rubric dimensions, and handoff
exclusions remain unchanged. `route` deliberately uses the request text alone
to test skill discovery, without attaching evidence or grading its substance.

Absolute paths, parent traversal, malformed `files` values, symlink escapes,
missing/non-text inputs, and ambiguous local/repository matches fail validation.
Run inputs are assembled before model calls. Fixture content changes invalidate
fixture-case resume reuse and calibration cache keys. Existing no-fixture
calibration cache names and assertion payloads remain compatible.

Cases are independent. Re-audit cases must supply previous finding IDs as well
as revised assets; a reference to a sample from a previous test is insufficient.
Keep expected calculations and verdicts in assertions, not in input fixtures.

The default model for runs, routing, and the judge is `claude-sonnet-5`. Override with `--model` and `--judge`.

Pass `--budget 15` to stop before API spend passes $15. `run` stops early if its projected cost is over budget, and keeps the outputs it finished. `run --resume STAMP` continues a stopped run and counts what it already spent.

System prompts (skill text, the skill catalog, rubrics, and graded examples) are sent with prompt caching, so repeated calls read them at a tenth of the input price. `agree` skips caching because each of its calls has a different system prompt.

The rubric judge in `run` and `agree` sees the hand-graded calibration outputs, with scores and notes, as examples. In `agree` the output being judged is always left out.

## Measured results

The latest numbers are in [RESULTS.md](RESULTS.md): rubric lift per dimension, em dash counts, and judge agreement with hand grades. They are early results.

## How to read results

- **Lift** is the number that matters. A skill that scores 80% with no lift is not adding value.
- **Non-discriminating assertions** pass or fail in every config. Rewrite or delete them.
- **Routing confusions** list which skill pairs steal each other's prompts. Fix those descriptions first.
- **Hand-off evals** (`handoff_to` in `evals.json`) check that a request goes to another skill. `route` counts them right when the router picks that skill. They are left out of rubric lift, and rubric-only runs skip them.

## Calibration

`calibrate` runs 3 prompts from each of 5 skills (`positioning-strategy`, `messaging-framework`, `copywriting`, `page-cro`, `competitor-alternatives`), once with the skill and once without. That makes 30 outputs.

| File | Contents |
|---|---|
| `calibration/outputs/A-01.md` to `A-30.md` | Shuffled blind outputs: prompt and response only |
| `calibration/grades.csv` | One row per output. Fill in `grounded`, `decisive`, `usable`, `sharp` (0, 1, or 2) and `notes` |
| `calibration/split.csv` | Which outputs are anchor pool, holdout, or unused. `calibrate` writes A-01 to A-10 as anchor, A-11 to A-20 as holdout, and the rest as unused; edit it to change the split |
| `results/calibration-key.csv` | Unblinding key: skill, eval id, config, model, stop reason, seed. Gitignored and kept away from the outputs so it stays out of sight while you grade |

Pick rubric anchors only from the anchor pool. Once grades are in, `report` unblinds them and adds mean rubric scores per config. It works without a `run`, counts only rows with all four scores, skips ungraded rows, and stops if a score is anything other than 0, 1, or 2. The command refuses to overwrite a `grades.csv` that has scores in it. Real runs cache each output in `results/cache/`, so an interrupted run resumes without paying twice.

## Output

Everything lands in `evals/results/` (gitignore it), except `report`, which writes the tracked summary to `evals/RESULTS.md`. Each run keeps raw outputs as markdown so you can read what the agent actually wrote, not just the score.
