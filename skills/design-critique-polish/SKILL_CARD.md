# Skill Card: design-critique-polish

## Description
Runs a focused critique-and-polish pass for frontend interfaces before shipping.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use after a frontend surface exists and needs critique, prioritization, and final quality improvements rather than a greenfield build.

## Out of Scope
Do not use as a substitute for initial product definition, browser testing itself, or full accessibility/performance audits across an entire large product without scoping.

## Sources and Attribution
ABVX adapted from pbakaus `impeccable` critique/polish/audit workflow ideas, plus local browser verification and web quality review practice.

## Inputs and Outputs
Inputs: screenshots, routes, files, URLs, existing design context, and known constraints.

Outputs: ranked critique findings, high-leverage fix list, ship blockers, and polish guidance.

## Risks and Mitigations
- Risk: generic critique. Mitigation: force ordered review categories and concrete findings.
- Risk: over-polishing. Mitigation: separate ship blockers from later refinements.
- Risk: hiding structural issues behind visual tweaks. Mitigation: call out wrong core design language explicitly.

## Evaluation
Evaluated by structural validation and manual review against frontend QA and pre-ship polish workflows.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
