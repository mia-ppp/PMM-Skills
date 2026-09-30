"""Deterministic portfolio migration integrity. No model calls or grading."""
import importlib.util
import json
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location("portfolio_harness", Path(__file__).parents[1] / "harness.py")
h = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(h)


class PortfolioTests(unittest.TestCase):
    def test_every_legacy_case_has_a_live_unique_destination(self):
        skills = h.load_skills()
        migration = json.loads((h.SKILLS / "_shared/portfolio-migration.json").read_text())
        originals = set()
        for item in migration["eval_id_migrations"]:
            source = (item["from_skill"], item["from_id"])
            self.assertNotIn(source, originals)
            originals.add(source)
            self.assertIn(item["to_skill"], skills)
            matches = [e for e in skills[item["to_skill"]]["evals"] if e["id"] == item["to_id"]]
            self.assertEqual(len(matches), 1, item)
        for legacy, target in migration["legacy_routes"].items():
            self.assertNotIn(legacy, skills)

    def test_all_mode_instructions_and_fixtures_resolve(self):
        for name, skill in h.load_skills().items():
            for case in skill["evals"]:
                with self.subTest(skill=name, case=case["id"]):
                    h.eval_prompt(name, case)
                    refs = h.eval_references(name, case)
                    self.assertTrue(all(p.is_file() for p in refs))
                    self.assertNotEqual(case.get("handoff_to"), name)

    def test_five_gtm_scenarios_are_distinct_and_isolated(self):
        skill = h.load_skills()["go-to-market-strategy"]
        required = {"accepted", "conflict", "ongoing", "routing", "gaps"}
        cases = {Path(e["files"][0]).stem: e for e in skill["evals"] if e.get("files")}
        self.assertTrue(required <= set(cases))
        for key in required:
            case = cases[key]
            rendered = h.eval_prompt("go-to-market-strategy", case)
            self.assertIn(h.eval_fixture("go-to-market-strategy", case["files"][0]).read_text(), rendered)
            for other in required - {key}:
                self.assertNotIn(f'path="fixtures/{other}.md"', rendered)
            self.assertGreaterEqual(len(case["assertions"]), 3)

    def test_mode_guidance_only_enters_skill_system(self):
        skill = h.load_skills()["marketing-copy"]
        case = next(e for e in skill["evals"] if e.get("references"))
        guided = h.system_for(skill, "with_skill", "marketing-copy", case)
        baseline = h.system_for(skill, "baseline", "marketing-copy", case)
        self.assertIn("<skill_reference", guided)
        self.assertNotIn("<skill_reference", baseline)
        self.assertNotIn("<skill_reference", h.eval_prompt("marketing-copy", case))

    def test_three_independent_review_owners_survive(self):
        skills = h.load_skills()
        for name in ("output-quality-check", "messaging-consistency-audit", "launch-readiness-check"):
            self.assertIn(name, skills)
        self.assertIn("ssot-context-loop", skills)


if __name__ == "__main__":
    unittest.main()
