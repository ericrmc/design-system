"""Tests for engine-v41 (DV-S134-1) and engine-v44 (DV-S153-1)
close-record sequencing defences:

- T-39 refuses session-close when no close_records row exists (UPDATE path).
- T-39b refuses INSERT INTO sessions with status='closed' without a
  close_records row (defence-in-depth, migration 028).
- T-40 refuses session-close when the close_records row carries zero
  close_state_items (migration 029, DV-S153-1).
- _submit_close_record refuses empty items[] at the handler pre-check
  (defence-in-depth companion to T-40).
- _validate_atom mirrors text_atoms.text CHECK + T-21 CR-guard at parse time
  with structured E_ATOM_* error codes that propagate through the CLI.
"""
from __future__ import annotations

import json
import sqlite3
from pathlib import Path

import pytest


from selvedge.errors import SelvedgeError
from selvedge.submit._helpers import _validate_atom


# ---------------------------------------------------------------------------
# T-39: session-close requires close_records row
# ---------------------------------------------------------------------------


def test_t39_refuses_session_close_without_close_record(clean_substrate, selvedge_cli):
    """T-39 fires when an open session is transitioned to closed without a
    close_records row. Closes the structural-coupling gap that bit S133."""
    res = selvedge_cli(
        ["submit", "session-close", "--payload", "{}"],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_REFUSAL_T39" in res["err"]
    assert "session-close requires a close_records row" in res["err"]


def test_t39_admits_session_close_with_close_record(clean_substrate, selvedge_cli, submit_minimal_close_record, db):
    """Round-trip: close-record then session-close succeeds; row persists."""
    submit_minimal_close_record(1)
    res = selvedge_cli(["submit", "session-close", "--payload", "{}"])
    assert res["out"]["ok"], res
    row = db.execute("SELECT status FROM sessions WHERE session_no=1").fetchone()
    assert row["status"] == "closed"


def test_t39b_refuses_direct_insert_of_closed_session(clean_substrate, db_path):
    """T-39b (migration 028, defence-in-depth) refuses INSERT INTO sessions
    with status='closed' bypassing the close_records gate. Direct sqlite3
    write to mirror the attack surface the CLI no longer exposes."""
    conn = sqlite3.connect(str(db_path))
    try:
        with pytest.raises(sqlite3.IntegrityError) as exc:
            conn.execute(
                "INSERT INTO sessions (session_no, slug, mode, workspace_id, "
                "engine_version_at_open, status, kind, workspace_session_no) "
                "VALUES (99, 'bypass', 'self-development', 'pytest', "
                "'engine-v17', 'closed', 'spec_only', 99)"
            )
        assert "E_REFUSAL_T39B" in str(exc.value)
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# T-40: session-close requires close_state_items
# ---------------------------------------------------------------------------


def test_t40_handler_refuses_empty_items_array(clean_substrate, selvedge_cli):
    """Handler-side pre-check refuses close-record with explicit empty
    items[] — surfaces E_VALIDATION before any close_records / text_atoms
    INSERT, so the caller cannot produce the S147-S150-class empty
    close_record rows that motivated DV-S153-1."""
    payload = {
        "session_no": 1,
        "summary": "well-formed summary atom for empty-items refusal test",
        "items": [],
    }
    res = selvedge_cli(
        ["submit", "close-record", "--payload", json.dumps(payload)],
        expect_ok=False,
    )
    assert res["rc"] != 0
    err = json.loads(res["err"])
    assert err["code"] == "E_VALIDATION"
    assert "non-empty items[]" in err["detail"]


def test_t40_handler_refuses_missing_items_field(clean_substrate, selvedge_cli):
    """Same refusal when the items field is absent entirely (treated as the
    empty case via `p.get('items') or []`)."""
    payload = {
        "session_no": 1,
        "summary": "well-formed summary atom for missing-items refusal test",
    }
    res = selvedge_cli(
        ["submit", "close-record", "--payload", json.dumps(payload)],
        expect_ok=False,
    )
    assert res["rc"] != 0
    err = json.loads(res["err"])
    assert err["code"] == "E_VALIDATION"
    assert "non-empty items[]" in err["detail"]


def test_t40_trigger_refuses_session_close_with_zero_items(clean_substrate, db, db_path):
    """T-40 fires at session-close when a close_records row exists for the
    session but no close_state_items row references it. Bypasses the handler
    pre-check via direct SQL to mirror the attack surface — same shape as
    test_t39b_refuses_direct_insert_of_closed_session."""
    conn = sqlite3.connect(str(db_path))
    try:
        atom_row = conn.execute(
            "INSERT INTO text_atoms (atom_type, text, created_session_id) "
            "VALUES ('close_summary', "
            "'direct-sql close-record summary for T-40 trigger refusal test', "
            "1) RETURNING atom_id"
        ).fetchone()
        atom_id = atom_row[0]
        conn.execute(
            "INSERT INTO close_records (session_id, summary_atom_id) VALUES (?, ?)",
            (1, atom_id),
        )
        with pytest.raises(sqlite3.IntegrityError) as exc:
            conn.execute(
                "UPDATE sessions SET status='closed' WHERE session_no=1"
            )
        assert "E_REFUSAL_T40" in str(exc.value)
        assert "at least one close_state_items entry" in str(exc.value)
    finally:
        conn.close()


def test_t40_admits_session_close_with_one_item(
    clean_substrate, selvedge_cli, submit_minimal_close_record, db
):
    """The minimal fixture submits exactly one close_state_items row; T-40
    admits session-close at the >=1 threshold. Round-trip ensures the
    threshold is not silently >=2 or higher."""
    submit_minimal_close_record(1)
    res = selvedge_cli(["submit", "session-close", "--payload", "{}"])
    assert res["out"]["ok"], res
    row = db.execute(
        "SELECT s.status, COUNT(csi.state_item_id) AS n "
        "FROM sessions s "
        "JOIN close_records cr ON cr.session_id=s.session_id "
        "LEFT JOIN close_state_items csi ON csi.close_record_id=cr.close_record_id "
        "WHERE s.session_no=1 GROUP BY s.session_id"
    ).fetchone()
    assert row["status"] == "closed"
    assert row["n"] == 1


# ---------------------------------------------------------------------------
# _validate_atom: parse-time mirror of text_atoms CHECK + T-21
# ---------------------------------------------------------------------------


def test_validate_atom_admits_well_formed_default_tier():
    _validate_atom("claim", "this is a normal claim atom comfortably in the 8-240 char window")


def test_validate_atom_refuses_too_short_default_tier():
    with pytest.raises(SelvedgeError) as exc:
        _validate_atom("claim", "tiny")
    assert exc.value.code == "E_ATOM_LENGTH"
    assert "minimum 8" in exc.value.detail


def test_validate_atom_refuses_too_long_default_tier():
    with pytest.raises(SelvedgeError) as exc:
        _validate_atom("close_state_item", "x" * 241, "items[2].text")
    assert exc.value.code == "E_ATOM_LENGTH"
    assert "items[2].text" in exc.value.detail
    assert "maximum 240" in exc.value.detail


def test_validate_atom_refuses_newline():
    with pytest.raises(SelvedgeError) as exc:
        _validate_atom("claim", "a claim with a\nnewline character which is forbidden")
    assert exc.value.code == "E_ATOM_NEWLINE"


def test_validate_atom_refuses_carriage_return():
    with pytest.raises(SelvedgeError) as exc:
        _validate_atom("claim", "a claim with a\rcarriage return which is forbidden")
    assert exc.value.code == "E_ATOM_CR"


def test_validate_atom_refuses_fenced_code():
    text = "claim with a " + "`" * 3 + "code" + "`" * 3 + " block which is forbidden"
    with pytest.raises(SelvedgeError) as exc:
        _validate_atom("claim", text)
    assert exc.value.code == "E_ATOM_FENCED_CODE"


def test_validate_atom_refuses_pipe_table_two_pipes():
    """SQL CHECK is `text NOT GLOB '*<pipe>*<pipe>*'` — refuses any text with
    two or more pipe chars. Python parity uses count('<pipe>') >= 2."""
    pipe = chr(124)
    text = f"col1 {pipe} col2 {pipe} col3 looks like a pipe-table row"
    with pytest.raises(SelvedgeError) as exc:
        _validate_atom("claim", text)
    assert exc.value.code == "E_ATOM_PIPE_TABLE"


def test_validate_atom_admits_single_pipe():
    """One pipe is admitted by the SQL GLOB and by the Python parity check."""
    pipe = chr(124)
    text = f"a single {pipe} pipe character is admitted by the validator"
    _validate_atom("claim", text)


def test_validate_atom_legacy_import_tier_window():
    """legacy_import admits up to 4000 chars per the SQL CHECK CASE."""
    _validate_atom("legacy_import", "x" * 4000)
    with pytest.raises(SelvedgeError) as exc:
        _validate_atom("legacy_import", "x" * 4001)
    assert exc.value.code == "E_ATOM_LENGTH"
    assert "maximum 4000" in exc.value.detail


def test_validate_atom_spec_clause_tier_window():
    """spec_clause admits 16-480 chars per the SQL CHECK CASE."""
    _validate_atom("spec_clause", "x" * 16)
    _validate_atom("spec_clause", "x" * 480)
    with pytest.raises(SelvedgeError) as exc:
        _validate_atom("spec_clause", "x" * 15)
    assert exc.value.code == "E_ATOM_LENGTH"
    assert "minimum 16" in exc.value.detail
    with pytest.raises(SelvedgeError) as exc:
        _validate_atom("spec_clause", "x" * 481)
    assert "maximum 480" in exc.value.detail


# ---------------------------------------------------------------------------
# Structured E_ATOM_* error codes propagate through CLI
# ---------------------------------------------------------------------------


def test_close_record_oversized_summary_surfaces_e_atom_length(clean_substrate, selvedge_cli):
    """An over-length summary must surface E_ATOM_LENGTH in the structured
    CLI error envelope so callers can branch on the code (the S133 surface
    that motivated DV-S134-1)."""
    payload = {
        "session_no": 1,
        "summary": "x" * 289,
        "items": [],
    }
    res = selvedge_cli(
        ["submit", "close-record", "--payload", json.dumps(payload)],
        expect_ok=False,
    )
    assert res["rc"] != 0
    err = json.loads(res["err"])
    assert err["ok"] is False
    assert err["code"] == "E_ATOM_LENGTH"
    assert "summary" in err["detail"]


def test_close_record_oversized_item_surfaces_e_atom_length(clean_substrate, selvedge_cli):
    """An over-length items[i].text surfaces E_ATOM_LENGTH naming the index;
    pre-validation catches it before any atom INSERT fires (so no half-built
    close-record is left in text_atoms)."""
    payload = {
        "session_no": 1,
        "summary": "well-formed summary atom",
        "items": [
            {"facet": "what_was_done", "text": "first item is well-formed"},
            {"facet": "state_at_close", "text": "x" * 289},
        ],
    }
    res = selvedge_cli(
        ["submit", "close-record", "--payload", json.dumps(payload)],
        expect_ok=False,
    )
    assert res["rc"] != 0
    err = json.loads(res["err"])
    assert err["code"] == "E_ATOM_LENGTH"
    assert "items[1].text" in err["detail"]


def test_decision_record_oversized_title_surfaces_e_atom_length(clean_substrate, selvedge_cli):
    """Validation fires uniformly for any atom-bearing handler, not just
    close-record. Decision-record's title atom triggers the same code."""
    payload = {
        "title": "x" * 289,
        "kind": "calibration",
        "outcome_type": "adopt",
        "target_kind": "process_rule",
        "target_key": "test-target",
    }
    res = selvedge_cli(
        ["submit", "decision-record", "--payload", json.dumps(payload)],
        expect_ok=False,
    )
    assert res["rc"] != 0
    err = json.loads(res["err"])
    assert err["code"] == "E_ATOM_LENGTH"


def test_close_record_with_newline_surfaces_e_atom_newline(clean_substrate, selvedge_cli):
    payload = {
        "session_no": 1,
        "summary": "summary atom containing a\nnewline character",
        "items": [],
    }
    res = selvedge_cli(
        ["submit", "close-record", "--payload", json.dumps(payload)],
        expect_ok=False,
    )
    assert res["rc"] != 0
    err = json.loads(res["err"])
    assert err["code"] == "E_ATOM_NEWLINE"
