---
type: "Skill Catalog Entry"
title: "RTK Assisted Shell"
description: "Applies RTK-style output filtering to shell-heavy coding and debugging workflows to reduce context waste."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/rtk-assisted-shell"
tags:
  - "skill"
  - "token-economy-context-control"
  - "experimental"
  - "adapted"
canonical: "skills/rtk-assisted-shell"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Applies RTK-style output filtering to shell-heavy coding and debugging workflows to reduce context waste.

# Trigger
Use RTK-style command filtering to reduce shell-output token waste on git, file reads, searches, test runs, linters, logs, and other noisy developer commands. Use when a task depends on shell commands that may emit large output and runtime output filtering can save context.

# Intended Use
Use when git, shell reads, searches, tests, builds, linters, and logs would otherwise flood the conversation with raw output.

# Out Of Scope
Do not use where exact raw output format is mandatory for parsing, or where compression would hide decisive failure detail.

# Inputs And Outputs
Inputs: planned shell commands, installed tool availability, expected signal.

Outputs: RTK-style commands or manual compact equivalents, shorter shell artifacts, and preserved decisive evidence.

# Risks
- Risk: filtered output hides detail. Mitigation: broaden from RTK summary to targeted raw excerpt only as needed.
- Risk: missing RTK install. Mitigation: fall back to manual compact shell patterns.
- Risk: format mismatch. Mitigation: keep raw command path when exact formatting matters.

# Metadata
* Group: [Token Economy & Context Control](../groups/token-economy-context-control/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.5.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/rtk-assisted-shell/SKILL.md)
* [SKILL_CARD.md](../../skills/rtk-assisted-shell/SKILL_CARD.md)

# Attribution
ABVX adapted from RTK ideas around command rewriting, compact output filters, and shell-first token reduction.
