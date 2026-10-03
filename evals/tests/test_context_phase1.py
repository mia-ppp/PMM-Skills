"""Phase 1 eval input isolation and instruction/evidence separation. No API calls."""
import importlib.util
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location(
    "context_harness", Path(__file__).parents[1] / "harness.py")
h = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(h)


class ContextPhase1Tests(unittest.TestCase):
    def test_intelligence_routing_keeps_entry_decisions_separate(self):
        root = Path(__file__).resolve().parents[2]
        contract = (root / "skills/_shared/context-establishment.md").read_text()
        rows = [line for line in contract.splitlines() if line.startswith("| ")]
        external = next(row for row in rows if "External market structure" in row)
        entry = next(row for row in rows if "Company-specific sizing" in row)
        competitive = next(row for row in rows if "Competitive landscape" in row)
        self.assertIn("| market-intelligence |", external)
        self.assertNotIn("market-entry-brief", external)
        self.assertIn("| market-entry-brief", entry)
        self.assertIn("| competitor-profiling", competitive)
        case = next(case for case in h.load_skills()["product-marketing-context"]["evals"]
                    if case["id"] == 10)
        routing = " ".join(case["assertions"])
        for owner in ("market-intelligence", "market-entry-brief", "competitor-profiling"):
            self.assertIn(owner, routing)

    def test_starting_states_and_conflicts_have_isolated_evidence(self):
        skill = h.load_skills()["product-marketing-context"]
        cases = {case["id"]: case for case in skill["evals"]}
        expected = {8: "substantial", 9: "partial", 10: "scratch",
                    11: "contradictions", 12: "canon-conflict",
                    13: "hold-independent", 14: "return-integration"}
        for case_id, name in expected.items():
            with self.subTest(case=case_id):
                case = cases[case_id]
                self.assertEqual(case["files"], [f"fixtures/{name}.md"])
                prompt = h.eval_prompt("product-marketing-context", case)
                raw = h.eval_fixture("product-marketing-context", case["files"][0]).read_text()
                self.assertIn(raw, prompt)
                for other in set(expected.values()) - {name}:
                    self.assertNotIn(f'path="fixtures/{other}.md"', prompt)
                self.assertGreaterEqual(len(case["assertions"]), 4)

    def test_workspace_template_is_instruction_not_company_evidence(self):
        skill = h.load_skills()["product-marketing-context"]
        case = next(case for case in skill["evals"] if case["id"] == 8)
        template = h.eval_references("product-marketing-context", case)[0].read_text()
        self.assertIn(template, h.system_for(skill, "with_skill", "product-marketing-context", case))
        self.assertNotIn(template, h.system_for(skill, "baseline", "product-marketing-context", case))
        self.assertNotIn(template, h.eval_prompt("product-marketing-context", case))

    def test_specialist_smokes_resolve_without_live_sources(self):
        names = ("customer-research", "ssot-context-loop", "competitor-profiling",
                 "win-loss-intelligence", "objection-intelligence", "icp-and-buyer-personas",
                 "market-entry-brief", "pricing-strategy", "positioning-strategy",
                 "messaging-framework", "competitor-alternatives", "content-strategy",
                 "launch-strategy")
        skills = h.load_skills()
        for name in names:
            with self.subTest(skill=name):
                case = next(case for case in skills[name]["evals"] if case["id"] == 100)
                self.assertEqual(len(case["files"]), 1)
                prompt = h.eval_prompt(name, case)
                self.assertIn("Fictional Maple source bundle", prompt)
                self.assertTrue(all(path.is_file() for path in h.eval_references(name, case)))
                self.assertNotEqual(case.get("handoff_to"), name)


if __name__ == "__main__":
    unittest.main()
