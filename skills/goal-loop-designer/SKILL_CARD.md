# Skill Card: goal-loop-designer

## Description
Compiles a raw agent `/goal` or long task prompt into a bounded loop harness with clearer stop rules, verification rubric, judge prompt, budget policy, and portable YAML/JSON/Mermaid artifacts.

## Owner
ABVX / Anton Biletskiy-Volokh

## License
MIT. See repository LICENSE.

## Intended Use
Use before starting long Codex, Claude Code, MiMo Code, Ollama/OpenAI-compatible, or generic CLI-agent runs where the goal needs stronger completion criteria, budget controls, and independent evaluation.

## Out of Scope
Do not use to run autonomous loops by itself, approve destructive actions, collect provider credentials, or replace deterministic tests with model judgment when real checks exist.

## Sources and Attribution
ABVX original, informed by LoopOps practice, Claude Code `/goal` workflows, local MiMo Code evaluation experiments, and public loop-harness discussions including ksimback `looper`.

## Inputs and Outputs
Inputs: raw goal, target agent host, repo or artifact scope, allowed and forbidden actions, available verification checks, judge options, and budget limits.

Outputs: improved goal, supervisor contract, verification rubric, judge prompt, budget policy, Mermaid diagram, YAML spec, JSON spec, and manual run commands for the chosen host.

## Risks and Mitigations
- Risk: process overhead for small tasks. Mitigation: classify single-pass work and reject unnecessary loops.
- Risk: token burn from broad iteration. Mitigation: require iteration, time, model-call, or file-scope limits.
- Risk: weak self-evaluation. Mitigation: prefer deterministic checks and separate judge models where feasible.
- Risk: unsafe autonomy. Mitigation: require explicit forbidden actions and human approval gates for destructive, external, credentialed, expensive, or privacy-sensitive steps.

## Model Sensitivity
Works best on models that can produce structured artifacts and keep budget boundaries stable. Smaller local models may be useful as judges only after a direct response smoke test passes.

## Composable With
- `loopops-protocol`
- `delivery-preflight-gate`
- `phase-spec-execution`
- `recovery-loop-3strike`
- `token-efficient-execution`

## Anti-Patterns
- compiling every one-off prompt into a loop
- using an LLM judge when tests or static checks already decide success
- omitting non-goals and forbidden actions
- allowing retries without a new hypothesis or changed evidence

## Evaluation
Evaluated by structural validation, manual review, and applying the generated harness to real ABVX coding-agent tasks before long autonomous runs.

## Version
0.1.0

## Reporting Issues
Open an issue in the repository.
