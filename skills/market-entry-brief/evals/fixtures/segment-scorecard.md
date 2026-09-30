# Synthetic segment-scorecard evaluation fixture

This is fictional test data, not company SSOT content. Scores use the default
weights from `skills/_shared/segment-selection.md`, in criterion order. `S` =
Sourced, `A` = Assumed, `G` = Gap. Values are score/label.

| Criterion (weight) | Segment A: Regional clinics | Segment B: Multi-site care groups | Segment C: Independent practices |
|---|---|---|---|
| Market opportunity (12%) | 5/S | 5/A | 3/S |
| Pain intensity (12%) | 5/S | 5/A | 4/S |
| JTBD fit (10%) | 4/S | 5/A | 4/S |
| Underserved (7%) | 4/S | 5/A | 3/S |
| Differentiation / ability to win (10%) | 5/S | 5/A | 4/S |
| Reachability (8%) | 4/S | 4/A | 4/S |
| Acquisition ease (7%) | 3/S | 4/A | 3/S |
| Customer effort required (5%) | 4/S | 4/A | 3/S |
| Existing product engagement (6%) | 4/S | Gap | 4/S |
| Stickiness / retention (6%) | 4/S | 4/A | 4/S |
| Expansion / upgrade potential (6%) | 5/S | 5/A | 3/S |
| LTV potential (6%) | 4/S | 4/A | 4/S |
| Proof strength (5%) | 4/S | 4/A | 5/S |

Evidence packet for this fixture:

- `R1` is a recent account-count and serviceable-spend report, broken out by
  segment, and `R2` is the company's stated opportunity threshold. These support
  market-opportunity ratings A=5, B=5 (assumed extrapolation), C=3.
- `R3` is recent interview/survey research on problem frequency, cost, and
  urgency, and `R4` maps the priority JTBD to product workflows. These support
  pain and JTBD ratings A=5/4, B=5/5 (assumed analogy), C=4/4.
- `R5` is a competitor/alternative study and win-loss synthesis, supporting
  underserved and differentiation ratings A=4/5, B=5/5 (assumed analogy),
  C=3/4.
- `R6` is CRM account coverage, channel response, acquisition cost, and sales
  cycle data, supporting reachability and acquisition ease A=4/3, B=4/4
  (assumed analogy), C=4/3.
- `R7` is implementation/onboarding/support data, supporting effort ratings
  A=4, B=4 (assumed analogy), C=3.
- `R8` is segment cohort product usage, supporting engagement A=4 and C=4.
  There is no B cohort usage data, so B engagement is a Gap.
- `R9` is segment retention, expansion, and revenue history. It supports
  stickiness, expansion, and LTV ratings A=4/5/4, B=4/5/4 (assumed analogy),
  C=4/3/4.
- `R10` is segment customer outcome evidence and case studies, supporting proof
  ratings A=4, B=4 (assumed analogy), C=5.
- For Segment A, `R1` through `R10` are recent, direct, independent, and
  consistent. For Segment C, the corresponding segment-level records support
  every scored dimension. Segment B's ratings are assumptions based on analogous
  markets and interviews with non-customers, not product or revenue cohorts.
  Its high projected score is provisional and a validation priority.
