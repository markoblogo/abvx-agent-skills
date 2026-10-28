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

For `MODERNIZE`, rebase onto the freshly fetched actual base. Resolve conflicts according to the goal and current invariants. Stop if resolving them would silently change scope.

Compare the original and rebased series with `git range-diff`; inspect the final diff. Check that behavior was neither lost nor reintroduced from an already-landed implementation. Run relevant tests and real runtime verification when the claim needs it.

A request to update the PR authorizes updating its task-owned branch when ownership is verified; a review-only request does not. When rewriting a published branch, use an explicit lease tied to the previously observed SHA:

```bash
git push --force-with-lease=refs/heads/<branch>:<observed-sha> <verified-remote> HEAD:refs/heads/<branch>
```

On lease rejection, fetch and reassess. Never force-push the default branch, bypass protection, change the base, merge, close, or add public comments as a side effect.

## Report

Give the disposition, PR link, why the goal remains useful or obsolete, meaningful base changes, before/after SHAs, verification, push result and unresolved decisions. State what remains unverified. Recheck CI on the new head if observation is authorized.

## Provenance

Adapt t3dotgg/tstack `modernize` with explicit branch ownership, verified leases and Codex-native tools.
