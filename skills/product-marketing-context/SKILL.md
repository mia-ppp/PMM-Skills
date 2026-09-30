---
name: product-marketing-context
description: "When the user wants to create or update their product marketing context document. Also use when the user mentions 'product context,' 'marketing context,' 'set up context,' 'who is my target audience,' 'describe my product,' or wants to avoid repeating foundational information across marketing tasks. Use this at the start of any new project before using other marketing skills. It creates `.agents/product-marketing-context.md` that all other skills reference for product, audience, and positioning context. For creating positioning, see positioning-strategy. For personas and ICP, see buyer-personas."
metadata:
  version: 1.2.0
---

# Product Marketing Context

You help users create and maintain a product marketing context document. This captures foundational positioning and messaging information that other marketing skills reference, so users don't repeat themselves.

The document is stored at `.agents/product-marketing-context.md`.

## Before Starting

**Load the shared reference:** read `../_shared/evidence-gaps.md` (relative to this skill's folder). Label every claim, finding, and number Sourced, Assumed, or Gap. In the context document, label each captured fact: Sourced when the user or a file states it, Assumed when you drafted it from context, Gap when nothing covers it.

## Workflow

### Step 1: Check for Existing Context

First, check if `.agents/product-marketing-context.md` already exists. Also check `.claude/product-marketing-context.md` for older setups. If found there but not in `.agents/`, offer to move it.

**If it exists:**
- Read it and summarize what's captured
- Ask which sections they want to update
- Only gather info for those sections

**If it doesn't exist, offer two options:**

1. **Auto-draft from codebase** (recommended): You'll study the repo: README, landing pages, marketing copy, package.json, etc.: and draft a V1 of the context document. The user then reviews, corrects, and fills gaps. This is faster than starting from scratch.

2. **Start from scratch**: Walk through each section conversationally, gathering info one section at a time.

Most users prefer option 1. After presenting the draft, ask: "What needs correcting? What's missing?"

### Step 2: Gather Information

**If auto-drafting:**
1. Read the codebase: README, landing pages, marketing copy, about pages, meta descriptions, package.json, any existing docs
2. Draft all sections based on what you find. Label every drafted line Sourced (cite the file) or Assumed, and mark empty fields Gap
3. Present the draft and ask what needs correcting or is missing
4. Iterate until the user is satisfied

**If starting from scratch:**
Walk through each section below conversationally, one at a time. Don't dump all questions at once.

For each section:
1. Briefly explain what you're capturing
2. Ask relevant questions
3. Confirm accuracy
4. Move to the next

Push for verbatim customer language: exact phrases are more valuable than polished descriptions because they reflect how customers actually think and speak, which makes copy more resonant.

---

## Sections to Capture

### 1. Product Overview
- One-line description
- What it does (2-3 sentences)
- Product category (what "shelf" you sit on: how customers search for you)
- Product type (SaaS, marketplace, e-commerce, service, etc.)
- Business model and pricing

### 2. Target Audience
- Primary audience plus alternates, each labeled Sourced, Assumed, or Gap. Keep alternates that lack proof; see `../_shared/segment-selection.md`
- Target company type (industry, size, stage)
- Target decision-makers (roles, departments)
- Primary use case (the main problem you solve)
- Jobs to be done (2-3 things customers "hire" you for)
- Specific use cases or scenarios

### 3. Personas (B2B only)
If multiple stakeholders are involved in buying, capture for each:
- User, Champion, Decision Maker, Financial Buyer, Technical Influencer
- What each cares about, their challenge, and the value you promise them

### 4. Problems & Pain Points
- Core challenge customers face before finding you
- Why current solutions fall short
- What it costs them (time, money, opportunities)
- Emotional tension (stress, fear, doubt)

### 5. Competitive Landscape
- **Direct competitors**: Same solution, same problem (e.g., Calendly vs SavvyCal)
- **Secondary competitors**: Different solution, same problem (e.g., Calendly vs Superhuman scheduling)
- **Indirect competitors**: Conflicting approach (e.g., Calendly vs personal assistant)
- How each falls short for customers

### 6. Differentiation
- Key differentiators (capabilities alternatives lack)
- How you solve it differently
- Why that's better (benefits)
- Why customers choose you over alternatives

### 7. Objections & Anti-Personas
- Top 3 objections heard in sales and how to address them
- Who is NOT a good fit (anti-persona)

### 8. Switching Dynamics
The JTBD Four Forces:
- **Push**: What frustrations drive them away from current solution
- **Pull**: What attracts them to you
- **Habit**: What keeps them stuck with current approach
- **Anxiety**: What worries them about switching

### 9. Customer Language
- How customers describe the problem (verbatim)
- How they describe your solution (verbatim)
- Words/phrases to use
- Words/phrases to avoid
- Glossary of product-specific terms

### 10. Brand Voice
- Tone (professional, casual, playful, etc.)
- Communication style (direct, conversational, technical)
- Brand personality (3-5 adjectives)

### 11. Proof Points
- Key metrics or results to cite
- Notable customers/logos
- Testimonial snippets
- Main value themes and supporting evidence

### 12. Goals
- Primary business goal
- Key conversion action (what you want people to do)
- Current metrics (if known)

### 13. Positioning
Written by positioning-strategy. Other skills read it as the source of truth for the position.
- **Statement:** one sentence in the form "[Product] is a [category + one short differentiating phrase] for [segment]."
- **Derivation trace:** Category, Differentiating phrase, Segment, and Trigger (the event that starts the search), each with its source and label
- **Capability table:** every differentiating capability, with what it does for the buyer, proof, buyer voice, and label

messaging-framework builds its capability rows only from this table. If the section is empty, recommend positioning-strategy.

### 14. Persona message map
Written by buyer-personas. messaging-framework starts its persona lines from it.
- **Persona:** role-based name with the buying role in brackets, such as (champion) or (financial buyer)
- **What matters to them:** 1 to 2 short phrases
- **Message:** the core message in 1 to 2 sentences
- **Proof label:** Sourced, Assumed, or Gap for the proof behind the message

---

## Step 3: Create the Document

After gathering information, create `.agents/product-marketing-context.md` with this structure:

```markdown
# Product Marketing Context

*Last updated: [date]*

## Product Overview
**One-liner:**
**What it does:**
**Product category:**
**Product type:**
**Business model:**

## Target Audience
**Primary audience:** [segment] (Sourced / Assumed / Gap)
**Alternate audiences:**
- [segment] (Sourced / Assumed / Gap)
**Target companies:**
**Decision-makers:**
**Primary use case:**
**Jobs to be done:**
-
**Use cases:**
-

## Personas
| Persona | Cares about | Challenge | Value we promise |
|---------|-------------|-----------|------------------|
| | | | |

## Problems & Pain Points
**Core problem:**
**Why alternatives fall short:**
-
**What it costs them:**
**Emotional tension:**

## Competitive Landscape
**Direct:** [Competitor], which falls short because...
**Secondary:** [Approach], which falls short because...
**Indirect:** [Alternative], which falls short because...

## Differentiation
**Key differentiators:**
-
**How we do it differently:**
**Why that's better:**
**Why customers choose us:**

## Objections
| Objection | Response |
|-----------|----------|
| | |

**Anti-persona:**

## Switching Dynamics
**Push:**
**Pull:**
**Habit:**
**Anxiety:**

## Customer Language
**How they describe the problem:**
- "[verbatim]"
**How they describe us:**
- "[verbatim]"
**Words to use:**
**Words to avoid:**
**Glossary:**
| Term | Meaning |
|------|---------|
| | |

## Brand Voice
**Tone:**
**Style:**
**Personality:**

## Proof Points
**Metrics:**
**Customers:**
**Testimonials:**
> "[quote]" ([who])
**Value themes:**
| Theme | Proof |
|-------|-------|
| | |

## Goals
**Business goal:**
**Conversion action:**
**Current metrics:**

## Positioning
**Statement:** [Product] is a [category + one short differentiating phrase] for [segment].

**Derivation trace:**
| Slot | Filled with | Source | Label |
|---|---|---|---|
| Category | | | Sourced / Assumed / Gap |
| Differentiating phrase | | | |
| Segment | | | |
| Trigger | [the event that starts the search] | | |

**Capabilities:**
| Capability | What it does for the buyer | Proof | Buyer voice | Label |
|---|---|---|---|---|
| | | | | Sourced / Assumed / Gap |

## Persona message map
| Persona (buying role) | What matters to them | Message | Proof label |
|---|---|---|---|
| [Role-based name] (champion) | | | Sourced / Assumed / Gap |

## Evidence gaps
| Rank | Item | Label | Why it matters | How to resolve | Owner | Resolve by |
|---|---|---|---|---|---|---|
```

---

## Step 4: Confirm and Save

- Show the completed document
- Ask if anything needs adjustment
- Save to `.agents/product-marketing-context.md`
- Tell them: "Other marketing skills will now use this context automatically. Run `/product-marketing-context` anytime to update it."

---

## Tips

- **Be specific**: Ask "What's the #1 frustration that brings them to you?" not "What problem do they solve?"
- **Capture exact words**: Customer language beats polished descriptions
- **Ask for examples**: "Can you give me an example?" unlocks better answers
- **Validate as you go**: Summarize each section and confirm before moving on
- **Skip what doesn't apply**: Not every product needs all sections (e.g., Personas for B2C)

## Output Rules

- No em dashes in output.
