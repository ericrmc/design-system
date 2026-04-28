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
import shutil
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


def _seed_ef_files(peer: Path, *names: tuple[str, str]) -> None:
    ef = peer / "engine-feedback"
    ef.mkdir(exist_ok=True)
    for fname, body in names:
        (ef / fname).write_text(body)


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
    assert "## Engine-feedback outbox" in md
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
    assert pkt["ef_outbox_files"] == []


def test_status_lists_engine_feedback_files(clean_substrate, selvedge_cli, peer_workspace):
    _seed_ef_files(
        peer_workspace,
        ("EF-001-first.md", "Flag: observation\n\nfirst body.\n"),
        ("EF-001-second.md", "flag: blocker\n\nsecond body.\n"),
    )
    res = selvedge_cli(["monitor-external", "status", "--workspace", str(peer_workspace), "--json"])
    paths = sorted(f["path"] for f in res["out"]["ef_outbox_files"])
    assert paths == [
        "engine-feedback/EF-001-first.md",
        "engine-feedback/EF-001-second.md",
    ]


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


def test_harvest_ef_dry_run_lists_plan_without_writing(
    clean_substrate, selvedge_cli, peer_workspace,
):
    _seed_ef_files(
        peer_workspace,
        ("EF-002-alpha.md", "Flag: observation\n\nalpha body.\n"),
        ("EF-003-beta.md", "flag: blocker\n\nbeta body.\n"),
    )
    res = selvedge_cli([
        "monitor-external", "harvest-ef",
        "--workspace", str(peer_workspace), "--dry-run",
    ])
    assert res["rc"] == 0
    assert res["out"]["dry_run"] is True
    actions = {entry["path"]: entry for entry in res["out"]["plan"]}
    assert actions["engine-feedback/EF-002-alpha.md"]["flag"] == "observation"
    assert actions["engine-feedback/EF-003-beta.md"]["flag"] == "blocker"
    assert all(e["action"] == "harvest" for e in res["out"]["plan"])
    # Verify no engine_feedback rows were written.
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        n = conn.execute("SELECT COUNT(*) FROM engine_feedback").fetchone()[0]
    finally:
        conn.close()
    assert n == 0


def test_harvest_ef_applies_and_creates_engine_feedback_rows(
    clean_substrate, selvedge_cli, peer_workspace,
):
    _seed_ef_files(
        peer_workspace,
        ("EF-002-alpha.md", "Flag: observation\n\nalpha body content.\n"),
        ("EF-003-beta.md", "flag: blocker\n\nbeta body content.\n"),
    )
    res = selvedge_cli([
        "monitor-external", "harvest-ef",
        "--workspace", str(peer_workspace),
    ])
    assert res["rc"] == 0
    assert res["out"]["dry_run"] is False
    successes = [r for r in res["out"]["results"] if r["status"] == "success"]
    assert len(successes) == 2
    flags = sorted(r["flag"] for r in successes)
    assert flags == ["blocker", "observation"]
    # Confirm the rows landed in the self-dev substrate (PRIMARY_DB) and that
    # the body_md preserves the original body plus the harvest preface.
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        rows = conn.execute(
            "SELECT flag, body_md FROM engine_feedback ORDER BY feedback_id"
        ).fetchall()
    finally:
        conn.close()
    assert len(rows) == 2
    # Order is filename-sort: alpha then beta.
    assert rows[0][0] == "observation"
    assert "Harvested from external workspace" in rows[0][1]
    assert "alpha body content." in rows[0][1]
    assert rows[1][0] == "blocker"
    assert "beta body content." in rows[1][1]


def test_harvest_ef_skips_below_since_session(
    clean_substrate, selvedge_cli, peer_workspace,
):
    _seed_ef_files(
        peer_workspace,
        ("EF-001-old.md", "Flag: observation\n\nold body.\n"),
        ("EF-005-new.md", "Flag: observation\n\nnew body.\n"),
    )
    res = selvedge_cli([
        "monitor-external", "harvest-ef",
        "--workspace", str(peer_workspace),
        "--since-session", "2",
    ])
    assert res["rc"] == 0
    by_status: dict[str, list[str]] = {}
    for entry in res["out"]["results"]:
        by_status.setdefault(entry["status"], []).append(entry["path"])
    assert by_status["success"] == ["engine-feedback/EF-005-new.md"]
    assert by_status["skipped"] == ["engine-feedback/EF-001-old.md"]


def test_harvest_ef_skips_unparseable_filenames(
    clean_substrate, selvedge_cli, peer_workspace,
):
    _seed_ef_files(
        peer_workspace,
        ("EF-001-good.md", "Flag: observation\n\ngood body.\n"),
        ("EF-bad-not-numeric.md", "flag: observation\n\nstray body.\n"),
    )
    res = selvedge_cli([
        "monitor-external", "harvest-ef",
        "--workspace", str(peer_workspace), "--dry-run",
    ])
    assert res["rc"] == 0
    by_path = {p["path"]: p for p in res["out"]["plan"]}
    assert by_path["engine-feedback/EF-001-good.md"]["action"] == "harvest"
    assert by_path["engine-feedback/EF-bad-not-numeric.md"]["action"] == "skip"
    assert "filename does not match" in by_path["engine-feedback/EF-bad-not-numeric.md"]["reason"]


def test_harvest_ef_handles_missing_engine_feedback_dir(
    clean_substrate, selvedge_cli, peer_workspace,
):
    # peer_workspace has no engine-feedback/ directory yet.
    res = selvedge_cli([
        "monitor-external", "harvest-ef",
        "--workspace", str(peer_workspace),
    ])
    assert res["rc"] == 0
    assert res["out"]["harvested"] == []
    assert "no engine-feedback/" in res["out"]["note"]


def test_harvest_ef_ignores_flag_buried_in_prose(
    clean_substrate, selvedge_cli, peer_workspace,
):
    """A 'flag: blocker' deep in prose must not override the default."""
    _seed_ef_files(
        peer_workspace,
        ("EF-001-mid-prose-flag.md",
         "This file's first paragraph carries no flag header.\n\n"
         "Several sentences in, the author writes flag: blocker as part of\n"
         "an unrelated narrative that should not change classification.\n"),
    )
    res = selvedge_cli([
        "monitor-external", "harvest-ef",
        "--workspace", str(peer_workspace), "--dry-run",
    ])
    assert res["rc"] == 0
    plan = res["out"]["plan"]
    assert len(plan) == 1
    assert plan[0]["flag"] == "observation"


def test_harvest_ef_ignores_selvedge_db_path_override(
    clean_substrate, peer_workspace,
):
    """harvest-ef must write to workspace_root()/state/selvedge.sqlite even
    when SELVEDGE_DB_PATH points elsewhere (S108 review F-84 / F-91). The
    explicit `Conn.open(self_db)` pin must bypass `db_path()`'s SELVEDGE_DB_PATH
    override."""
    _seed_ef_files(
        peer_workspace,
        ("EF-001-pin-test.md", "Flag: observation\n\npin-test body content.\n"),
    )
    peer_db = peer_workspace / "state" / "selvedge.sqlite"
    proc = _run_external_cli(
        ["monitor-external", "harvest-ef", "--workspace", str(peer_workspace)],
        extra_env={
            "SELVEDGE_WORKSPACE": str(WORKSPACE),
            "SELVEDGE_DB_PATH": str(peer_db),
        },
    )
    assert proc.returncode == 0, f"harvest-ef failed: {proc.stderr}"
    summary = json.loads(proc.stdout)
    successes = [r for r in summary["results"] if r["status"] == "success"]
    assert len(successes) == 1
    # If harvest-ef obeyed SELVEDGE_DB_PATH, the row would have landed in the
    # peer's substrate. The explicit pin must override that.
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        n_self = conn.execute(
            "SELECT COUNT(*) FROM engine_feedback WHERE body_md LIKE '%pin-test body%'"
        ).fetchone()[0]
    finally:
        conn.close()
    peer_conn = sqlite3.connect(str(peer_db))
    try:
        n_peer = peer_conn.execute(
            "SELECT COUNT(*) FROM engine_feedback WHERE body_md LIKE '%pin-test body%'"
        ).fetchone()[0]
    finally:
        peer_conn.close()
    assert n_self == 1, "row must land in self-dev PRIMARY_DB"
    assert n_peer == 0, "row must NOT leak into the peer substrate"


def test_harvest_ef_refuses_without_explicit_self_workspace_env(
    clean_substrate, peer_workspace, tmp_path,
):
    """Iter-3 F-92 guard: refuse harvest-ef when SELVEDGE_WORKSPACE is unset.
    Without the env var, workspace_root() walks cwd upward and could land in
    any peer that happens to have a MODE.md, routing writes to the wrong
    substrate. Demonstrate by running with cwd in a third workspace and no
    SELVEDGE_WORKSPACE set."""
    third = _bootstrap_peer(tmp_path / "third")
    _seed_ef_files(
        peer_workspace,
        ("EF-001-env-test.md", "Flag: observation\n\nenv-required body.\n"),
    )
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
    _seed_ef_files(
        peer_workspace,
        ("EF-001-cwd-test.md", "Flag: observation\n\ncwd-guard body.\n"),
    )
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
