# Segment selection and sizing

Skills that choose an audience, ICP, beachhead, or wedge load this file and follow it. Label every score, size, and claim with Sourced, Assumed, or Gap, as defined in `evidence-gaps.md`.

Proof strength is one input to the choice. It is never the filter that decides which segments get considered.

## 1. List every plausible segment

- **Start from the problem, not from where proof exists.** Ask who has the pain, then split that group by industry, company size, business model, geography, or buyer role.
- **Keep segments with zero published proof on the list.** No logos, case studies, or stats lowers the proof score. It never removes the segment.
- **List before you choose.** Build the full list first, then score it.

Example: a fraud tool's pain is card fraud losses, which hit every online merchant. The list covers AI companies, marketplaces, SaaS, e-commerce, travel, and digital goods. It includes the segments no vendor has published about.

## 2. Size the full market before choosing

Size every segment on the list before you score or choose. The reach or revenue score in step 3 comes from these sizes.

- **Size the full addressable market first.** Cover every segment from step 1, then total it.
- **Never invent market sizes.** An Assumed size shows its method, for example "[count of accounts] x [average price]". A size derived from a sourced total is not invented (see step 5).
- **Build the full market as a range from any sourced total.** Label the total Sourced and each ratio or split Assumed, with its basis. The full market is never "Gap: not sized" when a sourced total exists.
- **Keep unsized segments in the plan.** Label them "Gap: not sized" and say how to size them, for example "pull merchant counts by vertical from internal data".
- **Size the market the pain defines, not the market the proof covers.** If the loss pool is cross-industry, the full market is cross-industry.
- **Reconcile any headline figure with the sizing.** If the brief or research gives a loss pool or market figure, show the steps from it to the full market.
- **State every exclusion.** If sizing leaves a segment out, name it and give the reason in one line.

### Plausibility rules for derived numbers

- **Show each derived count as a share of its anchor.** Example: "15,000 AI accounts, 5% of the 300,000 Billing anchor." When several segments split one anchor, state their combined share too.
- **Justify any share above 50% in one line.** A high share is often right, but it must say why.
- **Build revenue per account from a formula.** Use price plus usage: "[list price x 12] + [units per month x unit price x 12]". Label each input. Never pick a round number.

```
| Segment | Accounts (share of anchor) | Revenue per account (formula) | Size | Label |
|---|---|---|---|---|
| [segment] | [count] ([x]% of [anchor]) | [price x 12] + [units x unit price x 12] = [$] | [size, or "not sized"] | Sourced / Assumed / Gap |
| **Full addressable market** | [total] ([x]% of [anchor]) | | [low to high range] | Derived from [sourced total] |

Excluded from sizing: [segment], because [reason]. (Or: "None.")
```

## 3. Score each segment and calculate attractiveness

When comparing segments, build one side-by-side scorecard. Score each criterion
from 1 to 5, keep every criterion visible, and label each score `Sourced`,
`Assumed`, or `Gap`. Use the market sizing from section 2 for market opportunity.

| Criterion | What a high score means | Default weight |
|---|---|---:|
| **Market opportunity** | Large, serviceable opportunity against the company's stated goals | 12% |
| **Pain intensity** | Frequent, costly, urgent problem | 12% |
| **JTBD fit** | The product directly addresses an important job-to-be-done | 10% |
| **Underserved** | Current alternatives leave meaningful needs unmet | 7% |
| **Differentiation / ability to win** | Clear advantage buyers value and competitors cannot easily match | 10% |
| **Reachability** | The company can identify and reach buyers through available channels | 8% |
| **Acquisition ease** | Buyers can be acquired with reasonable cost, time, and sales friction | 7% |
| **Customer effort required** | Low implementation, onboarding, support, or behavior-change burden | 5% |
| **Existing product engagement** | Strong usage or adoption in this segment, when a cohort exists | 6% |
| **Stickiness / retention** | The solution becomes durable in the customer's workflow | 6% |
| **Expansion / upgrade potential** | Clear path to additional teams, use cases, or higher plans | 6% |
| **LTV potential** | Attractive lifetime value based on labeled retention, expansion, and revenue inputs | 6% |
| **Proof strength** | Existing customers, outcomes, data, and quotes support success in this segment | 5% |
| **Total** | | **100%** |

Use the same default weights for every candidate in a comparison. They favor the
size of the opportunity, intensity of the need, fit, and ability to win, while
also accounting for go-to-market practicality and durable economics. Proof gets
a deliberately smaller weight so a lack of historical proof does not screen out
a promising segment. The weights are an `Assumed` starting model, not a universal
truth.

### Consistent scale

Use the same scale for every criterion and segment:

| Score | General meaning |
|---:|---|
| 1 | Very weak attractiveness on this criterion |
| 2 | Below average or materially constrained |
| 3 | Adequate, mixed, or near the decision threshold |
| 4 | Strong attractiveness with a manageable weakness |
| 5 | Exceptional attractiveness relative to the alternatives |

For **customer effort required**, score in the favorable direction: 5 means low
effort for the customer and company; 1 means substantial implementation,
adoption, or support burden. For all other criteria, higher means more attractive.
State the specific basis for each score. For market opportunity, anchor the score
to the sized TAM/SAM/SOM and the company's stated threshold. For acquisition ease,
use cost or sales-cycle evidence where available. Do not substitute a guessed
number for absent data.

### Weighted Segment Attractiveness Score

Calculate a weighted average on the same 1-to-5 scale:

```text
Segment Attractiveness Score =
  sum(score × criterion weight for scoreable criteria)
  ÷ sum(weights for scoreable criteria)
```

With all criteria scored, the denominator is 100. Show the weights and result
explicitly. Label the composite `Derived`; retain the evidence label and source
or assumption beside every individual score. If a criterion cannot reasonably be
scored, write `Gap: [what evidence is missing]`, assign no number, and omit only
that criterion's weight from the denominator. Show the **weight coverage** as the
sum of scoreable weights over 100. Mark the composite provisional whenever
coverage is below 100%. If no criteria can be scored, mark the composite
unavailable. Never treat a Gap as zero or silently fill it with an estimate.

If company strategy makes another factor more important, the decision owner may
change the weights. State who set them and why, list the revised weight for every
criterion, keep the total at 100%, and apply the same weights to all candidates.
Do not change weights after seeing scores just to make a preferred segment win.
Avoid double-counting overlapping criteria; if one is folded into another, say
which criterion and keep the original dimension visible as a separate diagnostic
only if it can be scored without duplication.

### Evidence confidence

Report `Evidence confidence: High / Medium / Low` separately from attractiveness.
It reflects weighted evidence support, not market attractiveness and not a
statistical probability. Calculate the support coverage using each criterion's
weight:

```text
Evidence support =
  (100% × weights labeled Sourced
   + 50% × weights labeled Assumed
   + 0% × weights labeled Gap) ÷ total criterion weights
```

Use `High` for support coverage of 80% or more, `Medium` for 50% to less than
80%, and `Low` below 50%. Also consider source recency, directness, independence,
and contradictions: lower the rating and explain why if these make the evidence
less reliable. Show the support percentage and the main reason beside the rating.
These cutoffs are a consistent decision aid, not statistical confidence bounds.

A high-scoring segment with low confidence is a validation priority, not an
automatic lead or rejection. A lower-scoring segment with high confidence remains
visible and may be the safer near-term choice. Never let the composite hide a
weak dimension, an evidence gap, a blocking constraint, or the decision owner's
strategic priority.

```markdown
| Criterion | Weight | Segment A | Segment B | Segment C |
|---|---:|---|---|---|
| Market opportunity | 12% | [1-5, label, source/basis] | | |
| Pain intensity | 12% | [1-5, label, source/basis] | | |
| JTBD fit | 10% | [1-5, label, source/basis] | | |
| Underserved | 7% | [1-5, label, source/basis] | | |
| Differentiation / ability to win | 10% | [1-5, label, source/basis] | | |
| Reachability | 8% | [1-5, label, source/basis] | | |
| Acquisition ease | 7% | [1-5, label, source/basis] | | |
| Customer effort required | 5% | [1-5, label, source/basis] | | |
| Existing product engagement | 6% | [1-5 or Gap, label, source/basis] | | |
| Stickiness / retention | 6% | [1-5, label, source/basis] | | |
| Expansion / upgrade potential | 6% | [1-5, label, source/basis] | | |
| LTV potential | 6% | [1-5, label, formula/source] | | |
| Proof strength | 5% | [1-5, label, source/basis] | | |
| **Segment Attractiveness Score** | **100%** | [formula] / 5, Derived; weight coverage: [%] | | |
| **Evidence confidence** | | [High / Medium / Low; support coverage and basis] | | |
```

Keep the 13 criteria as their own rows. If the task-specific output needs the
former compact three-axis view, include it as a summary, not a replacement for
this scorecard.

## 4. Pick a lead segment

Name one lead segment and explain the 2 to 3 decision factors that drove the choice.
Then state its biggest weakness and the most important evidence gap separately.

- **Name the axes that drove the choice.**
- **Say so when proof strength decided it,** and name what the larger or higher-pain segment needs before it can lead.
- **Put anything longer in the sequence.** The sequencing line carries the detail.

```
Lead: [segment]. [2 to 3 decision factors, naming the criteria and evidence labels.]
Biggest weakness: [one line.]
Most important evidence gap: [one line and how to close it.]
```

## 5. Sequence the segments that follow and size the wedge

Write one sequencing line for each remaining segment: its order, the trigger that starts it, and the validation task that unlocks it.

```
2. [Segment]: starts when [trigger: a metric, a proof milestone, or a product capability]. Unlock: [validation task].
3. [Segment]: ...
Parked: [segment], because [reason]. Revisit when [condition].
```

- **Make every trigger observable.** "3 beta accounts show a lower chargeback rate" works. "When ready" does not.
- **Give parked segments a reason and a revisit condition.** No segment disappears between the list and the plan.

Then size the **year-one wedge**: the lead segment plus any segment sequenced into year one, shown as a share of the full market.

```
| Segment | Size | In year-one wedge? |
|---|---|---|
| [segment] | [size from step 2] | Yes / No, starts when [trigger] |
| **Year-one wedge** | [total] ([x]% of full) | |
```

- **Derived is not invented.** When a sourced total exists, such as a loss pool or market figure, always build the full market from it as a range. Label the total Sourced and each ratio or split Assumed, with its basis.
- **Invented means a number with no sourced anchor and no stated basis.** That stays banned.
- **"Gap: not sized" is allowed per segment.** It is never allowed for the full market when a sourced total exists.
- **Make the year-one wedge a subset of segments.** Give a one-line reason for each segment left out of it.

## 6. Consistency check (GTM final review)

GTM skills run this check in their final review. The segments must match across the market sizing, the positioning statement, the Phase 2 plan, the KPIs, and the copy. Copy means the hero line, the subhead, and each segment's first line.

- **Account for every segment named in the strategy, positioning, or copy in the sizing.** If it is missing, it must be listed as an exclusion with a reason.
- **Give the lead segment at least one KPI.** Give each sequenced segment the KPI that measures its trigger.
- **Match scope words to sizing and KPIs.** "Scale to all customers", "every industry", or "cross-industry" in the strategy needs sizing and KPIs that cover that scope.
- **Match copy scope to the segments it is meant to cover.** A hero or subhead meant for several segments must not use one segment's words. Example: "free credits" or "compute" in a hero meant for AI, SaaS, and consumer subscriptions.
- **Fix every mismatch before delivering, or state why it is intentional.** The table below goes in the deliverable. It records the match. It is not a pass or fail grade.

```
## Consistency check
| Segment | In sizing | In positioning | In Phase 2 plan | In KPIs | In copy | Mismatch |
|---|---|---|---|---|---|---|
| [segment] | Yes / No | Yes / No | Yes / No | Yes / No | Hero / subhead / first line / No | [none, or what does not match and the fix] |

| Copy line | Meant to cover | Segment-specific words | Fix |
|---|---|---|---|
| Hero: "[line]" | [segments] | [words that fit only one segment, or "none"] | [rewrite, or scope the line to one segment] |
```

Example mismatch: the strategy says "scale to all merchants" while every KPI tracks AI companies. Fix: add KPIs for the sequenced segments, or narrow the strategy line to AI companies and name the others as later phases.

Example copy mismatch: the hero "Free credits for real users only" is meant for AI, SaaS, and consumer subscriptions. "Free credits" fits AI only. Fix: move it to the AI first line, and give the hero words every covered segment uses, such as "free trials and signups."

## 7. Trace every figure before finishing

Before delivering, trace every number in the deliverable to one of three bases.

| Basis | What it needs |
|---|---|
| **Sourced** | A citation |
| **Derived** | A formula whose inputs are all labeled |
| **Assumed** | A stated basis (an anchor, benchmark, or analogy) and what would confirm it |

- **Treat a figure with none of these as manufactured.** Remove it, or relabel it Gap and say how to get it.
- **Keep this trace internal.** Fix what fails. Do not add a pass or fail report to the deliverable.
