---
name: html-diagram-artifact
description: Create a self-contained HTML artifact for architecture, stack, and system-flow explanation using SVG-first diagrams and minimal prose. Use when the user needs a standalone visual deliverable that makes a system, request path, ownership map, or execution flow click quickly.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# HTML Diagram Artifact

Produce a standalone HTML deliverable, not a production app surface.

Review:

- `references/architecture-example.html`
- `references/style-notes.md`

## Best Fit

- architecture overviews;
- request or event flows;
- stack explainers;
- system boundary maps;
- component relationship diagrams;
- interactive walkthroughs where flow highlighting genuinely improves understanding.

## Not The Best Fit

- full product frontends;
- landing pages;
- dense prose reports;
- diagrams that would be clearer as Mermaid or a static image;
- speculative visual polish without a concrete explanation job.

## Output Contract

Create one self-contained `.html` file that:

- works without a build step;
- uses semantic HTML plus inline CSS and JS only when needed;
- includes a dark mode toggle;
- persists theme via `localStorage`;
- applies theme before paint in `<head>`;
- uses SVG as the primary diagram surface;
- drives SVG colors from CSS variables rather than hard-coded values inside the SVG;
- remains usable on desktop and mobile widths.

## Diagram Rules

- Lead with structure first, decoration second.
- Keep prose light: title, framing line, labels, and optional detail panel.
- Prefer 1-2 dominant flows over showing every possible edge.
- Group by zones, boundaries, or ownership domains.
- Make important nodes distinct through role, not random styling.
- Use interaction only when it helps explain sequence, causality, or scope.
- Respect reduced-motion preferences.

## Visual Rules

- Use a restrained palette with one accent family.
- Use hierarchy through typography, spacing, and contrast.
- Keep labels short and scannable.
- Avoid dashboard chrome, fake browser frames, and decorative card spam.
- If serif headings help, use them sparingly.

## Verification

Before finishing:

1. Open the artifact in a browser.
2. Check desktop and mobile layouts.
3. Check there is no horizontal overflow.
4. Check the theme toggle works and persists.
5. Check SVG text remains legible in both themes.
6. Check interactive highlighting if present.
7. Report limitations honestly.

Pair with `browser-verification` when browser tooling is available.

## Final Report

Include:

- output file path;
- artifact type;
- flows or areas covered;
- browser checks run;
- known omissions or simplifications.
