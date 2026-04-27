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


def test_spec_version_supersedes_flips_prev_to_superseded(clean_substrate, selvedge_cli, db):
    """OI-S090-4 regression: handler must flip prev to superseded BEFORE inserting
    the new active row, or T-03 (unique partial index on active rows per spec_id)
    refuses the insert. Tripped in S087, S088, S089."""
    body_dir = WORKSPACE / "state" / "tests" / "spec-bodies"
    body_dir.mkdir(parents=True, exist_ok=True)
    v1 = body_dir / "supersede-v1.md"
    v2 = body_dir / "supersede-v2.md"
    v1.write_text("supersede fixture v1\n")
    v2.write_text("supersede fixture v2\n")
    v1_rel = v1.relative_to(WORKSPACE).as_posix()
    v2_rel = v2.relative_to(WORKSPACE).as_posix()
    v1_sha = hashlib.sha256(v1.read_bytes()).hexdigest()
    v2_sha = hashlib.sha256(v2.read_bytes()).hexdigest()
    try:
        r1 = selvedge_cli(
            [
                "submit", "spec-version", "--payload",
                json.dumps({
                    "session_no": 1, "spec_id": "supersede-fixture",
                    "version": 1, "body_path": v1_rel, "body_sha256": v1_sha,
                }),
            ]
        )
        assert r1["out"]["ok"], r1
        v1_alias = r1["out"]["result"]["alias"]

        r2 = selvedge_cli(
            [
                "submit", "spec-version", "--payload",
                json.dumps({
                    "session_no": 1, "spec_id": "supersede-fixture",
                    "version": 2, "body_path": v2_rel, "body_sha256": v2_sha,
                    "supersedes": v1_alias,
                    "supersedes_reason_md": "regression test for OI-S090-4 handler reorder",
                }),
            ]
        )
        assert r2["out"]["ok"], r2
        assert r2["out"]["result"]["refs"] == 1

        rows = db.execute(
            "SELECT version, status FROM spec_versions WHERE spec_id='supersede-fixture' ORDER BY version"
        ).fetchall()
        assert [(r["version"], r["status"]) for r in rows] == [(1, "superseded"), (2, "active")]
    finally:
        v1.unlink(missing_ok=True)
        v2.unlink(missing_ok=True)


def test_engine_manifest_bump_updates_workspace_metadata(clean_substrate, selvedge_cli, db):
    """OI-S091 regression: when spec_id='engine-manifest', the handler must
    propagate the new version into workspace_metadata.current_engine_version
    atomically. Migration 007 seeded this row; bumps in S087-S090 did not
    propagate, leaving the metadata four versions stale at S091 open."""
    body_dir = WORKSPACE / "state" / "tests" / "spec-bodies"
    body_dir.mkdir(parents=True, exist_ok=True)
    body = body_dir / "engine-manifest-coherence.md"
    body.write_text("engine-manifest coherence fixture\n")
    body_rel = body.relative_to(WORKSPACE).as_posix()
    sha = hashlib.sha256(body.read_bytes()).hexdigest()

    before = db.execute(
        "SELECT value FROM workspace_metadata WHERE key='current_engine_version'"
    ).fetchone()
    assert before is not None, "fixture should have current_engine_version seeded"

    try:
        r = selvedge_cli(
            [
                "submit", "spec-version", "--payload",
                json.dumps({
                    "session_no": 1, "spec_id": "engine-manifest",
                    "version": 999, "body_path": body_rel, "body_sha256": sha,
                }),
            ]
        )
        assert r["out"]["ok"], r

        after = db.execute(
            "SELECT value FROM workspace_metadata WHERE key='current_engine_version'"
        ).fetchone()
        assert after["value"] == "engine-v999", (
            f"expected current_engine_version='engine-v999' after engine-manifest bump, "
            f"got {after['value']!r}"
        )

        # Non-engine-manifest specs must NOT touch the metadata. Submit a
        # different spec_id and confirm the value is unchanged.
        other = body_dir / "other-coherence.md"
        other.write_text("other spec body\n")
        other_rel = other.relative_to(WORKSPACE).as_posix()
        other_sha = hashlib.sha256(other.read_bytes()).hexdigest()
        try:
            r2 = selvedge_cli(
                [
                    "submit", "spec-version", "--payload",
                    json.dumps({
                        "session_no": 1, "spec_id": "other-fixture",
                        "version": 1, "body_path": other_rel, "body_sha256": other_sha,
                    }),
                ]
            )
            assert r2["out"]["ok"], r2
            still = db.execute(
                "SELECT value FROM workspace_metadata WHERE key='current_engine_version'"
            ).fetchone()
            assert still["value"] == "engine-v999", (
                f"non-engine-manifest spec must not change current_engine_version; got {still['value']!r}"
            )
        finally:
            other.unlink(missing_ok=True)
    finally:
        body.unlink(missing_ok=True)


def test_spec_version_two_active_refused_by_t03(clean_substrate, selvedge_cli, db):
    """T-03 must refuse a direct INSERT of a second active row for the same spec_id.
    Confirms the unique partial index is the structural guarantee that the handler
    reorder relies on."""
    body_dir = WORKSPACE / "state" / "tests" / "spec-bodies"
    body_dir.mkdir(parents=True, exist_ok=True)
    body = body_dir / "t03-fixture.md"
    body.write_text("t03 fixture body\n")
    body_rel = body.relative_to(WORKSPACE).as_posix()
    sha = hashlib.sha256(body.read_bytes()).hexdigest()
    try:
        r1 = selvedge_cli(
            [
                "submit", "spec-version", "--payload",
                json.dumps({
                    "session_no": 1, "spec_id": "t03-fixture",
                    "version": 1, "body_path": body_rel, "body_sha256": sha,
                }),
            ]
        )
        assert r1["out"]["ok"], r1

        conn = sqlite3.connect(str(PRIMARY_DB))
        try:
            with pytest.raises(sqlite3.IntegrityError):
                conn.execute(
                    "INSERT INTO spec_versions (spec_id, version, body_path, body_sha256, status, session_id) "
                    "VALUES ('t03-fixture', 2, ?, ?, 'active', 1)",
                    (body_rel, sha),
                )
                conn.commit()
        finally:
            conn.close()
    finally:
        body.unlink(missing_ok=True)


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


def _seed_issue_and_work_item(selvedge_cli, *, alias="OI-S001-1", priority="MEDIUM"):
    """Helper: create one issue (via submit issue) and one work_item (via direct
    SQL since work_items.insert is __cli__-permitted but lacks a submit kind)
    and return (issue_id, work_item_id)."""
    res = selvedge_cli(
        [
            "submit",
            "issue",
            "--payload",
            json.dumps(
                {
                    "session_no": 1,
                    "citable_alias": alias,
                    "title": "pytest seed issue for issue-work-item linkage",
                    "priority": priority,
                }
            ),
        ]
    )
    assert res["out"]["ok"], res
    iid = res["out"]["result"]["issue_id"]
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        cur = conn.execute(
            "INSERT INTO work_items (session_id, kind, payload_json, status) "
            "VALUES (1, 'issue_resolution', '{}', 'queued')"
        )
        conn.commit()
        wid = cur.lastrowid
    finally:
        conn.close()
    return iid, wid


def test_issue_work_item_happy_path_inserts_link(clean_substrate, selvedge_cli, db):
    iid, wid = _seed_issue_and_work_item(selvedge_cli)
    res = selvedge_cli(
        [
            "submit",
            "issue-work-item",
            "--payload",
            json.dumps({"session_no": 1, "issue_id": iid, "work_item_id": wid}),
        ]
    )
    assert res["out"]["ok"], res
    row = db.execute(
        "SELECT issue_id, work_item_id, relation FROM issue_work_items WHERE issue_work_item_id=?",
        (res["out"]["result"]["issue_work_item_id"],),
    ).fetchone()
    assert row["issue_id"] == iid
    assert row["work_item_id"] == wid
    assert row["relation"] == "resolves"


def test_issue_work_item_resolves_alias(clean_substrate, selvedge_cli):
    iid, wid = _seed_issue_and_work_item(selvedge_cli, alias="OI-S001-2")
    res = selvedge_cli(
        [
            "submit",
            "issue-work-item",
            "--payload",
            json.dumps(
                {
                    "session_no": 1,
                    "citable_alias": "OI-S001-2",
                    "work_item_id": wid,
                    "relation": "informs",
                }
            ),
        ]
    )
    assert res["out"]["ok"], res
    assert res["out"]["result"]["issue_id"] == iid
    assert res["out"]["result"]["relation"] == "informs"


def test_issue_work_item_t24_refuses_resolve_with_queued_link(clean_substrate, selvedge_cli):
    iid, wid = _seed_issue_and_work_item(selvedge_cli, alias="OI-S001-3")
    selvedge_cli(
        [
            "submit",
            "issue-work-item",
            "--payload",
            json.dumps({"session_no": 1, "issue_id": iid, "work_item_id": wid}),
        ]
    )
    # T-24 refuses moving issue to resolved while linked work_item is queued.
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        with pytest.raises(sqlite3.IntegrityError) as exc:
            conn.execute("UPDATE issues SET status='resolved' WHERE issue_id=?", (iid,))
        assert "E_REFUSAL_T24" in str(exc.value)
    finally:
        conn.close()


def test_issue_work_item_unknown_work_item_refused(clean_substrate, selvedge_cli):
    iid, _wid = _seed_issue_and_work_item(selvedge_cli, alias="OI-S001-4")
    res = selvedge_cli(
        [
            "submit",
            "issue-work-item",
            "--payload",
            json.dumps({"session_no": 1, "issue_id": iid, "work_item_id": 999999}),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_NOT_FOUND" in res["err"]


def test_t25_lease_renewal_monotonic_refuses_backwards(clean_substrate):
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        conn.execute(
            "INSERT INTO work_items (session_id, kind, payload_json, status, leased_by, leased_at, lease_expires_at) "
            "VALUES (1, 'review', '{}', 'leased', 'tester', "
            "strftime('%Y-%m-%dT%H:%M:%fZ','now'), '2099-01-01T00:00:00.000Z')"
        )
        conn.commit()
        wid = conn.execute("SELECT MAX(work_item_id) AS w FROM work_items").fetchone()[0]
        # Backwards renewal refused.
        with pytest.raises(sqlite3.IntegrityError) as exc:
            conn.execute(
                "UPDATE work_items SET lease_expires_at='2098-01-01T00:00:00.000Z' WHERE work_item_id=?",
                (wid,),
            )
        assert "E_REFUSAL_T25" in str(exc.value)
        # Equal value also refused (strictly forward).
        with pytest.raises(sqlite3.IntegrityError) as exc:
            conn.execute(
                "UPDATE work_items SET lease_expires_at='2099-01-01T00:00:00.000Z' WHERE work_item_id=?",
                (wid,),
            )
        assert "E_REFUSAL_T25" in str(exc.value)
        # Forward renewal admitted.
        conn.execute(
            "UPDATE work_items SET lease_expires_at='2099-06-01T00:00:00.000Z' WHERE work_item_id=?",
            (wid,),
        )
        conn.commit()
        # Releasing the lease (NEW.status != 'leased') unaffected by T-25.
        conn.execute(
            "UPDATE work_items SET status='completed', lease_expires_at=NULL, completed_at=strftime('%Y-%m-%dT%H:%M:%fZ','now') WHERE work_item_id=?",
            (wid,),
        )
        conn.commit()
    finally:
        conn.close()


def test_issue_work_item_unknown_issue_id_refused(clean_substrate, selvedge_cli):
    _iid, wid = _seed_issue_and_work_item(selvedge_cli, alias="OI-S001-5")
    res = selvedge_cli(
        [
            "submit",
            "issue-work-item",
            "--payload",
            json.dumps({"session_no": 1, "issue_id": 999999, "work_item_id": wid}),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_NOT_FOUND" in res["err"]


def _seed_engine_feedback(*, flag="observation", body="x"*40, disposition=None):
    """Helper: insert one engine_feedback row tied to S001 with matching objects
    row (mirrors the raw-SQL pattern used in S092 since there is no submit
    handler for engine_feedback yet — see EF-S092-4 follow-up note)."""
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        cur = conn.execute(
            "INSERT INTO engine_feedback (session_id, flag, body_md, disposition) VALUES (1, ?, ?, ?)",
            (flag, body, disposition),
        )
        fid = cur.lastrowid
        cur2 = conn.execute(
            "INSERT INTO objects (object_kind, typed_row_id, citable_alias) VALUES ('engine_feedback', ?, ?)",
            (fid, f"EF-S001-{fid}"),
        )
        oid = cur2.lastrowid
        conn.execute("UPDATE engine_feedback SET object_id=? WHERE feedback_id=?", (oid, fid))
        conn.commit()
        return fid, f"EF-S001-{fid}"
    finally:
        conn.close()


def _orient_json(selvedge_cli):
    res = selvedge_cli(["orient", "--json"])
    assert res["rc"] == 0, res
    return res["out"]


def test_orient_includes_untriaged_feedback_section_when_empty(clean_substrate, selvedge_cli):
    packet = _orient_json(selvedge_cli)
    assert "untriaged_feedback" in packet
    assert "untriaged_feedback_total" in packet
    assert "untriaged_feedback_truncated" in packet
    assert packet["untriaged_feedback"] == []
    assert packet["untriaged_feedback_total"] == 0
    assert packet["untriaged_feedback_truncated"] is False


def test_orient_surfaces_undisposed_feedback(clean_substrate, selvedge_cli):
    fid, alias = _seed_engine_feedback(
        flag="observation",
        body="**bug heading**\n\nLong body that spans paragraphs and should not appear in the orient head.",
    )
    packet = _orient_json(selvedge_cli)
    assert packet["untriaged_feedback_total"] == 1
    row = packet["untriaged_feedback"][0]
    assert row["alias"] == alias
    assert row["flag"] == "observation"
    assert isinstance(row["surfaced_in"], int) and row["surfaced_in"] >= 1
    assert row["head"] == "**bug heading**"
    assert "\n" not in row["head"]


def test_orient_filters_disposed_feedback(clean_substrate, selvedge_cli):
    _seed_engine_feedback(disposition="triaged-into-OI-001")
    packet = _orient_json(selvedge_cli)
    assert packet["untriaged_feedback_total"] == 0
    assert packet["untriaged_feedback"] == []


def test_orient_markdown_renders_feedback_table(clean_substrate):
    _seed_engine_feedback(body="head with a | pipe inside should be escaped")
    import os, subprocess
    env = os.environ | {"SELVEDGE_WORKSPACE": str(WORKSPACE)}
    proc = subprocess.run(
        [str(WORKSPACE / "bin" / "selvedge"), "orient"],
        capture_output=True, text=True, env=env,
    )
    assert proc.returncode == 0, proc.stderr
    out = proc.stdout
    assert "## Untriaged engine feedback (1 of 1)" in out
    assert "| Alias | Flag | Surfaced | Head |" in out
    assert "head with a \\| pipe inside should be escaped" in out


def test_orient_head_skips_leading_blank_lines(clean_substrate, selvedge_cli):
    _seed_engine_feedback(body="\n\n\nactual content after blank lines")
    packet = _orient_json(selvedge_cli)
    assert packet["untriaged_feedback"][0]["head"] == "actual content after blank lines"


def test_orient_falls_back_when_feedback_object_missing(clean_substrate, selvedge_cli):
    """A feedback row without a paired objects row (legacy / out-of-band write)
    must still appear in orient with a synthetic alias rather than NULL."""
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        cur = conn.execute(
            "INSERT INTO engine_feedback (session_id, flag, body_md) VALUES (1, 'observation', 'orphan row')"
        )
        fid = cur.lastrowid
        conn.commit()
    finally:
        conn.close()
    packet = _orient_json(selvedge_cli)
    rows = [r for r in packet["untriaged_feedback"] if r["head"] == "orphan row"]
    assert len(rows) == 1
    assert rows[0]["alias"] == f"feedback_id={fid}"
