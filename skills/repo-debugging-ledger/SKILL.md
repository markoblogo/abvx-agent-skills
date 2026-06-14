---
name: repo-debugging-ledger
description: Debug repositories with a hypothesis ledger, checked locations, and loop-breaking discipline. Use when tests fail, CI fails, behavior regresses, local tooling errors, flaky bugs appear, or an investigation risks repeated searches, repeated commands, circular hypotheses, or unverified fixes.
license: MIT
---

# Repo Debugging Ledger

Use this skill as a lightweight overlay on normal debugging. Its job is to prevent loops and untested assumptions.

## Start With A Repro Signal

Create the smallest useful pass/fail loop:

- unit/integration test,
- CLI command,
- HTTP request,
- browser script,
- fixture replay,
- log assertion,
- repeated flake trigger.

If no loop exists, state the best available signal and what artifact would make it deterministic.

## Hypothesis Ledger

Before editing, write or mentally maintain 3-5 ranked hypotheses:

```text
H1:
Prediction:
Probe:
Result:
Status: open / supported / falsified
```

Probe one variable at a time. Prefer evidence that distinguishes between hypotheses.

## Checked-Location Ledger

Track what has already been inspected:

```text
Checked:
- file/function/command:
  evidence:
  conclusion:
```

Do not reopen the same file, rerun the same broad search, or repeat the same command unless a phase change makes it newly relevant: new failing signal, new stack trace, changed code, or a narrowed hypothesis.

## Search And Instrumentation

- Use `rg` and targeted file reads first.
- Search for exact symbols, error text, config keys, route names, and call sites before broad terms.
- Tag temporary logs with a unique marker such as `[DEBUG-7b3c]`.
- Remove temporary instrumentation before finalizing.
- If a likely area is exhausted, broaden to a different subsystem instead of cycling through the same files.

## Fix Discipline

- Add or identify a regression check before the fix when a reasonable seam exists.
- Keep the fix scoped to the supported hypothesis.
- Re-run the original repro signal after the fix.
- Run the project’s normal checks before finalizing, or explain the blocker.

## Final Report

Include:

- root cause or best-supported cause,
- files changed,
- verification run,
- residual risks or missing test seam.
