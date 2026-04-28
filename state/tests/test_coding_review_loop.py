"""Tests for substrate enforcement of the coding review loop (engine-v31, S104).

Covers:
- sessions.kind classification at open (default coding, immutable post-open via t29).
- review-pass submit handler (review_passes table).
- t30 close-gate refusing coding-session close without terminal review_pass.
- T-20 narrowing to admit halt path (nonconverged review_pass) while still
  blocking open medium+ findings on normal close.
- t_review_pass_nonconverged_requires_halt_issue trigger.
"""
from __future__ import annotations

import json

import pytest

from conftest import PRIMARY_DB


def _open_session(selvedge_cli, *, slug: str, kind: str | None = None) -> dict:
    payload: dict = {"slug": slug}
    if kind is not None:
        payload["kind"] = kind
    res = selvedge_cli(["submit", "session-open", "--payload", json.dumps(payload)])
    assert res["out"]["ok"], res
    return res["out"]["result"]


def _submit(selvedge_cli, kind: str, payload: dict, *, expect_ok: bool = True) -> dict:
    res = selvedge_cli(
        ["submit", kind, "--payload", json.dumps(payload)],
        expect_ok=expect_ok,
    )
    return res


def _err_payload(res: dict) -> dict:
    """The CLI writes error JSON to stderr; parse it for code/detail asserts."""
    err = res.get("err") or ""
    try:
        return json.loads(err)
    except (json.JSONDecodeError, TypeError):
        return {"_raw": err}


def _minimal_review_pass(**overrides) -> dict:
    base = {
        "iteration": 1,
        "outcome": "clean",
        "head_sha": "abc1234567",
        "summary": "review pass smoketest minimal",
    }
    base.update(overrides)
    return base


def _close_clean(selvedge_cli):
    """Close the currently-open session via a clean review-pass + close-record.
    Used by tests that opened a kind=coding session and need to drain it via
    the t30 happy path (clean review_pass)."""
    rp = _submit(selvedge_cli, "review-pass", _minimal_review_pass())
    assert rp["out"]["ok"], rp
    _close_after_record(selvedge_cli)


def _close_clean_specony(selvedge_cli):
    """Close the kind=spec_only fixture session (no review_pass required;
    t30 only fires on kind=coding)."""
    _close_after_record(selvedge_cli)


def _close_after_record(selvedge_cli):
    cr = _submit(
        selvedge_cli,
        "close-record",
        {"summary": "fixture drain", "items": [{"facet": "what_was_done", "text": "pytest fixture coverage placeholder text"}]},
    )
    assert cr["out"]["ok"], cr
    res = selvedge_cli(["submit", "session-close", "--payload", "{}"])
    assert res["out"]["ok"], res


# ---------------------------------------------------------------------------
# sessions.kind classification
# ---------------------------------------------------------------------------


def test_session_open_default_kind_is_coding(clean_substrate, selvedge_cli, db):
    # The fixture session is kind=spec_only by design (so existing tests can
    # close without a review_pass). Verify that an explicit second session
    # without a kind field defaults to 'coding'.
    _close_clean_specony(selvedge_cli)
    res = _open_session(selvedge_cli, slug="default-kind-check")
    assert res["kind"] == "coding"
    row = db.execute("SELECT kind FROM sessions WHERE session_id=?", (res["session_id"],)).fetchone()
    assert row["kind"] == "coding"


def test_session_open_accepts_spec_only(clean_substrate, selvedge_cli, db):
    _close_clean(selvedge_cli)
    res = _open_session(selvedge_cli, slug="spec-only-session", kind="spec_only")
    assert res["kind"] == "spec_only"
    new_sid = res["session_id"]
    row = db.execute("SELECT kind FROM sessions WHERE session_id=?", (new_sid,)).fetchone()
    assert row["kind"] == "spec_only"


def test_session_open_rejects_invalid_kind(clean_substrate, selvedge_cli):
    _close_clean(selvedge_cli)
    res = selvedge_cli(
        [
            "submit",
            "session-open",
            "--payload",
            json.dumps({"slug": "bad", "kind": "not-a-real-kind"}),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert _err_payload(res).get("code") == "E_VALIDATION"


def test_t29_sessions_kind_immutable(clean_substrate, db):
    # Fixture session is kind=spec_only; flip to a different value to trigger t29.
    with pytest.raises(Exception) as excinfo:
        db.execute(
            "UPDATE sessions SET kind='coding' WHERE session_id=?",
            (clean_substrate,),
        )
    assert "T29" in str(excinfo.value)


# ---------------------------------------------------------------------------
# review-pass handler
# ---------------------------------------------------------------------------


def test_review_pass_clean_writes_row(clean_substrate, selvedge_cli, db):
    res = _submit(selvedge_cli, "review-pass", _minimal_review_pass())
    assert res["out"]["ok"], res
    rpid = res["out"]["result"]["review_pass_id"]
    row = db.execute(
        "SELECT iteration, outcome, head_sha, halt_issue_id FROM review_passes WHERE review_pass_id=?",
        (rpid,),
    ).fetchone()
    assert row["iteration"] == 1
    assert row["outcome"] == "clean"
    assert row["head_sha"] == "abc1234567"
    assert row["halt_issue_id"] is None


def test_review_pass_head_sha_too_short_refused(clean_substrate, selvedge_cli):
    res = _submit(
        selvedge_cli,
        "review-pass",
        _minimal_review_pass(head_sha="abc"),
        expect_ok=False,
    )
    assert _err_payload(res).get("code") == "E_VALIDATION"


def test_review_pass_invalid_outcome_refused(clean_substrate, selvedge_cli):
    res = _submit(
        selvedge_cli,
        "review-pass",
        _minimal_review_pass(outcome="bogus"),
        expect_ok=False,
    )
    assert _err_payload(res).get("code") == "E_VALIDATION"


def test_review_pass_iteration_check_refuses_zero(clean_substrate, selvedge_cli):
    res = _submit(
        selvedge_cli,
        "review-pass",
        _minimal_review_pass(iteration=0),
        expect_ok=False,
    )
    # CHECK constraint on iteration BETWEEN 1 AND 4 fires from sqlite layer.
    assert res["rc"] != 0
    assert _err_payload(res).get("code") in ("E_REFUSAL_CHECK", "E_VALIDATION")


def test_review_pass_iteration_check_refuses_five(clean_substrate, selvedge_cli):
    res = _submit(
        selvedge_cli,
        "review-pass",
        _minimal_review_pass(iteration=5),
        expect_ok=False,
    )
    assert res["rc"] != 0


def test_review_pass_nonconverged_without_halt_issue_refused(clean_substrate, selvedge_cli):
    res = _submit(
        selvedge_cli,
        "review-pass",
        _minimal_review_pass(outcome="nonconverged", iteration=4),
        expect_ok=False,
    )
    # Application-layer validation (E_VALIDATION) fires before the trigger
    # (E_REFUSAL_RP1); both are correct enforcement.
    assert res["rc"] != 0
    code = _err_payload(res).get("code", "")
    assert code == "E_VALIDATION" or code.startswith("E_REFUSAL")


# ---------------------------------------------------------------------------
# t30 close-gate
# ---------------------------------------------------------------------------


def _open_coding_session(selvedge_cli, slug: str):
    """Drain the spec_only fixture session and open a fresh kind=coding session
    so t30 fires on its close attempt."""
    _close_clean_specony(selvedge_cli)
    return _open_session(selvedge_cli, slug=slug, kind="coding")


def test_t30_refuses_coding_close_without_review_pass(clean_substrate, selvedge_cli):
    _open_coding_session(selvedge_cli, "t30-no-pass")
    cr = _submit(
        selvedge_cli,
        "close-record",
        {"summary": "pytest close attempt summary placeholder text", "items": [{"facet": "what_was_done", "text": "pytest fixture coverage placeholder text"}]},
    )
    assert cr["out"]["ok"], cr
    res = selvedge_cli(["submit", "session-close", "--payload", "{}"], expect_ok=False)
    assert res["rc"] != 0
    assert "T30" in (res["err"] or "")


def test_t30_admits_coding_close_after_clean_pass(clean_substrate, selvedge_cli, db):
    coding_open = _open_coding_session(selvedge_cli, "t30-happy")
    sid = coding_open["session_id"]
    rp = _submit(selvedge_cli, "review-pass", _minimal_review_pass())
    assert rp["out"]["ok"]
    cr = _submit(
        selvedge_cli,
        "close-record",
        {"summary": "pytest close attempt summary placeholder text", "items": [{"facet": "what_was_done", "text": "pytest fixture coverage placeholder text"}]},
    )
    assert cr["out"]["ok"]
    res = selvedge_cli(["submit", "session-close", "--payload", "{}"])
    assert res["out"]["ok"], res
    row = db.execute("SELECT status FROM sessions WHERE session_id=?", (sid,)).fetchone()
    assert row["status"] == "closed"


def test_t30_findings_only_does_not_admit_close(clean_substrate, selvedge_cli):
    _open_coding_session(selvedge_cli, "t30-findings-only")
    rp = _submit(selvedge_cli, "review-pass", _minimal_review_pass(outcome="findings"))
    assert rp["out"]["ok"]
    cr = _submit(
        selvedge_cli,
        "close-record",
        {"summary": "pytest close attempt summary placeholder text", "items": [{"facet": "what_was_done", "text": "pytest fixture coverage placeholder text"}]},
    )
    assert cr["out"]["ok"]
    res = selvedge_cli(["submit", "session-close", "--payload", "{}"], expect_ok=False)
    assert res["rc"] != 0
    assert "T30" in (res["err"] or "")


def test_t30_admits_spec_only_close_without_review_pass(clean_substrate, selvedge_cli, db):
    # The fixture session itself is kind=spec_only — close it directly without
    # recording any review_pass; t30 must not fire because kind != coding.
    cr = _submit(
        selvedge_cli,
        "close-record",
        {"summary": "spec-only close pytest summary placeholder text", "items": [{"facet": "what_was_done", "text": "pytest fixture coverage placeholder text"}]},
    )
    assert cr["out"]["ok"]
    res = selvedge_cli(["submit", "session-close", "--payload", "{}"])
    assert res["out"]["ok"], res
    row = db.execute("SELECT status FROM sessions WHERE session_id=?", (clean_substrate,)).fetchone()
    assert row["status"] == "closed"


# ---------------------------------------------------------------------------
# halt path: t30 admits halt; T-20 narrowed to admit unresolved findings
# ---------------------------------------------------------------------------


def test_halt_path_admits_close_with_open_findings(clean_substrate, selvedge_cli, db):
    coding_open = _open_coding_session(selvedge_cli, "halt-path-test")
    sid = coding_open["session_id"]
    # Record an open medium finding (would normally block via T-20).
    rf = _submit(
        selvedge_cli,
        "review-finding",
        {
            "iteration": 1,
            "severity": "medium",
            "finding": "halt-path test: an unresolved medium finding the loop did not converge on",
        },
    )
    assert rf["out"]["ok"]

    # Open the halt-issue (the substrate requires the issue exist before
    # nonconverged review_pass references it).
    # Issue alias derived from the new coding session's workspace_session_no.
    new_wno = coding_open["workspace_session_no"]
    halt_alias = f"OI-S{new_wno:03d}-9"
    iss = _submit(
        selvedge_cli,
        "issue",
        {
            "alias": halt_alias,
            "title": "Halt-path pytest issue: findings unresolved at fourth iteration",
            "summary": "Pytest fixture issue to satisfy halt-issue_id FK on the halt-path test.",
            "priority": "MEDIUM",
        },
    )
    assert iss["out"]["ok"], iss

    # Record the nonconverged review_pass.
    rp = _submit(
        selvedge_cli,
        "review-pass",
        _minimal_review_pass(
            iteration=4,
            outcome="nonconverged",
            summary="halt-path: loop did not converge by fourth iteration",
            halt_issue_alias=halt_alias,
        ),
    )
    assert rp["out"]["ok"], rp

    cr = _submit(
        selvedge_cli,
        "close-record",
        {"summary": "halt close pytest summary placeholder text", "items": [{"facet": "what_was_done", "text": "halt-path pytest close-state placeholder"}]},
    )
    assert cr["out"]["ok"]

    res = selvedge_cli(["submit", "session-close", "--payload", "{}"])
    assert res["out"]["ok"], res
    row = db.execute("SELECT status FROM sessions WHERE session_id=?", (sid,)).fetchone()
    # Halted-as-status-value deferred (DV-S104-7 / OI-S104-3); halted is
    # encoded by review_passes.outcome=nonconverged on a status='closed' row.
    assert row["status"] == "closed"


def test_t20_still_blocks_normal_close_with_open_medium_finding(clean_substrate, selvedge_cli):
    rf = _submit(
        selvedge_cli,
        "review-finding",
        {
            "iteration": 1,
            "severity": "medium",
            "finding": "regression test for T-20: open medium finding on normal close path",
        },
    )
    assert rf["out"]["ok"]
    # No nonconverged review_pass — record a 'findings' outcome instead.
    rp = _submit(selvedge_cli, "review-pass", _minimal_review_pass(outcome="findings"))
    assert rp["out"]["ok"]
    cr = _submit(
        selvedge_cli,
        "close-record",
        {"summary": "pytest close attempt summary placeholder text", "items": [{"facet": "what_was_done", "text": "pytest fixture coverage placeholder text"}]},
    )
    assert cr["out"]["ok"]
    res = selvedge_cli(["submit", "session-close", "--payload", "{}"], expect_ok=False)
    assert res["rc"] != 0
    # Could refuse via T-20 (open medium finding) or T-30 (no clean pass).
    # Either is correct enforcement; assert close was refused.
    assert "T20" in (res["err"] or "") or "T30" in (res["err"] or "")
