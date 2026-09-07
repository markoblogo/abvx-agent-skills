#!/usr/bin/env python3
"""Regenerate the measured demo pages from retained CLI evidence."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "benchmarks/measured/2026-09-07"
ARMS = ("without_skill", "with_skill")
PAGES = {
    "minimal-diff-builder": ("minimal-diff-builder", "Small bug fixes", "Correctness is checked by independent Python assertions. Production edits and retained tests are shown separately; more test lines are not automatically worse."),
    "token-efficient-execution": ("token-economy", "Targeted configuration lookup", "Each fixture contains one active configuration, its reader, and 60 obsolete migration notes. The answer must name the correct value and both source paths."),
    "public-release-verification": ("public-release-verification", "Release evidence review", "Three synthetic evidence packets cover a build without a deployment, a broken public route, and pending owner approval. Exact status fields and rejection of an unsupported live announcement are checked."),
}


def main():
    results = json.loads((EVIDENCE / "results.json").read_text())
    manifest = json.loads((EVIDENCE / "manifest.json").read_text())
    expected = {(c["id"], arm) for c in manifest["cases"] for arm in ARMS}
    if len(results) != 18 or {(r["case"], r["arm"]) for r in results} != expected:
        raise ValueError("Expected all 18 paired runs; refusing a partial summary")
    enriched = []
    for row in results:
        if row["returncode"] != 0 or not row["usage"] or row.get("isolation_violations"):
            raise ValueError("Incomplete run: " + row["case"])
        item = dict(row)
        folder = EVIDENCE / (row["case"] + "--" + row["arm"])
        events = [json.loads(line) for line in (folder / "events.jsonl").read_text().splitlines()]
        completed = [e["item"] for e in events if e.get("type") == "item.completed"]
        commands = [i for i in completed if i.get("type") == "command_execution"]
        item["tool_calls"] = len(commands)
        item["tool_output_bytes"] = sum(len(i.get("aggregated_output", "").encode()) for i in commands)
        item["total_tokens"] = row["usage"]["input_tokens"] + row["usage"]["output_tokens"]
        item["production_changed_lines"] = 0
        item["test_changed_lines"] = 0
        file = ""
        for line in (folder / "changes.diff").read_text().splitlines():
            if line.startswith("+++ b/"):
                file = line[6:]
            elif line.startswith(("+", "-")) and not line.startswith(("+++", "---")):
                if file == "app.py":
                    item["production_changed_lines"] += 1
                elif Path(file).name.startswith("test_") or file.startswith("tests/"):
                    item["test_changed_lines"] += 1
        enriched.append(item)
    (EVIDENCE / "summary.json").write_text(json.dumps(enriched, indent=2) + "\n")
    overview = []
    for skill, (slug, title, rubric) in PAGES.items():
        rows = [r for r in enriched if r["skill"] == skill]
        totals = {arm: sum(r["total_tokens"] for r in rows if r["arm"] == arm) for arm in ARMS}
        passes = {arm: sum(r["grade"]["passed"] for r in rows if r["arm"] == arm) for arm in ARMS}
        delta = (totals["with_skill"] / totals["without_skill"] - 1) * 100
        check_label = "Exact status rubric" if skill == "public-release-verification" else "Correct"
        table = [f"| Case | Arm | {check_label} | Input + output tokens | Cached input subset | Seconds | Tool output bytes |", "|---|---|---|---:|---:|---:|---:|"]
        for row in rows:
            table.append(f"| {row['case']} | {row['arm']} | {'yes' if row['grade']['passed'] else 'no'} | {row['total_tokens']:,} | {row['usage'].get('cached_input_tokens', 0):,} | {row['duration_seconds']:.1f} | {row['tool_output_bytes']:,} |")
        result = f"{check_label}: **{passes['without_skill']}/3 without**, **{passes['with_skill']}/3 with**. Total recorded tokens: **{totals['without_skill']:,} without**, **{totals['with_skill']:,} with** ({delta:+.1f}% with the skill)."
        extra = ""
        if skill == "minimal-diff-builder":
            extra = "\n\n| Case | Arm | Production lines added + removed | Test lines added + removed |\n|---|---|---:|---:|\n" + "\n".join(f"| {r['case']} | {r['arm']} | {r['production_changed_lines']} | {r['test_changed_lines']} |" for r in rows)
            extra += "\n\nSee each `changes.diff` and `changed_files` field for complete scope, including any generated cache files. Binary cache files are excluded from textual line counts."
        if skill == "public-release-verification":
            announcements = {arm: 0 for arm in ARMS}
            mismatch_rows = []
            for row in rows:
                answer = (EVIDENCE / (row["case"] + "--" + row["arm"]) / "answer.txt").read_text().strip()
                if answer.startswith("```"):
                    answer = answer.split("\n", 1)[1].rsplit("```", 1)[0].strip()
                parsed = json.loads(answer)
                announcements[row["arm"]] += parsed.get("can_announce_live") is True
                for field, mismatch in row["grade"].get("mismatches", {}).items():
                    mismatch_rows.append(f"| {row['case']} | {row['arm']} | {field} | {mismatch['expected']} | {mismatch['actual']} |")
            extra = f"\n\nUnsupported live announcements: **{announcements['without_skill']}/3 without**, **{announcements['with_skill']}/3 with**. This safety-relevant field is reported separately from exact status-label agreement."
            if mismatch_rows:
                extra += "\n\n| Case | Arm | Field | Predeclared expectation | Observed |\n|---|---|---|---|---|\n" + "\n".join(mismatch_rows)
                extra += "\n\nThe author-fixed rubric is intentionally retained. `PARTIAL` versus `UNKNOWN` can be a defensible interpretation of queued deployment evidence; conservative repository-proof labels can also disagree with it. A rubric mismatch is not automatically an unsafe answer. A future evaluation should distinguish semantic safety from status-label calibration before running new cases."
        page = f"""# Measured demo: {title}

{result}

## Task and check

{rubric}

## Captured results

{chr(10).join(table)}{extra}

## Interpretation

This small pilot describes these runs only. A tied check score does not
show that the skill improved correctness. Lower token usage is an observation,
not a guaranteed saving; higher token usage is retained rather than hidden.
The minimal-diff skill may trade additional retained tests for higher cost.
No outcome here establishes cross-model superiority or production safety.

## Reproduce and inspect

See the [method, fixtures, prompts, raw traces, and limitations](../../benchmarks/measured/2026-09-07/README.md).
All nine cases are generated by `scripts/run_measured_demos.py`; the committed
manifest retains their exact inputs and grader expectations.

Install this skill alone:

```bash
gh skill install markoblogo/abvx-agent-skills {skill} --agent codex --scope user
```
"""
        (ROOT / "docs/demos" / (slug + ".md")).write_text(page)
        overview.append(f"| [{skill}](../../../docs/demos/{slug}.md) | {passes['without_skill']}/3 | {passes['with_skill']}/3 | {totals['without_skill']:,} | {totals['with_skill']:,} | {delta:+.1f}% |")
    readme = f"""# Measured demos — 2026-09-07

Nine synthetic tasks, two arms each, one run per arm: **18 fresh agent sessions**.
Model: `{manifest['model']}`; reasoning effort: `{manifest['reasoning_effort']}`;
CLI: `{manifest['cli']}`; host: `{manifest['host']}`. Grader: `{manifest['grader_python']}`.

| Skill | Checks passed without | Checks passed with | Tokens without | Tokens with | Change with skill |
|---|---:|---:|---:|---:|---:|
{chr(10).join(overview)}

## Method

- Fresh Git fixture and ephemeral CLI session for every run; serial execution,
  alternating arm order by case. User config and project instruction loading
  are disabled; an isolated Codex home starts with only an authentication link.
  Installed host and bundled skills are disabled by explicit `skills.config`
  paths; skill search, apps, and plugins are off. An inventory probe must return
  NONE before task runs start. Flags and the path count are retained in the
  manifest. The runner rejects observed external local-skill reads.
- Same task, files, model, effort, and sandbox for each pair. Only the with-skill
  prompt includes the target SKILL.md. Companion skills are unavailable.
  This evaluates explicit skill use, not automatic trigger selection.
- Coding cases may edit their disposable fixture; lookup and release cases use
  the read-only sandbox. No real production resources are evaluation targets.
- Correctness is deterministically graded. Python assertions are outside the
  agent workspace. Lookup answers must match the active value and source paths.
  Release answers are scored against the predeclared exact status rubric; the
  demo separately reports unsupported live announcements and explains label
  disagreements. No LLM judge chooses winners.
- Token totals are CLI `input_tokens + output_tokens` across each run. Cached
  input is a subset, not added twice. These counters include agent/harness
  overhead and are not billed dollars or unique-context size. Reasoning counters
  are retained separately without adding them again.
- Duration is wall time including startup/shutdown, not model-only latency.
  Tool output bytes sum completed command output, not a tokenizer estimate.
  Diff line counts include additions and removals, with tests reported separately.

## Evidence

- [manifest.json](manifest.json): exact task files, prompts, expectations, host,
  source commit, and model configuration.
- [isolation-check.json](isolation-check.json): initial inventory probe result;
  this setup check is excluded from the 18 task-run metrics.
- [results.json](results.json): original grades, timings, usage, and skill hashes.
- [summary.json](summary.json): derived totals, tool output, and diff metrics.
- Each `<case>--<arm>/` directory contains the actual prompt, final answer,
  sanitized JSONL event trace, code diff, and per-run metrics. Local paths and
  ephemeral session IDs are replaced; authentication files are never published.
  Skill bodies under test are retained in with-skill prompts, identified by hash.

## Limitations

One model, one run per arm, nine deliberately small synthetic tasks. No repeats,
confidence intervals, held-out validation, or long-session token benchmark.
The author selected both fixtures and rubric. Cache state, CLI startup, and
service latency can affect results. These runs use local shell/file work;
they do not prove browser behavior, deployment health, or cross-host compatibility.
Perfect baseline scores can make a task too easy to establish added value.
All outcomes are retained, including ties, additional cost, and scope overhead.

An initial series was invalidated after traces revealed automatic loading of a
local `ast-index` skill despite `--ignore-user-config`. It was stopped and
excluded in full, not selectively filtered by score. Local third-party skill
contents from that series are not redistributed. The clean series below uses
explicit discovery/plugin isolation; no initial-series numbers enter this report.

Evidence tier: bounded `rollout_checked`, not `held_out_validated`.

## Reproduce

Requires Git, Python 3.10+, and an authenticated Codex CLI supporting the flags
below. Uses normal model quota; the live experiment is intentionally not run in CI.
Use new output/work directories for every run; never overwrite retained evidence.

```bash
python scripts/run_measured_demos.py \\
  --work-dir /tmp/abvx-demo-private-NEW \\
  --output /tmp/abvx-demo-results-NEW \\
  --model {manifest['model']} --effort {manifest['reasoning_effort']}
```

Regenerate the checked-in demo pages from this retained run:

```bash
python scripts/summarize_measured_demos.py
```

The runner uses only the selected skill source from the current checkout. To
repeat the exact older prompt snapshot after a skill changes, restore that body
from the retained with-skill prompt first. The deterministic grader's regression
tests run in CI; they do not replace these live agent runs.
"""
    (EVIDENCE / "README.md").write_text(readme)
    print("Generated three measured demo pages and evidence summary")


if __name__ == "__main__":
    main()
