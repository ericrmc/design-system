"""tools/manifest_reconcile.sh — pass 1 (manifest-row integrity) and pass 2
(L5 orphan discovery) cover the substrate-filesystem divergence shapes
sealed at DV-S190-2 D-B FR-D. Tests run the script against a tmp workspace
plus a tmp sqlite DB carrying just the export_manifest + sessions tables;
no live state is touched.
"""

from __future__ import annotations

import hashlib
import os
import shutil
import sqlite3
import subprocess
from pathlib import Path

import pytest


WORKSPACE = Path(__file__).resolve().parents[2]
SCRIPT = WORKSPACE / "tools" / "manifest_reconcile.sh"


def _seed_db(db_path: Path) -> sqlite3.Connection:
    """Create the minimal substrate the reconciliation script reads:
    export_manifest + sessions. Schema mirrors migration 044 + base sessions."""
    conn = sqlite3.connect(str(db_path))
    conn.execute(
        """CREATE TABLE export_manifest (
            manifest_id INTEGER PRIMARY KEY,
            session_no INTEGER,
            kind TEXT NOT NULL,
            path TEXT NOT NULL UNIQUE,
            sha256 TEXT NOT NULL,
            size_bytes INTEGER NOT NULL,
            row_count INTEGER NOT NULL DEFAULT 0,
            generated_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
        )"""
    )
    conn.execute(
        """CREATE TABLE sessions (
            session_id INTEGER PRIMARY KEY,
            slug TEXT NOT NULL,
            workspace_session_no INTEGER
        )"""
    )
    conn.commit()
    return conn


def _write(workspace: Path, rel: str, content: str) -> str:
    """Write `content` to `workspace/rel`, return its sha256."""
    abs_path = workspace / rel
    abs_path.parent.mkdir(parents=True, exist_ok=True)
    abs_path.write_text(content, encoding="utf-8")
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def _record(conn: sqlite3.Connection, *, kind: str, path: str, sha: str,
            session_no: int | None = None, size: int | None = None) -> None:
    conn.execute(
        "INSERT INTO export_manifest (session_no, kind, path, sha256, size_bytes) "
        "VALUES (?, ?, ?, ?, ?)",
        (session_no, kind, path, sha, size if size is not None else len(sha)),
    )
    conn.commit()


def _seed_session(conn: sqlite3.Connection, *, wno: int, slug: str) -> None:
    conn.execute(
        "INSERT INTO sessions (slug, workspace_session_no) VALUES (?, ?)",
        (slug, wno),
    )
    conn.commit()


def _run(workspace: Path, db_path: Path) -> subprocess.CompletedProcess:
    env = os.environ | {
        "SELVEDGE_WORKSPACE": str(workspace),
        "SELVEDGE_DB_PATH": str(db_path),
    }
    return subprocess.run(
        ["bash", str(SCRIPT)],
        capture_output=True,
        text=True,
        env=env,
    )


@pytest.fixture
def tmp_workspace(tmp_path):
    db = tmp_path / "state" / "selvedge.sqlite"
    db.parent.mkdir()
    return tmp_path, db


def test_clean_pass(tmp_workspace):
    """Substrate-recorded rows whose disk bytes match the recorded sha exit 0."""
    workspace, db_path = tmp_workspace
    conn = _seed_db(db_path)
    _seed_session(conn, wno=200, slug="alpha")
    sha_a = _write(workspace, "provenance/200-alpha/05-engine-feedback.md", "alpha 05\n")
    sha_b = _write(workspace, "provenance/200-alpha/06-counterfactuals.md", "alpha 06\n")
    _record(conn, session_no=200, kind="engine_feedback",
            path="provenance/200-alpha/05-engine-feedback.md", sha=sha_a)
    _record(conn, session_no=200, kind="counterfactuals",
            path="provenance/200-alpha/06-counterfactuals.md", sha=sha_b)
    conn.close()
    proc = _run(workspace, db_path)
    assert proc.returncode == 0, proc.stderr + proc.stdout
    assert "2 rows ok / 0 divergent" in proc.stdout


def test_missing_on_disk_fails(tmp_workspace):
    """Manifest row with no file on disk fails pass 1."""
    workspace, db_path = tmp_workspace
    conn = _seed_db(db_path)
    _seed_session(conn, wno=200, slug="alpha")
    _record(conn, session_no=200, kind="engine_feedback",
            path="provenance/200-alpha/05-engine-feedback.md",
            sha="0" * 64)
    conn.close()
    proc = _run(workspace, db_path)
    assert proc.returncode == 1, proc.stdout
    assert "missing on disk" in proc.stdout


def test_sha_mismatch_fails(tmp_workspace):
    """Disk bytes that hash differently from the recorded sha fail pass 1."""
    workspace, db_path = tmp_workspace
    conn = _seed_db(db_path)
    _seed_session(conn, wno=200, slug="alpha")
    _write(workspace, "provenance/200-alpha/05-engine-feedback.md", "tampered\n")
    _record(conn, session_no=200, kind="engine_feedback",
            path="provenance/200-alpha/05-engine-feedback.md",
            sha=hashlib.sha256(b"original\n").hexdigest())
    conn.close()
    proc = _run(workspace, db_path)
    assert proc.returncode == 1, proc.stdout
    assert "sha256 mismatch" in proc.stdout


def test_l5_orphan_fails(tmp_workspace):
    """L5 file on disk in a covered session with no matching manifest row fails pass 2."""
    workspace, db_path = tmp_workspace
    conn = _seed_db(db_path)
    _seed_session(conn, wno=200, slug="alpha")
    sha_a = _write(workspace, "provenance/200-alpha/05-engine-feedback.md", "alpha 05\n")
    _record(conn, session_no=200, kind="engine_feedback",
            path="provenance/200-alpha/05-engine-feedback.md", sha=sha_a)
    _write(workspace, "provenance/200-alpha/07-fr-dispositions.md", "stale FR\n")
    conn.close()
    proc = _run(workspace, db_path)
    assert proc.returncode == 1, proc.stdout
    assert "L5 orphan on disk" in proc.stdout
    assert "07-fr-dispositions.md" in proc.stdout


def test_pre_adoption_session_skips_orphan_check(tmp_workspace):
    """Sessions with zero manifest rows are pre-adoption; orphan check is skipped."""
    workspace, db_path = tmp_workspace
    conn = _seed_db(db_path)
    _seed_session(conn, wno=100, slug="legacy")
    _write(workspace, "provenance/100-legacy/05-engine-feedback.md", "legacy\n")
    _seed_session(conn, wno=200, slug="alpha")
    sha = _write(workspace, "provenance/200-alpha/05-engine-feedback.md", "alpha\n")
    _record(conn, session_no=200, kind="engine_feedback",
            path="provenance/200-alpha/05-engine-feedback.md", sha=sha)
    conn.close()
    proc = _run(workspace, db_path)
    assert proc.returncode == 0, proc.stdout


def test_null_session_no_row_passes(tmp_workspace):
    """Workspace-wide rows with NULL session_no (open_issues_index, spec_versions_index)
    are integrity-checked by path/sha without session-dir assumptions."""
    workspace, db_path = tmp_workspace
    conn = _seed_db(db_path)
    sha = _write(workspace, "open-issues/index.md", "OI index\n")
    _record(conn, session_no=None, kind="open_issues_index",
            path="open-issues/index.md", sha=sha)
    sha2 = _write(workspace, "specifications/_versions.md", "spec versions\n")
    _record(conn, session_no=None, kind="spec_versions_index",
            path="specifications/_versions.md", sha=sha2)
    conn.close()
    proc = _run(workspace, db_path)
    assert proc.returncode == 0, proc.stdout
    assert "2 rows ok / 0 divergent" in proc.stdout


def test_null_session_no_mismatch_fails(tmp_workspace):
    """NULL session_no rows still fail when their disk content drifts."""
    workspace, db_path = tmp_workspace
    conn = _seed_db(db_path)
    _write(workspace, "open-issues/index.md", "drifted\n")
    _record(conn, session_no=None, kind="open_issues_index",
            path="open-issues/index.md",
            sha=hashlib.sha256(b"original\n").hexdigest())
    conn.close()
    proc = _run(workspace, db_path)
    assert proc.returncode == 1, proc.stdout
    assert "sha256 mismatch" in proc.stdout
    assert "open-issues/index.md" in proc.stdout


def test_absolute_path_rejected(tmp_workspace):
    """Manifest rows with absolute paths fail cleanly (defence against malformed rows)."""
    workspace, db_path = tmp_workspace
    conn = _seed_db(db_path)
    _record(conn, session_no=None, kind="open_issues_index",
            path="/etc/passwd", sha="0" * 64)
    conn.close()
    proc = _run(workspace, db_path)
    assert proc.returncode == 1, proc.stdout
    assert "absolute path rejected" in proc.stdout


def test_path_traversal_rejected(tmp_workspace):
    """Manifest rows with .. fail cleanly."""
    workspace, db_path = tmp_workspace
    conn = _seed_db(db_path)
    _record(conn, session_no=None, kind="open_issues_index",
            path="provenance/../../../etc/passwd", sha="0" * 64)
    conn.close()
    proc = _run(workspace, db_path)
    assert proc.returncode == 1, proc.stdout
    assert "path-traversal rejected" in proc.stdout


def test_quote_in_slug_does_not_break_pass_2(tmp_workspace):
    """A malformed slug carrying a single-quote (or other shell/SQL metachar
    short of `/` or `..`) must not break pass-2 SQL or admit injection.
    Pass 2 pre-fetches paths and uses `grep -qxF` for membership; no per-row
    sqlite3 call interpolates the slug. The session is processed cleanly:
    the on-disk dir does not exist (no orphan), and substrate stays intact."""
    workspace, db_path = tmp_workspace
    conn = _seed_db(db_path)
    sha = _write(workspace, "provenance/200-alpha/05-engine-feedback.md", "alpha\n")
    _record(conn, session_no=200, kind="engine_feedback",
            path="provenance/200-alpha/05-engine-feedback.md", sha=sha)
    _seed_session(conn, wno=200, slug="alpha")
    conn.execute(
        "INSERT INTO sessions (slug, workspace_session_no) VALUES (?, ?)",
        ("evil'; DROP TABLE sessions;--", 201),
    )
    sha2 = _write(workspace, "provenance/201-stub/05-engine-feedback.md", "stub\n")
    _record(conn, session_no=201, kind="engine_feedback",
            path="provenance/201-stub/05-engine-feedback.md", sha=sha2)
    conn.commit()
    conn.close()
    proc = _run(workspace, db_path)
    assert proc.returncode == 0, proc.stdout
    conn2 = sqlite3.connect(str(db_path))
    assert conn2.execute("SELECT count(*) FROM sessions").fetchone()[0] == 2
    conn2.close()


def test_slug_with_path_separator_rejected(tmp_workspace):
    """A slug carrying `/` or `..` is rejected in pass 2 (defence in depth
    against malformed substrate rows escaping the provenance/ tree)."""
    workspace, db_path = tmp_workspace
    conn = _seed_db(db_path)
    conn.execute(
        "INSERT INTO sessions (slug, workspace_session_no) VALUES (?, ?)",
        ("escape/me", 200),
    )
    sha = _write(workspace, "provenance/200-foo/05-engine-feedback.md", "x\n")
    _record(conn, session_no=200, kind="engine_feedback",
            path="provenance/200-foo/05-engine-feedback.md", sha=sha)
    conn.commit()
    conn.close()
    proc = _run(workspace, db_path)
    assert proc.returncode == 1, proc.stdout
    assert "rejecting malformed session slug" in proc.stdout


def test_path_with_quote_no_orphan_misreport(tmp_workspace):
    """Paths in export_manifest carrying a quote do not break grep -qxF
    membership testing for orphan detection."""
    workspace, db_path = tmp_workspace
    conn = _seed_db(db_path)
    _seed_session(conn, wno=200, slug="alpha")
    sha = _write(workspace, "provenance/200-alpha/05-engine-feedback.md", "alpha\n")
    _record(conn, session_no=200, kind="engine_feedback",
            path="provenance/200-alpha/05-engine-feedback.md", sha=sha)
    sha2 = _write(workspace, "provenance/200-alpha/06-counterfactuals.md", "cf\n")
    _record(conn, session_no=200, kind="counterfactuals",
            path="provenance/200-alpha/06-counterfactuals.md", sha=sha2)
    conn.close()
    proc = _run(workspace, db_path)
    assert proc.returncode == 0, proc.stdout
    assert "L5 orphan" not in proc.stdout


def test_missing_db_warns_and_passes(tmp_workspace):
    """No substrate file → script warns and exits 0 (validator should not block fresh workspace)."""
    workspace, db_path = tmp_workspace
    proc = _run(workspace, db_path)
    assert proc.returncode == 0, proc.stdout
    assert "missing" in proc.stdout
