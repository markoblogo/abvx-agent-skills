# Skill Card: rtk-assisted-shell

## Description
Applies RTK-style output filtering to shell-heavy coding and debugging workflows to reduce context waste.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when git, shell reads, searches, tests, builds, linters, and logs would otherwise flood the conversation with raw output.

## Out of Scope
Do not use where exact raw output format is mandatory for parsing, or where compression would hide decisive failure detail.

## Sources and Attribution
ABVX adapted from RTK ideas around command rewriting, compact output filters, and shell-first token reduction.

## Inputs and Outputs
Inputs: planned shell commands, installed tool availability, expected signal.

Outputs: RTK-style commands or manual compact equivalents, shorter shell artifacts, and preserved decisive evidence.

## Risks and Mitigations
- Risk: filtered output hides detail. Mitigation: broaden from RTK summary to targeted raw excerpt only as needed.
- Risk: missing RTK install. Mitigation: fall back to manual compact shell patterns.
- Risk: format mismatch. Mitigation: keep raw command path when exact formatting matters.

## Evaluation
Evaluated by structural validation and manual review against git, test, and log workflows.

## Version
0.5.0

## Reporting Issues
Open an issue in the repository.
