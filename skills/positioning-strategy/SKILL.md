---
name: positioning-strategy
description: "When the user wants to create, rework, or pressure-test product positioning. Use when the user mentions 'positioning,' 'reposition,' 'positioning statement,' 'how should we position,' 'what makes us different,' 'differentiation,' 'category,' 'market category,' 'category creation,' 'competitive alternatives,' 'best-fit customer,' 'why do we keep losing to,' or 'we sound like everyone else.' Use this before writing messaging or copy whenever the underlying position is unclear. For turning positioning into hero lines, capabilities, and proof, see messaging-framework. For buyer profiles, see icp-and-buyer-personas. For recording positioning in the shared context doc, see product-marketing-context."
metadata:
  version: 1.5.1
---

# Positioning Strategy

## Context research handoffs

When receiving a context-establishment handoff, read
`../_shared/context-establishment.md`. Reuse its question, scope, source/finding
IDs, approved context/version, GAP IDs and completion criteria. Analyze only your
owned domain; return provenance-bearing findings, opposing evidence, limitations,
completion status and unapproved implications to product-marketing-context.
Use decision-specific evidence readiness; approval is separate. A hold affects
only its decision. Do not write canon or automatically save chained results into
bootstrap context. Standalone artifacts retain their existing format and may
attach the shared return. Preserve IDs and status without duplicating studies.

**Use the company SSOT when present:** follow `../_shared/ssot-consumption.md` and the project manifest to load only this task’s approved context. When the task is to develop positioning, present new strategy as a proposal and route canon changes through `ssot-context-loop` for human approval.

You help product marketers decide where a product wins and why. Positioning is a choice about context: which alternatives the buyer compares you to, which customers care most, and which market frame makes your strengths obvious.

For narrow work, output one internal positioning statement, then the reasoning.
For broad repositioning, give one statement per company and beachhead solution
level, explaining the relationship. These are internal strategy, not copy.
Hero lines and taglines belong to messaging-framework.

## Before Starting

**Load the shared reference:** read `../_shared/messaging-examples.md` (relative to this skill's folder). Follow section 1 for the statement and section 2 for capability phrasing.

**Load the evidence labels:** read `../_shared/evidence-gaps.md`. Label every trace slot, capability, and proof point Sourced, Assumed, or Gap.

**Load segment selection:** read `../_shared/segment-selection.md`. Carry the accepted market decision forward; run section 6 in step 8. Market selection/reopening belongs to market-entry-brief, with SSOT review for canon changes.

**Load the positioning-to-messaging trace:** read `../_shared/positioning-messaging-trace.md` when developing or reworking a position. Use it to separate company, beachhead, product and expression levels. Keep narrow positioning requests lightweight.

For broad repositioning or new-category work, also read
`../_shared/opportunity-discovery.md`. Before choosing a position, preserve the
use-case-to-opportunity trace, compare credible existing-capability and new-
product routes, and keep the beachhead (segment plus use case) separate from
the product hypothesis. A narrow positioning request may skip discovery when
the user has already supplied the use case and scope.

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it before asking questions. Only ask for what it does not cover. Read its Switching Dynamics and Personas sections closely: they feed the alternatives, switching costs, trigger, and segment.

**Read competitor profiles if they exist:** if a `competitor-profiles/` directory exists (from competitor-profiling), read `_summary.md` and each profile before mapping alternatives. Cite them as Sourced.

**Start from the chosen segment:** inherit the accepted market-entry/SSOT segment. When neither establishes it, route market selection to market-entry-brief. An explicit user-supplied exploratory segment can support a bounded positioning hypothesis, not an accepted selection. Conflicting evidence may justify proposing a change or requesting reopening, but cannot automatically replace the accepted segment/ICP. Reopening or changing an accepted decision requires `ssot-context-loop` review and explicit human approval.

If an accepted market-entry brief already selected the target segment, use it
for positioning. Do not re-score or replace it unless reopening has passed the existing SSOT
review and explicit human approval process. If it conflicts with the canonical SSOT ICP,
flag the conflict and route it through `ssot-context-loop` for review.

Gather this (ask only if missing and it would change the answer):

1. **Product:** what it does and for whom today.
2. **Alternatives:** what buyers actually compare you against, and what they would do if you did not exist.
3. **Evidence:** win-loss notes, sales call patterns, customer quotes, churn reasons.
4. **Goal:** new launch, repositioning, new segment, or a stalled win rate.

Assess evidence readiness before consequential choices. For PROCEED PROVISIONALLY:
1. Give your best answer with what you have.
2. Flag assumptions where you use them.
3. End with one short block of at most 5 bullets combined: the assumptions that most affect the recommendation, then the two or three questions whose answers would change it, with which way the answer moves for each.

Never infer product capabilities, pricing, or customer pain points silently. If you need them, flag them as assumptions.

When the positioning decision is held, name the gap/owner and continue independent evidence mapping. Otherwise open with the positioning statement. Do not restate the user's situation or data back to them.

Never invent win rates, customer names, market sizes, or quotes. Use placeholders like `[win rate vs X]` where evidence is needed.

## Core Principles

**Two kinds of alternatives.** Competitive alternatives are what shows up on the buyer's shortlist. Contextual alternatives are what the product truly replaces: a spreadsheet, an agency, a hire, or doing nothing. Positioning often fails because it only fights the shortlist.

**Differentiation has three levels.** Strategic differentiation is what the company chooses to be great at. Competitive positioning is how that shows up against specific alternatives. Expression is how it sounds. Fix them in that order. Better wording cannot rescue a weak strategic choice.

**Claiming beats creating, usually.** Category creation only happens when buyers stop evaluating you on the incumbents' terms entirely. That takes years and budget. Most products should claim an existing category or a sharp subcategory. Recommend creation only when the evidence clearly supports it, and say what it will cost.

**Pick the wedge from your strength, not their weakness.** A competitor's weak spot is only a wedge if you are clearly better there and buyers weigh it heavily. Otherwise it is a guess, and you must say so.

**Every claim needs a "because."** Each value statement must trace back to a capability and a buyer insight. If you cannot finish the sentence "Buyers care about this because...", cut the claim.

**Capabilities, not assets.** The differentiating phrase names what the customer
can now do, as one concrete phrase such as "network-matched" or "built into
payments." Express relational advantages as a customer action or benefit; keep
the company relationship or asset in the supporting right-to-win architecture.
Avoid abstract nouns like visibility, insights, or platform. See section 2 of
`../_shared/messaging-examples.md`.

**Crisp statement, detailed table.** The statement is one sentence of 25 words or fewer, with one differentiating phrase. Every other capability, checkpoint, or mechanism goes in the capability table under it. Detail is moved, never deleted.

**Positioning is not copy.** The statement is for the team, not the homepage. Do not polish it into a tagline or add a hero line. If the user asks for a headline, write the statement, then hand the hero line to messaging-framework.

## Process

### 1. Map the alternatives
List competitive and contextual alternatives separately. For each, note what buyers like about it. You cannot beat an alternative you do not respect.

For each alternative, state the switching cost: what the buyer loses or must redo to leave it (data migration, retraining, contract terms, workflow change). Label each Sourced, Assumed, or Gap.

For broad repositioning, add the compact competitive win-conditions table from
the shared trace. Include why each alternative is attractive, the buyer criterion
that decides the comparison, the proposed advantage, proof required, and the
condition that would mean win, loss, or disqualification. Do not imply that a
relationship or capability is exclusive unless evidence supports that claim.

### 2. Isolate meaningful advantages
List capabilities the main alternatives lack or do meaningfully worse. Include
supported combinations or account-specific operating advantages when they change
a buyer criterion. Explain the scope; do not call shared features exclusive.
Shared features with no comparative buying reason go in "table stakes."

### 3. Translate advantage into value
For each meaningful capability or comparative advantage: what changes for the
buyer, which alternative it improves on, then proof. Label proof Sourced,
Assumed, or Gap. Keep the right-to-win basis separate from customer-facing value.

### 4. Apply the best-fit customer scope
Use the accepted market/segment and relevant persona evidence. Do not run market
selection inside positioning. If absent, route selection to market-entry-brief;
an explicit exploratory candidate may support a labeled positioning hypothesis
with its risk/scope/validation trigger. Missing consequential fit evidence can
hold the positioning choice while alternatives/capability analysis continues.
Preserve canonical ICP where decisions conflict. Reopening or replacing an
accepted decision requires SSOT review and human approval, never bootstrap saving.

### 5. Choose the market frame
First state the category buyers currently place the product in, with evidence (how they search, what they compare you to, what they call you on calls or in reviews). Label it Sourced, Assumed, or Gap.

Then recommend claim, subcategory, or create. Explain which frame makes the unique value obvious to the best-fit customer in the fewest words. If the recommended frame differs from where buyers place you today, name the gap and the cost of moving buyers across it (education, content, sales cycle length, budget).

### 6. State the trade-offs
Say what this positioning gives up: segments de-prioritized, messages dropped, deals you will now lose. Positioning without trade-offs is a wish list.

Add one line on the main competitor's likely response to this positioning, and what it would do to the position.

### 7. Tighten the statement
Apply the shared preference-before-drafting check to the choice already made.
Preserve its buyer tension, alternative, relative advantage and proof in the
handoff to messaging; a category label alone does not complete this decision.

Count the words and the capabilities in your draft. If it runs past 25 words, or names more than one capability, move each extra capability to the capability table, pick the single phrase that best sets the product apart, and rewrite. Repeat until it passes.

### 8. Stress-test it
Run each test and report the result honestly:
- **Swap test:** could a named competitor say this truthfully? If yes, test whether
  the complete, evidence-supported combination of capability, workflow,
  deployment boundary, account access or operating model still changes the
  buyer's comparison. A combination may be a defensible right to win without
  being exclusive. If no buyer criterion or proof supports the combination, fail
  it as generic.
- **Copy test:** could a competitor make this claim true within 12 months, by shipping a feature or changing pricing? If yes, say which one and how, and treat the position as temporary.
- **Proof test:** is every claim backed by something you have or can get this quarter? Fail a claim if churn reasons or support data contradict it, and cite the contradicting data.
- **Rep test:** can a sales rep say it in one sentence without notes?
- **Buyer test:** does it use the words customers use, not internal vocabulary?
- **Consistency test:** run section 6 of `../_shared/segment-selection.md` on everything this work names. That covers the statement's segment, any sizing or KPIs in the context, and any hero line, subhead, or segment first line already written. Flag segment-specific words, such as "free credits," in a line meant for several segments. Fix each mismatch or state why it is intentional.

## Output Format

Lead with the statement. Use this structure:

```
## Positioning statement (internal strategy, not copy)
[Product] is a [category + one short differentiating phrase] for [segment].
(One sentence, 25 words or fewer, one capability.)

## Derivation trace
| Slot | Filled with | Source | Label |
|---|---|---|---|
| Category | [claim / subcategory / create, and why] | [research finding or quote] | Sourced / Assumed / Gap |
| Differentiating phrase | [one concrete phrase] | | |
| Segment | [a specific segment, never "everyone" or "businesses"] | | |
| Trigger | [the event that starts the search, such as a failed audit or a new hire] | | |

Competitive alternatives: [what is on the shortlist, with switching cost for each]
Contextual alternative: [what the product truly replaces, with switching cost]
Current category: [where buyers place the product today, with evidence and label]

## Capabilities
| Capability | What it does for the buyer | Proof | Buyer voice | Label |
|---|---|---|---|---|
| [every capability, checkpoint, or mechanism not in the statement] | | [proof, or "Gap: need ..."] | ["quote", or "Gap: need a buyer quote"] | Sourced / Assumed / Gap |

## Trade-offs we are making
[Include one line on the main competitor's likely response.]
## Stress-test results
## Consistency check
[Tables from section 6 of ../_shared/segment-selection.md, for the segments this work names]
## Assumptions and open questions
[At most 5 bullets combined, one line each. The assumptions that most affect the answer first, then the 2 or 3 questions that would change it.]
## Evidence gaps (top five)
[Ranked table from ../_shared/evidence-gaps.md, then the appendix with every remaining Assumed and Gap item.]
```

Fill every slot in the trace. Cite its finding or quote and label it Sourced,
Assumed or Gap. After comparing alternatives, recommend one statement per
applicable positioning level, not an unranked list. Every capability considered
appears in the differentiating phrase or capability table. **Rework mode:** test
the old statement before rewriting. Report its failed stress tests directly after
the new statement, then show the old and new statements side by side and explain
what changed.

For broad repositioning, add a short **Positioning levels** block after the
statement: company position, beachhead solution position, relationship between
them, and the evidence gate for the next expansion. Add the competitive
win-conditions table required by the shared trace. Do not add these blocks for a
narrow product positioning request.

## Common Failure Modes

- Positioning on features the top competitor also has.
- Choosing "everyone" as the target to avoid a hard call.
- Recommending category creation because it sounds bold.
- Writing a tagline and calling it positioning.
- Adding a hero line or a second catchy sentence under the statement. Hand that to messaging-framework.
- Capabilities phrased as assets ("the data we already have") or abstract nouns ("visibility", "insights").
- Listing four frameworks instead of producing one position.
- A statement that breaks the "[Product] is a [category + one short differentiating phrase] for [segment]" structure, runs past 25 words, or lists capabilities.
- Dropping a capability when tightening the statement instead of moving it to the capability table.
- Trace slots with no Sourced, Assumed, or Gap label.
- Choosing a wedge only because a competitor is weak there.

## After Delivering

For PMC-originated work, return the proposal and findings for integration; skip
automatic bootstrap saving. For standalone work, save the proposed statement,
derivation trace (including Trigger), and capability table with labels to the Positioning section of `.agents/product-marketing-context.md`. Do this by default, then tell the user what was saved. Saving this bootstrap section does not approve the position or modify canonical SSOT. Preserve approval status and label new strategy as a proposal. messaging-framework uses approved mapped SSOT for covered claims and this section for uncovered provisional context. Suggest messaging-framework as the next step.

## Output Rules

- No em dashes in output.

## Related Skills

- **messaging-framework**: Carry the capability table forward and turn this positioning into hero lines and persona messaging
- **icp-and-buyer-personas**: Define and validate the best-fit customer in depth
- **competitor-profiling**: Research alternatives before positioning
- **customer-research**: Gather the evidence this skill depends on
- **product-marketing-context**: Save the positioning so every skill uses it
