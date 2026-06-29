# Skill Card: delivery-preflight-gate

## Description
Runs a compact baseline preflight before long implementation, autonomous execution, or PR publication so the agent does not thrash against pre-existing repo breakage or publish a noisy branch.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use before multi-phase delivery, autonomous execution loops, migrations, risky feature slices, or push/PR flows where a broken baseline or noisy branch would distort later verification.

## Out of Scope
Do not force heavyweight preflight for trivial one-file edits, exploratory work where no meaningful repo command exists, or changes that require human approval because they touch secrets, auth, billing, destructive actions, or broad behavior.

## Sources and Attribution
ABVX adapted from the preflight and mandatory-command discipline in robzilla1738 `supergoal`, rewritten as a compact reusable skill for Codex-style project work.

Push-gate mode is inspired by the disposable worktree and gate-before-push pattern in kunchenguid `no-mistakes`, adapted here as a tool-agnostic workflow rule rather than a copy of the implementation.

## Inputs and Outputs
Inputs: task scope, repo command surface, current workspace state, intended remote/branch when publication is in scope.

Outputs: deduplicated baseline commands, green/red classification, push-gate decision when relevant, and a proceed-or-fix recommendation.

## Risks and Mitigations
- Risk: overchecking small tasks. Mitigation: require the smallest useful command set.
- Risk: treating pre-existing failures as new regressions. Mitigation: classify baseline state before implementation.
- Risk: false confidence from skipped checks. Mitigation: require honest reporting of skipped or unavailable commands.
- Risk: auto-fix scope creep before PR publication. Mitigation: isolate push-gate repair work and require approval for behavior changes or broad cleanup.

## Evaluation
Evaluated by structural validation and manual review against multi-phase delivery and PR publication workflows.

## Version
0.2.0

## Reporting Issues
Open an issue in the repository.
