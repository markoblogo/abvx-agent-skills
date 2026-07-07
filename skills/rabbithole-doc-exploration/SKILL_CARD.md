# Skill Card: rabbithole-doc-exploration

## Description
Uses local Rabbithole as an optional human-in-the-loop reading canvas for dense agent-facing docs, skills, SET plans, and repo context seeds.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when a human wants to inspect, question, and branch through generated repo contracts or skill docs before making durable changes.

## Out of Scope
Do not use as CI, source of truth, branch manager, or required dependency for ABVX products.

## Sources and Attribution
Inspired by Rabbithole's local MCP canvas pattern: open a document, select text, ask questions, and branch answers into child documents.

## Inputs and Outputs
Inputs: seed markdown files, AGENTS/RUNBOOK docs, repomaps, SET planner exports, skill docs.

Outputs: branch answers, compact synthesis, and optional follow-up edits to durable repo docs.

## Risks and Mitigations
- Risk: hidden dependency. Mitigation: Rabbithole is optional and has a direct-review fallback.
- Risk: canvas notes become stale source of truth. Mitigation: promote only stable findings into repo docs.
- Risk: sensitive local context exposure. Mitigation: avoid secrets and private files unless explicitly approved.

## Evaluation
Evaluated by structural validation and manual review against AGENTS.md, skill, and SET planning review scenarios.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
