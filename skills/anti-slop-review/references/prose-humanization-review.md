# Prose Humanization Review

Use this reference for public prose, README copy, tool pages, launch notes, guides, partner-facing drafts, and in-product explanatory text that sounds generic or AI-generated.

This is not an AI-detector evasion checklist. The goal is truthful, natural, source-faithful prose.

## Modes

- `detect`: identify named prose patterns with quoted evidence and a short fix; do not rewrite and do not claim AI authorship.
- `edit`: make the smallest useful rewrite, preserve voice and facts, then run the post-edit eval.

## Contract

- Preserve facts, names, dates, citations, metrics, links, and claim boundaries.
- Do not add specificity unless the source or user supplied it.
- Prefer plain, direct wording over “human-like” performance.
- Match an approved voice sample when available; otherwise use the project register.
- Keep the smallest useful rewrite span.
- Run a second pass for remaining AI tells and accidental fact drift.

## Common AI-Writing Tells

- Inflated importance: `pivotal`, `transformative`, `testament`, `landscape`, `revolutionary`.
- Promotional scenery: `nestled`, `breathtaking`, `vibrant`, `seamlessly blends`, `rich tapestry`.
- Vague authority: `experts say`, `users love`, `industry leaders`, `widely recognized` without source.
- Formulaic contrast: `not just X, but Y`, `more than just`, `at its core`, `what truly sets it apart`.
- Rule of three where two or four items would be natural.
- Chatbot residue: `I hope this helps`, `let me know`, `here's what you need to know`, `let's dive in`.
- Generic closers: `the future looks bright`, `marks a new chapter`, `only time will tell`.
- Formatting tells: excessive bold, title-case microheadings, repeated em dashes, inline label prose.
- Diff-anchored writing: `we added`, `this update introduces`, when public copy should describe current behavior.
- Fake-candid rhythm: `Honestly?`, `The truth is`, `Here's the thing` without a real authorial reason.

## Rewrite Moves

- Replace inflated framing with the concrete fact.
- Replace vague authority with a named source or remove the claim.
- Replace “not just X but Y” with one direct sentence.
- Replace promotional adjectives with observable details.
- Repeat the clearest noun instead of cycling synonyms.
- Use headings to label sections; do not repeat the heading as inline prose.
- For product/docs copy, describe current behavior rather than implementation history.
- Preserve quirks from a voice sample when they are intentional and readable.

## Finding Format

```text
ID: AS-001
Type: PROSE_TELL
Severity: high | medium | low
Evidence: file:line or quoted short span
Impact: why trust, clarity, source fidelity, or voice is weakened
Smallest correction: bounded rewrite or edit instruction
Verification: no new facts, voice/register preserved, source boundary intact
```

## Short Rewrite Format

```text
Boundary preserved: no new facts / no new dates / no new claims
Before: ...
After: ...
Second-pass check: no leftover AI tells; no fact drift found
```

## Post-Edit Eval

Answer each check implicitly before returning an edited draft:

- same point, no invented specifics;
- same writer or project register, not flattened into generic polish;
- strong lines preserved where they were already working;
- inflated framing and vague authority removed or sourced;
- no obvious leftover rhetorical setup or recap filler;
- formatting cleaned without turning the piece into sterile prose;
- final read still sounds natural aloud.

## Non-Goals

- no detector gaming;
- no invisible Unicode or fingerprint tricks;
- no laundering unsupported claims into confident prose;
- no global style flattening;
- no rewriting legal, methodology, pricing, safety, or market-data claims without source review.
