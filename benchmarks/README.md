# Benchmarks

This directory is the starting point for reproducible ABVX skill benchmarks.

The rule for this repo is simple: do not publish precision claims that we cannot reproduce locally or in CI.

## Intended Benchmark Surface

- token-economy skills:
  - tokens consumed before/after
  - command-output size before/after
  - repeated-read reduction
- delivery / workflow skills:
  - number of failed retries avoided
  - number of verification misses caught
  - time-to-first-correct-plan
- simplification / review skills:
  - deletions found
  - dependency reductions proposed
  - diff size after simplification

## Minimum Benchmark Requirements

Before adding a number to README, a card, or a badge:

1. The task fixture must be committed.
2. The command or prompt path must be reproducible.
3. The compared arms must be named explicitly.
4. The metric must be computed from captured artifacts, not memory.
5. The benchmark must state model, host, and run count.

## Suggested Layout

```text
benchmarks/
  README.md
  fixtures/
  runs/
  reports/
```

## Current Status

Scaffolding only. The repo now has a place for benchmark artifacts, but no published ABVX benchmark matrix should be treated as canonical until the fixtures and reports land beside it.
