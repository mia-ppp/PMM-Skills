---
name: icp-and-buyer-personas
description: "Define ICP, buyer personas, buying committees and anti-personas within an accepted market. Use for ideal customer profiles, persona research, buying roles and exclusion criteria. Propose audience changes through SSOT governance."
metadata:
  version: 1.3.0
---

# ICP and Buyer Personas


**Use the company SSOT when present:** follow `../_shared/ssot-consumption.md` and the project manifest to load only relevant approved context. Preserve covered strategic meaning while keeping this skill’s existing scope and frameworks.

You build personas that change decisions. A persona earns its place only if it changes what the team says, where it shows up, or who it sells to. Demographic filler does not.

Deliver the personas themselves, not a template for making them.

## Ownership and accepted market

Own ICP, personas, buying committees and anti-personas within accepted market selection.
Inherit the accepted market; do not use persona work to select another market.
Proposed ICP or persona changes require `ssot-context-loop` governance and human approval.
Include fit/exclusion criteria, committee roles, evidence confidence and gaps in the output.


## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it before asking questions.

**Check for an existing segment decision before selecting an ICP.** Look for an
accepted market-entry brief for the same company and market, and read the
manifest-mapped SSOT ICP/decision context using `../_shared/ssot-consumption.md`.
If an accepted brief already selected a segment and it does not conflict with
canonical SSOT, use that segment for persona work. Do not independently rescore
or choose a different market. An `Explore` decision means the segment remains a
hypothesis; a `Pass` is not the current target. If the brief and SSOT conflict,
flag the conflict and route it through `ssot-context-loop` for review. Do not
silently prefer a newer brief or overwrite the canonical ICP. Reopen prioritization
through `market-entry-brief` only when the user explicitly asks to reconsider it.

Find out which mode applies:
- **Evidence mode:** the user has interviews, call notes, CRM data, win-loss, or surveys. Build from those.
- **Hypothesis mode:** little or no research. Draft personas with attributes labeled Assumed or Gap, then give a plan to validate them.

If key information is missing, answer provisionally: give your best personas, label assumptions where you use them, and end with one short block of at most 5 bullets combined: the assumptions that most affect the personas, then the two or three questions that would change them. The validation plan's interview questions do not count toward the 5. Open with the persona message map, then the recommended segment. Do not restate the brief.

When no accepted market-entry/SSOT decision establishes the market, route market
selection to `market-entry-brief`. Persona hypotheses may remain provisional,
with that dependency explicit; they do not select or approve a new market.
When an accepted decision exists, consume it and skip market selection.

Label every persona attribute Sourced, Assumed, or Gap, as defined in the Labels section of `../_shared/evidence-gaps.md`. Never present a guess as research. Never invent quotes. If you use a quote, it must come from the user's material.

## Core Principles

**Start qualitative, validate quantitatively.** Interviews reveal the real segments and language. Surveys then show how many buyers self-select into each. Doing it in the other order produces tidy but wrong personas.

**Four attributes matter most.** Background, pain points, discovery channels, and evaluation process. These drive messaging, channel, and sales decisions. Age and hobbies rarely do.

**B2B buys by committee.** Map the user, champion, decision maker, financial buyer, and technical influencer. Each needs a different reason to say yes.

**Name the anti-persona.** Say who looks like a fit but is not, and why. This saves sales time and sharpens messaging.

## Process

### 1. Segment before you profile
If an accepted market-entry/SSOT decision already establishes the segment, carry
it forward unchanged and profile personas within it. State the source and whether
the segment is approved or exploratory. If no decision exists and multiple
segments are being compared, use the complete scorecard in
`../_shared/segment-selection.md`, including all 13 criteria, weights, evidence
labels, attractiveness score, and separate evidence confidence. Do not create a
persona-specific scoring method. Then name the lead segment, rationale, biggest
weakness, and key evidence gap. Use the shared sequencing framework for remaining
segments. Treat any selection as a recommendation, not a canon change.

### 2. Profile each persona
Cover: role and background, trigger events, pain points in their words, discovery channels, evaluation process, objections, what success looks like to them, and their role in the buying committee.

### 3. Map the buying committee
Show who starts the purchase, who blocks it, who signs, and what each needs to hear.

### 4. Define the anti-persona
Describe the look-alike buyer who churns, stalls, or costs too much to serve.

### 5. Plan validation
For hypothesis-mode personas, write the five to eight interview questions that would confirm or kill each one. Cover role, awareness, evaluation, requirements, alternatives considered, and the buying committee. End with: "If you were CEO, what would you do to compete better?" Suggest a short survey to size each segment afterward.

### 6. Write the persona message map
Summarize the persona profiles and the committee map in one table. It opens the output. Write it last, from the finished profiles.
- **Persona:** the role-based name, with the buying role in brackets, such as (champion), (evaluator), or (financial buyer).
- **What matters to them:** 1 to 2 short phrases naming the priorities that decide the deal for this persona. Examples: conversion rate, compliance, compute cost, integration effort.
- **Message:** the core message for this persona in 1 to 2 sentences, tied to a proof point with its label (Sourced, Assumed, or Gap). It is the argument that wins them over, not an opening line or hook.
- **Language:** no "X, not Y" or "Do this, not that" constructions, no clichés (unlock, seamless, game-changer, leverage, revolutionize, next-generation), and no em dashes.

## Output Format

```
## Persona message map
| Persona | What matters to them | Message |
|---|---|---|
| [Role-based name] (champion) | [1 to 2 short phrases] | [Core message, 1 to 2 sentences. Proof: [proof point] (Sourced / Assumed / Gap)] |

## Recommended primary segment
[If inherited: selected segment, source decision, status, and conflict check. Do not rescore. If not established: include the full shared scorecard, lead-segment rationale, biggest weakness, most important evidence gap, and sequence for remaining segments.]

## Persona: [Role-based name, not a cute alias]
| Attribute | Detail | Source |
|---|---|---|
| Background | | Sourced / Assumed / Gap |
| Trigger events | | |
| Pain points | | |
| Discovery channels | | |
| Evaluation process | | |
| Objections | | |
| Success looks like | | |
| Committee role | | |

**What this changes:** [the messaging, channel, or sales decision this persona drives]

## Buying committee map
## Anti-persona
## Validation plan
## Assumptions and open questions
[At most 5 bullets combined, one line each. The assumptions that most affect the answer first, then the 2 or 3 questions that would change it.]
```

Use role-based names like "RevOps Lead at a Series B SaaS company," not invented names like "Marketing Mary." Invented names hide weak detail.

## Common Failure Modes

- Personas built from demographics instead of buying behavior.
- Assumed attributes presented as Sourced findings.
- Too many personas. Three is usually enough for one product.
- Personas that do not change any decision.
- Skipping the buying committee in B2B.

## Account-level handoff

`account-based-marketing` consumes the accepted ICP and persona/committee model
for account selection, tiers, contextual hypotheses, and coordinated plays.
Personas owns the reusable buyer model; ABM owns account-specific application.

## After Delivering

Save personas to the Personas section of `.agents/product-marketing-context.md`, and the persona message map to its Persona message map section. Do this by default, then tell the user what was saved. Write one map row per persona: Persona (buying role), What matters to them, Message, and the proof's label (Sourced, Assumed, or Gap). messaging-framework starts its persona lines from that map when no applicable SSOT supplies approved persona messaging. Saving personas or the map does not approve strategy or modify canonical SSOT. Preserve approval status and mark proposed strategic changes as proposals; route canon conflicts through `ssot-context-loop`. Suggest positioning-strategy or messaging-framework as next steps.

## Output Rules

- No em dashes in output.

## Related Skills

- **customer-research**: Gather and synthesize the interviews personas depend on
- **positioning-strategy**: Use the primary persona as the best-fit customer
- **messaging-framework**: Translate messaging for each persona
- **sales-enablement**: Build persona-specific talk tracks and objection handling
- **product-marketing-context**: Save personas so every skill uses them
