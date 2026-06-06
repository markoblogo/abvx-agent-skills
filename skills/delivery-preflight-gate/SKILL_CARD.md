# Skill Card: delivery-preflight-gate

## Description
Runs a compact baseline preflight before long implementation or autonomous execution so the agent does not thrash against pre-existing repo breakage.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use before multi-phase delivery, autonomous execution loops, migrations, or risky feature slices where a broken baseline would distort later verification.

## Out of Scope
Do not force heavyweight preflight for trivial one-file edits or exploratory work where no meaningful repo command exists.

## Sources and Attribution
ABVX adapted from the preflight and mandatory-command discipline in robzilla1738 `supergoal`, rewritten as a compact reusable skill for Codex-style project work.

## Inputs and Outputs
Inputs: task scope, repo command surface, current workspace state.

Outputs: deduplicated baseline commands, green/red classification, and a proceed-or-fix recommendation.

## Risks and Mitigations
- Risk: overchecking small tasks. Mitigation: require the smallest useful command set.
- Risk: treating pre-existing failures as new regressions. Mitigation: classify baseline state before implementation.
- Risk: false confidence from skipped checks. Mitigation: require honest reporting of skipped or unavailable commands.

## Evaluation
Evaluated by structural validation and manual review against multi-phase delivery workflows.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
