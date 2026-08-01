# Generated Skill Review Gate

`abvx-agent-skills` may use generated skill drafts as proposal material. A
generated skill is not accepted, installable, catalog-visible, or published
until it passes the normal pack review gates.

This is a compact adaptation of the useful part of
`yusufkaraaslan/Skill_Seekers`: source-to-skill generation, quality reporting,
and multi-target packaging. This repo keeps the review and catalog authority.

Source: https://github.com/yusufkaraaslan/Skill_Seekers

## Intake requirements

Every generated skill proposal must include:

- source URL, repo, file, document, or export path;
- source version, commit, date, or checksum when available;
- generation command or tool;
- model/agent used for enhancement, if any;
- included and excluded source ranges;
- known conflicts or stale-source risks.

## Review gates

Before a generated skill can be accepted:

- trigger is narrow and actionable;
- `SKILL.md` follows local progressive-disclosure expectations;
- `SKILL_CARD.md` states intended use, risks, and evaluation;
- references are source-linked and license-safe;
- catalog fields are complete and accurate;
- eval tier is assigned honestly;
- generated wording is edited for pack voice and no invented capabilities.

## Quality states

Use these proposal states:

- `generated_draft`;
- `needs_source_review`;
- `needs_eval`;
- `accepted_for_pack`;
- `rejected_with_reason`.

`accepted_for_pack` still requires maintainer review and the normal generated
catalog drift checks.

## Boundary

Do not accept:

- generated skills that only summarize upstream docs;
- huge monolithic skills from large doc sites;
- platform upload or marketplace publish automation;
- source material with unclear license;
- skill claims without a fixture, rollout note, or explicit structural-only
  limitation.

Generated skill production is a drafting aid, not a publication route.
