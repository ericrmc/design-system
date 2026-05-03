"""Tests for the engine-v22+ issue handlers and engine-v26+ feedback handlers
that were left uncovered: issue-disposition, issue-link, issue-note,
engine-feedback, engine-feedback-disposition, forward-reference-disposition."""
from __future__ import annotations

import json
import sqlite3

import pytest

from conftest import PRIMARY_DB


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _seed_issue(selvedge_cli, *, alias: str, priority: str = "MEDIUM", title: str | None = None) -> int:
    res = selvedge_cli(
        [
            "submit", "issue", "--payload",
            json.dumps({
                "session_no": 1,
                "alias": alias,
                "title": title or f"pytest seed issue for {alias}",
                "priority": priority,
            }),
        ]
    )
    assert res["out"]["ok"], res
    return res["out"]["result"]["issue_id"]


# ---------------------------------------------------------------------------
# issue-disposition
# ---------------------------------------------------------------------------


def test_issue_disposition_resolves_via_alias(clean_substrate, selvedge_cli, db):
    iid = _seed_issue(selvedge_cli, alias="OI-S001-1")
    res = selvedge_cli(
        [
            "submit", "issue-disposition", "--payload",
            json.dumps({
                "session_no": 1,
                "alias": "OI-S001-1",
                "to_status": "resolved",
                "reason": "resolving via the pytest issue-disposition handler test",
            }),
        ]
    )
    assert res["out"]["ok"], res
    assert res["out"]["result"]["from_status"] == "open"
    assert res["out"]["result"]["to_status"] == "resolved"
    row = db.execute(
        "SELECT status, resolved_session_id FROM issues WHERE issue_id=?", (iid,)
    ).fetchone()
    assert row["status"] == "resolved"
    assert row["resolved_session_id"] is not None


def test_issue_disposition_via_issue_id(clean_substrate, selvedge_cli, db):
    iid = _seed_issue(selvedge_cli, alias="OI-S001-2")
    res = selvedge_cli(
        [
            "submit", "issue-disposition", "--payload",
            json.dumps({
                "session_no": 1,
                "issue_id": iid,
                "to_status": "superseded",
                "reason": "superseding by issue_id rather than alias for branch coverage",
            }),
        ]
    )
    assert res["out"]["ok"], res
    row = db.execute(
        "SELECT status, resolved_session_id FROM issues WHERE issue_id=?", (iid,)
    ).fetchone()
    assert row["status"] == "superseded"
    assert row["resolved_session_id"] is not None


def test_issue_disposition_noop_refused(clean_substrate, selvedge_cli):
    _seed_issue(selvedge_cli, alias="OI-S001-3")
    res = selvedge_cli(
        [
            "submit", "issue-disposition", "--payload",
            json.dumps({
                "session_no": 1,
                "alias": "OI-S001-3",
                "to_status": "open",
                "reason": "no-op transition that should be refused by the handler",
            }),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_VALIDATION" in res["err"]


def test_issue_disposition_unknown_alias_refused(clean_substrate, selvedge_cli):
    res = selvedge_cli(
        [
            "submit", "issue-disposition", "--payload",
            json.dumps({
                "session_no": 1,
                "alias": "OI-S999-9",
                "to_status": "resolved",
                "reason": "issue does not exist; should refuse with E_NOT_FOUND",
            }),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_NOT_FOUND" in res["err"]


# ---------------------------------------------------------------------------
# issue-link
# ---------------------------------------------------------------------------


def test_issue_link_inserts_via_aliases(clean_substrate, selvedge_cli, db):
    src = _seed_issue(selvedge_cli, alias="OI-S001-1")
    tgt = _seed_issue(selvedge_cli, alias="OI-S001-2")
    res = selvedge_cli(
        [
            "submit", "issue-link", "--payload",
            json.dumps({
                "session_no": 1,
                "source_alias": "OI-S001-1",
                "target_alias": "OI-S001-2",
                "relation": "duplicates",
                "reason": "pytest fixture creating an issue link via aliases",
            }),
        ]
    )
    assert res["out"]["ok"], res
    assert res["out"]["result"]["source_issue_id"] == src
    assert res["out"]["result"]["target_issue_id"] == tgt
    assert res["out"]["result"]["relation"] == "duplicates"


def test_issue_link_via_ids(clean_substrate, selvedge_cli, db):
    src = _seed_issue(selvedge_cli, alias="OI-S001-1")
    tgt = _seed_issue(selvedge_cli, alias="OI-S001-2")
    res = selvedge_cli(
        [
            "submit", "issue-link", "--payload",
            json.dumps({
                "session_no": 1,
                "source_issue_id": src,
                "target_issue_id": tgt,
                "relation": "blocks",
            }),
        ]
    )
    assert res["out"]["ok"], res


# ---------------------------------------------------------------------------
# issue-note
# ---------------------------------------------------------------------------


def test_issue_note_appends_seq_per_issue(clean_substrate, selvedge_cli, db):
    iid = _seed_issue(selvedge_cli, alias="OI-S001-1")
    r1 = selvedge_cli(
        [
            "submit", "issue-note", "--payload",
            json.dumps({
                "session_no": 1, "issue_id": iid,
                "note": "first note attached to the pytest issue fixture",
            }),
        ]
    )
    r2 = selvedge_cli(
        [
            "submit", "issue-note", "--payload",
            json.dumps({
                "session_no": 1, "alias": "OI-S001-1",
                "note": "second note attached via alias resolution path",
            }),
        ]
    )
    assert r1["out"]["result"]["seq"] == 1
    assert r2["out"]["result"]["seq"] == 2


# ---------------------------------------------------------------------------
# engine-feedback
# ---------------------------------------------------------------------------


def test_engine_feedback_inserts_with_alias(clean_substrate, selvedge_cli, db):
    res = selvedge_cli(
        [
            "submit", "engine-feedback", "--payload",
            json.dumps({
                "session_no": 1,
                "flag": "observation",
                "body_md": "**pytest engine-feedback** — test that the substrate handler lands a row.",
            }),
        ]
    )
    assert res["out"]["ok"], res
    fid = res["out"]["result"]["feedback_id"]
    assert res["out"]["result"]["alias"].startswith("EF-S")
    assert res["out"]["result"]["refs"] == 0  # no [alias] tokens in body_md
    row = db.execute(
        "SELECT flag, disposition FROM engine_feedback WHERE feedback_id=?", (fid,)
    ).fetchone()
    assert row["flag"] == "observation"
    assert row["disposition"] is None


def test_engine_feedback_with_inline_ref_records_refs_row(clean_substrate, selvedge_cli, db):
    """body_md containing [SPEC-something-vN] resolves to a refs row when the
    target object exists. We use a known existing alias from the seeded fixture."""
    seed = selvedge_cli(
        [
            "submit", "engine-feedback", "--payload",
            json.dumps({
                "session_no": 1, "flag": "observation",
                "body_md": "anchor body for the pytest feedback ref test",
            }),
        ]
    )
    anchor_alias = seed["out"]["result"]["alias"]
    res = selvedge_cli(
        [
            "submit", "engine-feedback", "--payload",
            json.dumps({
                "session_no": 1, "flag": "reframe",
                "body_md": f"this references [{anchor_alias}] which should resolve and record a ref row",
            }),
        ]
    )
    assert res["out"]["ok"], res
    assert res["out"]["result"]["refs"] >= 1


# ---------------------------------------------------------------------------
# engine-feedback-disposition
# ---------------------------------------------------------------------------


def test_engine_feedback_disposition_via_alias(clean_substrate, selvedge_cli, db):
    seed = selvedge_cli(
        [
            "submit", "engine-feedback", "--payload",
            json.dumps({
                "session_no": 1, "flag": "observation",
                "body_md": "feedback row to be dispositioned via alias path",
            }),
        ]
    )
    alias = seed["out"]["result"]["alias"]
    res = selvedge_cli(
        [
            "submit", "engine-feedback-disposition", "--payload",
            json.dumps({
                "session_no": 1,
                "alias": alias,
                "disposition": "addressed-by-pytest",
            }),
        ]
    )
    assert res["out"]["ok"], res
    row = db.execute(
        "SELECT disposition FROM engine_feedback WHERE feedback_id=?",
        (res["out"]["result"]["feedback_id"],),
    ).fetchone()
    assert row["disposition"] == "addressed-by-pytest"


def test_engine_feedback_disposition_via_feedback_id(clean_substrate, selvedge_cli, db):
    seed = selvedge_cli(
        [
            "submit", "engine-feedback", "--payload",
            json.dumps({
                "session_no": 1, "flag": "observation",
                "body_md": "feedback row to be dispositioned via feedback_id path",
            }),
        ]
    )
    fid = seed["out"]["result"]["feedback_id"]
    res = selvedge_cli(
        [
            "submit", "engine-feedback-disposition", "--payload",
            json.dumps({
                "session_no": 1,
                "feedback_id": fid,
                "disposition": "addressed-by-feedback-id-path",
            }),
        ]
    )
    assert res["out"]["ok"], res


def test_engine_feedback_disposition_missing_identifier_refused(clean_substrate, selvedge_cli):
    res = selvedge_cli(
        [
            "submit", "engine-feedback-disposition", "--payload",
            json.dumps({"session_no": 1, "disposition": "nothing-to-update"}),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_VALIDATION" in res["err"]
    # Pin the validation message so a future refactor that drops the explicit
    # "feedback_id or alias" guard but still refuses for some other reason
    # would be caught (reviewer F4).
    assert "feedback_id" in res["err"] or "alias" in res["err"]


def test_engine_feedback_disposition_unknown_alias_refused(clean_substrate, selvedge_cli):
    res = selvedge_cli(
        [
            "submit", "engine-feedback-disposition", "--payload",
            json.dumps({
                "session_no": 1, "alias": "EF-S999-99",
                "disposition": "alias-does-not-resolve",
            }),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_REFUSAL_T01" in res["err"] or "E_NOT_FOUND" in res["err"]


# ---------------------------------------------------------------------------
# forward-reference-disposition
# ---------------------------------------------------------------------------


def test_forward_reference_disposition_resolves_state_item(clean_substrate, selvedge_cli, db):
    """Seed a close-record with a next_session_should item, then dispose the
    forward-reference pointing at it."""
    cr = selvedge_cli(
        [
            "submit", "close-record", "--payload",
            json.dumps({
                "session_no": 1,
                "summary": "fixture close-record for FR disposition test",
                "items": [
                    {"facet": "next_session_should", "text": "pytest follow-up forward reference"},
                ],
            }),
        ]
    )
    assert cr["out"]["ok"], cr
    # workspace_session_no for session 1 = 1 + init_session_offset (179) = 180.
    target_wno = db.execute(
        "SELECT workspace_session_no FROM sessions WHERE session_no=1"
    ).fetchone()["workspace_session_no"]
    res = selvedge_cli(
        [
            "submit", "forward-reference-disposition", "--payload",
            json.dumps({
                "session_no": 1,
                "target_session": target_wno, "seq": 1,
                "note": "addressed by the pytest FR-disposition fixture",
            }),
        ]
    )
    assert res["out"]["ok"], res
    assert res["out"]["result"]["ref"] == f"FR-S{target_wno:03d}-1"


def test_forward_reference_disposition_unknown_target_refused(clean_substrate, selvedge_cli):
    res = selvedge_cli(
        [
            "submit", "forward-reference-disposition", "--payload",
            json.dumps({
                "session_no": 1,
                "target_session": 9999, "seq": 99,
            }),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_NOT_FOUND" in res["err"]


def test_forward_reference_disposition_target_wrong_facet_refused(clean_substrate, selvedge_cli, db):
    """A close_state_items row with facet != 'next_session_should' must not
    resolve as a forward reference target — handler returns E_NOT_FOUND."""
    cr = selvedge_cli(
        [
            "submit", "close-record", "--payload",
            json.dumps({
                "session_no": 1,
                "summary": "close-record whose item is what_was_done — not an FR target",
                "items": [
                    {"facet": "what_was_done", "text": "pytest non-FR item to confirm facet guard"},
                ],
            }),
        ]
    )
    assert cr["out"]["ok"], cr
    target_wno = db.execute(
        "SELECT workspace_session_no FROM sessions WHERE session_no=1"
    ).fetchone()["workspace_session_no"]
    res = selvedge_cli(
        [
            "submit", "forward-reference-disposition", "--payload",
            json.dumps({
                "session_no": 1,
                "target_session": target_wno, "seq": 1,
            }),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_NOT_FOUND" in res["err"]
