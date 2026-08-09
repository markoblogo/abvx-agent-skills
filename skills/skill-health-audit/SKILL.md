---
name: skill-health-audit
description: Audit an agent skill or skillpack for trigger fit, false activation, structure, metadata, intended use, risks, composability, model sensitivity, fixtures, held-out evidence, prompt overhead, catalog drift, and regression risk. Use when deciding whether a skill is ready to publish, revise, evaluate, or keep structural-only.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: original
  abvx_eval_tier: structural_only
---

# Skill Health Audit

Review a skill as a versioned procedural artifact. The audit produces evidence
for a maintainer; it does not become an autonomous editing or publishing loop.

## Audit Lenses

Check the target skill and its neighboring public surfaces for:

- trigger fit and false activation;
- required structure and metadata;
- intended use, out-of-scope boundaries, risks, and anti-patterns;
- composability and conflict with neighboring skills;
- model sensitivity and instruction-following burden;
- activation cases, positive fixtures, negative cases, and fixture/held-out evidence;
- prompt bloat, repeated rules, and context overhead;
- catalog/README drift, card drift, and generated-artifact drift;
- regression risk, unsafe authority expansion, and missing human gates;
- the highest evidence-supported evaluation tier.

## Method

1. Identify the target skill version, source paths, and evaluation scope.
2. Read the trigger and output contract before reading supporting prose.
3. Inspect the card, metadata, companion skills, fixtures, and catalog entry.
4. Run only the available deterministic checks; label absent runtime evidence.
5. Check one positive activation and one negative/anti-pattern case where
   fixtures exist.
6. Rank findings by user harm, false confidence, drift, and maintenance cost.
7. Recommend `structural_only`, `fixture_checked`, `rollout_checked`, or
   `held_out_validated` only when the captured evidence supports it.

## Review Status

Return exactly one recommendation:

- `ACCEPT` — contract and evidence are adequate for the stated tier;
- `REVISE` — concrete changes are needed before acceptance;
- `INSUFFICIENT_EVIDENCE` — the skill may be sound but the claimed tier is not
  proven;
- `REJECT` — the skill is unsafe, redundant, misleading, or not reusable.

## Output

```text
Skill: <name>
Version: <card/frontmatter version>
Recommended tier: <tier>
Status: ACCEPT | REVISE | INSUFFICIENT_EVIDENCE | REJECT

Trigger fit: <finding>
Structure/metadata: <finding>
Evidence: <fixtures, reports, or missing proof>
Drift: <catalog/README/card result>
Regression and authority risk: <finding>
Top findings: <ranked list>
Maintainer decision needed: <yes/no and scope>
```

The audit must not edit skills, catalog files, `best_skill.md`, release files,
or installed skills. It must not promote a draft or treat a persuasive prose
review as behavioral evidence.

## Composition

- Use `bounded-evaluation` to design stronger fixture or held-out checks.
- Use `private-vs-publishable-skill-audit` before public extraction.
- Use `context-degradation-review` for prompt bloat or instruction conflict.
- Use `confidence-fragility-review` when the claimed tier exceeds its proof.
