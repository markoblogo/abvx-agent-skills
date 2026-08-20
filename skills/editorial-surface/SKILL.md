---
name: editorial-surface
description: Shape editorial and reading-first surfaces with strong hierarchy, readable measure, and disciplined media rhythm. Use for articles, guides, books, blog indexes, featured/recent cards, and other longform or text-heavy public surfaces.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
  abvx_eval_tier: structural_only
---

# Editorial Surface

Treat reading experience as a product requirement, not decorative polish.

Use this when the surface is text-first and the common failure mode is bad hierarchy, empty cards, oversized hero treatments, weak excerpt logic, or unreadable body rhythm.

## Best Fit

- article pages;
- blog and writing indexes;
- guide pages;
- book and booklet landing sections;
- featured and recent content cards;
- mixed text/media editorial layouts.

## Design Priorities

- title, deck, metadata, and body must read as one system;
- body measure and paragraph rhythm win over decorative hero treatment;
- cards should carry the right amount of information for their role;
- media should support reading, not interrupt it;
- text-only surfaces should still feel intentionally composed.

## Workflow

1. Identify the content role:
   - index, featured card, recent card, article page, guide, or mixed editorial section.
2. State the reading job:
   - skim, choose, commit, or read deeply.
3. Check the hierarchy:
   - label/source/date;
   - title;
   - deck/excerpt;
   - body;
   - supporting media;
   - actions and related links.
4. Fix the common structural failures first:
   - oversized title block;
   - empty right side on text-only featured cards;
   - recent cards with dead space instead of useful excerpt;
   - metadata too faint to scan;
   - body too light, narrow, or long-line;
   - video or external resources placed without narrative rhythm.
5. For mixed media, place media where it helps comprehension:
   - not automatically adjacent to cover art if that creates a media wall;
   - not after the entire article if it belongs near the core narrative.
6. Verify desktop and mobile reading comfort before calling the change ready.

## Output Shape

Return:

- `content role`
- `reading job`
- `hierarchy fixes`
- `excerpt rule`
- `media placement rule`
- `desktop/mobile reading checks`

## Guardrails

- Do not rewrite owner-approved article body unless explicitly asked.
- Do not turn editorial pages into generic marketing pages.
- Do not add decorative imagery to cover for weak hierarchy.
- Do not shrink content density so far that text-first surfaces become empty.
- Do not imitate Medium or Substack blindly when the project has its own identity.

## Final Report

Include:

- the content role handled;
- the main hierarchy correction;
- the excerpt or media rule applied;
- desktop/mobile reading evidence;
- any remaining issue that still needs `anti-slop-review` or `browser-verification`.
