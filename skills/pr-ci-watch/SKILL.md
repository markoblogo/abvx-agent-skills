---
name: pr-ci-watch
description: Monitor a specific GitHub pull request through CI and review within a bounded active session. Use when explicitly asked to watch CI, babysit a PR, or invoke pr-ci-watch. Monitoring alone does not authorize code fixes, public replies, or merging.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
  abvx_eval_tier: fixture_checked
---

# PR CI Watch

Watch one identified PR within the active task. Preserve the user's action scope. Do not merge, enable auto-merge, enter a merge queue, deploy, or claim that monitoring continues after the session ends.

## Preflight

Resolve owner/repository, PR number, URL, base/head SHAs, draft/open state and existing auto-merge or queue state. Read current CI, human reviews, unresolved threads and relevant bot findings first. Use the connected GitHub tools when sufficient; otherwise use authenticated `gh`. Never copy credentials between tools.

Default to a 30-minute observation budget and at most three fix-and-recheck cycles. Share one deadline across restarts; a new head does not reset it. Use one watcher per PR. Do not start a delegated watcher from a review child.

If auto-merge or a queue can merge the PR externally, disclose that state. Monitoring does not authorize changing it. Never promise the PR will stay unmerged unless that condition is verified.

## Observe

With local authenticated `gh`, run the bundled helper:

```bash
python3 <absolute-skill-dir>/scripts/watch_ci.py <number> --repo <owner/repository> --timeout 1800
```

It uses GitHub CLI's own required-check watcher, pins the head and enforces a deadline. Its result concerns CI only. `CI_PASSED` is not `READY`; `NO_REQUIRED_CHECKS` is not approval. Never count API errors, missing permissions, a timeout or an unavailable check set as success.

If using connectors, read a complete PR/check/review snapshot, then use an exposed bounded watch operation if available. Without one, return a one-time snapshot and `WATCH_UNAVAILABLE`; do not invent background wakeups, create a scheduler, or implement a tight polling loop.

Respect rate limits and server retry hints. Do not retry authentication or permission failures blindly. Retain event evidence without printing credentials or private logs.

## Handle events

Verify every material finding against the current source, including still-open findings from older commits. Determine whether a reported failure is caused by this change, baseline breakage or infrastructure. Never discard a finding based solely on its timestamp.

Fix only when the task already authorizes fixes. Reproduce the issue where practical, make a minimal change, verify it, and update the same task-owned branch only if pushing is authorized. Otherwise report the actionable finding.

Public replies and thread resolution require user authorization. Prefer editing the PR description over unsolicited comments. Resolve a thread only after verifying a justified reply or fix.

After a new push, restart observation for the new head within the original deadline. Reassess after meaningful base changes. Stop after three fix cycles or the deadline, preserving the open issues.

## Finish

Refresh head, base, required checks, unresolved threads, human reviews and mergeability. Report `READY` only when checks on the current head pass, required review approvals are present, no material finding is open, and the branch is current and conflict-free. Treat unknown mergeability, absent required checks without policy evidence, or inaccessible reviews as `INCONCLUSIVE`.

Report `WAITING`, `CHANGES_NEEDED`, `BLOCKED`, `MERGED_EXTERNALLY`, or `CLOSED` as appropriate. Include the PR URL, checked SHAs, observation duration, remaining gate and whether the watcher has stopped.

## Provenance

Adapt t3dotgg/tstack `babysit-pr`. Replace its long-running host-specific watcher with a bounded GitHub CLI helper and explicit connector fallback. The helper is original ABVX code.
