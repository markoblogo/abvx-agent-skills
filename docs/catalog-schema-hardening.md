# Catalog Schema Hardening

The public catalog should be generated from stable skill truth, not from ad-hoc
copy.

## Canonical inputs

Each public skill entry should derive from:

- `skills/<name>/SKILL.md`
- `skills/<name>/SKILL_CARD.md`
- `skills/<name>/agents/openai.yaml`

## Minimum public entry fields

Each catalog entry should have, at minimum:

- `name`
- `display_name`
- `category`
- `description`
- `intended_use`
- `path`
- `card_path`
- `github_skill_url`
- `github_card_url`

Recommended when present in source truth:

- `model_sensitivity`
- `composable_with`
- `anti_patterns`
- `risks`

## Hardening rule

The catalog may shorten or normalize source text, but it must not:

- invent capabilities;
- silently omit the existence of risks;
- re-categorize a skill into a misleading lane;
- drift from the actual skill trigger or intended use.
