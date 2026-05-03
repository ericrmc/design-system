"""`selvedge init` — fresh substrate from migration 001 + any later migrations.

L1a live-substrate guard (DV-S081-1, S082): when `--force` would unlink an
existing substrate that already carries `sessions` rows, the command refuses
with `E_LIVE_SUBSTRATE` and names the row count + recovery path. The override
is `--really-force`, a separate flag the operator types deliberately. The
guard never fires on a path that does not exist or that exists without a
`sessions` table populated. Predicate is "any sessions row exists" per S082
codex-shape-consult; alternatives (workspace_metadata presence, file-size
threshold, fixture allowlist) were rejected as overfiring or brittle.

Substrate-files-without-sessions-table (corrupt, partial-init, or unreadable)
are treated as not-live by design (no work to defend, recovery requires
`--force` admit). The guard's commitment is narrow: refuse `--force` on a
substrate that has at least one row of recorded session work. Anything else
admits the existing `--force` semantics.
"""

from __future__ import annotations

import hashlib
import sqlite3
import sys
from pathlib import Path

from .migrations import _apply_pending, _migration_state
from .paths import db_path, migrations_dir
from .snapshots import take_snapshot


def _live_substrate_session_count(path: Path) -> int:
    """Return the row count of the `sessions` table on the substrate at
    `path`, or 0 if the file is unreadable, the table is absent, or the
    query fails. Read-only access; never mutates the substrate."""
    if not path.exists():
        return 0
    try:
        conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    except sqlite3.Error:
        return 0
    try:
        try:
            row = conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='sessions'"
            ).fetchone()
            if row is None:
                return 0
            count = conn.execute("SELECT COUNT(*) FROM sessions").fetchone()[0]
            return int(count)
        except sqlite3.Error:
            return 0
    finally:
        conn.close()


def cmd_init(args) -> int:
    path = db_path()
    really_force = bool(getattr(args, "really_force", False))
    force = bool(getattr(args, "force", False)) or really_force
    if path.exists() and not force:
        print(f"refused: {path} already exists; use --force to overwrite", file=sys.stderr)
        return 2
    if path.exists() and not really_force:
        sessions = _live_substrate_session_count(path)
        if sessions > 0:
            # L3 init_refused snapshot before refusal so the agent who hit
            # this guard can grab a fresh anchor copy of the substrate state
            # they were about to wipe (DV-S081-1, OI-S081-3).
            take_snapshot("init_refused", source_path=path)
            print(
                f"refused: E_LIVE_SUBSTRATE — {path} carries {sessions} session row(s); "
                f"--force is refused on a substrate with active session rows. Recovery: "
                f"restore from a snapshot via `bin/selvedge restore --from <snapshot> "
                f"--to {path} --confirm` or, if destruction is the deliberate intent, "
                f"rerun with --really-force.",
                file=sys.stderr,
            )
            return 2
    if path.exists():
        if really_force and _live_substrate_session_count(path) > 0:
            # L3 init_forced snapshot before unlink so even a deliberate
            # destructive override leaves a recoverable anchor on disk.
            take_snapshot("init_forced", source_path=path)
        path.unlink()
    for sidecar in [path.with_suffix(".sqlite-wal"), path.with_suffix(".sqlite-shm")]:
        if sidecar.exists():
            sidecar.unlink()
    migration = migrations_dir() / "001-initial.sql"
    if not migration.exists():
        print(f"missing migration: {migration}", file=sys.stderr)
        return 2
    sql = migration.read_text()
    sha = hashlib.sha256(sql.encode()).hexdigest()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path))
    try:
        conn.executescript(sql)
        conn.execute(
            "UPDATE schema_migrations SET sha256 = ? WHERE name = ?",
            (sha, "001-initial.sql"),
        )
        conn.commit()
    finally:
        conn.close()
    print(f"initialised {path}")
    print(f"migration: 001-initial.sql sha256={sha}")

    pending = _migration_state(path)["pending"]
    if pending:
        applied_now = _apply_pending(path, pending)
        for name, sha_applied in applied_now:
            print(f"migration: {name} sha256={sha_applied}")
    return 0
