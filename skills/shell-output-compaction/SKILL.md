---
name: shell-output-compaction
description: Reduce shell and tool-output token waste by preferring targeted commands, diff-only views, error-first logs, narrow slices, counts, and concise summaries instead of large raw stdout dumps. Use on coding, debugging, audits, CI triage, or repo exploration when command output is likely to dominate token usage.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Shell Output Compaction

Save tokens by shrinking command output before it reaches the model.

## Core Principle

The cheapest output is the output you never ask the shell to print. Shape commands so they emit the smallest artifact that still answers the question.

## Command Shaping Rules

- Ask what exact signal is needed before running a command: status, count, match, diff, failing test, or tail of logs.
- Prefer `rg`, exact paths, exact symbols, and line-numbered slices over broad directory dumps.
- Prefer match-only, filename-only, or count-style results over full content when triaging.
- Read files through targeted ranges or symbol searches before opening them fully.
- Prefer `git diff --stat`, file-scoped diffs, or changed-hunk views before whole diffs.
- Prefer error-only, warning-only, or final-summary build output before full logs.
- Prefer `head`, `tail`, and bounded excerpts over raw multi-screen output.
- When the same command is rerun, capture only the new failure, new diff, or new tail.

## Common Patterns

### Repo Discovery

- Use `rg --files` or targeted `find` patterns, not recursive `ls`.
- Search for exact identifiers, routes, env keys, or error strings first.
- Return only the few paths worth opening next.

### File Inspection

- Read the smallest useful slice first.
- Expand only if the local context is insufficient.
- Keep line numbers with excerpts so later references stay precise.

### Git

- Start with branch status, changed-file list, and diff stats.
- Open per-file hunks only for relevant files.
- Avoid pasting long commit history unless chronology matters.

### Logs, Tests, And CI

- Run failing tests first, not the entire suite, when the failure scope is known.
- Prefer quiet or summary flags when they preserve the needed signal.
- For large logs, inspect the error block and a short leading context window.

## Reporting Rules

- Summarize long command output instead of replaying it verbatim.
- Preserve exact commands, errors, or paths only when they affect the next action.
- If raw output must be kept for handoff, save the location or the key excerpt, not the full dump.

## Guardrails

- Do not truncate away the only stack trace, SQL error, or failing assertion that explains the issue.
- Do not compress safety-critical output into ambiguity.
- If the narrow view is inconclusive, broaden one step at a time.

## Final Report

Include the outcome, the key evidence, and any exact raw lines that remain important. Leave the rest compact.
