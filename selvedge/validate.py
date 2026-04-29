"""`selvedge validate --precommit` — substrate integrity + spec hash checks."""

from __future__ import annotations

import hashlib
import sqlite3
import sys

from .paths import db_path, workspace_root


def cmd_validate(args) -> int:
    path = db_path()
    if not path.exists():
        print(f"no substrate at {path} (run `selvedge init` first)", file=sys.stderr)
        return 2
    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    failures: list[str] = []

    if (row := conn.execute("PRAGMA integrity_check").fetchone()) and row[0] != "ok":
        failures.append(f"integrity_check: {row[0]}")
    fk = conn.execute("PRAGMA foreign_key_check").fetchall()
    if fk:
        failures.append(f"foreign_key_check: {len(fk)} violations: {[dict(r) for r in fk[:5]]}")

    rows = conn.execute(
        "SELECT spec_id, version, body_path, body_sha256 FROM spec_versions WHERE status='active'"
    ).fetchall()
    for r in rows:
        p = workspace_root() / r["body_path"]
        if not p.exists():
            failures.append(f"spec hash: missing file {r['body_path']}")
            continue
        sha = hashlib.sha256(p.read_bytes()).hexdigest()
        if sha != r["body_sha256"]:
            failures.append(
                f"spec hash mismatch: {r['spec_id']}-v{r['version']} {sha[:8]} != {r['body_sha256'][:8]}"
            )

    bad_refs = conn.execute(
        "SELECT ref_id FROM refs WHERE source_object_id NOT IN (SELECT object_id FROM objects) "
        "OR target_object_id NOT IN (SELECT object_id FROM objects)"
    ).fetchall()
    if bad_refs:
        failures.append(f"refs: {len(bad_refs)} unresolved")

    n_open = conn.execute("SELECT COUNT(*) AS n FROM sessions WHERE status='open'").fetchone()["n"]
    if n_open > 1:
        failures.append(f"more than one open session: {n_open}")

    last_mig = conn.execute(
        "SELECT name, sha256 FROM schema_migrations ORDER BY migration_id DESC LIMIT 1"
    ).fetchone()
    if last_mig is None:
        failures.append("no schema_migrations rows; substrate appears uninitialised")

    conn.close()
    if failures:
        for f in failures:
            print(f"FAIL  {f}", file=sys.stderr)
        return 1
    print("validate --precommit: ok")
    return 0
