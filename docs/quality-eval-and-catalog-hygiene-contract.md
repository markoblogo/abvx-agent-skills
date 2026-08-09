# Quality Eval And Catalog Hygiene Contract

`abvx-agent-skills` can adopt a compact subset of the useful quality discipline
seen in larger agent marketplaces without copying the marketplace model itself.

This contract keeps the repo small, reviewable, and validation-gated while
still treating skills and catalog entries as maintained artifacts rather than
prompt dumps.

## Goal

Make every published skill and every catalog entry defensible:

- the skill should be structurally valid;
- the catalog should describe the real skill, not a marketing rewrite;
- quality changes should be evidence-backed.

## Quality-eval minimum

Treat each skill as a versioned artifact with explicit evaluation, even when
the evaluation remains lightweight.

Minimum expected layers:

- structural validation;
- intended-use and risk review;
- at least one bounded evidence path for whether the skill helps or harms.

Good evidence can include:

- rollout notes;
- held-out fixtures;
- activation checks;
- before/after task comparisons;
- bounded evaluation results.

## Catalog hygiene

The catalog is a maintained projection of the repo, not a second editorial
surface.

Catalog entries should stay:

- source-linked;
- concise;
- synchronized with the actual skill files;
- explicit about intended use, risks, and related skills.

Do not let catalog text drift into:

- hype;
- invented capabilities;
- stale descriptions after a skill changed;
- category sprawl that hides the pack's real shape.

## Source of truth

The skill directory remains canonical:

- `skills/<name>/SKILL.md`
- `skills/<name>/SKILL_CARD.md`
- optional scripts, references, and assets

Derived catalog artifacts such as `docs/catalog.json`, `CATALOG.md`, or public
catalog pages must be regenerated from repo truth and checked for drift.

## Publish gate

Before a new skill or a materially changed skill is treated as published:

- validate structure;
- confirm catalog metadata is present and accurate;
- record evaluation or the reason evaluation is still limited;
- keep acceptance human-reviewed.

## GEPA-style note

If later experiments use GEPA-style search for prompt or skill improvement,
keep the adaptation narrow:

- optimize only versioned text artifacts with stable evaluators;
- preserve useful trace detail such as failure classes, judge notes, or tool
  errors instead of reducing every run to one scalar score;
- keep search budgeted by candidate count and evaluation cost;
- treat optimizer output as proposal material until held-out validation and
  maintainer review pass.
## Boundary

- this repo does not become a giant marketplace;
- quantity is not a goal by itself;
- skill quality beats catalog size;
- no automatic promotion from draft idea to published pack entry without
  maintainer review.
