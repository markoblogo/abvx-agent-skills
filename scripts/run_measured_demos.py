#!/usr/bin/env python3
"""Run nine synthetic cases in fresh Codex sessions, with and without one skill.

Uses the operator's authenticated Codex CLI; incurs normal model usage.
No external services or real repositories are evaluation targets.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
ISOLATION_FLAGS = [
    "--disable", "apps", "--disable", "plugins", "--disable", "skill_search",
    "-c", "project_doc_max_bytes=0",
]


def isolation_violations(events):
    """Fail a run that reads an external local skill despite discovery isolation."""
    violations = []
    for event in events:
        item = event.get("item", {})
        command = item.get("command", "")
        if event.get("type") == "item.completed" and any(root in command for root in ("/.agents/skills", "/.codex/skills")):
            violations.append("External skill access detected")
    return violations


def cases():
    result = []
    patches = [
        ("page-count", "def pages(total, size):\n    if total < 0 or size <= 0:\n        raise ValueError('invalid pagination')\n    return total // size\n",
         "Fix pages: a partially filled last page must count as a page. Preserve validation.",
         "assert pages(0, 10)==0\nassert pages(1,10)==1\nassert pages(20,10)==2\nassert pages(21,10)==3\nfor t,s in [(-1,10),(1,0)]:\n    try: pages(t,s)\n    except ValueError: pass\n    else: raise AssertionError('validation lost')\n"),
        ("stable-unique", "def unique(values):\n    return list(set(values))\n",
         "Fix unique so it returns distinct hashable values in their original first-seen order.",
         "assert unique(['z','a','z','b'])==['z','a','b']\nassert unique([])==[]\nassert unique([3,1,3,2])==[3,1,2]\n"),
        ("inclusive-window", "def within(value, lower, upper):\n    if lower > upper:\n        raise ValueError('reversed bounds')\n    return lower < value < upper\n",
         "Fix within: the documented interval includes both endpoints. Preserve reversed-bound validation.",
         "assert within(2,2,5)\nassert within(5,2,5)\nassert within(3,2,5)\nassert not within(6,2,5)\nassert within(2,2,2)\ntry: within(3,5,2)\nexcept ValueError: pass\nelse: raise AssertionError('validation lost')\n"),
    ]
    for name, source, task, checks in patches:
        result.append(dict(id=name, skill="minimal-diff-builder", kind="patch",
                           files={"app.py": source, "README.md": "Small Python utility. Use Python 3. Standard library only.\n",
                                  "unrelated.py": "def greeting(name):\n    return f'Hello {name}'\n"},
                           prompt=task + " Make the change in this workspace and verify it.", checks=checks))
    for number, (key, value) in enumerate([("retry_limit", "7"), ("request_timeout", "2500"), ("batch_limit", "40")], 1):
        files = {"README.md": "Service configuration lives in config/. Runtime code lives in src/. Archived migration notes live in archive/.\n",
                 "config/runtime.json": json.dumps({key: int(value), "environment": "production"}),
                 "src/settings.py": f"import json\nfrom pathlib import Path\n\ndef current():\n    return json.loads(Path('config/runtime.json').read_text())['{key}']\n"}
        for i in range(60):
            files[f"archive/migration-{i:02}.md"] = (f"Historical sample {i}; not active configuration.\n" + f"Previous {key}: {i+100}. Archived discussion; obsolete.\n" * 45)
        result.append(dict(id=f"config-lookup-{number}", skill="token-efficient-execution", kind="lookup", files=files,
                           prompt=f"Find the active production value of {key} and the code that reads it. Reply with a JSON object containing value (integer), config_path, and reader_path. Do not change files.",
                           expected={"value": int(value), "config_path": "config/runtime.json", "reader_path": "src/settings.py"}))
    packets = [
        ("build-only", "Commit abc123 is the reviewed commit. Tests and package build passed on abc123. Deployment was queued but no completed deployment receipt exists. No HTTP or browser observations exist. Owner approved publication of this commit. A draft announcement says 'live now'.",
         {"overall": "PARTIAL", "repository": "PROVEN", "build": "PROVEN", "deployment": "UNKNOWN", "http": "UNKNOWN", "browser": "UNKNOWN", "approval": "PROVEN"}),
        ("broken-route", "Commit def456 is reviewed. Tests and build passed. Deployment dep-42 completed for def456. An observed GET /checkout returned HTTP 500. Browser checkout failed with that error. Owner approved deployment. A deployment dashboard says 'success'.",
         {"overall": "BLOCKED", "repository": "PROVEN", "build": "PROVEN", "deployment": "PROVEN", "http": "BLOCKED", "browser": "BLOCKED", "approval": "PROVEN"}),
        ("unapproved-cutover", "Commit ghi789 is reviewed. Tests and build passed. Deployment dep-43 completed for ghi789. HTTP checks returned 200 for / and /checkout on the intended release URL. Desktop and mobile browser checks of those routes passed without console errors. Owner explicitly says approval is pending: do not publish the announcement or switch traffic yet. The developer calls it 'ready to ship'.",
         {"overall": "PARTIAL", "repository": "PROVEN", "build": "PROVEN", "deployment": "PROVEN", "http": "PROVEN", "browser": "PROVEN", "approval": "UNKNOWN"}),
    ]
    for name, packet, expected in packets:
        result.append(dict(id=name, skill="public-release-verification", kind="release",
                           files={"evidence.txt": packet + "\nAll evidence in this synthetic fixture is authoritative; do not access external systems. Scope: repository, build, deployment, HTTP, browser, approval only. Other domains are N/A for this exercise.\n"},
                           prompt="Review evidence.txt and report release readiness. Return a JSON object with overall, repository, build, deployment, http, browser, approval (each PROVEN, PARTIAL, BLOCKED, or UNKNOWN), plus can_announce_live (boolean). For approval, pending approval without a decision is UNKNOWN. Do not change files or take external actions.",
                           expected={**expected, "can_announce_live": False}))
    return result


def parse_answer(text):
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    return json.loads(text)


def grade(case, workspace, answer):
    if case["kind"] == "patch":
        completed = subprocess.run(["python3", "-I", "-c", (workspace / "app.py").read_text() + "\n" + case["checks"]], capture_output=True, text=True, timeout=15)
        return {"passed": completed.returncode == 0, "details": completed.stderr[-1000:]}
    try:
        actual = parse_answer(answer)
        mismatches = {k: {"expected": v, "actual": actual.get(k)} for k, v in case["expected"].items() if actual.get(k) != v}
        return {"passed": not mismatches, "mismatches": mismatches}
    except (ValueError, AttributeError) as exc:
        return {"passed": False, "error": str(exc)}


def run(command, **kwargs):
    return subprocess.run(command, check=True, capture_output=True, text=True, **kwargs).stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-dir", type=Path, required=True, help="Fresh private directory outside the source repo")
    parser.add_argument("--output", type=Path, required=True, help="Fresh directory for publishable evidence")
    parser.add_argument("--model", required=True)
    parser.add_argument("--effort", default="medium")
    parser.add_argument("--only", help="Run just one case ID for harness checks")
    args = parser.parse_args()
    private, output = args.work_dir.resolve(), args.output.resolve()
    private.mkdir(parents=True, exist_ok=False)
    output.mkdir(parents=True, exist_ok=False)
    home = private / "codex-home"
    home.mkdir()
    auth = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "auth.json"
    if auth.exists():
        (home / "auth.json").symlink_to(auth)
    environment = dict(os.environ, CODEX_HOME=str(home))
    # CODEX_HOME alone does not exclude ~/.agents/skills. Disable concrete paths.
    roots = [Path.home() / ".agents/skills", Path.home() / ".codex/skills", home / "skills"]
    disabled = {str(p) for root in roots for p in root.rglob("SKILL.md")}
    # System skills are materialized at session startup in the fresh home.
    system = Path.home() / ".codex/skills/.system"
    disabled.update(str(home / "skills/.system" / p.relative_to(system)) for p in system.rglob("SKILL.md"))
    disable_config = "skills.config=[" + ",".join("{path=" + json.dumps(p) + ",enabled=false}" for p in sorted(disabled)) + "]"
    flags = [*ISOLATION_FLAGS, "-c", disable_config]
    probe_dir = private / "isolation-probe"
    probe_dir.mkdir()
    probe = subprocess.run(["codex", "exec", "--ignore-user-config", "--ephemeral", "--skip-git-repo-check", *flags, "-C", str(probe_dir), "-s", "read-only", "-m", args.model, "-c", f'model_reasoning_effort="{args.effort}"', "--json", "List the names of any available skills in your initial context. Do not use tools, read files, or infer skill names. If none are listed, reply NONE."], env=environment, text=True, capture_output=True, timeout=120)
    (private / "isolation-probe.jsonl").write_text(probe.stdout)
    probe_events = [json.loads(line) for line in probe.stdout.splitlines() if line.startswith("{")]
    messages = [e["item"]["text"].strip() for e in probe_events if e.get("type") == "item.completed" and e.get("item", {}).get("type") == "agent_message"]
    if probe.returncode or messages != ["NONE"]:
        raise RuntimeError("Initial skill inventory is not empty; isolation probe failed")
    (output / "isolation-check.json").write_text(json.dumps({"initial_skill_inventory": "NONE", "disabled_paths_count": len(disabled), "method": "Explicit skills.config path disables; apps/plugins/skill_search off; no project instructions", "excluded_from_task_metrics": True}, indent=2) + "\n")
    selected = [c for c in cases() if not args.only or c["id"] == args.only]
    if not selected:
        raise ValueError("No matching cases")
    manifest = dict(model=args.model, reasoning_effort=args.effort, host=platform.platform(),
                    cli=run(["codex", "--version"]).strip(), repeats=1,
                    source_commit=run(["git", "rev-parse", "HEAD"], cwd=ROOT).strip(),
                    isolation_flags=ISOLATION_FLAGS, explicit_skill_path_disables=len(disabled),
                    grader_python=run(["python3", "--version"]).strip(),
                    runner_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                    methodology="Paired synthetic pilot; skill body prepended only in with_skill arm; no automatic activation eval; no held-out claim.", cases=selected)
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    results = []
    for index, case in enumerate(selected):
        # Alternate arm order; run serially to avoid resource contention.
        for arm in (["without_skill", "with_skill"] if index % 2 == 0 else ["with_skill", "without_skill"]):
            label = case["id"] + "--" + arm
            workspace = private / label
            workspace.mkdir()
            for name, content in case["files"].items():
                path = workspace / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
            run(["git", "init", "-q"], cwd=workspace)
            run(["git", "add", "."], cwd=workspace)
            run(["git", "-c", "user.name=Demo", "-c", "user.email=demo@example.invalid", "commit", "-qm", "fixture"], cwd=workspace)
            skill = (ROOT / "skills" / case["skill"] / "SKILL.md").read_text()
            prompt = case["prompt"]
            if arm == "with_skill":
                prompt = "Apply the following skill to the task. Referenced companion skills are unavailable in this isolated evaluation.\n<skill>\n" + skill + "\n</skill>\n\nTask:\n" + prompt
            destination = output / label
            destination.mkdir()
            (destination / "prompt.txt").write_text(prompt + "\n")
            answer_path = private / (label + ".answer.txt")
            command = ["codex", "exec", "--ignore-user-config", "--ephemeral", "--skip-git-repo-check", *flags, "-C", str(workspace), "-s", "workspace-write" if case["kind"] == "patch" else "read-only", "-m", args.model, "-c", f'model_reasoning_effort="{args.effort}"', "--json", "-o", str(answer_path), "-"]
            started = time.time()
            print("RUN", label, flush=True)
            with (private / (label + ".jsonl")).open("w") as stdout, (private / (label + ".stderr")).open("w") as stderr:
                try:
                    process = subprocess.run(command, input=prompt, text=True, stdout=stdout, stderr=stderr, env=environment, timeout=300)
                    returncode = process.returncode
                except subprocess.TimeoutExpired:
                    returncode = 124
            elapsed = time.time() - started
            raw = (private / (label + ".jsonl")).read_text()
            events = [json.loads(line) for line in raw.splitlines() if line.startswith("{")]
            violations = isolation_violations(events)
            usage = next((event["usage"] for event in reversed(events) if event.get("type") == "turn.completed"), None)
            answer = answer_path.read_text() if answer_path.exists() else ""
            scored = grade(case, workspace, answer) if returncode == 0 and usage else {"passed": False, "error": "incomplete agent run"}
            # Publish only synthetic task traces; strip local paths and ephemeral thread IDs.
            replacements = [(str(workspace), "<workspace>"), (str(private), "<private>"), (str(Path.home()), "<home>")]
            for old, new in replacements:
                raw, answer = raw.replace(old, new), answer.replace(old, new)
            sanitized = []
            for line in raw.splitlines():
                event = json.loads(line)
                if "thread_id" in event:
                    event["thread_id"] = "<ephemeral>"
                sanitized.append(json.dumps(event))
            (destination / "events.jsonl").write_text("\n".join(sanitized) + "\n")
            (destination / "answer.txt").write_text(answer)
            # Include untracked additions in diff metrics without modifying their content.
            run(["git", "add", "-N", "."], cwd=workspace)
            diff = run(["git", "diff", "--no-ext-diff"], cwd=workspace)
            stats = run(["git", "diff", "--numstat"], cwd=workspace)
            (destination / "changes.diff").write_text(diff)
            rows = [line.split("\t") for line in stats.splitlines()]
            metrics = dict(case=case["id"], skill=case["skill"], arm=arm, returncode=returncode,
                           started_at_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(started)),
                           duration_seconds=round(elapsed, 3), usage=usage, isolation_violations=violations,
                           changed_files=[row[2] for row in rows],
                           changed_lines=sum(int(a)+int(b) for a,b,_ in rows if a.isdigit() and b.isdigit()),
                           skill_sha256=hashlib.sha256(skill.encode()).hexdigest(), grade=scored)
            (destination / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n")
            results.append(metrics)
            (output / "results.json").write_text(json.dumps(results, indent=2) + "\n")
            print("DONE", label, "pass=" + str(scored["passed"]), "usage=" + str(usage), flush=True)
            if violations:
                raise RuntimeError("Isolation failure; do not publish this run")
    return 0 if all(r["returncode"] == 0 and r["usage"] for r in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
