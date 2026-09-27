---
name: messaging-framework
description: "When the user wants to build or fix a messaging framework, messaging house, or value proposition hierarchy. Use when the user mentions 'messaging,' 'messaging framework,' 'messaging house,' 'messaging pillars,' 'hero line,' 'value props,' 'key messages,' 'proof points,' 'boilerplate,' 'elevator pitch,' 'message by persona,' 'launch messaging,' or 'our messaging is inconsistent.' Use this after positioning is set and before writing page copy, decks, or campaigns. For deciding the position itself, see positioning-strategy. For turning messaging into web copy, see copywriting. For sales materials, see sales-enablement."
metadata:
  version: 1.2.0
---

# Messaging Framework

You turn an internal positioning statement into messaging every team can reuse: a recommended hero line, a capability table with proof and buyer voice, and translations by persona. Positioning is strategy. Hero lines are the first expression of it.

Deliver the finished framework, not advice about how to write one.

## Before Starting

**Load the shared phrasing rules:** read `../_shared/capability-phrasing.md` (relative to this skill's folder). Use its capability rules for every row and subhead, and its archetypes for hero lines.

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it. Positioning, personas, and proof points there are your inputs.

You need a position to build from. If none exists:
- If the user gave enough detail, infer a provisional position, label it clearly, and continue.
- If the position is truly unclear, say so and recommend positioning-strategy first. Still give provisional hero lines so the user has something to react to.

Never invent stats, customers, or quotes as proof. Mark missing proof or buyer quotes as gaps in the table.

If key information is missing, answer provisionally: give your best framework and flag assumptions where you use them. Put the assumptions that most affect it in the Assumptions block under the capability table, and end with the two or three questions that would change it. Keep the two together to 5 bullets at most. Never infer customer pain points or product benefits silently. Label them as assumptions.

Open with the recommended hero line. Do not restate the brief.

## Core Principles

**The swap test.** A capability only belongs in the table if a competitor cannot claim it word for word and be telling the truth. Claims every player can make, such as ease of use, security, or saving time, are table stakes. List them separately. Buyers expect them, and they do not win deals.

**Concrete capabilities.** Name each capability as a 2 to 4 word mechanism an engineer could point to. No assets the company holds, and no abstract nouns like visibility, insights, or platform.

**One archetype, named.** Hero lines follow one archetype from the shared phrasing rules, chosen to match the axis of differentiation. Say which, and why.

**Outcome over description.** Messaging says how the buyer's life gets better, not what the product is. Test every line with "so what?" until it lands on an outcome the buyer cares about.

**Proof or it did not happen.** Every capability needs at least one proof point: a metric, a customer, a demo moment, or a third-party signal. If you do not have it, the table says so.

**Name the trade-off.** Say what this messaging emphasizes and what it gives up or leaves for later. A framework that emphasizes everything emphasizes nothing.

**Customer words beat company words.** Pull verbatim language from interviews, reviews, and sales calls when available. Internal jargon goes in the "avoid" list.

## Process

### 1. Confirm the inputs
Restate the position, best-fit customer, and top two alternatives in three lines. Flag anything you had to assume.

### 2. Write hero lines
1. **Name the axis of differentiation** from the positioning: audience, problem, category, mechanism, unique feature, or outcome.
2. **Pick the matching archetype** and say why in one line.
3. **Write 3 to 5 hero lines** in that archetype. Give each a subhead that names concrete capabilities.
4. **Recommend one** and cite the research finding or quote behind it. If there is none, say the pick is an assumption.

### 3. Build the capability table
One row per differentiating capability: the capability, what it does for the buyer, the proof, and the buyer's own words. Mark missing proof or quotes as gaps. Directly under the table, list the assumptions the table rests on.

### 4. Separate table stakes
List the claims that are true but shared. Note where each can still appear, such as on a feature page, without leading the message.

### 5. Translate by persona
For each key persona, adapt the emphasis, not the facts. Show which capability leads for that persona and the one line they should hear first.

### 6. Write the boilerplate
Provide three lengths: a one-liner (about 10 words), an elevator pitch (about 30 words), and a company boilerplate (about 60 words).

### 7. Set language rules
List words to use (customer language) and words to avoid (jargon, clichés, competitor terms).

## Output Format

```
## Hero line
Axis of differentiation: [audience / problem / category / mechanism / unique feature / outcome]
Archetype: [name], because [one line]

1. [Hero line]
   [Subhead naming capabilities]
2. ...
(3 to 5 in total)

**Recommended:** [line number and line], because [research finding or quote]

## Capabilities
| Capability | What it does for the buyer | Proof | Buyer voice |
|---|---|---|---|
| [2 to 4 word mechanism] | | [proof, or "Gap: need ..."] | ["quote", or "Gap: need a buyer quote"] |

### Assumptions
[The assumptions this table rests on, one line each.]

## What this emphasizes and gives up
## Table stakes (not differentiators)
## Messaging by persona
| Persona | Lead capability | First line they hear |
|---|---|---|

## Boilerplate
One-liner / Elevator / Boilerplate

## Language
Use: ... | Avoid: ...

## Questions that would change this
[2 or 3 questions. Together with the Assumptions block, 5 bullets at most.]
```

For launch messaging, add a short block covering target, market, segment, category, unique value, and proof, so the launch team has one reference.

## Common Failure Modes

- Pasting the positioning statement in as the headline.
- Hero lines with no named archetype, or mixing archetypes in one set.
- Capabilities phrased as abstract nouns (visibility, insights, intelligence, protection, platform) or as assets the company holds.
- Capabilities any competitor could claim.
- One message for every persona with no change in emphasis.
- Proof or buyer voice cells full of vague claims like "customers love it" instead of a marked gap.
- Headlines or lines in the form "Do this, not that" or "X, not Y." They read as AI-written.
- Em dashes anywhere in the messaging.
- Clichés: unlock, seamless, game-changer, leverage, revolutionize, next-generation.

## After Delivering

Offer to save the recommended hero line and capability table to `.agents/product-marketing-context.md`. Suggest copywriting for pages and sales-enablement for decks.

## Output Rules

- No em dashes in output.

## Related Skills

- **positioning-strategy**: Set the position before building messaging
- **buyer-personas**: Define who each message variant is for
- **copywriting**: Turn the framework into page copy
- **sales-enablement**: Turn it into decks, one-pagers, and talk tracks
- **launch-strategy**: Use launch messaging in a release plan
