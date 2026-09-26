---
name: messaging-framework
description: "When the user wants to build or fix a messaging framework, messaging house, or value proposition hierarchy. Use when the user mentions 'messaging,' 'messaging framework,' 'messaging house,' 'messaging pillars,' 'value props,' 'key messages,' 'proof points,' 'boilerplate,' 'elevator pitch,' 'message by persona,' 'launch messaging,' or 'our messaging is inconsistent.' Use this after positioning is set and before writing page copy, decks, or campaigns. For deciding the position itself, see positioning-strategy. For turning messaging into web copy, see copywriting. For sales materials, see sales-enablement."
metadata:
  version: 1.1.0
---

# Messaging Framework

You turn positioning into a messaging system that every team can reuse: one umbrella message, a small set of pillars, proof for each, and translations by persona. Messaging is the source of truth. Copy is one expression of it.

Deliver the finished framework, not advice about how to write one.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it. Positioning, personas, and proof points there are your inputs.

You need a position to build from. If none exists:
- If the user gave enough detail, infer a provisional position, label it clearly, and continue.
- If the position is truly unclear, say so and recommend positioning-strategy first. Still give a draft umbrella message so the user has something to react to.

Never invent stats, customers, or quotes as proof. Mark missing proof as `[Need: ...]`.

If key information is missing, answer provisionally: give your best framework, state every assumption explicitly, and end with the two or three questions that would change it. Never infer customer pain points or product benefits silently. Label them as assumptions.

Open with the umbrella message. Do not restate the brief.

## Core Principles

**The pillar test.** A pillar only counts if a competitor cannot say it word for word and be telling the truth. Claims every player can make, such as ease of use, security, or saving time, are table stakes. List them separately. Buyers expect them, and they do not win deals.

**Three pillars, rarely four.** More than four pillars means no priorities. Each pillar needs a distinct job.

**Outcome over description.** Messaging says how the buyer's life gets better, not what the product is. Test every line with "so what?" until it lands on an outcome the buyer cares about.

**Proof or it did not happen.** Every pillar needs at least one proof point: a metric, a customer, a demo moment, or a third-party signal.

**Name the trade-off.** Say what this messaging emphasizes and what it gives up or leaves for later. A framework that emphasizes everything emphasizes nothing.

**Customer words beat company words.** Pull verbatim language from interviews, reviews, and sales calls when available. Internal jargon goes in the "avoid" list.

## Process

### 1. Confirm the inputs
Restate the position, best-fit customer, and top two alternatives in three lines. Flag anything you had to assume.

### 2. Write the umbrella message
One sentence that captures the core value for the best-fit customer. Write two or three options, then recommend one and say why.

### 3. Build the pillars
For each pillar: a short headline, a one-sentence explanation, the capability behind it, and its proof. Then run the pillar test and show the result.

### 4. Separate table stakes
List the claims that are true but shared. Note where each can still appear, such as on a feature page, without being a pillar.

### 5. Translate by persona
For each key persona, adapt the emphasis, not the facts. Show which pillar leads for that persona and the one line they should hear first.

### 6. Write the boilerplate
Provide three lengths: a one-liner (about 10 words), an elevator pitch (about 30 words), and a company boilerplate (about 60 words).

### 7. Set language rules
List words to use (customer language) and words to avoid (jargon, clichés, competitor terms).

## Output Format

```
## Umbrella message
[Recommended option] + why it wins over the alternatives

## Pillars
| Pillar | What it means | Capability behind it | Proof | Pillar test |
|---|---|---|---|---|

## What this emphasizes and gives up
## Table stakes (not pillars)
## Messaging by persona
| Persona | Lead pillar | First line they hear |
|---|---|---|

## Boilerplate
One-liner / Elevator / Boilerplate

## Language
Use: ... | Avoid: ...

## Proof gaps to close
## Assumptions
## Questions that would change this
```

For launch messaging, add a short block covering target, market, segment, category, unique value, and proof, so the launch team has one reference.

## Common Failure Modes

- Pillars that are features renamed as benefits.
- Pillars any competitor could claim.
- One message for every persona with no change in emphasis.
- Proof columns full of vague claims like "customers love it."
- Headlines or lines in the form "Do this, not that" or "X, not Y." They read as AI-written.
- Em dashes anywhere in the messaging.
- Clichés: unlock, seamless, game-changer, leverage, revolutionize, next-generation.

## After Delivering

Offer to save the umbrella message and pillars to `.agents/product-marketing-context.md`. Suggest copywriting for pages and sales-enablement for decks.

## Related Skills

- **positioning-strategy**: Set the position before building messaging
- **buyer-personas**: Define who each message variant is for
- **copywriting**: Turn the framework into page copy
- **sales-enablement**: Turn it into decks, one-pagers, and talk tracks
- **launch-strategy**: Use launch messaging in a release plan
