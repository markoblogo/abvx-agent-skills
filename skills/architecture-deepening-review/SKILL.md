---
name: architecture-deepening-review
description: "Review a codebase for architecture deepening opportunities: shallow modules, weak seams, scattered domain logic, low testability, high coupling, and AI-navigability friction. Use when the user asks for architecture improvement, refactoring opportunities, modularity, test seams, or maintainability review."
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Architecture Deepening Review

Find refactors that increase leverage and locality. A deeper module hides meaningful behavior behind a smaller, clearer interface.

## Vocabulary

- Module: code with an interface and implementation.
- Interface: everything callers must know, including types, invariants, errors, ordering, config, and side effects.
- Seam: place where behavior can vary without editing callers.
- Adapter: concrete implementation behind a seam.
- Depth: useful behavior hidden behind a small interface.
- Locality: related behavior and knowledge concentrated in one place.

## Review Workflow

1. Read the nearest README, architecture docs, domain glossary, ADRs, and tests when present.
2. Map the user-facing or domain workflow before judging structure.
3. Look for friction:
   - understanding one concept requires bouncing across many files;
   - modules pass through data with little leverage;
   - tests exist only around extracted fragments, not real behavior;
   - domain rules are duplicated across callers;
   - adapters exist in theory but only one implementation exists;
   - hidden coupling crosses package or component boundaries;
   - naming does not match domain language.
4. Apply the deletion test: if removing a module only moves complexity into callers, it may be shallow. If removing it spreads domain complexity everywhere, it is probably earning its keep.
5. Rank candidates by payoff, risk, and confidence.

## Candidate Format

For each candidate:

- files/modules;
- current friction;
- proposed deeper module or seam;
- expected locality and leverage gain;
- testability improvement;
- risks and migration path;
- recommendation strength: strong, worth exploring, or speculative.

Do not implement broad refactors without user confirmation. For implementation, carve one vertical slice and preserve behavior with tests.

## Final Report

End with the top recommendation, the smallest first step, and what evidence would change the recommendation.
