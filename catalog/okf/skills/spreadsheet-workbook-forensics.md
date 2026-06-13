---
type: "Skill Catalog Entry"
title: "Spreadsheet Workbook Forensics"
description: "Edits and verifies spreadsheet workbooks while preserving structure, formatting, and target-cell correctness."
resource: "https://github.com/markoblogo/abvx-agent-skills/tree/main/skills/spreadsheet-workbook-forensics"
tags:
  - "skill"
  - "structured-data-spreadsheet-work"
  - "experimental"
  - "original"
canonical: "skills/spreadsheet-workbook-forensics"
source: "abvx-agent-skills"
status: "experimental"
kind: "skill"
---

# Summary
Edits and verifies spreadsheet workbooks while preserving structure, formatting, and target-cell correctness.

# Trigger
Edit, repair, or generate spreadsheet workbooks with structure-preserving Python. Use for Excel or spreadsheet tasks involving .xlsx/.xlsm files, formulas, lookup tables, summaries, formatting preservation, target ranges, workbook QA, or any task where cells must be computed, written, and verified rather than guessed from previews.

# Intended Use
Use for Excel or workbook tasks involving formulas, target ranges, lookups, summaries, formatting preservation, and output verification.

# Out Of Scope
Do not use for destructive workbook changes without explicit instruction. Do not expose sensitive workbook contents in summaries.

# Inputs And Outputs
Inputs: `.xlsx` or compatible workbooks, requested changes, source tables, target ranges.

Outputs: modified workbooks, Python scripts, verification notes, representative cell checks.

# Risks
- Risk: stale formulas or unevaluated outputs. Mitigation: compute literal values when needed and reopen outputs.
- Risk: formatting damage. Mitigation: preserve unrelated sheets and copy local styles.
- Risk: key mismatch. Mitigation: normalize IDs, text, dates, and numbers deliberately.

# Metadata
* Group: [Structured Data & Spreadsheet Work](/groups/structured-data-spreadsheet-work/index.md)
* Status: `experimental`
* Origin: `original`
* Version: `0.1.0`
* Owner: ABVX / Anton Biletskiy-Volokh

# Citations
* [SKILL.md](../../skills/spreadsheet-workbook-forensics/SKILL.md)
* [SKILL_CARD.md](../../skills/spreadsheet-workbook-forensics/SKILL_CARD.md)

# Attribution
ABVX original, informed by spreadsheet benchmark patterns and repeated workbook-editing failure modes.
