# Product Marketing Skills for Claude Code and Codex

PMM Skills is an open-source collection of product marketing skills for AI agents, including Claude Code and OpenAI Codex. Product marketers can use them for customer research, market intelligence, competitive intelligence, positioning, messaging, go-to-market (GTM) planning, launches, and sales enablement.

The collection is for product marketers and teams using AI for structured product marketing work, from research and strategy through GTM, execution, and review.

## Why PMM skills?

Individual prompts can produce isolated outputs. PMM work connects across jobs: customer research informs segmentation, segmentation informs positioning, and positioning informs messaging.

Messaging then guides launch strategy, sales enablement, and channel execution. These AI agent skills provide reusable workflows and shared company context so work can pass between skills while preserving approved strategy.

The skills distinguish evidence from assumptions and gaps, and check downstream assets against the same source of truth. Changes to approved positioning, messaging, or other strategy require human approval.

Jump to: [What you can do](#what-you-can-do) · [Quick start](#quick-start) · [How it works](#how-the-system-works) · [Example workflows](#example-workflows) · [Capability map](#capability-map) · [Shared context / SSOT](#shared-context-and-approval) · [Reviews](#three-separate-reviews) · [Installation](#installation-and-use) · [Validation & contributing](#validation-and-extending-the-system)

## What you can do

- Synthesize customer research, analyze win/loss outcomes, and track recurring sales objections.
- Research market conditions, category conventions, and emerging opportunities.
- Map the competitive landscape, profile competitors, and investigate competitive signals.
- Evaluate market entry, compare segments, and develop an ideal customer profile (ICP) and buyer personas.
- Define positioning, build a messaging framework, and evaluate pricing and packaging.
- Plan launches, events, account-based marketing (ABM), customer marketing, and partner programs.
- Create sales enablement materials, website copy, email sequences, social content, and paid campaigns.
- Measure performance, run experiments, and manage revenue handoffs.
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
Use product-marketing-context to establish context for this decision from these materials.
Inventory the sources, assess readiness, and route consequential research gaps.
Separate evidence, interpretations, assumptions, and approval dependencies for review.
```

For a project with approved company context, try `positioning-strategy`, `messaging-framework`, or another skill in the [capability map](#capability-map). See [installation and use](#installation-and-use) for shared references, existing installations, and governed projects.

## How the system works

Product marketing connects customer, market, and competitive intelligence to decisions, launches, and the assets buyers see. The skills share approved company context, or SSOT (single source of truth), so each workflow builds on the same product claims, positioning, and messaging.

```text
┌───────────────────────────────┐   ┌───────────────────────────────┐
│ COMPANY INPUTS                │   │ EXISTING PMM CONTEXT          │
│                               │   │                               │
│ Market data                   │   │ Positioning                   │
│ Product & funnel data         │   │ Messaging                     │
│ Product docs                  │   │ Personas / ICP                │
│ Product roadmap               │   │ Prior research                │
│ CRM data                      │   │ Existing decisions            │
│ Sales calls                   │   │                               │
└───────────────────────────────┘   └───────────────────────────────┘

RESEARCH & INTELLIGENCE
┌───────────────────────────────┐   ┌───────────────────────────────┐   ┌───────────────────────────────┐
│ CUSTOMER INTELLIGENCE         │   │ MARKET INTELLIGENCE           │   │ COMPETITIVE INTELLIGENCE      │
│                               │   │                               │   │                               │
│ Customer research             │   │ Market intelligence           │   │ Competitive landscape         │
│ Win/loss                      │   │ Category intelligence         │   │ Competitor profiling          │
│ Objection intelligence        │   │ Emerging opportunities        │   │ Competitive signals           │
└───────────────────────────────┘   └───────────────────────────────┘   └───────────────────────────────┘
                                                     ↓
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ PMM CONTEXT / SSOT                                                                                      │
│ Product marketing context                                                                               │
│ SSOT context loop                                                                                       │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                     ↓
┌───────────────────────────────┐   ┌───────────────────────────────┐   ┌───────────────────────────────┐
│ PMM STRATEGY                  │   │ GO-TO-MARKET                  │   │ EXECUTION                     │
│                               │   │                               │   │                               │
│ Market entry                  │   │ GTM strategy                  │   │ Sales enablement              │
│ ICP & buyer personas          │   │ Market entry orchestration    │   │ Marketing copy                │
│ Positioning                   │   │ Launch strategy               │   │ Cold email                    │
│ Messaging                     │   │ Account-based marketing       │   │ Email sequences               │
│ Pricing                       │   │ Events                        │   │ Social content                │
│                               │   │ Customer marketing            │   │ Paid ads                      │
│                               │   │ Partner marketing             │   │ Content strategy              │
│                               │   │ Product communications        │   │ Search discovery              │
│                               │   │                               │   │ Website journey               │
│                               │   │                               │   │ Competitor alternatives       │
└───────────────────────────────┘   └───────────────────────────────┘   └───────────────────────────────┘
                                                     ↓
┌───────────────────────────────┐   ┌───────────────────────────────┐   ┌───────────────────────────────┐
│ GROWTH                        │   │ MEASUREMENT                   │   │ REVIEW & GOVERNANCE           │
│                               │   │                               │   │                               │
│ Acquisition conversion        │   │ Analytics                     │   │ Output quality                │
│ Product activation            │   │ Experimentation               │   │ Messaging consistency         │
│ Upgrade conversion            │   │ RevOps                        │   │ Launch readiness              │
│ Community marketing           │   │                               │   │ Localization & claims         │
│ Referral programs             │   │                               │   │ SSOT governance               │
│ Buyer resources               │   │                               │   │                               │
└───────────────────────────────┘   └───────────────────────────────┘   └───────────────────────────────┘
                                                     ↓
                                               Field Learning
                                                     ↓
                                          human review / approval
                                           ↺ PMM Context / SSOT
```

Company inputs and existing PMM context are resources available to the system. Skills use them as the task requires. Product & funnel data covers quantitative usage, activation, retention, conversion, and pipeline performance.

Customer, Market, and Competitive Intelligence produce reusable understanding that informs the central PMM Context / SSOT layer and strategy decisions. Market intelligence examines external market and category conditions; market entry uses that evidence to decide where or whether to enter. Approved context supports PMM Strategy, Go-to-Market, and Execution. Field learning can propose context and strategy updates, but human approval is required before changing canon.

Start at the point your task needs. A page edit can use approved context directly; a new-market decision needs evidence and segment analysis first.

Channel skills express approved strategy. Observed evidence can challenge it and trigger review, but does not silently rewrite canon.

Measurement tracks results, experiments, and revenue handoffs. Review & Governance applies across workflows, including research outputs and market-facing assets.

### Shared context and approval

`product-marketing-context` and `ssot-context-loop` support the central PMM Context / SSOT layer. The former establishes and integrates provisional understanding; the latter maintains governed context and its approval loop.

[product-marketing-context](skills/product-marketing-context/SKILL.md) inventories supplied materials and existing research, separates evidence from interpretations and assumptions, and records contradictions and gaps. It assesses readiness for the intended decision, routes consequential gaps to specialist owners, and integrates their returned findings using the [context establishment contract](skills/_shared/context-establishment.md).

Its provisional workspace uses `.agents/product-marketing-context.md` (with legacy `.claude/` support), preserving existing profiles and applicable approved context. Evidence readiness does not grant approval. Context proposals go to `ssot-context-loop`; saving the workspace does not change canon.

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

### Market intelligence → Market entry / ICP

> Use market-intelligence to research market conditions, category conventions, and emerging opportunities. Use competitor-profiling to map the competitive landscape and investigate competitive signals. Keep reusable findings separate from our market-entry recommendation.

> Compare these market segments using the segmentation framework. Show the evidence gaps before recommending a target, then develop buyer personas from the accepted decision.

> Analyze these customer interviews, identify recurring pain points, and use the evidence and accepted segment to propose a positioning direction. Once positioning is approved, build a messaging framework from it and our buyer personas.

`product-marketing-context` intake and readiness assessment → targeted `customer-research`, `market-intelligence`, or `competitor-profiling` work as needed → findings integrated into context and readiness reassessed → `market-entry-brief` entry decision and shared segment scoring → accepted market decision → `icp-and-buyer-personas` → `positioning-strategy` → `messaging-framework` → `ssot-context-loop` approval and canonical record. With existing canon, proposed changes enter its review gates.

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
