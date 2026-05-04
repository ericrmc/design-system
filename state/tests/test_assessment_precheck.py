"""Tests for T-38 assessment-precheck gate (S195 DV-S195-1).

Coverage:
- T-38 refusal: assessment-submit without precheck_nonce is refused.
- T-38 admit: valid nonce from `bin/selvedge context` admits assessment-submit.
- Single-use consumption: same nonce cannot be re-used after first submit.
- Substrate-presented floor: bin/selvedge context with no --target still
  emits a pack populated from undisposed FRs + open HIGH OIs.
- Targeted context: --target alias surfaces anchored harvest EFs whose
  anchor lands on the target.
"""
from __future__ import annotations

import json
import re
import sqlite3
import subprocess

from conftest import PRIMARY_DB, _run_cli, BIN, WORKSPACE


def _close_open_session() -> None:
    """The clean_substrate fixture leaves session-1 open; close it so a
    fresh kind=coding session can be opened to exercise the gate."""
    cr = _run_cli([
        "submit", "close-record", "--payload",
        json.dumps({
            "summary": "test fixture close.",
            "items": [
                {"facet": "engine_version", "text": "engine-v17 unchanged in fixture close-record."},
                {"facet": "what_was_done", "text": "fixture-only: closed pytest seed session."},
                {"facet": "state_at_close", "text": "no substrate writes in fixture close-record."},
                {"facet": "next_session_should", "text": "fixture-only: precheck test will open the next."},
                {"facet": "validator_summary", "text": "fixture not exercised by validator."},
            ],
        }),
    ])
    assert cr["rc"] == 0, cr
    sc = _run_cli(["submit", "session-close", "--payload", "{}"])
    assert sc["rc"] == 0, sc


def _open_fresh_session(slug: str = "test-precheck", kind: str = "coding") -> int:
    res = _run_cli([
        "submit", "session-open", "--payload",
        json.dumps({"slug": slug, "kind": kind}),
    ])
    assert res["rc"] == 0, res
    return res["out"]["result"]["session_id"]


def _run_context_cli(targets: list[str] | None = None) -> dict:
    """Run `bin/selvedge context [--target X]* --print` and parse the nonce
    from the receipt summary line."""
    args = ["context", "--print"]
    for t in (targets or []):
        args += ["--target", t]
    import os
    env = os.environ | {"SELVEDGE_WORKSPACE": str(WORKSPACE)}
    proc = subprocess.run(
        [str(BIN), *args],
        capture_output=True, text=True, env=env,
    )
    out = proc.stdout
    err = proc.stderr
    if proc.returncode != 0:
        raise AssertionError(f"context CLI failed: rc={proc.returncode}\nstdout={out}\nstderr={err}")
    # Parse the receipt summary line (last non-empty line).
    summary_line = next((ln for ln in reversed(out.strip().splitlines()) if ln.strip()), "")
    m = re.search(r"nonce=(\S+)", summary_line)
    assert m, f"could not parse nonce from context CLI output: {summary_line!r}"
    return {
        "nonce": m.group(1),
        "body": out,
        "summary": summary_line,
    }


def test_assessment_submit_refused_without_nonce(clean_substrate):
    """T-38: assessment-submit refuses when precheck_nonce is missing."""
    _close_open_session()
    _open_fresh_session("test-no-nonce", "coding")

    res = _run_cli([
        "submit", "assessment", "--payload",
        json.dumps({"state": "test state without nonce, gate should fire.", "agenda": ["item one."]}),
    ], expect_ok=False)
    assert res["rc"] != 0, res
    payload = res["out"] or json.loads(res["err"])
    assert payload["ok"] is False
    assert payload["code"] == "E_REFUSAL_T38"
    assert "bin/selvedge context" in payload["detail"]


def test_assessment_submit_admits_with_valid_nonce(clean_substrate):
    """T-38: valid nonce from `bin/selvedge context` admits the submit."""
    _close_open_session()
    _open_fresh_session("test-valid-nonce", "coding")

    ctx = _run_context_cli([])
    res = _run_cli([
        "submit", "assessment", "--payload",
        json.dumps({
            "state": "test state with valid nonce, gate should pass.",
            "agenda": ["item one."],
            "precheck_nonce": ctx["nonce"],
        }),
    ])
    assert res["rc"] == 0, res
    assert res["out"]["ok"] is True
    assert res["out"]["result"]["alias"].startswith("A-S")


def test_nonce_single_use_consumption(clean_substrate):
    """Once consumed, the same nonce must not admit a second submit."""
    _close_open_session()
    _open_fresh_session("test-single-use", "coding")

    ctx = _run_context_cli([])
    res1 = _run_cli([
        "submit", "assessment", "--payload",
        json.dumps({
            "state": "first submit using the nonce.",
            "agenda": ["item one."],
            "precheck_nonce": ctx["nonce"],
        }),
    ])
    assert res1["rc"] == 0, res1
    # The first submit succeeded but immediately a second submit on the same
    # session would be refused by T-29 (one assessment per session). So we
    # need to verify single-use semantics differently: query the precheck
    # row and ensure consumed_at is set.
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        consumed = conn.execute(
            "SELECT consumed_at, consumed_by_assessment_id FROM assessment_prechecks "
            "WHERE nonce=?", (ctx["nonce"],)
        ).fetchone()
    finally:
        conn.close()
    assert consumed is not None
    assert consumed[0] is not None, "consumed_at not set after first submit"
    assert consumed[1] is not None, "consumed_by_assessment_id not set after first submit"


def test_substrate_presented_floor_with_no_targets(clean_substrate):
    """bin/selvedge context with no --target should still produce a pack
    using the substrate-presented floor (FRs + HIGH OIs)."""
    _close_open_session()
    _open_fresh_session("test-floor", "coding")

    ctx = _run_context_cli([])
    # The body must contain the floor section even if floor is empty.
    assert "Substrate-presented floor" in ctx["body"]
    # The summary line carries floor count.
    assert "floor=" in ctx["summary"]


def test_context_cli_with_target_surfaces_anchored_efs(clean_substrate):
    """When --target points at an alias with anchored harvest EFs, the
    pack must surface them under the target's section."""
    _close_open_session()
    _open_fresh_session("test-targeted", "coding")

    # Find an alias with at least one anchored EF; the seed substrate may
    # not have any, so we create a harvest EF + anchor first.
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        spec_row = conn.execute(
            "SELECT o.alias FROM spec_versions sv "
            "JOIN objects o ON o.object_id=sv.object_id WHERE sv.status='active' LIMIT 1"
        ).fetchone()
    finally:
        conn.close()
    if spec_row is None:
        return  # seed substrate has no active spec; skip
    spec_alias = spec_row[0]

    ef_res = _run_cli([
        "submit", "engine-feedback", "--payload",
        json.dumps({
            "flag": "observation",
            "body_md": "historical-harvest: source=archive/test.md\n\ntest body.",
            "anchors": [{"alias": spec_alias, "role": "about"}],
        }),
    ])
    assert ef_res["rc"] == 0, ef_res
    ef_alias = ef_res["out"]["result"]["alias"]

    ctx = _run_context_cli([spec_alias])
    assert spec_alias in ctx["body"]
    assert "anchored_harvest" in ctx["body"]
    assert ef_alias in ctx["body"]


def test_nonce_cross_session_rejected(clean_substrate):
    """Review-finding S195 iter-1 critical: nonce obtained in session-A must
    not admit assessment-submit in session-B. The handler verifies session_id
    + nonce match (line 44-46 of selvedge/submit/assessment.py); nonce_a's
    session_id is session-A, so submit-time WHERE clause finds no row.

    Test pattern: create TWO nonces in session-A (one consumable, one
    reserved for the cross-session test), submit session-A's assessment to
    close it cleanly, open session-B, attempt session-A's un-consumed
    nonce — must refuse."""
    _close_open_session()
    # Use kind=spec_only so close does not require a review-pass (T-30).
    _open_fresh_session("test-cross-A", "spec_only")
    ctx_a_consume = _run_context_cli([])  # nonce A1: will admit session-A submit
    ctx_a_reserved = _run_context_cli([])  # nonce A2: tied to session-A, never consumed

    # Submit session-A's assessment using A1 (consumes A1).
    res_a = _run_cli([
        "submit", "assessment", "--payload",
        json.dumps({
            "state": "session A submit consumes nonce A1; A2 stays unused for cross-test.",
            "agenda": ["item one."],
            "precheck_nonce": ctx_a_consume["nonce"],
        }),
    ])
    assert res_a["rc"] == 0, res_a

    # Close session-A.
    cr = _run_cli([
        "submit", "close-record", "--payload",
        json.dumps({
            "summary": "session A close to free up for session B.",
            "items": [
                {"facet": "engine_version", "text": "engine-v17 unchanged in fixture."},
                {"facet": "what_was_done", "text": "session A close fixture for cross-session test."},
                {"facet": "state_at_close", "text": "session A closed cleanly."},
                {"facet": "next_session_should", "text": "session B will try A nonce reserved one."},
                {"facet": "validator_summary", "text": "fixture not exercised."},
            ],
        }),
    ])
    assert cr["rc"] == 0, cr
    sc = _run_cli(["submit", "session-close", "--payload", "{}"])
    assert sc["rc"] == 0, sc

    # Open session-B (spec_only too) and attempt session-A's un-consumed nonce A2.
    _open_fresh_session("test-cross-B", "spec_only")
    res_b = _run_cli([
        "submit", "assessment", "--payload",
        json.dumps({
            "state": "session B trying session A reserved nonce should be refused.",
            "agenda": ["item one."],
            "precheck_nonce": ctx_a_reserved["nonce"],
        }),
    ], expect_ok=False)
    assert res_b["rc"] != 0, res_b
    payload = res_b["out"] or json.loads(res_b["err"])
    assert payload["code"] == "E_REFUSAL_T38"
    assert "does not match" in payload["detail"]


def test_nonce_expired_after_ttl(clean_substrate):
    """Review-finding S195 iter-1 critical: TTL expiry must refuse stale
    nonces. We force-update the precheck row's created_at to simulate an
    aged nonce, then verify T-38 refuses with `expired` in the detail."""
    _close_open_session()
    _open_fresh_session("test-ttl-expiry", "coding")

    ctx = _run_context_cli([])
    # Backdate the precheck row by 7200s (well past the 1800s default TTL).
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        conn.execute(
            "UPDATE assessment_prechecks SET created_at = "
            "strftime('%Y-%m-%dT%H:%M:%fZ','now','-7200 seconds') "
            "WHERE nonce=?", (ctx["nonce"],),
        )
        conn.commit()
    finally:
        conn.close()

    res = _run_cli([
        "submit", "assessment", "--payload",
        json.dumps({
            "state": "expired nonce should be refused with E_REFUSAL_T38 expired.",
            "agenda": ["item one."],
            "precheck_nonce": ctx["nonce"],
        }),
    ], expect_ok=False)
    assert res["rc"] != 0, res
    payload = res["out"] or json.loads(res["err"])
    assert payload["code"] == "E_REFUSAL_T38"
    assert "expired" in payload["detail"]
