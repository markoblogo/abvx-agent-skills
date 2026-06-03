# Skill Card: spreadsheet-workbook-forensics

## Description
Edits and verifies spreadsheet workbooks while preserving structure, formatting, and target-cell correctness.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for Excel or workbook tasks involving formulas, target ranges, lookups, summaries, formatting preservation, and output verification.

## Out of Scope
Do not use for destructive workbook changes without explicit instruction. Do not expose sensitive workbook contents in summaries.

## Sources and Attribution
ABVX original, informed by spreadsheet benchmark patterns and repeated workbook-editing failure modes.

## Inputs and Outputs
Inputs: `.xlsx` or compatible workbooks, requested changes, source tables, target ranges.

Outputs: modified workbooks, Python scripts, verification notes, representative cell checks.

## Risks and Mitigations
- Risk: stale formulas or unevaluated outputs. Mitigation: compute literal values when needed and reopen outputs.
- Risk: formatting damage. Mitigation: preserve unrelated sheets and copy local styles.
- Risk: key mismatch. Mitigation: normalize IDs, text, dates, and numbers deliberately.

## Evaluation
Evaluated by structural validation and manual review against spreadsheet edit and verification workflows.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
