#!/usr/bin/env python3
"""Run the bounded ABVX versus Chisle benchmark in isolated Codex sessions."""
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
ARMS = ("baseline", "abvx", "abvx_chisle")
ARM_ORDERS = (
    ARMS,
    ("abvx", "abvx_chisle", "baseline"),
    ("abvx_chisle", "baseline", "abvx"),
)
ISOLATION_FLAGS = [
    "--disable", "apps", "--disable", "plugins", "--disable", "skill_search",
    "-c", "project_doc_max_bytes=0",
]


def cases():
    return [
        {
            "id": "ttl-units", "kind": "coding",
            "files": {
                "app.py": "def is_expired(issued_at_seconds, ttl_seconds, now_ms):\n    if issued_at_seconds < 0 or ttl_seconds < 0 or now_ms < 0:\n        raise ValueError('timestamps must be non-negative')\n    return now_ms >= issued_at_seconds + ttl_seconds\n",
                "test_app.py": "from app import is_expired\n\ndef test_expiry_boundary():\n    assert not is_expired(100, 30, 129_999)\n    assert is_expired(100, 30, 130_000)\n",
            },
            "prompt": "Fix is_expired: issued_at_seconds and ttl_seconds are seconds, while now_ms is milliseconds. Preserve validation. Make the smallest correct change and run the tests.",
            "checks": "assert not is_expired(100,30,129999)\nassert is_expired(100,30,130000)\nassert is_expired(0,0,0)\nfor args in [(-1,1,1),(1,-1,1),(1,1,-1)]:\n try: is_expired(*args)\n except ValueError: pass\n else: raise AssertionError('validation lost')\n",
        },
        {
            "id": "retry-budget", "kind": "coding",
            "files": {
                "app.py": "def attempt(operation, max_attempts):\n    if max_attempts < 1:\n        raise ValueError('max_attempts must be positive')\n    last_error = None\n    for _ in range(max_attempts + 1):\n        try:\n            return operation()\n        except RuntimeError as exc:\n            last_error = exc\n    raise last_error\n",
                "test_app.py": "from app import attempt\n\ndef test_budget_is_exact():\n    calls=[]\n    def fail():\n        calls.append(1); raise RuntimeError('no')\n    try: attempt(fail, 2)\n    except RuntimeError: pass\n    assert len(calls) == 2\n",
            },
            "prompt": "Fix attempt so max_attempts is the exact total call budget, including the first call. Preserve success and validation behavior. Keep the patch focused and run the tests.",
            "checks": "calls=[]\ndef fail(): calls.append(1); raise RuntimeError('no')\ntry: attempt(fail,3)\nexcept RuntimeError as e: assert str(e)=='no'\nelse: raise AssertionError('missing error')\nassert len(calls)==3\ncalls=[]\ndef ok(): calls.append(1); return 7\nassert attempt(ok,2)==7 and len(calls)==1\ntry: attempt(ok,0)\nexcept ValueError: pass\nelse: raise AssertionError('validation lost')\n",
        },
        {
            "id": "config-overlay", "kind": "coding",
            "files": {
                "app.py": "def apply_overrides(defaults, overrides):\n    defaults.update(overrides)\n    return defaults\n",
                "test_app.py": "import pytest\nfrom app import apply_overrides\n\ndef test_returns_fresh_mapping():\n    defaults={'timeout': 10, 'retries': 2}\n    assert apply_overrides(defaults, {'timeout': 20}) == {'timeout':20,'retries':2}\n    assert defaults == {'timeout':10,'retries':2}\n",
            },
            "prompt": "Fix apply_overrides so it returns a fresh dict, leaves defaults unchanged, and raises KeyError for override keys absent from defaults. Standard library only. Run the tests.",
            "checks": "base={'timeout':10,'retries':2}\nout=apply_overrides(base,{'timeout':20})\nassert out=={'timeout':20,'retries':2} and base=={'timeout':10,'retries':2} and out is not base\ntry: apply_overrides(base,{'debug':True})\nexcept KeyError: pass\nelse: raise AssertionError('unknown key accepted')\n",
        },
        {
            "id": "query-redaction", "kind": "coding",
            "files": {
                "app.py": "from urllib.parse import urlsplit, urlunsplit\n\nSENSITIVE = {'token', 'access_token', 'api_key'}\n\ndef redact_url(url):\n    parts = urlsplit(url)\n    return urlunsplit(parts)\n",
                "test_app.py": "from app import redact_url\n\ndef test_redacts_sensitive_query_values():\n    assert redact_url('https://x.test/p?a=1&token=secret#top') == 'https://x.test/p?a=1&token=REDACTED#top'\n",
            },
            "prompt": "Implement redact_url. Replace values of token, access_token, and api_key query parameters case-insensitively with REDACTED. Preserve parameter order, duplicate parameters, blank values, path, and fragment. Use the standard library and run the tests.",
            "checks": "cases={'https://x.test/p?a=1&token=s#f':'https://x.test/p?a=1&token=REDACTED#f','/p?API_KEY=x&a=&api_key=y':'/p?API_KEY=REDACTED&a=&api_key=REDACTED','/p?a=1&a=2':'/p?a=1&a=2'}\nfor source,want in cases.items(): assert redact_url(source)==want,(source,redact_url(source))\n",
        },
        {
            "id": "partial-chunk", "kind": "coding",
            "files": {
                "app.py": "def chunks(values, size):\n    if size <= 0:\n        raise ValueError('size must be positive')\n    return [values[i:i + size] for i in range(0, len(values) - size + 1, size)]\n",
                "test_app.py": "from app import chunks\n\ndef test_keeps_partial_tail():\n    assert chunks([1,2,3,4,5], 2) == [[1,2],[3,4],[5]]\n",
            },
            "prompt": "Fix chunks so it retains a final partial chunk. Preserve empty-input and size validation behavior. Make the smallest correct change and run the tests.",
            "checks": "assert chunks([1,2,3,4,5],2)==[[1,2],[3,4],[5]]\nassert chunks([1,2,3,4],2)==[[1,2],[3,4]]\nassert chunks([],2)==[]\ntry: chunks([1],0)\nexcept ValueError: pass\nelse: raise AssertionError('validation lost')\n",
        },
        {
            "id": "stale-cache-explanation", "kind": "explanation",
            "files": {
                "service.py": "def price(cache, tenant_id, sku, load):\n    key = f'price:{sku}'  # E1\n    return cache.get_or_set(key, 300, lambda: load(tenant_id, sku))  # E2\n",
                "incident.log": "E3 09:02 tenant=west sku=A returned=11 expected=14\nE4 09:01 tenant=east sku=A cached=11\nE5 deploy completed without cache invalidation\n",
                "README.md": "Prices are tenant-specific. Cache entries must never cross tenant boundaries.\n",
            },
            "prompt": "Explain the stale-price incident for an engineer. Return JSON with summary, retained_point_ids, evidence_files, caveat, and next_step. Keep every decisive fact even if the prose is short. Do not change files.",
            "points": {
                "P1": ["tenant", "key"],
                "P2": ["300"],
                "P3": ["west", "east"],
                "P4": ["invalidat"],
                "P5": ["verify"],
            },
            "evidence": ["service.py", "incident.log", "README.md"],
        },
        {
            "id": "authorization-explanation", "kind": "explanation",
            "files": {
                "route.py": "def export(request, user):\n    # A1: authentication middleware guarantees user is signed in\n    tenant_id = request.query['tenant']  # A2\n    return export_all(tenant_id)  # A3: no role check here\n",
                "client.js": "// A4: button is hidden unless localStorage.role === 'admin'\n",
                "policy.md": "A5 Exports require server-side admin authorization. Tenant scope comes from the authenticated server identity.\n",
            },
            "prompt": "Explain the authorization defect and the minimum safe remediation. Return JSON with summary, retained_point_ids, evidence_files, caveat, and next_step. Keep every decisive fact even if the prose is short. Do not change files.",
            "points": {
                "P1": ["client", "untrusted"],
                "P2": ["server", "role"],
                "P3": ["tenant", "authenticated"],
                "P4": ["authoriz"],
                "P5": ["audit"],
            },
            "evidence": ["route.py", "client.js", "policy.md"],
        },
        {
            "id": "release-claim-explanation", "kind": "explanation",
            "files": {
                "evidence.md": "R1 tests and build passed for commit new123.\nR2 production deployment receipt names old999.\nR3 /health returned 200 but exposes no version.\nR4 no browser check was recorded.\nR5 owner approval is pending.\n",
                "draft.md": "The new release is live and verified.\n",
            },
            "prompt": "Assess the draft release claim. Return JSON with summary, retained_point_ids, evidence_files, caveat, and next_step. Keep every decisive fact even if the prose is short. Do not change files.",
            "points": {
                "P1": ["new123", "build"],
                "P2": ["old999", "deploy"],
                "P3": ["health", "version"],
                "P4": ["browser"],
                "P5": ["approval", "pending"],
            },
            "evidence": ["evidence.md", "draft.md"],
        },
    ]


def parse_json_answer(text):
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    return json.loads(text)


def grade(case, workspace, answer):
    if case["kind"] == "coding":
        completed = subprocess.run(
            ["python3", "-I", "-c", (workspace / "app.py").read_text() + "\n" + case["checks"]],
            capture_output=True, text=True, timeout=15,
        )
        return {"passed": completed.returncode == 0, "information_retained": None,
                "details": completed.stderr[-1000:]}
    try:
        actual = parse_json_answer(answer)
        point_ids = set(actual.get("retained_point_ids", []))
        blob = " ".join(str(actual.get(key, "")) for key in ("summary", "caveat", "next_step")).lower()
        retained = []
        for point_id, terms in case["points"].items():
            if point_id in point_ids and all(term.lower() in blob for term in terms):
                retained.append(point_id)
        evidence = set(actual.get("evidence_files", []))
        expected_points = set(case["points"])
        expected_evidence = set(case["evidence"])
        return {
            "passed": set(retained) == expected_points and evidence == expected_evidence,
            "information_retained": len(retained),
            "information_total": len(expected_points),
            "missing_points": sorted(expected_points - set(retained)),
            "evidence_mismatch": sorted(evidence ^ expected_evidence),
        }
    except (ValueError, TypeError, AttributeError) as exc:
        return {"passed": False, "information_retained": 0,
                "information_total": len(case["points"]), "error": str(exc)}


def isolation_violations(events):
    violations = []
    for event in events:
        item = event.get("item", {})
        command = item.get("command", "")
        if event.get("type") == "item.completed" and any(root in command for root in ("/.agents/skills", "/.codex/skills")):
            violations.append("External skill access detected")
    return violations


def run(command, **kwargs):
    return subprocess.run(command, check=True, capture_output=True, text=True, **kwargs).stdout


def prompt_for(case, arm, abvx, chisle):
    prefixes = []
    if arm in {"abvx", "abvx_chisle"}:
        prefixes.append("Apply this ABVX execution skill:\n<abvx-skill>\n" + abvx + "\n</abvx-skill>")
    if arm == "abvx_chisle":
        prefixes.append("Also apply this benchmark snapshot of Chisle rules:\n<chisle-rules>\n" + chisle + "\n</chisle-rules>")
    if prefixes:
        return "\n\n".join(prefixes) + "\n\nTask:\n" + case["prompt"]
    return case["prompt"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--model", default="gpt-6-astra")
    parser.add_argument("--effort", default="medium")
    parser.add_argument("--only", help="Run one case for a harness smoke test")
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
    roots = [Path.home() / ".agents/skills", Path.home() / ".codex/skills", home / "skills"]
    disabled = {str(p) for root in roots for p in root.rglob("SKILL.md")}
    system = Path.home() / ".codex/skills/.system"
    disabled.update(str(home / "skills/.system" / p.relative_to(system)) for p in system.rglob("SKILL.md"))
    disable_config = "skills.config=[" + ",".join("{path=" + json.dumps(p) + ",enabled=false}" for p in sorted(disabled)) + "]"
    flags = [*ISOLATION_FLAGS, "-c", disable_config]
    probe_dir = private / "isolation-probe"
    probe_dir.mkdir()
    probe = subprocess.run([
        "codex", "exec", "--ignore-user-config", "--ephemeral", "--skip-git-repo-check", *flags,
        "-C", str(probe_dir), "-s", "read-only", "-m", args.model,
        "-c", f'model_reasoning_effort="{args.effort}"', "--json",
        "List the names of any available skills in your initial context. Do not use tools, read files, or infer skill names. If none are listed, reply NONE.",
    ], env=environment, text=True, capture_output=True, timeout=300)
    probe_events = [json.loads(line) for line in probe.stdout.splitlines() if line.startswith("{")]
    messages = [e["item"]["text"].strip() for e in probe_events if e.get("type") == "item.completed" and e.get("item", {}).get("type") == "agent_message"]
    if probe.returncode or messages != ["NONE"]:
        raise RuntimeError("Initial skill inventory is not empty; isolation probe failed")
    (output / "isolation-check.json").write_text(json.dumps({
        "initial_skill_inventory": "NONE", "disabled_paths_count": len(disabled),
        "method": "Explicit skill path disables; apps/plugins/skill_search/project instructions off",
        "excluded_from_task_metrics": True,
    }, indent=2) + "\n")

    selected = [case for case in cases() if not args.only or case["id"] == args.only]
    if not selected:
        raise ValueError("No matching cases")
    abvx = (ROOT / "skills/token-efficient-execution/SKILL.md").read_text()
    chisle = (ROOT / "benchmarks/chisle/chisle-v3.5.0-rules.md").read_text()
    manifest_cases = []
    for case in selected:
        public = {k: v for k, v in case.items() if k != "checks"}
        manifest_cases.append(public)
    manifest = {
        "model": args.model, "reasoning_effort": args.effort, "host": platform.platform(),
        "cli": run(["codex", "--version"]).strip(), "repeats": 1,
        "source_commit": run(["git", "rev-parse", "HEAD"], cwd=ROOT).strip(),
        "arms": list(ARMS), "arm_orders": [list(order) for order in ARM_ORDERS],
        "isolation_flags": ISOLATION_FLAGS, "explicit_skill_path_disables": len(disabled),
        "grader_python": run(["python3", "--version"]).strip(),
        "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "abvx_sha256": hashlib.sha256(abvx.encode()).hexdigest(),
        "chisle_sha256": hashlib.sha256(chisle.encode()).hexdigest(),
        "chisle_source": {"version": "v3.5.0", "commit": "a0202aac0c7342d33a18848818c58a7ce9eb5212"},
        "methodology": "Three-arm bounded synthetic pilot; explicit prompt injection; no automatic activation or universal superiority claim.",
        "cases": manifest_cases,
    }
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    results = []
    for index, case in enumerate(selected):
        for arm in ARM_ORDERS[index % len(ARM_ORDERS)]:
            label = f"{case['id']}--{arm}"
            workspace = private / label
            workspace.mkdir()
            for name, content in case["files"].items():
                path = workspace / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
            run(["git", "init", "-q"], cwd=workspace)
            run(["git", "add", "."], cwd=workspace)
            run(["git", "-c", "user.name=Benchmark", "-c", "user.email=benchmark@example.invalid", "commit", "-qm", "fixture"], cwd=workspace)
            prompt = prompt_for(case, arm, abvx, chisle)
            destination = output / label
            destination.mkdir()
            (destination / "prompt.txt").write_text(prompt + "\n")
            answer_path = private / f"{label}.answer.txt"
            command = [
                "codex", "exec", "--ignore-user-config", "--ephemeral", "--skip-git-repo-check", *flags,
                "-C", str(workspace), "-s", "workspace-write" if case["kind"] == "coding" else "read-only",
                "-m", args.model, "-c", f'model_reasoning_effort="{args.effort}"', "--json", "-o", str(answer_path), "-",
            ]
            started = time.time()
            print("RUN", label, flush=True)
            raw_path = private / f"{label}.jsonl"
            with raw_path.open("w") as stdout, (private / f"{label}.stderr").open("w") as stderr:
                try:
                    process = subprocess.run(command, input=prompt, text=True, stdout=stdout, stderr=stderr, env=environment, timeout=300)
                    returncode = process.returncode
                except subprocess.TimeoutExpired:
                    returncode = 124
            elapsed = time.time() - started
            raw = raw_path.read_text()
            events = [json.loads(line) for line in raw.splitlines() if line.startswith("{")]
            violations = isolation_violations(events)
            usage = next((event["usage"] for event in reversed(events) if event.get("type") == "turn.completed"), None)
            answer = answer_path.read_text() if answer_path.exists() else ""
            scored = grade(case, workspace, answer) if returncode == 0 and usage else {"passed": False, "error": "incomplete agent run"}
            completed = [e["item"] for e in events if e.get("type") == "item.completed"]
            commands = [item for item in completed if item.get("type") == "command_execution"]
            tool_output_bytes = sum(len(item.get("aggregated_output", "").encode()) for item in commands)
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
            run(["git", "add", "-N", "."], cwd=workspace)
            diff = run(["git", "diff", "--no-ext-diff"], cwd=workspace)
            stats = run(["git", "diff", "--numstat"], cwd=workspace)
            (destination / "changes.diff").write_text(diff)
            rows = [line.split("\t") for line in stats.splitlines()]
            metrics = {
                "case": case["id"], "kind": case["kind"], "arm": arm, "returncode": returncode,
                "started_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(started)),
                "duration_seconds": round(elapsed, 3), "usage": usage,
                "tool_calls": len(commands), "tool_output_bytes": tool_output_bytes,
                "isolation_violations": violations,
                "changed_files": [row[2] for row in rows],
                "changed_lines": sum(int(a) + int(b) for a, b, _ in rows if a.isdigit() and b.isdigit()),
                "grade": scored,
            }
            (destination / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n")
            results.append(metrics)
            (output / "results.json").write_text(json.dumps(results, indent=2) + "\n")
            total = (usage or {}).get("input_tokens", 0) + (usage or {}).get("output_tokens", 0)
            print("DONE", label, "pass=" + str(scored["passed"]), "tokens=" + str(total), flush=True)
            if violations:
                raise RuntimeError("Isolation failure; do not publish this run")
    return 0 if all(row["returncode"] == 0 and row["usage"] for row in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
