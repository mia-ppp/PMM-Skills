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

## 3. Score each segment on three separate axes

Score each axis from 1 to 5 and label every score. Base reach or revenue on the step 2 sizes.

| Axis | Question | 1 | 5 |
|---|---|---|---|
| **Pain intensity** | How costly and frequent is the problem for them? | Rare or cheap | Frequent and expensive |
| **Reach or revenue** | How much revenue can this segment bring, or how many buyers can we reach? | Small or hard to reach | Large and reachable |
| **Proof strength** | How much evidence do we have today that they buy and succeed? | None | Customers, data, and quotes |

- **Keep the three axes in separate columns.** Never collapse them into one score that hides a low proof score.
- **Read a high-pain, high-reach, low-proof segment as a validation priority.** It is not a reject.
- **Add skill-specific criteria as extra columns if needed.** Examples: JTBD fit, reachability, expansion. The three axes always stay.

```
| Segment | Pain intensity | Reach or revenue | Proof strength | Notes and labels |
|---|---|---|---|---|
| [segment] | [1-5] (Sourced / Assumed / Gap) | [1-5] (...) | [1-5] (...) | [source, assumption, or missing proof] |
```

## 4. Pick a lead segment

Name one lead segment and say why in 2 to 3 sentences in total. The limit covers everything below.

- **Name the axes that drove the choice.**
- **Say so when proof strength decided it,** and name what the larger or higher-pain segment needs before it can lead.
- **Put anything longer in the sequence.** The sequencing line carries the detail.

```
Lead: [segment]. [Why, naming the axes.] [If proof decided it: which segment lost on proof, and what it needs to lead.]
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
