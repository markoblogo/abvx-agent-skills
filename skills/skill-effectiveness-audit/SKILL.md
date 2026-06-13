---
name: skill-effectiveness-audit
description: Audit whether installed or proposed skills appear to help, drift, or add noise using docs/ai/skill-usage.json and docs/ai/skill-effectiveness.md. Use when a repo exports skill reflection artifacts and you need to decide which skills to keep, tighten, de-emphasize, or rewrite before adding more agent instruction surface.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: original
---

# Skill Effectiveness Audit

Judge skills by observed usage patterns and downstream editing value, not by how polished the skill text looks.

## Inputs

Prefer these in order:

1. `docs/ai/skill-effectiveness.md`
2. `docs/ai/skill-usage.json`
3. related `SKILL.md` and `SKILL_CARD.md` files for the named skills

If the first two artifacts are missing, say so and ask for `agentsgen reflect skills .` before performing a manual audit.

## Audit Questions

For each relevant skill, ask:

- is it actually being invoked;
- does it correlate with fewer redirects or better plan-first behavior;
- is it low-signal because it is rare or because it is badly positioned;
- should it be kept, tightened, moved, split, or retired;
- is the problem the skill itself or the trigger wording around it.

## Audit Workflow

1. Rank skills by the strongest keep/watch/review signals.
2. Inspect only the small set that matters for the current repo.
3. For each audited skill, classify the next action:
   - keep;
   - rewrite trigger;
   - tighten body;
   - split into narrower skills;
   - demote or remove.
4. Check whether the skill duplicates higher-priority instructions or another local skill.
5. Recommend the smallest edit set that could improve the next reflection pass.

## Output Shape

Report:

- which skills look healthy;
- which skills look weak or noisy;
- the most likely reason;
- the smallest concrete edit to test next.

## Guardrails

- Do not treat the generated bucket labels as ground truth.
- Do not rewrite many skills at once from weak evidence.
- Do not confuse low usage with low value when a skill is intentionally specialized.
