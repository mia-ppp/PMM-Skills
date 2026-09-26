# Measured results

Early result: small samples, one judge model, and rubrics still being calibrated. Treat as directional.

## Correction (2026-09-26)

Each skill has hand-off evals that check a request goes to a different skill. Earlier results scored them as routing misses when the router picked that other skill, and counted them in rubric lift, where the judge marks a hand-off down for not doing the task. Routing accuracy was reported as 81.5%. Hand-off evals are now scored against the skill they hand off to and left out of rubric lift. Numbers below use the corrected scoring, including for earlier runs.

## Changed skills: lift before (20260926-150948) and after (20260926-160737)

Lift is the with-skill mean minus the baseline mean, on the 0-2 scale. Before used 3 trials, after used 1.

| Skill | Grounded | Decisive | Usable | Sharp |
|---|---|---|---|---|
| buyer-personas | n/a → +1.00 | n/a → +0.20 | n/a → +0.00 | n/a → +0.60 |
| competitor-alternatives | +0.53 → +1.20 | -0.47 → -0.20 | -0.60 → -0.40 | -0.07 → +0.00 |
| messaging-framework | +1.33 → +1.25 | +0.67 → +0.75 | +0.50 → +0.75 | +0.58 → +0.75 |
| positioning-strategy | +1.20 → +1.20 | +0.93 → +1.40 | +0.40 → +0.60 | +0.40 → +0.40 |

## Run 20260926-160737

38 outputs: 4 skills (buyer-personas, competitor-alternatives, messaging-framework, positioning-strategy), 19 prompts, with skill and baseline, 1 trial. Rubric judge: claude-sonnet-5, shown 10 hand-graded examples.

## Rubric scores (0-2), with skill vs baseline

| Dimension | With skill | Baseline | Lift |
|---|---|---|---|
| Grounded | 1.68 (n=19) | 0.53 (n=19) | +1.16 |
| Decisive | 1.63 (n=19) | 1.11 (n=19) | +0.53 |
| Usable | 1.21 (n=19) | 1.00 (n=19) | +0.21 |
| Sharp | 0.95 (n=19) | 0.53 (n=19) | +0.42 |

| Skill | With skill | Baseline | Lift |
|---|---|---|---|
| buyer-personas | 1.30 | 0.85 | +0.45 |
| competitor-alternatives | 1.30 | 1.15 | +0.15 |
| messaging-framework | 1.44 | 0.56 | +0.88 |
| positioning-strategy | 1.45 | 0.55 | +0.90 |


## Em dashes (hard check, not part of the rubric)

| Config | Outputs | Total | Mean per output | Outputs with any |
|---|---|---|---|---|
| with_skill | 19 | 13 | 0.7 | 7 |
| baseline | 19 | 167 | 8.8 | 19 |

## Run 20260926-150948

174 outputs: 5 skills (competitor-alternatives, copywriting, messaging-framework, page-cro, positioning-strategy), 29 prompts, with skill and baseline, 3 trials. Rubric judge: claude-sonnet-5, shown 10 hand-graded examples. 18 hand-off outputs are left out of the rubric tables.

## Rubric scores (0-2), with skill vs baseline

| Dimension | With skill | Baseline | Lift |
|---|---|---|---|
| Grounded | 1.59 (n=78) | 0.79 (n=78) | +0.79 |
| Decisive | 1.17 (n=78) | 1.03 (n=78) | +0.14 |
| Usable | 1.03 (n=78) | 0.99 (n=78) | +0.04 |
| Sharp | 0.72 (n=78) | 0.49 (n=78) | +0.23 |

| Skill | With skill | Baseline | Lift |
|---|---|---|---|
| competitor-alternatives | 0.90 | 1.05 | -0.15 |
| copywriting | 1.14 | 0.96 | +0.18 |
| messaging-framework | 1.50 | 0.73 | +0.77 |
| page-cro | 0.78 | 0.65 | +0.12 |
| positioning-strategy | 1.45 | 0.72 | +0.73 |


## Em dashes (hard check, not part of the rubric)

| Config | Outputs | Total | Mean per output | Outputs with any |
|---|---|---|---|---|
| with_skill | 87 | 828 | 9.5 | 83 |
| baseline | 87 | 642 | 7.4 | 86 |


## Routing

Routing accuracy: 94.6% over 222 prompts, with every skill competing. Hand-off evals count as right when the router picks the skill they hand off to (scored when run: 81.5%). Last route run: 2026-09-26, with the skill descriptions of that date.

| Expected | Picked | Count |
|---|---|---|
| copywriting | ab-test-setup | 1 |
| copywriting | copy-editing | 1 |
| customer-research | messaging-framework | 1 |
| customer-research | churn-prevention | 1 |
| launch-strategy | marketing-ideas | 1 |
| marketing-ideas | content-strategy | 1 |
| messaging-framework | positioning-strategy | 1 |
| pricing-strategy | marketing-psychology | 1 |
| product-marketing-context | copywriting | 1 |
| programmatic-seo | competitor-alternatives | 1 |

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
