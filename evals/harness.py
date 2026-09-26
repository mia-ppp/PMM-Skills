#!/usr/bin/env python3
"""
PMM-Skills eval harness. Zero dependencies (Python 3.9+ stdlib only).

Five commands:
  lint       Static checks on every skill's evals.json. No API calls.
  route      Routing eval: can the model pick the right skill from every skill description?
             Reuses every eval prompt as a labeled test case. Cheapest, highest-signal run.
  run        Runs each eval prompt twice: with the skill loaded, and baseline (no skill).
             Grades every assertion with an LLM judge. Repeats N trials for variance.
  report     Aggregates results/ into results/REPORT.md.
  calibrate  Generates blind, shuffled outputs (with skill and baseline) for hand-grading
             the L2 rubrics in evals/rubrics/. The unblinding key goes to results/.

Usage:
  export ANTHROPIC_API_KEY=sk-...
  python evals/harness.py lint
  python evals/harness.py route --trials 1
  python evals/harness.py run --skills page-cro,copywriting --trials 3
  python evals/harness.py report
  python evals/harness.py calibrate

Add --mock to any command to exercise the pipeline with fake model calls (no key needed).
Mock results go to evals/results/mock/ so they never mix with real runs.
"""
import argparse, csv, json, os, random, re, statistics, sys, time, urllib.error, urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
OUT = ROOT / "evals" / "results"
CALIBRATION = ROOT / "evals" / "calibration"
API = "https://api.anthropic.com/v1/messages"
DEFAULT_MODEL = "claude-sonnet-5"
MAX_TOKENS = 16000
RETRYABLE = {408, 409, 429, 500, 502, 503, 504, 529}
MOCK = False

# ---------- model call ----------

def request(system, user, model, max_tokens=MAX_TOKENS):
    """One Messages API call. Returns (text, stop_reason)."""
    if MOCK:
        time.sleep(0.01)
        if "JUDGE" in system:
            return json.dumps({"passed": random.random() > 0.35, "evidence": "mock"}), "end_turn"
        if "ROUTER" in system:
            names = re.findall(r"^- ([a-z0-9-]+):", user, re.M)
            return random.choice(names + ["none"]), "end_turn"
        first = user.strip().splitlines()[0][:80]
        return f"## Quick Wins\nMock output referencing product-marketing-context.md.\n\nRequest: {first}", "end_turn"
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        sys.exit("Set ANTHROPIC_API_KEY or pass --mock")
    # No temperature: current models reject sampling params. Thinking is adaptive by default,
    # and its tokens count toward max_tokens, so even short calls get a generous cap.
    body = json.dumps({"model": model, "max_tokens": max_tokens, "system": system,
                       "messages": [{"role": "user", "content": user}]}).encode()
    req = urllib.request.Request(API, body, {"x-api-key": key, "anthropic-version": "2023-06-01",
                                             "content-type": "application/json"})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=600) as r:
                d = json.load(r)
            return "".join(b.get("text", "") for b in d["content"] if b["type"] == "text"), d.get("stop_reason")
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")[:500]
            if e.code not in RETRYABLE or attempt == 4:
                raise RuntimeError(f"API error {e.code}: {detail}") from None
            wait = float(e.headers.get("retry-after") or 2 ** attempt * 3)
        except (urllib.error.URLError, TimeoutError) as e:
            if attempt == 4:
                raise RuntimeError(f"Network error: {e}") from None
            wait = 2 ** attempt * 3
        time.sleep(wait)

def call(system, user, model, max_tokens=MAX_TOKENS):
    return request(system, user, model, max_tokens)[0]

# ---------- loading ----------

def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm = m.group(1) if m else ""
    get = lambda k: (re.search(rf"^{k}:\s*(.*)$", fm, re.M) or [None, ""])[1].strip().strip('"')
    return get("name"), get("description")

def load_skills():
    out = {}
    for p in sorted(SKILLS.glob("*/SKILL.md")):
        text = p.read_text()
        name, desc = frontmatter(text)
        ev = p.parent / "evals" / "evals.json"
        out[p.parent.name] = {"desc": desc, "body": text,
                              "evals": json.loads(ev.read_text())["evals"] if ev.exists() else []}
    return out

def pick(skills, arg):
    if not arg:
        return skills
    want = set(arg.split(","))
    missing = want - set(skills)
    if missing:
        sys.exit(f"Unknown skills: {', '.join(sorted(missing))}")
    return {k: v for k, v in skills.items() if k in want}

# ---------- lint ----------

PROCESS = re.compile(r"product-marketing-context|framework|section|format|structure|organized|follows|applies", re.I)

def lint(skills, _):
    rows, total = [], Counter()
    for name, s in skills.items():
        ev = s["evals"]
        if not ev:
            rows.append((name, "NO EVALS", "", "", ""))
            total["no_evals"] += 1
            continue
        a = [x for e in ev for x in e.get("assertions", [])]
        proc = sum(bool(PROCESS.search(x)) for x in a)
        urls = sum(bool(re.search(r"https?://", e["prompt"])) and not e.get("files") for e in ev)
        rows.append((name, len(ev), len(a), f"{proc/len(a):.0%}" if a else "-", urls))
        total["cases"] += len(ev); total["assertions"] += len(a); total["process"] += proc
    print(f"{'skill':28}{'cases':>7}{'asserts':>9}{'process%':>10}{'url-no-fixture':>16}")
    for r in rows:
        print(f"{r[0]:28}{str(r[1]):>7}{str(r[2]):>9}{str(r[3]):>10}{str(r[4]):>16}")
    print(f"\n{total['cases']} cases, {total['assertions']} assertions, "
          f"{total['process']/max(total['assertions'],1):.0%} check process/format, "
          f"{total['no_evals']} skills with no evals")
    print("process% = assertions a baseline fails by construction (they check the skill's own template).")

# ---------- routing ----------

ROUTER_SYS = ("ROUTER. You pick which skill an AI agent should load for a user request. "
              "Reply with exactly one skill name from the list, or 'none'. No other text.")

def route(skills, args):
    catalog = "\n".join(f"- {k}: {v['desc']}" for k, v in skills.items())
    cases = [(k, e["prompt"]) for k, v in pick(skills, args.skills).items() for e in v["evals"]]
    jobs = [(lbl, p, t) for lbl, p in cases for t in range(args.trials)]

    def one(j):
        lbl, p, _ = j
        reply = call(ROUTER_SYS, f"Skills:\n{catalog}\n\nUser request:\n{p}", args.model, 4000).split()
        return {"expected": lbl, "got": reply[0].strip("`'\".") if reply else "none", "prompt": p[:160]}

    with ThreadPoolExecutor(args.workers) as ex:
        res = list(ex.map(one, jobs))
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "routing.json").write_text(json.dumps(res, indent=2))
    acc = sum(r["expected"] == r["got"] for r in res) / len(res)
    print(f"Routing accuracy: {acc:.1%} over {len(res)} calls")
    conf = Counter((r["expected"], r["got"]) for r in res if r["expected"] != r["got"])
    for (e, g), n in conf.most_common(15):
        print(f"  {e:26} -> {g:26} x{n}")

# ---------- run + grade ----------

JUDGE_SYS = ("JUDGE. You grade one assertion against an AI agent's output. Be strict: "
             "pass only if the output clearly satisfies it. Reply with JSON only: "
             '{"passed": true|false, "evidence": "<short quote or reason>"}')

def with_skill_system(s):
    return ("You are a marketing agent. Follow this skill file exactly.\n\n<skill>\n"
            + s["body"] + "\n</skill>")

BASELINE_SYS = "You are a marketing agent. Help the user with their request."

def system_for(s, cfg):
    return with_skill_system(s) if cfg == "with_skill" else BASELINE_SYS

def grade(output, assertion, model):
    raw = call(JUDGE_SYS, f"<output>\n{output}\n</output>\n\nAssertion: {assertion}", model, 4000)
    try:
        return json.loads(re.search(r"\{.*\}", raw, re.S).group(0))
    except Exception:
        return {"passed": False, "evidence": f"unparseable judge reply: {raw[:80]}"}

def run(skills, args):
    stamp = time.strftime("%Y%m%d-%H%M%S")
    jobs = [(name, s, e, cfg, t) for name, s in pick(skills, args.skills).items()
            for e in s["evals"] for cfg in ("with_skill", "baseline") for t in range(args.trials)]
    print(f"{len(jobs)} runs queued")

    def one(j):
        name, s, e, cfg, t = j
        t0 = time.time()
        out, stop = request(system_for(s, cfg), e["prompt"], args.model)
        secs = round(time.time() - t0, 1)
        grades = [{"text": a, **grade(out, a, args.judge)} for a in e.get("assertions", [])]
        rec = {"skill": name, "eval_id": e["id"], "config": cfg, "trial": t, "seconds": secs,
               "stop_reason": stop, "output_chars": len(out), "expectations": grades,
               "pass_rate": sum(g["passed"] for g in grades) / max(len(grades), 1)}
        d = OUT / stamp / name / f"eval-{e['id']}" / cfg
        d.mkdir(parents=True, exist_ok=True)
        (d / f"trial-{t}.md").write_text(out)
        (d / f"grading-{t}.json").write_text(json.dumps(rec, indent=2))
        return rec

    with ThreadPoolExecutor(args.workers) as ex:
        recs = list(ex.map(one, jobs))
    (OUT / stamp / "runs.json").write_text(json.dumps(recs, indent=2))
    cut = [f"{r['skill']} #{r['eval_id']} {r['config']}" for r in recs if r["stop_reason"] != "end_turn"]
    if cut:
        print(f"Warning: {len(cut)} outputs did not end cleanly: {', '.join(cut[:10])}")
    print(f"Saved to {OUT / stamp}. Run `report` next.")

# ---------- report ----------

def report(skills, args):
    runs = sorted(OUT.glob("*/runs.json"))
    kp = OUT / "calibration-key.csv"
    cal = calibration_summary(kp, Path(args.out) if args.out else CALIBRATION) if kp.exists() else []
    if not runs and not cal:
        sys.exit("No runs or calibration grades found. Run `run`, or grade calibration outputs first.")
    lines = run_summary(json.loads(runs[-1].read_text()), runs[-1].parent.name) if runs else ["# Eval report", ""]
    rp = OUT / "routing.json"
    if rp.exists():
        rr = json.loads(rp.read_text())
        lines.append(f"Routing accuracy: {sum(r['expected']==r['got'] for r in rr)/len(rr):.1%}")
    lines += cal
    (OUT / "REPORT.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))

def run_summary(recs, name):
    by = defaultdict(lambda: defaultdict(list))
    for r in recs:
        by[r["skill"]][r["config"]].append(r["pass_rate"])
    ms = lambda xs: (statistics.mean(xs), statistics.pstdev(xs)) if xs else (0, 0)
    lines = [f"# Eval report ({name})", "",
             "| Skill | With skill | Baseline | Lift |", "|---|---|---|---|"]
    lifts = []
    for k in sorted(by):
        (wm, ws), (bm, bs) = ms(by[k]["with_skill"]), ms(by[k]["baseline"])
        lifts.append((wm - bm, k))
        lines.append(f"| {k} | {wm:.0%} ± {ws:.0%} | {bm:.0%} ± {bs:.0%} | {wm-bm:+.0%} |")
    # assertions that pass everywhere or nowhere carry no signal
    per_a = defaultdict(list)
    for r in recs:
        for g in r["expectations"]:
            per_a[(r["skill"], g["text"])].append(g["passed"])
    dead = [a for a, v in per_a.items() if all(v) or not any(v)]
    lines += ["", f"Mean lift: {statistics.mean(l for l,_ in lifts):+.0%}",
              f"Skills with lift under 5 pts: {', '.join(k for l,k in lifts if l < .05) or 'none'}",
              f"Non-discriminating assertions (always pass or always fail): {len(dead)} of {len(per_a)}"]
    return lines

# ---------- calibrate ----------

CALIBRATION_SKILLS = "positioning-strategy,messaging-framework,copywriting,page-cro,competitor-alternatives"
ANCHOR_POOL = 20
DIMENSIONS = ["grounded", "decisive", "usable", "sharp"]

def has_grades(path):
    if not path.exists():
        return False
    with path.open(newline="") as f:
        return any(any(v.strip() for k, v in row.items() if k != "id") for row in csv.DictReader(f))

def write_csv(path, header, rows):
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)

def calibrate(skills, args):
    out = Path(args.out) if args.out else (OUT / "calibration" if MOCK else CALIBRATION)
    outputs, grades_path, key_path = out / "outputs", out / "grades.csv", OUT / "calibration-key.csv"
    if outputs.exists() and any(outputs.iterdir()) and not args.force:
        sys.exit(f"{outputs} already has outputs. Pass --force to regenerate.")
    if has_grades(grades_path):
        sys.exit(f"{grades_path} contains grades. Move it aside before regenerating.")

    jobs = []
    for name, s in pick(skills, args.skills or CALIBRATION_SKILLS).items():
        evals = sorted(s["evals"], key=lambda e: e["id"])
        if len(evals) < args.per_skill:
            sys.exit(f"{name} has only {len(evals)} evals, need {args.per_skill}")
        jobs += [{"skill": name, "eval_id": e["id"], "prompt": e["prompt"], "config": cfg}
                 for e in evals[:args.per_skill] for cfg in ("with_skill", "baseline")]

    # Real runs cache each output so an interrupted run resumes instead of paying twice.
    cache = None if MOCK else OUT / "cache" / args.model
    if cache:
        cache.mkdir(parents=True, exist_ok=True)

    def one(j):
        cp = cache / f"{j['skill']}-{j['eval_id']}-{j['config']}.json" if cache else None
        if cp and cp.exists():
            return json.loads(cp.read_text())
        text, stop = request(system_for(skills[j["skill"]], j["config"]), j["prompt"], args.model)
        res = {"text": text, "stop_reason": stop}
        if cp:
            cp.write_text(json.dumps(res))
        print(f"  done: {j['skill']} #{j['eval_id']} {j['config']} ({stop})", file=sys.stderr)
        return res

    print(f"{len(jobs)} calibration outputs queued on {args.model}{' (mock)' if MOCK else ''}")
    with ThreadPoolExecutor(args.workers) as ex:
        for j, res in zip(jobs, ex.map(one, jobs)):
            j.update(res)

    seed = args.seed if args.seed is not None else random.SystemRandom().randrange(10 ** 9)
    random.Random(seed).shuffle(jobs)

    outputs.mkdir(parents=True, exist_ok=True)
    for stale in outputs.glob("A-*.md"):
        stale.unlink()
    key, split = [], []
    for i, j in enumerate(jobs, 1):
        bid = f"A-{i:02d}"
        (outputs / f"{bid}.md").write_text(
            f"# {bid}\n\n## Prompt\n\n{j['prompt'].strip()}\n\n## Output\n\n{j['text'].strip()}\n")
        key.append([bid, j["skill"], j["eval_id"], j["config"], args.model, j["stop_reason"], seed])
        split.append([bid, "anchor" if i <= ANCHOR_POOL else "holdout"])

    OUT.mkdir(parents=True, exist_ok=True)
    write_csv(key_path, ["id", "skill", "eval_id", "config", "model", "stop_reason", "seed"], key)
    write_csv(out / "split.csv", ["id", "split"], split)
    write_csv(grades_path, ["id"] + DIMENSIONS + ["notes"], [[k[0]] + [""] * 5 for k in key])

    cut = [k[0] for k in key if k[5] != "end_turn"]
    if cut:
        print(f"Warning: did not end cleanly: {', '.join(cut)}")
    print(f"Wrote {len(jobs)} blind outputs to {outputs}")
    print(f"Grade in {grades_path}. Key (do not open while grading): {key_path}")

def calibration_summary(key_path, cal_dir):
    """Unblinds grades.csv with the key: mean rubric score per config and dimension."""
    grades_path = cal_dir / "grades.csv"
    if not has_grades(grades_path):
        return []
    with key_path.open(newline="") as f:
        cfg = {r["id"]: r["config"] for r in csv.DictReader(f)}
    scores = defaultdict(lambda: defaultdict(list))
    graded, skipped = 0, []
    with grades_path.open(newline="") as f:
        for r in csv.DictReader(f):
            cells = [(r.get(d) or "").strip() for d in DIMENSIONS]
            if r["id"] not in cfg or not all(cells):
                if any(cells):
                    skipped.append(r["id"])  # partly graded: flag rather than half-count it
                continue
            for d, v in zip(DIMENSIONS, cells):
                try:
                    n = float(v)
                except ValueError:
                    n = None
                if n not in (0, 1, 2):
                    sys.exit(f"{grades_path}: {r['id']} {d} is {v!r}. Scores must be 0, 1, or 2.")
                scores[cfg[r["id"]]][d].append(n)
            graded += 1
    lines = ["", f"## Calibration rubric scores (0-2), {graded} graded outputs", "",
             "| Config | " + " | ".join(d.title() for d in DIMENSIONS) + " |", "|---" * (len(DIMENSIONS) + 1) + "|"]
    for c in ("with_skill", "baseline"):
        cells = [f"{statistics.mean(v):.2f} (n={len(v)})" if (v := scores[c][d]) else "-" for d in DIMENSIONS]
        lines.append(f"| {c} | " + " | ".join(cells) + " |")
    if skipped:
        lines.append(f"\nSkipped partly graded rows (need all four scores): {', '.join(skipped)}")
    return lines

# ---------- main ----------

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["lint", "route", "run", "report", "calibrate"])
    ap.add_argument("--skills", help="comma-separated subset")
    ap.add_argument("--trials", type=int, default=3)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--judge", default=DEFAULT_MODEL)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--mock", action="store_true")
    ap.add_argument("--per-skill", type=int, default=3, help="calibrate: prompts per skill")
    ap.add_argument("--seed", type=int, help="calibrate: shuffle seed (random if omitted, saved in the key)")
    ap.add_argument("--out", help="calibrate: output directory (default evals/calibration)")
    ap.add_argument("--force", action="store_true", help="calibrate: overwrite ungraded outputs")
    a = ap.parse_args()
    MOCK = a.mock
    if MOCK:
        OUT = OUT / "mock"
    {"lint": lint, "route": route, "run": run, "report": report, "calibrate": calibrate}[a.cmd](load_skills(), a)
