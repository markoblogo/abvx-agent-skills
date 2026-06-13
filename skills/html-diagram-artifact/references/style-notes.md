# Style Notes

- Deliver one standalone HTML file with no build step.
- Prefer semantic HTML, inline CSS variables, and minimal inline JS.
- Include dark mode with:
  - theme variables on `:root`;
  - `html.dark` overrides;
  - a small toggle button;
  - `localStorage` persistence;
  - an apply-before-paint script in `<head>`.
- Use SVG as the main stage for diagrams.
- Style SVG via CSS classes and variables, not hard-coded colors.
- Keep the palette restrained: background, surface, ink, muted, one accent family.
- Use prose sparingly. The diagram should explain faster than a paragraph.
- Add interaction only when it clarifies sequence or scope.
- Keep mobile legible: avoid microscopic labels and overflow.
