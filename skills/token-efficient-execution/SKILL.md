---
name: token-efficient-execution
description: Reduce token waste in long coding-agent sessions by avoiding repeated reads, noisy output, oversized context, broad rewrites, and unnecessary narration. Use on long tasks, heavy repos, multi-file audits, shell-heavy debugging loops, or whenever token budget is a practical delivery constraint.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Token Efficient Execution

Save tokens by tightening the work loop, not only the answer style.

## Core Principle

The biggest waste usually comes from repeated exploration, repeated explanation, and oversized context reloads. Fix the loop first.

## Execution Rules

- Read targeted files, not whole trees.
- Search exact symbols, error text, route names, or config keys before broad terms.
- Do not reread the same file unless it changed or a new hypothesis makes it relevant.
- Prefer narrow patches over file rewrites.
- Avoid long “plan recap” messages after every small step.
- Keep intermediary updates to one or two sentences unless the user asked for a plan.
- Reuse gathered evidence instead of re-deriving it.
- Stop low-value parallel exploration once a clear winning path appears.

## Task Patterns

### Debugging

- Build one reproducible signal.
- Maintain a checked-location ledger.
- Rank hypotheses before opening more files.

### Implementation

- Read surrounding code once, then patch.
- Keep edits scoped to the behavior under change.
- Run the narrowest verification first, then broaden only as needed.

### Research

- Keep an evidence ledger with claims, sources, and open questions.
- Quote or cite only when needed.
- Do not re-open sources already summarized unless precision requires it.

## Anti-Patterns

- broad `grep` loops over the same code;
- rereading README, config, and the same module repeatedly;
- restating the task after every command;
- proposing before reading enough code;
- validating everything when only one seam changed;
- carrying stale notes forward after the code changed.

## Final Report

Include what changed, what was verified, and any remaining uncertainty. Do not spend tokens listing every trivial command unless it matters for continuation.
