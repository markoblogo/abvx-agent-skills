---
name: html-brief-artifact
description: Create a self-contained HTML brief for plans, status updates, PR summaries, incident notes, research explainers, or other structured narrative deliverables. Use when the user wants a polished standalone artifact instead of markdown, slides, or a full frontend.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# HTML Brief Artifact

Produce a standalone HTML brief, not a production app surface.

Review:

- `references/implementation-plan-example.html`
- `references/pr-review-example.html`
- `references/style-notes.md`

## Best Fit

- implementation plans;
- status reports;
- PR summaries;
- incident notes;
- research explainers;
- concept briefs.

## Not The Best Fit

- live product UI;
- long manuals or knowledge bases;
- spreadsheets or dense data tables better served by other tools;
- vague "make a webpage" requests without a document goal.

## Output Contract

Create one self-contained `.html` file that:

- has no build step or external dependency by default;
- uses clear narrative hierarchy and structured sections;
- includes dark mode with CSS variables, toggle, persistence, and pre-paint theme setup;
- reads cleanly on desktop and mobile;
- stays close to source meaning unless the user asked for a rewrite.

## Content Rules

- Preserve the user's meaning. Improve clarity, not authorship drift.
- Organize into a small number of sections with clear labels.
- Use timelines, summary strips, chips, callouts, comparison blocks, or checklists only when they improve scanning.
- Keep copy concrete and operational.
- Do not inflate a short brief into a faux strategy deck.
- If uncertainty exists, label it explicitly instead of smoothing it away.

## Visual Rules

- Favor calm, document-like presentation over app chrome.
- Use one accent family and disciplined spacing.
- Let headings carry hierarchy.
- Use cards, tables, and lists as tools, not defaults.
- Avoid generic landing-page composition.

## Verification

Before finishing:

1. Open the artifact in a browser.
2. Check desktop and mobile readability.
3. Check long lines, wrapping, and section spacing.
4. Check the theme toggle and persistence.
5. Check print-like readability if the artifact is document-heavy.
6. Report inferred structure or content gaps honestly.

Pair with `browser-verification` when browser tooling is available.

## Final Report

Include:

- output file path;
- brief type;
- source material transformed;
- browser checks run;
- assumptions made.
