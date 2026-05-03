"""`selvedge restore` — recover a substrate from an L3 snapshot file.

Closes OI-S081-4 per DV-S081-1 C-4 + FR-S081-11. The CLI mirrors the L1a
init guard's two-flag shape: a default-safe path that refuses to clobber a
live primary, and an explicit ``--confirm`` token the operator types when
the destructive overwrite is the deliberate intent.

Three operations:

1. ``restore --from <snapshot> --to <target>`` writes the snapshot bytes to
   the target path. If ``--to`` resolves to the live primary substrate
   (``state/selvedge.sqlite``) and ``--confirm`` is absent, the command
   refuses with E_LIVE_PRIMARY and exits 2.
2. ``--verify`` recomputes the snapshot file's sha256 and compares it
   against the ``snapshot_catalog`` row. Mismatch is exit 2; missing row is
   exit 2 with a different code so an out-of-catalog snapshot is
   distinguishable.
3. WAL/SHM sidecars at the target path are unlinked before the copy so a
   restored DB is not blended with stale write-ahead bytes from a prior
   open connection.

Restore writes via shutil.copy of the snapshot file. The snapshot was
itself produced by sqlite3.Connection.backup() (page-aware, transaction-
consistent), so a byte-for-byte copy of that file produces an equivalent
SQLite database. We do NOT run a live backup() in reverse because that
would require an open destination we are about to overwrite.
"""

from __future__ import annotations

import hashlib
import shutil
import sqlite3
import sys
from pathlib import Path
from typing import Optional

from .paths import db_path


def _sha256_file(path: Path, chunk: int = 1 << 16) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while buf := f.read(chunk):
            h.update(buf)
    return h.hexdigest()


def _catalog_lookup(snapshot_path: Path) -> Optional[dict]:
    """Find a snapshot_catalog row whose path matches ``snapshot_path``.

    Searches the live primary substrate first (so an operator who already
    has the catalog can verify against it). Returns None if either the
    primary substrate is unreadable, the catalog table is absent, or no row
    matches the resolved path.
    """
    primary = db_path()
    if not primary.exists():
        return None
    try:
        conn = sqlite3.connect(f"file:{primary}?mode=ro", uri=True)
    except sqlite3.Error:
        return None
    try:
        try:
            row = conn.execute(
                "SELECT snapshot_id, trigger, path, sha256, source_db_sha256, "
                "       sqlite_page_count, size_bytes, source_session_no, "
                "       engine_version, created_utc "
                "FROM snapshot_catalog WHERE path = ?",
                (str(snapshot_path),),
            ).fetchone()
        except sqlite3.Error:
            return None
        if row is None:
            return None
        return {
            "snapshot_id": row[0],
            "trigger": row[1],
            "path": row[2],
            "sha256": row[3],
            "source_db_sha256": row[4],
            "sqlite_page_count": row[5],
            "size_bytes": row[6],
            "source_session_no": row[7],
            "engine_version": row[8],
            "created_utc": row[9],
        }
    finally:
        conn.close()


def cmd_restore(args) -> int:
    # .resolve() canonicalises through symlinks AND any '..' segments. A
    # symlink at --to whose target is the live primary therefore resolves
    # to the same absolute path as db_path().resolve() and triggers the
    # E_LIVE_PRIMARY refusal below (RF-S084-17 confirmed safe by test
    # test_restore_refuses_symlink_to_primary).
    src = Path(args.from_).resolve()
    dst = Path(args.to).resolve()
    confirm = bool(getattr(args, "confirm", False))
    verify = bool(getattr(args, "verify", False))
    primary = db_path().resolve()

    if not src.exists():
        print(f"refused: snapshot {src} does not exist", file=sys.stderr)
        return 2
    if not src.is_file():
        print(f"refused: snapshot {src} is not a file", file=sys.stderr)
        return 2

    if verify:
        actual = _sha256_file(src)
        row = _catalog_lookup(src)
        if row is None:
            print(
                f"refused: E_NO_CATALOG_ROW — no snapshot_catalog row for {src}; "
                f"the snapshot exists on disk but the live substrate has no record "
                f"of it. Restore can still proceed without --verify.",
                file=sys.stderr,
            )
            return 2
        if row["sha256"] != actual:
            print(
                f"refused: E_VERIFY_MISMATCH — snapshot file sha256 {actual} "
                f"differs from snapshot_catalog row sha256 {row['sha256']}. "
                f"The file may be corrupted or modified post-snapshot.",
                file=sys.stderr,
            )
            return 2

    if dst == primary and not confirm:
        print(
            f"refused: E_LIVE_PRIMARY — refusing to overwrite the live primary "
            f"substrate at {dst} without --confirm. Restore to a tempdir target "
            f"first and inspect with `bin/selvedge query`, then re-run with "
            f"--confirm if the overwrite is the deliberate intent.",
            file=sys.stderr,
        )
        return 2

    dst.parent.mkdir(parents=True, exist_ok=True)
    for sidecar in [
        dst.with_name(dst.name + "-wal"),
        dst.with_name(dst.name + "-shm"),
    ]:
        if sidecar.exists():
            try:
                sidecar.unlink()
            except OSError as e:
                print(f"warning: could not unlink stale sidecar {sidecar}: {e}", file=sys.stderr)

    try:
        shutil.copy(src, dst)
    except OSError as e:
        print(f"refused: copy failed {src} -> {dst}: {e}", file=sys.stderr)
        return 2

    out_sha = _sha256_file(dst)
    print(
        f"restored: {dst}\n"
        f"  from: {src}\n"
        f"  sha256: {out_sha}\n"
        f"  size: {dst.stat().st_size} bytes\n"
        f"  verify: {'pass' if verify else 'skipped'}\n"
        f"  primary: {'overwritten' if dst == primary else 'untouched'}"
    )
    return 0
