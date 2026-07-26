# Catalog Eval Tiers

Public skills do not all have the same evidence depth. The catalog should make
that legible.

## Tiers

- `structural_only`
  - passes repository validation and metadata checks
  - no stronger behavior evidence recorded yet

- `fixture_checked`
  - at least one bounded fixture, activation test, or deterministic check exists

- `rollout_checked`
  - at least one real or mock rollout produced usable evidence about the skill's
    behavior

- `held_out_validated`
  - the skill has been checked against an independent or held-out set beyond its
    original drafting examples

## Rule

Higher tiers do not imply global superiority. They only describe the current
evidence depth for that skill.

Canonical source: `skills/<name>/SKILL.md` frontmatter metadata field
`abvx_eval_tier`.

If no tier is explicitly captured yet, treat the skill as `structural_only`.
