"""Deterministic infrastructure regressions. No API calls or behavioral grading."""
import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from argparse import Namespace
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("harness", Path(__file__).parents[1] / "harness.py")
h = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(h)


class HarnessTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.skills_dir = self.root / "skills"
        self.local = self.skills_dir / "sample" / "evals"
        self.local.mkdir(parents=True)
        for name, value in {"ROOT": self.root, "SKILLS": self.skills_dir,
                            "OUT": self.root / "results", "CALIBRATION": self.root / "calibration",
                            "SPENT": 0.0, "BUDGET": None, "MOCK": False}.items():
            p = patch.object(h, name, value)
            p.start()
            self.addCleanup(p.stop)
        self.write(self.local / "fixtures" / "one.md", "FIRST CASE ONLY")
        self.write(self.local / "fixtures" / "two.md", "SECOND CASE ONLY")
        self.case = {"id": 1, "prompt": "Analyze evidence", "assertions": ["Preserves evidence"],
                     "files": ["fixtures/one.md"]}

    @staticmethod
    def write(path, text):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def args(self, **changes):
        values = dict(resume=None, evals=None, skills=None, trials=1, no_assertions=False,
                      model=h.DEFAULT_MODEL, judge=h.DEFAULT_MODEL, max_tokens=100, workers=2,
                      out=None, force=False, per_skill=1, seed=0)
        values.update(changes)
        return Namespace(**values)

    def skills(self, cases=None):
        return {"sample": {"body": "Sample skill", "desc": "Sample description",
                           "evals": cases if cases is not None else [self.case]}}

    def test_local_fixture(self):
        self.assertEqual(h.eval_fixture("sample", "fixtures/one.md"),
                         self.local / "fixtures" / "one.md")

    def test_repo_relative_fixture(self):
        ref = "skills/sample/evals/fixtures/one.md"
        self.assertEqual(h.eval_fixture("sample", ref), self.local / "fixtures" / "one.md")

    def test_repo_relative_standard(self):
        self.write(self.skills_dir / "other" / "SKILL.md", "Originating standard")
        self.assertIn("Originating standard", h.eval_prompt("sample", dict(self.case,
                      files=["skills/other/SKILL.md"])))

    def test_missing_files_and_empty_list_preserve_prompt(self):
        for case in ({"id": 1, "prompt": "unchanged"}, {"id": 1, "prompt": "unchanged", "files": []}):
            self.assertEqual(h.eval_prompt("sample", case), "unchanged")

    def test_missing_fixture_fails(self):
        with self.assertRaisesRegex(ValueError, "Missing"):
            h.eval_fixture("sample", "fixtures/missing.md")

    def test_directory_is_not_a_fixture(self):
        with self.assertRaisesRegex(ValueError, "Missing"):
            h.eval_fixture("sample", "fixtures")

    def test_malformed_path_types(self):
        for ref in (None, 42, {}, [], "", " ", " fixtures/one.md", "one\n.md", "one\\two.md"):
            with self.subTest(ref=ref), self.assertRaises(ValueError):
                h.eval_fixture("sample", ref)

    def test_malformed_files_container(self):
        for files in (None, "fixtures/one.md", {}, 42):
            with self.subTest(files=files), self.assertRaisesRegex(ValueError, "list"):
                h.eval_prompt("sample", dict(self.case, files=files))

    def test_absolute_and_traversal_rejected_even_inside_repo(self):
        for ref in (str(self.local / "fixtures/one.md"), "../evals/fixtures/one.md",
                    "../../../../outside.md", "C:/fixture.md"):
            with self.subTest(ref=ref), self.assertRaisesRegex(ValueError, "Unsafe"):
                h.eval_fixture("sample", ref)

    def test_invalid_skill_rejected(self):
        with self.assertRaisesRegex(ValueError, "Invalid fixture skill"):
            h.eval_fixture("../sample", "fixtures/one.md")

    def test_symlink_escape_rejected(self):
        with tempfile.TemporaryDirectory() as outside:
            target = Path(outside) / "outside.md"
            target.write_text("must not be loaded")
            (self.local / "fixtures/link.md").symlink_to(target)
            with self.assertRaisesRegex(ValueError, "escapes"):
                h.eval_fixture("sample", "fixtures/link.md")

    def test_ambiguous_local_and_root_match_rejected(self):
        self.write(self.root / "fixtures/one.md", "WRONG FILE")
        with self.assertRaisesRegex(ValueError, "Ambiguous"):
            h.eval_fixture("sample", "fixtures/one.md")

    def test_order_and_only_named_inputs(self):
        prompt = h.eval_prompt("sample", dict(self.case, files=["fixtures/two.md", "fixtures/one.md"]))
        self.assertLess(prompt.index("SECOND CASE ONLY"), prompt.index("FIRST CASE ONLY"))
        single = h.eval_prompt("sample", self.case)
        self.assertNotIn("SECOND CASE ONLY", single)
        self.assertEqual(single.count("FIRST CASE ONLY"), 1)

    def test_parallel_cases_do_not_leak(self):
        cases = [self.case, dict(self.case, id=2, files=["fixtures/two.md"]),
                 dict(self.case, id=3, files=[])] * 10
        with ThreadPoolExecutor(4) as ex:
            prompts = list(ex.map(lambda e: h.eval_prompt("sample", e), cases))
        for case, prompt in zip(cases, prompts):
            self.assertEqual("FIRST CASE ONLY" in prompt, case["id"] == 1)
            self.assertEqual("SECOND CASE ONLY" in prompt, case["id"] == 2)

    def test_invalid_utf8_surfaces(self):
        (self.local / "fixtures/binary.md").write_bytes(b"\xff")
        with self.assertRaises(UnicodeError):
            h.eval_prompt("sample", dict(self.case, files=["fixtures/binary.md"]))

    def test_lint_fails_for_bad_fixture(self):
        with contextlib.redirect_stdout(io.StringIO()), self.assertRaises(SystemExit) as ex:
            h.lint(self.skills([dict(self.case, files="not a list")]), None)
        self.assertEqual(ex.exception.code, 1)

    def test_lint_fails_for_unknown_handoff(self):
        with contextlib.redirect_stdout(io.StringIO()), self.assertRaises(SystemExit):
            h.lint(self.skills([dict(self.case, handoff_to="missing")]), None)

    def test_run_preflights_before_calls_or_result_creation(self):
        with patch.object(h, "request") as request, self.assertRaises(ValueError):
            h.run(self.skills([dict(self.case, files=["missing.md"])]), self.args())
        request.assert_not_called()
        self.assertFalse(h.OUT.exists())

    def exercise_run(self, cases):
        with patch.object(h, "request", return_value=("Output", "end_turn")) as request, \
             patch.object(h, "grade", return_value={"passed": True, "evidence": "stub"}) as grade, \
             patch.object(h, "score_rubric", return_value={}) as rubric, \
             contextlib.redirect_stdout(io.StringIO()):
            h.run(self.skills(cases), self.args())
        return request, grade, rubric

    def test_run_uses_same_evidence_for_baseline_and_loaded_and_judges(self):
        request, grade, rubric = self.exercise_run([self.case])
        self.assertEqual(request.call_count, 2)
        prompts = [c.args[1] for c in request.call_args_list]
        self.assertEqual(prompts[0], prompts[1])
        self.assertIn("FIRST CASE ONLY", prompts[0])
        self.assertTrue(all(c.kwargs["prompt"] == prompts[0] for c in grade.call_args_list))
        self.assertTrue(all(c.args[0] == prompts[0] for c in rubric.call_args_list))

    def test_run_without_fixtures_keeps_legacy_inputs(self):
        request, grade, rubric = self.exercise_run([dict(self.case, files=[])])
        self.assertTrue(all(c.args[1] == self.case["prompt"] for c in request.call_args_list))
        self.assertTrue(all(c.kwargs["prompt"] is None for c in grade.call_args_list))
        self.assertTrue(all(c.args[0] == self.case["prompt"] for c in rubric.call_args_list))

    def test_resume_rebuilds_when_fixture_changes(self):
        self.exercise_run([self.case])
        stamp = next(h.OUT.iterdir()).name
        self.write(self.local / "fixtures/one.md", "UPDATED EVIDENCE")
        with patch.object(h, "request", return_value=("Output", "end_turn")) as request, \
             patch.object(h, "grade", return_value={"passed": True}), \
             patch.object(h, "score_rubric", return_value={}), contextlib.redirect_stdout(io.StringIO()):
            h.run(self.skills(), self.args(resume=stamp))
        self.assertEqual(request.call_count, 2)
        self.assertIn("UPDATED EVIDENCE", request.call_args.args[1])

    def test_calibration_cache_changes_with_fixture_contents(self):
        with patch.object(h, "request", return_value=("Output", "end_turn")) as request, \
             contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            h.calibrate(self.skills(), self.args(skills="sample", out=str(self.root / "cal-one")))
            self.write(self.local / "fixtures/one.md", "UPDATED EVIDENCE")
            h.calibrate(self.skills(), self.args(skills="sample", out=str(self.root / "cal-two")))
        self.assertEqual(request.call_count, 4)
        self.assertIn("UPDATED EVIDENCE", request.call_args.args[1])
        self.assertEqual(len(list((h.OUT / "cache" / h.DEFAULT_MODEL).glob("*.json"))), 4)

    def test_grade_without_fixture_has_identical_legacy_payload(self):
        with patch.object(h, "call", return_value='{"passed": true}') as call:
            h.grade("Output", "Assertion", "model")
        self.assertEqual(call.call_args.args[1], "<output>\nOutput\n</output>\n\nAssertion: Assertion")

    def test_transitive_shared_contract_is_loaded_once_despite_cycle(self):
        self.write(self.skills_dir / "_shared/evidence-gaps.md", "Read ../_shared/ssot-consumption.md")
        self.write(self.skills_dir / "_shared/ssot-consumption.md", "Read ../_shared/evidence-gaps.md")
        files = h.shared_files("Read ../_shared/evidence-gaps.md twice ../_shared/evidence-gaps.md")
        self.assertEqual([p.name for p in files], ["evidence-gaps.md", "ssot-consumption.md"])

    def test_mode_references_reject_unsafe_paths_and_invalid_container(self):
        for refs in (["../secret.md"], ["/tmp/secret.md"], "one.md", [42]):
            with self.subTest(refs=refs), self.assertRaises(ValueError):
                h.eval_references("sample", {"references": refs})

    def test_run_preflights_missing_mode_reference_without_api_calls(self):
        case = dict(self.case, references=["skills/sample/references/missing.md"])
        with patch.object(h, "request") as request, self.assertRaisesRegex(ValueError, "Missing"):
            h.run(self.skills([case]), self.args())
        request.assert_not_called()
        self.assertFalse(h.OUT.exists())


if __name__ == "__main__":
    unittest.main()
