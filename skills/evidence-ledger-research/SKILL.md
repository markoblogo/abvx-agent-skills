---
name: evidence-ledger-research
description: Research and answer evidence-sensitive questions with source, date, unit, and operand discipline. Use for web research, PDF/document QA, policy or finance facts, tables, time series, calculations from retrieved evidence, exact-answer extraction, and any task where wrong source selection, stale facts, nearby table confusion, or formatting errors would matter.
license: MIT
---

# Evidence Ledger Research

Use this skill when the answer must be tied to exact evidence rather than memory or broad summaries.

## Source Discipline

- Prefer primary sources, official data pages, original PDFs, repository files, or provided/oracle documents.
- If a guessed exact-date search fails, broaden to the official series, table name, dataset code, or download page.
- Read only the narrow span needed after locating a promising source, then verify entity, period, basis, unit, and version.
- If a provided document contains the answer, extract from it before searching elsewhere.
- For volatile facts, verify the latest source before answering.

## Evidence Ledger

Maintain a compact ledger for multi-step answers:

```text
Claim/operand:
Source:
Date/period:
Unit/scale:
Role:
Value/span:
Notes:
```

Use the ledger before arithmetic, comparisons, ranking, or final formatting. Do not compute from partial evidence unless the user explicitly accepts an estimate.

## Table And Document Rules

- Match row labels and exact column headers, not visual proximity alone.
- Watch for repeated month rows, fiscal vs calendar sections, continuation tables, estimates, totals, and footnotes.
- For forms and PDFs, locate the exact field/anchor in the question, then read the adjacent filled value from the same row, box, block, or table cell.
- For visual/document QA, prefer the smallest exact text span that answers the question.
- Preserve spelling, punctuation, capitalization, and numeric formatting when exact extraction matters.

## Calculation Rules

- Confirm every operand before calculating.
- Track scale and direction: thousands/millions/billions, currency, exchange-rate orientation, sign, percent vs percentage points.
- Preserve relation direction: "change from A to B" means `B - A`; "share accounted for by X" means `X / total`.
- For time windows, enumerate expected periods first and verify endpoint inclusion.
- Do not round intermediate values unless the source requires it.

## Final Answer

- Match the requested format exactly: option label, numeric value, list, date, or concise phrase.
- Include unit words only when requested or necessary for clarity.
- When citing sources, link the source and summarize the evidence without long quotations.
- Copy the final answer from the checked ledger value, not from an unverified intermediate.
