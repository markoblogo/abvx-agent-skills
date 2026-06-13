---
type: "Skill Catalog Entry"
title: "Token Frugal Mode"
description: "Compresses answers to save output tokens while preserving technical accuracy."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/token-frugal-mode"
tags:
  - "skill"
  - "token-economy-context-control"
  - "experimental"
  - "adapted"
canonical: "skills/token-frugal-mode"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Compresses answers to save output tokens while preserving technical accuracy.

# Trigger
Reduce output-token usage without losing technical accuracy. Use when the user asks to save tokens, be terse, stay brief, use caveman mode, use compressed answers, minimize chatter, or when the session is context-tight and the task does not need long prose.

# Intended Use
Use when the user explicitly wants lower token usage, terse answers, caveman-like compression, or when session budget is tight.

# Out Of Scope
Do not use to hide risk, skip verification, or compress safety-critical warnings into ambiguity.

# Inputs And Outputs
Inputs: user request, compression mode, current task state.

Outputs: shorter answers with preserved code, commands, errors, risks, and verification.

# Risks
- Risk: ambiguous wording. Mitigation: relax compression for high-risk or multi-step instructions.
- Risk: omitting context. Mitigation: preserve outcome, verification, and real blockers.
- Risk: meme mode overtaking utility. Mitigation: default to terse professional compression, not roleplay.

# Metadata
* Group: [Token Economy & Context Control](/groups/token-economy-context-control/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.3.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/token-frugal-mode/SKILL.md)
* [SKILL_CARD.md](../../skills/token-frugal-mode/SKILL_CARD.md)

# Attribution
ABVX adapted from local `caveman` usage plus ideas from public token-compression skills including JuliusBrussee/caveman.
