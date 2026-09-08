# Skill Card: professional-role-router

## Description

Routes substantial current work to one primary professional role and a small number of supporting roles with explicit context, deliverables, handoffs, and authority boundaries.

## Owner

ABVX / Anton Biletskiy-Volokh

## License

MIT. See repository LICENSE.

## Intended Use

Use for cross-domain personal, product, career, publishing, research, coaching, finance, support, and software tasks where specialist methods materially improve the result.

## Out of Scope

Do not use for simple one-step requests, theatrical personas, bulk prompt loading, automatic memory expansion, or permission assignment.

## Sources and Attribution

ABVX original. Professional-role decomposition and workflow patterns were informed by `msitarzewski/agency-agents`; no donor prompt corpus, pseudo-memory, tool declaration, metric, or authority claim is bundled.

## Inputs and Outputs

Inputs: current request, domain context, available specialist profiles, evidence needs, privacy and action policy.

Outputs: selected primary/supporting roles, completed role-appropriate deliverable, explicit handoff artifacts, and unresolved gates.

## Risks and Mitigations

- Role sprawl: cap the route at one primary and two supporting roles.
- Persona theatre: judge success by the deliverable and evidence.
- Context leakage: pass only the minimum handoff artifact.
- Authority confusion: role selection has no authority effect.
- Unsupported expertise: domain sources and policies override generic role patterns.

## Model Sensitivity

Works across models that can follow scoped instructions and preserve source/action boundaries. Weaker models may over-select roles or blur handoffs; keep routes smaller and outputs structured.

## Composable With

- `role-skill-pack-design`
- `personal-workspace-router`
- `evidence-ledger-research`
- `test-driven-execution`
- `public-release-verification`

## Anti-Patterns

- announcing roles without changing the work method;
- loading every specialist into one context;
- letting a supporting role take over without a handoff;
- treating a role as a credential or approval;
- persisting private context because multiple roles may need it later.

## Evaluation

Structurally validated. Needs paired outcome fixtures for career, publishing, engineering, and personal-operator routes before promotion beyond `experimental`.

## Version

0.1.0

## Reporting Issues

Open an issue in the repository.
