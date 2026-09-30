# SSOT Context Loop: Operational Specification

This reference defines the runtime files, section schema, evidence model, signal
taxonomy, drift verdicts, commands, and approval gates for `ssot-context-loop`.
Use it with `SKILL.md`; it does not replace the operating rules there.

## 1. Purpose and authority

Maintain one persistent PMM source of truth per client. The loop flags drift,
proposes file changes, and writes approved changes. A human PMM decides. Never
skip a gate. The project's GitHub-backed repository is the durable source of
truth. Chat history is not the system of record. Commit and push each file created
or changed by the workflow when that change is authorized. Never use persistence
to bypass Gate 1 or Gate 2, and never change or commit core without explicit human
approval at Gate 2.

Facts are events in a system of record, such as deals, calls, tickets, or press
releases. Opinions are strategic beliefs, such as who to sell to or which pitch
lands. The SSOT records opinions and grounds them in facts.

Claims use these tags:

| Tag | Meaning | Required handling |
|---|---|---|
| `[C]` | Cited | Name the source inline. Include quote or data, speaker and role, account type, system, date, and outcome or cost when known. |
| `[A]` | Assumed | State the reasoning. Do not present it as a fact. |
| `[G]` | Gap | State what evidence is missing and what would close the gap. |

Never invent facts. Missing facts do not stop work. Keep a segment even when it has
no evidence and mark the gap. Positioning must come from differentiators already
in core. Persona messaging must come from persona research already in the SSOT.
The field may be right and the canon stale, so drift always ends with a verdict,
never an automatic correction.

## 2. Runtime project layout

Create this structure in the user's working project, not in the PMM-Skills repo.
`manifest.yaml` lives at that project's repository root.

```text
manifest.yaml
ssot/<client-slug>/
  core/
    00-what-it-is.md
    01-how-you-position-it.md
    02-product.md
    03-who-it-is-for.md
  living/
    04-icp-signals.md
    05-use-cases.md
    06-competitive.md
    07-evidence.md
    08-objection-handling.md
  09-iteration.md
  decisions/
    YYYY-MM-DD-<slug>.md
  comms/
  state.md
```

| File | Layer and owner | Question it answers |
|---|---|---|
| `core/00-what-it-is.md` | Core, PMM decides and approves | Product description, category, anti-positioning, and platform pillars. |
| `core/01-how-you-position-it.md` | Core, PMM decides and approves | Wedge, pitch pillars, differentiators, say-this-not-that, and deprecated frames. |
| `core/02-product.md` | Core, PMM decides and approves | Capabilities, integrations, what ships and does not ship, and allowed roadmap claims. |
| `core/03-who-it-is-for.md` | Core, PMM decides and approves | Personas, buying committee, per-persona messaging, blockers, and reframes. |
| `living/04-icp-signals.md` | Living, field reports | Which accounts appear, what they share, and who is in the room. |
| `living/05-use-cases.md` | Living, field reports | Industry and function use cases, customer-described outcomes, and accepted POC metrics. |
| `living/06-competitive.md` | Living, field reports | Where the client wins and loses, competitor frames, displacement, and coexistence. |
| `living/07-evidence.md` | Living, field reports | Customer voice, proof points, metrics, third-party research, and analyst notes. |
| `living/08-objection-handling.md` | Living, field reports | Objection, answer that works, and the call it came from. |
| `09-iteration.md` | Loop log | Sources, cadence, drift criteria, and rejected findings with reasons. |
| `decisions/YYYY-MM-DD-<slug>.md` | Decision record | One approved canon change per file. |
| `comms/` | Raw captured inputs | Source transcripts and exports, never edited after capture. |
| `state.md` | Reconciler only | Status counts, stale and contested sections, gaps, validations, decisions, and scan state. |

The four core files are reviewed quarterly to monthly. The five living files are
reviewed weekly to monthly. Do not combine questions across files. When a claim
could fit more than one file, choose one and record the choice in `09-iteration.md`.

## 3. File and section schema

Every core and living file follows this structure. Use the exact file identifier
in frontmatter and the file's question as its one-line scope.

```markdown
---
file: 03-who-it-is-for
layer: core
client: <client-slug>
owner: <PMM name>
last_reviewed: YYYY-MM-DD
---
# 03: Who it is for
One-line scope of the question this file answers.

## <section-name>
Status: current | directional | pending | stale | contested | deprecated
Last validated: YYYY-MM-DD

[Every content line ends with exactly one evidence tag: [C], [A], or [G].]

Evidence
- <quote or data> (<who, role, account type>, <system>, <date>). <Outcome or cost.> [C]

Pending validation
- <What is unproven.> Next cycle: <evidence to pull and source.> [G]

## anti-patterns
What NOT to write anywhere this file's content is used. [C]
- Don't <X>. <Why, or where it belongs instead.> [C]
```

The schema example uses a core file. Set `layer: living` for living files. Put
`Status` and `Last validated` on every section, not only in frontmatter. Every
content line in every canonical SSOT file must end with exactly one evidence tag:
`[C]`, `[A]`, or `[G]`. This includes evidence, pending-validation, and
anti-pattern content lines. Structural frontmatter, headings, status/date labels,
and blank lines are not content lines. Evidence citations name the source, speaker,
role, account type, system, date, and outcome or cost when available. Include an
`anti-patterns` section in each file. Source anti-patterns from supplied material;
mark unsupported ones `[G]`.

A section without evidence is at most `directional`, never `current`. Preserve
unproven claims as `[A]` or `[G]` with a `Pending validation` action. Never delete
a section. Change it to `deprecated` and identify its replacement.

### Staleness and contested status

- A core section becomes stale 90 days after its last validation.
- A living section becomes stale 30 days after its last validation.
- Two or more independent field signals that contradict a section make it
  `contested` until Gate 1. Do not silently resolve the conflict.
- Set section validation dates only when the evidence actually validates that
  section. A file edit alone does not validate every section.

## 4. Signal taxonomy

Classify every field signal into one category. Preserve concise source quotes in
the drift report and retain full raw inputs in `comms/`.

| Category | Signals to identify |
|---|---|
| Who is in the room | Champion and detractor or blocker profiles; stakeholder shape in wins versus losses. |
| What lands | Aha moments and underlying pain; customer-described outcomes; use cases by industry; accepted POC metrics. |
| What blocks | Deal-killing objections; deal-blocking product gaps; pricing-model intelligence; pilot feedback. |
| Their words, not yours | Customer descriptions of product and pain; language a champion uses to sell internally. |
| Who you're up against | Competitor, reason, outcome; analyst briefings and reports; competitor launches and pricing. |

## 5. Drift types and verdicts

Classify drift separately from the taxonomy category.

| Drift type | Definition |
|---|---|
| Field drift | Sales, SEs, or CSMs describe the market, persona, or pitch differently from core. |
| Asset drift | A deck, playbook, talk track, web page, or enablement document conflicts with core. |
| AI drift | An agent output contains a claim that cannot be traced to the SSOT. |
| Market drift | A competitive or analyst change is not reflected in core. |

Give each finding exactly one proposed verdict:

| Verdict | Use when |
|---|---|
| `fix-asset` | Canon is right; an asset or talk track is wrong. |
| `update-living` | Signal is worth recording, with no canon change yet. |
| `update-core` | Evidence shows canon is stale. Requires Gate 2. |
| `noise` | Signal is one-off, unsourced, or outside the ICP. Record why. |

Assign each finding confidence `high`, `medium`, or `low`. Group repeated signals;
two or more independent sources raise confidence. Confidence is not a claim tag.

## 6. Commands and required outputs

### `/setup <client>`

**Input:** supplied positioning documents, persona research, competitive notes,
decks, and related source material.

1. Extract every claim and map it to exactly one file and section.
2. Make every content line in every canonical SSOT file end with exactly one
   evidence tag: `[C]`, `[A]`, or `[G]`.
3. Set section statuses. Use `directional` by default when evidence is thin.
4. Add source-backed anti-patterns. Mark unsupported anti-patterns `[G]`.
5. List every gap in a closing `Gaps to close` table with file, section, missing
   evidence, and where to get it.

**Output:** all nine core and living files, `09-iteration.md`, `state.md`, and
`decisions/<today>-baseline.md`. Create empty `decisions/` and `comms/` directories
when needed. In the baseline decision, document the initial canon and sources.
Do not invent missing content to make a file look complete.

Initial setup does not bypass core approval. Return baseline core files and the
baseline decision as proposals until the human PMM explicitly approves them at
Gate 2. Only then persist the approved baseline. A request to set up the SSOT is
not itself approval of strategy inferred while drafting it.

### `/scan <client>`

**Input:** current SSOT plus new call transcripts, Slack exports, support tickets,
win/loss notes, assets, AI outputs, competitive digests, or other supplied inputs.

1. Save raw inputs into `comms/` using their filenames and dates. Never alter them.
2. Extract signals and classify each by the taxonomy.
3. Compare every signal with its relevant SSOT section.
4. Flag drift only when a signal conflicts with, extends, or is missing from SSOT.
5. Check supplied assets and AI outputs line by line against core and anti-patterns.
6. Assign a proposed verdict and confidence to each finding.
7. Group repeated signals and note independent sources.

Return a drift report with these columns:

| ID | Drift type | Taxonomy | Signal (short quote) | Source | SSOT section it hits | Tag | Proposed verdict | Confidence |
|---|---|---|---|---|---|---|---|---|

Then give the top three findings, one line each, and `Needs your call` questions.
Stop and wait for Gate 1. Do not edit canonical or living content as a result of a
scan before the PMM responds.

### Gate 1: `/confirm <IDs>` and `/reject <ID> <reason>`

The PMM decides whether drift is real. Confirmed findings become eligible for
`/propose`. A rejected finding is recorded in `09-iteration.md` under
`Taught: not drift`, with its reason. Apply these lessons in future scans. Accept
PMM changes to a proposed verdict.

### `/propose`

For each confirmed finding, prepare the appropriate proposal:

- **`fix-asset`:** name the asset, quote the offending line, and give a sourced
  replacement from core.
- **`update-living`:** show proposed section content as before and after. Set its
  status to `pending` unless its evidence meets the `current` standard.
- **`update-core`:** show before and after, supporting evidence, what the change
  replaces, and a one-line rationale.

For every proposal, use `manifest.yaml` to list affected agents that read the
changed file. List known assets that need updating. Stop and wait for Gate 2.

### Gate 2: `/approve <IDs>` and `/revise <ID> <notes>`

Do not write an approved change until the PMM approves its ID. A revision updates
the proposal using the PMM's notes and waits for approval. On approval, return
ready-to-commit files:

1. Each changed SSOT file in full, in its own code block headed by its path.
2. One `decisions/YYYY-MM-DD-<slug>.md` record per core change, using this schema:

```markdown
Date: YYYY-MM-DD
Decided by: <PMM name>
Decision: <approved canon change>
Replaces: <previous decision file or "baseline">
Evidence: <finding IDs and sources>
Affected files: <paths>
Affected agents: <manifest entries>
Affected assets: <known assets>
```

3. Updated `state.md`, regenerated by the reconciler.
4. A commit message.

Only approved Gate 2 changes may alter core. Changes to living content also
require confirmation through the workflow; do not write proposed content before
the gate that authorizes it. After the applicable gate authorizes each file
creation or change, commit and push that output to the project's GitHub-backed
repository. Gate 1 and Gate 2 remain mandatory. Never commit a core change before
explicit Gate 2 approval.

### `/stale <client>`

List every section past its threshold: file, section, last validated date, and the
evidence that would revalidate it. Apply the 90-day core and 30-day living limits.

### `/state <client>`

Regenerate `state.md` with counts by status per file, stale and contested sections,
open gaps, pending validations and next-cycle actions, last five decisions, and
last scan date with findings grouped by verdict. Only the reconciler writes this
file. Treat this command as the reconciler.

### `/brief <client>`

Write a team-facing Slack summary of what changed this cycle. Maximum ten lines.
Include what changed, what to stop saying, what to start saying, and which assets
were updated. Omit internal gate details.

### `/manifest`

**Input:** a list of agents or skills, each with a one-line description. Output a
repo-root `manifest.yaml` mapping each agent to the SSOT files it must read and
flag any required file that does not exist yet. Do not imply the mapped skills
have already been changed to consume the manifest.

```yaml
agents:
  - name: <agent-name>
    reads: [core/01-how-you-position-it.md, living/07-evidence.md]
    writes: [] # Living files only, and only through /scan.
    notes: <why these files are needed>
```

Use paths relative to `ssot/<client-slug>/`. Map each reader only to needed files.
No agent writes to core. An agent may write to a living file only through this
skill's scan and approval workflow. Flag missing files rather than inventing them.

### `/audit-output <client>`

**Input:** one AI-generated asset. Trace every claim to an SSOT section. Flag
untraceable claims as AI drift and name the anti-pattern or evidence gap they hit.
Do not silently repair or approve the asset.

## 7. Default behavior and safety invariants

- With no command, ask which client and which files were uploaded, then list
  commands.
- Never write to core without Gate 2 approval.
- Never delete a section. Mark it deprecated and name what replaced it.
- Never edit `comms/` after capture.
- `state.md` is written only by the reconciler.
- A claim belongs in exactly one SSOT file. When uncertain, pick one and explain
  the choice in `09-iteration.md`.
- After each gate, stop at its required wait point. Silence is not approval.
- Keep decisions auditable: preserve sources, IDs, affected files, readers, and
  known assets in the proposal and decision record.

## 8. Intended agent-to-file map

Use `/manifest` to produce the actual mapping for a project. The following are
starting points, not a requirement that downstream skills change in this commit.

| Skill | Likely files to read | Relationship |
|---|---|---|
| `product-marketing-context` | `core/00-what-it-is.md`, `core/01-how-you-position-it.md`, `core/02-product.md`, `core/03-who-it-is-for.md`, `living/07-evidence.md` | Lightweight bootstrap stays distinct. Existing context can be used when no SSOT exists; covered claims defer to SSOT when it does. Never auto-overwrite the context document. |
| `positioning-strategy` | `core/00-what-it-is.md`, `core/01-how-you-position-it.md`, `core/02-product.md`, `core/03-who-it-is-for.md`, `living/04-icp-signals.md`, `living/06-competitive.md`, `living/07-evidence.md` | Reads canon and field evidence. It may propose strategy; only SSOT gates can change canon. |
| `messaging-framework` | `core/00-what-it-is.md`, `core/01-how-you-position-it.md`, `core/02-product.md`, `core/03-who-it-is-for.md`, `living/07-evidence.md`, `living/08-objection-handling.md` | Uses core differentiators and researched persona messages. Never creates positioning or persona research standalone. |
| `buyer-personas` | `core/03-who-it-is-for.md`, `living/04-icp-signals.md`, `living/05-use-cases.md`, `living/07-evidence.md` | Uses canon and validates persona/ICP hypotheses with signals. |
| `customer-research` | `core/03-who-it-is-for.md`, `living/04-icp-signals.md`, `living/05-use-cases.md`, `living/07-evidence.md`, `living/08-objection-handling.md` | Generates sourced findings that may enter living files through the loop. |
| `competitor-profiling` | `core/00-what-it-is.md`, `core/01-how-you-position-it.md`, `living/06-competitive.md`, `living/07-evidence.md` | Uses current client context and contributes dated market evidence. |
| `sales-enablement` | `core/01-how-you-position-it.md`, `core/02-product.md`, `core/03-who-it-is-for.md`, `living/05-use-cases.md`, `living/07-evidence.md`, `living/08-objection-handling.md` | Builds rep assets from approved positioning, evidence, use cases, and objections. |
| `copywriting` | `core/00-what-it-is.md`, `core/01-how-you-position-it.md`, `core/02-product.md`, `core/03-who-it-is-for.md`, `living/07-evidence.md` | Uses approved claims and voice evidence; audit generated copy when requested. |
| `launch-strategy` | `core/00-what-it-is.md`, `core/01-how-you-position-it.md`, `core/02-product.md`, `core/03-who-it-is-for.md`, `living/04-icp-signals.md`, `living/05-use-cases.md`, `living/07-evidence.md` | Builds a launch from current canon and field evidence. |
| `market-launch` | `core/00-what-it-is.md`, `core/01-how-you-position-it.md`, `core/02-product.md`, `core/03-who-it-is-for.md`, `living/04-icp-signals.md`, `living/06-competitive.md`, `living/07-evidence.md` | Orchestrates a market launch using canon and market signals. |
| `launch-readiness-check` | `core/00-what-it-is.md`, `core/01-how-you-position-it.md`, `core/02-product.md`, `core/03-who-it-is-for.md`, `living/07-evidence.md`, `living/08-objection-handling.md` | Checks supplied launch assets against approved claims and anti-patterns. |

The direction is one-way: downstream skills read the manifest and SSOT when
configured. They do not govern SSOT decisions. Avoid requiring the SSOT skill to
read downstream-generated artifacts as truth; treat them as inputs to scan and
cite their original sources.
