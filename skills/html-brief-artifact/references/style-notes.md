# Style Notes

- Deliver one standalone HTML file with no build step.
- Prefer semantic HTML and a document-first layout.
- Include dark mode with:
  - theme variables on `:root`;
  - `html.dark` overrides;
  - a small toggle button;
  - `localStorage` persistence;
  - an apply-before-paint script in `<head>`.
- Keep the palette restrained and readable.
- Use a clear hierarchy: title, framing line, section headers, supporting blocks.
- Use summary strips, timelines, callouts, and checklists only when they aid scanning.
- Keep the writing close to the source intent.
- Make the page easy to review on laptop and mobile widths.
