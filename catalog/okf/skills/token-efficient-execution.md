---
type: "Skill Catalog Entry"
title: "Token Efficient Execution"
description: "Reduces token waste during execution by tightening exploration, patching, and reporting loops."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/token-efficient-execution"
tags:
  - "skill"
  - "token-economy-context-control"
  - "experimental"
  - "adapted"
canonical: "skills/token-efficient-execution"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Reduces token waste during execution by tightening exploration, patching, and reporting loops.

# Trigger
Run coding and research tasks with lower token waste by reducing repeated reads, broad rewrites, unnecessary narration, and avoidable re-analysis. Use on long tasks, heavy repos, multi-file audits, repeated debugging loops, or whenever token budget is a practical constraint.

# Intended Use
Use for long coding tasks, audits, repeated debugging loops, large repos, and context-constrained sessions.

# Out Of Scope
Do not use to skip necessary reading, tests, or explanations when the task genuinely needs them.

# Inputs And Outputs
Inputs: repository, task, failure signal, current token pressure.

Outputs: tighter work loop, smaller diffs, reduced repeated reads, concise progress updates, honest verification.

# Risks
- Risk: under-reading important context. Mitigation: still read enough to support the change.
- Risk: over-compressing updates. Mitigation: expand when ambiguity or coordination risk appears.
- Risk: false savings from skipped validation. Mitigation: verification remains mandatory.

# Metadata
* Group: [Token Economy & Context Control](../groups/token-economy-context-control/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.3.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/token-efficient-execution/SKILL.md)
* [SKILL_CARD.md](../../skills/token-efficient-execution/SKILL_CARD.md)

# Attribution
ABVX adapted from public terse-execution guidance including drona23/claude-token-efficient and from local execution patterns.
