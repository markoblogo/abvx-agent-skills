---
name: book-to-skill
description: Convert books, papers, long documents, or prior reading notes into compact reusable agent skills. Use when the user provides a PDF, EPUB, DOCX, HTML, Markdown, text file, article bundle, or structured notes and wants reusable workflows, mental models, frameworks, checklists, anti-patterns, or a public/private SKILL.md artifact rather than a summary.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Book To Skill

Turn written knowledge into an actionable skill. Extract reusable structure, not a book report.

## Conversion Gate

Before generating files, decide whether the source deserves a skill:

- method density: frameworks, procedures, patterns, checklists, or decision rules;
- actionability: future work can be guided by "use X when Y";
- navigation value: sections can become references or trigger rules;
- extraction quality: text is legible enough to avoid invented structure;
- rights and privacy: no large raw excerpts, private data, or copyrighted chapter dumps.

If the source is mostly narrative, confidential, low quality OCR, or thin on reusable method, produce an extraction report or notes instead.

If the user wants the source document to become model memory or a generated adapter rather than a reusable instruction artifact, switch to `doc-to-lora-evaluator` before proposing any Doc-to-LoRA, RAG, or fine-tuning workflow.

## Modes

- Analyze only: extract frameworks, concepts, terms, and candidate workflows for review.
- Generate skill: create `SKILL.md`, optional references, and a short skill card from approved analysis.
- Refine existing skill: compare a current skill against the source and propose scoped improvements.

## Workflow

1. Validate the input path or URL and identify format, size, author/title if available, and likely extraction risk.
2. Extract text with the repo's available tooling. Prefer structured extractors for technical sources; use plain text extraction for prose.
3. Estimate scope before heavy work: source length, expected references, and whether generation should be split into sections.
4. Build a structure map: table of contents, named frameworks, repeated principles, examples, anti-patterns, and vocabulary.
5. Select the skill boundary. A good skill should have one clear job. Split broad sources into multiple skills only when trigger rules differ.
6. Write concise trigger-rich frontmatter. Keep always-loaded text small.
7. Put detailed examples, chapter notes, or long checklists in `references/` and load them only when needed.
8. Preserve precise names for frameworks, but paraphrase explanations and avoid long verbatim excerpts.
9. Add risk gates: copyright, privacy, domain accuracy, outdated claims, and source uncertainty.
10. Validate the resulting skill against the target repo's standard.

## Output Shape

Minimum public artifact:

```text
skills/<name>/
  SKILL.md
  SKILL_CARD.md
  agents/openai.yaml
```

Use optional `references/` only when the skill needs deeper reusable material.

## Final Report

Report:

- source and extraction method;
- generated skill path;
- what was intentionally omitted;
- validation run;
- copyright/privacy assumptions and residual risk.
