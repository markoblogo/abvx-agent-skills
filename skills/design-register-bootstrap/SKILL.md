---
name: design-register-bootstrap
description: Establish frontend design context before implementation. Use when a project lacks a clear PRODUCT.md or DESIGN.md, when the model needs to distinguish brand surfaces from product UI, or when design direction keeps drifting because audience, register, anti-references, and visual constraints are not explicit.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Design Register Bootstrap

Set the design register before styling anything substantial.

This skill exists for cases where the model is about to generate UI from vague vibes, default templates, or half-remembered brand intent.

## Use For

- new frontend projects without `PRODUCT.md` or `DESIGN.md`;
- redesigns where the surface is unclear: marketing brand page vs. app/product UI;
- teams that keep getting mismatched typography, palette, density, or motion across tasks;
- sessions where the agent should create or refresh design context before implementation.

## Core Rule

Classify the surface first:

- `brand`: marketing site, landing page, portfolio, campaign, editorial page, investor page, event page;
- `product`: dashboard, admin UI, internal tool, settings, onboarding flow, forms, data-heavy app shell.

Do not treat these as interchangeable. Brand surfaces can lead with identity and emotion. Product surfaces must optimize comprehension, workflow, and control clarity.

## Workflow

1. Read current evidence:
   - project files, CSS tokens, component library, screenshots, references, user brief;
   - any existing `PRODUCT.md`, `DESIGN.md`, brand notes, or design tokens.
2. Write a compact design register:
   - surface type: `brand` or `product`;
   - audience;
   - first-screen job;
   - brand/product lane;
   - anti-references: what this should explicitly not resemble;
   - color strategy: restrained, committed, full palette, or drenched;
   - typography direction;
   - motion tolerance;
   - density and radius rules.
3. If context files are missing, create or update:
   - `PRODUCT.md` for audience, product lane, workflow, tone, anti-references;
   - `DESIGN.md` for colors, typography, spacing, component patterns, do/don't rules.
4. If the surface is ambiguous, ask one clarifying question only when the branch between `brand` and `product` is genuinely unclear.
5. Use the register as a constraint system for later frontend work. Do not restyle pages in the same pass unless the task explicitly includes implementation.

## Output Shape

When working inline, summarize:

- `register`
- `audience`
- `design thesis`
- `anti-references`
- `color strategy`
- `typography direction`
- `motion and density`

When creating files, prefer concise machine-usable docs over long essays.

## Guardrails

- Do not default every warm or “premium” brief to beige paper backgrounds.
- Do not default every technical product to dark mode.
- Do not choose palette or typography before writing the surface classification.
- If existing project tokens are coherent, preserve them and document them instead of replacing them.
- If the repo already has a stable design system, this skill should describe and reinforce it, not invent a second one.

## Final Report

Include:

- whether the surface was classified as `brand` or `product`;
- files created or updated;
- unresolved uncertainty;
- downstream skills recommended, such as `frontend-taste-layer`, `frontend-product-builder`, or `web-quality-audit`.
