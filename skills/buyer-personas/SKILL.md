---
name: buyer-personas
description: "When the user wants to create, research, validate, or refresh buyer personas, ICP profiles, or buying committee maps. Use when the user mentions 'persona,' 'buyer persona,' 'ICP,' 'ideal customer profile,' 'who is our buyer,' 'buying committee,' 'decision maker,' 'champion,' 'persona interviews,' 'segment,' 'which segment should we target,' 'segmentation,' or 'anti-persona.' Use this whenever audience assumptions drive a positioning, messaging, or campaign decision. For interview synthesis across many sources, see customer-research. For using personas in positioning, see positioning-strategy. For recording personas in the shared context doc, see product-marketing-context."
metadata:
  version: 1.1.0
---

# Buyer Personas

You build personas that change decisions. A persona earns its place only if it changes what the team says, where it shows up, or who it sells to. Demographic filler does not.

Deliver the personas themselves, not a template for making them.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it before asking questions.

Find out which mode applies:
- **Evidence mode:** the user has interviews, call notes, CRM data, win-loss, or surveys. Build from those.
- **Hypothesis mode:** little or no research. Draft personas as clearly labeled hypotheses, then give a plan to validate them.

If key information is missing, answer provisionally: give your best personas, label assumptions where you use them, and end with one short block of at most 5 bullets combined: the assumptions that most affect the personas, then the two or three questions that would change them. The validation plan's interview questions do not count toward the 5. Open with the recommended segment. Do not restate the brief.

Label every persona attribute as `Evidence` or `Hypothesis`. Never present a guess as research. Never invent quotes. If you use a quote, it must come from the user's material.

## Core Principles

**Start qualitative, validate quantitatively.** Interviews reveal the real segments and language. Surveys then show how many buyers self-select into each. Doing it in the other order produces tidy but wrong personas.

**Four attributes matter most.** Background, pain points, discovery channels, and evaluation process. These drive messaging, channel, and sales decisions. Age and hobbies rarely do.

**B2B buys by committee.** Map the user, champion, decision maker, financial buyer, and technical influencer. Each needs a different reason to say yes.

**Name the anti-persona.** Say who looks like a fit but is not, and why. This saves sales time and sharpens messaging.

## Process

### 1. Segment before you profile
If there are several possible segments, score each from 1 to 5 on these criteria: size, JTBD fit, how underserved they are, differentiation, reachability, acquisition ease, required effort, engagement, stickiness, expansion likelihood, and LTV potential. Recommend a primary segment. Treat vertical prioritization as an investment decision, and say so when that applies.

### 2. Profile each persona
Cover: role and background, trigger events, pain points in their words, discovery channels, evaluation process, objections, what success looks like to them, and their role in the buying committee.

### 3. Map the buying committee
Show who starts the purchase, who blocks it, who signs, and what each needs to hear.

### 4. Define the anti-persona
Describe the look-alike buyer who churns, stalls, or costs too much to serve.

### 5. Plan validation
For hypothesis-mode personas, write the five to eight interview questions that would confirm or kill each one. Cover role, awareness, evaluation, requirements, alternatives considered, and the buying committee. End with: "If you were CEO, what would you do to compete better?" Suggest a short survey to size each segment afterward.

## Output Format

```
## Recommended primary segment
[Choice + one-line reason] (include scoring table if segments were compared)

## Persona: [Role-based name, not a cute alias]
| Attribute | Detail | Source |
|---|---|---|
| Background | | Evidence / Hypothesis |
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
- Hypotheses presented as findings.
- Too many personas. Three is usually enough for one product.
- Personas that do not change any decision.
- Skipping the buying committee in B2B.

## After Delivering

Offer to save personas to the Personas section of `.agents/product-marketing-context.md`. Suggest positioning-strategy or messaging-framework as next steps.

## Output Rules

- No em dashes in output.

## Related Skills

- **customer-research**: Gather and synthesize the interviews personas depend on
- **positioning-strategy**: Use the primary persona as the best-fit customer
- **messaging-framework**: Translate messaging for each persona
- **sales-enablement**: Build persona-specific talk tracks and objection handling
- **product-marketing-context**: Save personas so every skill uses them
