---
name: assumption-excavation
description: Surface hidden assumptions in plans, specs, AGENTS.md, SKILL.md, SET bundles, and workflow contracts before implementation or handoff. Use when an artifact looks plausible but may rely on unstated environment, dependency, behavioral, temporal, or success assumptions.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Assumption Excavation

Find what the artifact takes for granted before those assumptions become implementation bugs.

## Use When

- reviewing PRDs, specs, plans, or issue slices before work starts;
- reviewing `AGENTS.md`, `SKILL.md`, SET bundles, proof-loop contracts, or workflow docs;
- a proposal sounds confident but depends on unclear prerequisites;
- you need a lightweight pre-implementation review lens.

## Workflow

1. Identify the artifact and its intended consumer.
2. Read for implicit assumptions, not prose quality.
3. Classify assumptions:
   - environment: tools, services, files, auth, OS, network;
   - dependency: upstream state, input shape, prior checks;
   - behavioral: what humans, agents, or systems are expected to do;
   - temporal: what must remain stable over time;
   - success: what the artifact counts as done or safe.
4. Rank the assumptions by fragility:
   - high: likely to break or expensive if wrong;
   - medium: plausible risk with manageable fallout;
   - low: visible but not blocking.
5. Mark partially surfaced assumptions as `PARTIAL`.
6. Recommend what must be clarified, tested, or accepted before implementation.

## Output Shape

Use:

- verdict: `EXAMINED` or `UNEXAMINED`;
- top assumptions, ranked;
- fragility score or severity per item;
- missing evidence;
- smallest clarification or verification step.

## Guardrails

- Do not rewrite the artifact unless asked.
- Do not treat assumptions as errors by default; some are deliberate.
- Do not block on low-risk assumptions.
- State uncertainty as text-based inference, not mind reading.

## Provenance

Adapted from the `assumption-excavator` pattern in `aself101/agents-and-pipelines`, compressed for ABVX skill use and broader repo-contract review.
