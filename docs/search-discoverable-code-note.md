# Search-Discoverable Code Note

This repository can borrow one narrow idea from search-first coding guidance:
agent-readable code becomes easier to maintain when names, filenames, and short
comments behave well under plain-text search.

## What to keep

- skill names, exported CLI commands, and generated artifact names should stay
  specific and grep-able;
- repo docs should prefer one concept, one spelling;
- validator and generator code should avoid generic filenames when a
  concept-named module would be clearer;
- critical user-facing errors should remain traceable as literal strings.

## Where it applies here

Best fit:

- catalog generation and validation code;
- package/CLI surfaces;
- generated artifact naming;
- repo docs that define canonical terms.

Lower fit:

- individual skill prose, where pedagogical clarity matters more than naming
  formalism;
- outreach copy and marketing-style summaries.

## Boundary

This is a companion review note, not a new installable skill and not a mandate
to rename stable public skill IDs without a compatibility reason.
