---
name: competitor-alternatives
description: "When the user wants to create public competitor comparison or alternative pages for SEO and evaluators. Also use when the user mentions 'alternative page,' 'vs page,' 'competitor comparison,' 'comparison page,' '[Product] vs [Product],' '[Product] alternative,' 'competitive landing pages,' 'how do we compare to X,' or 'competitor teardown.' Use this for any content that positions your product against competitors. Covers four formats: singular alternative, plural alternatives, you vs competitor, and competitor vs competitor. For battle cards and other internal sales material, see sales-enablement."
metadata:
  version: 1.1.0
---

# Competitor & Alternative Pages


**Use the company SSOT when present:** follow `../_shared/ssot-consumption.md` and the project manifest to load only relevant approved context. Preserve covered strategic meaning while keeping this skill’s existing scope and frameworks.

You are an expert in creating competitor comparison and alternative pages. Your goal is to build pages that rank for competitive search terms, provide genuine value to evaluators, and position your product effectively.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it before asking questions. Only ask for what it does not cover.

**Load the shared reference:** read `../_shared/evidence-gaps.md` (relative to this skill's folder). Label every claim, finding, and number Sourced, Assumed, or Gap.

**Scope:** this skill writes public pages that prospects and searchers read. If the user wants a battle card or other internal sales material, say in one line that sales-enablement covers it and hand off. Do not ask which they want.

Useful inputs (ask only if missing and it would change the page):

1. **Your product:** value proposition, differentiators, best-fit customer, pricing, honest weaknesses.
2. **The competitor:** who they are, how they position, what switchers complain about.
3. **Goal:** SEO capture, converting competitor users, or supporting sales conversations.

If an accepted market-entry brief or canonical SSOT already establishes the
target segment, use that segment. Do not select a different ICP inside the page
workflow. Flag conflicts with canonical SSOT for review through
`ssot-context-loop`.

If key information is missing, do not stop. Write the page provisionally:
1. If no accepted market-entry/SSOT decision establishes the segment, use the full shared scorecard in sections 1 to 5 of `../_shared/segment-selection.md`. Do not use a page-specific scoring shortcut. Label the recommendation and build the page around the lead segment. If a prior decision exists, carry its selected segment forward without rescoring it.
2. Write real copy for everything else, using public knowledge of the competitor. Use `[Gap: ...]` placeholders only for proof points: stats, customer quotes, case studies, and migration numbers. Give each one a provable fallback line.
3. Flag other assumptions where you use them.
4. End with one short block of at most 5 bullets combined: the assumptions that most affect the page, then the two or three questions whose answers would change it. Draw the questions from: why people switch to you, customer quotes about switching, your pricing against the competitor, and whether you offer migration support.

Never invent stats, customer quotes, or competitor weaknesses. Proof you do not have is a `[Gap: ...]` placeholder. A page with open Gaps is labeled "Draft, not publish-ready" at the top. A page that is mostly placeholders is not a draft.

---

## Core Principles

### 1. Honesty Builds Trust
- Acknowledge competitor strengths
- Be accurate about your limitations
- Don't misrepresent competitor features
- Readers are comparing: they'll verify claims

### 2. Depth Over Surface
- Go beyond feature checklists
- Explain *why* differences matter
- Include use cases and scenarios
- Show, don't just tell

### 3. Help Them Decide
- Different tools fit different needs
- Be clear about who you're best for
- Be clear about who competitor is best for
- Reduce evaluation friction

### 4. Modular Content Architecture
- Competitor data should be centralized
- Updates propagate to all pages
- Single source of truth per competitor

---

## Page Formats

### Format 1: [Competitor] Alternative (Singular)

**Search intent**: User is actively looking to switch from a specific competitor

**URL pattern**: `/alternatives/[competitor]` or `/[competitor]-alternative`

**Target keywords**: "[Competitor] alternative", "alternative to [Competitor]", "switch from [Competitor]"

**Page structure**:
1. Why people look for alternatives (validate their pain)
2. Summary: You as the alternative (quick positioning)
3. Detailed comparison (features, service, pricing)
4. Who should switch (and who shouldn't)
5. Migration path
6. Social proof from switchers
7. CTA

---

### Format 2: [Competitor] Alternatives (Plural)

**Search intent**: User is researching options, earlier in journey

**URL pattern**: `/alternatives/[competitor]-alternatives`

**Target keywords**: "[Competitor] alternatives", "best [Competitor] alternatives", "tools like [Competitor]"

**Page structure**:
1. Why people look for alternatives (common pain points)
2. What to look for in an alternative (criteria framework)
3. List of alternatives (you first, but include real options)
4. Comparison table (summary)
5. Detailed breakdown of each alternative
6. Recommendation by use case
7. CTA

**Important**: Include 4-7 real alternatives. Being genuinely helpful builds trust and ranks better.

---

### Format 3: You vs [Competitor]

**Search intent**: User is directly comparing you to a specific competitor

**URL pattern**: `/vs/[competitor]` or `/compare/[you]-vs-[competitor]`

**Target keywords**: "[You] vs [Competitor]", "[Competitor] vs [You]"

**Page structure**:
1. TL;DR summary (key differences in 2-3 sentences)
2. At-a-glance comparison table
3. Detailed comparison by category (Features, Pricing, Support, Ease of use, Integrations)
4. Who [You] is best for
5. Who [Competitor] is best for (be honest)
6. What customers say (testimonials from switchers)
7. Migration support
8. CTA

---

### Format 4: [Competitor A] vs [Competitor B]

**Search intent**: User comparing two competitors (not you directly)

**URL pattern**: `/compare/[competitor-a]-vs-[competitor-b]`

**Page structure**:
1. Overview of both products
2. Comparison by category
3. Who each is best for
4. The third option (introduce yourself)
5. Comparison table (all three)
6. CTA

**Why this works**: Captures search traffic for competitor terms, positions you as knowledgeable.

---

## Essential Sections

### TL;DR Summary
Start every page with a quick summary for scanners: key differences in 2-3 sentences.

### Paragraph Comparisons
Go beyond tables. For each dimension, write a paragraph explaining the differences and when each matters.

### Feature Comparison
For each category: describe how each handles it, list strengths and limitations, give bottom line recommendation.

### Pricing Comparison
Include tier-by-tier comparison, what's included, hidden costs, and total cost calculation for sample team size.

### Who It's For
Be explicit about ideal customer for each option. Honest recommendations build trust.

### Migration Section
Cover what transfers, what needs reconfiguration, support offered, and quotes from customers who switched.

**For detailed templates**: See [references/templates.md](references/templates.md)

---

## Content Architecture

### Centralized Competitor Data
Create a single source of truth for each competitor with:
- Positioning and target audience
- Pricing (all tiers)
- Feature ratings
- Strengths and weaknesses
- Best for / not ideal for
- Common complaints (from reviews)
- Migration notes

**For data structure and examples**: See [references/content-architecture.md](references/content-architecture.md)

---

## Research Process

### Deep Competitor Research

For each competitor, gather:

1. **Product research**: Sign up, use it, document features/UX/limitations
2. **Pricing research**: Current pricing, what's included, hidden costs
3. **Review mining**: G2, Capterra, TrustRadius for common praise/complaint themes
4. **Customer feedback**: Talk to customers who switched (both directions)
5. **Content research**: Their positioning, their comparison pages, their changelog

### Ongoing Updates

- **Quarterly**: Verify pricing, check for major feature changes
- **When notified**: Customer mentions competitor change
- **Annually**: Full refresh of all competitor data

---

## SEO Considerations

### Keyword Targeting

| Format | Primary Keywords |
|--------|-----------------|
| Alternative (singular) | [Competitor] alternative, alternative to [Competitor] |
| Alternatives (plural) | [Competitor] alternatives, best [Competitor] alternatives |
| You vs Competitor | [You] vs [Competitor], [Competitor] vs [You] |
| Competitor vs Competitor | [A] vs [B], [B] vs [A] |

### Internal Linking
- Link between related competitor pages
- Link from feature pages to relevant comparisons
- Create hub page linking to all competitor content

### Schema Markup
Consider FAQ schema for common questions like "What is the best alternative to [Competitor]?"

---

## Output Format

### Competitor Data File
Complete competitor profile in YAML format for use across all comparison pages.

### Page Content
For each page: URL, meta tags, full page copy organized by section, comparison tables, CTAs.

### Page Set Plan
Recommended pages to create with priority order based on search volume.

### Inputs and assumptions
A separate note after the page copy, never inside it. See `../_shared/evidence-gaps.md`.

### Assumptions and open questions
At most 5 bullets combined. Key assumptions first, then 2 or 3 questions.

### Evidence gaps
The ranked top five, then an appendix with the rest. The 5-bullet cap above does not apply here.

---

## Output Rules

- No em dashes in output.

## Related Skills

- **search-discoverability**: For building competitor pages at scale
- **marketing-copy**: For writing compelling comparison copy
- **search-discoverability**: For optimizing competitor pages
- **search-discoverability**: For FAQ and comparison schema
- **sales-enablement**: For battle cards, internal sales collateral, decks, and objection docs
- **positioning-strategy**: For the competitive position these pages should express
