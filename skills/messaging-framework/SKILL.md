---
name: messaging-framework
description: "When the user wants to build or fix a messaging framework, messaging house, or value proposition hierarchy. Use when the user mentions 'messaging,' 'messaging framework,' 'messaging house,' 'messaging pillars,' 'hero line,' 'value props,' 'key messages,' 'proof points,' 'boilerplate,' 'elevator pitch,' 'message by persona,' 'launch messaging,' or 'our messaging is inconsistent.' Use this after positioning is set and before writing page copy, decks, or campaigns. For deciding the position itself, see positioning-strategy. For turning messaging into web copy, see marketing-copy. For sales materials, see sales-enablement."
metadata:
  version: 1.5.1
---

# Messaging Framework

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

**Use the company SSOT when present:** follow `../_shared/ssot-consumption.md` and the project manifest to load only this task’s approved context. Build the framework from approved positioning and persona research; route proposed canon changes through `ssot-context-loop` for human approval.

You turn an internal positioning statement into messaging every team can reuse: a capability table with proof and buyer voice, a recommended hero line derived from it, and translations by persona. Positioning is strategy. Hero lines are the first expression of it.

Deliver the finished framework, not advice about how to write one.

## Before Starting

**Load the shared reference:** read `../_shared/messaging-examples.md` (relative to this skill's folder). Follow section 2 for capabilities and section 3 for the hero line: who reads the hero, the decision tree, the against or for frame, and how to write and recommend.

**Load the evidence labels:** read `../_shared/evidence-gaps.md`. Label every capability, proof point, and persona line Sourced, Assumed, or Gap. Open the output with its "Inputs and assumptions" note and end with its Evidence gaps section.

**Load the consistency check:** read section 6 of `../_shared/segment-selection.md`. Run it in step 8.

**Load the positioning-to-messaging trace:** read `../_shared/positioning-messaging-trace.md` when developing a framework or revising its primary value argument. Preserve those levels in the message hierarchy. A narrow messaging request stays within its named product, use case and channel.

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it. Its Positioning section (statement, trace, and capability table), Persona message map, and proof points support initialization and chaining. Approved mapped SSOT is authoritative for covered claims; bootstrap inputs may fill uncovered provisional context but cannot override it. Missing bootstrap sections do not make approved SSOT unavailable.

You need an upstream position to build from. If neither approved context nor an
explicit upstream proposal supplies it, route to positioning-strategy; do not
infer a reusable position. Missing company understanding routes to PMC first.
A user-supplied or specialist-proposed position may support bounded expression
drafts, preserving its assumption/risk/scope/validation and approval dependency.

Never invent stats, customers, or quotes as proof. Mark missing proof or buyer quotes as gaps in the table.

Assess shared evidence readiness first. Hold only consequential unsupported
choices and continue independent sections. For permitted provisional expression,
flag assumptions, understood risk, scope and validation trigger. Put the assumptions that most affect it in the Assumptions block under the capability table, and end with the two or three questions that would change it. Keep the two together to 5 bullets at most. Never infer customer pain points or product benefits silently. Label them as assumptions.

Open with Inputs and assumptions, then the capability table. Do not restate the brief.

## Core Principles

**The swap test.** Test a claim against named alternatives and the buyer's decision
criteria. A supported combination of capability, operating model or account
relationship may matter without being exclusive. State its scope and proof.
Claims every player can make with equal relevance and proof, such as generic ease
of use or security, are table stakes. List them separately.

**Concrete capabilities.** A capability is the new ability a feature gives the
customer: verb-led and concrete, something an engineer could point to. Short
phrases like "auto-drafting invoices" work well. Express relationship advantages
as customer actions or benefits, not assets the company holds. Keep account
access in the internal right-to-win rationale. Avoid abstract nouns like
visibility, insights, or platform.

**The hero is for the loosely familiar visitor.** People who know the product go straight to the CTA, and people who don't know it read the whole page. The hero speaks to the ones in between, and the sections below carry the capabilities and proof.

**Anchor from evidence.** Choose the anchor by walking the decision tree in the shared reference, and back each answer with evidence. Where the evidence is thin, say so and show both branches.

**Outcome over description.** Messaging says how the buyer's life gets better, not what the product is. Test every line with "so what?" until it lands on an outcome the buyer cares about.

**Proof or it did not happen.** Every capability needs at least one proof point: a metric, a customer, a demo moment, or a third-party signal. If you do not have it, the table says so.

**Name the trade-off.** Say what this messaging emphasizes and what it gives up or leaves for later. A framework that emphasizes everything emphasizes nothing.

**Customer words beat company words.** Pull verbatim language from interviews, reviews, and sales calls when available. Internal jargon goes in the "avoid" list.

## Process

### 1. Confirm the inputs
Restate the position, best-fit customer, and top two alternatives in three lines. Flag anything you had to assume.

Write one line on the cost of doing nothing, taken from the positioning's contextual alternative: what the buyer keeps paying in time, money, or risk if they stay with it. Label it Sourced, Assumed, or Gap.

### 2. Build the capability table
One row per differentiating capability: the capability, what it does for the buyer, the proof, and the buyer's own words. Build rows from approved mapped SSOT positioning and capabilities where applicable. For uncovered provisional context, use the context doc's Positioning section: its differentiating phrase and every row of its capability table each become a row here, with their labels. Do not carry bootstrap rows that contradict covered canon into messaging; flag them for SSOT review. No applicable upstream capability may be silently dropped; excluded contradictory bootstrap rows remain review items. If the differentiating phrase and a table row name the same capability, merge them into one row. Log the merge in Inputs and assumptions as an upstream positioning issue. Mark missing proof or quotes as gaps inside the table. Directly under the table, list the assumptions it rests on.

**Never add a differentiator.** If one seems missing, list it under "Proposed for positioning" with a one-line reason, and do not use it anywhere in the messaging. The fix belongs in positioning-strategy.

If bootstrap Positioning is missing, use applicable approved SSOT inputs. Where neither source supplies the position, route to positioning-strategy and hold dependent strategic rows; do not infer new positioning. Do not invent differentiators for covered canon.

### 3. Write the hero line
Use the shared selected preference, buyer tension and proof from positioning,
not only its capability rows. If that choice is absent, request it from the
positioning owner; continue independent copy within supplied scope. Apply the
headline-plus-subhead substitution check before recommending the primary pair.

1. **Write for the loosely familiar visitor.**
2. **Walk the decision tree.** Answer each question in order (mature or immature category, then the branch questions) and state each answer and its evidence in one line. Name the anchor it leads to. If a branch has thin evidence, say so and show the hero for both branches.
3. **Choose the frame,** against a named alternative the buyer already uses or for the job they are trying to do, and say why in one line.
4. **Write 3 to 5 hero lines** in the chosen anchor and frame. Give each a subhead that carries the specifics: capabilities, a number, or the mechanism.
5. **Recommend one** and cite the research finding it rests on. If there is none, say the pick is an assumption.

### 4. Separate table stakes
List the claims that are true but shared. Note where each can still appear, such as on a feature page, without leading the message.

### 5. Translate by persona
Start from approved mapped SSOT persona messaging where applicable; otherwise use the context doc's Persona message map for uncovered provisional context.
Use relevant persona intelligence and any originating brief to choose the
leading capability/argument,
proof emphasis, objections to address and appropriate detail for each persona.
Preserve canonical strategic meaning, facts and approval status while adapting
expression. A bootstrap map cannot override covered SSOT. Explain these choices
in concise traceable rationale; final asset CTAs and channel mechanics
remain with execution owners.

For each leading pillar, retain a compact internal trace: buyer insight, named
alternative, differentiated value, proof label, relevant persona and sales action.
Use the application or business owner when their outcome or budget differs from
the infrastructure owner's. Do not turn internal rationale such as account access
or a validation plan into a customer-facing benefit.

For broad work, compare two or three plausible messaging hierarchies before
selecting one. Judge buyer outcome, distinction, product support, proof and
commercial usefulness. Keep the rationale internal; publish the selected copy
without repeating evidence labels in every line. Claim qualifications still
belong beside any claim whose meaning would otherwise change.

If the bootstrap map is missing, use applicable approved SSOT persona inputs. Where neither source supplies a persona, route profile generation to icp-and-buyer-personas. Do not generate reusable personas or persona priorities; hold dependent translations and continue independent sections.

### 6. Write the boilerplate
Provide three lengths: a one-liner (about 10 words), an elevator pitch (about 30 words), and a company boilerplate (about 60 words).

### 7. Set language rules
List words to use (customer language) and words to avoid (jargon, clichés, competitor terms).

### 8. Check consistency
Run section 6 of `../_shared/segment-selection.md`. The segments in the hero line, subhead, and each persona or segment first line must match the positioning's segment, and any sizing or KPIs in the context. Flag segment-specific words in a line meant for several segments. Example: "free credits" or "compute" in a hero meant for AI, SaaS, and consumer subscriptions. Fix each mismatch or state why it is intentional.

## Output Format

Use the complete format for a framework. For a narrow applied-copy request with
supplied positioning and persona scope, return only the requested copy plus any
material claim limitation or upstream conflict. Do not force a full messaging
house, positioning comparison or discovery study into that request.

```
## Inputs and assumptions
[Table from ../_shared/evidence-gaps.md. Record approved mapped SSOT and/or bootstrap Positioning and Persona message map inputs, their evidence labels, approval status, and missing context.]

## Capabilities
| Capability | What it does for the buyer | Proof | Buyer voice | Label |
|---|---|---|---|---|
| [row from approved SSOT or uncovered provisional positioning] | | [proof, or "Gap: need ..."] | ["quote", or "Gap: need a buyer quote"] | Sourced / Assumed / Gap |

### Assumptions
[The assumptions this table rests on, one line each.]

### Proposed for positioning
[Differentiators that seem missing from the positioning, one line each with the reason. Not used in this messaging. Omit if none.]

## Cost of doing nothing
[One line from the positioning's contextual alternative, with label.]

## Hero line
Reader: the loosely familiar visitor.

Decision tree:
- Q1 Category maturity: [mature / immature]. Evidence: [finding or quote, or "thin"]
- Q2 [branch question]: [answer]. Evidence: [...]
- Q3 [branch question]: [answer]. Evidence: [...]
Anchor: [persona / category / feature / capability / problem / benefit]
[If a branch has thin evidence: show the hero for both branches.]

Frame: [against X / for Y], because [one line]

1. [Hero line]
   [Subhead with capabilities, a number, or the mechanism]
2. ...
(3 to 5 in total)

**Recommended:** [line number and line], because [research finding or quote]

## What this emphasizes and gives up
## Table stakes (not differentiators)
## Messaging by persona
| Persona | Lead capability | First line they hear | Label |
|---|---|---|---|

## Boilerplate
One-liner / Elevator / Boilerplate

## Language
Use: ... | Avoid: ...

## Consistency check
[Tables from section 6 of ../_shared/segment-selection.md: hero, subhead, and first lines against the positioning's segments]

## Questions that would change this
[2 or 3 questions. Together with the Assumptions block, 5 bullets at most.]

## Evidence gaps (top five)
[Ranked table from ../_shared/evidence-gaps.md, then the appendix with every remaining Assumed and Gap item.]
```

For launch messaging, add a short block covering target, market, segment, category, unique value, and proof, so the launch team has one reference.

For company repositioning, add a **Message levels** block that connects the
company narrative to beachhead value, pillars, persona proof and sales action.
Use the shared trace for this handoff. Do not force a multilevel architecture or
full market discovery into a narrow copy request.

## Common Failure Modes

- Pasting the positioning statement in as the headline.
- Picking an anchor without walking the decision tree, or answering it without evidence.
- Hiding thin evidence instead of showing the hero for both branches.
- Leaving the frame implicit instead of choosing against or for.
- Capabilities phrased as abstract nouns (visibility, insights, intelligence, protection, platform) or as assets the company holds.
- Capabilities any competitor could claim.
- Dropping a capability that the positioning statement or its capability table named.
- Generic shared treatment that ignores material buyer differences. Shared
  treatment is valid when relevant evidence supports shared needs.
- Adding differentiators not in positioning. List them under "Proposed for positioning" instead.
- Treating missing bootstrap sections as missing canon when approved mapped SSOT supplies the inputs. If neither supplies persona context, route to icp-and-buyer-personas and hold dependent translations.
- Proof or buyer voice cells full of vague claims like "customers love it" instead of a marked gap.
- Headlines or lines in the form "Do this, not that" or "X, not Y." They read as AI-written. The one exception is in the shared reference's style notes: a deliberate parallel against-frame, at most once per page.
- Em dashes anywhere in the messaging.
- Clichés: unlock, seamless, game-changer, leverage, revolutionize, next-generation.

## After Delivering

For PMC-originated work, return proposals/findings for integration; skip bootstrap
saving. For standalone work, offer to save the proposed capability table and recommended hero line to `.agents/product-marketing-context.md`. Suggest marketing-copy for pages and sales-enablement for decks.

## Output Rules

- No em dashes in output.

## Related Skills

- **positioning-strategy**: Set the position before building messaging
- **icp-and-buyer-personas**: Define who each message variant is for
- **marketing-copy**: Turn the framework into page copy
- **sales-enablement**: Turn it into decks, one-pagers, and talk tracks
- **launch-strategy**: Use launch messaging in a release plan
