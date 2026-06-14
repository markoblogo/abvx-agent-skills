---
name: spreadsheet-workbook-forensics
description: Edit, repair, or generate spreadsheet workbooks with structure-preserving Python. Use for Excel or spreadsheet tasks involving .xlsx/.xlsm files, formulas, lookup tables, summaries, formatting preservation, target ranges, workbook QA, or any task where cells must be computed, written, and verified rather than guessed from previews.
license: MIT
---

# Spreadsheet Workbook Forensics

Use this skill for workbook edits where preserving structure and verifying target cells matters.

## Workflow

1. Inspect the actual workbook, not only a preview: sheet names, dimensions, merged cells, headers, formulas, named ranges, and nearby examples.
2. Locate source tables and destination ranges by labels, headers, surrounding structure, and requested ranges, not fixed coordinates unless explicitly given.
3. Write a small script with `INPUT_PATH` and `OUTPUT_PATH` constants.
4. Use `openpyxl` for structure-preserving read/write. Use `pandas` only for in-memory transformation, then write back with `openpyxl`.
5. Execute the script.
6. Reopen the saved workbook and verify representative and boundary target cells.

## Workbook Rules

- Preserve unrelated sheets, cells, formulas, formatting, widths, borders, and named ranges.
- Clear only the instructed output range before writing new results.
- Do not insert/delete rows, sort source records, or relocate tables unless explicitly requested.
- Copy style/number format from nearby template rows when adding outputs.
- Delete rows bottom-to-top if deletion is explicitly required.

## Formula And Value Rules

- `openpyxl` does not calculate formulas or update cached formula results.
- If the grader or user needs cell values, compute results in Python and write literal values unless live formulas are explicitly required.
- Load a second workbook with `data_only=True` when existing formulas are inputs:

```python
wb = openpyxl.load_workbook(INPUT_PATH)
wb_values = openpyxl.load_workbook(INPUT_PATH, data_only=True)
```

- Treat existing formulas as semantic specifications: referenced ranges, criteria, lookup keys, and error handling should guide the Python computation.
- Do not leave unevaluated formulas in target cells unless the deliverable explicitly asks for formulas.

## Matching And Normalization

- Normalize text by trimming, collapsing whitespace/NBSPs, and casefolding.
- Normalize numeric-looking IDs consistently: `330`, `330.0`, and `"330"` may be the same key when context says so.
- Parse numbers after removing currency symbols and commas while preserving signs and decimals.
- Normalize dates deliberately across `datetime`, Excel serials, and date-like strings.
- Build explicit single or composite keys for joins, lookups, deduplication, grouping, and interval matches.

## Output Verification

Before finalizing:

- Run the script once and fix syntax/runtime errors.
- Reopen `OUTPUT_PATH`.
- Check first, last, blank-sensitive, no-match, total, and representative target rows.
- Confirm expected target cells contain non-formula literals when values are expected.
- Confirm stale formulas or values were cleared from the target range.
- Avoid quoting large raw workbook contents in the final response if cells may contain sensitive text.
