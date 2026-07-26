---
name: agent-tool-contract-review
description: Review tools, MCP functions, CLI commands, SET inputs, and AGENTS.md generator outputs as agent-facing contracts. Use when a tool description, schema, workflow input, or generated instruction may be ambiguous, unsafe, noisy, or hard for agents to call correctly.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Agent Tool Contract Review

Use this skill to make a tool easier and safer for agents to call.

## Use When

- designing or reviewing MCP tools, CLI wrappers, GitHub Actions inputs, or SET planner outputs;
- changing AGENTS.md generator templates that tell agents which commands or tools to use;
- a tool has ambiguous parameters, hidden side effects, noisy output, or weak error messages;
- agent runs repeatedly misuse a command or need human intervention after avoidable failures.
- adapting an external skill, contract, or workflow into the local skill network.

## Adaptation Delta

Before writing an adapted external skill, classify each material source fragment in `templates/adaptation-delta.yaml`:

- `KEEP`: retain source mechanics or schema without semantic change;
- `ADAPT`: change paths, tools, authority, terminology, or environment assumptions;
- `ADD`: introduce local guardrails, routing, verification, or project boundaries;
- `REJECT`: exclude a fragment and record the reason plus source reference.

Every entry requires a stable ID and source fragment reference. Present the complete delta to the owner before writing. Record `APPROVED`, `REVISE`, or `REJECTED`; silence is not approval. Preserve attribution and license constraints independently of the classification.

## Review Dimensions

- purpose: what job the tool owns and what it does not own;
- schema: required fields, optional fields, enums, defaults, and validation;
- authority: read-only, proposal-only, write, destructive, external side effect;
- output: compact, structured, parseable, and stable enough for downstream agents;
- errors: actionable messages with the smallest useful recovery step;
- idempotency: safe retries, duplicate handling, and idempotency keys when needed;
- auditability: logs, dry-run mode, preview mode, and human approval boundary.

## Workflow

1. Identify the agent-facing tool surface and its intended caller.
2. Classify the authority level: `read`, `plan`, `proposal`, `write`, or `destructive`.
3. Check whether the name, description, schema, and examples make the safe path obvious.
4. Check whether the output can be consumed without reading a large log.
5. Check error paths and retry semantics.
6. Recommend the smallest contract change: rename, tighter schema, dry-run, better error, structured output, or approval gate.

## Output Shape

Use:

- verdict: `CONTRACT_OK`, `CONTRACT_AMBIGUOUS`, or `CONTRACT_UNSAFE`;
- tool surface reviewed;
- authority level;
- contract findings;
- smallest contract changes;
- tests or smoke checks.

## Guardrails

- Do not redesign the whole tool when a schema or description change is enough.
- Do not hide write or destructive behavior behind friendly wording.
- Do not require agents to infer defaults that can be encoded in schema.
- Do not make logs the primary machine interface when structured output is feasible.
- Do not silently omit or rewrite upstream behavior during adaptation.

## Provenance

Adapted from tool-design patterns in `muratcankoylan/Agent-Skills-for-Context-Engineering`, plus MakerSkills' explicit keep/adapt/add porting report. Narrowed for SET, AGENTS.md generator, MCP, CLI, and provider-neutral skill adaptation, with an added `REJECT` disposition and owner gate.
