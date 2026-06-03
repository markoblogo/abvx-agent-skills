---
name: frontend-product-builder
description: Build or improve frontend pages, apps, landing pages, pitch pages, redesigns, dashboards, and prototypes with strong hierarchy, responsive layout, real visual assets, ergonomic controls, and verification. Use when frontend quality, brand fit, product clarity, or design implementation matters.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Frontend Product Builder

Ship the usable experience first. Avoid generic card mosaics, vague hero copy, and decorative UI that does not help the user act.

## Start With A Short Thesis

Before building, define:

- audience and primary workflow;
- visual thesis: mood, material, density, and brand signal;
- first-screen job;
- key controls, states, and responsive constraints;
- verification plan.

For brand-aware work, pair with `designmd-brand-kit` or an equivalent brand extraction pass.

## Product Surface Rules

- SaaS, CRM, admin, analytics, and operations tools should be quiet, dense, and scannable.
- Landing pages need a real visual anchor and brand/product signal in the first viewport.
- Games and playful demos can be expressive, animated, and illustrative.
- Do not make a marketing landing page when the user asked for an app or tool.
- Use cards for repeated items, modals, or framed tools, not as default page sections.
- Prefer icons for obvious toolbar commands and text buttons for clear actions.
- Stable dimensions matter: boards, tiles, toolbars, controls, and counters must not resize during hover or loading.

## Implementation Loop

1. Read existing design system, components, CSS tokens, and layout conventions.
2. Build the smallest complete workflow, not only a static shell.
3. Add empty, loading, error, disabled, hover, focus, and mobile states where users expect them.
4. Use real, searched, generated, or existing assets when the subject needs visual inspection.
5. Keep text inside containers across common viewport widths.
6. Avoid palette monotony and excessive gradients.
7. Verify with browser checks: desktop, mobile, console errors, asset loads, horizontal overflow, and key interactions.

## Copy Rules

- UI text should orient, label, and enable action.
- Product surfaces use utility copy, not campaign language.
- Landing pages can be sharper, but the headline should not hide the brand or offer.
- Do not put design instructions, keyboard shortcut explanations, or implementation commentary into the UI unless the product itself requires it.

## Final Report

Include changed files, viewed URLs, browser verification, known limitations, and any assets added.
