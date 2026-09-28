# Calibration set

These are the 30 blind outputs I grade by hand to keep the rubric judge honest. If the judge drifts away from my grades, the rubric numbers in [RESULTS.md](../RESULTS.md) stop meaning much.

`python evals/harness.py calibrate` writes this folder. The [evals README](../README.md) covers the commands, and this file covers what's in here and how to grade it.

## What's here

| File | What it holds |
|---|---|
| `outputs/A-01.md` to `A-30.md` | One prompt and one response each, shuffled, with no skill name or config |
| `grades.csv` | My scores for `grounded`, `decisive`, `usable`, `sharp` (0, 1, or 2), plus a one-line `notes` |
| `split.csv` | Which outputs are anchor pool, holdout, or unused |

The unblinding key is kept out of this folder on purpose. It sits in `evals/results/calibration-key.csv`, which is gitignored, so I can't tell which skill wrote what while I'm grading.

## The split

| Outputs | Split | Status |
|---|---|---|
| A-01 to A-10 | Anchor pool | Graded |
| A-11 to A-20 | Holdout | Not graded yet |
| A-21 to A-30 | Unused | Spare |

Rubric anchors only ever come from the anchor pool. The holdout never becomes an anchor, because it's the only way to tell whether the judge learned the rubric or just memorized my examples.

## Grading

Read each output cold and score the four dimensions against [the rubrics](../rubrics/README.md). When I'm torn between two tiers I take the lower one, and every score gets a reason in `notes`.

`report` only counts rows with all four scores filled in. Anything other than 0, 1, or 2 stops it.

`calibrate` won't overwrite a `grades.csv` that already has scores, so regrading happens by hand in the file. After grading, `python evals/harness.py agree` shows how often the judge matches me.
