# Skill Card: brief-first-execution

## Description
Creates and maintains a single working brief for non-trivial tasks so scope, non-goals, risks, verification, and done criteria do not drift.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use before substantial implementation, audits, migrations, or long-running tasks that need one stable source of truth.

## Out of Scope
Do not force a brief onto tiny low-risk edits where the ceremony costs more than the clarity.

## Sources and Attribution
ABVX original, shaped by repeated long-session execution where drift and implicit scope caused more waste than the coding itself.

## Inputs and Outputs
Inputs: user request, repo context, blast radius, known risks, expected verification.

Outputs: a compact task brief that can be updated as the work evolves.

## Risks and Mitigations
- Risk: stale briefs. Mitigation: require updates when scope changes materially.
- Risk: empty ceremony. Mitigation: skip for trivial work and keep the brief compact.
- Risk: verification added too late. Mitigation: define checks before deep implementation starts.

## Evaluation
Evaluated by manual review against long-run implementation and audit scenarios.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
