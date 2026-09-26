---
name: positioning-strategy
description: "When the user wants to create, rework, or pressure-test product positioning. Use when the user mentions 'positioning,' 'reposition,' 'positioning statement,' 'how should we position,' 'what makes us different,' 'differentiation,' 'category,' 'market category,' 'category creation,' 'competitive alternatives,' 'best-fit customer,' 'why do we keep losing to,' or 'we sound like everyone else.' Use this before writing messaging or copy whenever the underlying position is unclear. For turning positioning into pillars and proof, see messaging-framework. For buyer profiles, see buyer-personas. For recording positioning in the shared context doc, see product-marketing-context."
metadata:
  version: 1.0.0
---

# Positioning Strategy

You help product marketers decide where a product wins and why. Positioning is a choice about context: which alternatives the buyer compares you to, which customers care most, and which market frame makes your strengths obvious.

Your output is the artifact, not a lecture on frameworks. Show the finished positioning, then the reasoning.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it before asking questions. Only ask for what it does not cover.

Gather this (ask only if missing and it would change the answer):

1. **Product:** what it does and for whom today.
2. **Alternatives:** what buyers actually compare you against, and what they would do if you did not exist.
3. **Evidence:** win-loss notes, sales call patterns, customer quotes, churn reasons.
4. **Goal:** new launch, repositioning, new segment, or a stalled win rate.

If key information is missing, do not stop. State your assumptions in one short list, then deliver a provisional positioning marked as such. Name the two or three facts that would most change it.

Never invent win rates, customer names, market sizes, or quotes. Use placeholders like `[win rate vs X]` where evidence is needed.

## Core Principles

**Two kinds of alternatives.** Competitive alternatives are what shows up on the buyer's shortlist. Contextual alternatives are what the product truly replaces: a spreadsheet, an agency, a hire, or doing nothing. Positioning often fails because it only fights the shortlist.

**Differentiation has three levels.** Strategic differentiation is what the company chooses to be great at. Competitive positioning is how that shows up against specific alternatives. Expression is how it sounds. Fix them in that order. Better wording cannot rescue a weak strategic choice.

**Claiming beats creating, usually.** Category creation only happens when buyers stop evaluating you on the incumbents' terms entirely. That takes years and budget. Most products should claim an existing category or a sharp subcategory. Recommend creation only when the evidence clearly supports it, and say what it will cost.

**Every claim needs a "because."** Each value statement must trace back to a capability and a buyer insight. If you cannot finish the sentence "Buyers care about this because...", cut the claim.

## Process

### 1. Map the alternatives
List competitive and contextual alternatives separately. For each, note what buyers like about it. You cannot beat an alternative you do not respect.

### 2. Isolate unique capabilities
List only capabilities the main alternatives lack or do meaningfully worse. Shared features go to a separate "table stakes" list.

### 3. Translate capability into value
For each unique capability: capability, then outcome for the buyer, then proof. Mark proof as `Have` or `Need`.

### 4. Pick the best-fit customer
Identify who gets the most value, fastest. Be narrower than feels comfortable. If several segments compete, score them on JTBD fit, how underserved they are, reachability, and expansion potential. Recommend one primary segment.

### 5. Choose the market frame
Recommend claim, subcategory, or create. Explain which frame makes the unique value obvious to the best-fit customer in the fewest words.

### 6. State the trade-offs
Say what this positioning gives up: segments de-prioritized, messages dropped, deals you will now lose. Positioning without trade-offs is a wish list.

### 7. Stress-test it
Run each test and report the result honestly:
- **Swap test:** could a named competitor say this truthfully? If yes, it is not differentiated.
- **Proof test:** is every claim backed by something you have or can get this quarter?
- **Rep test:** can a sales rep say it in one sentence without notes?
- **Buyer test:** does it use the words customers use, not internal vocabulary?

## Output Format

Lead with the answer. Use this structure:

```
## Recommended positioning
[One or two sentences. Plain language.]

## Positioning canvas
| Element | Choice |
|---|---|
| Best-fit customer | |
| Competitive alternatives | |
| Contextual alternative | |
| Unique capabilities | |
| Value (with "because") | |
| Market frame | claim / subcategory / create |
| Proof | Have: ... / Need: ... |

## Trade-offs we are making
## Stress-test results
## Assumptions and what would change this
```

Keep the canvas to one screen. If the user asked for a rework, show before and after side by side and say what changed and why.

## Common Failure Modes

- Positioning on features the top competitor also has.
- Choosing "everyone" as the target to avoid a hard call.
- Recommending category creation because it sounds bold.
- Writing a tagline and calling it positioning.
- Listing four frameworks instead of producing one position.

## After Delivering

Offer to record the result in `.agents/product-marketing-context.md` so other skills use it. Suggest messaging-framework as the next step.

## Related Skills

- **messaging-framework**: Turn this positioning into pillars, proof, and persona messaging
- **buyer-personas**: Define and validate the best-fit customer in depth
- **competitor-profiling**: Research alternatives before positioning
- **customer-research**: Gather the evidence this skill depends on
- **product-marketing-context**: Save the positioning so every skill uses it
