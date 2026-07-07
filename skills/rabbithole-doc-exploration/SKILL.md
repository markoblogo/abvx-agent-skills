---
name: rabbithole-doc-exploration
description: Use local Rabbithole for human-in-the-loop exploration of AGENTS.md, SKILL.md, SET plans, repomaps, and long repo docs. Use when the user wants to inspect, question, branch, or review dense agent-facing documents interactively before changing durable docs or workflow contracts.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: original
---

# Rabbithole Doc Exploration

Use a local Rabbithole MCP canvas to inspect dense documents with the human before turning findings into durable repo changes.

## Use When

- reviewing `AGENTS.md`, `RUNBOOK.md`, `docs/ai/repomap.compact.md`, or generated repo contracts;
- reviewing `SKILL.md` files, skill cards, or workflow packs;
- reviewing SET planner exports such as `orchestrator-bundle.json` or `rabbithole.seed.md`;
- the user wants to branch into questions from selected text instead of reading a long document linearly.

## Inputs

Good starting documents:

- `docs/ai/rabbithole.seed.md`
- `AGENTS.md`
- `RUNBOOK.md`
- `docs/ai/repomap.compact.md`
- `.set-plan/orchestrator-bundle.json`
- `.set-plan/rabbithole.seed.md`
- `skills/<name>/SKILL.md`

## Workflow

1. **Check availability**
   - If Rabbithole MCP tools are available, use `open_rabbithole` with a title and file path or content.
   - If they are not available, continue as a normal document review and tell the user Rabbithole is optional.
2. **Open the smallest useful seed**
   - Prefer `docs/ai/rabbithole.seed.md` or `.set-plan/rabbithole.seed.md` when present.
   - Otherwise open the single document the user named.
3. **Answer branches**
   - Treat each selected passage as the anchor.
   - Answer with concrete file paths, risks, and proposed doc/code follow-ups.
   - Keep answers branch-sized; do not turn every branch into a full audit.
4. **Promote findings carefully**
   - Only write durable repo docs when the finding is stable and broadly useful.
   - Keep Rabbithole notes out of CI contracts unless the repo explicitly stores them.
5. **Close with a compact synthesis**
   - List decisions, doc changes made, open questions, and any branch findings that should become tasks.

## Guardrails

- Do not make Rabbithole a required runtime dependency for generated docs, skills, or SET.
- Do not treat Rabbithole canvas state as source of truth.
- Do not paste secrets, private profiles, or sensitive local files into Rabbithole unless the user explicitly approves.
- Prefer seed docs over huge raw files.

## Fallback

If Rabbithole is unavailable, read the target document directly and produce the same synthesis without the interactive canvas.
