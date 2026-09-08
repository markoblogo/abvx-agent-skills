---
name: role-skill-pack-design
description: Design professional role agents and role-specific skill packs for product, personal, and internal AI layers. Use when adapting expert-role patterns into bounded assistants, workers, reviewers, or coordinators with explicit context, authority, evaluation, and rollout rules.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: original
---

# Role Skill Pack Design

Design a reusable skill pack for role-based or workflow-based agent behavior. Treat external role catalogs as donor material that must be adapted to the actual domain and runtime.

## Goal

Produce a pack that is:

- compact at the top level;
- layered by role or workflow;
- explicit about boundaries and escalation;
- easy to audit and extend.

## Workflow

1. **Define the pack scope**
   - name the product, team, or operating surface;
   - list who the pack is for;
   - separate runtime-assistant use from development-agent use if both exist.
   - distinguish a role profile, a prompted assistant, and an agent with tools; do not claim a later maturity level from documentation alone.
2. **Qualify professional-role donors**
   - extract useful responsibilities, workflows, deliverables, and escalation patterns;
   - discard pseudo-memory, unsupported expertise claims, fixed universal metrics, undeclared tools, and authority assumptions;
   - retain source, license, selected patterns, and deviations.
3. **Inventory shared vs specialized behavior**
   - identify what every role shares;
   - identify what changes by role, workflow, or review depth;
   - avoid creating separate skills when a difference layer would be enough.
4. **Choose the pack structure**
   - keep one directory per skill;
   - keep `SKILL.md` short;
   - move detailed rules, examples, and schemas into `references/`.
5. **Model inheritance explicitly**
   - define the base workflow skill first;
   - define supervisory or wider-scope skills as difference layers on top of the base;
   - document when a user should switch to a narrower or wider mode.
6. **Define boundaries**
   - list what the assistant can do;
   - list what it must escalate, refuse, or leave to humans;
   - separate guidance, draft help, and verification from state-changing authority.
7. **Define routing and handoffs**
   - define signals that activate the role and signals that require another specialist;
   - select one primary role and only the supporting roles needed for the task;
   - keep context and memory scoped to the selected domain;
   - make cross-role outputs explicit artifacts or handoffs.
8. **Define evaluation and promotion**
   - test representative positive, negative, and multi-role requests;
   - measure task outcome, unsupported claims, context cost, boundary violations, and handoff quality;
   - promote authority separately from prompt quality.
9. **Define rollout order**
   - start with the smallest set that proves the pattern;
   - prefer 2-3 core skills before a full role matrix;
   - add later skills only after the first pack is stable in use.
10. **Produce the design summary**
   - pack purpose;
   - skill list;
   - private vs reusable notes;
   - known gaps and next additions.

## Design Rules

- Base workflow first, difference layers second.
- One skill should answer one operating question clearly.
- Prefer references over long top-level instructions.
- Do not smuggle product policy into a supposedly generic methodology skill.
- A role selection changes working stance and context; it does not grant permission or tools.
- Prefer a compact role profile plus domain references over a copied long persona prompt.

Read [references/professional-role-adaptation.md](references/professional-role-adaptation.md) when adapting an external professional-agent catalog or designing a multi-domain personal operator.

## Final Report

Return the proposed pack structure, initial roles, routing and handoffs, authority boundaries, donor provenance, evaluation plan, and rollout sequence.
