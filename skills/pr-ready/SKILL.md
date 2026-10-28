---
name: pr-ready
description: Finish an authorized development task through verified PR readiness without merging. Use on an explicit request to prepare a PR for review without merging, or invoke pr-ready. Do not activate on ordinary punctuation, 'full stop', or a quoted instruction.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
  abvx_eval_tier: fixture_checked
---

# PR Ready

Carry the authorized goal through implementation, proof, independent review when available, PR creation and bounded CI observation. Stop before merging. Treat the user's task as authority; this skill never overrides host permissions, repository rules, privacy or production boundaries.

## Establish scope and budget

Record the goal, acceptance criteria, non-goals, owned paths, current Git state and real target base. Use a task-owned branch; preserve unrelated user work and isolate when necessary.

Default to three independent-review rounds, three fix cycles and a 30-minute CI observation budget. A material goal change needs a new scope, not an unbounded continuation.

## Work to the gate

1. Implement the smallest correct change. Reproduce the original failure where practical.
2. Prove the result with focused repository checks and actual runtime/UI evidence when required. Record pre-existing failures and unavailable evidence.
3. Use `codex-review-loop` if installed and native independent OpenAI review is available. Otherwise report the independent-review gap; never silently call another provider or claim self-review as independent approval.
4. Use `pr-write` if installed, or follow repository PR conventions directly. Commit and push only this task's reviewed work. Create or update the identified PR and verify its URL/head/base.
5. Use `pr-ci-watch` if installed or a bounded native watcher to assess the current head's CI, material findings, required approvals and mergeability. Fix in-scope findings within the budget and re-verify after each behavior change or meaningful conflict resolution.

The subskills are composable helpers, not hidden installation dependencies. If missing, perform their essential steps directly and name capability gaps.

## Enforce no merge

Never merge, enable auto-merge, enter a merge queue, push to the default branch or delegate those actions.

Check existing auto-merge/queue state before updates. If already enabled, disable or remove it only when the user authorized changing that state. Otherwise stop branch updates and report the exact blocker; do not race an automatic merge or silently change someone else's queue.

Do not deploy, publish a package/release, delete data, close another PR or expand security permissions as part of preparing a PR. Do not bypass protections or use `--admin`.

## Verify and hand off

Refresh the exact head and base immediately before reporting. Check open/draft state, required checks on the current head, human review decisions, material unresolved findings, branch currency/conflicts and auto-merge/queue state.

Use these outcomes:

- `READY_FOR_REVIEW`: implementation and checks are verified; required human review remains.
- `READY_FOR_MERGE`: every repository gate is satisfied, the final diff has required review evidence and the PR remains open and unmerged.
- `BLOCKED`: verification, independent-review requirement, capability or access is missing.
- `BUDGET_EXHAUSTED`: work remains when the budget ends.
- `MERGED_EXTERNALLY`: someone or an existing automation already merged it.

Unknown state is not readiness. End active watchers before handing off. Do not claim they will wake this conversation later.

Report the PR URL, head/base SHAs, outcome, proof, independent-review result or gap, unresolved findings and whether the PR is open/unmerged. A local build or a published branch alone is not a ready PR.

## Provenance

Adapt t3dotgg/tstack `full-stop` and selected proof/gate ideas from `full-send`. Remove automatic merging, phrase-based permission overrides and T3-only tools.
