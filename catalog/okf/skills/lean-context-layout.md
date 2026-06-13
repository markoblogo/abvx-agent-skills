---
type: "Skill Catalog Entry"
title: "Lean Context Layout"
description: "Restructures agent-facing repository context to reduce always-loaded token overhead."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/lean-context-layout"
tags:
  - "skill"
  - "token-economy-context-control"
  - "experimental"
  - "adapted"
canonical: "skills/lean-context-layout"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Restructures agent-facing repository context to reduce always-loaded token overhead.

# Trigger
Restructure agent-facing docs so the always-loaded context stays small and the rest is loaded on demand. Use when a repo has bloated AGENTS.md or CLAUDE-style docs, too many always-loaded notes, stale session history, oversized runbooks, or high startup token waste for coding agents.

# Intended Use
Use for repos with bloated startup docs, heavy session history, oversized agent instructions, or high token burn before work starts.

# Out Of Scope
Do not use to delete important documentation or bury critical safety constraints in obscure optional files.

# Inputs And Outputs
Inputs: repository doc layout, agent entry files, historical notes, startup context rules.

Outputs: leaner context layout, explicit on-demand references, smaller always-loaded core, token-savings report.

# Risks
- Risk: losing important context. Mitigation: relocate and index instead of deleting.
- Risk: fragmented docs. Mitigation: keep the startup core compact but coherent.
- Risk: optimizing the wrong thing. Mitigation: measure before and after.

# Metadata
* Group: [Token Economy & Context Control](../groups/token-economy-context-control/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.3.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/lean-context-layout/SKILL.md)
* [SKILL_CARD.md](../../skills/lean-context-layout/SKILL_CARD.md)

# Attribution
ABVX adapted from public context-optimization ideas including nadimtuhin/claude-token-optimizer and from local agentsgen-oriented workflow design.
