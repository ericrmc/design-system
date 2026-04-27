"""Pytest parallels for the four submit kinds that already had bash coverage
in state/tests/round_trip.sh. Added in S080 per the orchestrator's pytest
preference. These tests run faster, are easier to extend with refusal cases,
and let the workspace migrate off bash for substrate testing.
"""
from __future__ import annotations

import hashlib
import json
import sqlite3
from pathlib import Path

import pytest

from conftest import PRIMARY_DB, WORKSPACE


def test_session_open_creates_session_and_object(clean_substrate, db):
    sid = clean_substrate
    row = db.execute(
        "SELECT session_no, slug, status FROM sessions WHERE session_id=?", (sid,)
    ).fetchone()
    assert row["session_no"] == 1
    assert row["status"] == "open"
    obj = db.execute(
        "SELECT object_kind, citable_alias FROM objects WHERE object_kind='session' AND typed_row_id=?",
        (sid,),
    ).fetchone()
    assert obj["object_kind"] == "session"
    assert obj["citable_alias"] == "S001"


def test_t10_session_must_be_contiguous(clean_substrate, selvedge_cli):
    res = selvedge_cli(
        [
            "submit",
            "session-open",
            "--payload",
            json.dumps(
                {
                    "session_no": 5,
                    "slug": "skip",
                    "mode": "self-development",
                    "workspace_id": "selvedge-self-development",
                    "engine_version_at_open": "engine-v17",
                }
            ),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_REFUSAL_T10" in res["err"]


def test_decision_with_alternative_creates_alias(clean_substrate, selvedge_cli, db):
    res = selvedge_cli(
        [
            "submit",
            "decision",
            "--payload",
            json.dumps(
                {
                    "session_no": 1,
                    "kind": "substantive",
                    "title": "alpha decision",
                    "body_md": "body without refs",
                    "alternatives": [
                        {
                            "label": "R-1.1",
                            "summary": "rejected alt",
                            "rejection_reason_md": "rejected because the summary is at least sixteen chars",
                        }
                    ],
                }
            ),
        ]
    )
    assert res["out"]["ok"]
    did = res["out"]["result"]["decision_id"]
    assert res["out"]["result"]["alias"] == "D-S001-1"
    n_alts = db.execute(
        "SELECT COUNT(*) AS n FROM decision_alternatives WHERE decision_id=?", (did,)
    ).fetchone()["n"]
    assert n_alts == 1


def test_t02_substantive_decision_requires_alternative_at_close(clean_substrate, selvedge_cli):
    selvedge_cli(
        [
            "submit",
            "decision",
            "--payload",
            json.dumps(
                {
                    "session_no": 1,
                    "kind": "substantive",
                    "title": "no alts",
                    "body_md": "no alternatives provided",
                    "alternatives": [],
                }
            ),
        ]
    )
    res = selvedge_cli(
        [
            "submit",
            "session-close",
            "--payload",
            json.dumps({"session_no": 1, "engine_version_at_close": "engine-v17"}),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_REFUSAL_T02" in res["err"]


def test_t08_short_rejection_reason_refused(clean_substrate, selvedge_cli):
    res = selvedge_cli(
        [
            "submit",
            "decision",
            "--payload",
            json.dumps(
                {
                    "session_no": 1,
                    "kind": "substantive",
                    "title": "short reason",
                    "body_md": "body",
                    "alternatives": [
                        {"label": "R-1.1", "summary": "alt", "rejection_reason_md": "too short"}
                    ],
                }
            ),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_REFUSAL_CHECK" in res["err"] or "E_REFUSAL_T08" in res["err"]


def test_t01_unresolved_alias_refused(clean_substrate, selvedge_cli):
    res = selvedge_cli(
        [
            "submit",
            "decision",
            "--payload",
            json.dumps(
                {
                    "session_no": 1,
                    "kind": "substantive",
                    "title": "dangling ref",
                    "body_md": "this cites [SPEC-does-not-exist-v1] which is unresolved",
                    "alternatives": [
                        {
                            "label": "R-1.1",
                            "summary": "rejected alternative",
                            "rejection_reason_md": "rejected because we are testing T-01 unresolved-alias refusal",
                        }
                    ],
                }
            ),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_REFUSAL_T01" in res["err"]


def test_spec_version_hash_match_admitted(clean_substrate, selvedge_cli, tmp_path, db):
    body_dir = WORKSPACE / "state" / "tests" / "spec-bodies"
    body_dir.mkdir(parents=True, exist_ok=True)
    body_path = body_dir / "fixture.md"
    body_path.write_text("fixture spec body for pytest\n")
    body_rel = body_path.relative_to(WORKSPACE).as_posix()
    sha = hashlib.sha256(body_path.read_bytes()).hexdigest()
    try:
        res = selvedge_cli(
            [
                "submit",
                "spec-version",
                "--payload",
                json.dumps(
                    {
                        "session_no": 1,
                        "spec_id": "fixture",
                        "version": 1,
                        "body_path": body_rel,
                        "body_sha256": sha,
                    }
                ),
            ]
        )
        assert res["out"]["ok"]
        assert res["out"]["result"]["alias"] == "SPEC-fixture-v1"
    finally:
        body_path.unlink(missing_ok=True)


def test_spec_version_hash_mismatch_refused(clean_substrate, selvedge_cli):
    body_dir = WORKSPACE / "state" / "tests" / "spec-bodies"
    body_dir.mkdir(parents=True, exist_ok=True)
    body_path = body_dir / "mismatch.md"
    body_path.write_text("real content\n")
    body_rel = body_path.relative_to(WORKSPACE).as_posix()
    bogus_sha = hashlib.sha256(b"different content").hexdigest()
    try:
        res = selvedge_cli(
            [
                "submit",
                "spec-version",
                "--payload",
                json.dumps(
                    {
                        "session_no": 1,
                        "spec_id": "mismatch",
                        "version": 1,
                        "body_path": body_rel,
                        "body_sha256": bogus_sha,
                    }
                ),
            ],
            expect_ok=False,
        )
        assert res["rc"] != 0
        assert "E_REFUSAL_T04" in res["err"]
    finally:
        body_path.unlink(missing_ok=True)


def test_session_close_after_unresolved_workitems_refused(clean_substrate, selvedge_cli, db):
    """T-11 demonstrator. We can't insert a work_item via the CLI yet (no
    submit kind), so we go via direct sqlite3 with the __cli__ capability
    that's already seeded for work_items.insert."""
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        # Pre-create a work_item with status='queued' so it blocks close.
        # This is an out-of-band write that mirrors what a future submit
        # kind for work_items would do; permitted today because role checks
        # are application-layer (T-12 partial). The test still proves T-11.
        conn.execute(
            "INSERT INTO work_items (session_id, kind, payload_json, status) VALUES (1, 'review', '{}', 'queued')"
        )
        conn.commit()
    finally:
        conn.close()

    # T-11 is a trigger; close should refuse.
    res = selvedge_cli(
        [
            "submit",
            "session-close",
            "--payload",
            json.dumps({"session_no": 1, "engine_version_at_close": "engine-v17"}),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_REFUSAL_T11" in res["err"]


def test_session_close_admitted_when_workitems_clear(clean_substrate, selvedge_cli, db):
    res = selvedge_cli(
        [
            "submit",
            "session-close",
            "--payload",
            json.dumps({"session_no": 1, "engine_version_at_close": "engine-v17"}),
        ]
    )
    assert res["out"]["ok"]
    row = db.execute("SELECT status FROM sessions WHERE session_no=1").fetchone()
    assert row["status"] == "closed"


def test_t06_closed_decision_immutable_via_sql(clean_substrate, selvedge_cli):
    selvedge_cli(
        [
            "submit",
            "decision",
            "--payload",
            json.dumps(
                {
                    "session_no": 1,
                    "kind": "substantive",
                    "title": "to be closed",
                    "body_md": "body",
                    "alternatives": [
                        {
                            "label": "R-1.1",
                            "summary": "rejected alt",
                            "rejection_reason_md": "rejected because we want to test T-06 close-time immutability",
                        }
                    ],
                }
            ),
        ]
    )
    selvedge_cli(
        [
            "submit",
            "session-close",
            "--payload",
            json.dumps({"session_no": 1, "engine_version_at_close": "engine-v17"}),
        ]
    )
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        with pytest.raises(sqlite3.IntegrityError) as exc:
            conn.execute("UPDATE decisions SET title='mutated' WHERE decision_no=1")
        assert "E_REFUSAL_T06" in str(exc.value)
    finally:
        conn.close()
