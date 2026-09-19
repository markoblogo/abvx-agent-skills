#!/usr/bin/env python3
"""Regrade and summarize the retained three-arm Chisle benchmark."""
from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "benchmarks/measured/2026-09-19-chisle"
RUNNER = ROOT / "scripts/run_chisle_benchmark.py"
ARMS = ("baseline", "abvx", "abvx_chisle")


def load_runner():
    spec = importlib.util.spec_from_file_location("run_chisle_benchmark", RUNNER)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


def percent(current, reference):
    return (current / reference - 1) * 100 if reference else 0.0


def main():
    # Older raw traces may include the local account name in `ls -l` output.
    # Re-sanitize retained synthetic traces without changing measured content.
    username = os.environ.get("USER")
    if username:
        for path in EVIDENCE.glob("*--*/events.jsonl"):
            text = path.read_text()
            if username in text:
                path.write_text(text.replace(username, "<user>"))
    runner = load_runner()
    cases = {case["id"]: case for case in runner.cases()}
    results = json.loads((EVIDENCE / "results.json").read_text())
    expected = {(case_id, arm) for case_id in cases for arm in ARMS}
    observed = {(row["case"], row["arm"]) for row in results}
    if len(results) != 24 or observed != expected:
        raise ValueError("Expected all 24 benchmark runs; refusing a partial summary")

    corrected = []
    for row in results:
        item = dict(row)
        if row["returncode"] != 0 or not row["usage"] or row.get("isolation_violations"):
            raise ValueError(f"Incomplete or contaminated run: {row['case']}--{row['arm']}")
        folder = EVIDENCE / f"{row['case']}--{row['arm']}"
        if row["kind"] == "explanation":
            repaired = runner.grade(cases[row["case"]], Path("."), (folder / "answer.txt").read_text())
            item["original_grade"] = row["grade"]
            item["grade"] = repaired
            item["grading_correction"] = "Runner v1 used nonexistent P1-P5 IDs instead of fixture E/A/R evidence IDs; answers are unchanged and regraded deterministically."
        item["total_tokens"] = row["usage"]["input_tokens"] + row["usage"]["output_tokens"]
        corrected.append(item)
    (EVIDENCE / "summary.json").write_text(json.dumps(corrected, indent=2) + "\n")

    aggregates = {}
    for arm in ARMS:
        rows = [row for row in corrected if row["arm"] == arm]
        coding = [row for row in rows if row["kind"] == "coding"]
        explanation = [row for row in rows if row["kind"] == "explanation"]
        aggregates[arm] = {
            "checks_passed": sum(row["grade"]["passed"] for row in rows),
            "checks_total": len(rows),
            "total_tokens": sum(row["total_tokens"] for row in rows),
            "coding_tokens": sum(row["total_tokens"] for row in coding),
            "explanation_tokens": sum(row["total_tokens"] for row in explanation),
            "coding_changed_lines": sum(row["changed_lines"] for row in coding),
            "tool_output_bytes": sum(row["tool_output_bytes"] for row in rows),
            "information_retained": sum(row["grade"].get("information_retained") or 0 for row in explanation),
            "information_total": sum(row["grade"].get("information_total") or 0 for row in explanation),
        }
    (EVIDENCE / "aggregates.json").write_text(json.dumps(aggregates, indent=2) + "\n")

    table = []
    for arm in ARMS:
        data = aggregates[arm]
        table.append(
            f"| {arm} | {data['checks_passed']}/{data['checks_total']} | "
            f"{data['information_retained']}/{data['information_total']} | {data['total_tokens']:,} | "
            f"{data['coding_changed_lines']} | {data['tool_output_bytes']:,} |"
        )
    abvx = aggregates["abvx"]
    combined = aggregates["abvx_chisle"]
    token_delta = percent(combined["total_tokens"], abvx["total_tokens"])
    coding_delta = percent(combined["coding_tokens"], abvx["coding_tokens"])
    explanation_delta = percent(combined["explanation_tokens"], abvx["explanation_tokens"])
    diff_delta = combined["coding_changed_lines"] - abvx["coding_changed_lines"]
    tool_delta = percent(combined["tool_output_bytes"], abvx["tool_output_bytes"])
    quality_held = (
        combined["checks_passed"] >= abvx["checks_passed"]
        and combined["information_retained"] >= abvx["information_retained"]
    )
    diff_percent = percent(combined["coding_changed_lines"], abvx["coding_changed_lines"])
    improved = quality_held and (token_delta < 0 or diff_percent < 0 or tool_delta < 0)
    decision = (
        "Chisle improved diff and tool-output economy without reducing acceptance scores, but increased total tokens. Two unique stopping/scope rules are promoted; the complete Chisle ruleset is not adopted."
        if improved else
        "Chisle did not improve the current ABVX stack in this pilot. No Chisle rule is promoted into token-efficient-execution."
    )
    manifest = json.loads((EVIDENCE / "manifest.json").read_text())
    readme = f"""# ABVX + Chisle benchmark — 2026-09-19

Eight synthetic tasks, three arms, one run per arm: **24 fresh Codex sessions**.
Five tasks edit code and run checks; three explain evidence packets. Model:
`{manifest['model']}` at `{manifest['reasoning_effort']}` effort; CLI: `{manifest['cli']}`.

| Arm | Checks | Explanation points retained | Input + output tokens | Coding diff lines | Tool output bytes |
|---|---:|---:|---:|---:|---:|
{chr(10).join(table)}

## Decision

{decision}

Compared with ABVX alone, ABVX + Chisle used **{token_delta:+.1f}%** total tokens
({coding_delta:+.1f}% coding; {explanation_delta:+.1f}% explanation), changed
**{diff_delta:+d}** coding lines ({diff_percent:+.1f}%), and produced
**{tool_delta:+.1f}%** tool-output bytes.
Correctness and information retention must not decline for a candidate to qualify.

## Arms

- `baseline`: task only, with local skills, plugins, apps, skill search, and project instructions disabled.
- `abvx`: task plus the checked-in `token-efficient-execution` skill.
- `abvx_chisle`: ABVX arm plus the vendored Chisle v3.5.0 rules snapshot at commit
  `a0202aac0c7342d33a18848818c58a7ce9eb5212`.

Chisle is not installed globally and is not added to repository instructions.
For Codex, this evaluates Chisle's static rules only; its tool-result compression
hooks target other supported agents and are outside this comparison.

## Measures

- Correctness: hidden Python assertions for five coding tasks.
- Information loss: five predeclared evidence points and an exact source set for
  each explanation task, 15 points total per arm.
- Tokens: CLI `input_tokens + output_tokens`; cached input remains a subset.
- Diff size: added plus removed lines in coding fixtures.
- Tool output: bytes in completed command outputs from the retained event stream.

The runner rotates arm order to reduce simple ordering bias. Every session uses
a fresh Git fixture and an ephemeral Codex home. The initial inventory probe must
return `NONE`; external local-skill reads invalidate the run.

## Grading correction

The first runner version mistakenly named explanation expectations `P1`–`P5`,
while the fixtures and all unchanged answers use their actual evidence IDs:
`E1`–`E5`, `A1`–`A5`, and `R1`–`R5`. The original failed grades remain in
`summary.json` as `original_grade`; `grade` is the deterministic corrected score.
No answer, token count, trace, or diff was regenerated or discarded.

## Evidence and limits

`manifest.json` retains fixtures, prompts, hashes, host, model, and arm order.
`results.json` is the runner's original output. `summary.json` adds corrected
grades and token totals; `aggregates.json` contains the table inputs. Each run
directory retains prompt, answer, sanitized event trace, diff, and raw metrics.

This is one model, one run per arm, and eight author-designed synthetic tasks.
There are no repeats, confidence intervals, cost conversion, or cross-model
claims. Prompt length contributes to token totals, so an added ruleset must earn
back its own context cost to count as an improvement.

## Reproduce

```bash
python scripts/run_chisle_benchmark.py \\
  --work-dir /tmp/abvx-chisle-work-NEW \\
  --output /tmp/abvx-chisle-results-NEW \\
  --model {manifest['model']} --effort {manifest['reasoning_effort']}
```

Regenerate this report from retained evidence:

```bash
python scripts/summarize_chisle_benchmark.py
```
"""
    (EVIDENCE / "README.md").write_text(readme)

    demo = f"""# Measured comparison: ABVX and Chisle

{decision}

The bounded three-arm pilot ran five coding tasks and three explanation tasks.
All raw evidence and limitations are in the
[retained benchmark](../../benchmarks/measured/2026-09-19-chisle/README.md).

| Arm | Checks | Information retained | Total tokens |
|---|---:|---:|---:|
""" + "\n".join(
        f"| {arm} | {aggregates[arm]['checks_passed']}/{aggregates[arm]['checks_total']} | "
        f"{aggregates[arm]['information_retained']}/{aggregates[arm]['information_total']} | "
        f"{aggregates[arm]['total_tokens']:,} |" for arm in ARMS
    ) + f"""

Adding Chisle to ABVX changed total recorded tokens by **{token_delta:+.1f}%**,
with **{diff_delta:+d}** coding diff lines ({diff_percent:+.1f}%) and
**{tool_delta:+.1f}%** tool-output bytes. The bounded port adds only the
first-sufficient-solution stopping rule and an adjacent-scope guard. Chisle
remains a benchmark competitor rather than a global dependency or default
instruction layer.
"""
    (ROOT / "docs/demos/chisle-comparison.md").write_text(demo)
    print(json.dumps({"decision": decision, "abvx_chisle_token_delta_percent": round(token_delta, 2), "aggregates": aggregates}, indent=2))


if __name__ == "__main__":
    main()
