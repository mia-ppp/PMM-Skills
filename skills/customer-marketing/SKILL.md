---
name: customer-marketing
description: When the user wants a PMM-led post-sale motion for onboarding, adoption, value realization, retention, cancellation-reason synthesis, win-back, expansion, advocacy, references, case studies, champion development, or customer launches. For billing operations, route to the billing/CS owner; for customer research, see customer-research.
metadata:
  version: 1.0.0
---

# Customer Marketing

Orchestrate customer-facing PMM programs across onboarding, adoption, value
realization, expansion, and advocacy. This skill owns the objective, audience,
message brief, proof plan, coordination, and learning. It does not own Customer
Success operations or final channel assets.

## Activation and commercial boundaries

`product-activation` owns first-value definitions and experience briefs; this skill orchestrates post-sale cohort programs with Product/CS.
`upgrade-conversion` owns in-product upgrade eligibility/timing and `pricing-strategy` owns commercial terms. Expansion campaigns consume those approved decisions.

## Retention and win-back mode

Read [retention briefs](references/retention-programs.md) for cancellation-reason synthesis, cohort hypotheses, retained-value measurement and learning loops.
Own value realization, respectful retention briefs and win-back triggers. Preserve easy cancellation and consent; never invent save offers, discounts or roadmap promises.
Billing retries, payment-provider configuration and access management route to operational owners. PMM may brief truthful payment-recovery communication but does not run billing.
Read [customer review programs](references/customer-reviews.md) when reviews support advocacy; no coerced or fabricated reviews.


## Before planning

Read `../_shared/evidence-gaps.md` and `../_shared/ssot-consumption.md`.
Load the project manifest's relevant approved context and record sources used.
Read `../_shared/segment-selection.md` only when choosing audiences; inherit
accepted segment decisions without redefining canonical ICP.

## Workflow

1. Choose one primary objective: adoption, retention support, expansion,
   advocacy, reference creation, or customer evidence collection.
2. Define eligible customer cohort using evidence such as lifecycle, product
   usage, account tier, persona, use case, or documented opportunity. Do not
   infer satisfaction, readiness, or expansion potential.
3. Identify customer need, desired action, barriers, owner, consent, timing, and
   appropriate CS/Sales coordination. Keep any unsupported rationale labeled.
4. Build the canonical message brief and select approved proof. Case study and
   outcome claims require customer permission and source verification.
5. Route email to `email-sequence`, community coordination to
   `community-marketing`, reference materials or customer-facing sales proof to
   `sales-enablement`, and other assets to their channel owner.
6. Define cohort-level leading indicators and outcomes with source, owner, and
   window. Record learning and evidence for reuse.

## Required output

Inputs and assumptions; objective and cohort; eligibility/evidence; customer
value and intended action; message/proof brief; cross-functional roles; asset
handoffs; measurement; consent/readiness gaps; and ranked evidence gaps.
**Output quality:** `output-quality-check` can verify objective/cohort fit,
evidence labels, readiness safety, proof/consent gaps, clear owners, measures,
and explicit handoffs.

## Boundaries and feedback

- Retention programs belong here; billing operations, payment retries, provider configuration and access management belong to external billing/CS operations.
- `community-marketing` owns community design, member engagement, and community
  advocate programs. This skill may define a customer-community objective and
  hand it off.
- `customer-research` owns research design and evidence synthesis, including
  the reusable VoC language bank. Route collected quotes/feedback there.
- `revops` owns lifecycle definitions, CRM automation, routing, and revenue
  process. `analytics-tracking` owns instrumentation.
- Route any proposed canon change through `ssot-context-loop`; do not edit SSOT.
  Customer campaigns and case studies are market-facing and should pass
  `messaging-consistency-audit` after `output-quality-check`.

## Related skills

`community-marketing`, `customer-research`,
`email-sequence`, `sales-enablement`, `revops`, `analytics-tracking`,
`messaging-consistency-audit`, `ssot-context-loop`, `output-quality-check`.
