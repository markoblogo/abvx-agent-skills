---
name: reversible-agent-task
description: Run risky or multi-file agent work as a reviewable proposal before mutating the target workspace. Use when a task should produce retained output, inspectable diffs, and an explicit select/apply/discard decision instead of direct edits.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Reversible Agent Task

Use a proposal-first workflow when direct mutation would make review, rollback, or comparison harder.

## Use When

- an agent runner, SET bundle, or planning doc mentions retained output, proposal lifecycle, settlement, or reversible traces;
- the task can be attempted in a worktree, draft branch, sandbox, retained-output folder, or external runner proposal;
- multiple possible implementations should be compared before one is applied;
- the target repo should remain unchanged until a human or supervisor reviews the output.

## Lifecycle

1. `run`: execute the task in a proposal context, such as a worktree, draft branch, sandbox, or retained-output directory.
2. `retained_output`: keep generated files, diffs, logs, and proof artifacts separate from the target workspace.
3. `inspect`: review diff scope, verification evidence, assumptions, and expected artifacts.
4. `select`: mark one retained output as the candidate result.
5. `apply`: merge or copy the selected proposal into the target workspace only after gates pass.
6. `discard`: reject the proposal and leave the target workspace unchanged.

## Procedure

1. Define the target workspace and the proposal workspace.
2. State the mutation rule: no direct writes to the target workspace until `apply`.
3. Capture expected artifacts and verification commands before the run.
4. Run the agent or implementation loop in the proposal context.
5. Inspect the retained output:
   - changed files;
   - generated artifacts;
   - tests or checks run;
   - unresolved assumptions;
   - scope drift.
6. Choose exactly one settlement action: `select`, `apply`, or `discard`.

## Output Shape

Include:

- target workspace;
- proposal workspace or retained-output location;
- lifecycle state reached;
- artifacts produced;
- verification evidence;
- settlement action: `select`, `apply`, or `discard`;
- blockers or assumptions.

## Guardrails

- Do not present retained output as applied work.
- Do not hide failed proposals; summarize why they were discarded.
- Do not mutate the target workspace during `run` or `inspect`.
- Do not use this skill for trivial one-file edits where normal git diff review is enough.
- Keep the proposal mechanism host-agnostic: worktree, branch, sandbox, retained directory, or external runner are all acceptable.

## Pair With

- `pipeline-readiness-gate` for pre/post/ship gate selection.
- `assumption-excavation` before running high-ambiguity proposals.
- `confidence-fragility-review` before applying a proposal with public or release claims.
- `delivery-baseline-audit` before calling applied work complete.

## Provenance

Adapted from proposal lifecycle patterns in reversible agent runtimes such as `shepherd-agents/shepherd`, narrowed into a host-agnostic ABVX review discipline. This skill does not require Shepherd.
