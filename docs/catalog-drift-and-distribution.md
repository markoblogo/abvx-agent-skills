# Catalog Drift And Distribution

This note covers three things:

- drift checking for generated catalog surfaces;
- category hygiene;
- which surfaces are published where.

## Drift checker rule

`docs/catalog.json` and `CATALOG.md` are generated projections.

They should be regenerated and checked whenever a change affects:

- `SKILL.md`
- `SKILL_CARD.md`
- `agents/openai.yaml`
- README category lanes that drive catalog grouping or positioning

If generated catalog artifacts drift from source truth, commit the regenerated
outputs in the same change.

## Category hygiene

Categories should remain:

- few enough to scan quickly;
- broad enough to absorb nearby skills;
- specific enough to preserve search value.

Do not add a new category unless an existing one clearly misfits the skill and
the new lane will hold more than one narrow edge case over time.

## Distribution surface matrix

| Surface | Purpose | Publish target |
| --- | --- | --- |
| `SKILL.md` + `SKILL_CARD.md` | canonical skill truth | GitHub repo |
| `docs/catalog.json` | machine-readable generated catalog | GitHub repo + ABVX Lab consumer |
| `CATALOG.md` | scan-friendly generated text catalog | GitHub repo |
| `docs/index.html` / Lab page | searchable public browsing surface | ABVX Lab |
| package metadata / PyPI | install and package discovery | package registry |
| outreach docs | submission and listing support | GitHub repo |

## Boundary

- GitHub repo remains the source of truth;
- ABVX Lab is a public catalog consumer, not a separate editorial source;
- package metadata should stay compact and install-oriented, not become a full
  catalog copy.
