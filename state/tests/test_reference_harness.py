"""Tests for the reference_harness substrate kind (engine-v35+, S125 closing
OI-S124-2).

The harness is a workspace-experimental substrate kind for the disaster-
response arc stage-2-onward pilot, NOT a kernel third validation sense. The
kernel-promotion question defers to OI-S124-1 at arc close.

Coverage:
    happy_path        full lifecycle: open -> targets/claims/stresses/results
                      /dissent/triggers -> seal -> verify status
    alias_format      T-34 refuses malformed alias
    p2_guardrail      results enum admits exactly the five P-4 labels;
                      domain_validated is structurally unwritable
    seal_immutability T-32 refuses sub-table writes after seal
    transition_lock   T-33 refuses non-lifecycle status transitions
    expiry_check      expiry_sessions >= 1 enforced
    declaration_required absence_declaration is mandatory (not nullable)
    cross_harness_dissent dissent.source_claim_id must belong to the same harness
"""
from __future__ import annotations

import json
import sqlite3

import pytest

from conftest import PRIMARY_DB


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

OPEN_PAYLOAD = {
    "session_no": 1,
    "arc_slug": "disaster-response",
    "stage_n": 2,
    "absence_declaration": "Disaster response is a fictional brief; no domain actor exists to validate stage outputs against real-world function.",
    "expiry_sessions": 5,
}


def _open_harness(selvedge_cli, **overrides) -> dict:
    payload = {**OPEN_PAYLOAD, **overrides}
    res = selvedge_cli(["submit", "harness-open", "--payload", json.dumps(payload)])
    assert res["out"]["ok"], res
    return res["out"]["result"]


# ---------------------------------------------------------------------------
# Happy path
# ---------------------------------------------------------------------------


def test_happy_path_lifecycle(clean_substrate, selvedge_cli, db):
    h = _open_harness(selvedge_cli)
    hid = h["harness_id"]
    # Alias is RH-S<workspace_session_no>-<seq>; the conftest fixture opens
    # session_no=1 which lands at workspace_session_no = init_offset + 1.
    assert h["alias"].startswith("RH-S")
    assert h["alias"].endswith("-1")
    assert h["status"] == "open"

    target = selvedge_cli([
        "submit", "harness-target", "--payload", json.dumps({
            "session_no": 1, "harness_id": hid,
            "descriptor": "stage-2 evacuation route plan markdown artefact",
            "artifact_path": "applications/001-disaster-response/stage-2/plan.md",
        }),
    ])["out"]["result"]
    assert target["ord"] == 1

    claim = selvedge_cli([
        "submit", "harness-claim", "--payload", json.dumps({
            "session_no": 1, "harness_id": hid,
            "claim": "Evacuation routes remain navigable under simulated 30cm flood depth.",
            "world_constraint": "Brief states fictional flood depths range 10-50cm at peak.",
            "load_bearing": True,
        }),
    ])["out"]["result"]
    cid = claim["claim_id"]
    assert claim["load_bearing"] is True

    stress = selvedge_cli([
        "submit", "harness-stress", "--payload", json.dumps({
            "session_no": 1, "harness_id": hid,
            "protocol_kind": "counterfactual",
            "description": "Replay route selection assuming 50cm depth (brief upper bound) instead of 30cm.",
        }),
    ])["out"]["result"]
    assert stress["protocol_kind"] == "counterfactual"

    result = selvedge_cli([
        "submit", "harness-result", "--payload", json.dumps({
            "session_no": 1, "claim_id": cid,
            "result": "strained",
            "evidence": "At 50cm two of seven routes become impassable; partial pass.",
        }),
    ])["out"]["result"]
    assert result["result"] == "strained"

    selvedge_cli([
        "submit", "harness-dissent", "--payload", json.dumps({
            "session_no": 1, "harness_id": hid,
            "dissent": "Surrogate stakeholder for elderly residents disputes 30cm baseline as unrealistic.",
            "source_claim_id": cid,
        }),
    ])

    selvedge_cli([
        "submit", "harness-trigger", "--payload", json.dumps({
            "session_no": 1, "harness_id": hid,
            "trigger": "Brief revision raising upper-bound flood depth above 50cm reopens the harness.",
        }),
    ])

    sealed = selvedge_cli([
        "submit", "harness-seal", "--payload", json.dumps({
            "session_no": 1, "harness_id": hid,
        }),
    ])["out"]["result"]
    assert sealed["status"] == "sealed"

    row = db.execute(
        "SELECT status, sealed_at, sealed_session_id FROM reference_harnesses WHERE harness_id=?",
        (hid,),
    ).fetchone()
    assert row["status"] == "sealed"
    assert row["sealed_at"] is not None
    assert row["sealed_session_id"] is not None


# ---------------------------------------------------------------------------
# T-34 alias format
# ---------------------------------------------------------------------------


def test_t34_alias_format_refusal(clean_substrate, selvedge_cli):
    res = selvedge_cli(
        [
            "submit", "harness-open", "--payload",
            json.dumps({**OPEN_PAYLOAD, "alias": "BAD-FORMAT-1"}),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_REFUSAL_T34" in res["err"]
    # Migration 032 (DV-S177-1) expanded the refusal text with a concrete
    # example so operators learn the accepted form from the error itself,
    # closing DV-S151-1 D-19 friction #3 (HRN-to-RH learning failure).
    assert "RH-S172-1" in res["err"]


# ---------------------------------------------------------------------------
# P-2 guardrail: results enum admits exactly five labels; no domain_validated
# ---------------------------------------------------------------------------


def test_p2_guardrail_results_enum_no_domain_validated(clean_substrate, selvedge_cli, db):
    h = _open_harness(selvedge_cli)
    claim = selvedge_cli([
        "submit", "harness-claim", "--payload", json.dumps({
            "session_no": 1, "harness_id": h["harness_id"],
            "claim": "claim text for guardrail test of result enum",
        }),
    ])["out"]["result"]

    # Each admitted label round-trips. We rebuild a fresh claim per label
    # because reference_harness_results.claim_id is UNIQUE.
    for label in ["survived", "strained", "broken", "untestable", "deferred"]:
        c = selvedge_cli([
            "submit", "harness-claim", "--payload", json.dumps({
                "session_no": 1, "harness_id": h["harness_id"],
                "claim": f"claim text for {label} round-trip in guardrail test",
            }),
        ])["out"]["result"]
        r = selvedge_cli([
            "submit", "harness-result", "--payload", json.dumps({
                "session_no": 1, "claim_id": c["claim_id"],
                "result": label,
                "evidence": f"evidence that the claim was assessed as {label} under stress",
            }),
        ])
        assert r["out"]["ok"], (label, r)

    # And: domain_validated is structurally refused by the CHECK enum.
    bad = selvedge_cli([
        "submit", "harness-result", "--payload", json.dumps({
            "session_no": 1, "claim_id": claim["claim_id"],
            "result": "domain_validated",
            "evidence": "this should be refused by the CHECK enum on reference_harness_results.result",
        }),
    ], expect_ok=False)
    assert bad["rc"] != 0
    # SQLite CHECK violations surface as IntegrityError; the handler raises
    # SelvedgeError on E_REFUSAL_* tags, but plain CHECK comes through as a
    # raw integrity message. Either way, ok=false.
    assert bad["out"] is None or bad["out"].get("ok") is False


# ---------------------------------------------------------------------------
# T-32 seal immutability
# ---------------------------------------------------------------------------


def test_t32_no_claim_after_seal(clean_substrate, selvedge_cli):
    h = _open_harness(selvedge_cli)
    selvedge_cli(["submit", "harness-seal", "--payload", json.dumps({
        "session_no": 1, "harness_id": h["harness_id"],
    })])
    res = selvedge_cli(
        [
            "submit", "harness-claim", "--payload",
            json.dumps({
                "session_no": 1, "harness_id": h["harness_id"],
                "claim": "post-seal claim attempt for T-32 refusal coverage",
            }),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_REFUSAL_T32" in res["err"]


def test_t32_no_result_after_seal(clean_substrate, selvedge_cli):
    h = _open_harness(selvedge_cli)
    claim = selvedge_cli([
        "submit", "harness-claim", "--payload", json.dumps({
            "session_no": 1, "harness_id": h["harness_id"],
            "claim": "claim recorded before seal so we can attempt a post-seal result write",
        }),
    ])["out"]["result"]
    selvedge_cli(["submit", "harness-seal", "--payload", json.dumps({
        "session_no": 1, "harness_id": h["harness_id"],
    })])
    res = selvedge_cli(
        [
            "submit", "harness-result", "--payload",
            json.dumps({
                "session_no": 1, "claim_id": claim["claim_id"],
                "result": "survived",
                "evidence": "post-seal evidence write that should be refused by T-32 on reference_harness_results",
            }),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_REFUSAL_T32" in res["err"]


# ---------------------------------------------------------------------------
# T-33 status-transition lock
# ---------------------------------------------------------------------------


def test_t33_invalid_transition_open_to_expired(clean_substrate, selvedge_cli, db):
    h = _open_harness(selvedge_cli)
    # Direct UPDATE bypasses the seal handler. Triggers still apply.
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        with pytest.raises(sqlite3.IntegrityError) as exc:
            conn.execute(
                "UPDATE reference_harnesses SET status='expired', "
                "sealed_at=strftime('%Y-%m-%dT%H:%M:%fZ','now'), sealed_session_id=1 "
                "WHERE harness_id=?",
                (h["harness_id"],),
            )
            conn.commit()
        assert "E_REFUSAL_T33" in str(exc.value)
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# CHECK constraint coverage
# ---------------------------------------------------------------------------


def test_expiry_sessions_must_be_positive(clean_substrate, selvedge_cli):
    res = selvedge_cli(
        [
            "submit", "harness-open", "--payload",
            json.dumps({**OPEN_PAYLOAD, "expiry_sessions": 0}),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0


def test_absence_declaration_required(clean_substrate, selvedge_cli):
    payload = {k: v for k, v in OPEN_PAYLOAD.items() if k != "absence_declaration"}
    res = selvedge_cli(
        ["submit", "harness-open", "--payload", json.dumps(payload)],
        expect_ok=False,
    )
    assert res["rc"] != 0


# ---------------------------------------------------------------------------
# Cross-harness dissent guard
# ---------------------------------------------------------------------------


def test_assumption_basis_records_origin_and_status(clean_substrate, selvedge_cli, db):
    h = _open_harness(selvedge_cli)
    res = selvedge_cli([
        "submit", "harness-assumption", "--payload", json.dumps({
            "session_no": 1, "harness_id": h["harness_id"],
            "assumption": "Brief states fictional flood depths peak at 50cm; load-bearing for route choice.",
            "status": "active",
        }),
    ])
    assert res["out"]["ok"], res
    aid = res["out"]["result"]["assumption_id"]
    row = db.execute(
        "SELECT harness_id, status, origin_session_id FROM reference_harness_assumptions WHERE assumption_id=?",
        (aid,),
    ).fetchone()
    assert row["status"] == "active"
    assert row["origin_session_id"] is not None


def test_t32_no_update_after_seal(clean_substrate, selvedge_cli, db):
    h = _open_harness(selvedge_cli)
    claim = selvedge_cli([
        "submit", "harness-claim", "--payload", json.dumps({
            "session_no": 1, "harness_id": h["harness_id"],
            "claim": "claim recorded before seal so we can attempt a post-seal UPDATE",
        }),
    ])["out"]["result"]
    selvedge_cli(["submit", "harness-seal", "--payload", json.dumps({
        "session_no": 1, "harness_id": h["harness_id"],
    })])
    # Direct UPDATE on a sealed claim is refused by T-32 BEFORE UPDATE.
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        with pytest.raises(sqlite3.IntegrityError) as exc:
            conn.execute(
                "UPDATE reference_harness_claims SET load_bearing=1 WHERE claim_id=?",
                (claim["claim_id"],),
            )
            conn.commit()
        assert "E_REFUSAL_T32" in str(exc.value)
    finally:
        conn.close()


def test_t32_no_delete_after_seal(clean_substrate, selvedge_cli, db):
    h = _open_harness(selvedge_cli)
    claim = selvedge_cli([
        "submit", "harness-claim", "--payload", json.dumps({
            "session_no": 1, "harness_id": h["harness_id"],
            "claim": "claim that we will attempt to DELETE after the harness is sealed for T-32 coverage",
        }),
    ])["out"]["result"]
    selvedge_cli(["submit", "harness-seal", "--payload", json.dumps({
        "session_no": 1, "harness_id": h["harness_id"],
    })])
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        with pytest.raises(sqlite3.IntegrityError) as exc:
            conn.execute(
                "DELETE FROM reference_harness_claims WHERE claim_id=?",
                (claim["claim_id"],),
            )
            conn.commit()
        assert "E_REFUSAL_T32" in str(exc.value)
    finally:
        conn.close()


def test_t36_sealed_harness_immutable_non_status_columns(clean_substrate, selvedge_cli, db):
    h = _open_harness(selvedge_cli)
    selvedge_cli(["submit", "harness-seal", "--payload", json.dumps({
        "session_no": 1, "harness_id": h["harness_id"],
    })])
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        with pytest.raises(sqlite3.IntegrityError) as exc:
            conn.execute(
                "UPDATE reference_harnesses SET arc_slug='different-arc' WHERE harness_id=?",
                (h["harness_id"],),
            )
            conn.commit()
        assert "E_REFUSAL_T36" in str(exc.value)
    finally:
        conn.close()


def test_t37_trigger_fire_cascades_to_reopened(clean_substrate, selvedge_cli, db):
    fixture_session_id = clean_substrate
    h = _open_harness(selvedge_cli)
    trig = selvedge_cli([
        "submit", "harness-trigger", "--payload", json.dumps({
            "session_no": 1, "harness_id": h["harness_id"],
            "trigger": "Brief revision raising flood depth above 50cm reopens this harness for replay.",
        }),
    ])["out"]["result"]
    selvedge_cli(["submit", "harness-seal", "--payload", json.dumps({
        "session_no": 1, "harness_id": h["harness_id"],
    })])
    fire = selvedge_cli([
        "submit", "harness-trigger-fire", "--payload", json.dumps({
            "session_no": 1, "trigger_id": trig["trigger_id"],
        }),
    ])
    assert fire["out"]["ok"], fire
    row = db.execute(
        "SELECT status, reopened_session_id FROM reference_harnesses WHERE harness_id=?",
        (h["harness_id"],),
    ).fetchone()
    assert row["status"] == "reopened"
    # Reopened harness records the firing session, not just any non-null value.
    assert row["reopened_session_id"] == fixture_session_id


def test_t36_lifecycle_columns_immutable_outside_transition(clean_substrate, selvedge_cli, db):
    """T-36 (post-iter-2): rewriting sealed_at on a sealed harness without
    changing status is timeline falsification and refused."""
    h = _open_harness(selvedge_cli)
    selvedge_cli(["submit", "harness-seal", "--payload", json.dumps({
        "session_no": 1, "harness_id": h["harness_id"],
    })])
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        with pytest.raises(sqlite3.IntegrityError) as exc:
            conn.execute(
                "UPDATE reference_harnesses SET sealed_at='1970-01-01T00:00:00.000Z' "
                "WHERE harness_id=?",
                (h["harness_id"],),
            )
            conn.commit()
        assert "E_REFUSAL_T36" in str(exc.value)
    finally:
        conn.close()


def test_t38_no_delete_after_open(clean_substrate, selvedge_cli, db):
    h = _open_harness(selvedge_cli)
    selvedge_cli(["submit", "harness-seal", "--payload", json.dumps({
        "session_no": 1, "harness_id": h["harness_id"],
    })])
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        with pytest.raises(sqlite3.IntegrityError) as exc:
            conn.execute(
                "DELETE FROM reference_harnesses WHERE harness_id=?",
                (h["harness_id"],),
            )
            conn.commit()
        assert "E_REFUSAL_T38" in str(exc.value)
    finally:
        conn.close()


def test_t32_assumptions_no_update_after_seal(clean_substrate, selvedge_cli, db):
    h = _open_harness(selvedge_cli)
    res = selvedge_cli([
        "submit", "harness-assumption", "--payload", json.dumps({
            "session_no": 1, "harness_id": h["harness_id"],
            "assumption": "load-bearing assumption recorded before seal for UPDATE-immutability coverage",
        }),
    ])
    aid = res["out"]["result"]["assumption_id"]
    selvedge_cli(["submit", "harness-seal", "--payload", json.dumps({
        "session_no": 1, "harness_id": h["harness_id"],
    })])
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        with pytest.raises(sqlite3.IntegrityError) as exc:
            conn.execute(
                "UPDATE reference_harness_assumptions SET status='invalidated' WHERE assumption_id=?",
                (aid,),
            )
            conn.commit()
        assert "E_REFUSAL_T32" in str(exc.value)
    finally:
        conn.close()


def test_t32_assumptions_no_delete_after_seal(clean_substrate, selvedge_cli, db):
    h = _open_harness(selvedge_cli)
    res = selvedge_cli([
        "submit", "harness-assumption", "--payload", json.dumps({
            "session_no": 1, "harness_id": h["harness_id"],
            "assumption": "load-bearing assumption recorded for DELETE-immutability coverage on a sealed harness",
        }),
    ])
    aid = res["out"]["result"]["assumption_id"]
    selvedge_cli(["submit", "harness-seal", "--payload", json.dumps({
        "session_no": 1, "harness_id": h["harness_id"],
    })])
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        with pytest.raises(sqlite3.IntegrityError) as exc:
            conn.execute(
                "DELETE FROM reference_harness_assumptions WHERE assumption_id=?",
                (aid,),
            )
            conn.commit()
        assert "E_REFUSAL_T32" in str(exc.value)
    finally:
        conn.close()


def test_trigger_pair_check_constraint(clean_substrate, selvedge_cli, db):
    """fired_at and reopened_session_id must be both NULL or both NOT NULL."""
    h = _open_harness(selvedge_cli)
    trig = selvedge_cli([
        "submit", "harness-trigger", "--payload", json.dumps({
            "session_no": 1, "harness_id": h["harness_id"],
            "trigger": "trigger text used for pair-CHECK constraint coverage in tests",
        }),
    ])["out"]["result"]
    selvedge_cli(["submit", "harness-seal", "--payload", json.dumps({
        "session_no": 1, "harness_id": h["harness_id"],
    })])
    conn = sqlite3.connect(str(PRIMARY_DB))
    try:
        with pytest.raises(sqlite3.IntegrityError):
            # Set fired_at without reopened_session_id — CHECK constraint refuses.
            conn.execute(
                "UPDATE reference_harness_triggers "
                "SET fired_at=strftime('%Y-%m-%dT%H:%M:%fZ','now') "
                "WHERE trigger_id=?",
                (trig["trigger_id"],),
            )
            conn.commit()
    finally:
        conn.close()


def test_trigger_fire_one_shot(clean_substrate, selvedge_cli):
    h = _open_harness(selvedge_cli)
    trig = selvedge_cli([
        "submit", "harness-trigger", "--payload", json.dumps({
            "session_no": 1, "harness_id": h["harness_id"],
            "trigger": "one-shot test trigger that we will attempt to fire twice for coverage",
        }),
    ])["out"]["result"]
    selvedge_cli(["submit", "harness-seal", "--payload", json.dumps({
        "session_no": 1, "harness_id": h["harness_id"],
    })])
    first = selvedge_cli([
        "submit", "harness-trigger-fire", "--payload", json.dumps({
            "session_no": 1, "trigger_id": trig["trigger_id"],
        }),
    ])
    assert first["out"]["ok"]
    second = selvedge_cli(
        [
            "submit", "harness-trigger-fire", "--payload",
            json.dumps({"session_no": 1, "trigger_id": trig["trigger_id"]}),
        ],
        expect_ok=False,
    )
    assert second["rc"] != 0


def test_dissent_source_claim_must_belong_to_harness(clean_substrate, selvedge_cli):
    h1 = _open_harness(selvedge_cli)
    h2 = _open_harness(selvedge_cli, stage_n=3)
    foreign = selvedge_cli([
        "submit", "harness-claim", "--payload", json.dumps({
            "session_no": 1, "harness_id": h2["harness_id"],
            "claim": "foreign claim belonging to a different harness for cross-harness dissent guard",
        }),
    ])["out"]["result"]
    res = selvedge_cli(
        [
            "submit", "harness-dissent", "--payload",
            json.dumps({
                "session_no": 1, "harness_id": h1["harness_id"],
                "dissent": "dissent text attempting to cite a foreign claim for guard coverage",
                "source_claim_id": foreign["claim_id"],
            }),
        ],
        expect_ok=False,
    )
    assert res["rc"] != 0
    assert "E_VALIDATION" in res["err"]
