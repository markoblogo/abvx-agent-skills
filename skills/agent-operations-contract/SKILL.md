---
name: agent-operations-contract
description: Define and review concrete agent capability cards, asynchronous operation receipts, isolated memory scopes, and evidence-backed provider or tool registry entries. Use when a project introduces named agents, scheduled or long-running work, durable memory, provider routing, MCP tools, or external-action approval boundaries.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Agent Operations Contract

Use this skill to make configured agents and their operations inspectable without installing an agent runtime. It complements skill cards: a skill describes a reusable method; an agent card describes one actual worker, its current capabilities, and its authority.

This contract is opt-in and fail-closed. Documentation, configuration, marketplace presence, or a successful probe never grants authority.

## 1. Agent Capability Card

Create one card per concrete agent from `templates/agent-capability-card.yaml`.

Require:

- stable `agent_id`, purpose, bounded responsibilities, owner;
- authority: `read`, `proposal`, `write`, or `external_action`;
- configured models, tools, and knowledge bases;
- allowed schedules, including whether unattended runs are permitted;
- explicit approval boundary;
- dated capability confirmations with evidence.

Rules:

- List secret names, never values.
- `external_action` names exact action families; it is not blanket permission.
- An allowed schedule controls timing, not authority.
- Missing owner, approval boundary, or current confirmation blocks use.
- Capability changes update the card before a run depends on them.

## 2. Async Operation Receipt

Use `templates/operation-receipt.json` for scheduled, queued, or long-running work.

Allowed states:

```text
QUEUED -> RUNNING -> NEEDS_APPROVAL -> SUCCEEDED | FAILED | CANCELLED
```

`RUNNING` may settle directly when approval is unnecessary. Each retry creates a new `operation_id` or records a stable parent/idempotency relationship; never overwrite a failed receipt as success.

`NEEDS_APPROVAL` must retain an action fingerprint and the exact proposed action. Approval is one-shot, expires, and cannot widen the agent card. A receipt contains compact operational facts and evidence references, not hidden reasoning, credentials, private content, full prompts, transcripts, or unrestricted logs.

## 3. Scoped Memory

Use `templates/memory-record.yaml`. Every memory record has exactly one scope:

- `personal`: reviewed owner preferences;
- `project`: repository or product context;
- `agent`: reviewed domain knowledge for one agent;
- `run`: temporary operation state.

Every record declares provenance, owner, editability, and retention. Cross-project reads, background learning, and automatic scope promotion are off by default. `run` memory expires unless a human-reviewed proposal promotes it. Memory is context, not completion evidence.

## 4. Provider And Tool Registry

Use `templates/provider-tool-capability.yaml` for each model provider, local runtime, API, CLI, or MCP surface.

Record:

- modalities, tool calling, structured output, streaming, and async support;
- `local` or `cloud` execution;
- required secret names and data-egress boundary;
- availability: `declared`, `probed`, `confirmed`, or `unavailable`;
- dated cost and rate-limit observations with sources;
- authority and exact side effects.

Availability meanings:

- `declared`: documentation or configuration only;
- `probed`: endpoint, binary, or authentication path was reachable;
- `confirmed`: the relevant task path succeeded with evidence;
- `unavailable`: missing, disabled, incompatible, or insufficient for the task.

Route only through entries whose confirmed capabilities and authority satisfy the task. Treat cost, limits, models, and availability as expiring observations.

## Project Gate

Before enabling a named agent or schedule, report:

| Check | Evidence |
| --- | --- |
| agent card owner and authority | card path and revision |
| provider/tool route | registry entry and current status |
| memory scope | allowed scopes and retention |
| operation persistence | receipt location and redaction rule |
| approval boundary | action families and approver |
| cancellation/idempotency | recovery behavior |
| verification | real runtime path exercised |

If any row is missing, return `CONTRACT_AMBIGUOUS` and keep the route disabled or report-only.

## Output

- **Verdict:** `CONTRACT_OK`, `CONTRACT_AMBIGUOUS`, or `CONTRACT_UNSAFE`.
- **Authority:** effective authority of the reviewed agent and operation.
- **Cards/receipts/registry:** paths or missing artifacts.
- **Findings:** ambiguity, stale evidence, over-broad authority, unsafe memory crossing, or hidden side effects.
- **Smallest changes:** bounded edits required before enablement.
- **Verification:** checks run and unavailable runtime evidence.

## Non-Goals

- Do not install LobeHub, an agent marketplace, MCP servers, schedulers, databases, or memory services.
- Do not create self-assembling teams or infer authority from agent assignment.
- Do not authorize messages, transactions, production writes, device writes, or protected-data access.
- Do not turn a successful operation into durable memory automatically.

## Attribution

Adapted at the contract level from LobeHub's agent-as-unit, scheduling/status, white-box memory, and multi-provider ideas. Rewritten as a provider-neutral ABVX review contract without the LobeHub runtime or codebase.
