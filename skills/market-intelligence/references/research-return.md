# Market research evidence and specialist return

The shared context-establishment contract owns the schema. This reference adds
market checks and a compatible minimum for installations without that contract.
Do not override a present shared contract with this template.

## Evidence and confidence

Keep Sourced / Assumed / Gap separate from kind, confidence, approval, and health.
A cited forecast establishes what its author forecast, not verified future demand.
Use High / Medium / Low confidence with finding-specific rationale: directness,
scope fit, method, independence, bias, freshness, and counterevidence.
No universal source-count threshold establishes sufficiency. A single authoritative
scoped record can substantiate an event; broad adoption claims need suitable
population evidence. Separate observation confidence from implication confidence.
Keep limitations visible even at High confidence. Reuse does not strengthen evidence.

## Compatible minimum packet

Preserve existing project-scoped IDs. Assign stable IDs only as needed.
Omit inapplicable envelope fields; unknown source metadata stays explicit.

```yaml
contract: pmm-context-v1
artifact: research-return
project: [project]
product_scope: [scope]
id: [return ID]
version: [artifact version]
updated: [date]
owner: market-intelligence
goal: [question/intended action]
return_to: [originating PMC workflow or requester]
```

Open with Inputs and assumptions, applicable canon/version, selected mode,
scope, inspected coverage, HND/GAP IDs, and return status:
answered | partially answered | inconclusive | unable to complete.

Source inventory: SRC ID; location/exact locator; type; author/reporter/role;
event/collection date; source version; ingestion date; scope/coverage;
inspection state; original/derivative IDs; limitations/access/use restrictions.

Finding register: FND ID; statement/kind (evidence, interpretation, assumption,
historical/current approved decision, unknown); evidence label; SRC IDs/locators;
supporting/opposing findings; scope; method/formula with labeled inputs;
meaningful sample/denominator; confidence/rationale; real approval reference or
explicit unapproved/unknown status; limits; expiry/review trigger.

Contradiction register: CTR ID; linked findings; scope; type; affected decisions;
severity; owner; proposed disposition/status; resolution evidence or smallest test.
Classify scope, time/version, definition/measurement, reporter, evidence versus
interpretation, decision conflict, factual conflict, or evidence against canon.
Do not resolve by newest wording, popularity, or count. Demonstrated scope/time/
definition differences can explain apparent conflicts; record the reasoning.
An unresolved consequential conflict holds dependent claims, not all research.
One material contradiction can warrant review even if one-off or outside the ICP.

Completion/return: questions/GAP IDs addressed; method and limitations; criteria
met/unmet; unanswered questions; domain artifact link; unapproved implications;
suggested destinations; consumer/owner handoffs. A report alone does not close a
gap. Preserve findings with supersession links instead of silently replacing them.

## Readiness and approval

Use the goal/action-specific readiness table:

| Requirement | Why needed | Source/version | Support | Authority | Health | GAP ID | Evidence readiness | Permitted next action | Approval dependency |
|---|---|---|---|---|---|---|---|---|---|

Support: evidence, interpretation, assumption, unknown.
Authority: approved, proposed, unapproved, approval unknown.
Health: current, stale, conflicting, superseded, missing.

- PROCEED means sufficient evidence for this action, never approval.
- PROCEED PROVISIONALLY records assumption, risk, permitted scope, validation trigger.
- HOLD THIS DECISION names consequential gap, owner, and closure criteria.
  Continue independent work. Missing approval is a separate dependency.

PMC integrates returns and consolidates gaps. Suggest market/category evidence
for living/07-evidence.md or a scoped SSOT-owned approved reference without
writing canon. Initial baseline: setup proposal → Gate 2. Existing canon:
scan → Gate 1 → proposal → Gate 2. Human approval is mandatory for canon changes.
Correcting or saving research never approves strategic inferences.

End with ranked Evidence gaps covering every Assumed/Gap item, top five in the
body and remainder in an appendix. Include counterfactual impact, priority/type,
existing findings, retrieval/test, primary owner/contributors, completion criteria,
status, dependencies, return_to, and resolution milestone. Mark suggested owners
and milestones as suggestions rather than inventing commitments.


## Return completeness check

Before delivering, check each finding for scope, source/locator, method, confidence
rationale, approval status, limits, and review trigger. Mark missing metadata
unknown; a generic artifact note does not supply missing field-level status.
Check each contradiction and gap against the required fields above. Show support,
authority, health, permitted action, and approval dependency for task-critical
readiness items. Report unmet completion criteria instead of claiming a complete
return because the domain report exists.
