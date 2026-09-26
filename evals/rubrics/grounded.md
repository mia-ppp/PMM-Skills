# Grounded

**Question:** Does the output stay true to the provided context, and does it say what it assumed?

## Great (2)
- Uses specific details from the prompt or input files.
- States every assumption explicitly, as a list or inline.
- When information is missing, ends with the questions whose answers would change the recommendation.

## OK (1)
- Uses the context, but some advice would fit any company.
- Makes a key assumption without flagging it, but the rest is grounded.
- Builds a recommendation on a guess that is plausible but unstated.
- Key information is missing, and it answers without asking the clarifying questions it needed.

## Bad (0)
- Invents stats, pricing tiers, customers, quotes, or case studies and presents them as fact.
- Infers product capabilities, customer pain points, or segment knowledge without saying so.
- Ignores or contradicts key details the user gave.

## Edge cases
- Answering before asking is fine if assumptions are stated. See the provisional rule.
- Clearly marked placeholders ("[customer name]", "[X]% lift"): fine. Example stats in draft copy count as placeholders only if bracketed or labeled as examples. Otherwise they are invented.
- Common benchmarks framed as rough norms ("typically 3-5%"): fine. Precise unsourced stats presented as fact: not fine.
- Closing questions are required only when information is missing.
- If there is no product marketing context and the output is full of specifics, ask where they came from. Unexplained specifics are Bad.

## Anchors

| Tier | Sample | Skill (config) | Excerpt | Why |
|---|---|---|---|---|
| Great | A-02 | positioning-strategy (with skill) | I did not find a `.agents/product-marketing-context.md`, so this is provisional based on what you told me. Assumptions made:<br>1. **Vanta/Drata collect raw evidence but don't draft audit-narrative text from engineering activity.** If they already do this well, your differentiation collapses to "we do it better," which is a much weaker, feature-level claim [...]<br>2. **The stalled deals are mostly with existing Vanta/Drata customers**, not prospects evaluating GRC tools for the first time. | Assumptions and trade-offs clearly stated. |
| OK | A-03 | messaging-framework (baseline) | 2. **Who complains about Fivetran that becomes your customer?** (Common ones: unpredictable/expensive MAR-based pricing, black-box transformations, support that's slow at scale, limited customization)<br>If your wedge is **pricing predictability**:<br>- "Transparent, predictable pricing" (vs. Fivetran's MAR surprise-bill reputation) | Leans on pricing because it's a Fivetran weakness, with no evidence it's the product's strength. |
| Bad | A-08 | positioning-strategy (baseline) | **Positioning line:** "Vanta tells you what evidence you're missing. We write it."<br>The wedge: **Vanta/Drata's biggest complaint in every G2 review is "still requires tons of manual evidence collection from engineers."**<br>Ask: "How many engineer-hours did your last audit cycle burn on evidence collection?" That number is usually 40-100+ hours. | Assumes the product's core capabilities without saying so. |
