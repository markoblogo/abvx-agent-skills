---
name: agent-friction-ledger
description: Capture recurring agent-development friction as a local, privacy-safe Markdown report. Use only when the user explicitly requests a friction review or a session has repeatedly hit blockers, misleading errors, missing documentation, incompatible tools, or manual workarounds that should improve a doc, tool, skill, process, or evaluation.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Agent Friction Ledger

Turn repeatable agent friction into a small, actionable local artifact. This skill is opt-in and never sends session data outside the workspace.

## Trigger

Use only when:

- the user explicitly asks for a friction report or review; or
- a session has a repeated blocker or workaround worth preserving.

Do not run merely because a task had normal shell output, a single failed command, or a clean completion.

## Capture Rules

Record only friction that is actionable and evidenced by the current task:

- repeated blocker or retry loop;
- misleading, incomplete, or contradictory error;
- missing, stale, or hard-to-find documentation;
- tool, provider, environment, or version incompatibility;
- manual workaround that should become a durable improvement.

Do not record every tool call, full conversation, raw logs, private URLs, credentials, personal data, client data, or unrelated working-tree changes.

## Workflow

1. Name the task boundary and identify only the material friction events.
2. For each event, record: `symptom -> attempted -> root cause -> resolution -> durable fix`.
3. Mark confidence: confirmed, likely, or unresolved. Do not turn a guess into a root cause.
4. Redact or omit sensitive content before writing.
5. Write a local report at `artifacts/agent-friction/YYYY-MM-DD-<task>.md` unless the repo defines an approved alternative.
6. Group action items under `docs`, `tooling`, `skill/process`, and `research`.
7. Propose the smallest durable change, but do not apply it without normal task authorization.

## Report Shape

```markdown
# Agent Friction Report: <task>

## Scope
## Material Friction
### <short label>
- Symptom:
- Attempted:
- Root cause: <confirmed|likely|unresolved>
- Resolution:
- Durable fix:

## Action Items
### Docs
### Tooling
### Skill / Process
### Research

## Decision
- Keep local / propose follow-up / no durable change
```

## Guardrails

- Local Markdown only. Never POST to a viewer, telemetry endpoint, or external API.
- A friction report is not permission to create a ticket, alter a skill, edit docs, or change a process.
- Prefer one concise report over a growing per-turn buffer.
- If the task contains regulated, personal, client, deal, financial, or credential data, record the abstract failure mode only.

## Pair With

- `repo-debugging-ledger` for hypothesis-driven technical diagnosis;
- `durable-context-maintenance` when an accepted fix belongs in repo context;
- `token-usage-audit` when the friction is context or tool-output waste;
- `skillopt-evolve-skills` and `bounded-evaluation` when an accepted skill change needs validation.

## Provenance

Adapted from `aurorascharff/agent-friction-skill`, narrowed to explicit, local-only, privacy-safe friction capture with proposal-gated follow-up.
