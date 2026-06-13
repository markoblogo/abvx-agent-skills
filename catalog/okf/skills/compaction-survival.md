---
type: "Skill Catalog Entry"
title: "Compaction Survival"
description: "Preserves the minimum high-value working state so long sessions survive compaction without expensive re-derivation."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/compaction-survival"
tags:
  - "skill"
  - "token-economy-context-control"
  - "experimental"
  - "adapted"
canonical: "skills/compaction-survival"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Preserves the minimum high-value working state so long sessions survive compaction without expensive re-derivation.

# Trigger
Preserve working state across long sessions and context compaction by checkpointing decisions, edited files, blockers, open hypotheses, and unresolved errors into compact resumable artifacts. Use on long coding tasks, audits, research, or any session at risk of losing state after compaction.

# Intended Use
Use on long coding tasks, audits, research sessions, and any workflow where context compaction or resume loss would be expensive.

# Out Of Scope
Do not use as a replacement for good repo docs, or as a license to store large stale histories and raw logs.

# Inputs And Outputs
Inputs: current task state, touched files, unresolved issues, existing handoff artifacts.

Outputs: compact checkpoints, resumable state summaries, and explicit artifact pointers.

# Risks
- Risk: stale checkpoints. Mitigation: update only when state materially changes and remove invalidated hypotheses.
- Risk: checkpoint bloat. Mitigation: preserve only objective, evidence, next steps, and artifact paths.
- Risk: false confidence. Mitigation: keep verification and blockers explicit.

# Metadata
* Group: [Token Economy & Context Control](/groups/token-economy-context-control/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.5.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/compaction-survival/SKILL.md)
* [SKILL_CARD.md](../../skills/compaction-survival/SKILL_CARD.md)

# Attribution
ABVX adapted from Token Optimizer ideas around compaction survival, compact checkpoints, and state restoration after long sessions.
