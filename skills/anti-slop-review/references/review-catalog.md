# Anti-Slop Review Catalog

This is an on-demand diagnostic catalog, not a ban list. Read it only when the compact skill cannot resolve a suspected repeated pattern.

## Functional and resilience failures

- Content must remain visible if entrance animation, hydration, IntersectionObserver, or a scroll timeline fails.
- A static readable fallback is preferable to motion that can strand content at opacity zero.
- Verify text and controls near `clip-path`, masks, notches, fixed heights, sticky layers, and `overflow: hidden` at the failing viewport.
- Comparison columns should preserve shared row alignment even when titles, descriptions, prices, or feature counts differ.
- Every control that looks interactive must respond to pointer and keyboard input and expose a visible state change.
- Test long labels, localization-like expansion, missing data, loading, empty, disabled, and error states.
- Keep text and controls clear of viewport/container edges with deliberate gutters.
- Verify intended centering mathematically and optically, especially inside SVGs and irregular shapes.
- Contrast and focus visibility are functional requirements, not palette preferences.
- Motion must respect reduced motion and must not be the only carrier of state or meaning.

## Coherence questions

- What is the primary user task, and does the first viewport make it obvious?
- Do palette, typography, iconography, geometry, spacing, shadows, and motion belong to one system?
- Are different information roles distinguishable, or does every label/card/button receive the same treatment?
- Does the page maintain its visual language after the hero?
- Is the product shown through real behavior and specific data rather than a decorative generic mockup?
- Does brand expression support the workflow or compete with it?
- Are asymmetry, empty space, density, and motion deliberate rather than accidental?
- Are logos, testimonials, customer names, and metrics genuine and authorized?

## Template-risk families

Scrutinize, but do not automatically reject:

- eyebrow, headline, subline, and two-CTA hero stacks;
- text-left and decorative-panel-right split heroes;
- three identical feature cards with icons in tinted rounded tiles;
- category/status text wrapped in pills everywhere;
- blue-purple or pastel gradients used without a product-specific palette reason;
- background glow, floating cards, hover lift, faux glass, or graph-paper grids used as atmosphere by default;
- generic macOS/code windows with traffic-light dots and invented product content;
- Free/Pro/Enterprise pricing cards with a highlighted middle tier;
- testimonial cards with invented avatars, titles, or performance metrics;
- full-width pre-footer CTA slabs;
- default fill-primary plus outline-secondary button pairs;
- repetitive small-label-over-large-heading section openings;
- decorative hairlines, accent bars, and mono uppercase labels used to make plain hierarchy look designed;
- one trendy display font and one neutral sans selected by category stereotype;
- default card shadows, glow borders, and translate-up hover behavior;
- a full page assembled as hero, feature cards, tabs, pricing, FAQ, CTA, and multi-column footer without a product-specific composition.

The issue is not the component itself. The issue is an unexamined combination that could be moved unchanged to an unrelated product.

## Context-sensitive exceptions

- Pills are valid for compact status, filters, segmented choices, or a design-system primitive.
- Cards are valid when they express real grouping and comparison.
- A split hero is valid when the second column demonstrates actual product behavior.
- A grid is valid when it communicates measurements, structure, or a specific technical metaphor.
- Glass and glow are valid when the material, background, contrast, and performance support them.
- Inter or another common typeface is valid as a neutral workhorse; it is weak only when expected to supply identity by itself.
- Familiar pricing or settings layouts may reduce cognitive load and conversion risk.
- Utility-first dashboards may correctly prioritize density, regularity, and established controls over visual novelty.

## Positive correction strategies

- Remove non-functional decoration before adding another visual device.
- Strengthen hierarchy through scale, spacing, grouping, and copy before effects.
- Choose one product-specific visual anchor rather than decorating every section.
- Reuse accessible behavior from existing components while adapting visual treatment to the project system.
- Prefer real product states, real data shapes, and real constraints over illustrative filler.
- Use one coherent palette and interaction language across the reviewed surface.
- Keep motion purposeful, bounded, and visible without requiring an entrance reveal.
- Fix local defects locally unless evidence shows the core visual language is wrong.

## Rejected interpretations

- A named font, gradient, pill, card, serif, icon library, or familiar layout is not a defect by itself.
- “Premium” is not a universal product goal.
- Avoiding every known pattern does not produce a coherent design.
- A comprehensive review does not require reporting every detectable preference.
- The reviewer should not promise point-by-point compliance with a long taste document before seeing the product context.
