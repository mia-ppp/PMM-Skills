# Product Marketing Skills for Claude Code and Codex

45 open-source skills connecting research, positioning, messaging, and execution.

[![PMM Skills workflow: company inputs and research feed shared context, which supports strategy, go-to-market, execution, and quality review. Strategy updates require human approval.](assets/pmm-system.gif)](assets/pmm-system@2x.png)

<a id="why-pmm-skills"></a>
I built PMM Skills to connect work that usually gets done in separate documents and conversations: customer research, competitive intelligence, positioning, go-to-market planning, launches, and sales enablement.

They cover win/loss, objection intelligence, ICP and buyer personas, pricing, and go-to-market strategy.

The skills work from shared company context. Research keeps evidence separate from assumptions. Approved positioning carries through to the materials buyers see. Changes to that strategy require your approval.

[Quick start](#quick-start) · [Capability map](#capability-map) · [Evaluation results](evals/RESULTS.md)

## Quick start

1. **Fork** this repository.
2. **Clone** it into the project where you want to use the skills:

   ```bash
   git clone https://github.com/<your-username>/PMM-Skills.git
   ```

3. **Install** the skills for your agent:

   ```bash
   # Claude Code
   mkdir -p .claude/skills && cp -R PMM-Skills/skills/* .claude/skills/

   # Codex
   mkdir -p .agents/skills && cp -R PMM-Skills/skills/* .agents/skills/
   ```

These commands copy every skill folder plus `_shared/`, which the skills depend on. If your skills folder already has PMM skills or `_shared/`, review those files first, because `cp -R` replaces matching files.

Start your agent in the project and try:

```text
Use product-marketing-context to review these materials for [the decision I need to make].
Show what we know, what we're assuming, and what needs research or approval before we proceed.
```

Start from the decision you need to make. You don't need to run every skill.

<a id="example-workflows"></a>
## Start with a task

| If you need to... | Start here |
|---|---|
| Understand a market or competitor | `market-intelligence` or `competitor-profiling` |
| Decide who to serve and what to say | `icp-and-buyer-personas`, then `positioning-strategy` |
| Check whether existing materials still tell the right story | `messaging-consistency-audit` |

For example:

> Compare our website, sales deck, and outbound emails with our approved positioning. Flag contradictions and unsupported claims. Recommend changes for review.

Longer chains for market entry, launches, evidence feedback, events, and ABM are in [example workflows](docs/workflows.md).

<a id="how-the-system-works"></a><a id="shared-context-and-approval"></a><a id="evidence-and-segment-decisions"></a>
## How shared context works

Research, positioning, and execution should stay connected as the company learns.

`product-marketing-context` reviews the materials you have and identifies what is missing. `ssot-context-loop` manages approved strategy and proposed updates.

- **Evidence stays identifiable.** Findings, interpretations, assumptions, and gaps are kept distinct.
- **Strategy changes require approval.** New research can inform a proposed change. It cannot silently replace approved positioning.
- **Related materials can be reviewed together.** When positioning changes, the system helps identify messaging and assets that need another look.

Read the [shared-context specification](skills/ssot-context-loop/references/ssot-spec.md). Evidence labels are defined in the [evidence contract](skills/_shared/evidence-gaps.md), and segment scoring in the [segment-selection framework](skills/_shared/segment-selection.md).

## Three separate reviews

| Review | Question it answers | What happens next |
|---|---|---|
| [output-quality-check](skills/output-quality-check/SKILL.md) | Does the artifact meet the requirements of the skill that produced it? This read-only check includes required shared standards; missing verification evidence remains UNVERIFIABLE. | Route corrections to the originating skill. |
| [messaging-consistency-audit](skills/messaging-consistency-audit/SKILL.md) | Does market-facing messaging match applicable SSOT and stay consistent across the supplied assets? Legitimate channel variation is allowed. | Route asset corrections to owners; suspected canon issues to SSOT review; inspect corrected assets in re-audit. |
| [launch-readiness-check](skills/launch-readiness-check/SKILL.md) | Is the launch ready to proceed under applicable canon and stricter restrictions? This final go/no-go check includes review coverage. | Hold launch-wide clearance for blockers or unreviewed required assets. |

## Evaluation and benchmarks

**Do the skills improve the work?**

The evaluation harness runs the same tasks with and without skills, then scores the outputs against defined criteria. Separate automated checks catch broken requirements and regressions.

An early comparison covered 19 prompts across four skills, with one trial per condition:

| Use of supplied context | With skills | Without skills |
|---|---:|---:|
| Grounded score, out of 2 | 1.68 | 0.53 |

This score measures whether outputs use the supplied information and make assumptions explicit. It does not establish independent factual accuracy.

These are early, directional results. The AI evaluator's agreement with human grades remained below the calibration target, and this run does not establish performance across all 45 skills.

[Evaluation methodology](evals/README.md) · [Results and limitations](evals/RESULTS.md)

<a id="what-you-can-do"></a>
## Capability map

The portfolio contains **45 standalone skills**. Skills are installed as sibling folders so their shared references resolve. Open a skill to see its inputs, output requirements, and handoffs.

The diagram shows capabilities, not one directory per label. `market-intelligence` owns Market intelligence, Category intelligence, and Emerging opportunities through its modes. `competitor-profiling` owns Competitive landscape, Competitor profiling, and Competitive signals through its modes. The links below map the architecture to invocable skills.

| Architecture area | Skills |
|---|---|
| Customer Intelligence | [customer-research](skills/customer-research/SKILL.md), [win-loss-intelligence](skills/win-loss-intelligence/SKILL.md), [objection-intelligence](skills/objection-intelligence/SKILL.md) |
| Market Intelligence | [market-intelligence](skills/market-intelligence/SKILL.md) |
| Competitive Intelligence | [competitor-profiling](skills/competitor-profiling/SKILL.md) |
| PMM Context / SSOT | [product-marketing-context](skills/product-marketing-context/SKILL.md), [ssot-context-loop](skills/ssot-context-loop/SKILL.md) |
| PMM Strategy | [market-entry-brief](skills/market-entry-brief/SKILL.md), [icp-and-buyer-personas](skills/icp-and-buyer-personas/SKILL.md), [positioning-strategy](skills/positioning-strategy/SKILL.md), [messaging-framework](skills/messaging-framework/SKILL.md), [pricing-strategy](skills/pricing-strategy/SKILL.md) |
| Go-to-Market | [go-to-market-strategy](skills/go-to-market-strategy/SKILL.md), [market-entry-orchestration](skills/market-entry-orchestration/SKILL.md), [launch-strategy](skills/launch-strategy/SKILL.md), [account-based-marketing](skills/account-based-marketing/SKILL.md), [events](skills/events/SKILL.md), [customer-marketing](skills/customer-marketing/SKILL.md), [partner-marketing](skills/partner-marketing/SKILL.md), [product-communications](skills/product-communications/SKILL.md) |
| Execution | [sales-enablement](skills/sales-enablement/SKILL.md), [marketing-copy](skills/marketing-copy/SKILL.md), [cold-email](skills/cold-email/SKILL.md), [email-sequence](skills/email-sequence/SKILL.md), [social-content](skills/social-content/SKILL.md), [paid-ads](skills/paid-ads/SKILL.md), [content-strategy](skills/content-strategy/SKILL.md), [search-discoverability](skills/search-discoverability/SKILL.md), [website-buyer-journey](skills/website-buyer-journey/SKILL.md), [competitor-alternatives](skills/competitor-alternatives/SKILL.md) |
| Growth | [acquisition-conversion](skills/acquisition-conversion/SKILL.md), [product-activation](skills/product-activation/SKILL.md), [upgrade-conversion](skills/upgrade-conversion/SKILL.md), [community-marketing](skills/community-marketing/SKILL.md), [referral-program](skills/referral-program/SKILL.md), [buyer-resources](skills/buyer-resources/SKILL.md) |
| Measurement | [analytics-tracking](skills/analytics-tracking/SKILL.md), [marketing-experimentation](skills/marketing-experimentation/SKILL.md), [revops](skills/revops/SKILL.md) |
| Review & Governance | [output-quality-check](skills/output-quality-check/SKILL.md), [messaging-consistency-audit](skills/messaging-consistency-audit/SKILL.md), [launch-readiness-check](skills/launch-readiness-check/SKILL.md), [localization-claims](skills/localization-claims/SKILL.md), [ssot-context-loop](skills/ssot-context-loop/SKILL.md) (approval and governance) |

**Additional skills:** [ad-creative](skills/ad-creative/SKILL.md) · [aso-audit](skills/aso-audit/SKILL.md)

## Installation and use

Codex uses `.agents/skills/`; Claude Code uses `.claude/skills/`.

For a personal installation across projects, use `~/.agents/skills/` for Codex or `~/.claude/skills/` for local Claude Code sessions. Other agents need their own documented skill discovery configuration; the Agent Skills format does not prescribe a universal installation directory.

Keep `_shared/` alongside the skill folders. When installing only selected skills, include their shared references and any skills required by the intended handoff.

Copy complete folders, including `references/`, `scripts/`, and `assets/` where present. When updating an existing installation, review differences before copying because `cp -R` replaces matching files.

Ask naturally, or explicitly select a skill using your agent's supported invocation syntax:

```text
Compare these markets and recommend which evidence to validate first.
Build an event GTM strategy from our approved SSOT and route the assets.
Check this brief against the requirements of the skill that produced it.
Audit this website, sales deck and outbound against our SSOT and each other.
```

For governed projects, use `ssot-context-loop /setup <client>` to draft the baseline and obtain required approval. Use `/manifest` to map readers.

Supply the active client, sources, assets, and task scope. The repository does not bundle a company SSOT or project manifest.

Tool guides and optional CLI integrations are indexed in [tools/REGISTRY.md](tools/REGISTRY.md). They support execution; external actions remain subject to the user's instructions and the relevant workflow approvals.

<a id="validation-and-extending-the-system"></a>
<details>
<summary><b>For contributors</b></summary>

Skills are content, with no build step. Run the local checks from the repository root:

```bash
bash validate-skills.sh
python3 evals/harness.py lint
python3 evals/check_references.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s evals/tests -v
git diff --check
```

The [eval documentation](evals/README.md) separates structural checks, deterministic regressions, mock pipeline runs, and real model evaluations. Mock runs exercise the pipeline with fake outputs and random grades; they do not show that a skill makes good PMM decisions. Real runs need a configured API and an authorized budget.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md). Report skill problems separately from production deliverables, and don't edit skills during a production run.

</details>

## License

[MIT license](LICENSE).
