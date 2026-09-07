# SkillSpector 2.11 reference-resolution review

Reviewed on 2026-09-07 for the v0.14.0 release. Source scan: [CI run 34119256861](https://github.com/markoblogo/abvx-agent-skills/actions/runs/34119256861), skill source commit `40045e343827c87e6f83c021a2bb443a4c040462`.

The workflow previously installed the moving upstream Git head. That run resolved SkillSpector 2.11.0 at `88eedca754c74260dfae4e6d6cfb293a0053c908`. Both security workflows now pin this same audited revision; no scanner downgrade or severity threshold change is involved.

Nine HIGH AE1 findings report "Referenced artifact was not completely inspected". Inspection of the source snippets and reference-resolution ledgers shows generic file types, optional caller-repository inputs, proposed outputs, and slash-separated prose categories. Those references do not name bundled executable payloads. The exceptions below accept this specific static-analysis limitation; they do not claim complete analysis of arbitrary future caller inputs.

| Source | Line | Review rationale |
|---|---:|---|
| `skills/agent-learning-layer-triage/SKILL.md` | 81 | Names target artifact types and decision categories for future work; these are not bundled dependencies. |
| `skills/assumption-excavation/SKILL.md` | 17 | Lists document types to review in a caller repository; SKILL.md is a generic input type, not a hidden dependency. |
| `skills/book-to-skill/SKILL.md` | 31 | Describes generating SKILL.md as an output from approved analysis; the proposed output cannot be an existing scan dependency. |
| `skills/delivery-preflight-gate/SKILL.md` | 24 | Lists alternative destinations for a reusable lesson; script/tool and pass/fail are prose categories. |
| `skills/durable-context-maintenance/SKILL.md` | 26 | Lists possible lesson destinations, caller AGENTS.md files, and cleanup risk categories; no uninspected bundled payload is referenced. |
| `skills/goal-loop-designer/SKILL.md` | 57 | Lists possible lesson destinations, host types, and token/tool budgets; these are generic workflow categories. |
| `skills/rabbithole-doc-exploration/SKILL.md` | 17 | Enumerates optional files in the caller repository to inspect when present; they are user inputs, not required bundled artifacts. |
| `skills/skillopt-evolve-skills/SKILL.md` | 15 | Names instruction artifacts to create or edit after layer selection; generic filenames and slash-separated rejection reasons are not bundled dependencies. |
| `skills/skillopt-evolve-skills/SKILL.md` | 19 | Names instruction artifacts to create or edit after layer selection; generic filenames and slash-separated rejection reasons are not bundled dependencies. |

## Enforcement

Each exception in `.abvx/skillspector-baseline.json` matches the exact rule, source path, line range, and full-file SHA-256 and expires on 2026-10-07. A source edit or missing file invalidates its content-bound exception. New AE1 locations and other HIGH/CRITICAL findings remain blocking. Regression coverage checks that changing or removing the reviewed file stops the exception from matching.

Revisit these findings when upgrading the scanner or editing the affected skills. Review the source again before updating a hash or extending an expiry. Existing baseline entries retain their prior semantics. The gate also fails when the report directory is missing or contains no JSON reports; an empty scan cannot produce a passing result.
