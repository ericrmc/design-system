"""Pytest fixtures for Selvedge substrate tests.

Per-test fixtures point `SELVEDGE_DB_PATH` and `SELVEDGE_SNAPSHOTS_DIR` at an
ephemeral tmp directory so the workspace's primary substrate
(`state/selvedge.sqlite`) is never touched during pytest runs. The legacy
`_snapshot_primary` save/restore is removed; a session-scoped sha256 guard
catches any leakage that lands despite the per-test isolation.

Public fixture surface:
- `db_path` — Path to the per-test ephemeral substrate file.
- `clean_substrate` — Returns session_id of a freshly-init'd S001 in the
  ephemeral substrate. Backward-compatible signature with the pre-S206
  fixture; internals point at tmp DB.
- `db` — sqlite3.Connection on the ephemeral substrate.
- `selvedge_cli` — callable for CLI subprocess invocations.
- `submit_minimal_close_record`, `open_deliberation` — helpers.

S206 / DV-S206-1 / OI-S205-1 closure.
"""
from __future__ import annotations

import hashlib
import json
import os
import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest

WORKSPACE = Path(__file__).resolve().parents[2]
PRIMARY_DB = WORKSPACE / "state" / "selvedge.sqlite"
BIN = WORKSPACE / "bin" / "selvedge"

if str(WORKSPACE) not in sys.path:
    sys.path.insert(0, str(WORKSPACE))


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


def _sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


@pytest.fixture(scope="session", autouse=True)
def _primary_substrate_leakage_guard():
    """Session-scoped sha256 guard on the workspace primary substrate.

    Replaces the pre-S206 `_snapshot_primary` copy/restore (DV-S206-1,
    OI-S205-1). Per-test fixtures point SELVEDGE_DB_PATH at a tmp file, so
    the primary should be untouched across the full test session. If the
    sha changes, the session fails with a diagnostic.
    """
    pre = _sha256(PRIMARY_DB) if PRIMARY_DB.exists() else None
    yield
    post = _sha256(PRIMARY_DB) if PRIMARY_DB.exists() else None
    if pre != post:
        raise AssertionError(
            "primary substrate sha256 changed during pytest run: "
            f"pre={pre} post={post} at {PRIMARY_DB} — a test wrote to "
            "the primary substrate; check db_path / clean_substrate fixture "
            "usage in any test that connects via sqlite3 directly."
        )


@pytest.fixture(autouse=True)
def db_path(tmp_path, monkeypatch):
    """Per-test ephemeral substrate path.

    Sets SELVEDGE_DB_PATH and SELVEDGE_SNAPSHOTS_DIR in os.environ for the
    duration of the test so subprocess CLI invocations route ALL writes
    away from the workspace primary. Returns the Path to the tmp DB so
    tests doing direct `sqlite3.connect(...)` use the same file.

    Autouse so even tests that don't request db_path explicitly get the
    env override — defence-in-depth against the S204 leakage class.
    Tests that build their own isolated workspace (test_clone_substrate,
    test_engine_v52_marker, test_init_guard, test_manifest_reconcile,
    test_migrate, test_snapshots_and_restore) override SELVEDGE_DB_PATH
    in their own subprocess `extra_env`, so autouse here does not
    interfere with those flows.
    """
    db = tmp_path / "selvedge.sqlite"
    snaps = tmp_path / "snapshots"
    snaps.mkdir()
    monkeypatch.setenv("SELVEDGE_DB_PATH", str(db))
    monkeypatch.setenv("SELVEDGE_SNAPSHOTS_DIR", str(snaps))
    # Hard refusal if a fixture mistake routed db_path back to primary.
    if db.resolve() == PRIMARY_DB.resolve():
        raise AssertionError(
            f"db_path fixture resolved to primary substrate: {db} == {PRIMARY_DB}"
        )
    return db


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
def clean_substrate(db_path):
    """Reset substrate to post-init + S001-open. Returns the session_id.

    Backed by a per-test tmp DB via SELVEDGE_DB_PATH (S206 DV-S206-1,
    OI-S205-1 closure). The previous PRIMARY_DB sidecar-unlink + init dance
    is removed because the tmp DB starts empty and is discarded with
    `tmp_path` cleanup. The L1a init-guard refusal of `init --force`
    against carrying-sessions substrate (DV-S081-1) is preserved at the
    primary scope by the session-level sha256 guard above; the per-test
    init runs against an empty tmp file where the L1a guard admits.
    """
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
                    # Default fixture kind is spec_only so close paths do not
                    # require a clean review_pass via t30 (engine-v31, S104).
                    # Tests that need to exercise coding-review semantics open
                    # their own kind=coding session.
                    "kind": "spec_only",
                }
            ),
        ]
    )
    assert open_res["out"]["ok"], open_res
    return open_res["out"]["result"]["session_id"]


def _submit_minimal_close_record(session_no: int = 1) -> dict:
    """Submit a minimal close-record so tests can exercise session-close
    without tripping T-39 (engine-v41, DV-S134-1) or T-40 (engine-v44,
    DV-S153-1). The clean_substrate fixture applies all migrations, so tests
    run against the latest engine-version on disk; this fixture's items[]
    shape must satisfy the strictest gate currently applied. T-40 requires
    at least one close_state_items row, so the fixture carries one
    well-formed item; the empty-items[] shape that sufficed under T-39
    alone is now refused at the handler pre-check. If a future engine bump
    raises the threshold above 1 (e.g. per-facet coverage R-1.1), this
    fixture must be widened to match — otherwise tests passing here would
    not exercise session-close under the deployed gate."""
    return _run_cli(
        [
            "submit",
            "close-record",
            "--payload",
            json.dumps(
                {
                    "session_no": session_no,
                    "summary": "pytest minimal close-record for T-39 plus T-40 prerequisite",
                    "items": [
                        {
                            "facet": "what_was_done",
                            "text": "pytest minimal close-record fixture sole item to satisfy T-40",
                        }
                    ],
                }
            ),
        ],
    )


@pytest.fixture
def submit_minimal_close_record():
    return _submit_minimal_close_record


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
def db(db_path, clean_substrate):
    """Read-only sqlite3.Connection on the per-test ephemeral substrate.
    Used by tests that need to inspect rows or attempt direct mutations to
    verify trigger refusals from the SQL layer."""
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()
