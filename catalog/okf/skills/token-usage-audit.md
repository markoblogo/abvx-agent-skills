---
type: "Skill Catalog Entry"
title: "Token Usage Audit"
description: "Audits token waste categories and maps them to the smallest useful corrective skill or policy change."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/token-usage-audit"
tags:
  - "skill"
  - "token-economy-context-control"
  - "experimental"
  - "adapted"
canonical: "skills/token-usage-audit"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Audits token waste categories and maps them to the smallest useful corrective skill or policy change.

# Trigger
Audit where tokens are being wasted across startup context, shell output, repeated file reads, bloated agent docs, oversized summaries, and compaction loss. Use when token budget is tight, sessions are degrading, or an agent setup needs measurement-driven optimization.

# Intended Use
Use when token budget is tight, sessions are degrading, or a Codex setup needs measurement-driven context optimization.

# Out Of Scope
Do not build heavyweight telemetry or dashboards when a dominant waste category is already obvious from local evidence.

# Inputs And Outputs
Inputs: current session behavior, startup docs, shell usage, repeated-read patterns, compaction pain points.

Outputs: a ranked waste diagnosis, corrective skills or config changes, and expected savings.

# Risks
- Risk: over-instrumentation. Mitigation: use coarse categories and local evidence first.
- Risk: optimizing the wrong layer. Mitigation: rank waste categories before acting.
- Risk: audit churn. Mitigation: record only the highest-value findings and interventions.

# Metadata
* Group: [Token Economy & Context Control](../groups/token-economy-context-control/index.md)
* Status: `experimental`
* Origin: `adapted`
* Version: `0.5.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/token-usage-audit/SKILL.md)
* [SKILL_CARD.md](../../skills/token-usage-audit/SKILL_CARD.md)

# Attribution
ABVX adapted from Token Optimizer ideas around waste categorization, intervention loops, and verifying whether optimization actually helped.
