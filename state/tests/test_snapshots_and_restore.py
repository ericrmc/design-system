"""L3 boundary snapshots + restore CLI (DV-S081-1, OI-S081-3, OI-S081-4, S084).

Tests run against an isolated substrate under tmp_path so the production
snapshots directory and primary substrate are never touched.

Coverage:
  - take_snapshot fires at session_open + session_close + migrate_apply +
    init_refused + init_forced; row appears in snapshot_catalog with matching
    sha256.
  - restore --to=tempdir happy path with --verify pass.
  - restore --to=primary refuses without --confirm (E_LIVE_PRIMARY exit 2).
  - restore --verify rejects sha256 mismatch (E_VERIFY_MISMATCH).
  - restore --verify rejects missing catalog row (E_NO_CATALOG_ROW).
  - manual snapshot trigger writes both file and catalog row.
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
def isolated(tmp_path):
    """Tmp workspace + tmp snapshots dir; init creates a fresh DB so we can
    exercise every snapshot trigger without touching production paths."""
    (tmp_path / "MODE.md").write_text("---\nmode: self-development\nworkspace_id: tmp-snapshot\n---\n")
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
    return {"env": env, "db": db, "snaps": snaps, "root": tmp_path}


def _open_session(env: dict) -> dict:
    return _run(
        env,
        [
            "submit",
            "session-open",
            "--payload",
            json.dumps({"slug": "snapshot-test", "kind": "spec_only"}),
        ],
    )


def _catalog_rows(db: Path) -> list[dict]:
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    try:
        rows = conn.execute(
            "SELECT * FROM snapshot_catalog ORDER BY snapshot_id"
        ).fetchall()
    finally:
        conn.close()
    return [dict(r) for r in rows]


def test_session_open_fires_snapshot(isolated):
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init
    assert _catalog_rows(isolated["db"]) == [], "no rows expected before any session"

    open_res = _open_session(isolated["env"])
    assert open_res["rc"] == 0, open_res

    rows = _catalog_rows(isolated["db"])
    assert len(rows) == 1, rows
    assert rows[0]["trigger"] == "session_open"
    assert rows[0]["source_session_no"] is not None
    snap_path = Path(rows[0]["path"])
    assert snap_path.exists()
    assert snap_path.parent == isolated["snaps"]
    assert _sha256(snap_path) == rows[0]["sha256"]
    assert rows[0]["sqlite_page_count"] > 0


def test_session_close_fires_snapshot(isolated):
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init
    open_res = _open_session(isolated["env"])
    assert open_res["rc"] == 0, open_res
    wno = open_res["out"]["result"]["workspace_session_no"]

    # Minimal close-record + session-close path; close-record is required by T-39.
    close_rec = _run(
        isolated["env"],
        [
            "submit",
            "close-record",
            "--payload",
            json.dumps(
                {
                    "summary": "snapshot test minimal close-record",
                    "items": [
                        {
                            "facet": "what_was_done",
                            "text": "snapshot test fixture sole item to satisfy T-40",
                        }
                    ],
                }
            ),
        ],
    )
    assert close_rec["rc"] == 0, close_rec

    close_res = _run(
        isolated["env"],
        ["submit", "session-close", "--payload", json.dumps({})],
    )
    assert close_res["rc"] == 0, close_res

    rows = _catalog_rows(isolated["db"])
    triggers = [r["trigger"] for r in rows]
    assert "session_open" in triggers
    assert "session_close" in triggers
    close_row = [r for r in rows if r["trigger"] == "session_close"][-1]
    assert close_row["source_session_no"] == wno
    assert _sha256(Path(close_row["path"])) == close_row["sha256"]


def test_migrate_apply_fires_snapshot(isolated, tmp_path):
    """Apply only migrations 001..041 first, then 042+ on a second pass so we
    exercise the post-apply snapshot path. Easiest setup: copy through 041,
    init, then drop 042 in and run migrate --apply."""
    early_mig = tmp_path / "migrations-early"
    early_mig.mkdir()
    full_mig = Path(isolated["env"]["SELVEDGE_MIGRATIONS_DIR"])
    later: list[Path] = []
    for src in sorted(full_mig.iterdir()):
        if src.suffix != ".sql":
            continue
        # Migrations 001..041 first; 042+ deferred to second pass.
        n = int(src.name.split("-", 1)[0])
        if n <= 41:
            shutil.copy(src, early_mig / src.name)
        else:
            later.append(src)
    early_env = isolated["env"] | {"SELVEDGE_MIGRATIONS_DIR": str(early_mig)}
    init = _run(early_env, ["init", "--force"])
    assert init["rc"] == 0, init
    # After early init, snapshot_catalog table does not yet exist; confirm.
    conn = sqlite3.connect(f"file:{isolated['db']}?mode=ro", uri=True)
    try:
        has = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='snapshot_catalog'"
        ).fetchone()
    finally:
        conn.close()
    assert has is None, "snapshot_catalog should not exist after migrations <= 041"

    # Now apply 042 + later via the production migrations dir.
    res = _run(isolated["env"], ["migrate", "--apply"])
    assert res["rc"] == 0, res

    rows = _catalog_rows(isolated["db"])
    assert len(rows) == 1, rows
    assert rows[0]["trigger"] == "migrate_apply"
    assert _sha256(Path(rows[0]["path"])) == rows[0]["sha256"]


def test_init_refused_fires_snapshot_then_refuses(isolated):
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init
    open_res = _open_session(isolated["env"])
    assert open_res["rc"] == 0, open_res
    pre_rows = _catalog_rows(isolated["db"])

    # Second init --force should refuse AND leave a snapshot row behind.
    refused = _run(isolated["env"], ["init", "--force"])
    assert refused["rc"] == 2, refused
    assert "E_LIVE_SUBSTRATE" in refused["err"]

    post_rows = _catalog_rows(isolated["db"])
    assert len(post_rows) == len(pre_rows) + 1
    assert post_rows[-1]["trigger"] == "init_refused"
    assert _sha256(Path(post_rows[-1]["path"])) == post_rows[-1]["sha256"]


def test_init_forced_fires_snapshot_before_unlink(isolated):
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init
    open_res = _open_session(isolated["env"])
    assert open_res["rc"] == 0, open_res

    forced = _run(isolated["env"], ["init", "--really-force"])
    assert forced["rc"] == 0, forced

    # The init_forced snapshot is on the OLD substrate (now wiped); the file
    # should still be on disk under SELVEDGE_SNAPSHOTS_DIR.
    snap_files = sorted(isolated["snaps"].glob("*-init_forced*.sqlite"))
    assert len(snap_files) >= 1, list(isolated["snaps"].iterdir())
    # The catalog row was written into the OLD substrate (now gone), so the
    # NEW substrate's catalog is empty until the next trigger fires.
    rows = _catalog_rows(isolated["db"])
    assert all(r["trigger"] != "init_forced" for r in rows), rows
    # Verify the snapshot file itself is a valid SQLite database with the old
    # session row preserved.
    snap = snap_files[-1]
    conn = sqlite3.connect(f"file:{snap}?mode=ro", uri=True)
    try:
        cnt = conn.execute("SELECT COUNT(*) FROM sessions").fetchone()[0]
    finally:
        conn.close()
    assert cnt == 1


def test_restore_to_tempdir_with_verify(isolated, tmp_path):
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init
    open_res = _open_session(isolated["env"])
    assert open_res["rc"] == 0, open_res
    rows = _catalog_rows(isolated["db"])
    snap = Path(rows[-1]["path"])

    out = tmp_path / "restored.sqlite"
    res = _run(isolated["env"], ["restore", "--from", str(snap), "--to", str(out), "--verify"])
    assert res["rc"] == 0, res
    assert out.exists()
    assert _sha256(out) == _sha256(snap)


def test_restore_refuses_primary_without_confirm(isolated, tmp_path):
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init
    open_res = _open_session(isolated["env"])
    assert open_res["rc"] == 0, open_res
    rows = _catalog_rows(isolated["db"])
    snap = Path(rows[-1]["path"])

    res = _run(
        isolated["env"],
        ["restore", "--from", str(snap), "--to", str(isolated["db"])],
    )
    assert res["rc"] == 2, res
    assert "E_LIVE_PRIMARY" in res["err"]
    assert "--confirm" in res["err"]


def test_restore_refuses_symlink_to_primary(isolated, tmp_path):
    """RF-S084-17: a --to that is a symlink resolving to the live primary
    must trip E_LIVE_PRIMARY just as a literal --to=primary path would."""
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init
    open_res = _open_session(isolated["env"])
    assert open_res["rc"] == 0, open_res
    rows = _catalog_rows(isolated["db"])
    snap = Path(rows[-1]["path"])

    link = tmp_path / "primary-link.sqlite"
    link.symlink_to(isolated["db"])
    res = _run(isolated["env"], ["restore", "--from", str(snap), "--to", str(link)])
    assert res["rc"] == 2, res
    assert "E_LIVE_PRIMARY" in res["err"]


def test_restore_admits_primary_with_confirm(isolated):
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init
    open_res = _open_session(isolated["env"])
    assert open_res["rc"] == 0, open_res
    rows = _catalog_rows(isolated["db"])
    snap = Path(rows[-1]["path"])

    res = _run(
        isolated["env"],
        ["restore", "--from", str(snap), "--to", str(isolated["db"]), "--confirm"],
    )
    assert res["rc"] == 0, res
    assert _sha256(isolated["db"]) == _sha256(snap)


def test_restore_verify_mismatch(isolated, tmp_path):
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init
    open_res = _open_session(isolated["env"])
    assert open_res["rc"] == 0, open_res
    rows = _catalog_rows(isolated["db"])
    snap = Path(rows[-1]["path"])

    # Corrupt a copy of the snapshot file but keep the catalog pointing at
    # the corrupted path so verify fires E_VERIFY_MISMATCH.
    corrupted = tmp_path / "corrupted-snapshot.sqlite"
    shutil.copy(snap, corrupted)
    with corrupted.open("ab") as f:
        f.write(b"GARBAGE_BYTES_TO_FORCE_SHA_MISMATCH")
    # Insert a catalog row pointing at the corrupted file with the ORIGINAL
    # snapshot sha256 (so the recompute will mismatch).
    conn = sqlite3.connect(str(isolated["db"]))
    try:
        conn.execute(
            "INSERT INTO snapshot_catalog "
            "(trigger, path, sha256, source_db_sha256, sqlite_page_count, "
            " size_bytes, source_session_no, engine_version) "
            "VALUES ('manual', ?, ?, ?, ?, ?, NULL, 'engine-v51')",
            (
                str(corrupted),
                rows[-1]["sha256"],  # original sha256, will not match corrupted file
                rows[-1]["source_db_sha256"],
                rows[-1]["sqlite_page_count"],
                corrupted.stat().st_size,
            ),
        )
        conn.commit()
    finally:
        conn.close()

    out = tmp_path / "restored.sqlite"
    res = _run(
        isolated["env"],
        ["restore", "--from", str(corrupted), "--to", str(out), "--verify"],
    )
    assert res["rc"] == 2, res
    assert "E_VERIFY_MISMATCH" in res["err"]
    assert not out.exists(), "verify failure must short-circuit before copy"


def test_restore_verify_no_catalog_row(isolated, tmp_path):
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init

    # Make a snapshot file by hand that has no catalog row.
    rogue = tmp_path / "rogue-snapshot.sqlite"
    shutil.copy(isolated["db"], rogue)

    out = tmp_path / "restored.sqlite"
    res = _run(
        isolated["env"],
        ["restore", "--from", str(rogue), "--to", str(out), "--verify"],
    )
    assert res["rc"] == 2, res
    assert "E_NO_CATALOG_ROW" in res["err"]


def test_restore_without_verify_skips_catalog(isolated, tmp_path):
    """Without --verify, restore copies the file even if no catalog row exists.
    Operators may legitimately restore from out-of-band snapshots (e.g. a
    pre-migrate-backup) where no catalog row was ever written."""
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init
    rogue = tmp_path / "rogue.sqlite"
    shutil.copy(isolated["db"], rogue)
    out = tmp_path / "restored.sqlite"
    res = _run(isolated["env"], ["restore", "--from", str(rogue), "--to", str(out)])
    assert res["rc"] == 0, res
    assert out.exists()


def test_restore_missing_source(isolated, tmp_path):
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init
    out = tmp_path / "restored.sqlite"
    res = _run(
        isolated["env"],
        ["restore", "--from", str(tmp_path / "does-not-exist.sqlite"), "--to", str(out)],
    )
    assert res["rc"] == 2, res
    assert "does not exist" in res["err"]


def test_dry_run_submit_does_not_snapshot(isolated):
    """Dry-run submit rolls back; no snapshot must be written for either
    session-open or session-close (otherwise we leak boundary anchors that
    the rolled-back substrate state has no rows for)."""
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init
    pre_files = list(isolated["snaps"].iterdir()) if isolated["snaps"].exists() else []

    res = _run(
        isolated["env"],
        [
            "submit",
            "session-open",
            "--dry-run",
            "--payload",
            json.dumps({"slug": "dry-run-test", "kind": "spec_only"}),
        ],
    )
    assert res["rc"] == 0, res
    post_files = list(isolated["snaps"].iterdir()) if isolated["snaps"].exists() else []
    assert post_files == pre_files, (
        "dry-run session-open must not produce a snapshot",
        pre_files,
        post_files,
    )
    rows = _catalog_rows(isolated["db"])
    assert rows == [], rows


def test_manual_snapshot_via_python_api(isolated):
    """take_snapshot('manual') is the operator-visible trigger reserved at v1
    (no CLI exposure yet); the python entrypoint must work for tooling."""
    init = _run(isolated["env"], ["init", "--force"])
    assert init["rc"] == 0, init

    # Run via subprocess so SELVEDGE_SNAPSHOTS_DIR + SELVEDGE_DB_PATH apply.
    code = (
        "from selvedge.snapshots import take_snapshot;"
        "p = take_snapshot('manual');"
        "print(p)"
    )
    proc = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True,
        text=True,
        env=isolated["env"],
        cwd=str(WORKSPACE),
    )
    assert proc.returncode == 0, proc.stderr
    out = proc.stdout.strip()
    assert out, proc.stderr
    snap = Path(out)
    assert snap.exists()
    rows = _catalog_rows(isolated["db"])
    assert any(r["trigger"] == "manual" for r in rows), rows
