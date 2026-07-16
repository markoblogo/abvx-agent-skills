---
name: hook-rule-fixtures
description: Test opt-in per-project hook rules with small synthetic fixtures before rollout. Use when a warn or block hook needs match, no-match, exception, bypass, and regression cases without enabling global hooks.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: original
---

# Hook Rule Fixtures

Test a project-local rule as data before it is enabled. Do not test against live sessions, developer prompts, or unbounded repository history.

## Fixture matrix

Every rule needs these cases where applicable:

| Case | Expected result |
|---|---|
| intended match | declared `warn` or `block` with redacted evidence |
| ordinary no-match | `pass` and no evidence payload |
| allowed exception | `pass` with the exception identifier |
| missing required verification | declared promotion outcome |
| approved bypass | `pass` only with approver, reason, and expiry |

## Workflow

1. Freeze the rule version and event schema.
2. Write minimal synthetic inputs; never place live protected data in fixtures.
3. Assert `outcome`, `rule_id`, redacted evidence keys, and remediation text.
4. Add one regression fixture for every false positive or false negative found in review.
5. Start disabled, then observe in `warn`; promote to `block` only after reviewed fixture evidence supports it.

## Example fixture

```yaml
rule_id: named-verification-before-promotion
input:
  candidate:
    id: c-17
    status: ready-for-promotion
  verification:
    name: browser-smoke
    result: missing
expect:
  outcome: block
  evidence_keys: [candidate_id, verification.name, verification.result]
  remediation_contains: "Run and record"
```

## Non-goals

- Do not execute hooks globally to collect test data.
- Do not use production secrets, customer data, or full prompts as fixtures.
- Do not promote a rule because it looks plausible; retain fixture results and review notes.

## Output contract

Return the rule version, fixture table, expected result per fixture, actual result, failures, and the rollout recommendation.
