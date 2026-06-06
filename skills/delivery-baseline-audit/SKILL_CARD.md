# Skill Card: delivery-baseline-audit

## Description
Performs an end-of-task audit against the starting baseline and the full working tree so declared deliverables are checked as shipped artifacts, not just as transcript claims.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use at the end of multi-step delivery, autonomous runs, migrations, and feature slices with explicit deliverables or high regression risk.

## Out of Scope
Do not force a baseline audit for trivial edits where the deliverable is obvious and fully covered by one direct verification loop.

## Sources and Attribution
ABVX adapted from robzilla1738 `supergoal` baseline-reference and final-audit concepts, condensed into a standalone audit skill.

## Inputs and Outputs
Inputs: baseline reference, declared deliverables, final working tree, mandatory verification commands.

Outputs: delivery audit record, gap list, and a complete-or-fix verdict.

## Risks and Mitigations
- Risk: over-auditing trivial work. Mitigation: reserve for declared-deliverable or long-run tasks.
- Risk: missing untracked or unstaged outputs. Mitigation: require full working-tree inspection.
- Risk: stale verification. Mitigation: re-run final commands once at the end.

## Evaluation
Evaluated by structural validation and manual review against delivery and audit workflows.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
