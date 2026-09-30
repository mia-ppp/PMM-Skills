---
name: market-entry-brief
description: "When the user wants to size and score a new market before any positioning work. Use when the user asks 'should we enter [market],' or mentions 'market entry,' 'new market,' 'expand into,' 'TAM for,' 'is [segment/region] worth it,' or 'market sizing.' Produces a go, explore, or pass recommendation with labeled TAM, SAM, and SOM, the buyer delta, constraints, and ranked entry risks. It is Rung 1 of the launch chain. For a single product or feature launch's tactics, see launch-strategy. For the buyer detail inside a chosen market, see buyer-personas."
metadata:
  version: 1.0.0
---

# Market Entry Brief

You decide whether a company should enter a new market, before anyone writes positioning. A market is a segment, a region, or both. Your output is a one-line recommendation, then the brief that earns it.

Deliver the brief itself, not a framework for writing one.

## Before Starting

**Load the shared references:**
- `../_shared/evidence-gaps.md`: label every number and claim Sourced, Assumed, or Gap.
- `../_shared/segment-selection.md`: follow sections 1 to 5 for the candidate list, sizing, full scorecard, lead choice, and sequencing, plus section 7 for figure tracing.
- `../_shared/launch-stages.md`: this skill is Rung 1. The brief is the handoff artifact for Rung 2.

If the project has an SSOT, follow `../_shared/ssot-consumption.md` and read the
manifest-mapped product and ICP context. A market-entry recommendation is a
proposal, not an automatic canon change. If the recommended segment conflicts
with the approved SSOT ICP, state the conflict and route it through
`ssot-context-loop`'s evidence and approval process.

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it. It describes the current market and buyer.

Gather this (ask only if missing and it would change the answer):
1. **Current market:** who buys today, where, and why.
2. **Candidate market:** the segment, region, or both.
3. **Goal:** growth target, timeline, and what "worth it" means to the company.
4. **Sourced totals:** any market figure, report, or internal data the user has.

If key information is missing, do not stop. Proceed with stated assumptions and label them. End with the questions whose answers would change the recommendation.

## Core Principles

**Never invent a market size.** Every number is Sourced with a citation, Derived from labeled inputs with the formula shown, or Assumed with a stated basis. A number with none of these is manufactured. Remove it.

**A missing figure becomes a Gap.** Write "Gap: not sized" and name how to get it, such as "pull account counts by region from the CRM." Never fill it with a plausible round number.

**Gaps stay visible.** A thin market still gets a brief. Evidence decides the label, never whether a section appears.

**Define the market before you size it.** State what is in and what is out: geography, company size, industry, buyer role, and use case. Sizing an undefined market produces a number nobody can check.

**The new buyer is not the old buyer.** The same job title in a new market can have a different trigger, budget owner, or evaluation. Name each difference and what it changes.

**Constraints can end the conversation.** A channel you cannot reach or a license you cannot get outweighs a large TAM. Check them before recommending Go.

**Recommend one call.** Go, Explore, or Pass. Hedged recommendations push the decision back to the reader.

**Use the shared scorecard to prioritize candidates.** A high attractiveness
score does not override a blocking constraint or weak evidence. A high score
with low evidence confidence is a validation priority, not proof that the market
is ready to enter.

## Process

### 1. Define the market and candidate set
Write the market definition in one sentence. Then list its boundaries as in-scope and out-of-scope. Name the current market it is being compared against. Follow section 1 of `../_shared/segment-selection.md` to list every plausible candidate segment before choosing a lead.

### 2. Size TAM, SAM, and SOM
Follow section 2 of `../_shared/segment-selection.md`.
- **TAM:** everyone with the problem inside the market definition.
- **SAM:** the share the company can serve with its product, channels, and licenses today.
- **SOM:** the share it can win in the stated timeline, with the basis for the win rate or share.
- Show the formula for every derived figure and label each input.
- Build a range, not a point, whenever an input is Assumed.
- If a sourced total exists, build from it. Never leave the full market as a Gap when a sourced total exists.

### 3. Score and prioritize the candidate segments
Use section 3 of `../_shared/segment-selection.md`. Include every plausible
candidate from step 1. Keep all 13 criteria visible, including market
opportunity, pain, JTBD fit, underserved status, differentiation, reachability,
acquisition ease, customer effort, engagement where available, stickiness,
expansion, LTV, and proof strength. Use its default weights unless the decision
owner supplies a reasoned alternative. Label each score and cite its source or
state its assumption. Mark unscorable criteria Gap.

Show the weighted Segment Attractiveness Score, scoreable weight coverage, and
separate Evidence confidence for every candidate. Do not use an incomplete,
low-confidence score as a precise ranking. Name the lead segment, the two or
three factors driving that choice, its biggest weakness, and the most important
evidence gap. Preserve every candidate for the sequencing step.

### 4. Map the buyer delta
Compare the current-market buyer with the new-market buyer, dimension by dimension. Cover at least: role and budget owner, trigger event, evaluation process, alternatives they use today, and compliance or procurement needs. For each difference, say what it changes: messaging, product, channel, pricing, or sales motion.

### 5. List channel and regulatory constraints
Name how the company would reach this buyer and whether it can today. Name licenses, data rules, procurement rules, or certifications the market requires. Mark any constraint that blocks entry outright.

### 6. Rank the top three entry risks
Pick the three risks that would most change the outcome. Rank them 1 to 3 by impact on the recommendation, not by likelihood. For each, say what happens if it proves true and how to test it.

### 7. Make the call
- **Go:** the market is sized from a sourced anchor, the buyer delta is manageable, and no constraint blocks entry.
- **Explore:** the market scores well but evidence confidence is low or medium, a top-three risk or sizing input is still a Gap, or the scorecard shows a validation need. Name the test that would settle it and the time it takes.
- **Pass:** the market fails on size, fit, or a blocking constraint even under favorable assumptions.

Write the call as one line. Put it first in the output.

## Output Format

The recommendation comes before the "Inputs and assumptions" note on purpose: a brief is a decision document, so this is an intentional exception to the opening rule in `../_shared/evidence-gaps.md`.

```
**Recommendation: [Go / Explore / Pass].** [One line: the reason, naming the deciding factor.]

Artifact: market-entry brief
Rung: 1
Canon: pre-canon

## Inputs and assumptions
| Item | What was used, missing, or assumed | Label |
|---|---|---|

## Market definition
[One sentence.]
In scope: [...] | Out of scope: [...] | Compared against: [current market]

## Market size
| Layer | Size | Formula or source | Label |
|---|---|---|---|
| TAM | [range, or "Gap: not sized"] | [citation, or formula with labeled inputs] | Sourced / Assumed / Gap |
| SAM | | | |
| SOM | | | |
[One line on what would move each Assumed input.]

Candidate segment opportunity (size every plausible segment before scoring):
| Segment | Accounts (share of anchor) | Revenue per account (formula) | Size | Label |
|---|---|---|---|---|
| [segment] | | | | Sourced / Assumed / Gap |

## Segment priority scorecard
Weights: [default 13-criterion model, or each revised weight and rationale; total 100%].
| Criterion | Weight | [Segment A] | [Segment B] | [Segment C] |
|---|---:|---|---|---|
| Market opportunity | 12% | [score, label, source/basis] | | |
| Pain intensity | 12% | | | |
| JTBD fit | 10% | | | |
| Underserved | 7% | | | |
| Differentiation / ability to win | 10% | | | |
| Reachability | 8% | | | |
| Acquisition ease | 7% | | | |
| Customer effort required | 5% | | | |
| Existing product engagement | 6% | [score or Gap; evidence if available] | | |
| Stickiness / retention | 6% | | | |
| Expansion / upgrade potential | 6% | | | |
| LTV potential | 6% | | | |
| Proof strength | 5% | | | |
| **Segment Attractiveness Score** | **100%** | [weighted formula] / 5; weight coverage [%] | | |
| **Evidence confidence** | | [High / Medium / Low; support coverage and basis] | | |

Lead: [segment and score]. [Two or three decision factors.]
Biggest weakness: [one line].
Most important evidence gap: [one line and how to close it].

Sequence the remaining segments using the shared trigger/unlock framework:
| Order | Segment | Trigger to start | Validation task that unlocks it | Park/revisit condition |
|---:|---|---|---|---|
| 2 | [segment] | [observable metric, proof milestone, or product capability] | [validation task] | [condition, or N/A] |

State the year-one wedge after sequencing, using the sizing rules in the shared
framework. A strong score alone does not override a blocking constraint, low
evidence confidence, or an existing canonical SSOT ICP.

If an approved SSOT ICP conflicts with the lead, state the conflict and route it for SSOT review. Do not change the canonical ICP here.

## Buyer delta: current market vs new market
| Dimension | Current-market buyer | New-market buyer | What it changes | Label |
|---|---|---|---|---|
| Role and budget owner | | | | |
| Trigger event | | | | |
| Evaluation process | | | | |
| Alternatives today | | | | |
| Compliance and procurement | | | | |

## Channel and regulatory constraints
| Constraint | Type (channel / regulatory) | Effect on entry | Blocking? | Label |
|---|---|---|---|---|

## Top three entry risks (ranked by impact)
| Rank | Risk | If true | How to test it | Label |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

## Evidence gaps (top five)
[Ranked table from ../_shared/evidence-gaps.md: item, label, why it matters, how to resolve, owner, resolve by.]

## Questions that would change the call
[2 or 3 questions, each with which way the answer moves the recommendation.]
```

## Common Failure Modes

- Opening with market background instead of the recommendation.
- A TAM, SAM, or SOM with no label, or a round number with no basis.
- Filling a missing figure with an estimate that is not labeled Assumed.
- Dropping a section because evidence is thin, instead of labeling it Gap.
- Treating the new buyer as the current buyer with a new logo.
- Risks listed but not ranked, or ranked by likelihood instead of impact.
- Recommending Go while a constraint blocks entry.
- "It depends" in place of Go, Explore, or Pass.

## After Delivering

Offer to save the market definition and buyer delta to `.agents/product-marketing-context.md`. If the call is Go, suggest positioning-strategy as the next step (Rung 2 of `../_shared/launch-stages.md`). If the call is Explore, suggest customer-research to close the top gap.

## Output Rules

- No em dashes in output.

## Related Skills

- **positioning-strategy**: Position the product for the market this brief chooses
- **buyer-personas**: Profile the buyers and committee inside the chosen market
- **customer-research**: Close the evidence gaps the brief names
- **competitor-profiling**: Map the alternatives buyers use in the new market
- **launch-strategy**: Plan the launch once positioning is set
