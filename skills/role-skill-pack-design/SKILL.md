---
name: role-skill-pack-design
description: Design role-specific or workflow-specific agent skill packs without collapsing everything into one prompt. Use when creating assistant layers for teams, products, functions, or operating roles. Define base-vs-difference layers, pack boundaries, references, triggers, and rollout order.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: original
---

# Role Skill Pack Design

Design a reusable skill pack for role-based or workflow-based agent behavior.

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
2. **Inventory shared vs specialized behavior**
   - identify what every role shares;
   - identify what changes by role, workflow, or review depth;
   - avoid creating separate skills when a difference layer would be enough.
3. **Choose the pack structure**
   - keep one directory per skill;
   - keep `SKILL.md` short;
   - move detailed rules, examples, and schemas into `references/`.
4. **Model inheritance explicitly**
   - define the base workflow skill first;
   - define supervisory or wider-scope skills as difference layers on top of the base;
   - document when a user should switch to a narrower or wider mode.
5. **Define boundaries**
   - list what the assistant can do;
   - list what it must escalate, refuse, or leave to humans;
   - separate guidance, draft help, and verification from state-changing authority.
6. **Define rollout order**
   - start with the smallest set that proves the pattern;
   - prefer 2-3 core skills before a full role matrix;
   - add later skills only after the first pack is stable in use.
7. **Produce the design summary**
   - pack purpose;
   - skill list;
   - private vs reusable notes;
   - known gaps and next additions.

## Design Rules

- Base workflow first, difference layers second.
- One skill should answer one operating question clearly.
- Prefer references over long top-level instructions.
- Do not smuggle product policy into a supposedly generic methodology skill.

## Final Report

Return the proposed pack structure, the first skills to build, the difference-layer model, and the rollout sequence.
