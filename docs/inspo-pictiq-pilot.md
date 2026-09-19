# Inspo MCP pilot: Pictiq

Date: 2026-09-19

## Purpose

Test whether Inspo can improve reference research for an unusual web product
without flattening its identity into a conventional landing-page template.

The target was the current Pictiq symbol-first landing mode: black-and-white
glyph sequences carry the visible message, while accessible labels preserve a
text interpretation for assistive technology. The existing composition and
icon geometry were treated as constraints, not material for a redesign.

## Method

The pilot used Inspo MCP v0.1.16 in its `lite` profile. Two routes were compared:

1. a general recommendation from a product brief;
2. targeted screen searches followed by inspection of individual references.

Lazyweb provided an independent reference search against the same product
direction. The rendered Pictiq page was checked locally and against the current
page open in Comet.

## Findings

The general recommendation was a poor fit. It selected a marquee hero and
agency/SaaS examples, inferred a dark presentation, and prioritized familiar
landing-page conventions over Pictiq's visual-language model.

Targeted searches were useful. Searches for `type specimen`, `glyph system`,
and `ecosystem index` surfaced references whose transferable patterns were:

- glyphs as primary content rather than decoration;
- strong scale changes between symbol sequences and supporting controls;
- predictable index rhythm for browsing a lexicon;
- restrained spatial grouping that preserves a black-and-white identity.

The independent Lazyweb selection supported the same direction. Its retained
[Pictiq reference set](https://www.lazyweb.com/agentic-search/e501cb06-8594-4ae8-ac04-8f19931516d8)
contains three bounded composition references.

## Decision

Keep Inspo as an optional external companion. For distinctive products such as
Pictiq, skip generic recommendations and search for a precise screen type or
visual system. Inspect each source, transfer only the relevant composition
principle, and preserve the project's own symbols, palette, type, and behavior.

Do not create a dedicated ABVX skill yet. Revisit that decision after two more
real UI pilots show a repeatable query, selection, and rejection workflow.

No Pictiq production files were changed by this research pilot.
