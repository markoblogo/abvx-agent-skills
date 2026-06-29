---
name: agent-learning-layer-triage
description: Route reusable agent learning after an error, success pattern, review finding, or repeated workflow. Use when deciding whether an improvement belongs in the model prompt, memory/context note, durable docs, SKILL.md, checklist, script/tool, eval, golden fixture, or should be rejected as overfit.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: original
---

# Agent Learning Layer Triage

Use this skill when a task produces a lesson and the next question is: where should this learning live?

ABVX does not assume the model itself learns. Most useful operational learning belongs in an auditable layer around the model: context, skills, scripts, gates, and evals.

## Learning Layers

Classify the candidate into the cheapest durable layer that solves the repeated problem:

1. **Leave as prompt/session behavior**: one-off correction, low recurrence, no durable value.
2. **Memory or context note**: stable preference, repo fact, operator convention, or short reminder that should be easy to read and revise.
3. **Durable repo doc**: stable repo architecture, setup, verification, deployment, or workflow fact that future agents must discover reliably.
4. **Checklist**: repeated human or agent sequence where order matters but no portable behavior layer is needed yet.
5. **SKILL.md**: reusable behavior with a clear trigger, action rules, anti-patterns, and verification discipline.
6. **Script or tool**: deterministic repeated step where code is more reliable than prose.
7. **Eval or golden fixture**: behavior must be regression-tested, especially after a bug, review failure, or model drift.
8. **Reject / park**: plausible but overfit, too broad, not validated, duplicative, or unsafe.

Prefer the lowest layer that makes the next run materially better.

## Triage Questions

Ask in order:

1. Did this happen more than once, or is recurrence likely?
2. Is the lesson stable across repos, or only local to one repo/session?
3. Is the value factual recall, procedural behavior, deterministic execution, or regression detection?
4. Can the lesson be verified by a command, fixture, review rubric, or before/after trace?
5. Would adding this to always-loaded context increase startup cost more than it reduces future mistakes?
6. Does it duplicate a stronger existing skill, script, doc, or higher-priority instruction?
7. Could it weaken a safety, trust, authorization, privacy, or destructive-action boundary?

If uncertainty remains, park as a note with evidence instead of promoting it.

## Routing Rules

- Use **memory/context note** for preferences, compact conventions, and stable facts that do not need a workflow.
- Use **durable docs** for repo-local facts that should survive sessions and be discoverable from the repo.
- Use **checklists** when sequence is the main value and the steps remain partly human-supervised.
- Use **SKILL.md** when the behavior should load on demand across tasks and needs trigger discipline.
- Use **script/tool** when prose keeps producing inconsistent execution for a deterministic operation.
- Use **eval/golden fixture** when the lesson came from a failure that should not regress.
- Use **rejected buffer** when the idea is attractive but not yet proven.

## Output Shape

Return a compact decision record:

```text
Learning candidate: <one sentence>
Evidence: <trace, PR, review, failure, success pattern>
Chosen layer: prompt | memory | durable-doc | checklist | skill | script | eval | reject
Why this layer: <short rationale>
Artifact to update: <path or destination>
Verification: <how we know the learning helps>
Rejected higher layers: <why not skill/script/eval/etc.>
Next action: <one concrete edit or no-op>
```

## Promotion Guardrails

- Do not turn every useful sentence into a skill.
- Do not put repo-local facts into global skills unless the behavior generalizes.
- Do not create scripts for workflows that still require judgment at every step.
- Do not create evals without a stable fixture or observable pass/fail condition.
- Do not store secrets, private user data, credential hints, or sensitive client context in publishable artifacts.
- Do not weaken existing authorization, safety, or verification gates to make learning feel smoother.

## Pair With

- `skillopt-evolve-skills` when the chosen layer is `SKILL.md` or agent instructions.
- `durable-context-maintenance` when the chosen layer is repo-local durable docs.
- `goal-loop-designer` when the lesson should become a bounded loop contract, judge rubric, or stop rule.
- `delivery-preflight-gate` when repeated failure suggests a missing preflight, push gate, or regression fixture.

## Final Report

State the chosen layer, the artifact changed or intentionally not changed, and the verification or evidence threshold for promotion.