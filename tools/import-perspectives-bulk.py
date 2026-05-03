#!/usr/bin/env python3
"""Bulk-import perspectives into an open deliberation from structured plain-text files.

Each input file is one perspective body authored as:

    POSITION: <one-paragraph distilled position, 8-240 chars>

    SCHEMA_SKETCH:
    - <claim>
    - <claim>

    CLI_SURFACE:
    - <claim>

    MIGRATION_PATH:
    - <claim>

    WHAT_NOT:
    - <claim>

    OPEN_QUESTION:
    - <claim>

    RISK:
    - <claim>

    WHAT_LOST:
    - <claim>

The importer:
- submits a `perspective` row (body_md = full file text)
- submits a `perspective-position` row from the POSITION line
- submits one `perspective-claim` per bullet under each typed section

Atom rules are pre-applied per file: claim text is sanitised by replacing `|`
with `/` (T-21 pipe-table refusal) and truncated to 240 chars. Provenance of
the un-sanitised body is preserved by the perspective.body_md.

Authored at S081 (DV-S081-1 deliberation) where 4 perspectives x ~45 claims
required ~190 CLI roundtrips before this script consolidated the work to one.

Usage:
    python3 tools/import-perspectives-bulk.py --deliberation-id N \
        --perspective P-1:anthropic:/path/p1.txt \
        --perspective P-2:openai:/path/p2.txt \
        ...

Each --perspective is "label:family:path" where family is one of
anthropic | openai | google | other-llm | human and label matches the
P-N convention.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Optional

SECTION_KINDS = {
    "SCHEMA_SKETCH": "schema_sketch",
    "CLI_SURFACE": "cli_surface",
    "MIGRATION_PATH": "migration_path",
    "WHAT_NOT": "what_not",
    "OPEN_QUESTION": "open_question",
    "RISK": "risk",
    "WHAT_LOST": "what_lost",
}

REPO_ROOT = Path(__file__).resolve().parent.parent
SELVEDGE_BIN = str(REPO_ROOT / "bin" / "selvedge")


def _sanitise_atom(claim: str) -> str:
    claim = claim.replace("|", "/")
    if len(claim) > 240:
        claim = claim[:237] + "..."
    return claim


def _submit(kind: str, payload: dict) -> dict:
    cmd = [SELVEDGE_BIN, "submit", kind, "--payload", json.dumps(payload)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        sys.stderr.write(f"FAIL submit {kind}: {proc.stderr}\n")
        sys.stderr.write(f"     payload (truncated): {json.dumps(payload)[:300]}\n")
        sys.exit(2)
    return json.loads(proc.stdout)["result"]


def _parse(text: str) -> tuple[Optional[str], dict[str, list[str]]]:
    position: Optional[str] = None
    sections: dict[str, list[str]] = {}
    current: Optional[str] = None
    for line in text.splitlines():
        if line.startswith("POSITION:"):
            position = line[len("POSITION:"):].strip()
            current = None
            continue
        stripped = line.rstrip(":").strip()
        if stripped in SECTION_KINDS:
            current = SECTION_KINDS[stripped]
            sections[current] = []
            continue
        if line.startswith("- ") and current:
            claim = _sanitise_atom(line[2:].strip())
            if 8 <= len(claim) <= 240:
                sections[current].append(claim)
    return position, sections


def main() -> int:
    ap = argparse.ArgumentParser(description="Bulk-import perspectives into an open deliberation.")
    ap.add_argument("--deliberation-id", type=int, required=True,
                    help="deliberation_id from `selvedge submit deliberation-open`.")
    ap.add_argument("--perspective", action="append", required=True, dest="perspectives",
                    metavar="LABEL:FAMILY:PATH",
                    help="One perspective spec. Repeatable. Example: P-1:anthropic:/tmp/p1.txt")
    ap.add_argument("--existing-id", action="append", default=[], dest="existing_ids",
                    metavar="LABEL:PERSPECTIVE_ID:SKIP_CLAIMS",
                    help="Resume an already-partially-submitted perspective. Repeatable.")
    args = ap.parse_args()

    resume_map: dict[str, tuple[int, int]] = {}
    for spec in args.existing_ids:
        label, pid, skip = spec.split(":")
        resume_map[label] = (int(pid), int(skip))

    for spec in args.perspectives:
        label, family, path_str = spec.split(":", 2)
        path = Path(path_str)
        if not path.is_file():
            sys.stderr.write(f"missing file: {path}\n")
            return 2
        text = path.read_text()
        position, sections = _parse(text)
        if not position:
            sys.stderr.write(f"no POSITION line in {path}\n")
            return 2
        if len(position) > 240:
            position = position[:237] + "..."

        if label in resume_map:
            persp_id, skip_n = resume_map[label]
            print(f"  perspective {label} ({family}) → resume id={persp_id} skip={skip_n}")
        else:
            r = _submit("perspective", {
                "deliberation_id": args.deliberation_id,
                "label": label,
                "family": family,
                "body_md": text,
            })
            persp_id = r["perspective_id"]
            print(f"  perspective {label} ({family}) → id={persp_id}")
            _submit("perspective-position", {
                "perspective_id": persp_id,
                "position": position,
            })
            skip_n = 0

        total = 0
        for section_kind, claims in sections.items():
            for claim in claims:
                if skip_n > 0:
                    skip_n -= 1
                    continue
                _submit("perspective-claim", {
                    "perspective_id": persp_id,
                    "claim": claim,
                    "section_kind": section_kind,
                })
                total += 1
        print(f"    -> {total} claim(s) submitted")

    return 0


if __name__ == "__main__":
    sys.exit(main())
