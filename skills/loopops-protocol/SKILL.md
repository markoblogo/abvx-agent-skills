---
name: loopops-protocol
description: Design and evolve agent skills into cost-bounded loops, workflows, scripts, and memory updates. Use when creating or auditing reusable agent methods, converting prompts or skills into workflows, designing open or closed agent loops, defining supervisor/evaluator contracts, or deciding whether repeated agent work should become a skill, checklist, script, workflow, or autonomous loop.
license: MIT
---

# LoopOps Protocol

Use this skill when reusable agent behavior should become more than a better prompt.

The goal is to choose the smallest durable artifact that improves future runs:

```text
prompt -> skill -> checklist -> script -> workflow -> loop
```

Do not promote work upward unless the extra machinery buys reliability, reuse, or cheaper future execution.

## Artifact Ladder

Classify the candidate method first:

- **Prompt**: one-off instruction for this run.
- **Skill**: compact reusable context, procedure, or tool adapter loaded on demand.
- **Checklist**: ordered human/agent validation sequence.
- **Script**: deterministic repeatable action with parameters.
- **Workflow**: ordered tool/process execution with gates and evidence.
- **Loop**: workflow plus evaluator, memory write, retry policy, and stop rule.

Prefer the lowest artifact that handles the task reliably.

## Loop Suitability Gate

Promote a workflow into a loop only when all are true:

- The goal has an observable completion condition.
- Progress can be evaluated without trusting the worker agent blindly.
- A retry is likely to improve the result.
- Cost can be bounded by iteration, time, token, or tool budget.
- Failure has a clear stop, rollback, or human-escalation path.

If any condition is missing, keep it as a supervised workflow or checklist.

## Open vs Closed Loop

Use an **open loop** when:

- the solution space is unknown,
- discovery or exploration matters,
- multiple valid approaches may exist,
- the output is research, architecture, strategy, or design direction.

Use a **closed loop** when:

- acceptance criteria are known,
- tests, checks, or review criteria exist,
- regression risk matters,
- the task can be decomposed into verifiable steps.

Open loops need tighter budget limits. Closed loops need stronger evaluators.

## Supervisor Contract

Every loop must define:

```text
Goal:
Completion condition:
Loop type: open | closed
Worker action:
Evaluator:
Evidence:
Memory write:
Retry policy:
Budget:
Stop rule:
Rollback or escalation:
```

The evaluator can be a test command, lint/typecheck/build, browser check, static analysis, script, human review, or a separate model. Prefer deterministic evaluators when available.

## Memory Policy

After each iteration, save only durable signal:

- current hypothesis,
- changed files or artifacts,
- verification result,
- blocker or failure mode,
- next intended action,
- reusable lesson if it generalizes.

Do not append raw logs, long transcripts, secrets, private data, or one-off observations to durable memory.

## Skill Evolution

After a loop completes, update skills only with lessons that are:

- procedural,
- reusable,
- testable,
- not already covered by higher-priority instructions,
- worth their token cost.

Good updates:

- missing repo-specific command,
- repeated failure mode,
- verification step that caught a real issue,
- script or workflow that replaced repeated manual work,
- rejected path that should not be retried.

Bad updates:

- generic coding advice,
- motivational wording,
- model-behavior hacks,
- single-incident preferences,
- rules that increase context without reducing errors.

## Cost Controls

Every loop must have at least two:

- max iterations,
- max wall-clock time,
- max token/tool budget if measurable,
- narrowest useful verification first,
- summarized memory instead of raw logs,
- stop after repeated identical blocker,
- human approval before external, destructive, expensive, or privacy-sensitive actions.

If cost cannot be bounded, do not run autonomously.

## Compiler Rule

When the same step is repeated three times, decide whether to compile it:

- repeated prose instruction -> skill rule,
- repeated checklist -> workflow,
- repeated shell/Python/JS snippet -> script,
- repeated verification pattern -> evaluator,
- repeated failure recovery -> stop hook or escalation rule.

Prefer scripts and deterministic checks over longer instructions.

## Final Report

When designing or updating a loop-capable method, report:

- chosen artifact level,
- why higher levels were rejected or accepted,
- supervisor contract if a loop is used,
- cost controls,
- memory writes,
- validation performed,
- skill/workflow/script files changed.
