---
name: anti-slop-review
description: Review an implemented product UI or public prose surface for hard visual defects, design-system incoherence, repeated template patterns, and AI-writing tells without treating subjective taste as universal law. Use for pre-ship screenshots, browser review, README/tool-page copy, launch notes, guide prose, or redesigns that may be generic, clipped, inaccessible, visually inconsistent, overbuilt from familiar AI-generated patterns, or inflated by AI-ish language.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
  abvx_eval_tier: fixture_checked
---

# Anti-Slop Review

Review evidence, not vibes. This skill critiques an implemented interface; it does not replace the brief, design system, accessibility checks, or product requirements.

Use `frontend-taste-layer` while choosing a visual direction. Use this skill after implementation or on screenshots/live UI. Use `design-critique-polish` for broader polish and `web-quality-audit` for full accessibility, performance, privacy, and security coverage.

For prose-only work, use the prose pass below and skip browser-specific checks unless the text is already placed in a live UI.

For prose requests, choose one mode up front:

- `detect`: identify named prose patterns with quoted evidence and bounded fixes; do not rewrite the draft;
- `edit`: make the smallest useful rewrite, then run the post-edit eval before returning it.

## Authority

Default authority is `read` and `proposal`. Inspect files, screenshots, and browser behavior; report findings. Change code only when the user asked to fix or polish the interface. Do not add dependencies, replace a design system, license fonts/assets, or invent brand/customer claims without authorization.

## Establish the contract

Before judging style, identify:

- surface and critical user task;
- audience and product/brand register;
- existing tokens, components, and design constraints;
- required breakpoints and input modes;
- references the user explicitly approved.

For dashboards, settings, admin tools, firmware UI, and other utility-first products, clarity and density may correctly outweigh novelty. A familiar pattern is not a defect merely because it is familiar.

## Review hierarchy

Classify every finding as exactly one type.

### HARD_DEFECT

Observable failures that can block shipment:

- content hidden when JavaScript, hydration, scroll observers, or animation fails;
- clipped text or controls near fixed heights, notches, masks, and `overflow: hidden`;
- unreadable contrast, missing focus, broken keyboard path, or ignored reduced motion;
- dead controls, fake interactivity, console errors, or missing loading/error/empty states;
- horizontal overflow, broken responsive layout, unsafe tap targets, or misaligned comparison rows;
- content or controls visibly off-center when centering is part of the design.

Hard defects require reproduced evidence: screenshot, viewport, interaction, console/network observation, or file/line location. Do not infer them from visual preference.

### COHERENCE

System-level problems that weaken comprehension or identity:

- typography, palette, geometry, shadows, iconography, and motion speak different visual languages;
- hierarchy does not reveal the primary task or first action;
- atmosphere ends after the hero and the remaining page becomes unrelated filler;
- decoration competes with workflow or brand expression overwhelms product utility;
- repeated labels, cards, borders, shadows, or motion treatments flatten distinct roles;
- fake examples, placeholder product data, or generic copy make the surface feel ungrounded.

Tie each finding to the brief, existing system, user task, or repeated inconsistency. “I dislike this font” is not evidence.

### TEMPLATE_RISK

Non-blocking signals that the surface may be interchangeable:

- centered hero stack or text-left/panel-right hero used without a product-specific reason;
- repeated icon tiles, tinted chips, card grids, paired fill/outline CTAs, generic pricing/testimonial/FAQ sequences;
- decorative app windows, code windows, glows, grids, glass, gradients, or floating cards that do not communicate real product behavior;
- trendy fonts, palettes, or motion selected by category stereotype rather than the brief;
- the same section skeleton or house style reused across unrelated products;
- avoidance-only design: removing every familiar device without adding a product-specific idea.

These are prompts for scrutiny, not bans. A pattern is acceptable when it serves the task, matches the design system, and is executed coherently.

### DETECTOR_RULE

Deterministic, repeatable checks for visual or prose defects. Use this type when a finding can be detected from code, rendered DOM, CSS, screenshots, or text without relying on taste:

- nested cards or page sections styled as cards;
- long line length, cramped padding, unsafe tap target, skipped heading level, or missing focus state;
- gray text on colored backgrounds with poor contrast;
- repeated layout skeletons across unrelated sections;
- bounce/elastic motion used without a product reason;
- overflow-prone fixed heights, clipped strings, or hidden content paths;
- prose tells matched from an explicit pattern list.

Detector rules are evidence, not automatic verdicts. A rule can be waived when the project design context, brand system, legacy constraint, or explicit owner direction justifies it.
If a deterministic finding also qualifies as a shipment-blocking accessibility, visibility, interaction, or responsive failure, classify it as `HARD_DEFECT`; hard-defect precedence wins over `DETECTOR_RULE`.

### PROSE_TELL

AI-writing patterns that weaken trust, specificity, or project voice:

- inflated significance, generic `pivotal/testament/landscape` framing, or travel-brochure adjectives;
- vague attribution, unsupported experts/users/industry claims, or filler where a source is missing;
- formulaic contrasts such as `not just X, but Y`, rule-of-three lists, fake-candid openings, or chatbot closers;
- repeated em dashes, title-case microheadings, boldface overuse, and inline label prose that makes the text feel templated;
- diff-anchored public writing that describes what changed instead of the current behavior;
- voice drift away from an approved user, brand, or project sample.

Apply the no-fabrication rule: rewrites must not invent facts, names, dates, citations, metrics, customer claims, or source context. If specificity is missing, ask for it or leave a bounded placeholder. Do not optimize for hiding AI origin; optimize for truthful, natural, source-faithful prose.

## Evidence pass

When browser access is available, verify at minimum:

1. primary desktop and mobile viewports;
2. keyboard navigation and visible focus;
3. every control that appears interactive;
4. long copy, missing data, loading, error, and empty states where relevant;
5. reduced motion and a no-animation/no-JS fallback for content visibility;
6. clipping around masks, notches, fixed heights, sticky layers, and section overlaps;
7. alignment of repeated rows, cards, comparison columns, and anchored actions.

Use screenshots at the actual failing viewport. Zoom into suspected clipping or centering problems instead of relying on a normal-scale impression.

## Prose pass

Use this for README sections, tool pages, release notes, public guides, Substack drafts, partner-facing copy, and in-product explanatory text.

1. Choose mode:
   - `detect` when the user asks whether a text sounds AI-generated, generic, inflated, or “sloppy” and wants evidence first;
   - `edit` when the user wants a rewrite, cleanup, polish, or humanization pass.
2. Identify the register: technical, product, guide, editorial, partner-facing, or personal voice.
3. Check source boundaries: which facts, dates, names, claims, and links are allowed.
4. Scan for `PROSE_TELL` patterns and separate real defects from harmless personal style.
5. If a voice sample exists, preserve its rhythm and vocabulary; otherwise keep the rewrite plain and project-specific.
6. In `detect` mode, return named patterns with quoted evidence and a short bounded fix; do not rewrite or guess whether AI wrote it.
7. In `edit` mode, rewrite only the smallest useful span, then run a second pass for leftover AI tells and accidental fact drift.

Return prose findings using the normal `AS-###` format with `Type: PROSE_TELL`. For short direct rewrites, include a compact `Before -> After` block and the no-fabrication boundary you preserved.

## Post-edit eval

Run this only for prose `edit` mode before returning the rewrite.

1. Point preserved: no new claims, examples, names, dates, stats, links, or opinions were added.
2. Voice preserved: the draft still sounds like the same writer or project register, not generic polished filler.
3. Minimum effective edit: strong human lines were left alone; cutting is proportional to the actual problem.
4. Concrete over inflated: puffery, vague authority, and fake significance were replaced with facts or removed.
5. Pattern cleanup: no obvious leftover binary contrast, throat-clearing opener, faux-insight setup, colon-reveal drama, synonym cycling, or generic recap ending remains unless intentionally preserved.
6. Formatting cleanup: bold, bullets, em dashes, and microheadings were not used as decorative residue.
7. Second-pass boundary: no fact drift found; no detector-gaming tactics introduced.

If any item fails, fix the draft before returning it.

## Bounded findings

Return at most seven findings per pass. Use stable IDs `AS-001`, `AS-002`, and so on. Order by `HARD_DEFECT`, then user impact, then leverage.

Each finding contains:

```text
ID: AS-001
Type: HARD_DEFECT | COHERENCE | TEMPLATE_RISK | PROSE_TELL | DETECTOR_RULE
Severity: blocker | high | medium | low
Evidence: screenshot/viewport/interaction/file:line
Impact: concrete user or product consequence
Smallest correction: bounded change
Verification: browser or code check that proves resolution
```

Do not fill seven slots with cosmetic preferences. If there are no actionable findings, return `SHIP_READY_WITHIN_REVIEWED_SCOPE`.

## Fix pass

When authorized to change code:

1. fix hard defects first;
2. preserve product behavior and design-system contracts;
3. make the smallest coherent correction rather than reskinning the whole page;
4. do not add a dependency for one decorative effect;
5. rerun the exact evidence pass at affected viewports;
6. report unresolved findings and deliberate exceptions.

A style exception is valid when it follows explicit user direction or a documented design-system decision. Record the reason; do not repeatedly reopen it.

## On-demand reference

Read `references/review-catalog.md` only when a suspected template pattern is ambiguous, the user requests a comprehensive anti-slop pass, or repeated reviews keep producing the same surface-level result.

Read `references/prose-humanization-review.md` only when prose is the main surface, the user asks to humanize/polish text, public copy sounds AI-generated, or a rewrite risks changing factual claims or project voice.

A local installation may also contain `references/slop-source.local.md`, the full user-supplied source. Load it only on explicit request or when the compact catalog cannot resolve a disputed pattern. It is not a point-by-point shipping checklist.

## Verdict

- `SHIP_BLOCKED`: at least one unresolved hard defect blocks the reviewed path;
- `REVISE`: no blocker, but high-impact coherence, prose, or detector-rule work remains;
- `SHIP_READY_WITHIN_REVIEWED_SCOPE`: no actionable blocker or high-impact finding;
- `INSUFFICIENT_EVIDENCE`: the surface, states, or viewport evidence cannot support a verdict.

## Attribution

Adapted from a user-supplied anti-slop design law with no supplied provenance or redistribution license. The original is not distributed in this repository. This contract retains only general review ideas and rewrites them as evidence-based, context-sensitive ABVX guidance.

The prose pass is a compact local adaptation of public AI-writing cleanup patterns, including `blader/humanizer`, with a stricter ABVX no-fabrication and source-boundary rule. It is not an AI-detection or evasion tool.
