---
name: session-retrospective
description: Review recent agent sessions through derived artifacts such as docs/ai/agent-sessions.json, docs/ai/agent-signals.json, and docs/ai/session-patterns.md. Use when a repo already exports session reflection artifacts and you need a compact retrospective on drift, redirects, prompt shape, long-session behavior, or what should change before the next run.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: original
---

# Session Retrospective

Use derived session artifacts, not raw transcript replay, unless the artifacts are missing or clearly stale.

## Inputs

Prefer these in order:

1. `docs/ai/agent-signals.json`
2. `docs/ai/session-patterns.md`
3. `docs/ai/agent-sessions.json`

If they are absent, say so and ask for `agentsgen reflect sessions .` rather than reconstructing the same analysis manually.

## What To Look For

Review:

- plan-first ratio;
- redirect count and redirect-heavy sessions;
- long-session frequency;
- repeated short prompts;
- prompt volume versus useful work;
- which repos or tasks seem to trigger drift.

## Retrospective Workflow

1. Confirm the artifact dates and scan scope.
2. Identify the 2-4 strongest signals, not every metric.
3. Separate:
   - stable strengths;
   - recurring waste;
   - one-off noise.
4. Convert findings into concrete changes:
   - add or tighten a skill;
   - shorten startup context;
   - add a verification gate;
   - change prompt or handoff shape;
   - split durable context.
5. Name the next experiment or intervention explicitly.

## Output Shape

Report:

- what the session layer says happened;
- the highest-value pattern or failure mode;
- what should change before the next session;
- which skill or doc should own that change.

## Guardrails

- Do not summarize whole transcripts when reflection artifacts already exist.
- Do not treat one noisy session as a durable pattern.
- Do not recommend broad process changes without pointing to a concrete signal in the artifacts.
