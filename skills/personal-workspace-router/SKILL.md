---
name: personal-workspace-router
description: Design or maintain a local personal AI workspace that routes requests to isolated domains and professional role profiles. Use when one personal operator spans projects, career, publishing, research, coaching, fitness, finance, and internal development without mixing all context or memory.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Personal Workspace Router

Build a compact local operating layer above project repos. The goal is not one giant memory file; it is routing to the smallest relevant context.

## Workspace Shape

```text
WORKSPACE/
├── AGENTS.md
├── MEMORY.md
├── DECISIONS.md
├── ROUTING-LOG.md
└── domains/
    └── <domain>/
        ├── AGENTS.md
        └── MEMORY.md
```

## Core Rules

1. **Root router first**: `AGENTS.md` maps domain signals to `domains/<name>/`.
2. **On-demand domain context**: read only the routed domain's `AGENTS.md`; read its `MEMORY.md` only when durable preferences matter or the user asks about remembered context.
3. **Professional role routing**: inside the selected domain, choose one primary role and only the supporting professionals needed for the current deliverable. A role changes stance and context, not authority.
4. **User-triggered memory**: write memory only when the user explicitly says to remember, log, save, note, or not forget something.
5. **Conflict check**: if a requested memory contradicts existing memory, show the conflict and ask how to reconcile it.
6. **Decision log sparingly**: append one-line preference signals to `DECISIONS.md` only after meaningful forks.
7. **Routing log sparingly**: append to `ROUTING-LOG.md` only after user correction, a new durable signal, or repeated ambiguity.

## Domain Creation

When adding a domain:

1. Ask a short interview:
   - domain name;
   - routing signals;
   - repo paths or external surfaces;
   - default stance and forbidden actions;
   - what memory is safe to store.
2. Create `domains/<domain>/AGENTS.md`.
3. Create `domains/<domain>/MEMORY.md` with a user-triggered policy and empty entries.
4. Add the domain to the root routing map.
5. Define initial professional role profiles only for current repeated work; route ambiguous intake through the personal assistant/coordinator.

## Guardrails

- Do not ask for confirmation before every routine step; ask only when route, memory, or action risk is real.
- Do not store secrets, credentials, private contacts, raw transcripts, or bulky logs.
- Do not turn every successful route into a routing-log entry.
- Do not let personal workspace rules override repo-local safety, tests, or approval gates.
- Do not treat role routing as durable memory, model selection, tool permission, or external-action approval.

## Pair With

- `project-context-bootstrap` when a repo/domain has weak starting context.
- `durable-context-maintenance` when repo docs drift after work.
- `doc-grounded-grilling` when domain language or durable decisions need sharpening.
- `agent-learning-layer-triage` when deciding whether a lesson belongs in memory, docs, a skill, script, or eval.
- `role-skill-pack-design` when defining or adapting the professional profiles used within domains.

## Final Report

Return the workspace path, created domains, initial professional roles, memory policy, decision-log policy, and unresolved routing ambiguities.
