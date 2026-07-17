#!/usr/bin/env python3
"""Classify captured targeted and broader bug-fix evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROUTE_STATES = ("route accepted", "used and confirmed", "unavailable")
REQUIRED_RECORD_FIELDS = ("argv", "command_sha256", "exit_code", "timed_out", "repository")


def load_record(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"expected an object in {path}")
    missing = [field for field in REQUIRED_RECORD_FIELDS if field not in data]
    if missing:
        raise ValueError(f"missing {', '.join(missing)} in {path}")
    return data


def classify(before: dict[str, Any], after: dict[str, Any], broader: list[dict[str, Any]], symptom_match: str) -> tuple[str, str]:
    if before["command_sha256"] != after["command_sha256"] or before["argv"] != after["argv"]:
        return "INCONCLUSIVE", "Before and after did not run the exact same targeted argv."
    if before["timed_out"]:
        return "INCONCLUSIVE", "The before record timed out."
    if before["exit_code"] == 0:
        return "NOT_REPRODUCED", "The proposed reproducer passed before the fix."
    if symptom_match != "confirmed":
        return "INCONCLUSIVE", "The failing before record was not confirmed to match the target symptom."
    if after["timed_out"] or after["exit_code"] != 0:
        return "STILL_FAILING", "The same targeted command still fails after the attempted fix."
    if not broader:
        return "FIX_UNVERIFIED", "The targeted command passes, but no broader check record was captured."
    if any(item["timed_out"] or item["exit_code"] != 0 for item in broader):
        return "FIX_REGRESSION", "The targeted command passes, but a captured broader check fails."
    return "FIX_PROVEN", "The same targeted command changed from failing to passing and all captured broader checks passed."


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("before", type=Path)
    parser.add_argument("after", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--broader", type=Path, action="append", default=[])
    parser.add_argument("--symptom-match", choices=["confirmed", "unconfirmed"], default="unconfirmed")
    parser.add_argument("--route-state", choices=ROUTE_STATES, required=True)
    parser.add_argument("--route-detail", required=True)
    parser.add_argument("--cpat-id")
    parser.add_argument("--limitation", action="append", default=[])
    args = parser.parse_args()

    before = load_record(args.before)
    after = load_record(args.after)
    broader = [load_record(path) for path in args.broader]
    status, reason = classify(before, after, broader, args.symptom_match)
    identity = json.dumps(
        [before["command_sha256"], before["repository"].get("head"), after["repository"].get("head")],
        separators=(",", ":"),
    )
    packet = {
        "schema_version": 1,
        "evidence_id": "BUGE-" + hashlib.sha256(identity.encode()).hexdigest()[:12].upper(),
        "repository": before["repository"].get("root"),
        "git_before": before["repository"].get("head"),
        "git_after": after["repository"].get("head"),
        "targeted_before": before,
        "targeted_after": after,
        "broader_checks": broader,
        "symptom_match": args.symptom_match,
        "route_evidence": {"state": args.route_state, "detail": args.route_detail},
        "classification": {"status": status, "reason": reason},
        "limitations": args.limitation,
        "cpat_id": args.cpat_id,
    }
    output = args.output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(f"{status}: {reason} -> {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
