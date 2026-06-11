#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import date
from fnmatch import fnmatch
from pathlib import Path

import yaml


@dataclass
class Finding:
    skill: str
    rule_id: str
    severity: str
    path: str
    start_line: int
    end_line: int
    message: str

    @property
    def fingerprint(self) -> str:
        return f"{self.rule_id}:{self.path}:{self.start_line}:{self.end_line}"


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def include_path(path: str, include: list[str], exclude: list[str]) -> bool:
    if include and not any(fnmatch(path, pattern) for pattern in include):
        return False
    if any(fnmatch(path, pattern) for pattern in exclude):
        return False
    return True


def suppression_matches(finding: Finding, suppressions: list[dict]) -> bool:
    for item in suppressions:
        rule_id = item.get("rule_id", "*")
        path = item.get("path", "*")
        if fnmatch(finding.rule_id, rule_id) and fnmatch(finding.path, path):
            return True
    return False


def baseline_matches(finding: Finding, baseline_fingerprints: set[str]) -> bool:
    return finding.fingerprint in baseline_fingerprints


def load_baseline(path: Path | None) -> tuple[set[str], list[str]]:
    if path is None or not path.is_file():
        return set(), []

    data = load_json(path)
    fingerprints: set[str] = set()
    expired: list[str] = []
    today = date.today()

    for item in data.get("findings", []):
        fp = item.get("fingerprint")
        if fp:
            fingerprints.add(fp)
        expires_on = item.get("expires_on")
        if expires_on and date.fromisoformat(expires_on) < today:
            expired.append(fp or "<missing fingerprint>")

    return fingerprints, expired


def iter_findings(reports_dir: Path) -> tuple[list[Finding], dict[str, int]]:
    findings: list[Finding] = []
    max_scores: dict[str, int] = {}

    for report_path in sorted(reports_dir.glob("*.json")):
        data = load_json(report_path)
        skill = report_path.stem
        risk = data.get("risk_assessment", {})
        max_scores[skill] = int(risk.get("score", 0))

        for issue in data.get("issues", []):
            location = issue.get("location", {}) or {}
            rel_file = str(location.get("file") or issue.get("file") or "").lstrip("./")
            repo_path = f"skills/{skill}/{rel_file}" if rel_file else f"skills/{skill}/SKILL.md"
            findings.append(
                Finding(
                    skill=skill,
                    rule_id=str(issue.get("rule_id") or issue.get("id") or "UNKNOWN"),
                    severity=str(issue.get("severity", "LOW")).upper(),
                    path=repo_path,
                    start_line=int(location.get("start_line") or issue.get("start_line", 1) or 1),
                    end_line=int(
                        location.get("end_line")
                        or issue.get("end_line")
                        or location.get("start_line")
                        or issue.get("start_line", 1)
                        or 1
                    ),
                    message=str(issue.get("message") or issue.get("finding") or ""),
                )
            )

    return findings, max_scores


def severity_rank(value: str) -> int:
    order = {"LOW": 1, "MEDIUM": 2, "HIGH": 3, "CRITICAL": 4}
    return order.get(value.upper(), 0)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reports-dir", type=Path, required=True)
    parser.add_argument("--policy", type=Path, required=True)
    parser.add_argument("--baseline", type=Path)
    args = parser.parse_args()

    policy = load_yaml(args.policy)
    thresholds = policy.get("thresholds", {})
    paths = policy.get("paths", {})
    suppressions = policy.get("suppressions", [])

    include = list(paths.get("include", []))
    exclude = list(paths.get("exclude", []))
    fail_on = {str(x).upper() for x in thresholds.get("fail_on_severity", ["HIGH", "CRITICAL"])}
    max_risk_score = int(thresholds.get("max_risk_score", 50))

    baseline_fingerprints, expired = load_baseline(args.baseline)
    findings, scores = iter_findings(args.reports_dir)

    considered: list[Finding] = []
    suppressed: list[Finding] = []
    baseline_hits: list[Finding] = []
    blocking: list[Finding] = []

    for finding in findings:
        if not include_path(finding.path, include, exclude):
            continue
        considered.append(finding)

        if suppression_matches(finding, suppressions):
            suppressed.append(finding)
            continue

        if baseline_matches(finding, baseline_fingerprints):
            baseline_hits.append(finding)
            continue

        if finding.severity in fail_on:
            blocking.append(finding)

    score_blockers = [f"{skill}: score {score}" for skill, score in scores.items() if score > max_risk_score]

    print(f"Reports: {args.reports_dir}")
    print(f"Findings: total={len(findings)} considered={len(considered)}")
    print(f"Suppressed: {len(suppressed)}")
    print(f"Baseline matches: {len(baseline_hits)}")
    print(f"Blocking findings: {len(blocking)}")
    print(f"Score blockers: {len(score_blockers)}")

    for item in expired:
        print(f"Expired baseline entry: {item}")

    for item in score_blockers:
        print(f"Risk blocker: {item}")

    for finding in sorted(blocking, key=lambda f: (f.skill, -severity_rank(f.severity), f.path, f.start_line)):
        print(
            f"Blocking: {finding.skill} {finding.severity} {finding.rule_id} "
            f"{finding.path}:{finding.start_line} {finding.message}"
        )

    if expired or score_blockers or blocking:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
