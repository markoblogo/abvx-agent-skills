---
name: project-hook-guardrails
description: Design narrowly scoped, opt-in per-project hook rules with explicit warn versus block outcomes, bounded patterns and conditions, and no global observer or session hooks. Use when a repository needs a small safety or promotion guardrail without adopting a hook runtime.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Project Hook Guardrails

Design one small project-local hook rule at a time. A rule is opt-in configuration for a named repository and event; it is not a global observer, session hook, memory layer, or enforcement runtime.

## Use when

- a repository needs a warning when public and protected data appear in one artifact;
- promotion requires a named verification record;
- a project needs a narrowly bounded pre-commit, pre-publish, or promotion check;
- the team can name the event, inputs, false-positive tolerance, owner, and bypass path.

## Rule design

1. Name the project, event, and single risk.
2. Choose `warn` unless a false negative would create an irreversible or policy-breaking promotion. `block` must have an explicit owner-approved bypass.
3. Define compact `pattern` and `conditions`; do not infer broad intent from arbitrary session context.
4. State the evidence the rule emits and the remediation path.
5. Add allowlisted exceptions with expiry or issue reference.
6. Write fixtures before enabling the rule for a project.

## Reference format

```yaml
version: 1
scope:
  project: owner/repository
  enabled: false
  event: promotion_candidate
rules:
  - id: named-verification-before-promotion
    outcome: block
    pattern:
      required_fields: [verification.name, verification.result]
    conditions:
      all:
        - candidate.status == "ready-for-promotion"
        - verification.result != "passed"
    evidence: [candidate_id, verification.name, verification.result]
    remediation: "Run and record the named verifier, or use an approved one-shot bypass."
    bypass:
      requires: [approver, reason, expires_at]
```

## Two safe starters

| Rule | Default | Condition |
|---|---|---|
| `public-protected-data-mix` | `warn` | public artifact also matches a project-defined protected-data marker |
| `named-verification-before-promotion` | `block` | promotion candidate lacks a named verifier with a passing result |

Keep protected-data patterns project-defined and redacted in emitted evidence. A hook must never copy secrets or protected source material into logs.

## Non-goals

- Do not install global observer, session, or lifecycle hooks.
- Do not monitor every file, tool call, or prompt.
- Do not turn warnings into blocks without fixtures, an owner, and a bypass path.
- Do not treat hook output as hidden reasoning or as a substitute for a verifier.

## Output contract

Return a project-local rule packet:

```text
Scope: <project + event>
Mode: <disabled | warn | block>
Risk and trigger:
Evidence emitted (redacted):
Fixture matrix:
Bypass / owner:
Rollout: disabled -> shadow/warn -> reviewed block (if justified)
```

## Attribution

Adapted from the rule-shape discipline in [ECC hookify-rules](https://github.com/affaan-m/ECC/blob/main/skills/hookify-rules/SKILL.md), reduced to opt-in project rules and explicit test fixtures.
