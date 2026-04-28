"""Pytest fixtures for Selvedge substrate tests.

Each test runs against a clean substrate. We snapshot the workspace's primary
substrate at test-session start and restore on teardown, so production state is
not polluted. Inside the test session, tests get a `clean_substrate` fixture that
re-inits the substrate via `selvedge init --force` and then opens a session-1
row so deliberation/perspective/synthesis tests have a parent session to attach
to. The `selvedge_cli` fixture returns a callable that runs the CLI in a
subprocess and parses the JSON result.
"""
from __future__ import annotations

import json
import os
import shutil
import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest

WORKSPACE = Path(__file__).resolve().parents[2]
PRIMARY_DB = WORKSPACE / "state" / "selvedge.sqlite"
BACKUP_DB = WORKSPACE / "state" / "selvedge.sqlite.pytest-backup"
BIN = WORKSPACE / "bin" / "selvedge"

# Make the in-tree `selvedge` package importable so unit tests can call helpers
# (e.g., the T-15 parser) directly without going through the CLI subprocess.
if str(WORKSPACE) not in sys.path:
    sys.path.insert(0, str(WORKSPACE))


@pytest.fixture(scope="session", autouse=True)
def _snapshot_primary():
    """Back up the primary substrate before tests, restore after."""
    if PRIMARY_DB.exists():
        shutil.copy(PRIMARY_DB, BACKUP_DB)
    try:
        yield
    finally:
        for sidecar in [PRIMARY_DB, PRIMARY_DB.with_suffix(".sqlite-wal"), PRIMARY_DB.with_suffix(".sqlite-shm")]:
            if sidecar.exists():
                sidecar.unlink()
        if BACKUP_DB.exists():
            shutil.move(BACKUP_DB, PRIMARY_DB)


_TESTS_DIR = Path(__file__).resolve().parent


def _coverage_active() -> bool:
    """True iff a coverage measurement is in progress in this pytest run.
    Detection is via `coverage.Coverage.current()` because pytest-cov 7.x no
    longer exports a COV_CORE_* env marker we can sniff."""
    try:
        import coverage  # type: ignore
    except ImportError:
        return False
    return coverage.Coverage.current() is not None


def _coverage_subprocess_env() -> dict:
    """Return env additions that make CLI subprocess invocations contribute to
    coverage measurement. The shim in `state/tests/sitecustomize.py` calls
    `coverage.process_startup()` when COVERAGE_PROCESS_START is set."""
    if not _coverage_active():
        return {}
    extra = {"COVERAGE_PROCESS_START": str(WORKSPACE / "pyproject.toml")}
    existing = os.environ.get("PYTHONPATH", "")
    parts = [str(_TESTS_DIR)]
    if existing:
        parts.append(existing)
    extra["PYTHONPATH"] = os.pathsep.join(parts)
    return extra


def _run_cli(args: list[str], *, expect_ok: bool = True, input_payload: dict | None = None) -> dict:
    env = os.environ | {"SELVEDGE_WORKSPACE": str(WORKSPACE)} | _coverage_subprocess_env()
    # Under coverage, route through the venv's interpreter (which has the
    # `coverage` package installed and the sitecustomize shim on PYTHONPATH)
    # rather than the bash shim's `python3`, which resolves to system Python
    # and would not contribute to the coverage report.
    proc = subprocess.run(
        [str(BIN), *args],
        capture_output=True,
        text=True,
        env=env,
        input=json.dumps(input_payload) if input_payload is not None else None,
    )
    out = (proc.stdout or "").strip()
    err = (proc.stderr or "").strip()
    payload = None
    if out:
        try:
            payload = json.loads(out)
        except json.JSONDecodeError:
            payload = {"_raw": out}
    if expect_ok and proc.returncode != 0:
        raise AssertionError(f"CLI failed: {args}\nrc={proc.returncode}\nstdout={out}\nstderr={err}")
    return {"rc": proc.returncode, "out": payload, "err": err}


@pytest.fixture
def selvedge_cli():
    return _run_cli


@pytest.fixture
def clean_substrate():
    """Reset substrate to post-init + S001-open. Returns the session_id."""
    for sidecar in [PRIMARY_DB, PRIMARY_DB.with_suffix(".sqlite-wal"), PRIMARY_DB.with_suffix(".sqlite-shm")]:
        if sidecar.exists():
            sidecar.unlink()
    init = _run_cli(["init", "--force"])
    assert init["rc"] == 0, init
    # `selvedge init` chains the migrate runner since engine-v18 (S082); this
    # call is a defence-in-depth no-op that proves the substrate is fully
    # migrated before any test row is written. If a future migration regresses
    # init's auto-apply, this surfaces it at fixture-time rather than via a
    # mid-test trigger absence.
    migrate = _run_cli(["migrate", "--apply"])
    assert migrate["rc"] == 0, migrate
    open_res = _run_cli(
        [
            "submit",
            "session-open",
            "--payload",
            json.dumps(
                {
                    "session_no": 1,
                    "slug": "pytest",
                    "mode": "self-development",
                    "workspace_id": "selvedge-self-development",
                    "engine_version_at_open": "engine-v17",
                }
            ),
        ]
    )
    assert open_res["out"]["ok"], open_res
    return open_res["out"]["result"]["session_id"]


@pytest.fixture
def open_deliberation(clean_substrate):
    """Open a deliberation in the clean S001 substrate. Returns deliberation_id."""
    res = _run_cli(
        [
            "submit",
            "deliberation-open",
            "--payload",
            json.dumps({"session_no": 1, "topic": "pytest deliberation"}),
        ]
    )
    return res["out"]["result"]["deliberation_id"]


@pytest.fixture
def db():
    """Read-only sqlite3.Connection on the primary substrate (used by tests
    that need to inspect or directly attempt mutations to verify trigger
    refusals from the SQL layer)."""
    conn = sqlite3.connect(str(PRIMARY_DB))
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()
