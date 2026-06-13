---
type: "Skill Catalog Entry"
title: "Evidence Ledger Research"
description: "Researches evidence-sensitive questions with source, date, unit, table, and operand discipline."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/evidence-ledger-research"
tags:
  - "skill"
  - "research-knowledge-methods"
  - "experimental"
  - "original"
canonical: "skills/evidence-ledger-research"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Researches evidence-sensitive questions with source, date, unit, table, and operand discipline.

# Trigger
Research and answer evidence-sensitive questions with source, date, unit, and operand discipline. Use for web research, PDF/document QA, policy or finance facts, tables, time series, calculations from retrieved evidence, exact-answer extraction, and any task where wrong source selection, stale facts, nearby table confusion, or formatting errors would matter.

# Intended Use
Use for web research, document QA, PDF/table extraction, financial or policy facts, calculations, and source-cited answers.

# Out Of Scope
Do not use as a substitute for professional legal, medical, financial, or compliance review. Do not compute from unsupported operands.

# Inputs And Outputs
Inputs: user questions, documents, URLs, data tables, extracted facts.

Outputs: evidence ledgers, sourced claims, calculations, concise final answers.

# Risks
- Risk: stale or wrong sources. Mitigation: prefer primary sources and verify volatile facts.
- Risk: table misread. Mitigation: match row labels, headers, units, periods, and footnotes.
- Risk: arithmetic drift. Mitigation: confirm operands before calculating.

# Metadata
* Group: [Research, Knowledge & Reusable Methods](../groups/research-knowledge-methods/index.md)
* Status: `experimental`
* Origin: `original`
* Version: `0.1.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/evidence-ledger-research/SKILL.md)
* [SKILL_CARD.md](../../skills/evidence-ledger-research/SKILL_CARD.md)

# Attribution
ABVX original, informed by SkillOpt-style validation and repeated source-grounding failures in agent work.
