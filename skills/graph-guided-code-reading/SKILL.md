---
name: graph-guided-code-reading
description: Reduce repository-reading token waste by navigating code through symbols, entrypoints, dependencies, changed files, and blast radius instead of broad whole-tree or whole-file reading. Use on medium-to-large repos, PR reviews, architecture questions, onboarding, debugging across modules, or long-running audits.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Graph Guided Code Reading

Save tokens by reading the codebase as a dependency graph, not as a pile of files.

## Core Principle

Most repo-reading waste comes from opening too many files too early. Build a small relevance graph first, then read only the nodes that matter.

## Minimal Relevance Graph

For each task, identify only:

- the user-visible entrypoint or changed surface;
- the owning module or service;
- the direct dependencies and dependents that shape behavior;
- the nearest tests, config, or contracts that constrain the change.

Stop expanding once the next action is clear.

## Reading Workflow

1. Start from the highest-signal anchor:
   - changed files;
   - failing test;
   - route, command, job, or entry function;
   - exact symbol or error text.
2. Build a compact focus set:
   - entrypoint;
   - implementation module;
   - adjacent callers/callees or imports;
   - validating tests.
3. Read narrow slices around the relevant symbols first.
4. Expand one edge at a time only if the current node does not answer the question.
5. Maintain a short checked-location ledger so files are not reopened without a reason.

## Preferred Tools

- If a repo graph, repomap, AST, or change-impact tool exists, use it first.
- If not, emulate graph reading with:
  - `rg` for symbol ownership;
  - `git diff --name-only` or failing-test paths for anchors;
  - imports, call sites, and config references for edges;
  - nearby tests for behavior contracts.

## Task Patterns

### PR Review

- Start with changed files and public interfaces.
- Trace immediate blast radius: callers, consumers, schemas, tests.
- Review the impact set before reading unrelated modules.

### Debugging

- Start from the failing surface and walk inward.
- Prefer one causal path over opening every suspected file.
- Keep hypotheses tied to specific nodes in the focus set.

### Architecture Questions

- Start from entrypoints and major seams, not internal helpers.
- Build a compact service/module map before diving into implementation details.

### Long Audits

- Partition the codebase into focused subgraphs.
- Finish one subgraph with evidence before opening the next.

## Guardrails

- Do not force graph formalism on tiny repos where two files answer the question.
- Do not skip critical config, generated interfaces, or migration boundaries when they affect behavior.
- Do not keep expanding the graph after the winning path is already clear.

## Final Report

Include the focus set, the decisive nodes, what was not read, and any remaining uncertainty at the edges.
