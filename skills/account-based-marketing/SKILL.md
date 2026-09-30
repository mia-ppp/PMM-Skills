---
name: account-based-marketing
description: When the user wants to select target accounts, tier them, map buying committees, and coordinate account or account-cluster GTM plays. For campaign assets, see channel skills such as cold-email, email-sequence, copywriting, and social-content.
metadata:
  version: 1.0.0
---

# Account-Based Marketing

Own PMM strategy and orchestration from ICP to account learning. This is not a
generic campaign generator. Read `../_shared/evidence-gaps.md`,
`../_shared/ssot-consumption.md`, and `../_shared/segment-selection.md` when
selecting audiences. Carry accepted canonical ICP and positioning forward.

## Workflow

1. Define objective, scope, timeframe, and decision owner.
2. Consume accepted ICP/segment decisions. If absent, route ICP selection to
   `buyer-personas` or `market-entry-brief`; do not create a competing ICP.
3. Set account inclusion/exclusion criteria using available evidence. Record
   source, date, and missing data. Never invent intent, tools, initiatives,
   executive views, or account pain.
4. Tier accounts and choose 1:1, 1:few, or 1:many according to evidence,
   strategic value, customization capacity, and repeatable shared needs. Mark
   unsupported tier logic as Assumed or Gap.
5. Map known buying-committee roles, likely jobs/triggers/barriers, and unknowns.
   Separate known account evidence from account or cluster hypotheses.
6. Build a contextual message hypothesis from canonical messaging. Select
   relevant approved proof. Do not independently redefine positioning or claims.
7. Plan coordinated plays with owner, audience, timing, objective, handoff, and
   follow-up. Define Marketing, SDR, AE, and CS responsibilities where relevant.
8. Define engagement and business outcome measures, data source, window,
   baseline, and target only where supported. Distinguish influence from
   causality; capture learnings and review account hypotheses.

## Required output

Inputs and assumptions; objective; canonical ICP/message and version; account
selection criteria and evidence; tiering and motion rationale; buying-committee
map; known facts vs hypotheses; account/cluster message and approved proof;
coordinated play table; team responsibilities; measurement; learning plan; and
ranked evidence gaps. **Output quality:** `output-quality-check` verifies these
sections, labeling, evidence traceability, absence of fabricated personalization,
and that hypotheses remain hypotheses.

## Handoffs and governance

Route persona/committee gaps to `buyer-personas`; account systems and routing to
`revops`; measurement instrumentation to `analytics-tracking`; event plays to
`events`; rep talk tracks to `sales-enablement`; execution assets to
`cold-email`, `email-sequence`, `copywriting`, `social-content`, and `paid-ads` as needed.
Do not write those assets here. Final market-facing ABM messaging goes through
`messaging-consistency-audit`. Canon conflicts or repeated evidence that
challenges ICP go to `ssot-context-loop` for review and human approval. ABM does
not change canon.

## Related skills

`buyer-personas`, `market-entry-brief`, `sales-enablement`, `events`,
`cold-email`, `email-sequence`, `copywriting`, `social-content`, `paid-ads`, `revops`,
`analytics-tracking`, `messaging-consistency-audit`, `ssot-context-loop`,
`output-quality-check`.
