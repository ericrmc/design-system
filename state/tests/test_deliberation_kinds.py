"""Tests for the deliberation/perspective/synthesis-point submit kinds added in S080.

Coverage:
  - happy paths for deliberation-open, perspective, deliberation-seal, synthesis-point
  - T-05 refusal: perspective insert blocked once deliberation sealed
  - T-13 refusal: cannot null-out sealed_at via direct SQL UPDATE
  - T-14 refusal: convergence synthesis with <2 source_perspectives refused (CHECK)
  - T-06 refusal: closed-session deliberations/perspectives/synthesis_points immutable
  - T-12 refusal: non-__cli__ role with no capability is refused
  - state-machine guards: synthesis-point requires sealed deliberation;
                          deliberation-seal refuses already-sealed deliberation
  - alias parsing: perspective body_md emits a refs row when it cites an existing alias
"""
from __future__ import annotations

import json
import sqlite3

import pytest




def _attest_nil(selvedge_cli, did):
    """Submit a nil_attestation cheap-exit deliberation_counterfactuals row so
    deliberation-seal admits past T-36 (DV-S180-1, engine-v50, migration 040).
    Tests that exercise post-seal behavior call this immediately before the
    seal submit."""
    return selvedge_cli(
        [
            "submit",
            "deliberation-counterfactual",
            "--payload",
            json.dumps(
                {
                    "deliberation_id": did,
                    "position": "pytest cheap-exit nil_attestation: no counterfactuals.",
                    "why": "tactical pytest seal; stance-space exhaustion not load-bearing.",
                    "disposition": "nilled-by-exclusion",
                    "exclusion_kind": "out-of-scope",
                    "nil_attestation": 1,
                }
            ),
        ]
    )


# ---------------------------------------------------------------------------
# happy paths
# ---------------------------------------------------------------------------


def test_deliberation_open_creates_row_and_object(clean_substrate, selvedge_cli, db):
    res = selvedge_cli(
        [
            "submit",
            "deliberation-open",
            "--payload",
            json.dumps({"session_no": 1, "topic": "happy"}),
        ]
    )
    assert res["out"]["ok"]
    did = res["out"]["result"]["deliberation_id"]
    row = db.execute(
        "SELECT topic, sealed_at, object_id FROM deliberations WHERE deliberation_id=?",
        (did,),
    ).fetchone()
    assert row["topic"] == "happy"
    assert row["sealed_at"] is None
    assert row["object_id"] is not None
    obj = db.execute("SELECT object_kind FROM objects WHERE object_id=?", (row["object_id"],)).fetchone()
    assert obj["object_kind"] == "deliberation"


def test_perspective_insert_before_seal(open_deliberation, selvedge_cli, db):
    did = open_deliberation
    res = selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps(
                {"deliberation_id": did, "label": "anth-1", "family": "anthropic", "body_md": "claude position"}
            ),
        ]
    )
    assert res["out"]["ok"]
    pid = res["out"]["result"]["perspective_id"]
    row = db.execute("SELECT label, family, object_id FROM perspectives WHERE perspective_id=?", (pid,)).fetchone()
    assert row["label"] == "anth-1"
    assert row["family"] == "anthropic"
    assert row["object_id"] is not None


def test_deliberation_seal_sets_timestamp_and_synthesis(open_deliberation, selvedge_cli, db):
    did = open_deliberation
    selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p1", "family": "anthropic", "body_md": "a"}),
        ]
    )
    selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p2", "family": "openai", "body_md": "b"}),
        ]
    )
    _attest_nil(selvedge_cli, did)
    res = selvedge_cli(
        [
            "submit",
            "deliberation-seal",
            "--payload",
            json.dumps({"deliberation_id": did, "synthesis_md": "synthesis"}),
        ]
    )
    assert res["out"]["ok"]
    row = db.execute(
        "SELECT sealed_at, synthesis_md FROM deliberations WHERE deliberation_id=?", (did,)
    ).fetchone()
    assert row["sealed_at"] is not None
    assert row["synthesis_md"] == "synthesis"


def test_synthesis_point_after_seal(open_deliberation, selvedge_cli, db):
    did = open_deliberation
    pids = []
    for label, family in [("p1", "anthropic"), ("p2", "openai")]:
        r = selvedge_cli(
            [
                "submit",
                "perspective",
                "--payload",
                json.dumps({"deliberation_id": did, "label": label, "family": family, "body_md": label}),
            ]
        )
        pids.append(r["out"]["result"]["perspective_id"])
    _attest_nil(selvedge_cli, did)
    selvedge_cli(
        [
            "submit",
            "deliberation-seal",
            "--payload",
            json.dumps({"deliberation_id": did}),
        ]
    )
    res = selvedge_cli(
        [
            "submit",
            "synthesis-point",
            "--payload",
            json.dumps(
                {
                    "deliberation_id": did,
                    "kind": "convergence",
                    "label": "conv-1",
                    "summary": "both agree",
                    "source_perspectives": pids,
                }
            ),
        ]
    )
    assert res["out"]["ok"]
    spid = res["out"]["result"]["synthesis_point_id"]
    row = db.execute(
        "SELECT kind, source_perspectives FROM synthesis_points WHERE synthesis_point_id=?", (spid,)
    ).fetchone()
    assert row["kind"] == "convergence"
    assert json.loads(row["source_perspectives"]) == pids


# ---------------------------------------------------------------------------
# refusals
# ---------------------------------------------------------------------------


def test_t05_perspective_after_seal_refused(open_deliberation, selvedge_cli):
    did = open_deliberation
    selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p1", "family": "anthropic", "body_md": "a"}),
        ]
    )
    _attest_nil(selvedge_cli, did)
    selvedge_cli(
        [
            "submit",
            "deliberation-seal",
            "--payload",
            json.dumps({"deliberation_id": did}),
        ]
    )
    res = selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "late", "family": "openai", "body_md": "late"}),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_REFUSAL_T05" in res["err"]


def test_t13_resealing_to_null_refused(open_deliberation, selvedge_cli, db_path):
    did = open_deliberation
    selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p1", "family": "anthropic", "body_md": "a"}),
        ]
    )
    _attest_nil(selvedge_cli, did)
    selvedge_cli(
        [
            "submit",
            "deliberation-seal",
            "--payload",
            json.dumps({"deliberation_id": did}),
        ]
    )
    # CLI has no path to revert sealed_at; verify the trigger refuses a direct UPDATE.
    conn = sqlite3.connect(str(db_path))
    try:
        with pytest.raises(sqlite3.IntegrityError) as exc:
            conn.execute("UPDATE deliberations SET sealed_at=NULL WHERE deliberation_id=?", (did,))
        assert "E_REFUSAL_T13" in str(exc.value)
    finally:
        conn.close()


def test_t14_convergence_with_one_source_refused(open_deliberation, selvedge_cli):
    did = open_deliberation
    r = selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p1", "family": "anthropic", "body_md": "a"}),
        ]
    )
    pid = r["out"]["result"]["perspective_id"]
    _attest_nil(selvedge_cli, did)
    selvedge_cli(
        [
            "submit",
            "deliberation-seal",
            "--payload",
            json.dumps({"deliberation_id": did}),
        ]
    )
    res = selvedge_cli(
        [
            "submit",
            "synthesis-point",
            "--payload",
            json.dumps(
                {
                    "deliberation_id": did,
                    "kind": "convergence",
                    "label": "lonely",
                    "summary": "only one",
                    "source_perspectives": [pid],
                }
            ),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_REFUSAL_CHECK" in res["err"] or "CHECK" in res["err"]


def test_t14_convergence_with_zero_sources_refused(open_deliberation, selvedge_cli):
    did = open_deliberation
    selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p1", "family": "anthropic", "body_md": "a"}),
        ]
    )
    _attest_nil(selvedge_cli, did)
    selvedge_cli(
        [
            "submit",
            "deliberation-seal",
            "--payload",
            json.dumps({"deliberation_id": did}),
        ]
    )
    res = selvedge_cli(
        [
            "submit",
            "synthesis-point",
            "--payload",
            json.dumps(
                {
                    "deliberation_id": did,
                    "kind": "convergence",
                    "label": "empty",
                    "summary": "no sources",
                    "source_perspectives": [],
                }
            ),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_REFUSAL_CHECK" in res["err"] or "CHECK" in res["err"]


def test_t14_divergence_with_one_source_admitted(open_deliberation, selvedge_cli, db):
    did = open_deliberation
    r = selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p1", "family": "anthropic", "body_md": "a"}),
        ]
    )
    pid = r["out"]["result"]["perspective_id"]
    _attest_nil(selvedge_cli, did)
    selvedge_cli(
        [
            "submit",
            "deliberation-seal",
            "--payload",
            json.dumps({"deliberation_id": did}),
        ]
    )
    res = selvedge_cli(
        [
            "submit",
            "synthesis-point",
            "--payload",
            json.dumps(
                {
                    "deliberation_id": did,
                    "kind": "divergence",
                    "label": "div-1",
                    "summary": "only p1 takes this view",
                    "source_perspectives": [pid],
                }
            ),
        ]
    )
    assert res["out"]["ok"]
    row = db.execute(
        "SELECT kind, source_perspectives FROM synthesis_points WHERE synthesis_point_id=?",
        (res["out"]["result"]["synthesis_point_id"],),
    ).fetchone()
    assert row["kind"] == "divergence"
    assert json.loads(row["source_perspectives"]) == [pid]


def test_t14_minority_with_one_source_admitted(open_deliberation, selvedge_cli, db):
    did = open_deliberation
    r = selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p1", "family": "anthropic", "body_md": "a"}),
        ]
    )
    pid = r["out"]["result"]["perspective_id"]
    _attest_nil(selvedge_cli, did)
    selvedge_cli(
        [
            "submit",
            "deliberation-seal",
            "--payload",
            json.dumps({"deliberation_id": did}),
        ]
    )
    res = selvedge_cli(
        [
            "submit",
            "synthesis-point",
            "--payload",
            json.dumps(
                {
                    "deliberation_id": did,
                    "kind": "minority",
                    "label": "min-1",
                    "summary": "p1 holds a minority position worth recording",
                    "source_perspectives": [pid],
                }
            ),
        ]
    )
    assert res["out"]["ok"]
    row = db.execute(
        "SELECT kind FROM synthesis_points WHERE synthesis_point_id=?",
        (res["out"]["result"]["synthesis_point_id"],),
    ).fetchone()
    assert row["kind"] == "minority"


def test_t06_closed_deliberation_topic_immutable(open_deliberation, selvedge_cli, submit_minimal_close_record, db_path):
    """Migration 002 (S082) added T-06 triggers on `deliberations` UPDATE/DELETE.
    A closed-session deliberation's `topic` and `synthesis_md` are now refused
    by direct SQL writers. This test was the strict xfail pinning OI-080-001
    pre-S082; it flips to a pass post-migration 002 and OI-080-001 closes."""
    did = open_deliberation
    selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p1", "family": "anthropic", "body_md": "a"}),
        ]
    )
    selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p2", "family": "openai", "body_md": "b"}),
        ]
    )
    _attest_nil(selvedge_cli, did)
    selvedge_cli(
        [
            "submit",
            "deliberation-seal",
            "--payload",
            json.dumps({"deliberation_id": did, "synthesis_md": "original synthesis"}),
        ]
    )
    submit_minimal_close_record(1)
    selvedge_cli(
        [
            "submit",
            "session-close",
            "--payload",
            json.dumps({"session_no": 1, "engine_version_at_close": "engine-v18"}),
        ]
    )
    conn = sqlite3.connect(str(db_path))
    try:
        with pytest.raises(sqlite3.IntegrityError) as exc:
            conn.execute("UPDATE deliberations SET topic='mutated' WHERE deliberation_id=?", (did,))
        assert "E_REFUSAL_T06" in str(exc.value)
    finally:
        conn.close()


def test_t13_refuses_resealing_to_other_timestamp(open_deliberation, selvedge_cli, db_path):
    """Migration 002 (S082) tightened T-13 from `NEW.sealed_at IS NULL` to
    `NEW.sealed_at IS NOT OLD.sealed_at`. Any change to a non-NULL sealed_at
    is now refused, including a re-seal at a different timestamp. This test
    was the second strict xfail pinning OI-080-001 pre-S082.

    Asserts on migration 002's specific error text (`is immutable once non-NULL`)
    so a regression that reverted T-13 to migration 001's wording (which
    *would* admit this UPDATE silently — `pytest.raises` would then fail
    correctly, but the assertion text-match prevents a future T-13 rewrite
    from drifting the error message without intent)."""
    did = open_deliberation
    selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p1", "family": "anthropic", "body_md": "a"}),
        ]
    )
    _attest_nil(selvedge_cli, did)
    selvedge_cli(
        [
            "submit",
            "deliberation-seal",
            "--payload",
            json.dumps({"deliberation_id": did}),
        ]
    )
    conn = sqlite3.connect(str(db_path))
    try:
        with pytest.raises(sqlite3.IntegrityError) as exc:
            conn.execute(
                "UPDATE deliberations SET sealed_at='2025-01-01T00:00:00.000Z' WHERE deliberation_id=?",
                (did,),
            )
        assert "E_REFUSAL_T13" in str(exc.value)
        assert "immutable once non-NULL" in str(exc.value), (
            "T-13 must surface the migration-002 wording; a regression that "
            "reverts to migration 001's `cannot be set back to NULL` text "
            "would silently admit non-NULL→other-non-NULL writes."
        )
    finally:
        conn.close()


def test_t13_admits_idempotent_same_value_sealed_at_write(open_deliberation, selvedge_cli, db, db_path):
    """Migration 002's tightened T-13 condition is `NEW.sealed_at IS NOT
    OLD.sealed_at`. For OLD='X' NEW='X', `'X' IS NOT 'X'` is false, so the
    trigger does not fire. A no-op update must be admitted (this is the
    third row of the truth table the migration documents). Without this
    test, a regression that strengthened the condition to `<>` (which would
    fire on same-value writes due to SQLite's NULL handling) would not be
    caught — the workspace's CLI never writes same-value, so no integration
    test would surface the regression."""
    did = open_deliberation
    selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p1", "family": "anthropic", "body_md": "a"}),
        ]
    )
    _attest_nil(selvedge_cli, did)
    selvedge_cli(
        [
            "submit",
            "deliberation-seal",
            "--payload",
            json.dumps({"deliberation_id": did}),
        ]
    )
    sealed_at = db.execute(
        "SELECT sealed_at FROM deliberations WHERE deliberation_id=?", (did,)
    ).fetchone()["sealed_at"]
    assert sealed_at is not None

    conn = sqlite3.connect(str(db_path))
    try:
        # Same-value write: OLD.sealed_at == NEW.sealed_at; trigger must not fire.
        conn.execute(
            "UPDATE deliberations SET sealed_at = ? WHERE deliberation_id = ?",
            (sealed_at, did),
        )
        conn.commit()
    finally:
        conn.close()
    after = db.execute(
        "SELECT sealed_at FROM deliberations WHERE deliberation_id=?", (did,)
    ).fetchone()["sealed_at"]
    assert after == sealed_at


def test_t06_closed_session_perspective_immutable(open_deliberation, selvedge_cli, submit_minimal_close_record, db_path):
    did = open_deliberation
    r1 = selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p1", "family": "anthropic", "body_md": "a"}),
        ]
    )
    pid = r1["out"]["result"]["perspective_id"]
    selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p2", "family": "openai", "body_md": "b"}),
        ]
    )
    _attest_nil(selvedge_cli, did)
    selvedge_cli(
        [
            "submit",
            "deliberation-seal",
            "--payload",
            json.dumps({"deliberation_id": did}),
        ]
    )
    submit_minimal_close_record(1)
    selvedge_cli(
        [
            "submit",
            "session-close",
            "--payload",
            json.dumps({"session_no": 1, "engine_version_at_close": "engine-v17"}),
        ]
    )
    conn = sqlite3.connect(str(db_path))
    try:
        with pytest.raises(sqlite3.IntegrityError) as exc:
            conn.execute("UPDATE perspectives SET body_md='mutated' WHERE perspective_id=?", (pid,))
        assert "E_REFUSAL_T06" in str(exc.value)
    finally:
        conn.close()


def test_t06_closed_session_synthesis_point_immutable(open_deliberation, selvedge_cli, submit_minimal_close_record, db_path):
    did = open_deliberation
    pids = []
    for label in ["p1", "p2"]:
        r = selvedge_cli(
            [
                "submit",
                "perspective",
                "--payload",
                json.dumps({"deliberation_id": did, "label": label, "family": "anthropic", "body_md": label}),
            ]
        )
        pids.append(r["out"]["result"]["perspective_id"])
    _attest_nil(selvedge_cli, did)
    selvedge_cli(
        [
            "submit",
            "deliberation-seal",
            "--payload",
            json.dumps({"deliberation_id": did}),
        ]
    )
    sp = selvedge_cli(
        [
            "submit",
            "synthesis-point",
            "--payload",
            json.dumps(
                {
                    "deliberation_id": did,
                    "kind": "convergence",
                    "label": "c1",
                    "summary": "agree",
                    "source_perspectives": pids,
                }
            ),
        ]
    )
    spid = sp["out"]["result"]["synthesis_point_id"]
    submit_minimal_close_record(1)
    selvedge_cli(
        [
            "submit",
            "session-close",
            "--payload",
            json.dumps({"session_no": 1, "engine_version_at_close": "engine-v17"}),
        ]
    )
    conn = sqlite3.connect(str(db_path))
    try:
        with pytest.raises(sqlite3.IntegrityError) as exc:
            conn.execute("UPDATE synthesis_points SET summary='mutated' WHERE synthesis_point_id=?", (spid,))
        assert "E_REFUSAL_T06" in str(exc.value)
    finally:
        conn.close()


def test_t12_non_cli_role_refused(open_deliberation, selvedge_cli):
    did = open_deliberation
    res = selvedge_cli(
        [
            "submit",
            "perspective",
            "--role",
            "stranger",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "px", "family": "anthropic", "body_md": "x"}),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_REFUSAL_T12" in res["err"]


# ---------------------------------------------------------------------------
# state-machine guards (CLI-level, not trigger-level)
# ---------------------------------------------------------------------------


def test_synthesis_point_requires_sealed_deliberation(open_deliberation, selvedge_cli):
    did = open_deliberation
    selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p1", "family": "anthropic", "body_md": "a"}),
        ]
    )
    selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p2", "family": "openai", "body_md": "b"}),
        ]
    )
    # Don't seal. Try to write a synthesis-point.
    res = selvedge_cli(
        [
            "submit",
            "synthesis-point",
            "--payload",
            json.dumps(
                {
                    "deliberation_id": did,
                    "kind": "convergence",
                    "label": "premature",
                    "summary": "agree",
                    "source_perspectives": [1, 2],
                }
            ),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_NOT_SEALED" in res["err"]


def test_double_seal_refused(open_deliberation, selvedge_cli):
    did = open_deliberation
    selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p1", "family": "anthropic", "body_md": "a"}),
        ]
    )
    _attest_nil(selvedge_cli, did)
    selvedge_cli(
        [
            "submit",
            "deliberation-seal",
            "--payload",
            json.dumps({"deliberation_id": did}),
        ]
    )
    res = selvedge_cli(
        [
            "submit",
            "deliberation-seal",
            "--payload",
            json.dumps({"deliberation_id": did}),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_ALREADY_SEALED" in res["err"]


# ---------------------------------------------------------------------------
# alias parsing — perspective body_md citing an existing alias creates a refs row
# ---------------------------------------------------------------------------


def test_perspective_body_alias_resolves_to_refs(open_deliberation, selvedge_cli, db):
    did = open_deliberation
    # First perspective creates alias P-<did>-anchor
    r1 = selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "anchor", "family": "anthropic", "body_md": "first"}),
        ]
    )
    anchor_alias = r1["out"]["result"]["alias"]
    assert anchor_alias == f"P-{did}-anchor"

    # Second perspective cites it.
    r2 = selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps(
                {
                    "deliberation_id": did,
                    "label": "citer",
                    "family": "openai",
                    "body_md": f"responds to [{anchor_alias}] with disagreement",
                }
            ),
        ]
    )
    assert r2["out"]["result"]["refs"] == 1
    n = db.execute("SELECT COUNT(*) AS n FROM refs").fetchone()["n"]
    assert n == 1


# ---------------------------------------------------------------------------
# T-36 deliberation_counterfactuals + deliberation-seal gate (DV-S180-1)
# ---------------------------------------------------------------------------


def test_t36_seal_refused_when_no_counterfactual_rows(open_deliberation, selvedge_cli):
    """T-36 (engine-v50, migration 040): deliberation-seal refuses when the
    deliberation has zero deliberation_counterfactuals rows."""
    did = open_deliberation
    selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p1", "family": "anthropic", "body_md": "a"}),
        ]
    )
    res = selvedge_cli(
        [
            "submit",
            "deliberation-seal",
            "--payload",
            json.dumps({"deliberation_id": did}),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_REFUSAL_T36" in res["err"]


def test_t36_seal_admits_after_one_counterfactual_row(open_deliberation, selvedge_cli, db):
    """T-36 admits seal once a single counterfactual row exists (substantive disposition path)."""
    did = open_deliberation
    selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p1", "family": "anthropic", "body_md": "a"}),
        ]
    )
    selvedge_cli(
        [
            "submit",
            "deliberation-counterfactual",
            "--payload",
            json.dumps(
                {
                    "deliberation_id": did,
                    "position": "Hybrid coexistence: typed primitive plus prose-prefix coexist.",
                    "why": "Foreclosed by Q1 graduate-or-subtract framing; not in stance-space.",
                    "disposition": "addressed-in-synthesis",
                    "disposition_note": "synthesis_md frame paragraph already addresses coexistence.",
                }
            ),
        ]
    )
    res = selvedge_cli(
        [
            "submit",
            "deliberation-seal",
            "--payload",
            json.dumps({"deliberation_id": did}),
        ]
    )
    assert res["out"]["ok"]
    n = db.execute(
        "SELECT COUNT(*) AS n FROM deliberation_counterfactuals WHERE deliberation_id=?",
        (did,),
    ).fetchone()["n"]
    assert n == 1


def test_nil_attestation_cheap_exit_admits_seal(open_deliberation, selvedge_cli, db):
    """The cheap-exit nil_attestation=1 row admits seal mirroring §8.5 audit-step:0."""
    did = open_deliberation
    selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p1", "family": "anthropic", "body_md": "a"}),
        ]
    )
    r = selvedge_cli(
        [
            "submit",
            "deliberation-counterfactual",
            "--payload",
            json.dumps(
                {
                    "deliberation_id": did,
                    "position": "Tactical-pytest-seal cheap-exit attestation row.",
                    "why": "Tactical scope; stance-space-exhaustion not load-bearing here.",
                    "disposition": "nilled-by-exclusion",
                    "exclusion_kind": "out-of-scope",
                    "nil_attestation": 1,
                }
            ),
        ]
    )
    assert r["out"]["ok"]
    assert r["out"]["result"]["nil_attestation"] == 1
    res = selvedge_cli(
        [
            "submit",
            "deliberation-seal",
            "--payload",
            json.dumps({"deliberation_id": did}),
        ]
    )
    assert res["out"]["ok"]


def test_disposition_addressed_in_synthesis_requires_note(open_deliberation, selvedge_cli):
    did = open_deliberation
    res = selvedge_cli(
        [
            "submit",
            "deliberation-counterfactual",
            "--payload",
            json.dumps(
                {
                    "deliberation_id": did,
                    "position": "A position no perspective took during the deliberation.",
                    "why": "Why it would change synthesis if adopted.",
                    "disposition": "addressed-in-synthesis",
                }
            ),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "addressed-in-synthesis requires disposition_note" in res["err"]


def test_disposition_nilled_by_exclusion_requires_kind(open_deliberation, selvedge_cli):
    did = open_deliberation
    res = selvedge_cli(
        [
            "submit",
            "deliberation-counterfactual",
            "--payload",
            json.dumps(
                {
                    "deliberation_id": did,
                    "position": "A position no perspective took during the deliberation.",
                    "why": "Why it would change synthesis if adopted.",
                    "disposition": "nilled-by-exclusion",
                }
            ),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "exclusion_kind" in res["err"]


def test_t13_counterfactual_after_seal_refused(open_deliberation, selvedge_cli):
    """T-13: cannot insert a counterfactual after parent deliberation is sealed."""
    did = open_deliberation
    selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p1", "family": "anthropic", "body_md": "a"}),
        ]
    )
    _attest_nil(selvedge_cli, did)
    selvedge_cli(
        [
            "submit",
            "deliberation-seal",
            "--payload",
            json.dumps({"deliberation_id": did}),
        ]
    )
    res = selvedge_cli(
        [
            "submit",
            "deliberation-counterfactual",
            "--payload",
            json.dumps(
                {
                    "deliberation_id": did,
                    "position": "Late counterfactual after seal — should be refused.",
                    "why": "T-13 mirrors synthesis_points / perspectives ordering discipline.",
                    "disposition": "nilled-by-exclusion",
                    "exclusion_kind": "out-of-scope",
                }
            ),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_REFUSAL_T13" in res["err"]


def test_nil_attestation_must_be_only_row(open_deliberation, selvedge_cli):
    """nil_attestation=1 cheap-exit row must be the only counterfactual."""
    did = open_deliberation
    selvedge_cli(
        [
            "submit",
            "deliberation-counterfactual",
            "--payload",
            json.dumps(
                {
                    "deliberation_id": did,
                    "position": "First substantive counterfactual.",
                    "why": "Some reason it would have changed synthesis.",
                    "disposition": "nilled-by-exclusion",
                    "exclusion_kind": "out-of-scope",
                }
            ),
        ]
    )
    res = selvedge_cli(
        [
            "submit",
            "deliberation-counterfactual",
            "--payload",
            json.dumps(
                {
                    "deliberation_id": did,
                    "position": "Second cheap-exit attestation should be refused.",
                    "why": "nil_attestation cheap-exit cannot follow another row.",
                    "disposition": "nilled-by-exclusion",
                    "exclusion_kind": "out-of-scope",
                    "nil_attestation": 1,
                }
            ),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "nil_attestation=1 cheap-exit row must be the only counterfactual" in res["err"]


def test_atom_rules_position_too_short_refused(open_deliberation, selvedge_cli):
    """deliberation_counterfactuals.position CHECK enforces length>=8."""
    did = open_deliberation
    res = selvedge_cli(
        [
            "submit",
            "deliberation-counterfactual",
            "--payload",
            json.dumps(
                {
                    "deliberation_id": did,
                    "position": "short",
                    "why": "long enough why text here.",
                    "disposition": "nilled-by-exclusion",
                    "exclusion_kind": "out-of-scope",
                }
            ),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0


def test_atom_rules_why_with_newline_refused(open_deliberation, selvedge_cli):
    """deliberation_counterfactuals.why CHECK refuses embedded newline."""
    did = open_deliberation
    res = selvedge_cli(
        [
            "submit",
            "deliberation-counterfactual",
            "--payload",
            json.dumps(
                {
                    "deliberation_id": did,
                    "position": "valid position text long enough.",
                    "why": "first line\nsecond line text long enough.",
                    "disposition": "nilled-by-exclusion",
                    "exclusion_kind": "out-of-scope",
                }
            ),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0


def test_atom_rules_position_with_pipe_table_refused(open_deliberation, selvedge_cli):
    """deliberation_counterfactuals.position CHECK refuses pipe-table syntax."""
    did = open_deliberation
    res = selvedge_cli(
        [
            "submit",
            "deliberation-counterfactual",
            "--payload",
            json.dumps(
                {
                    "deliberation_id": did,
                    "position": "header | col1 | col2 forbidden pipe.",
                    "why": "valid why text long enough here.",
                    "disposition": "nilled-by-exclusion",
                    "exclusion_kind": "out-of-scope",
                }
            ),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0


def test_invalid_exclusion_kind_refused(open_deliberation, selvedge_cli):
    """exclusion_kind CHECK admits only 4 values; invalid value refused."""
    did = open_deliberation
    res = selvedge_cli(
        [
            "submit",
            "deliberation-counterfactual",
            "--payload",
            json.dumps(
                {
                    "deliberation_id": did,
                    "position": "valid position text long enough.",
                    "why": "valid why text long enough here.",
                    "disposition": "nilled-by-exclusion",
                    "exclusion_kind": "made-up-not-in-enum",
                }
            ),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "exclusion_kind" in res["err"]


def test_t06_counterfactual_immutable_after_close(open_deliberation, selvedge_cli, db, submit_minimal_close_record, db_path):
    """T-06: closed-session deliberation_counterfactuals row is immutable."""
    did = open_deliberation
    selvedge_cli(
        [
            "submit",
            "perspective",
            "--payload",
            json.dumps({"deliberation_id": did, "label": "p1", "family": "anthropic", "body_md": "a"}),
        ]
    )
    cf_res = selvedge_cli(
        [
            "submit",
            "deliberation-counterfactual",
            "--payload",
            json.dumps(
                {
                    "deliberation_id": did,
                    "position": "Tactical seal cheap-exit attestation row.",
                    "why": "Tactical scope; stance-space-exhaustion not load-bearing.",
                    "disposition": "nilled-by-exclusion",
                    "exclusion_kind": "out-of-scope",
                    "nil_attestation": 1,
                }
            ),
        ]
    )
    cfid = cf_res["out"]["result"]["counterfactual_id"]
    selvedge_cli(
        [
            "submit",
            "deliberation-seal",
            "--payload",
            json.dumps({"deliberation_id": did}),
        ]
    )
    # Close the session via close-record + session-close.
    submit_minimal_close_record()
    selvedge_cli(["submit", "session-close", "--payload", json.dumps({})])
    # Now any direct UPDATE / DELETE should fire T-06.
    conn = sqlite3.connect(str(db_path))
    try:
        with pytest.raises(sqlite3.IntegrityError) as exc:
            conn.execute(
                "UPDATE deliberation_counterfactuals SET disposition_note='post-close mutation' WHERE counterfactual_id=?",
                (cfid,),
            )
        assert "E_REFUSAL_T06" in str(exc.value)
        with pytest.raises(sqlite3.IntegrityError) as exc:
            conn.execute(
                "DELETE FROM deliberation_counterfactuals WHERE counterfactual_id=?",
                (cfid,),
            )
        assert "E_REFUSAL_T06" in str(exc.value)
    finally:
        conn.close()
