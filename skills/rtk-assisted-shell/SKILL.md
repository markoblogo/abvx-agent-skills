---
name: rtk-assisted-shell
description: Reduce shell output token waste on git, file reads, searches, test runs, linters, logs, and other noisy developer commands with RTK-style filtering. Use when shell-heavy work is flooding the session with logs, diffs, or command output that should be compacted before it reaches the model.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# RTK Assisted Shell

Save tokens by routing noisy shell workflows through RTK-style filtering first.

## Goal

Before running a command that could dump large output, prefer an RTK-shaped command or an equivalent compact shell pattern so the model receives a smaller artifact.

## Default Rewrites

Prefer these forms first when RTK is installed:

- `git status` -> `rtk git status`
- `git diff` -> `rtk git diff`
- `git log` -> `rtk git log`
- `cat file`, `head file`, `tail file` -> `rtk read file`
- `rg pattern`, `grep pattern` -> `rtk grep pattern .`
- `ls`, large `find` flows -> `rtk ls` or compact `find`
- `pytest`, `npm test`, `cargo test`, `go test`, `tsc`, linters -> `rtk <command>`
- `docker logs`, `kubectl logs` -> `rtk docker logs ...`, `rtk kubectl logs ...`

If RTK is not installed or does not support the command, fall back to compact native shell patterns:

- file-scoped diffs, not whole history;
- bounded excerpts, not full files;
- failing tests first, not full suites;
- error-first or summary-first log views.

## Workflow

1. Decide whether the command is likely to be noisy.
2. If yes, prefer RTK rewrite first.
3. If RTK output is still insufficient, broaden one step:
   - summary -> excerpt -> raw command.
4. If RTK is unavailable, preserve the same compactness policy manually.
5. Keep exact raw output only when it materially changes diagnosis or handoff.

## When To Use Aggressively

- repo exploration;
- git state and diff inspection;
- test and lint failures;
- CI logs;
- container and cluster logs;
- broad searches over large repos.

## Guardrails

- Do not use RTK if output format must remain exact for downstream parsing.
- Do not hide the only decisive stack trace or assertion.
- If RTK filtering obscures the needed detail, fall back to a narrower raw command before using a broad raw command.

## Final Report

State whether RTK or manual compact output shaping was used, what decisive signal was kept, and what large output was intentionally avoided.
