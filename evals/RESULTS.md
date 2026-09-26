# Measured results

Early result: small samples, one judge model, and rubrics still being calibrated. Treat as directional.

## Run 20260926-150948

174 outputs: 5 skills (competitor-alternatives, copywriting, messaging-framework, page-cro, positioning-strategy), 29 prompts, with skill and baseline, 3 trials. Rubric judge: claude-sonnet-5, shown 10 hand-graded examples.

## Rubric scores (0-2), with skill vs baseline

| Dimension | With skill | Baseline | Lift |
|---|---|---|---|
| Grounded | 1.47 (n=87) | 0.79 (n=87) | +0.68 |
| Decisive | 1.05 (n=87) | 0.98 (n=87) | +0.07 |
| Usable | 0.92 (n=87) | 0.97 (n=87) | -0.05 |
| Sharp | 0.64 (n=87) | 0.44 (n=87) | +0.21 |

| Skill | With skill | Baseline | Lift |
|---|---|---|---|
| competitor-alternatives | 0.79 | 0.94 | -0.15 |
| copywriting | 0.98 | 0.89 | +0.08 |
| messaging-framework | 1.50 | 0.73 | +0.77 |
| page-cro | 0.68 | 0.65 | +0.02 |
| positioning-strategy | 1.45 | 0.72 | +0.73 |


## Em dashes (hard check, not part of the rubric)

| Config | Outputs | Total | Mean per output | Outputs with any |
|---|---|---|---|---|
| with_skill | 87 | 828 | 9.5 | 83 |
| baseline | 87 | 642 | 7.4 | 86 |

## Routing

Routing accuracy: 81.5% over 222 prompts, with every skill competing.

## Calibration rubric scores (0-2), 10 graded outputs

| Config | Grounded | Decisive | Usable | Sharp |
|---|---|---|---|---|
| with_skill | 2.00 (n=4) | 1.50 (n=4) | 1.50 (n=4) | 1.00 (n=4) |
| baseline | 0.67 (n=6) | 1.33 (n=6) | 1.00 (n=6) | 0.67 (n=6) |

## Em dashes in calibration outputs (hard check, not part of the rubric)

| Config | Outputs | Total | Mean per output | Outputs with any |
|---|---|---|---|---|
| with_skill | 15 | 247 | 16.5 | 15 |
| baseline | 15 | 121 | 8.1 | 15 |

## Judge agreement: leave-one-out on 10 hand-graded outputs

Judge: claude-sonnet-5. Each output was scored with its own grades and anchors hidden.

| Dimension | Exact | Within one |
|---|---|---|
| Grounded | 40% | 100% |
| Decisive | 60% | 100% |
| Usable | 50% | 100% |
| Sharp | 60% | 90% |

Below the 70% exact-agreement bar: grounded, decisive, usable, sharp. Judge scores on these dimensions are directional only.
