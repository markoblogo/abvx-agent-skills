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
  skill-evolution/
```

## Current Status

Scaffolding only. The repo now has a place for benchmark artifacts, but no published ABVX benchmark matrix should be treated as canonical until the fixtures and reports land beside it.

The initial bounded skill-evolution pilot is defined in [`skill-evolution/manifest.json`](skill-evolution/manifest.json). It is manual-pilot only: no skill edits are applied or published without evidence, validation, and explicit maintainer acceptance.

For SkillOpt-style evolution, candidate generation should be diversity-first: create several bounded edit proposals, discard duplicates or guardrail-weakening ideas, then validate only the proposals worth testing. Do not use model-stated probabilities as benchmark scores.

The next researcher-loop structure is `source -> mechanism -> proposal -> novelty_check -> validation -> pr_ready`. Keep it manual until source registries, accepted/rejected ledgers, activation cases, and a skill health gate exist in this directory.
