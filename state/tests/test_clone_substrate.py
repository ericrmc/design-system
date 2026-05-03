"""L2b subagent tempdir-clone (DV-S081-1, OI-S081-2, S186).

Tests run against an isolated substrate so the production primary and
snapshots directory are never touched.

Coverage:
  - clone-substrate produces a valid SQLite file matching the primary.
  - writes against the clone DO NOT propagate to the primary (codex Q2
    isolation guarantee for the L2b subagent dispatch surface).
  - clone-substrate refuses --to=primary with E_LIVE_PRIMARY.
  - clone-substrate refuses --to=symlink-to-primary with E_LIVE_PRIMARY.
  - clone-substrate refuses when the primary does not exist (E_NO_SOURCE).
  - clone with explicit --to writes to that path.
  - default clone path uses the selvedge-subagent-clone- prefix.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest

WORKSPACE = Path(__file__).resolve().parents[2]
BIN = WORKSPACE / "bin" / "selvedge"


def _sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def _run(env: dict, args: list[str]) -> dict:
    proc = subprocess.run(
        [str(BIN), *args],
        capture_output=True,
        text=True,
        env=env,
    )
    return {
        "rc": proc.returncode,
        "stdout": (proc.stdout or "").strip(),
        "err": (proc.stderr or "").strip(),
    }


@pytest.fixture
def isolated(tmp_path):
    (tmp_path / "MODE.md").write_text("---\nmode: self-development\nworkspace_id: tmp-clone\n---\n")
    mig_dir = tmp_path / "migrations"
    mig_dir.mkdir()
    for src in (WORKSPACE / "state" / "migrations").iterdir():
        if src.suffix == ".sql":
            shutil.copy(src, mig_dir / src.name)
    db = tmp_path / "selvedge.sqlite"
    snaps = tmp_path / "snapshots"
    env = os.environ | {
        "SELVEDGE_WORKSPACE": str(tmp_path),
        "SELVEDGE_DB_PATH": str(db),
        "SELVEDGE_MIGRATIONS_DIR": str(mig_dir),
        "SELVEDGE_SNAPSHOTS_DIR": str(snaps),
    }
    init = _run(env, ["init", "--force"])
    assert init["rc"] == 0, init
    return {"env": env, "db": db, "root": tmp_path}


def _open_session(env: dict) -> dict:
    return _run(
        env,
        [
            "submit",
            "session-open",
            "--payload",
            json.dumps({"slug": "clone-test", "kind": "spec_only"}),
        ],
    )


def test_clone_default_path_produces_valid_sqlite(isolated, tmp_path):
    open_res = _open_session(isolated["env"])
    assert open_res["rc"] == 0, open_res

    res = _run(isolated["env"], ["clone-substrate"])
    assert res["rc"] == 0, res
    clone_path = Path(res["stdout"])
    assert clone_path.exists(), res
    assert clone_path.name.startswith("selvedge-subagent-clone-"), clone_path
    assert clone_path.suffix == ".sqlite", clone_path

    # The clone is a valid SQLite DB carrying the same session row.
    conn = sqlite3.connect(f"file:{clone_path}?mode=ro", uri=True)
    try:
        cnt = conn.execute("SELECT COUNT(*) FROM sessions").fetchone()[0]
    finally:
        conn.close()
    assert cnt == 1, "clone should carry the open session row"

    clone_path.unlink()


def test_clone_to_explicit_path(isolated, tmp_path):
    _open_session(isolated["env"])
    target = tmp_path / "subagent-scratch.sqlite"
    res = _run(isolated["env"], ["clone-substrate", "--to", str(target)])
    assert res["rc"] == 0, res
    assert target.exists()
    assert Path(res["stdout"]) == target.resolve()


def test_clone_isolation_writes_do_not_touch_primary(isolated, tmp_path):
    """codex Q2 strengthening: writes against the clone must not propagate
    to the primary. Spawn a subagent-style subprocess with SELVEDGE_DB_PATH
    pointed at the clone, mutate it, and verify the primary is unchanged."""
    _open_session(isolated["env"])
    primary_sha_before = _sha256(isolated["db"])

    # Take the clone.
    res = _run(isolated["env"], ["clone-substrate"])
    assert res["rc"] == 0, res
    clone_path = Path(res["stdout"])

    # Mutate the clone via a fresh subprocess with SELVEDGE_DB_PATH pointed
    # at the clone, mirroring the subagent dispatch shape.
    subagent_env = isolated["env"] | {"SELVEDGE_DB_PATH": str(clone_path)}
    mutate = _run(
        subagent_env,
        [
            "submit",
            "session-open",
            "--payload",
            json.dumps({"slug": "subagent-mutation", "kind": "meta"}),
        ],
    )
    # The clone already had an open session, so a second open is refused
    # by E_SESSION_ALREADY_OPEN — that refusal itself proves the clone is
    # intact and matches primary state, which is part of the isolation
    # claim. The load-bearing assertion is that the PRIMARY substrate has
    # not changed regardless of clone activity. To prove writes can land
    # against the clone surface, write a sentinel via raw sqlite3 using a
    # write surface (PRAGMA user_version) that bypasses table constraints.
    assert mutate["rc"] != 0 and "E_SESSION_ALREADY_OPEN" in (mutate["err"] + mutate["stdout"]), mutate
    conn = sqlite3.connect(str(clone_path))
    try:
        conn.execute("PRAGMA user_version = 99")
        conn.commit()
    finally:
        conn.close()

    # Primary substrate sha256 must be unchanged.
    primary_sha_after = _sha256(isolated["db"])
    assert primary_sha_before == primary_sha_after, (
        "clone writes leaked into primary: "
        f"{primary_sha_before} != {primary_sha_after}"
    )

    # Read back the clone to confirm the sentinel landed there.
    conn = sqlite3.connect(f"file:{clone_path}?mode=ro", uri=True)
    try:
        clone_uv = conn.execute("PRAGMA user_version").fetchone()[0]
    finally:
        conn.close()
    assert clone_uv == 99, "clone should carry the sentinel pragma"

    # And the primary must NOT carry the sentinel.
    conn = sqlite3.connect(f"file:{isolated['db']}?mode=ro", uri=True)
    try:
        primary_uv = conn.execute("PRAGMA user_version").fetchone()[0]
    finally:
        conn.close()
    assert primary_uv != 99, "primary should not carry clone-only writes"

    clone_path.unlink()


def test_clone_refuses_to_overwrite_primary(isolated):
    _open_session(isolated["env"])
    res = _run(isolated["env"], ["clone-substrate", "--to", str(isolated["db"])])
    assert res["rc"] == 2, res
    assert "E_LIVE_PRIMARY" in res["err"], res


def test_clone_refuses_symlink_to_primary(isolated, tmp_path):
    _open_session(isolated["env"])
    link = tmp_path / "primary-link.sqlite"
    link.symlink_to(isolated["db"])
    res = _run(isolated["env"], ["clone-substrate", "--to", str(link)])
    assert res["rc"] == 2, res
    assert "E_LIVE_PRIMARY" in res["err"], res


def test_clone_refuses_when_dst_is_a_directory(isolated, tmp_path):
    """If --to resolves to an existing directory, sqlite3.connect fails to
    open it as a database file; clone-substrate must surface the failure
    cleanly (rc=2, refusal message) rather than crashing."""
    _open_session(isolated["env"])
    target_dir = tmp_path / "scratch-dir"
    target_dir.mkdir()
    res = _run(isolated["env"], ["clone-substrate", "--to", str(target_dir)])
    assert res["rc"] == 2, res
    assert "refused" in res["err"], res


def test_clone_refuses_corrupt_source(tmp_path):
    """If SELVEDGE_DB_PATH points at a file that is not a valid SQLite
    database, sqlite3.backup() fails inside cmd_clone_substrate; the CLI
    must refuse cleanly without leaving an empty stub at --to."""
    (tmp_path / "MODE.md").write_text("---\nmode: self-development\nworkspace_id: tmp-clone\n---\n")
    mig_dir = tmp_path / "migrations"
    mig_dir.mkdir()
    for src in (WORKSPACE / "state" / "migrations").iterdir():
        if src.suffix == ".sql":
            shutil.copy(src, mig_dir / src.name)
    # Corrupt source: a non-SQLite file at the SELVEDGE_DB_PATH location.
    bad_db = tmp_path / "selvedge.sqlite"
    bad_db.write_bytes(b"NOT A SQLITE FILE - clone must refuse cleanly\n" * 64)
    env = os.environ | {
        "SELVEDGE_WORKSPACE": str(tmp_path),
        "SELVEDGE_DB_PATH": str(bad_db),
        "SELVEDGE_MIGRATIONS_DIR": str(mig_dir),
        "SELVEDGE_SNAPSHOTS_DIR": str(tmp_path / "snapshots"),
    }
    out_path = tmp_path / "should-be-cleaned-up.sqlite"
    res = _run(env, ["clone-substrate", "--to", str(out_path)])
    assert res["rc"] == 2, res
    assert "refused" in res["err"], res
    # Cleanup invariant: failed clone must not leave a non-empty stub at
    # --to. (sqlite3.connect creates the file on connect, but the failure
    # branch in cmd_clone_substrate unlinks it.)
    assert not out_path.exists() or out_path.stat().st_size == 0, (
        "failed clone must clean up its destination stub"
    )


def test_clone_refuses_when_primary_missing(tmp_path):
    """Without a primary substrate at SELVEDGE_DB_PATH, clone-substrate
    refuses with E_NO_SOURCE rather than producing an empty file."""
    (tmp_path / "MODE.md").write_text("---\nmode: self-development\nworkspace_id: tmp-clone\n---\n")
    mig_dir = tmp_path / "migrations"
    mig_dir.mkdir()
    for src in (WORKSPACE / "state" / "migrations").iterdir():
        if src.suffix == ".sql":
            shutil.copy(src, mig_dir / src.name)
    env = os.environ | {
        "SELVEDGE_WORKSPACE": str(tmp_path),
        "SELVEDGE_DB_PATH": str(tmp_path / "does-not-exist.sqlite"),
        "SELVEDGE_MIGRATIONS_DIR": str(mig_dir),
        "SELVEDGE_SNAPSHOTS_DIR": str(tmp_path / "snapshots"),
    }
    res = _run(env, ["clone-substrate"])
    assert res["rc"] == 2, res
    assert "E_NO_SOURCE" in res["err"], res
