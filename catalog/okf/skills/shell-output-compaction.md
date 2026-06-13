---
type: "Skill Catalog Entry"
title: "Shell Output Compaction"
description: "Reduces shell and tool-output token waste by shaping commands toward narrow, high-signal output."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/shell-output-compaction"
tags:
  - "skill"
  - "token-economy-context-control"
  - "experimental"
  - "adapted"
canonical: "skills/shell-output-compaction"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Reduces shell and tool-output token waste by shaping commands toward narrow, high-signal output.

# Trigger
Reduce shell and tool-output token waste by preferring targeted commands, diff-only views, error-first logs, narrow slices, counts, and concise summaries instead of large raw stdout dumps. Use on coding, debugging, audits, CI triage, or repo exploration when command output is likely to dominate token usage.

# Intended Use
Use when coding, debugging, CI triage, audits, or repo exploration would otherwise generate large amounts of shell output.

# Out Of Scope
Do not use to suppress critical stack traces, hide failing assertions, or omit the only raw artifact that explains a high-risk issue.

# Inputs And Outputs
Inputs: task context, command candidates, expected signal.

Outputs: narrower commands, shorter stdout/stderr excerpts, compact summaries, and preserved key evidence.

# Risks
- Risk: over-truncating. Mitigation: preserve the first decisive error block and expand only when needed.
- Risk: missing context. Mitigation: broaden iteratively from count or match to excerpt to full artifact.
- Risk: unstable debugging loop. Mitigation: keep exact commands and line references when they affect the next action.

# Metadata
* Group: [Token Economy & Context Control](../groups/token-economy-context-control/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.4.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/shell-output-compaction/SKILL.md)
* [SKILL_CARD.md](../../skills/shell-output-compaction/SKILL_CARD.md)

# Attribution
ABVX adapted from Token Savior ideas around Bash output compaction plus existing ABVX token-efficiency patterns.
