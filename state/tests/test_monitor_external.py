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


def _peer_context_nonce(peer_root: Path) -> str:
    """Run `bin/selvedge context --print` on the peer to obtain a single-use
    nonce; required for assessment-submit per S195 DV-S195-1 T-38."""
    proc = _run_external_cli(
        ["context", "--print"],
        extra_env={
            "SELVEDGE_WORKSPACE": str(peer_root),
            "SELVEDGE_MIGRATIONS_DIR": str(WORKSPACE / "state" / "migrations"),
        },
    )
    assert proc.returncode == 0, f"peer context failed: {proc.stderr}"
    summary_line = next((ln for ln in reversed(proc.stdout.strip().splitlines()) if ln.strip()), "")
    import re as _re
    m = _re.search(r"nonce=(\S+)", summary_line)
    assert m, f"could not parse nonce from peer context output: {summary_line!r}"
    return m.group(1)


def _peer_submit(peer_root: Path, kind: str, payload: dict) -> dict:
    if kind == "assessment" and "precheck_nonce" not in payload:
        payload = {**payload, "precheck_nonce": _peer_context_nonce(peer_root)}
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


def _seed_peer_ef(peer: Path, slug: str, *bodies: tuple[str, str]) -> dict:
    """Open a fresh peer session, submit one engine-feedback row per body, close.

    Each `bodies` entry is `(flag, body_md)`. Returns
    `{"wno": <peer workspace_session_no>, "feedback": [<per-row submit result>]}`.
    The peer session is `kind=spec_only` so T-30's review-pass gate does not apply.

    The peer's `init_session_offset` is migration-seeded (OI-S091-1) so wno is
    not 1-based on a fresh peer; tests must read it from the result rather than
    hard-coding it.
    """
    open_res = _peer_submit(peer, "session-open", {"slug": slug, "kind": "spec_only"})
    wno = int(open_res["workspace_session_no"])
    _peer_submit(peer, "assessment", {
        "state": f"peer ef-seed session {slug} for harvest-ef coverage tests.",
        "agenda": ["seed engine_feedback rows for harvest-ef coverage."],
    })
    feedback = [_peer_submit(peer, "engine-feedback", {"flag": f, "body_md": b})
                for f, b in bodies]
    _peer_submit(peer, "close-record", {
        "summary": f"peer ef-seed close for {slug}.",
        "items": [
            {"facet": "engine_version", "text": "engine-v34 to engine-v34, no bump."},
            {"facet": "what_was_done", "text": "seeded peer engine_feedback rows for tests."},
            {"facet": "state_at_close", "text": "peer engine_feedback populated for tests."},
            {"facet": "open_issues", "text": "no open issues recorded in fixture."},
            {"facet": "next_session_should", "text": "harvest tests will run against this seed."},
            {"facet": "validator_summary", "text": "validator not exercised in fixture."},
        ],
    })
    _peer_submit(peer, "session-close", {})
    return {"wno": wno, "feedback": feedback}


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


# ---------------------------------------------------------------------------
# harvest-ef substrate-direct (S110, OI-S121-1)
#
# These tests exercise the substrate-direct harvest path: peer engine_feedback
# rows are read directly from the peer SQLite via `monitor_external._me_read_peer_ef`
# and written into self-dev's substrate via the engine-feedback handler, with
# per-row provenance recorded in `harvested_engine_feedback`.
# ---------------------------------------------------------------------------


def _harvest_ef(peer_workspace, *, dry_run: bool = False,
                 since_session: int | None = None) -> dict:
    """Run `selvedge monitor-external harvest-ef` against `peer_workspace`.

    `SELVEDGE_WORKSPACE` is pinned to the test workspace root so harvest writes
    target the snapshotted self-dev substrate (see `_snapshot_primary` in
    conftest), not whatever cwd the test happens to inherit. `dry_run` and
    `since_session` map to `--dry-run` and `--since-session`. Returns the
    parsed JSON envelope; asserts a 0 exit code at the call site.
    """
    args = ["monitor-external", "harvest-ef", "--workspace", str(peer_workspace)]
    if dry_run:
        args.append("--dry-run")
    if since_session is not None:
        args += ["--since-session", str(since_session)]
    proc = _run_external_cli(
        args,
        extra_env={"SELVEDGE_WORKSPACE": str(WORKSPACE)},
    )
    assert proc.returncode == 0, f"harvest-ef failed: {proc.stderr}"
    return json.loads(proc.stdout)


def test_harvest_ef_dry_run_empty_peer(clean_substrate, peer_workspace):
    """Peer with no engine_feedback rows yields an empty plan and a note."""
    out = _harvest_ef(peer_workspace, dry_run=True)
    assert out["dry_run"] is True
    assert out["peer_rows_total"] == 0
    assert out["plan"] == []
    assert "no engine_feedback rows" in out["note"]


def test_harvest_ef_dry_run_lists_unharvested_rows(
    clean_substrate, peer_workspace,
):
    """Each unharvested peer row appears in the plan with action=harvest, the
    peer alias, and the peer workspace_session_no. No self rows are written."""
    seed = _seed_peer_ef(
        peer_workspace, "ef-seed-1",
        ("observation", "**peer-ef-1** harvest-ef dry-run coverage atom one."),
        ("calibration", "**peer-ef-2** harvest-ef dry-run coverage atom two."),
    )
    wno = seed["wno"]
    expected_aliases = [f"EF-S{wno:03d}-1", f"EF-S{wno:03d}-2"]
    assert [r["alias"] for r in seed["feedback"]] == expected_aliases

    out = _harvest_ef(peer_workspace, dry_run=True)
    assert out["dry_run"] is True
    assert out["peer_rows_total"] == 2
    plan = out["plan"]
    assert [e["action"] for e in plan] == ["harvest", "harvest"]
    assert [e["peer_alias"] for e in plan] == expected_aliases
    assert [e["peer_wno"] for e in plan] == [wno, wno]
    assert [e["flag"] for e in plan] == ["observation", "calibration"]
    assert out["peer_workspace_id"]

    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        n_ef = conn.execute(
            "SELECT COUNT(*) FROM engine_feedback WHERE body_md LIKE '%peer-ef-%'"
        ).fetchone()[0]
        n_ledger = conn.execute(
            "SELECT COUNT(*) FROM harvested_engine_feedback"
        ).fetchone()[0]
    finally:
        conn.close()
    assert n_ef == 0
    assert n_ledger == 0


def test_harvest_ef_imports_with_provenance_preface_and_ledger(
    clean_substrate, peer_workspace,
):
    """Live harvest writes engine_feedback rows with the provenance preface,
    populates harvested_engine_feedback, and returns success per row."""
    seed = _seed_peer_ef(
        peer_workspace, "ef-seed-1",
        ("observation", "**peer-import-1** harvest-ef import coverage atom one."),
        ("blocker", "**peer-import-2** harvest-ef import coverage atom two."),
    )
    wno = seed["wno"]
    peer_fids = [r["feedback_id"] for r in seed["feedback"]]
    expected_aliases = [f"EF-S{wno:03d}-1", f"EF-S{wno:03d}-2"]

    out = _harvest_ef(peer_workspace)
    assert out["dry_run"] is False
    statuses = [r["status"] for r in out["results"]]
    assert statuses == ["success", "success"]
    self_aliases = [r["self_alias"] for r in out["results"]]
    assert all(a.startswith("EF-S") for a in self_aliases)

    peer_ws_id = out["peer_workspace_id"]
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        rows = conn.execute(
            "SELECT body_md, flag FROM engine_feedback "
            "WHERE body_md LIKE '%peer-import-%' ORDER BY feedback_id"
        ).fetchall()
        ledger = conn.execute(
            "SELECT peer_workspace_id, peer_feedback_id, peer_alias "
            "FROM harvested_engine_feedback ORDER BY harvest_id"
        ).fetchall()
    finally:
        conn.close()
    assert len(rows) == 2
    for body, _flag in rows:
        assert body.startswith("_Harvested from peer substrate")
        assert f"external session S{wno:03d}" in body
    assert [r[0] for r in ledger] == [peer_ws_id, peer_ws_id]
    assert [r[1] for r in ledger] == peer_fids
    assert [r[2] for r in ledger] == expected_aliases


def test_harvest_ef_idempotent_on_second_run(clean_substrate, peer_workspace):
    """Re-running harvest-ef against an unchanged peer skips already-harvested
    rows by ledger lookup; no duplicate self-substrate rows are written."""
    _seed_peer_ef(
        peer_workspace, "ef-seed-1",
        ("observation", "**peer-idem-1** idempotency atom one."),
        ("observation", "**peer-idem-2** idempotency atom two."),
    )

    first = _harvest_ef(peer_workspace)
    assert [r["status"] for r in first["results"]] == ["success", "success"]

    second = _harvest_ef(peer_workspace, dry_run=True)
    assert [e["action"] for e in second["plan"]] == ["skip", "skip"]
    assert all("already-harvested" in e["reason"] for e in second["plan"])

    third = _harvest_ef(peer_workspace)
    assert [r["status"] for r in third["results"]] == ["skipped", "skipped"]

    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        n_ef = conn.execute(
            "SELECT COUNT(*) FROM engine_feedback WHERE body_md LIKE '%peer-idem-%'"
        ).fetchone()[0]
        n_ledger = conn.execute(
            "SELECT COUNT(*) FROM harvested_engine_feedback"
        ).fetchone()[0]
    finally:
        conn.close()
    assert n_ef == 2
    assert n_ledger == 2


def test_harvest_ef_since_session_filter(clean_substrate, peer_workspace):
    """--since-session N skips peer rows whose peer_wno <= N."""
    early = _seed_peer_ef(
        peer_workspace, "ef-seed-early",
        ("observation", "**peer-since-early** filter atom from earlier peer session."),
    )
    later = _seed_peer_ef(
        peer_workspace, "ef-seed-later",
        ("observation", "**peer-since-later** filter atom from later peer session."),
    )
    early_wno, later_wno = early["wno"], later["wno"]
    assert later_wno > early_wno

    out = _harvest_ef(peer_workspace, dry_run=True, since_session=early_wno)
    by_wno = {e["peer_wno"]: e for e in out["plan"]}
    assert by_wno[early_wno]["action"] == "skip"
    assert f"since-session {early_wno}" in by_wno[early_wno]["reason"]
    assert by_wno[later_wno]["action"] == "harvest"

    live = _harvest_ef(peer_workspace, since_session=early_wno)
    statuses = {r["peer_wno"]: r["status"] for r in live["results"]}
    assert statuses == {early_wno: "skipped", later_wno: "success"}

    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        n_early = conn.execute(
            "SELECT COUNT(*) FROM engine_feedback WHERE body_md LIKE '%peer-since-early%'"
        ).fetchone()[0]
        n_later = conn.execute(
            "SELECT COUNT(*) FROM engine_feedback WHERE body_md LIKE '%peer-since-later%'"
        ).fetchone()[0]
    finally:
        conn.close()
    assert n_early == 0
    assert n_later == 1
