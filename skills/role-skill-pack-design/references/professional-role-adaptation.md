# Professional role adaptation

Use this reference when turning external professional personas into real product, personal, or internal agents.

## Role maturity

Keep these states distinct:

1. `PATTERN_SOURCE`: reviewed donor material only.
2. `ROLE_PROFILE`: purpose, context, deliverables, and boundaries are defined.
3. `ROUTABLE_PROFILE`: a deterministic or reviewed router can select the role.
4. `ASSISTANT`: a model can advise or draft through evaluated inputs and outputs.
5. `TOOL_AGENT`: the role can use an allowlisted tool set within explicit policy.
6. `BOUNDED_AUTONOMY`: selected actions are pre-authorized, observable, reversible where possible, and independently evaluated.

Promotion is per role and per action. A stronger model, a longer prompt, or a successful demo does not advance authority.

## Adaptation card

For each role, record:

- role ID, purpose, owner, and maturity;
- activation and exclusion signals;
- primary and supporting role relationships;
- approved context sources and memory scope;
- capabilities and expected deliverables;
- tools, source policy, action policy, and approval boundary;
- escalation and handoff artifacts;
- donor source, license, retained patterns, and rejected patterns;
- evaluation fixtures, observed outcomes, and promotion decision.

## Common role families

- Product operations: support, success, research, finance, compliance, sales, domain officers.
- Internal delivery: senior engineer, architect, reviewer, test engineer, incident responder, technical writer.
- Publishing: market researcher, writer, editor, designer, publishing manager, distribution analyst.
- Career: opportunity researcher, career advisor, application writer, interview coach, accountability coach.
- Personal operator: assistant/coordinator, personal coach, fitness coach, financial planner, business strategist.

Role families are starting maps. Build only roles tied to current work.

## Routing rules

- Use the coordinator as fallback for ambiguous or cross-domain intake.
- Choose one primary professional for the current deliverable.
- Add a supporting professional only when its output is an explicit dependency.
- Do not load all role prompts or memories into one context.
- Ask one focused question when the route changes access, memory, cost, or external-action requirements.
- User corrections are routing evidence; update durable routing only when the user asks to retain the preference.

## Evaluation

Use realistic tasks and verify:

- correct activation and abstention;
- domain accuracy and source use;
- unsupported-claim rate;
- context and tool cost;
- authority and privacy boundary compliance;
- usefulness of the deliverable;
- handoff completeness when another role continues the work.

Compare an adapted role with the existing baseline. Keep a donor pattern only when it improves the observed result enough to justify added context and maintenance.
