"""`selvedge init` — fresh substrate from migration 001 + any later migrations."""

from __future__ import annotations

import hashlib
import sqlite3
import sys

from .migrations import _apply_pending, _migration_state
from .paths import db_path, migrations_dir


def cmd_init(args) -> int:
    path = db_path()
    if path.exists() and not args.force:
        print(f"refused: {path} already exists; use --force to overwrite", file=sys.stderr)
        return 2
    if path.exists():
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
