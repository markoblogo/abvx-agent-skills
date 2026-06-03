---
name: complexity-optimizer
description: Analyze or improve codebase complexity and performance hotspots without broad rewrites. Use when reviewing nested loops, repeated scans, N+1 queries, rendering churn, excessive recomputation, slow tests, large-input paths, memory pressure, or requests to reduce complexity while preserving behavior and tests.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Complexity Optimizer

Optimize only when behavior is understood and can be preserved. A small measured improvement beats a clever rewrite.

## Modes

- Report mode: rank opportunities and do not edit.
- Implementation mode: change scoped code after identifying a repro, test, benchmark, or reviewable invariant.
- Audit mode: scan broad areas, then inspect only the highest-impact leads.

## Workflow

1. Establish scope: language, framework, hot paths, data sizes, tests, build command, and user-facing risk.
2. Find leads: nested scans, repeated filtering, loops inside render paths, N+1 database/API calls, redundant serialization, unbounded recursion, cache misses, and avoidable work in hooks or lifecycle methods.
3. Rank by likely impact and blast radius. Treat static findings as leads, not proof.
4. For each serious finding, record:
   - file and location;
   - current pattern;
   - estimated current complexity;
   - proposed change;
   - expected complexity after change;
   - correctness risk;
   - verification needed.
5. Before editing, preserve behavior with existing tests, a focused regression test, a fixture, or a clear invariant.
6. Optimize conservatively:
   - replace repeated linear lookup with maps or sets when equality is stable;
   - pre-index or group data before joins;
   - batch database/API access while preserving tenant, permission, filtering, ordering, and pagination;
   - memoize derived UI data only when inputs are stable;
   - virtualize or paginate large rendered collections;
   - avoid caches without invalidation strategy.
7. Run narrow checks first, then broader relevant checks.

## Safety Checklist

Before finalizing:

- output ordering is preserved or intentionally changed;
- duplicates and null/missing values are handled;
- mutation and object identity assumptions are not broken;
- authorization and tenant filters survive batching;
- cache invalidation is explicit;
- the original performance or failure signal was rerun.

## Final Report

Include:

- top findings or changed files;
- before/after complexity estimates;
- verification commands and results;
- residual risks and missing measurement gaps.
