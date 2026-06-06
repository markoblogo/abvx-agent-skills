---
name: workflow-policy-layering
description: Separate workflow instructions from safety, authority, escalation, and validation rules. Use when an assistant, agent, or skill pack is getting muddled because process steps, permissions, forbidden actions, and review gates are mixed together.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: original
---

# Workflow Policy Layering

Separate operating workflow from policy and authority.

## Goal

Turn a messy assistant spec into clear layers:

- workflow;
- authority and boundaries;
- escalation;
- validation.

## Workflow

1. **Extract the workflow**
   - write the actual operating sequence without policy noise;
   - keep it in business or task language.
2. **Extract authority separately**
   - list what the assistant may do directly;
   - list what requires confirmation;
   - list what is forbidden.
3. **Extract escalation paths**
   - define what should be handed to a human, another role, or another system;
   - make the next step concrete instead of vague refusal.
4. **Extract validation**
   - define what should be checked before a response, mutation, recommendation, or delivery is considered complete;
   - keep this as a short checklist or gate list.
5. **Rewrite the spec**
   - keep workflow in the main skill body;
   - keep detailed policy and validation in `references/` or clearly named sections;
   - ensure the assistant does not confuse “can explain” with “can execute”.
6. **Run a conflict check**
   - look for steps that assume authority the policy layer does not grant;
   - look for policy text that silently changes the workflow;
   - fix contradictions before release.

## Output Shape

Return:

- workflow layer;
- authority layer;
- escalation layer;
- validation layer;
- open contradictions, if any.

## Design Rules

- Do not hide forbidden actions inside workflow prose.
- Do not let validation sprawl into generic QA philosophy.
- Keep escalation concrete and actionable.
- Treat drafts, summaries, and recommendations as different from real execution authority.
