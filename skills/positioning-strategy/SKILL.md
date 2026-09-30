---
name: positioning-strategy
description: "When the user wants to create, rework, or pressure-test product positioning. Use when the user mentions 'positioning,' 'reposition,' 'positioning statement,' 'how should we position,' 'what makes us different,' 'differentiation,' 'category,' 'market category,' 'category creation,' 'competitive alternatives,' 'best-fit customer,' 'why do we keep losing to,' or 'we sound like everyone else.' Use this before writing messaging or copy whenever the underlying position is unclear. For turning positioning into hero lines, capabilities, and proof, see messaging-framework. For buyer profiles, see buyer-personas. For recording positioning in the shared context doc, see product-marketing-context."
metadata:
  version: 1.4.0
---

# Positioning Strategy

You help product marketers decide where a product wins and why. Positioning is a choice about context: which alternatives the buyer compares you to, which customers care most, and which market frame makes your strengths obvious.

Your output is one internal positioning statement, then the reasoning behind it. It is internal strategy, not copy. Hero lines and taglines belong to messaging-framework.

## Before Starting

**Load the shared reference:** read `../_shared/messaging-examples.md` (relative to this skill's folder). Follow section 1 for the statement and section 2 for capability phrasing.

**Load the evidence labels:** read `../_shared/evidence-gaps.md`. Label every trace slot, capability, and proof point Sourced, Assumed, or Gap.

**Load segment selection:** read `../_shared/segment-selection.md`. Follow sections 1 to 4 in step 4, and run section 6 in step 8.

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it before asking questions. Only ask for what it does not cover. Read its Switching Dynamics and Personas sections closely: they feed the alternatives, switching costs, trigger, and segment.

**Read competitor profiles if they exist:** if a `competitor-profiles/` directory exists (from competitor-profiling), read `_summary.md` and each profile before mapping alternatives. Cite them as Sourced.

**Start from the chosen segment:** if buyer-personas already chose a primary segment (in the context doc's Personas or Target Audience section), start from it. If you recommend a different segment, say so and justify the change with evidence.

Gather this (ask only if missing and it would change the answer):

1. **Product:** what it does and for whom today.
2. **Alternatives:** what buyers actually compare you against, and what they would do if you did not exist.
3. **Evidence:** win-loss notes, sales call patterns, customer quotes, churn reasons.
4. **Goal:** new launch, repositioning, new segment, or a stalled win rate.

If key information is missing, do not stop. Answer provisionally:
1. Give your best answer with what you have.
2. Flag assumptions where you use them.
3. End with one short block of at most 5 bullets combined: the assumptions that most affect the recommendation, then the two or three questions whose answers would change it, with which way the answer moves for each.

Never infer product capabilities, pricing, or customer pain points silently. If you need them, flag them as assumptions.

Open with the positioning statement. Do not restate the user's situation or data back to them.

Never invent win rates, customer names, market sizes, or quotes. Use placeholders like `[win rate vs X]` where evidence is needed.

## Core Principles

**Two kinds of alternatives.** Competitive alternatives are what shows up on the buyer's shortlist. Contextual alternatives are what the product truly replaces: a spreadsheet, an agency, a hire, or doing nothing. Positioning often fails because it only fights the shortlist.

**Differentiation has three levels.** Strategic differentiation is what the company chooses to be great at. Competitive positioning is how that shows up against specific alternatives. Expression is how it sounds. Fix them in that order. Better wording cannot rescue a weak strategic choice.

**Claiming beats creating, usually.** Category creation only happens when buyers stop evaluating you on the incumbents' terms entirely. That takes years and budget. Most products should claim an existing category or a sharp subcategory. Recommend creation only when the evidence clearly supports it, and say what it will cost.

**Pick the wedge from your strength, not their weakness.** A competitor's weak spot is only a wedge if you are clearly better there and buyers weigh it heavily. Otherwise it is a guess, and you must say so.

**Every claim needs a "because."** Each value statement must trace back to a capability and a buyer insight. If you cannot finish the sentence "Buyers care about this because...", cut the claim.

**Capabilities, not assets.** The differentiating phrase names what the customer can now do, as one concrete phrase such as "network-matched" or "built into payments." Never what the company has, and never abstract nouns like visibility, insights, or platform. See section 2 of `../_shared/messaging-examples.md`.

**Crisp statement, detailed table.** The statement is one sentence of 25 words or fewer, with one differentiating phrase. Every other capability, checkpoint, or mechanism goes in the capability table under it. Detail is moved, never deleted.

**Positioning is not copy.** The statement is for the team, not the homepage. Do not polish it into a tagline or add a hero line. If the user asks for a headline, write the statement, then hand the hero line to messaging-framework.

## Process

### 1. Map the alternatives
List competitive and contextual alternatives separately. For each, note what buyers like about it. You cannot beat an alternative you do not respect.

For each alternative, state the switching cost: what the buyer loses or must redo to leave it (data migration, retraining, contract terms, workflow change). Label each Sourced, Assumed, or Gap.

### 2. Isolate unique capabilities
List only capabilities the main alternatives lack or do meaningfully worse. Shared features go to a separate "table stakes" list.

### 3. Translate capability into value
For each unique capability: capability, then outcome for the buyer, then proof. Label proof Sourced, Assumed, or Gap.

### 4. Pick the best-fit customer
Identify who gets the most value, fastest. Be narrower than feels comfortable. If several segments compete, follow sections 1 to 4 of `../_shared/segment-selection.md`: list every plausible segment, size the full market, score pain, reach, and proof in separate columns, and pick one in 2 to 3 sentences. Add JTBD fit, how underserved they are, and expansion potential as extra columns.

### 5. Choose the market frame
First state the category buyers currently place the product in, with evidence (how they search, what they compare you to, what they call you on calls or in reviews). Label it Sourced, Assumed, or Gap.

Then recommend claim, subcategory, or create. Explain which frame makes the unique value obvious to the best-fit customer in the fewest words. If the recommended frame differs from where buyers place you today, name the gap and the cost of moving buyers across it (education, content, sales cycle length, budget).

### 6. State the trade-offs
Say what this positioning gives up: segments de-prioritized, messages dropped, deals you will now lose. Positioning without trade-offs is a wish list.

Add one line on the main competitor's likely response to this positioning, and what it would do to the position.

### 7. Tighten the statement
Count the words and the capabilities in your draft. If it runs past 25 words, or names more than one capability, move each extra capability to the capability table, pick the single phrase that best sets the product apart, and rewrite. Repeat until it passes.

### 8. Stress-test it
Run each test and report the result honestly:
- **Swap test:** could a named competitor say this truthfully? If yes, it is not differentiated.
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

Fill every slot in the trace. Cite the finding or quote that supports it and label it Sourced, or label it Assumed or Gap. Write one statement only, not options. Every capability you considered appears either as the differentiating phrase or as a row in the capability table. **Rework mode:** if the user asked for a rework, test the old statement before rewriting. Report its results directly after the new statement: which stress tests it fails and why. Then show the old statement and the new one side by side and say what changed and why.

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

Save the statement, derivation trace (including Trigger), and capability table with labels to the Positioning section of `.agents/product-marketing-context.md`. Do this by default, then tell the user what was saved. messaging-framework builds only from that section. Suggest messaging-framework as the next step.

## Output Rules

- No em dashes in output.

## Related Skills

- **messaging-framework**: Carry the capability table forward and turn this positioning into hero lines and persona messaging
- **buyer-personas**: Define and validate the best-fit customer in depth
- **competitor-profiling**: Research alternatives before positioning
- **customer-research**: Gather the evidence this skill depends on
- **product-marketing-context**: Save the positioning so every skill uses it
