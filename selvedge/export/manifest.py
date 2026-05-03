"""export_manifest substrate-side recovery index (engine-v52, OI-S081-7).

One row per markdown file actually written by `selvedge export`. The
manifest is a recovery index — not an audit log — so re-export replaces
the existing row via UNIQUE(path) + INSERT OR REPLACE rather than
appending history. Loss of `state/selvedge.sqlite` leaves this index
recoverable from the markdown files themselves plus git history.

Shape decisions sealed at S081 DV-1 C-9 + S188 codex-shape-consult:

- path stored relative to workspace_root (cross-machine portable).
- sha256 computed on the bytes that landed on disk, after the write.
- session_no carries workspace_session_no for per-session artefacts;
  NULL for workspace-wide indices (open-issues index, spec_versions
  ledger).
- row_count is informational (rows the file materialised); defaults to
  0 when the caller cannot supply a meaningful count.
- Failed writes produce no row: callers invoke `record_manifest_entry`
  only after the write succeeded.
"""

from __future__ import annotations

import hashlib
import sqlite3
from pathlib import Path
from typing import Optional

from ..paths import workspace_root


VALID_KINDS = frozenset({
    "assessment",
    "deliberation",
    "decisions",
    "close",
    "review",
    "engine_feedback",
    "counterfactuals",
    "fr_dispositions",
    "prechecks",
    "chain_walks",
    "harness",
    "open_issues_index",
    "open_issue",
    "spec_versions_index",
})


def workspace_relative(path: Path) -> str:
    """Public helper that mirrors `_relative_path` for callers outside this
    module who need the same workspace-root-anchored normalization (e.g.
    stale-file reconciliation in session.py / issues.py). Raises ValueError
    when `path` is outside workspace_root."""
    return _relative_path(path)


def _relative_path(path: Path) -> str:
    """Return path relative to workspace_root.

    Raises ValueError when `path` lives outside the workspace boundary so
    the manifest never silently records absolute paths (which would break
    cross-machine recovery). Callers in this module always pass paths
    under workspace_root by construction; a raise here surfaces a real
    bug rather than corrupting the index.
    """
    return str(path.resolve().relative_to(workspace_root().resolve()))


def record_manifest_entry(
    conn: sqlite3.Connection,
    *,
    kind: str,
    path: Path,
    session_no: Optional[int] = None,
    row_count: int = 0,
    content: Optional[str] = None,
) -> bool:
    """Write one export_manifest row for `path`. Returns False on failure or
    if the manifest table is absent (substrate predates migration 044) or if
    the file does not exist on disk.

    `content` is optional: when provided, sha256 is computed from the string
    bytes (cheaper than re-reading the file just-written). When omitted,
    sha256 is computed by reading the file from disk. Either way, the read
    happens AFTER the write so the recorded sha matches the bytes that
    landed.
    """
    if kind not in VALID_KINDS:
        return False
    if not path.exists():
        return False
    has = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='export_manifest'"
    ).fetchone()
    if has is None:
        return False
    if content is not None:
        sha = hashlib.sha256(content.encode("utf-8")).hexdigest()
        size_bytes = len(content.encode("utf-8"))
    else:
        h = hashlib.sha256()
        with path.open("rb") as f:
            while buf := f.read(1 << 16):
                h.update(buf)
        sha = h.hexdigest()
        size_bytes = path.stat().st_size
    try:
        rel_path = _relative_path(path)
    except ValueError:
        return False
    conn.execute(
        "INSERT OR REPLACE INTO export_manifest "
        "(session_no, kind, path, sha256, size_bytes, row_count) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (session_no, kind, rel_path, sha, size_bytes, int(row_count)),
    )
    conn.commit()
    return True


# Mapping from per-session filename -> manifest kind. Used by session.py
# after it writes each 00–09 file. Kept here so the kind enum lives next to
# the writer.
SESSION_FILE_KINDS = {
    "00-assessment.md":      "assessment",
    "01-deliberation.md":    "deliberation",
    "02-decisions.md":       "decisions",
    "03-close.md":           "close",
    "04-review.md":          "review",
    "05-engine-feedback.md": "engine_feedback",
    "06-counterfactuals.md": "counterfactuals",
    "07-fr-dispositions.md": "fr_dispositions",
    "08-prechecks.md":       "prechecks",
    "09-chain-walks.md":     "chain_walks",
}
