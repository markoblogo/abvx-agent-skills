---
name: agents-best-practices
description: Design, audit, or improve agentic systems and agent harnesses. Use for agent MVP blueprints, tool design, permission models, planning and goal loops, context compaction, memory, skills, connectors, observability, evals, safety, and provider-neutral agent architecture.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Agents Best Practices

An agent harness is the control plane around a model. The model proposes; the harness validates, authorizes, executes, records, and returns observations.

## Start With The Boundary

Identify:

- domain and user;
- autonomy level: answer-only, draft-only, approval-gated action, or autonomous within policy;
- risk level: read-only, internal write, external communication, financial, legal, healthcare, security, destructive, or privileged;
- state duration: single turn, session, resumable workflow, or long-running goal;
- tool surface;
- validation signal.

## Minimal Harness Shape

```text
task
  -> context builder
  -> model call
  -> proposed tool/action
  -> schema validation
  -> permission decision
  -> execution or approval pause
  -> structured observation
  -> state update
  -> finish or continue within budget
```

## Harness Checklist

Before recommending implementation, cover these surfaces:

- agentic loop: turn budget, stop rules, loop detection, checkpoint/resume;
- tool registry: static vs dynamic tools, schema quality, denial/error shape, MCP boundaries;
- context assembly: priority order, just-in-time loading, compaction, source attribution;
- memory: session state vs durable memory, write policy, contradiction handling;
- guardrails: trust boundaries, prompt-injection exposure, sandbox/network/filesystem policy;
- permissions: read/write/send/delete/pay/deploy classes, approval gates, classifier-assisted routing only with deterministic backstops;
- observability: event log, tool outcomes, user-visible state, no hidden-reasoning leakage;
- evals: success fixtures, safety fixtures, eval noise budget, floor/ceiling checks;
- managed-agent architecture: separate brain, hands, credentials, session state, and worker lifecycle when the agent becomes long-running.

## Design Rules

- Application code enforces safety; prompts only describe desired behavior.
- Every tool call returns a structured result, including denials and errors.
- Risky side effects require explicit policy and usually human approval.
- Draft and commit/send/pay/delete are separate actions.
- Tool schemas should be narrow, typed, validated, and auditable.
- Context should be tight, source-aware, and loaded just in time.
- Skills and connectors use progressive disclosure; do not expose every capability up front.
- Long-running goals need budgets, checkpoints, resumable state, and a measurable done condition.
- Observability records events and outcomes without exposing hidden reasoning.
- Sandboxes and permission gates belong in the harness, not in the agent's self-restraint.
- Treat classifier-based permission helpers as advisory unless a deterministic policy layer can still deny unsafe actions.

## MVP Blueprint Output

When asked to design an agent, produce:

- objective and MVP boundary;
- autonomy and risk model;
- core loop;
- instruction architecture;
- tool registry and permissions;
- context, memory, retrieval, and compaction;
- skills/connectors;
- safety and approvals;
- sandbox, scheduling, and managed-agent boundaries when relevant;
- observability and evals;
- minimal implementation path.

Avoid multi-agent systems until a single-agent harness has measurable failure cases that require decomposition.
