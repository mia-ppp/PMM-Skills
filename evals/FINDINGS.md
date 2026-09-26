# PMM-Skills audit: what the evals show

Audit of `mia-ppp/PMM-Skills` as of September 26, 2026. Static analysis only; no model runs yet.

## Summary

- **The library is structurally clean.** 38 of 40 skills pass the spec validator. Two carry warnings.
- **The eval set is large but never executed.** 209 test cases and 1,323 assertions exist with no runner. Nothing proves any skill beats a plain prompt.
- **One in five assertions measures template compliance, not quality.** These inflate lift against a baseline by construction.
- **Routing is the biggest untested risk.** 40 descriptions compete for every request, and several pairs overlap heavily.
- **Repo hygiene undercuts the credential.** Template placeholders and mismatched names are visible on first click.

## 1. Structure

| Check | Result |
|---|---|
| Spec validator (`validate-skills.sh`) | 38 pass, 2 warn, 0 fail |
| `copy-editing` | 508 lines, over the 500-line guideline |
| `marketing-psychology` | Description has no "for X, see Y" scope boundary |
| Skills reading `product-marketing-context` first | 40 of 40 |

**Action:** move `copy-editing` detail into `references/`. Add a scope line to `marketing-psychology`.

## 2. Eval coverage

- 33 of 40 skills have `evals/evals.json`. About 6 cases and 40 assertions per skill.
- **No evals:** `aso-audit`, `community-marketing`, `competitor-profiling`, `directory-submissions`, `image`, `lead-magnets`, `video`.
- **Zero of 209 cases include input files.** Prompts point at `example.com` URLs the agent cannot read. Outputs will be generic advice, so graders reward plausible structure over real analysis.

**Action:** add a `fixtures/` folder with 5 to 10 real pages, briefs, and transcripts. Point audit-style evals at them.

## 3. Assertion quality

Classification of all 1,323 assertions by keyword:

| Type | Share | Example |
|---|---|---|
| Content or judgment | ~74% | "Notes message match between ads and landing page" |
| Names the skill's own framework | ~9% | "Applies Pricing Page CRO framework" |
| Format or section headers | ~8% | "Output has Quick Wins section" |
| Numeric or count | ~5% | "Provides 2-3 headline alternatives" |
| Checks for context file | ~4% | "Checks for product-marketing-context.md" |

- **About 20% check process, not outcome.** A baseline agent fails these by definition, so they manufacture lift.
- **Worst offenders:** `product-marketing-context` (41%), `site-architecture` (40%), `pricing-strategy` (32%).
- **Missing entirely:** negative assertions. Nothing checks for invented stats, fake case studies, or generic filler.

**Action:** for each skill, keep one format check and replace the rest with outcome checks. Add two negative assertions per skill ("Does not invent conversion benchmarks").

## 4. Routing risk

Descriptions average 634 characters, about 25,000 characters total competing for every request. Word overlap between description pairs:

| Pair | Overlap | Likely confusion |
|---|---|---|
| `form-cro` / `signup-flow-cro` | 0.38 | "Our signup form converts badly" |
| `onboarding-cro` / `signup-flow-cro` | 0.34 | Trial activation requests |
| `ad-creative` / `paid-ads` | 0.30 | "Write LinkedIn ads" |
| `competitor-profiling` / `competitor-alternatives` | 0.29 | "Analyze competitor X" |
| `free-tool-strategy` / `lead-magnets` | 0.28 | "Build a calculator for leads" |

**Action:** run `harness.py route` first. It reuses all 209 prompts as labeled routing tests at near-zero cost. Fix the top five confusion pairs before tuning skill bodies.

## 5. Repo hygiene

- **README install block still reads `[your-username]/[your-repo]`.**
- **`AGENTS.md` names the repo `mia-ppp/marketingskills`**, not `PMM-Skills`. It references `.claude-plugin/marketplace.json` and `VERSIONS.md`, neither of which exists.
- **Tool counts drift.** `AGENTS.md` says 51 CLI tools; `tools/clis/` holds 62.
- **Scope mismatch.** The library covers growth marketing broadly: SEO, CRO, ads, video. There is no dedicated positioning, messaging, persona, or win/loss skill.

**Action:** fix the placeholders this week. They are the first thing a hiring manager sees.

## Eval plan

1. `lint` to confirm baseline coverage. Free.
2. `route` across all 209 prompts. Fix descriptions for the top confusion pairs.
3. `run` on 5 core skills with 3 trials each: `copywriting`, `page-cro`, `competitor-alternatives`, `customer-research`, `launch-strategy`.
4. Cut or rewrite any skill showing under 5 points of lift. Delete assertions the report flags as non-discriminating.
5. Publish the lift table in the README. Measured lift per skill is the proof point most skill libraries lack.
