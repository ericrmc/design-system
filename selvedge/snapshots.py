"""L3 boundary snapshots (DV-S081-1, OI-S081-3, FR-S081-11).

Closes part of the substrate-loss-defense package sealed at S081. A snapshot
is a sqlite3.Connection.backup() copy of the primary substrate written to
``state/snapshots/<utc>-<trigger>-<wno>.sqlite`` with a
``snapshot_catalog`` row recording trigger, sha256 of the snapshot file,
sha256 of the source DB, page count, size, source session, engine version,
and the retention band that placed the row.

Snapshots fire AFTER the trigger event commits — never inside the same
write_tx — so a rolled-back submit produces no snapshot. The L3 dispatcher
opens its own short-lived connection to the target file via
``sqlite3.Connection.backup()`` and closes it before recording the catalog
row in a second connection. Failures on snapshot are non-fatal: they log to
stderr and otherwise return cleanly so the trigger event is not undone by a
defense layer that itself misfires.

The snapshot directory lives at ``state/snapshots/`` inside the workspace
boundary (codex-shape-consult Q3, S084) but outside the git boundary via
.gitignore. Runtime recoverability beats clone portability; a freshly
cloned workspace rebuilds snapshots forward as the engine runs.
"""

from __future__ import annotations

import hashlib
import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from .paths import db_path, workspace_root


# Trigger enum mirrors the snapshot_catalog.trigger CHECK in migration 042.
VALID_TRIGGERS = frozenset({
    "session_open",
    "session_close",
    "migrate_apply",
    "init_refused",
    "init_forced",
    "manual",
})


def snapshots_dir() -> Path:
    """Return the snapshot directory; create it if missing.

    Honours SELVEDGE_SNAPSHOTS_DIR for tests + alternate-workspace overrides.
    """
    if override := os.environ.get("SELVEDGE_SNAPSHOTS_DIR"):
        d = Path(override).resolve()
    else:
        d = workspace_root() / "state" / "snapshots"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _sha256_file(path: Path, chunk: int = 1 << 16) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while buf := f.read(chunk):
            h.update(buf)
    return h.hexdigest()


def _source_db_sha256(source: Path) -> str:
    """sha256 of the live source DB file as bytes-on-disk.

    Captured AFTER backup() runs so it represents the source-as-bytes at
    snapshot completion time (the source is read-only during backup, so the
    bytes are stable across the backup window). Pairs with the snapshot's
    own sha256: identical values mean the snapshot file is a byte-for-byte
    copy of the source DB; divergence is normal when WAL pages exist that
    backup() flattens into the snapshot but the source still carries on
    disk.
    """
    if not source.exists():
        return "0" * 64
    return _sha256_file(source)


def take_snapshot(
    trigger: str,
    *,
    source_path: Optional[Path] = None,
    source_session_no: Optional[int] = None,
    engine_version: Optional[str] = None,
) -> Optional[Path]:
    """Take a boundary snapshot of the source DB and record it in
    ``snapshot_catalog``.

    Returns the snapshot file path on success, or ``None`` if the snapshot
    could not be taken (missing source, write failure, missing catalog
    table). Failures emit a single line to stderr; they do not raise so that
    a defense-layer misfire never undoes the trigger event itself.
    """
    if trigger not in VALID_TRIGGERS:
        print(f"snapshot: refusing unknown trigger {trigger!r}", file=sys.stderr)
        return None
    src = source_path if source_path is not None else db_path()
    if not src.exists():
        return None

    try:
        d = snapshots_dir()
    except Exception as e:
        print(f"snapshot: cannot resolve snapshots dir: {e}", file=sys.stderr)
        return None

    # Path includes microsecond timestamp + pid so two simultaneous calls
    # (cross-process or fast-retry within-process) cannot collide on the
    # snapshot_catalog UNIQUE(path) constraint and orphan a snapshot file
    # on disk (RF-S084-16, RF-S084-19).
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    wno_part = f"-S{source_session_no:03d}" if source_session_no is not None else ""
    out = d / f"{ts}-{trigger}{wno_part}-pid{os.getpid()}.sqlite"

    try:
        src_conn = sqlite3.connect(f"file:{src}?mode=ro", uri=True)
    except sqlite3.Error as e:
        print(f"snapshot: cannot open source {src}: {e}", file=sys.stderr)
        return None
    try:
        dst_conn = sqlite3.connect(str(out))
        try:
            src_conn.backup(dst_conn)
            page_count = dst_conn.execute("PRAGMA page_count").fetchone()[0]
        finally:
            dst_conn.close()
    except sqlite3.Error as e:
        print(f"snapshot: backup failed for {src} -> {out}: {e}", file=sys.stderr)
        if out.exists():
            try:
                out.unlink()
            except OSError:
                pass
        return None
    finally:
        src_conn.close()

    # Both sha256 values captured post-backup: src_sha is the source bytes
    # at snapshot-completion time (RF-S084-18 fix; previously captured pre-
    # backup which created a small drift window).
    src_sha = _source_db_sha256(src)
    snap_sha = _sha256_file(out)
    size_bytes = out.stat().st_size

    if engine_version is None:
        engine_version = _read_engine_version(src) or "unknown"

    if not _record_catalog_row(
        src,
        path=out,
        trigger=trigger,
        sha256=snap_sha,
        source_db_sha256=src_sha,
        sqlite_page_count=int(page_count),
        size_bytes=int(size_bytes),
        source_session_no=source_session_no,
        engine_version=engine_version,
    ):
        return None

    return out


def _read_engine_version(src: Path) -> Optional[str]:
    """Read workspace_metadata.current_engine_version from the source DB."""
    try:
        conn = sqlite3.connect(f"file:{src}?mode=ro", uri=True)
    except sqlite3.Error:
        return None
    try:
        try:
            row = conn.execute(
                "SELECT value FROM workspace_metadata WHERE key='current_engine_version'"
            ).fetchone()
            return row[0] if row else None
        except sqlite3.Error:
            return None
    finally:
        conn.close()


def _record_catalog_row(
    src: Path,
    *,
    path: Path,
    trigger: str,
    sha256: str,
    source_db_sha256: str,
    sqlite_page_count: int,
    size_bytes: int,
    source_session_no: Optional[int],
    engine_version: str,
) -> bool:
    """Insert one snapshot_catalog row in the source DB. Returns False on
    catalog-table absence (substrate predates migration 042) or insert
    failure; in both cases the snapshot file remains on disk so a future
    catalog-aware run can re-record it."""
    try:
        conn = sqlite3.connect(str(src))
    except sqlite3.Error as e:
        print(f"snapshot: cannot open source for catalog write: {e}", file=sys.stderr)
        return False
    try:
        has = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='snapshot_catalog'"
        ).fetchone()
        if has is None:
            return False
        try:
            conn.execute(
                "INSERT INTO snapshot_catalog "
                "(trigger, path, sha256, source_db_sha256, sqlite_page_count, "
                " size_bytes, source_session_no, engine_version) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    trigger,
                    str(path),
                    sha256,
                    source_db_sha256,
                    sqlite_page_count,
                    size_bytes,
                    source_session_no,
                    engine_version,
                ),
            )
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"snapshot: catalog insert failed: {e}", file=sys.stderr)
            return False
    finally:
        conn.close()
