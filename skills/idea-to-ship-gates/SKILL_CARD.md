# Skill Card: idea-to-ship-gates

## Description
Routes vague ideas and product changes through delivery gates: intent, spec, slices, architecture, execution, proof, convergence, and release.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use when a task is bigger than a one-shot fix and needs a disciplined path from idea to shipped slice without adopting a heavyweight project-management workflow.

## Out of Scope
Do not use for tiny edits, pure research notes, or tasks where the user explicitly wants exploration without implementation. It is a delivery router, not a replacement for product judgment or repo-specific tests.

## Sources and Attribution
ABVX adapted. Informed by ABVX LoopOps practice, existing ABVX delivery gates, and public gated delivery patterns in smixs `disruptor-skills`: setup routers, architecture guardrails, slice breakdown, QA, and converge-and-polish loops. The ABVX version is rewritten as a compact composable router and does not install or vendor the upstream skill pack.

## Inputs and Outputs
Inputs: idea, feature request, repo context, constraints, available tests, release target, and current proof artifacts.

Outputs: gate classification, next gate action, acceptance criteria, proof record, convergence decision, and release or handoff recommendation.

## Risks and Mitigations
- Risk: ceremonial process. Mitigation: start at the first missing gate and skip gates already satisfied by evidence.
- Risk: fake progress. Mitigation: require proof before review and release gates.
- Risk: over-scoping. Mitigation: reslice when the current slice crosses too many boundaries.
- Risk: installing external workflows wholesale. Mitigation: adapt only the small gate pattern that improves ABVX delivery discipline.

## Model Sensitivity
Works best on models that can separate product uncertainty from engineering uncertainty and can route to more specific skills when a gate needs depth.

## Composable With
- `rapid-grilling`
- `spec-to-prd`
- `plan-to-issues`
- `delivery-preflight-gate`
- `phase-spec-execution`
- `test-driven-execution`
- `delivery-baseline-audit`
- `agent-learning-layer-triage`

## Anti-Patterns
- creating PRDs for obvious one-line fixes
- calling a feature shipped before proof exists
- using release notes as verification
- looping on vague review feedback without acceptance criteria
- importing an entire external skill pack when one routing pattern is enough

## Evaluation
Evaluated by structural validation and by checking whether medium-sized tasks produce clearer slices, proof records, and release decisions than an ungated implementation pass.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
