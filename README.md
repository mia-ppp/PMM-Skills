# Product Marketing Skills for Claude Code and Codex

PMM Skills is an open-source collection of product marketing skills for AI agents, including Claude Code and OpenAI Codex. Product marketers can use them for customer research, competitive intelligence, positioning, messaging, go-to-market (GTM) planning, launches, and sales enablement.

The collection is for product marketers and teams using AI for structured product marketing work, from research and strategy through GTM, execution, and review.

## Why PMM skills?

Individual prompts can produce isolated outputs. PMM work connects across jobs: customer research informs segmentation, segmentation informs positioning, and positioning informs messaging.

Messaging then guides launch strategy, sales enablement, and channel execution. These AI agent skills provide reusable workflows and shared company context so work can pass between skills while preserving approved strategy.

The skills distinguish evidence from assumptions and gaps, and check downstream assets against the same source of truth. Changes to approved positioning, messaging, or other strategy require human approval.

Jump to: [What you can do](#what-you-can-do) · [Quick start](#quick-start) · [How it works](#how-the-system-works) · [Example workflows](#example-workflows) · [Capability map](#capability-map) · [Shared context / SSOT](#shared-context-and-approval) · [Reviews](#three-separate-reviews) · [Installation](#installation-and-use) · [Validation & contributing](#validation-and-extending-the-system)

## What you can do

- Synthesize customer and market research, compare segments, and develop an ideal customer profile (ICP) and buyer personas.
- Define positioning, build a messaging framework, and evaluate pricing and packaging.
- Research competitors, analyze win/loss outcomes, and track recurring sales objections.
- Plan launches, events, account-based marketing (ABM), customer marketing, and partner programs.
- Create sales enablement materials, website copy, email sequences, social content, and paid campaigns.
- Check whether outputs meet their requirements, audit messaging against approved company context, and assess launch readiness.

## Quick start

With Git and your agent installed, run this from the project where you want to use the PMM skills:

```bash
git clone https://github.com/mia-ppp/PMM-Skills.git
```

For a fresh installation, choose the directory for your agent. If it already contains PMM skills or `_shared/`, review those files before copying because `cp -R` replaces matching files.

### Codex skills

```bash
mkdir -p .agents/skills
cp -R PMM-Skills/skills/* .agents/skills/
```

### Claude Code skills

```bash
mkdir -p .claude/skills
cp -R PMM-Skills/skills/* .claude/skills/
```

These commands copy the skill folders and `_shared/`. Start your agent in this project, then ask:

```text
Use product-marketing-context to draft our company context from these notes.
Separate sourced facts, assumptions, and evidence gaps for me to review.
```

For a project with approved company context, try `positioning-strategy`, `messaging-framework`, or another skill in the [capability map](#capability-map). See [installation and use](#installation-and-use) for shared references, existing installations, and governed projects.

## How the system works

Product marketing connects customer evidence to decisions, launches, and the assets buyers see. The skills share approved company context, or SSOT (single source of truth), so each workflow builds on the same product claims, positioning, and messaging.

| Research & Intelligence | PMM Strategy | Go-to-Market | Execution | Growth | Systems & Review |
|---|---|---|---|---|---|
| `customer-research` | `icp-and-buyer-personas` | `go-to-market-strategy` | `sales-enablement` | `content-strategy` | `product-marketing-context` |
| `competitor-profiling` | `positioning-strategy` | `market-entry-orchestration` | `marketing-copy` | `search-discoverability` | `ssot-context-loop` |
| `win-loss-intelligence` | `messaging-framework` | `launch-strategy` | `cold-email` | `website-buyer-journey` | `output-quality-check` |
| `objection-intelligence` | `pricing-strategy` | `account-based-marketing` | `email-sequence` | `aso-audit` | `messaging-consistency-audit` |
| `market-entry-brief` |  | `events` | `social-content` | `acquisition-conversion` | `launch-readiness-check` |
|  |  | `customer-marketing` | `paid-ads` | `product-activation` | `localization-claims` |
|  |  | `partner-marketing` | `ad-creative` | `upgrade-conversion` | `analytics-tracking` |
|  |  | `product-communications` | `competitor-alternatives` | `community-marketing` | `marketing-experimentation` |
|  |  |  |  | `referral-program` | `revops` |
|  |  |  |  | `buyer-resources` |  |

Research → Context → Strategy → GTM → Execution → Growth → Learning ↺

Research informs strategy. Approved strategy drives execution. Field learning can propose updates to company context and strategy, but human approval is required before changing canon.

Start at the point your task needs. A page edit can use approved context directly; a new-market decision needs evidence and segment analysis first.

Channel skills express approved strategy. Observed evidence can challenge it and trigger review, but does not silently rewrite canon.

Quality and governance checks apply across workflows; they are shown together for readability.

| PMM job | What the skills help you do | Example capabilities |
|---|---|---|
| Customer & market intelligence | Find recurring customer needs, competitive patterns, and reasons deals are won or lost. Keep customer language and sourced findings separate from interpretation. | Customer research, Voice of Customer, competitive intelligence, win/loss, objection intelligence |
| Segmentation & audience | Compare candidate segments and evidence gaps, then develop personas from the accepted audience decision. | Market segmentation, ICP, buyer personas, buying committee maps |
| Positioning & messaging | Propose a positioning direction and build messaging from approved positioning and buyer context. Route strategic changes for human approval. | Positioning, messaging frameworks, value propositions |
| Pricing & packaging | Evaluate what to charge and how to structure plans using buyer needs and willingness-to-pay evidence. | Pricing research, packaging, value metrics, pricing tiers |
| Go-to-market & launches | Plan the market entry or launch, assign owners and dependencies, and hand asset briefs to channel skills. | GTM model, market entry, launch strategy, ABM, events, partner marketing, product communications |
| Customer & revenue growth | Plan customer adoption, expansion, advocacy, and retention programs from approved context. | Customer marketing, activation, retention, upgrades, referral programs, community marketing |
| Channels & execution | Turn approved strategy into sales materials and channel assets, then improve discovery and conversion. | Sales enablement, website/copy, email, social, paid acquisition, CRO, SEO, content, lead magnets, creative |
| Quality & governance | Check outputs against their originating skill, audit market-facing messaging against approved context, and assess overall launch readiness. Maintain approval gates for strategic changes. | Output quality, messaging consistency, launch readiness, localization/claims, SSOT governance |
| Learning loop | Measure results, manage revenue handoffs, and return field evidence for review and proposed updates to company context and strategy. | Measurement, experimentation, RevOps, win/loss and objection findings, human-approved SSOT updates |

### Shared context and approval

[product-marketing-context](skills/product-marketing-context/SKILL.md) creates a lightweight bootstrap at `.agents/product-marketing-context.md` (with legacy `.claude/` support). It captures sources, assumptions, and gaps separately from governed canon.

[ssot-context-loop](skills/ssot-context-loop/SKILL.md) manages `ssot/<client-slug>/` in the user's project. Core files hold approved product truth, positioning, and personas; living files hold field signals, use cases, competition, proof, and objections.

A project-root `manifest.yaml` maps each reader to the relevant files. The [operational specification](skills/ssot-context-loop/references/ssot-spec.md) defines the actual schemas and commands.

When an applicable SSOT exists, it is authoritative for covered claims. Skills use the [SSOT consumption contract](skills/_shared/ssot-consumption.md), load mapped context, and flag missing, stale, or contested inputs.

Existing stricter legal or claims-register restrictions also apply; conflicts require review.

Evidence can challenge canon without changing it. `/scan` stops for Gate 1 confirmation; `/propose` prepares changes; Gate 2 requires explicit human approval before core changes are persisted.

Initial baseline strategy also requires approval. Downstream skills do not edit canonical files, decisions, or `state.md`, and the bootstrap document is never automatically overwritten by the SSOT loop.

### Evidence and segment decisions

The [evidence contract](skills/_shared/evidence-gaps.md) distinguishes **Sourced**, **Assumed**, and **Gap**, with formulas for derived numbers and ranked validation work. SSOT files use `[C]`, `[A]`, and `[G]` for cited evidence, assumptions, and gaps.

Citing evidence does not approve a strategic change.

Customer quotes retain their source wording and provenance. VoC synthesis lives inside `customer-research`; it separates customer language, PMM interpretation, and proposed marketing language.

Win/loss and objection intelligence produce sourced findings and implications for strategy review.

The [segment-selection framework](skills/_shared/segment-selection.md) keeps all plausible candidates visible, uses thirteen weighted criteria, and reports attractiveness separately from evidence confidence.

A segment recommendation cannot automatically replace canonical ICP. Downstream persona and launch work inherit accepted decisions instead of independently selecting a different target.

### Three separate reviews

| Review | Question it answers | What happens next |
|---|---|---|
| [output-quality-check](skills/output-quality-check/SKILL.md) | Does the artifact meet the requirements of the skill that produced it? This read-only check includes required shared standards; missing verification evidence remains UNVERIFIABLE. | Route corrections to the originating skill. |
| [messaging-consistency-audit](skills/messaging-consistency-audit/SKILL.md) | Does market-facing messaging match applicable SSOT and stay consistent across the supplied assets? Legitimate channel variation is allowed. | Route asset corrections to owners; suspected canon issues to SSOT review; inspect corrected assets in re-audit. |
| [launch-readiness-check](skills/launch-readiness-check/SKILL.md) | Is the launch ready to proceed under applicable canon and stricter restrictions? This final go/no-go check includes review coverage. | Hold launch-wide clearance for blockers or unreviewed required assets. |

An artifact can meet its skill's output requirements and still need messaging correction. Internal evidence reports usually need output verification.

Use messaging audits for market-facing assets; definitive canon judgments require applicable SSOT. Skill evals are separate from launch readiness.

## Example workflows

Ask Claude Code or Codex in plain language, supplying your sources and approved context. These requests connect product marketing workflows; recommendations remain proposals until the required human approval.

### Market / ICP

> Compare these market segments using the segmentation framework. Show the evidence gaps before recommending a target, then develop buyer personas from the accepted decision.

> Analyze these customer interviews, identify recurring pain points, and use the evidence and accepted segment to propose a positioning direction. Once positioning is approved, build a messaging framework from it and our buyer personas.

customer and competitor evidence → `market-entry-brief` and shared segment scoring → accepted market decision → `icp-and-buyer-personas` → `positioning-strategy` → `messaging-framework` → `ssot-context-loop` approval and canonical record. With existing canon, proposed changes enter its review gates.

### Launch

> Build a launch plan from our approved positioning and messaging, then brief the channel owners. Audit the launch assets for contradictions and unsupported claims, and assess launch readiness after the required reviews.

approved SSOT → `launch-strategy` → channel owners and assets → `output-quality-check` → `messaging-consistency-audit` → `launch-readiness-check`. For new-market entry, `market-entry-orchestration` conducts the four gated rungs in the [launch contract](skills/_shared/launch-stages.md).

### Evidence feedback

> Analyze our closed-won and closed-lost opportunities for recurring competitive and objection patterns. Separate buyer evidence from seller interpretation, and route implications for strategy review without changing approved context.

`customer-research` / `win-loss-intelligence` / `objection-intelligence` → sourced findings and limitations → SSOT scan and proposals → human approval → affected readers and assets → re-audit. Repetition alone never makes a message canonical.

### Event

> Evaluate this event against our ICP and goals. If we decide to proceed, build the activation plan from approved messaging and brief the email, social, and sales enablement work.

approved SSOT → `events` investment decision, narrative and activation plan → `marketing-copy`, `email-sequence`, `cold-email`, `social-content`, or `sales-enablement` → output verification → messaging audit → measured follow-up and learning. Events owns the GTM motion; channel owners produce the assets.

### ABM

> Use our accepted ICP to propose account tiers and buying committee hypotheses. Plan coordinated outreach from approved messaging, then define how we will measure account engagement and return findings for review.

accepted ICP and SSOT → `account-based-marketing` account selection and tiers → account buying committee and message hypotheses → coordinated outreach, paid, event, and sales execution → `revops` / `analytics-tracking` measurement → account learning and evidence review. Account hypotheses cannot redefine ICP.

## Capability map

The portfolio contains **44 standalone skills**. Skills are installed as sibling folders so their shared references resolve. Open a skill to see its inputs, output requirements, and handoffs.

| Capability area | Skills |
|---|---|
| Evidence & intelligence | [customer-research](skills/customer-research/SKILL.md), [win-loss-intelligence](skills/win-loss-intelligence/SKILL.md), [objection-intelligence](skills/objection-intelligence/SKILL.md), [competitor-profiling](skills/competitor-profiling/SKILL.md) |
| Market & buyer strategy | [market-entry-brief](skills/market-entry-brief/SKILL.md), [icp-and-buyer-personas](skills/icp-and-buyer-personas/SKILL.md), [pricing-strategy](skills/pricing-strategy/SKILL.md) |
| Positioning & messaging | [positioning-strategy](skills/positioning-strategy/SKILL.md), [messaging-framework](skills/messaging-framework/SKILL.md) |
| GTM strategy & motions | [go-to-market-strategy](skills/go-to-market-strategy/SKILL.md), [market-entry-orchestration](skills/market-entry-orchestration/SKILL.md), [launch-strategy](skills/launch-strategy/SKILL.md), [events](skills/events/SKILL.md), [account-based-marketing](skills/account-based-marketing/SKILL.md), [customer-marketing](skills/customer-marketing/SKILL.md), [partner-marketing](skills/partner-marketing/SKILL.md), [product-communications](skills/product-communications/SKILL.md) |
| Channel execution: copy & sales | [marketing-copy](skills/marketing-copy/SKILL.md), [cold-email](skills/cold-email/SKILL.md), [email-sequence](skills/email-sequence/SKILL.md), [social-content](skills/social-content/SKILL.md), [sales-enablement](skills/sales-enablement/SKILL.md) |
| Channel execution: paid & media | [paid-ads](skills/paid-ads/SKILL.md), [ad-creative](skills/ad-creative/SKILL.md) |
| Channel execution: content & discovery | [content-strategy](skills/content-strategy/SKILL.md), [search-discoverability](skills/search-discoverability/SKILL.md), [website-buyer-journey](skills/website-buyer-journey/SKILL.md), [aso-audit](skills/aso-audit/SKILL.md), [competitor-alternatives](skills/competitor-alternatives/SKILL.md) |
| Growth & conversion | [acquisition-conversion](skills/acquisition-conversion/SKILL.md), [product-activation](skills/product-activation/SKILL.md), [upgrade-conversion](skills/upgrade-conversion/SKILL.md) |
| Growth & retention programs | [community-marketing](skills/community-marketing/SKILL.md), [referral-program](skills/referral-program/SKILL.md), [buyer-resources](skills/buyer-resources/SKILL.md) |
| Operations & measurement | [revops](skills/revops/SKILL.md), [analytics-tracking](skills/analytics-tracking/SKILL.md), [marketing-experimentation](skills/marketing-experimentation/SKILL.md) |
| Company context & SSOT | [product-marketing-context](skills/product-marketing-context/SKILL.md), [ssot-context-loop](skills/ssot-context-loop/SKILL.md) |
| Quality & governance | [output-quality-check](skills/output-quality-check/SKILL.md), [messaging-consistency-audit](skills/messaging-consistency-audit/SKILL.md), [launch-readiness-check](skills/launch-readiness-check/SKILL.md), [localization-claims](skills/localization-claims/SKILL.md) |

## Installation and use

The quick start installs project-local skills using the documented [Codex skill locations](https://learn.chatgpt.com/docs/build-skills) and [Claude Code skill locations](https://code.claude.com/docs/en/skills). Codex uses `.agents/skills/`; Claude Code uses `.claude/skills/`.

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

## Validation and extending the system

Skills are content, with no build step. Run the local checks from the repository root:

```bash
bash validate-skills.sh
python3 evals/harness.py lint
python3 evals/check_references.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s evals/tests -v
git diff --check
```

[Eval documentation](evals/README.md) separates structural checks, deterministic harness regressions, mock pipeline runs, and real model evaluations. `--mock` exercises orchestration with fake outputs and random grades; it does not prove PMM behavior.

Real runs require a configured API and authorized budget. Historical [measured results](evals/RESULTS.md) do not establish that later skill changes passed behavioral evaluation.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md). Preserve responsibility boundaries, reuse shared standards, keep evidence and approval explicit, and add focused evals for meaningful behavior.

Report skill problems separately from production deliverables; do not edit skills during a production run.

[MIT license](LICENSE).
