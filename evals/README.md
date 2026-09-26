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
export ANTHROPIC_API_KEY=sk-...
python evals/harness.py lint
python evals/harness.py route --trials 1
python evals/harness.py run --skills page-cro,copywriting --trials 3
python evals/harness.py report
python evals/harness.py calibrate
```

Add `--mock` to any command to test the pipeline without a key. Mock results go to `evals/results/mock/` so they never mix with real runs.

The default model for runs, routing, and the judge is `claude-sonnet-5`. Override with `--model` and `--judge`.

## How to read results

- **Lift** is the number that matters. A skill that scores 80% with no lift is not adding value.
- **Non-discriminating assertions** pass or fail in every config. Rewrite or delete them.
- **Routing confusions** list which skill pairs steal each other's prompts. Fix those descriptions first.

## Calibration

`calibrate` runs 3 prompts from each of 5 skills (`positioning-strategy`, `messaging-framework`, `copywriting`, `page-cro`, `competitor-alternatives`), once with the skill and once without. That makes 30 outputs.

| File | Contents |
|---|---|
| `calibration/outputs/A-01.md` to `A-30.md` | Shuffled blind outputs: prompt and response only |
| `calibration/grades.csv` | One row per output. Fill in `grounded`, `decisive`, `usable`, `sharp` (0, 1, or 2) and `notes` |
| `calibration/split.csv` | Which outputs are anchor pool, holdout, or unused. `calibrate` writes A-01 to A-20 as anchor and A-21 to A-30 as holdout; edit it to change the split |
| `results/calibration-key.csv` | Unblinding key: skill, eval id, config, model, stop reason, seed. Gitignored and kept away from the outputs so it stays out of sight while you grade |

Pick rubric anchors only from the anchor pool. Once grades are in, `report` unblinds them and adds mean rubric scores per config. It works without a `run`, counts only rows with all four scores, skips ungraded rows, and stops if a score is anything other than 0, 1, or 2. The command refuses to overwrite a `grades.csv` that has scores in it. Real runs cache each output in `results/cache/`, so an interrupted run resumes without paying twice.

## Output

Everything lands in `evals/results/` (gitignore it). Each run keeps raw outputs as markdown so you can read what the agent actually wrote, not just the score.
