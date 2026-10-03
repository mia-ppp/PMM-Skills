# Context workspace template

Use in the user's project, not the skill repository. Read
`../../_shared/context-establishment.md` for required fields and meanings.
Keep familiar context headings for compatibility. Reference approved context
rather than duplicating canon; preserve existing full bootstrap personas.
Include only applicable context, with missing relevant fields labeled Gap.
The registers can link existing domain artifacts instead of copying reports.

```markdown
---
contract: pmm-context-v1
artifact: context-workspace
project: <active-project>
product_scope: <product-and-applicable-scope>
id: CTX-001
version: 1
updated: YYYY-MM-DD
owner: product-marketing-context
goal: <user-goal-or-unknown>
return_to: product-marketing-context
---
# Product Marketing Context

*Provisional workspace. Saving does not approve canon.*

## Inputs and assumptions
[Use the shared evidence-gap note. Identify inspected versus unavailable sources.]

## Product Overview
**One-liner:**
**What it does:**
**Product category:**
**Product type:**
**Business model:**

## Target Audience
**Primary audience:** [segment] (Sourced / Assumed / Gap)
**Alternate audiences:**
- [segment] (Sourced / Assumed / Gap)
**Target companies:**
**Decision-makers:**
**Primary use case:**
**Jobs to be done:**
-
**Use cases:**
-

## Personas
| Persona | Cares about | Challenge | Value we promise |
|---------|-------------|-----------|------------------|
| | | | |

### Persona references / full bootstrap profiles
[For each persona: source path/section, version/review date, approval status
and approval reference, known gaps. Missing metadata stays Gap.
Reference applicable SSOT profiles without duplicating canon.
Otherwise retain the complete attribute profile from icp-and-buyer-personas:
background/responsibilities, triggers, pains, stakes/internal pressures,
current behavior/alternatives, discovery, evaluation context/criteria,
objections/risks, proof requirements, practitioner language, desired success/jobs,
and committee influence/authority, with source labels and confidence/gaps.
Preserve buying-committee and anti-persona detail alongside the profiles.]

## Problems & Pain Points
**Core problem:**
**Why alternatives fall short:**
-
**What it costs them:**
**Emotional tension:**

## Competitive Landscape
**Direct:** [Competitor], which falls short because...
**Secondary:** [Approach], which falls short because...
**Indirect:** [Alternative], which falls short because...

## Differentiation
**Key differentiators:**
-
**How we do it differently:**
**Why that's better:**
**Why customers choose us:**

## Objections
| Objection | Response |
|-----------|----------|
| | |

**Anti-persona:**

## Switching Dynamics
**Push:**
**Pull:**
**Habit:**
**Anxiety:**

## Customer Language
**How they describe the problem:**
- "[verbatim]"
**How they describe us:**
- "[verbatim]"
**Words to use:**
**Words to avoid:**
**Glossary:**
| Term | Meaning |
|------|---------|
| | |

## Brand Voice
**Tone:**
**Style:**
**Personality:**

## Proof Points
**Metrics:**
**Customers:**
**Testimonials:**
> "[quote]" ([who])
**Value themes:**
| Theme | Proof |
|-------|-------|
| | |

## Goals
**Business goal:**
**Conversion action:**
**Current metrics:**

## Positioning
**Statement:** [Product] is a [category + one short differentiating phrase] for [segment].

**Derivation trace:**
| Slot | Filled with | Source | Label |
|---|---|---|---|
| Category | | | Sourced / Assumed / Gap |
| Differentiating phrase | | | |
| Segment | | | |
| Trigger | [the event that starts the search] | | |

**Capabilities:**
| Capability | What it does for the buyer | Proof | Buyer voice | Label |
|---|---|---|---|---|
| | | | | Sourced / Assumed / Gap |

## Persona message map
| Persona (buying role) | What matters to them | Message | Proof label |
|---|---|---|---|
| [Role-based name] (champion) | | | Sourced / Assumed / Gap |

## Material inventory
| SRC ID | Location / locator | Type / reporter / role | Event date / version / ingested | Scope / coverage | Access / inspected portions | Lineage / duplicates | Limitations |
|---|---|---|---|---|---|---|---|

## Findings index
| FND ID | Statement / kind | Label | SRC IDs / locators | Supporting / opposing FND IDs | Scope | Method / sample / denominator | Confidence / rationale | Approval reference | Limits / review trigger |
|---|---|---|---|---|---|---|---|---|---|

## Contradictions
| CTR ID | Findings | Scope / type | Affected decision / severity | Owner | Proposed disposition / status | Resolution evidence |
|---|---|---|---|---|---|---|

## Context readiness
Goal: [user goal]. Intended action: [research / strategy proposal / draft / approved execution].
| Requirement / decision | Why needed | Source / version | Support | Authority | Health | GAP ID | Evidence readiness | Permitted next action | Approval dependency |
|---|---|---|---|---|---|---|---|---|---|
[Use PROCEED, PROCEED PROVISIONALLY or HOLD THIS DECISION. For provisional rows,
record assumption, understood risk, permitted scope and validation trigger.
For holds, name closure criteria and work that can continue independently.]

## Research gaps
| GAP ID / question | Affected goal / decision | Existing FND IDs | What changes if wrong | Priority / type | Primary owner / contributors | Method / completion criteria | Status / dependencies | Return to |
|---|---|---|---|---|---|---|---|---|

## Research handoffs and returns
[Use named HND records with linked GAP IDs, exact question, source/finding
references, approved context/version, hypotheses/opposing evidence, scope,
constraints/exclusions/dependencies, requested return/completion criteria,
owner/contributors and return_to. Index specialist artifacts and returned IDs.
Track answered, partially answered, inconclusive or unable to complete.]

## Context proposals
[One PRP record per proposed context change: exact wording and scope, existing
wording/reference, findings/sources, assumptions/interpretation/conflicts, domain
owner, destination, proposed authority/section status, validation/permitted uses,
affected readers/decisions/assets and the explicit human decision required.]

## Approved replacements and proposal history
[Reference approved SSOT destinations and decision IDs when supplied by SSOT.
Keep rejected/superseded proposal history and unresolved proposals distinct.]

## Evidence gaps
| Rank | Item | Label | Why it matters | How to resolve | Owner | Resolve by |
|---|---|---|---|---|---|---|
```
