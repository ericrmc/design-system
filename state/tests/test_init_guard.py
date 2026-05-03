"""L1a init --force live-substrate guard (DV-S081-1, S082, OI-S081-1).

The guard refuses `selvedge init --force` when the target substrate already
holds rows in the `sessions` table. The escape is `--really-force`. Tests
exercise the predicate against a substrate isolated under `tmp_path` so the
production substrate is never at risk.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

WORKSPACE = Path(__file__).resolve().parents[2]
BIN = WORKSPACE / "bin" / "selvedge"


def _run(env: dict, args: list[str]) -> dict:
    proc = subprocess.run(
        [str(BIN), *args],
        capture_output=True,
        text=True,
        env=env,
    )
    out = (proc.stdout or "").strip()
    err = (proc.stderr or "").strip()
    parsed = None
    if out:
        try:
            parsed = json.loads(out)
        except json.JSONDecodeError:
            parsed = {"_raw": out}
    return {"rc": proc.returncode, "out": parsed, "err": err}


@pytest.fixture
def isolated_substrate(tmp_path):
    """Stage a tmp workspace with a copy of migrations + MODE.md so init/migrate
    behave naturally but write to a substrate disjoint from the production DB."""
    (tmp_path / "MODE.md").write_text("---\nmode: self-development\nworkspace_id: tmp-init-guard\n---\n")
    mig_dir = tmp_path / "migrations"
    mig_dir.mkdir()
    for src in (WORKSPACE / "state" / "migrations").iterdir():
        if src.suffix == ".sql":
            shutil.copy(src, mig_dir / src.name)
    db = tmp_path / "selvedge.sqlite"
    env = os.environ | {
        "SELVEDGE_WORKSPACE": str(tmp_path),
        "SELVEDGE_DB_PATH": str(db),
        "SELVEDGE_MIGRATIONS_DIR": str(mig_dir),
    }
    return {"env": env, "db": db}


def _open_session(env: dict) -> dict:
    return _run(
        env,
        [
            "submit",
            "session-open",
            "--payload",
            json.dumps(
                {
                    "session_no": 1,
                    "slug": "init-guard-fixture",
                    "mode": "self-development",
                    "workspace_id": "tmp-init-guard",
                    "engine_version_at_open": "engine-v17",
                    "kind": "spec_only",
                }
            ),
        ],
    )


def test_init_force_succeeds_on_missing_substrate(isolated_substrate):
    """No DB present → init --force succeeds (round_trip.sh path)."""
    res = _run(isolated_substrate["env"], ["init", "--force"])
    assert res["rc"] == 0, res
    assert isolated_substrate["db"].exists()


def test_init_force_succeeds_on_initialised_empty_substrate(isolated_substrate):
    """DB exists but no sessions rows → init --force succeeds (conftest path)."""
    init1 = _run(isolated_substrate["env"], ["init", "--force"])
    assert init1["rc"] == 0, init1
    init2 = _run(isolated_substrate["env"], ["init", "--force"])
    assert init2["rc"] == 0, init2


def test_init_force_refuses_live_substrate(isolated_substrate):
    """DB exists with sessions row → init --force refuses with E_LIVE_SUBSTRATE."""
    init1 = _run(isolated_substrate["env"], ["init", "--force"])
    assert init1["rc"] == 0, init1
    open_res = _open_session(isolated_substrate["env"])
    assert open_res["rc"] == 0, open_res
    init2 = _run(isolated_substrate["env"], ["init", "--force"])
    assert init2["rc"] == 2, init2
    assert "E_LIVE_SUBSTRATE" in init2["err"]
    assert "session row" in init2["err"]
    assert "--really-force" in init2["err"]
    assert isolated_substrate["db"].exists()


def test_init_really_force_overrides_guard(isolated_substrate):
    """--really-force is the deliberate destructive override."""
    init1 = _run(isolated_substrate["env"], ["init", "--force"])
    assert init1["rc"] == 0, init1
    open_res = _open_session(isolated_substrate["env"])
    assert open_res["rc"] == 0, open_res
    init2 = _run(isolated_substrate["env"], ["init", "--really-force"])
    assert init2["rc"] == 0, init2
    init3 = _run(isolated_substrate["env"], ["init", "--force", "--really-force"])
    assert init3["rc"] == 0, init3


def test_init_no_flag_refuses_existing(isolated_substrate):
    """Existing-substrate refusal without --force still fires (regression check)."""
    init1 = _run(isolated_substrate["env"], ["init", "--force"])
    assert init1["rc"] == 0, init1
    init2 = _run(isolated_substrate["env"], ["init"])
    assert init2["rc"] == 2, init2
    assert "already exists" in init2["err"]


def test_init_really_force_succeeds_on_missing_substrate(isolated_substrate):
    """--really-force implies --force; works against a non-existent substrate."""
    res = _run(isolated_substrate["env"], ["init", "--really-force"])
    assert res["rc"] == 0, res
    assert isolated_substrate["db"].exists()


def test_init_force_admits_corrupt_substrate(isolated_substrate, tmp_path):
    """Substrate file exists but is unreadable as SQLite (corrupt random bytes):
    guard treats as not-live by design. No `sessions` rows = no work to defend."""
    db = isolated_substrate["db"]
    db.write_bytes(b"this is not a valid sqlite file" * 16)
    res = _run(isolated_substrate["env"], ["init", "--force"])
    assert res["rc"] == 0, res
    assert db.exists()


def test_init_force_admits_partial_init_no_sessions_table(isolated_substrate):
    """Substrate file exists but lacks the `sessions` table (partial schema):
    guard treats as not-live, --force proceeds without --really-force."""
    import sqlite3 as _sql

    db = isolated_substrate["db"]
    conn = _sql.connect(str(db))
    try:
        conn.executescript(
            "CREATE TABLE schema_migrations (name TEXT, sha256 TEXT);"
            "CREATE TABLE not_sessions (n INTEGER);"
            "INSERT INTO not_sessions (n) VALUES (1);"
        )
        conn.commit()
    finally:
        conn.close()
    res = _run(isolated_substrate["env"], ["init", "--force"])
    assert res["rc"] == 0, res


def test_init_force_refusal_message_clarity(isolated_substrate):
    """Refusal message names the row count and the recovery path without
    claiming --force never unlinks anything (RF-12 phrasing fix)."""
    init1 = _run(isolated_substrate["env"], ["init", "--force"])
    assert init1["rc"] == 0, init1
    open_res = _open_session(isolated_substrate["env"])
    assert open_res["rc"] == 0, open_res
    res = _run(isolated_substrate["env"], ["init", "--force"])
    assert res["rc"] == 2, res
    err = res["err"]
    assert "E_LIVE_SUBSTRATE" in err
    assert "refused" in err.lower()
    assert "--really-force" in err
    assert "restore" in err.lower() or "snapshot" in err.lower()
    assert "will not unlink a populated substrate" not in err
