# Skill Card: evidence-ledger-research

## Description
Researches evidence-sensitive questions with source, date, unit, table, and operand discipline.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use for web research, document QA, PDF/table extraction, financial or policy facts, calculations, and source-cited answers.

## Out of Scope
Do not use as a substitute for professional legal, medical, financial, or compliance review. Do not compute from unsupported operands.

## Sources and Attribution
ABVX original, informed by SkillOpt-style validation and repeated source-grounding failures in agent work.

## Inputs and Outputs
Inputs: user questions, documents, URLs, data tables, extracted facts.

Outputs: evidence ledgers, sourced claims, calculations, concise final answers.

## Risks and Mitigations
- Risk: stale or wrong sources. Mitigation: prefer primary sources and verify volatile facts.
- Risk: table misread. Mitigation: match row labels, headers, units, periods, and footnotes.
- Risk: arithmetic drift. Mitigation: confirm operands before calculating.

## Evaluation
Evaluated by structural validation and manual review against research, document QA, and table-calculation tasks.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
