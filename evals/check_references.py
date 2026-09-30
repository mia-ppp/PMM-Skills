#!/usr/bin/env python3
"""Local skill, shared-file, eval-fixture and README reference checks. No API calls.

Runtime project paths and placeholder examples are not repository dependencies.
Graph edges show mentions, not execution order; reciprocal links need owner review.
"""
import json
import re
from pathlib import Path
from urllib.parse import unquote

import harness

ROOT = harness.ROOT


def check():
    skills = harness.load_skills()
    errors = []
    incoming = {name: set() for name in skills}
    edges = set()
    documents = [ROOT / "README.md", *harness.SKILLS.glob("*/SKILL.md"),
                 *harness.SKILLS.glob("_shared/*.md")]
    fixture_count = 0
    cases = 0
    for name, skill in skills.items():
        for section in re.findall(r"^## Related [Ss]kills\s*\n(.*?)(?=^## |\Z)",
                                  skill["body"], flags=re.M | re.S):
            targets = re.findall(r"(?:`|\*\*)([a-z][a-z0-9]*(?:-[a-z0-9]+)+)(?:`|\*\*)", section)
            for target in targets:
                if target not in skills:
                    errors.append(f"BROKEN_HANDOFF: {name} related skill -> {target}")
        for target in skills:
            if target != name and re.search(r"(?<![a-z0-9-])" + re.escape(target) + r"(?![a-z0-9-])", skill["body"]):
                incoming[target].add(name)
                edges.add((name, target))
        for path in harness.shared_files(skill["body"]):
            if not path.is_file():
                errors.append(f"BROKEN_HANDOFF: {name} -> {path.relative_to(ROOT)}")
        path = harness.SKILLS / name / "evals/evals.json"
        if not path.exists():
            continue
        data = json.loads(path.read_text())
        if data.get("skill_name") != name:
            errors.append(f"Eval skill_name mismatch: {path.relative_to(ROOT)}")
        ids = set()
        for case in skill["evals"]:
            cases += 1
            if not isinstance(case.get("id"), int) or case["id"] in ids:
                errors.append(f"Invalid/duplicate eval ID: {name} #{case.get('id')}")
            ids.add(case.get("id"))
            for field in ("prompt", "expected_output"):
                if not isinstance(case.get(field), str) or not case[field].strip():
                    errors.append(f"Invalid {field}: {name} #{case['id']}")
            assertions = case.get("assertions")
            if not isinstance(assertions, list) or not assertions or not all(isinstance(a, str) and a.strip() for a in assertions):
                errors.append(f"Invalid assertions: {name} #{case['id']}")
            if case.get("handoff_to") and case["handoff_to"] not in skills:
                errors.append(f"BROKEN_HANDOFF: {name} #{case['id']} -> {case['handoff_to']}")
            try:
                harness.eval_prompt(name, case)
                fixture_count += len(case.get("files", []))
            except (ValueError, OSError, UnicodeError) as ex:
                errors.append(f"Invalid fixture: {name} #{case['id']}: {ex}")

    for path in documents:
        text = path.read_text()
        if "meta-verify" in text:
            errors.append(f"Obsolete skill name: {path.relative_to(ROOT)}")
        # Ignore links inside fenced examples (for example, sample site URLs).
        prose = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", text, flags=re.M | re.S)
        for target in re.findall(r"\]\(([^)]+)\)", prose):
            target = target.strip("<>")
            if re.match(r"[a-z]+:", target) or target.startswith(("#", "/")):
                continue
            target = unquote(target.split("#")[0])
            if any(char in target for char in "<>{}[]*"):
                continue
            if not (path.parent / target).exists():
                errors.append(f"Broken link: {path.relative_to(ROOT)} -> {target}")
        for ref in re.findall(r"`((?:\.\./|references/|skills/)[^`\s]+\.(?:md|json|yaml))`", prose):
            if any(char in ref for char in "<>{}[]*"):
                continue
            if not (path.parent / ref).exists() and not (ROOT / ref).exists():
                errors.append(f"Broken literal path: {path.relative_to(ROOT)} -> {ref}")

    readme = (ROOT / "README.md").read_text()
    # Capability map links must cover the actual catalog, without duplicates.
    catalog = re.findall(r"\]\(skills/([a-z0-9-]+)/SKILL\.md\)", readme)
    if set(catalog) != set(skills):
        errors.append(f"README catalog mismatch: missing={sorted(set(skills)-set(catalog))}, unknown={sorted(set(catalog)-set(skills))}")
    for name in re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", readme):
        if name not in skills:
            errors.append(f"Unknown README skill name: {name}")

    orphans = sorted(name for name, sources in incoming.items() if not sources)
    reciprocal = len({tuple(sorted((a, b))) for a, b in edges if (b, a) in edges})
    print(f"{len(skills)} skills; {cases} evals; {fixture_count} fixture references; {len(edges)} cross-skill mentions.")
    print(f"ORPHAN_SKILL (no incoming SKILL.md mention): {', '.join(orphans) or 'none'}")
    print(f"{reciprocal} reciprocal mention pairs. These are not automatically CIRCULAR_HANDOFF failures.")
    for error in errors:
        print(error)
    if errors:
        return 1
    print("Skill/shared/fixture/handoff/README references: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(check())
