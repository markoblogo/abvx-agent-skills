# Measured demos — 2026-09-07

Nine synthetic tasks, two arms each, one run per arm: **18 fresh agent sessions**.
Model: `gpt-6-astra`; reasoning effort: `medium`;
CLI: `codex-cli 0.153.4`; host: `macOS-26.6.2-arm64-arm-64bit-Mach-O`. Grader: `Python 3.14.5`.

| Skill | Checks passed without | Checks passed with | Tokens without | Tokens with | Change with skill |
|---|---:|---:|---:|---:|---:|
| [minimal-diff-builder](../../../docs/demos/minimal-diff-builder.md) | 3/3 | 3/3 | 193,428 | 190,239 | -1.6% |
| [token-efficient-execution](../../../docs/demos/token-economy.md) | 3/3 | 3/3 | 141,380 | 117,042 | -17.2% |
| [public-release-verification](../../../docs/demos/public-release-verification.md) | 1/3 | 2/3 | 84,696 | 77,979 | -7.9% |

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
python scripts/run_measured_demos.py \
  --work-dir /tmp/abvx-demo-private-NEW \
  --output /tmp/abvx-demo-results-NEW \
  --model gpt-6-astra --effort medium
```

Regenerate the checked-in demo pages from this retained run:

```bash
python scripts/summarize_measured_demos.py
```

The runner uses only the selected skill source from the current checkout. To
repeat the exact older prompt snapshot after a skill changes, restore that body
from the retained with-skill prompt first. The deterministic grader's regression
tests run in CI; they do not replace these live agent runs.
