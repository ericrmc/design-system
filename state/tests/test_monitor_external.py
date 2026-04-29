"""Tests for `bin/selvedge monitor-external` (engine-v31, OI-S106-2 / DV-S106-3).

The CLI surface is generic across external workspaces; tests use a peer
workspace built in tmp_path. The peer's substrate is initialised by running
`bin/selvedge init` with SELVEDGE_WORKSPACE pointing at the temporary
directory and SELVEDGE_MIGRATIONS_DIR pointing at the live migrations.

The harvest-ef path writes engine_feedback rows to *this* workspace's
substrate — `clean_substrate` from conftest provides isolation by snapshotting
PRIMARY_DB at session-start and restoring it at teardown.
"""
from __future__ import annotations

import json
import os
import sqlite3
import subprocess
from pathlib import Path

import pytest

from conftest import BIN, PRIMARY_DB, WORKSPACE, _coverage_subprocess_env


def _run_external_cli(args: list[str], *, cwd: Path | None = None,
                       extra_env: dict | None = None) -> subprocess.CompletedProcess:
    env = os.environ | _coverage_subprocess_env()
    if extra_env:
        env.update(extra_env)
    return subprocess.run(
        [str(BIN), *args],
        capture_output=True, text=True, env=env, cwd=str(cwd) if cwd else None,
    )


def _bootstrap_peer(peer_root: Path) -> Path:
    """Initialise a fresh substrate at peer_root and write a minimal MODE.md.

    Returns peer_root for chaining. The peer inherits migration 011's seed
    workspace_metadata (workspace_id=selvedge-self-development, mode=...)
    because we don't run the bootstrap script here — that is the operator's
    job in real use. For tests we only need substrate validity.
    """
    peer_root.mkdir(parents=True, exist_ok=True)
    (peer_root / "MODE.md").write_text("mode: external-problem\n")
    state = peer_root / "state"
    state.mkdir(exist_ok=True)
    proc = _run_external_cli(
        ["init"],
        extra_env={
            "SELVEDGE_WORKSPACE": str(peer_root),
            "SELVEDGE_MIGRATIONS_DIR": str(WORKSPACE / "state" / "migrations"),
        },
    )
    assert proc.returncode == 0, f"peer init failed: {proc.stderr}"
    return peer_root


def _peer_submit(peer_root: Path, kind: str, payload: dict) -> dict:
    proc = _run_external_cli(
        ["submit", kind, "--payload", json.dumps(payload)],
        extra_env={
            "SELVEDGE_WORKSPACE": str(peer_root),
            "SELVEDGE_MIGRATIONS_DIR": str(WORKSPACE / "state" / "migrations"),
        },
    )
    assert proc.returncode == 0, f"peer submit {kind} failed: {proc.stderr}"
    return json.loads(proc.stdout)["result"]


@pytest.fixture
def peer_workspace(tmp_path):
    """Tmp peer workspace with a closed S001 close-record fixture."""
    peer = _bootstrap_peer(tmp_path / "peer")
    _peer_submit(peer, "session-open", {"slug": "smoke-001", "kind": "spec_only"})
    _peer_submit(peer, "assessment", {
        "state": "peer fixture state seeded for monitor-external tests.",
        "agenda": ["seed agenda atom one for the test fixture."],
    })
    _peer_submit(peer, "close-record", {
        "summary": "peer fixture close-record for monitor-external coverage.",
        "items": [
            {"facet": "engine_version", "text": "engine-v31 to engine-v31, no bump."},
            {"facet": "what_was_done", "text": "seeded peer substrate for tests."},
            {"facet": "state_at_close", "text": "peer substrate populated cleanly."},
            {"facet": "open_issues", "text": "no open issues recorded in fixture."},
            {"facet": "next_session_should", "text": "carry-forward atom one for tests."},
            {"facet": "next_session_should", "text": "carry-forward atom two for tests."},
            {"facet": "validator_summary", "text": "validator not exercised in fixture."},
        ],
    })
    _peer_submit(peer, "session-close", {})
    return peer


# NOTE: the `_seed_ef_files` helper and 8 tests that exercised the
# md-glob harvest-ef model were removed in S121 because S110 rewrote
# harvest-ef to read peer engine_feedback rows substrate-direct. The
# substrate-direct test coverage is tracked by OI-S121-1.


# ---------------------------------------------------------------------------
# refusals
# ---------------------------------------------------------------------------


def test_status_refuses_missing_workspace(selvedge_cli, tmp_path):
    res = selvedge_cli(
        ["monitor-external", "status", "--workspace", str(tmp_path / "nope")],
        expect_ok=False,
    )
    assert res["rc"] == 3
    err = json.loads(res["err"])
    assert err["code"] == "E_NO_WORKSPACE"
    assert "does not exist" in err["detail"]


def test_status_refuses_missing_mode_md(selvedge_cli, tmp_path):
    (tmp_path / "state").mkdir()
    (tmp_path / "state" / "selvedge.sqlite").write_text("not a real db")
    res = selvedge_cli(
        ["monitor-external", "status", "--workspace", str(tmp_path)],
        expect_ok=False,
    )
    assert res["rc"] == 3
    err = json.loads(res["err"])
    assert err["code"] == "E_NO_WORKSPACE"
    assert "MODE.md" in err["detail"]


def test_status_refuses_missing_substrate(selvedge_cli, tmp_path):
    (tmp_path / "MODE.md").write_text("mode: external-problem\n")
    res = selvedge_cli(
        ["monitor-external", "status", "--workspace", str(tmp_path)],
        expect_ok=False,
    )
    assert res["rc"] == 3
    err = json.loads(res["err"])
    assert err["code"] == "E_NO_WORKSPACE"
    assert "substrate" in err["detail"]


def test_status_refuses_self_workspace(selvedge_cli):
    res = selvedge_cli(
        ["monitor-external", "status", "--workspace", str(WORKSPACE)],
        expect_ok=False,
    )
    assert res["rc"] == 3
    err = json.loads(res["err"])
    assert err["code"] == "E_REFUSAL_SELF"


# ---------------------------------------------------------------------------
# status
# ---------------------------------------------------------------------------


def test_status_emits_markdown_packet(clean_substrate, selvedge_cli, peer_workspace):
    res = selvedge_cli(["monitor-external", "status", "--workspace", str(peer_workspace)])
    assert res["rc"] == 0
    md = res["out"]["_raw"] if "_raw" in res["out"] else json.dumps(res["out"])
    # Markdown rendering produces specific section headings.
    assert "# monitor-external status" in md
    assert "## Recent sessions" in md
    assert "## Open issues" in md
    assert "## Engine-feedback (peer substrate, last 10)" in md
    assert "## Latest close-record next_session_should" in md
    assert "## Phase heuristic" in md
    assert "smoke-001" in md
    assert "carry-forward atom one for tests." in md


def test_status_emits_json_packet(clean_substrate, selvedge_cli, peer_workspace):
    res = selvedge_cli(["monitor-external", "status", "--workspace", str(peer_workspace), "--json"])
    assert res["rc"] == 0
    pkt = res["out"]
    assert pkt["workspace_path"].endswith("peer")
    assert pkt["workspace_metadata"]["current_engine_version"].startswith("engine-v")
    assert pkt["recent_sessions"][0]["slug"] == "smoke-001"
    assert pkt["recent_sessions"][0]["status"] == "closed"
    assert pkt["latest_close"]["next_session_should"] == [
        "carry-forward atom one for tests.",
        "carry-forward atom two for tests.",
    ]
    assert pkt["phase_heuristic"]["value"] == "P0"
    # S110 substrate-direct harvest-ef: status now reads peer engine_feedback
    # rows directly. Empty peer substrate returns ef_rows=[] (table exists but
    # no rows); a peer without the table returns ef_rows=None.
    assert pkt["ef_rows"] == []


def test_status_phase_heuristic_respects_sessions_per_phase(
    clean_substrate, selvedge_cli, peer_workspace,
):
    # peer fixture has 1 closed session → session_no=1; with default 3-per-phase
    # this is P0. Override to 1-per-phase → still P0 (since (1-1)//1=0).
    res = selvedge_cli([
        "monitor-external", "status", "--workspace", str(peer_workspace),
        "--json", "--sessions-per-phase", "1",
    ])
    assert res["out"]["phase_heuristic"]["sessions_per_phase"] == 1
    assert res["out"]["phase_heuristic"]["value"] == "P0"


# ---------------------------------------------------------------------------
# next-input
# ---------------------------------------------------------------------------


def test_next_input_carries_close_record_atoms(
    clean_substrate, selvedge_cli, peer_workspace,
):
    res = selvedge_cli([
        "monitor-external", "next-input",
        "--workspace", str(peer_workspace),
        "--phase", "P-1",
    ])
    assert res["rc"] == 0
    out = res["out"]
    assert out["phase"] == "P-1"
    assert out["next_external_session_no"] == 2
    assert out["latest_close"]["next_session_should"] == [
        "carry-forward atom one for tests.",
        "carry-forward atom two for tests.",
    ]
    assert out["draft_session_input"]["carry_forward_from_close"] == \
        out["latest_close"]["next_session_should"]
    assert "operator_must_fill" in out["draft_session_input"]


def test_next_input_embeds_arc_plan_when_passed(
    clean_substrate, selvedge_cli, peer_workspace, tmp_path,
):
    arc = tmp_path / "arc-plan.md"
    arc.write_text("# Arc-plan v2\n\nPhase P-1 stub goes here.\n")
    res = selvedge_cli([
        "monitor-external", "next-input",
        "--workspace", str(peer_workspace),
        "--arc-plan", str(arc),
        "--phase", "P-1",
    ])
    assert res["rc"] == 0
    assert res["out"]["arc_plan_path"].endswith("arc-plan.md")
    assert "Phase P-1 stub" in res["out"]["arc_plan_excerpt"]


def test_next_input_writes_to_out_path(
    clean_substrate, selvedge_cli, peer_workspace, tmp_path,
):
    out_file = tmp_path / "draft.json"
    res = selvedge_cli([
        "monitor-external", "next-input",
        "--workspace", str(peer_workspace),
        "--phase", "P-1",
        "--out", str(out_file),
    ])
    assert res["rc"] == 0
    assert res["out"]["wrote"] == str(out_file.resolve())
    assert out_file.exists()
    payload = json.loads(out_file.read_text())
    assert payload["phase"] == "P-1"


def test_next_input_refuses_missing_arc_plan(
    clean_substrate, selvedge_cli, peer_workspace, tmp_path,
):
    res = selvedge_cli([
        "monitor-external", "next-input",
        "--workspace", str(peer_workspace),
        "--arc-plan", str(tmp_path / "nope.md"),
    ], expect_ok=False)
    assert res["rc"] == 3
    err = json.loads(res["err"])
    assert err["code"] == "E_NO_FILE"


# ---------------------------------------------------------------------------
# harvest-ef
# ---------------------------------------------------------------------------


def test_harvest_ef_refuses_without_explicit_self_workspace_env(
    clean_substrate, peer_workspace, tmp_path,
):
    """Iter-3 F-92 guard: refuse harvest-ef when SELVEDGE_WORKSPACE is unset.
    Without the env var, workspace_root() walks cwd upward and could land in
    any peer that happens to have a MODE.md, routing writes to the wrong
    substrate. Demonstrate by running with cwd in a third workspace and no
    SELVEDGE_WORKSPACE set."""
    third = _bootstrap_peer(tmp_path / "third")
    env = os.environ.copy()
    env.pop("SELVEDGE_WORKSPACE", None)
    env["PYTHONPATH"] = str(WORKSPACE)
    proc = subprocess.run(
        [str(BIN), "monitor-external", "harvest-ef", "--workspace", str(peer_workspace)],
        cwd=str(third),
        env=env,
        capture_output=True, text=True,
    )
    assert proc.returncode == 3, f"expected refusal, got rc={proc.returncode}: {proc.stderr}"
    err = json.loads(proc.stderr)
    assert err["code"] == "E_REFUSAL_SELF"
    assert "SELVEDGE_WORKSPACE" in err["detail"]


def test_harvest_ef_refuses_when_cwd_inside_peer(
    clean_substrate, peer_workspace,
):
    """Iter-2 F-90 guard: refuse harvest-ef when the operator runs it from
    inside the peer workspace (the simpler footgun behind the cwd-confusion
    risk). SELVEDGE_WORKSPACE points at self-dev so the substrate validation
    succeeds — the refusal is purely on cwd grounds."""
    proc = _run_external_cli(
        ["monitor-external", "harvest-ef", "--workspace", str(peer_workspace)],
        cwd=peer_workspace,
        extra_env={
            "SELVEDGE_WORKSPACE": str(WORKSPACE),
            # PYTHONPATH so `python -m selvedge.cli` resolves from any cwd.
            "PYTHONPATH": str(WORKSPACE),
        },
    )
    assert proc.returncode == 3, f"expected refusal, got rc={proc.returncode}: {proc.stderr}"
    err = json.loads(proc.stderr)
    assert err["code"] == "E_REFUSAL_SELF"
    assert "inside the peer" in err["detail"]
    # Confirm no row landed anywhere.
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        n = conn.execute(
            "SELECT COUNT(*) FROM engine_feedback WHERE body_md LIKE '%cwd-guard body%'"
        ).fetchone()[0]
    finally:
        conn.close()
    assert n == 0
