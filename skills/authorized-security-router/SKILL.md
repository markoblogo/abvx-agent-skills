---
name: authorized-security-router
description: Route authorized defensive security and reverse-analysis tasks by scope, target type, user intent, and available toolchain before taking action. Use for APK review, static binary triage, frontend JavaScript security review, firmware inventory, malware/YARA analysis, API/LLM/supply-chain audit, security report planning, or security issues that need evidence-led classification without offensive exploitation.
license: MIT
metadata:
  abvx_status: experimental
  abvx_origin: adapted
---

# Authorized Security Router

Route security work before acting. This skill is for authorized defensive analysis, triage, and reporting. It is not an exploitation, evasion, credential, persistence, phishing, or C2 playbook.

## Scope Gate

Before selecting a route, establish:

- authorization: own system, internal review, client-approved scope, CTF/lab, or inspect-only public repository/artifact review;
- target boundary: repository, app, package, binary, API, URL, firmware image, sample hash, or document set;
- action level: inspect-only, local static analysis, local sandbox analysis, browser verification, report-only, or remediation planning;
- prohibited actions: no unauthorized access, no destructive testing, no live exploitation, no credential extraction, no persistence, no evasion, no phishing, no C2, no scope expansion.

Public review means inspect-only review of public repositories or static artifacts. It does not authorize interacting with public URLs, third-party apps, production APIs, login flows, or browser-driven security testing. URL, app, API, and browser-facing security routes require own-system, client-approved, internal, or lab/CTF authorization.

If scope is unclear or the request asks for offensive execution, stop and ask for a safer authorized framing.

## Allowed Routes

Use the smallest defensive route that fits the task:

| Target / intent | Route | Pair with |
|---|---|---|
| APK or mobile app review | Manifest, permissions, redacted secret indicators, network endpoints, package metadata, static call-chain notes | `evidence-ledger-research` |
| Static binary triage | File metadata, strings, imports, symbols, packer indicators, suspicious capability inventory | `evidence-ledger-research` |
| Frontend JS security review | Source maps, bundled endpoints, dangerous DOM sinks, token handling, request signing logic, redacted secret indicators | `browser-verification`, `web-quality-audit` |
| Firmware or IoT inventory | Filesystem layout, services, redacted credential indicators, exposed configs, SBOM hints, update mechanism notes | `evidence-ledger-research` |
| Malware or suspicious sample triage | Hashes, strings, YARA/Sigma candidate indicators, behavior hypotheses, sandbox-safe report plan | `evidence-ledger-research` |
| API or GraphQL audit | Auth boundaries, object-level access checks, token handling, schema exposure, unsafe defaults | `web-quality-audit` when browser-facing |
| LLM or agent security review | Prompt injection surface, tool permission boundaries, data exfil paths, memory poisoning risks | `agents-best-practices` |
| Supply chain audit | SBOM, dependency risk, redacted secret indicators, CI/CD exposure, package provenance, release integrity | `delivery-preflight-gate` |
| Security issue intake | Classify severity, affected surface, evidence needed, next actor, and remediation owner | `repo-issue-triage` |

## Secret Handling

If analysis finds keys, tokens, passwords, cookies, private URLs, or hardcoded credentials:

- do not reproduce full values in comments, reports, logs, issue bodies, or PR reviews;
- report only the secret type, evidence location, and at most a short fingerprint or redacted prefix/suffix;
- use an approved private secret-handling channel only when the user explicitly provides one;
- recommend rotation or revocation when exposure is plausible.

## Blocked Routes

Do not provide operational instructions for:

- exploit development or weaponization;
- EDR/AV bypass, stealth, anti-forensics, or evasion;
- credential extraction, password cracking against real targets, token theft, or session hijacking;
- persistence, lateral movement, C2, phishing, social engineering, or initial access;
- WAF bypass, live brute force, live vulnerability exploitation, or unauthorized scanning;
- modifying APKs/binaries to bypass protections or licensing;
- malware deployment, loader building, or payload delivery.

For blocked requests, offer a defensive alternative: detection logic, hardening checklist, secure code review, incident-response triage, or lab-only conceptual risk summary.

## Routing Workflow

1. Classify the request across four axes:
   - authorization and scope;
   - target type;
   - user intent;
   - available or acceptable toolchain.
2. Select one allowed route or declare `ROUTE_BLOCKED` / `ROUTE_UNCLEAR`.
3. Define the evidence ledger fields before analysis:
   - artifact;
   - observation;
   - source/path/offset/URL;
   - confidence;
   - risk;
   - next verification.
4. Choose the least invasive analysis level.
5. Produce findings as evidence-backed triage, not exploit steps.
6. End with report shape and remediation or next verification.

## Output Contract

Start with routing:

```text
Route: <allowed route | ROUTE_BLOCKED | ROUTE_UNCLEAR>
Authorization: <missing | own system | internal | client-approved | lab/CTF | inspect-only public artifact>
Target boundary:
Action level:
Blocked actions:
Paired skills:
```

Then provide either:

- a defensive analysis plan with evidence fields and verification steps; or
- a refusal of the unsafe route plus a safe alternative.

## Report Shape

For each finding:

- severity;
- evidence location;
- secret handling: redacted unless an approved private channel exists;
- confidence;
- affected component;
- risk in defensive terms;
- remediation or containment;
- verification.

## Attribution

Adapted from the routing architecture of `zhaoxuya520/reverse-skill`, reduced to an ABVX defensive security router with explicit authorization and blocked-action gates.
