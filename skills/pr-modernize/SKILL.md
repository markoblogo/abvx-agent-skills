---
name: pr-modernize
description: Reassess and update an outdated GitHub PR against its actual current base. Use when explicitly asked to rebase or modernize an old PR, or invoke pr-modernize. Determine whether its goal still matters before rebasing; do not merge or close it.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
  abvx_eval_tier: fixture_checked
---

# PR Modernize

Reassess the problem before updating the branch. Treat a conflict-free rebase as Git evidence, not proof that the change still belongs in the product.

## Inspect

Resolve the PR URL, author, head repository/branch/SHA, actual base, review state and checks. Read the goal, full diff, linked issues and material reviews. Inspect repository instructions and preserve all unrelated working-tree changes.

Fetch the exact head and base. Use a clean isolated worktree when the active checkout is dirty or shared. Record the remote head SHA before any rewrite. Do not assume the base is main or that the PR branch belongs to the user.

Read relevant base changes since divergence and look for a replacement implementation or overlapping PR. Distinguish a mechanical conflict from a changed architecture or obsolete goal.

## Decide before rewriting

Return one of:

- `MODERNIZE`: the goal is useful and the implementation still fits.
- `REWORK`: the goal is useful but needs a different implementation.
- `OBSOLETE`: the problem is already solved or no longer worth this change.
- `BLOCKED`: source, permission or evidence is unavailable.

For `REWORK`, continue only if the existing task authorizes that work. For `OBSOLETE`, explain the evidence and leave the PR open unless the user explicitly authorized closure.

## Update safely

Before updating an existing PR branch, inspect auto-merge and merge-queue state. If either can merge it automatically, stop updates unless changing that state is authorized. Never disable it silently or promise no merge while it remains enabled.

For `MODERNIZE`, preserve the published branch history. Refresh a task-owned existing PR branch by merging its freshly fetched actual base. If repository policy requires linear history or the user explicitly asks for a rebase, prepare the rebased work on a separate local continuation branch; publish that new branch or a replacement PR only when authorized. Leave the original published branch unchanged. Resolve conflicts according to the goal and current invariants, and stop if that would silently change scope.

For a separate rebased continuation, compare the original and rebased series with `git range-diff`. For a merge-based refresh, inspect the merge resolution and final diff against the current base. Check that behavior was neither lost nor reintroduced from an already-landed implementation. Run relevant tests and real runtime verification when the claim needs it.

A request to update the PR authorizes updating its task-owned branch when ownership is verified; a review-only request does not. Before a normal push, fetch the published head again and verify that no other contributor's changes would be lost. If the remote moved or the push is rejected, fetch and reassess; never force the update.

Do not force-push any published branch, push the default branch, bypass protection, change the PR base, merge or close the PR, or add public comments as a side effect. If preserving history cannot satisfy repository policy, report the need for an authorized replacement branch instead of rewriting the source.

## Report

Give the disposition, PR link, why the goal remains useful or obsolete, meaningful base changes, before/after SHAs, verification, push result and unresolved decisions. State what remains unverified. Recheck CI on the new head if observation is authorized.

## Provenance

Adapt t3dotgg/tstack `modernize` with explicit branch ownership, preserved published history and Codex-native tools.
