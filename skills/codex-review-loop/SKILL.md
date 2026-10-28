---
name: codex-review-loop
description: Review a code change with one independent OpenAI reviewer and at most three rounds. Use when the user explicitly requests bounded independent review or invokes codex-review-loop. Do not trigger on a casual mention of review or start a loop for trivial edits.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
  abvx_eval_tier: fixture_checked
---

# Codex Review Loop

Keep the change small and require evidence for correctness. Use OpenAI models only. Treat this skill as a workflow, never as permission to push, publish, merge, change model providers, or bypass the host's rules.

## Establish the review target

1. Read repository instructions. Capture the goal, non-goals, owned paths, clean/dirty state, base SHA and current head. Preserve unrelated and uncommitted user work; use an isolated worktree when needed.
2. Resolve the actual target branch from PR metadata or repository configuration. Fetch it when available and use its merge base. With no remote, use an explicitly known local base; review uncommitted changes against HEAD only when that is the requested scope. Report missing base evidence.
3. Include tracked and relevant untracked changes. Freeze a reproducible diff and run the focused checks that cover the intended behavior. Record pre-existing failures separately.

## Resolve the reviewer

Discover the current host's native subagent capability and the OpenAI model IDs it actually exposes. Use one separate read-only OpenAI reviewer, respecting user-selected models and host routing rules. Do not invent model IDs or require T3 Code tools. Do not call Claude or another provider. Never give the reviewer write or publication ownership.

If independent review cannot run, return `BLOCKED_INDEPENDENT_REVIEW`. A clearly labelled self-review can still help, but never report it as independent approval.

## Run a bounded loop

Set a total budget of three rounds, one reviewer at a time, no nested reviewers. Ask for a fresh read of the full scoped change in round one; later rounds cover changed behavior and open findings. Do not edit scoped files while review runs.

Give the reviewer the goal, base/head, diff command, paths, relevant untracked files and check results, without suggesting the expected verdict. Require:

- `APPROVE` or `CHANGES`;
- stable finding IDs, file/line, evidence, severity and a minimal proposed fix;
- `blocker` for broken intended behavior, `should` for a real in-scope bug, `nit` for optional polish.

Verify each finding yourself. Apply the smallest justified fix; reject false positives and out-of-scope work with evidence. Keep a finding ledger. Re-run relevant checks after behavior changes. Do not dismiss a consequential security or data-loss bug merely because it was labelled a nit.

Stop early when only optional nits remain. Do not add rounds for prose-only fixes. Count timeouts and failed attempts against the budget; neither counts as approval. Cancel and verify the old reviewer stopped before retrying.

## Finish

Report `APPROVED` only when independent approval covers the final behavior diff, no material findings remain, and your own checks support it. Otherwise report `CHANGES_NEEDED`, `BUDGET_EXHAUSTED`, or the capability blocker. Include base/head, rounds, verified reviewer identity if exposed, fixed/declined findings, checks and missing evidence. Never fabricate token usage.

Do not commit or push merely to complete a review. Keep the result in the user's language.

## Provenance

Adapt the bounded review and finding-ledger ideas from t3dotgg/tstack `sol-loop`. Remove hardcoded model names, T3 dependencies and cross-provider routing. See SKILL_CARD.md for attribution and evidence limits.
