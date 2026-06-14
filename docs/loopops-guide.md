# LoopOps Guide

LoopOps is the ABVX discipline for deciding when agent behavior should remain a prompt and when it should be promoted into a more durable artifact.

The core rule is simple: do not turn every repeated task into a skill. Promote only when reuse, reliability, or cost control justifies the overhead.

## Promotion Ladder

1. Prompt
   - one-off task
   - low cost of repetition
   - no recurring failure mode
2. Checklist
   - same task repeats
   - sequence matters
   - human or agent keeps forgetting a step
3. Skill
   - workflow is reusable and procedural
   - trigger language is stable
   - the instructions improve outcomes across tasks
4. Script
   - a deterministic step keeps getting rewritten
   - reliability matters more than prose flexibility
5. Loop / workflow
   - the task spans multiple cycles
   - a bounded evaluator, memory policy, and stop rule are needed

## Decision Heuristics

- Stay at the lowest artifact that reliably solves the problem.
- Prefer a prompt when the variation surface is high and the task is still cheap.
- Prefer a skill when the reusable value is procedural rather than code-level deterministic.
- Prefer a script when the same code keeps being generated.
- Prefer a loop only when bounded repetition beats manual supervision.

## Anti-Patterns

- turning one successful prompt into a published skill immediately;
- using a skill to hide the absence of verification;
- adding a loop without budget, stop rules, or escalation;
- building a script when a two-line shell command already works;
- turning local repo context into a "universal" skill without proving portability.

## Example: Prompt -> Skill

Situation:
- repeated repo tasks require the same "read narrowly, patch small, verify honestly" execution style
- the advice is procedural, not deterministic code

Promotion:
- prompt guidance becomes `token-efficient-execution`

Why not script:
- the value is in agent behavior shaping, not a deterministic transformation

## Example: Skill -> Script

Situation:
- a skill keeps re-explaining the same JSON export, data extraction, or harness bootstrap code

Promotion:
- keep the workflow in `SKILL.md`
- move the deterministic step into `scripts/`

Why:
- lower token cost
- fewer implementation drifts

## Example: Skill -> Loop

Situation:
- repeated task flow now needs:
  - a fixed budget,
  - memory policy,
  - evaluator,
  - escalation rule,
  - bounded retries

Promotion:
- use `loopops-protocol` and `dynamic-workflow-packets` to decide whether the work should become a supervised loop or packetized workflow

## Recommended Pairings

- `loopops-protocol` + `skillopt-evolve-skills`
- `loopops-protocol` + `dynamic-workflow-packets`
- `token-efficient-execution` before promoting a workflow that may only be noisy rather than truly reusable
- `delivery-preflight-gate` before longer autonomous loops

## Practical Rule

If you cannot explain:
- what recurring failure or cost this promotion fixes,
- why the lower artifact is insufficient,
- how the promoted artifact will be validated,

then do not promote it yet.
