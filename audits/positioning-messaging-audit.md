# Positioning and messaging workflow audit

Date: 16 October 2026. Baseline: 8babe52, main tracking origin/main. Working tree was clean before this audit. Scope: research-to-positioning-to-messaging-to-sales handoffs; Aiven V3 is the diagnostic artifact.

## Findings

The repository already distinguishes evidence, interpretation, assumptions, personas, competitive/contextual alternatives, opportunity selection, positioning and messaging. Customer Research owns customer evidence and language; market/competitive intelligence own external findings; market-entry owns market choice; ICP owns personas; positioning owns frame/differentiation; messaging owns expression; GTM and execution owners use those artifacts. Context/SSOT contracts preserve provenance and approval. This is not a broken end-to-end architecture.

The most likely weaknesses are at the synthesis and expression boundary:

| Supported observation | Consequence | Focused change |
|---|---|---|
| Positioning required one concise category-plus-capability statement and one segment; no required company/solution level distinction | A beachhead statement can stand in for the broader company repositioning | Optional broad-work company/beachhead architecture and evidence-gated expansion |
| Literal swap rules excluded any claim competitors could also say | Evidence-supported combinations and account-specific operating advantages could disappear, or invite false uniqueness | Buyer-criterion-based comparative test with explicit scope and proof |
| Alternative maps covered strengths and switching costs, but no explicit win/loss decision framework | Competitive facts can remain descriptive instead of shaping sales selection | Compact win conditions with attraction, criterion, advantage, proof, win/loss/disqualification |
| Rich persona fields existed, but committee instructions did not explicitly separate incumbent infrastructure owner from new application outcome owner and budget holder | A data-team relationship could be treated as AI buying access | Conditional cross-team committee split, authority uncertainty and stakeholder agreement |
| Messaging inherited capabilities and persona rows, but lacked explicit pillar-to-buyer-to-alternative-to-proof-to-sales trace | Operational/internal rationale could appear as customer value; persona names could leave copy unchanged | Shared trace and hierarchy comparison; separate internal rationale from applied copy |
| Existing tests emphasized statement form, table rows, hero options and governance, with no broad company repositioning case | Format success could mask strategic-quality gaps | Five fixture-based outcome regressions and rubric examples loaded by the existing harness |

These are instruction/artifact-supported likely causes. No Aiven V3 production invocation trace was found, so this audit does not claim to reconstruct which skill actually caused each line. Prompt framing and final editorial integration could also contribute.

## Historical execution inspected

Historical real-model results exist. `evals/results/20260926-160737/runs.json` contains 38 outputs, including 18 positioning/messaging outputs. `evals/RESULTS.md` reports directional lift for those older revisions. Cached raw positioning-1 and messaging-1 with-skill responses were inspected. Positioning-1 used a complementary compliance frame and marked important comparative assumptions. Messaging-1 inferred additional capabilities such as multi-entity consolidation and approval workflows, and expressed some unsupported competitor limitations. This demonstrates why preserving capability and comparative proof boundaries matters. Those cached outputs lack a precise current skill fingerprint and are not Aiven traces or proof about the new implementation. October 2 and October 16 earlier run directories inspected have empty runs.json files.

## Changes

- `skills/_shared/positioning-messaging-trace.md`: one shared reasoning/handoff contract, comparative territories, company/beachhead/product/expression levels, buyer-relevant advantage, win conditions and narrow-scope boundary.
- `skills/positioning-strategy/SKILL.md`: load shared contract for broad work; one concise statement per applicable level plus full value architecture; scope-aware combination/account advantage test; competitive win conditions.
- `skills/messaging-framework/SKILL.md`: load shared contract; compare broad hierarchies; preserve pillar/buyer/alternative/proof/sales trace; separate internal and applied copy; narrow applied-copy exception.
- `skills/icp-and-buyer-personas/SKILL.md`: conditional application outcome owner, infrastructure owner, sponsor, evaluator and budget split.
- `evals/rubrics/README.md`: concrete strategic-quality examples within the existing four dimensions. The harness loads README plus grounded, decisive, usable and sharp in rubric_text(), so these criteria execute without a loader change.
- `skills/positioning-strategy/evals/fixtures/aiven.md` and `securebuild.md`: explicitly scoped research/synthetic evidence packets, not expected answers.
- Positioning evals 102/103 and messaging evals 101/102/103: Aiven multilevel/relationship advantage, non-AI product-capability advantage, split buying priorities, stronger competitor/operating trade-off, provisional proof and narrow renewal-copy regression.

## Validation

Before edits: lint, reference checks and 35 unit tests passed. After edits: 45 skills passed spec validation; lint passed 347 cases and 1,984 assertions; all fixture/shared references resolved; 35 unit tests passed; git diff --check passed. These checks validate repository integrity and test assembly, not model reasoning quality.

Actual in-session SecureBuild reasoning smoke is saved separately at `scratch/positioning-messaging-audit/securebuild-smoke.md` for review. It uses the updated instructions and does not substitute mock output for strategy.

Real-model evaluation was attempted with the configured PMM_EVALS_API_KEY (value never printed), default model/judge, one trial, $10 budget. Initial sandbox DNS failure was retried with approved network escalation. The service returned HTTP 400 invalid_request_error: credit balance too low to access the Anthropic API. Run `20261016-150221` completed 0 of 12 outputs and spent $0. Its run/spend records remain in ignored evals/results; no scores or pass claims exist. The shared ID filter included five new cases plus existing positioning 101. No mock run was used as reasoning evidence.

## Limits and remaining work

The improvements are reproducible instructions and test cases, with deterministic integrity and an inspected in-session smoke. New real-model behavioral pass rates and lift are not established until service credits permit the scoped run. Aiven V4 is a strategic proposal; buyer preference, budget authority, willingness to pay, comparative workflow outcomes and support economics still require customer evidence. No unrelated architecture change is warranted by this audit.
