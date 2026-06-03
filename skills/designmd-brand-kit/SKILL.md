---
name: designmd-brand-kit
description: Create, inspect, and apply DESIGN.md brand kits for brand-aware frontend work. Use when building or reviewing landing pages, frontend UI, pitch pages, redesigns, client audits, brand-matched prototypes, or researching a potential client/company where website identity, design tokens, typography, layout, components, or do/don't guidance should shape the output.
---

# DesignMD Brand Kit

Use this skill to turn a public website or provided `DESIGN.md` into practical design constraints for Codex UI work and client research.

## Inputs

Accept any of:

- a public website URL or domain,
- a generated `DESIGN.md`,
- screenshots plus notes,
- existing CSS/Tailwind tokens,
- a client/company name for research.

If only a company name is given, find the official site before analyzing current visual identity.

## Workflow

1. Gather brand evidence:
   - Prefer an existing `DESIGN.md` if provided.
   - Otherwise use [designmd.supply](https://www.designmd.supply/) or a local `context-dot-dev/designmd-supply` run when credentials are available.
   - If unavailable, manually inspect the official site, screenshots, CSS, and page content.
2. Extract constraints:
   - brand name, positioning, tone,
   - colors and semantic roles,
   - typography scale and font families,
   - spacing, radii, borders, elevation,
   - layout patterns,
   - component patterns,
   - concrete do's and don'ts.
3. Verify:
   - Check the site/screenshot for obvious mismatches.
   - Treat extracted tokens as evidence, not gospel.
   - Flag uncertainty instead of inventing precise token values.
4. Apply:
   - Generate or update `DESIGN.md`, Tailwind v4 theme tokens, CSS variables, or implementation notes as the task requires.
   - Use the brand kit as constraints, not as a demand to clone the original site.
5. For client research, summarize design implications without publishing, emailing, or changing external systems unless the user approves.

## DESIGN.md Shape

Prefer this structure:

```markdown
---
version: alpha
name:
description:
colors:
typography:
rounded:
spacing:
components:
---

## Overview
## Colors
## Typography
## Layout
## Elevation & Depth
## Shapes
## Components
## Do's and Don'ts
```

YAML values should be machine-usable. Markdown should explain when and how to apply them.

## Token Rules

- Color values should be SRGB hex strings.
- Use semantic names: `primary`, `secondary`, `surface`, `on-surface`, `muted`, `border`, `accent`, `error`.
- Typography tokens should include font family, size, weight, line-height, and intended use.
- Spacing/radii should map to a small usable scale, not every observed value.
- Component tokens should describe repeated patterns: buttons, nav, cards, forms, badges, tables, hero, footer.
- If a token is inferred, say so in prose, not in the token value.

## Tailwind v4 Output

When asked for Tailwind v4, emit tokens in CSS-first form:

```css
@theme {
  --color-brand-primary: #000000;
  --color-brand-surface: #ffffff;
  --font-brand-sans: "Inter", sans-serif;
  --radius-brand-md: 8px;
  --spacing-brand-section: 4rem;
}
```

Only write these into a project after checking the existing Tailwind setup and naming conventions.

## CSS Variables Output

When asked for CSS variables, prefer:

```css
:root {
  --brand-primary: #000000;
  --brand-surface: #ffffff;
  --brand-text: #111111;
  --brand-muted: #666666;
  --brand-radius-md: 8px;
}
```

For dark themes or alternate modes, use scoped selectors such as `[data-theme="dark"]`.

## Frontend Application Rules

- Use the brand kit to guide hierarchy, color, spacing, typography, and interaction states.
- Preserve the project's existing design system when one already exists; map brand tokens into local conventions.
- Do not copy a competitor's site one-to-one. Use compatible visual language, not imitation.
- Verify with browser screenshots when implementing UI.
- If generated UI conflicts with the brand kit, revise the UI or explain why the project context overrides the kit.

## Client And Job Search Use

For potential clients or employers:

- Add a compact brand/design read to the company notes: visual positioning, maturity, inconsistencies, opportunities.
- Identify useful outreach angles from evidence: outdated UI, inconsistent tokens, unclear hierarchy, weak conversion path, accessibility issues, performance/design debt.
- Keep claims specific and non-accusatory.
- Draft messages only; sending, applying, posting, or changing public profiles requires user approval.
- Avoid storing screenshots, contacts, resumes, or private notes in reusable global skills.

## Final Output

Report:

- source used: URL, provided `DESIGN.md`, screenshot, or manual inspection,
- core brand constraints,
- files created or changed,
- verification performed,
- uncertainty and risks.
