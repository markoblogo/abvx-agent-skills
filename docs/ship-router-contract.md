# Ship Router Contract

This repo can expose a compact ship-router layer without adopting a full agent
runtime.

The point is not to add another generic "manager" skill. The point is to make
route choice explicit when work must move toward a real ship decision.

## Use when

Use a ship-router contract when a task needs one of these choices before the
agent proceeds:

- implement now versus review first;
- one-shot execution versus bounded loop;
- local artifact versus external action;
- direct completion claim versus owner ship gate.

## Minimum routing output

A route recommendation should state:

- objective;
- chosen lane;
- why that lane is the smallest correct one;
- authority level;
- required evidence;
- approval boundary;
- ship claim boundary.

## Recommended lanes

- `direct` — implement with normal repo checks.
- `review_first` — route through an audit, critique, or proof skill before
  change or release.
- `bounded_loop` — allow repeated execution only with cadence, stop condition,
  and owner review.
- `human_gate` — pause for approval before external action or higher-risk
  mutation.
- `blocked` — stop because prerequisites or authority are missing.

## Relationship to skills

This contract should stay small and compose with existing skills rather than
replace them.

Typical pairings:

- `delivery-preflight-gate`
- `pipeline-readiness-gate`
- `confidence-fragility-review`
- `delivery-baseline-audit`
- `loop-readiness-review`
- `agent-tool-contract-review`

## Boundary

- not a promise that the task is ready to ship;
- not a replacement for proof, review, or browser verification;
- not permission for external action by default;
- not a new autonomous scheduler.

## Attribution

Adapted from the routing and ship-flow ideas in
[AgentSystemLabs/core](https://github.com/AgentSystemLabs/core), rewritten as a
small contract for skill-level composition.
