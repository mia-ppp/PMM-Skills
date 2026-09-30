# Product Marketing Skills for Claude Code and Codex

PMM Skills is an open-source collection of product marketing skills for AI agents, including Claude Code and OpenAI Codex. Product marketers can use them for customer research, competitive intelligence, positioning, messaging, go-to-market (GTM) planning, launches, and sales enablement.

The skills work from shared company context, so research can feed strategy, approved strategy can feed launches and channel execution, and market-facing assets can be checked against the same source of truth. Each skill owns a specific job and hands work to the right downstream skill. Changes to approved strategy still require human approval.

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

SSOT means single source of truth: the approved company context skills use for product claims, positioning, messaging, and strategy. Research informs strategy proposals, channel skills produce assets from approved context, and new findings return for review:

```text
Evidence & intelligence → company context / SSOT → strategy proposals
                               ↑                         ↓
                     human-approved changes          GTM motions
                               ↑                         ↓
                     learning & evidence ← review ← channel execution
```

Start at the point your task needs. A page edit can use approved context directly; a new-market decision needs evidence and segment analysis first.

| Layer | Responsibility |
|---|---|
| Evidence & intelligence | Collect and synthesize customer language, opportunity outcomes, objections, and competitor observations. Separate sources from interpretations. |
| Company context / SSOT | Bootstrap a project, or maintain governed core strategy and living field intelligence with explicit approval gates. |
| Strategy | Decide markets, segments, personas, positioning, messaging, and pricing. Recommendations remain proposals until approved. |
| GTM motions | Set objectives, audiences, narrative briefs, owners, dependencies, and learning plans. Hand final assets to channel skills. |
| Channel execution | Express approved strategy for the channel, persona, and stage. Wording and emphasis can vary while meaning stays consistent. |
| Quality & governance | Check originating-skill requirements, audit market-facing messaging, and apply the final launch readiness gate. |
| Operations & learning | Instrument results, manage revenue handoffs, and return observed evidence to the appropriate owner. |

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

### Market / ICP

customer and competitor evidence → `market-entry-brief` and shared segment scoring → accepted market decision → `buyer-personas` → `positioning-strategy` → `messaging-framework` → `ssot-context-loop` approval and canonical record. With existing canon, proposed changes enter its review gates.

### Launch

approved SSOT → `launch-strategy` → channel owners and assets → `output-quality-check` → `messaging-consistency-audit` → `launch-readiness-check`. For new-market entry, `market-launch` conducts the four gated rungs in the [launch contract](skills/_shared/launch-stages.md).

### Evidence feedback

`customer-research` / `win-loss-intelligence` / `objection-intelligence` → sourced findings and limitations → SSOT scan and proposals → human approval → affected readers and assets → re-audit. Repetition alone never makes a message canonical.

### Event

approved SSOT → `events` investment decision, narrative and activation plan → `copywriting`, `email-sequence`, `cold-email`, `social-content`, or `sales-enablement` → output verification → messaging audit → measured follow-up and learning. Events owns the GTM motion; channel owners produce the assets.

### ABM

accepted ICP and SSOT → `account-based-marketing` account selection and tiers → account buying committee and message hypotheses → coordinated outreach, paid, event, and sales execution → `revops` / `analytics-tracking` measurement → account learning and evidence review. Account hypotheses cannot redefine ICP.

## Capability map

Skills are installed as sibling folders so their shared references resolve. Open a skill to see its inputs, output requirements, and handoffs.

| Capability area | Skills |
|---|---|
| Evidence & intelligence | [customer-research](skills/customer-research/SKILL.md), [win-loss-intelligence](skills/win-loss-intelligence/SKILL.md), [objection-intelligence](skills/objection-intelligence/SKILL.md), [competitor-profiling](skills/competitor-profiling/SKILL.md) |
| Market & buyer strategy | [market-entry-brief](skills/market-entry-brief/SKILL.md), [buyer-personas](skills/buyer-personas/SKILL.md), [pricing-strategy](skills/pricing-strategy/SKILL.md), [marketing-ideas](skills/marketing-ideas/SKILL.md), [marketing-psychology](skills/marketing-psychology/SKILL.md) |
| Positioning & messaging | [positioning-strategy](skills/positioning-strategy/SKILL.md), [messaging-framework](skills/messaging-framework/SKILL.md) |
| GTM motions | [market-launch](skills/market-launch/SKILL.md), [launch-strategy](skills/launch-strategy/SKILL.md), [events](skills/events/SKILL.md), [account-based-marketing](skills/account-based-marketing/SKILL.md), [customer-marketing](skills/customer-marketing/SKILL.md), [partner-marketing](skills/partner-marketing/SKILL.md), [product-communications](skills/product-communications/SKILL.md) |
| Channel execution: copy & sales | [copywriting](skills/copywriting/SKILL.md), [copy-editing](skills/copy-editing/SKILL.md), [cold-email](skills/cold-email/SKILL.md), [email-sequence](skills/email-sequence/SKILL.md), [social-content](skills/social-content/SKILL.md), [sales-enablement](skills/sales-enablement/SKILL.md) |
| Channel execution: paid & media | [paid-ads](skills/paid-ads/SKILL.md), [ad-creative](skills/ad-creative/SKILL.md), [image](skills/image/SKILL.md), [video](skills/video/SKILL.md) |
| Channel execution: content & discovery | [content-strategy](skills/content-strategy/SKILL.md), [seo-audit](skills/seo-audit/SKILL.md), [ai-seo](skills/ai-seo/SKILL.md), [programmatic-seo](skills/programmatic-seo/SKILL.md), [site-architecture](skills/site-architecture/SKILL.md), [schema-markup](skills/schema-markup/SKILL.md), [aso-audit](skills/aso-audit/SKILL.md), [competitor-alternatives](skills/competitor-alternatives/SKILL.md), [directory-submissions](skills/directory-submissions/SKILL.md) |
| Growth & conversion | [page-cro](skills/page-cro/SKILL.md), [signup-flow-cro](skills/signup-flow-cro/SKILL.md), [onboarding-cro](skills/onboarding-cro/SKILL.md), [form-cro](skills/form-cro/SKILL.md), [popup-cro](skills/popup-cro/SKILL.md), [paywall-upgrade-cro](skills/paywall-upgrade-cro/SKILL.md) |
| Growth & retention programs | [community-marketing](skills/community-marketing/SKILL.md), [churn-prevention](skills/churn-prevention/SKILL.md), [referral-program](skills/referral-program/SKILL.md), [lead-magnets](skills/lead-magnets/SKILL.md), [free-tool-strategy](skills/free-tool-strategy/SKILL.md) |
| Operations & measurement | [revops](skills/revops/SKILL.md), [analytics-tracking](skills/analytics-tracking/SKILL.md), [ab-test-setup](skills/ab-test-setup/SKILL.md) |
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
