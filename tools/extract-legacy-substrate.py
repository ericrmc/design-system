#!/usr/bin/env python3
"""L4B legacy-substrate extractor (DV-S081-1, OI-S081-5, S186).

One-shot inventory tool. Scans markdown evidence that survived the S180
substrate wipe and produces ``provenance/legacy-substrate-summary.md``
cataloguing what is recoverable as text vs what is genuinely lost.

Pivoted scope. The OI-S081-5 spec originally framed this as "extract from
pre-S180 substrate backup files". Discovery at S186-open: no pre-S180
binary substrate backups survive anywhere — ``state/selvedge.sqlite`` is
gitignored, ``state/selvedge.sqlite.pre-migrate-backup`` is an empty
post-S180-init artefact, and only S185-era L3 snapshots exist on disk.
The extractor therefore inventories the markdown evidence that does
survive, since that is the only signal future readers will have for the
pre-S180 sessions.

Sources scanned:
- ``provenance/`` — per-session export directories. The S080–S084 range
  contains both pre-S180-original and post-S180-recovery directories;
  the inventory flags both branches with their slug.
- ``archive/pre-restart/`` — engine-history + retired specifications +
  retired tools from the pre-S076 trim-and-restart.
- ``archive/v7-trial-2026-04-24-disaster-response/`` — disaster-recovery
  pilot artefacts.

Output sections:
- preamble: scope, what is lost, what is recovered
- per-directory inventory: session-no, slug, files present, alias counts
- alias index: DV-/OI-/EF-/FR- mentions across all directories
- summary: counts + pointers

Run: ``uv run tools/extract-legacy-substrate.py`` from workspace root.
"""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

WORKSPACE = Path(__file__).resolve().parents[1]

ALIAS_RE = re.compile(
    r"\b("
    r"DV-S\d+-\d+"
    r"|D-S\d+-\d+"
    r"|EF-S\d+-\d+"
    r"|FR-S\d+-\d+"
    r"|OI-(?:S\d+-\d+|\d+(?:-\d+)?)"
    r"|SPEC-[A-Za-z0-9_\-]+-v\d+"
    r"|A-\d{3}"
    r")\b"
)

SESSION_DIR_RE = re.compile(r"^(\d{3})-(.+)$")

PROVENANCE_FILES = [
    "00-assessment.md",
    "01-deliberation.md",
    "02-decisions.md",
    "03-close.md",
    "04-review.md",
]


def _scan_dir(d: Path) -> Tuple[Counter, List[str]]:
    """Return (alias-frequency-counter, file-list) for a session dir."""
    counter: Counter = Counter()
    files_present: List[str] = []
    for fname in PROVENANCE_FILES:
        f = d / fname
        if not f.exists():
            continue
        files_present.append(fname)
        try:
            text = f.read_text(errors="replace")
        except OSError:
            continue
        counter.update(ALIAS_RE.findall(text))
    perspectives = d / "perspectives"
    if perspectives.exists() and perspectives.is_dir():
        files_present.append("perspectives/")
        for pf in perspectives.glob("*.md"):
            try:
                counter.update(ALIAS_RE.findall(pf.read_text(errors="replace")))
            except OSError:
                continue
    return counter, files_present


def _provenance_inventory() -> List[Dict]:
    """Return one row per provenance/ session directory, sorted by session_no
    then slug. Doublet sessions (e.g. 081-deliberator-flow-exercise +
    081-substrate-loss-defense-design) emit two rows."""
    root = WORKSPACE / "provenance"
    rows: List[Dict] = []
    for d in sorted(root.iterdir()):
        if not d.is_dir():
            continue
        m = SESSION_DIR_RE.match(d.name)
        if not m:
            continue
        sess_no = int(m.group(1))
        slug = m.group(2)
        counter, files = _scan_dir(d)
        rows.append({
            "session_no": sess_no,
            "slug": slug,
            "dir": d.name,
            "files": files,
            "alias_count": sum(counter.values()),
            "alias_freq": counter,
        })
    rows.sort(key=lambda r: (r["session_no"], r["slug"]))
    return rows


def _detect_doublets(rows: List[Dict]) -> List[Tuple[int, List[str]]]:
    """Group dirs by session_no; return only those with >1 dir (S180-wipe
    recovery doublets)."""
    by_sess: Dict[int, List[str]] = defaultdict(list)
    for r in rows:
        by_sess[r["session_no"]].append(r["dir"])
    return [(s, dirs) for s, dirs in sorted(by_sess.items()) if len(dirs) > 1]


def _archive_inventory() -> Dict:
    """Inventory archive/ subtrees. Returns coarse stats; the archive is
    text-only, so the inventory is just a file list with alias counts."""
    out: Dict = {}
    archive_root = WORKSPACE / "archive"
    if not archive_root.exists():
        return out
    for sub in sorted(archive_root.iterdir()):
        if not sub.is_dir():
            continue
        files: List[str] = []
        counter: Counter = Counter()
        for f in sorted(sub.rglob("*")):
            if not f.is_file():
                continue
            rel = f.relative_to(archive_root)
            files.append(str(rel))
            if f.suffix in {".md", ".yaml", ".yml", ".txt"}:
                try:
                    counter.update(ALIAS_RE.findall(f.read_text(errors="replace")))
                except OSError:
                    continue
        out[sub.name] = {
            "files": files,
            "file_count": len(files),
            "alias_count": sum(counter.values()),
            "alias_freq": counter,
        }
    return out


def _alias_index_global(rows: List[Dict]) -> Counter:
    total: Counter = Counter()
    for r in rows:
        total.update(r["alias_freq"])
    return total


def _classify_alias_kind(alias: str) -> str:
    if alias.startswith("DV-S") or alias.startswith("D-S"):
        return "decisions"
    if alias.startswith("EF-S"):
        return "engine_feedback"
    if alias.startswith("FR-S"):
        return "forward_references"
    if alias.startswith("OI-"):
        return "open_issues"
    if alias.startswith("SPEC-"):
        return "spec_versions"
    if alias.startswith("A-"):
        return "assumptions"
    return "other"


def render(rows: List[Dict], doublets, archive: Dict, totals: Counter) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    by_kind: Dict[str, int] = defaultdict(int)
    for alias, n in totals.items():
        by_kind[_classify_alias_kind(alias)] += n

    lines: List[str] = []
    lines.append("# Legacy substrate summary — pre-S180 evidence inventory")
    lines.append("")
    lines.append(f"_Generated by tools/extract-legacy-substrate.py at {now}._")
    lines.append("")
    lines.append("## Scope and what is lost")
    lines.append("")
    lines.append(
        "L4B extractor pivoted at S186-open: no pre-S180 binary substrate "
        "backups survive. `state/selvedge.sqlite` is gitignored (never in "
        "git history); `state/selvedge.sqlite.pre-migrate-backup` is an "
        "empty post-S180-init artefact carrying only migration 001; the "
        "only on-disk backups are S185-era L3 boundary snapshots under "
        "`state/snapshots/`."
    )
    lines.append("")
    lines.append("**Lost as typed-row data (S001–S179):**")
    lines.append("")
    lines.append("- decision_v2 rows + their supports/alternatives/effects/cite walks")
    lines.append("- spec_versions rows + spec_sections/spec_clauses + body_sha256 chain")
    lines.append("- engine_feedback rows + their dispositions")
    lines.append("- forward_reference_dispositions + open-issue dispositions")
    lines.append("- assumption_register A-NNN rows")
    lines.append("- deliberation_counterfactuals + synthesis_points + perspectives rows")
    lines.append("- review_findings + decision_chain_walks receipts")
    lines.append("- objects.alias index for cross-row reference resolution")
    lines.append("")
    lines.append("**Recovered as markdown evidence:** the per-session export files committed to git over the S001–S185 arc (and rebuilt as post-S180-recovery exports for S080–S084).")
    lines.append("")

    lines.append("## Provenance directory inventory")
    lines.append("")
    lines.append(f"Total directories scanned: **{len(rows)}**.")
    lines.append("")
    if doublets:
        lines.append("### S180-wipe recovery doublets")
        lines.append("")
        lines.append(
            "Sessions S080–S084 carry two provenance directories each: the "
            "pre-S180 original (lost from substrate, preserved as markdown) "
            "and the post-S180 recovery session (rebuilt the substrate with "
            "the same workspace_session_no per S185 init_session_offset bump)."
        )
        lines.append("")
        lines.append("| session_no | dirs |")
        lines.append("|------------|------|")
        for sess_no, dirs in doublets:
            lines.append(f"| {sess_no} | {', '.join(dirs)} |")
        lines.append("")

    lines.append("### Per-session inventory (alias-bearing rows only)")
    lines.append("")
    lines.append("Rows with zero alias mentions (e.g. genesis, early scaffolding sessions) are omitted to keep the table readable; their directories are still on disk under `provenance/`.")
    lines.append("")
    lines.append("| session_no | dir | files | alias mentions |")
    lines.append("|------------|-----|-------|----------------|")
    for r in rows:
        if r["alias_count"] == 0:
            continue
        files_summary = ",".join(f.replace(".md", "") for f in r["files"])
        lines.append(
            f"| {r['session_no']:03d} | {r['dir']} | {files_summary} | {r['alias_count']} |"
        )
    lines.append("")

    lines.append("## Archive/ inventory")
    lines.append("")
    if not archive:
        lines.append("_No archive/ subtree present._")
    else:
        for name, info in archive.items():
            lines.append(f"### archive/{name}")
            lines.append("")
            lines.append(f"- file count: **{info['file_count']}**")
            lines.append(f"- alias mentions: **{info['alias_count']}**")
            if info["alias_count"]:
                top = info["alias_freq"].most_common(10)
                lines.append("- top aliases: " + ", ".join(f"`{a}`×{n}" for a, n in top))
            lines.append("")

    lines.append("## Alias index (global; pre-S180 + recovery markdown)")
    lines.append("")
    lines.append("Counts are markdown-mention frequencies, not substrate-row counts. The same alias often appears in multiple sessions (e.g. a DV cited in its origin session + downstream sessions that cite it).")
    lines.append("")
    lines.append("| kind | distinct aliases | total mentions |")
    lines.append("|------|------------------|----------------|")
    by_kind_distinct: Dict[str, set] = defaultdict(set)
    for alias in totals:
        by_kind_distinct[_classify_alias_kind(alias)].add(alias)
    for kind in sorted(by_kind):
        lines.append(
            f"| {kind} | {len(by_kind_distinct[kind])} | {by_kind[kind]} |"
        )
    lines.append("")
    lines.append(f"Total distinct aliases observed: **{len(totals)}**. Total mentions: **{sum(totals.values())}**.")
    lines.append("")

    lines.append("## Recovery posture")
    lines.append("")
    lines.append(
        "The markdown is human-readable but not substrate-typed — alias "
        "references resolve only by re-reading the export, not via "
        "`objects.alias` joins. A future session that needs a specific "
        "pre-S180 row's substantive content reads the markdown directly; "
        "no extractor can rebuild typed substrate rows from the export "
        "because the export is lossy (text_atoms by design, no foreign-key "
        "structure)."
    )
    lines.append("")
    lines.append(
        "Open question OI-S180-1 (HIGH) — \"manual rebuild from markdown "
        "exports\" — is therefore the operator's call: ship a "
        "`tools/rebuild-from-provenance.py` (FR-S080-9) that re-parses the "
        "markdown into substrate rows in chronological order, OR accept the "
        "markdown-only posture and close OI-S180-1 by-mechanism. This "
        "extractor intentionally does NOT attempt rebuild — it is the "
        "inventory side of the L4B layer per DV-S081-1 + OI-S081-5 scope."
    )
    lines.append("")

    return "\n".join(lines) + "\n"


def main() -> int:
    rows = _provenance_inventory()
    doublets = _detect_doublets(rows)
    archive = _archive_inventory()
    totals = _alias_index_global(rows)
    body = render(rows, doublets, archive, totals)
    out = WORKSPACE / "provenance" / "legacy-substrate-summary.md"
    out.write_text(body)
    print(f"wrote {out} ({len(body)} bytes; {len(rows)} dirs; "
          f"{len(totals)} distinct aliases; {sum(totals.values())} mentions)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
