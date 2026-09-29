# Launch stages

Skills that plan, build, or check a launch load this file and follow it. It defines the four-rung launch chain, what each rung hands to the next, and the gate between them.

Evidence labels follow `evidence-gaps.md`. Segment choices follow `segment-selection.md`.

## The chain

| Rung | Name | Skills | Handoff artifact |
|---|---|---|---|
| 1 | Market decision | `market-entry-brief`, fed by `product-marketing-context`, `customer-research`, `competitor-profiling` | Market-entry brief |
| 2 | Position and canon | `positioning-strategy`, then `messaging-framework`, then a company messaging rule book | Locked canon |
| 3 | Assets | `copywriting`, SEO skills, ads skills, `sales-enablement`, each grounded in the canon | On-canon launch assets |
| 4 | Guardrail and learn | `launch-readiness-check`, then the eval harness (`evals/`) | Go/no-go scorecard |

- **Run the rungs in order.** A rung starts only when the gate before it passes.
- **Go back one rung when a gate fails.** Fix the artifact that failed, then re-run the gate. Never patch a later artifact to hide an earlier gap.
## Rung 1. Market decision

Decide where to enter before anyone writes a line of positioning.

**Entry criteria**
- A brief names the product, the goal, and the decision owner.
- `product-marketing-context` has run, or the context gaps are listed as Gap.

**Inputs**
- Product marketing context for the assignment.
- Customer evidence from `customer-research`: interviews, reviews, win-loss, churn reasons.
- Alternatives from `competitor-profiling`: competitive and contextual.
- Segment list, sizing, and scores from `segment-selection.md` sections 1 to 5.

**Artifact: market-entry brief** (produced by `market-entry-brief`)
- A one-line Go, Explore, or Pass recommendation.
- Market definition and boundaries.
- TAM, SAM, and SOM, each figure labeled.
- Buyer delta: current-market buyer vs new-market buyer.
- Channel and regulatory constraints.
- Top three entry risks, ranked by impact.
- Evidence gaps (top five), ranked by impact on the recommendation.

**Gate to Rung 2**
- The recommendation is Go, or Explore with the settling test complete.
- The market definition names a specific segment or region. "Everyone" or "all businesses" fails.
- Every number traces to Sourced, Derived, or Assumed, per `segment-selection.md` section 7.
- Every top-five gap has an owner and a resolve-by milestone.
- The decision owner has accepted the recommendation.

## Rung 2. Position and canon

Turn the market decision into one source of truth that every asset copies.

**Entry criteria**
- The Rung 1 gate has passed.
- The market-entry brief is the input. No skill in this rung re-picks the segment.

**Sequence**
1. `positioning-strategy`: one statement of 25 words or fewer, derivation trace, capability table, trade-offs, stress tests.
2. `messaging-framework`: capability table with proof and buyer voice, recommended hero line, persona translations, boilerplate, language rules.
3. Company messaging rule book (for example `moonpay-messaging`): canon, approved numbers, claims register, terminology, audience overlays, changelog.

**Artifact: locked canon**
- Positioning statement and its derivation trace.
- Pillars, each with a swap-test result.
- Approved numbers table: wording, scope, source, notes.
- Claims register: Approved, Conditional (with required qualifier), Banned.
- Terminology and voice rules.
- A canon version in `vYYYY-MM-DD` form and a changelog entry.

**Gate to Rung 3**
- The statement passes the swap, proof, rep, buyer, and consistency tests in `positioning-strategy`.
- Every capability row has proof or a named Gap. None was dropped for lacking proof.
- The consistency check in `segment-selection.md` section 6 shows no unresolved mismatch.
- Every approved number carries its scope and source.
- The canon owner has locked the version. Later changes bump the version.

## Rung 3. Assets

Produce launch assets that say only what the canon allows.

**Entry criteria**
- The Rung 2 gate has passed.
- Each asset brief names its audience overlay, channel, and the canon version it builds on.

**Skills** (pick what the launch tier needs)
- Copy: `copywriting`, `email-sequence`, `cold-email`, `social-content`, `copy-editing`.
- SEO: `seo-audit`, `ai-seo`, `programmatic-seo`, `schema-markup`, `competitor-alternatives`.
- Ads: `paid-ads`, `ad-creative`.
- Sales enablement: `sales-enablement`.
- Plan and sequence: `launch-strategy`.
- Localization: `localization-claims`, run on every asset for the target market before the gate.

**Artifact: on-canon launch assets**
- The asset itself.
- A claim sources table after each asset: claim, canon row, label.
- `[Gap: ...]` placeholders with a provable fallback line under each, per `evidence-gaps.md`.
- "Draft, not publish-ready" at the top of any asset with an open Gap.

**Gate to Rung 4**
- Every claim maps to an Approved or Conditional canon row. Conditional claims keep their qualifier.
- No Banned claim appears, and no competitor is named in customer-facing copy unless the canon allows it.
- The rule book's review mode returns "Ready" or "Ready after Fix items," with the Fix items closed.
- Every asset's canon stamp matches the current locked version.
- `localization-claims` shows no open regulatory Gap stated as fact in any asset for the target market.

## Rung 4. Guardrail and learn

Decide go or no-go, then feed what the launch taught back into the canon and the skills.

**Entry criteria**
- The Rung 3 gate has passed for every asset in the launch tier.
- KPIs and targets are set, with baselines labeled Sourced, Assumed, or Gap.

**Sequence**
1. `launch-readiness-check`: grades every asset against the company canon with the rule book's Block, Fix, and Suggest review.
2. Eval harness (`evals/`): measures whether the skills that produced the assets beat the no-skill baseline and route correctly.

**Artifact: go/no-go scorecard**
- Verdict: Ready, Ready after fixes, or Not ready. Any Block in any asset means Not ready.
- Rollup: total assets, flags by severity, and the top blocking issues.
- One row per launch asset: type, canon stamp, flag counts, asset verdict.
- Every flag cites the file and rule ID it broke.
- Evidence gaps (top five), ranked by impact on the verdict.

**Gate: launch**
- The verdict is Ready, or Ready after fixes with every Fix item closed.
- No asset carries a stale canon stamp.
- No top-five gap undermines a claim that customer-facing copy states as fact.

**After launch**
- Review-mode drift flags feed the next canon version and changelog entry.
- Skill problems found during the launch are reported separately, after the run, per `AGENTS.md`. Skills are never edited mid-run.
- The eval harness runs only when the user asks. The launch gate never waits on it.

## Handoff contract

Every artifact that moves between rungs carries the same header and labels. A receiving rung rejects an artifact that is missing either.

**Header block** (top of every artifact)

```
Artifact: [market-entry brief / locked canon / asset name / go-no-go scorecard]
Rung: [1-4]
Canon: v[YYYY-MM-DD]   (Rung 1 writes "Canon: pre-canon")
Built from: [input artifacts and their canon stamps]
```

**Canon version stamp**
- Every artifact from Rung 2 on ends with `Canon vYYYY-MM-DD`.
- A new canon version marks every downstream artifact stale. Re-run the Rung 3 gate on stale assets before Rung 4.
- An artifact built on two canon versions fails the gate. Rebuild it on one.

**Evidence labels**
- Every claim, segment, and number carries one label: Sourced, Assumed, or Gap, as defined in `evidence-gaps.md`.
- Every artifact opens with the "Inputs and assumptions" note, or carries it after the copy for customer-facing assets.
- Labels travel with the claim. A later rung never upgrades Assumed or Gap to Sourced without adding the source.
- A resolved Gap names the source that closed it and the rung where it closed.
