---
type: "Skill Catalog Entry"
title: "Private Vs Publishable Skill Audit"
description: "Audits private skill packs before publication by classifying content as private, mixed, or reusable and gating release on real decontextualization."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/private-vs-publishable-skill-audit"
tags:
  - "skill"
  - "research-knowledge-methods"
  - "experimental"
  - "original"
canonical: "skills/private-vs-publishable-skill-audit"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Audits private skill packs before publication by classifying content as private, mixed, or reusable and gating release on real decontextualization.

# Trigger
Audit a private skill, prompt pack, or assistant workflow before publishing it. Use when extracting public reusable method from client, product, team, or repository-specific agent instructions. Mark private vs mixed vs reusable content, rewrite the mixed layer, and gate release on decontextualization.

# Intended Use
Use when extracting open reusable method from private assistant layers, client-specific prompts, product operating packs, or repository-specific skill sets.

# Out Of Scope
Do not use as a substitute for legal review, contractual review, or privacy review where those are required separately.

# Inputs And Outputs
Inputs: private skill pack contents, references, templates, examples, and packaging plan.

Outputs: classified inventory, rewritten mixed layer, and a release-safe artifact set.

# Risks
- Risk: accidental leakage. Mitigation: force explicit private / mixed / reusable classification.
- Risk: generic mush after cleanup. Mitigation: require the artifact to remain useful outside the original environment.
- Risk: publishing too much at once. Mitigation: publish only the release-safe subset.

# Metadata
* Group: [Research, Knowledge & Reusable Methods](../groups/research-knowledge-methods/index.md)
* Status: `experimental`
* Origin: `original`
* Version: `0.1.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/private-vs-publishable-skill-audit/SKILL.md)
* [SKILL_CARD.md](../../skills/private-vs-publishable-skill-audit/SKILL_CARD.md)

# Attribution
ABVX original, refined from practical public extraction of private role/workflow skill packs.
