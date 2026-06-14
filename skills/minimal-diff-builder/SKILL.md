---
name: minimal-diff-builder
description: Build the smallest correct implementation that solves the requested task without speculative abstractions or avoidable dependencies. Use when the user wants the simplest solution, minimal code, small reviewable diffs, stdlib-first implementation, or a shortest-path fix that still preserves security, accessibility, trust-boundary validation, and data-safety behavior.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Minimal Diff Builder

Default to the smallest correct change, not the most expandable design.

## Use When

- the user asks for the simplest implementation, shortest path, or least code;
- the task is local and well scoped;
- dependency avoidance matters;
- the repo already risks overbuilding or abstraction creep.

## Ladder

Stop at the first rung that fully solves the task:

1. Does this need to exist at all, or can the requirement be narrowed?
2. Does the standard library already solve it?
3. Does the native platform already solve it?
4. Does an existing repo dependency already solve it?
5. Can the solution stay as a tiny local change?
6. Only then write new custom code, still at the smallest useful scope.

## Core Rules

- Prefer deletion, inlining, and reuse over new layers.
- Do not add a dependency for a small utility problem unless the user explicitly wants it.
- Do not introduce interfaces, factories, configs, or extension points without a real second use.
- Prefer one-file or one-surface changes when they remain readable.
- Preserve existing repo patterns when they are already simple enough.
- If two options are similarly small, pick the more edge-case-correct one.

## Hard Exceptions

Do not simplify away:

- trust-boundary validation;
- error handling that prevents data loss;
- security-sensitive checks or secret handling;
- accessibility basics on user-facing surfaces;
- anything the user explicitly asked to retain.

## Workflow

1. Restate the narrow task in one sentence.
2. Check the ladder from top to bottom before writing code.
3. Choose the smallest implementation that fully meets the task.
4. Keep the diff local:
   - avoid broad renames or structural churn;
   - avoid adding files unless they clearly improve correctness or verification;
   - avoid speculative "future-proofing".
5. If you intentionally leave out a heavier design, say what was skipped and the threshold that would justify adding it later.
6. For non-trivial logic, leave behind one small runnable check:
   - one focused test, or
   - one assert-based demo/self-check if that fits the repo better.
7. Run the narrowest meaningful verification first, then broader relevant checks.

## Anti-Patterns

- building a reusable framework for a one-off task;
- adding configuration for a value that does not vary;
- wrapping stdlib or platform behavior in a thin custom abstraction;
- adding a new helper file when a local function would do;
- inflating the explanation after keeping the code small.

## Final Report

Include:

- what path on the ladder was used;
- what heavier options were intentionally skipped;
- verification run;
- residual threshold for when a bigger design would become justified.
