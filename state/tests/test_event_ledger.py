"""Tests for event-ledger v1 typed primitive (S204 DV-S204-1, OI-S196-4 close).

Coverage:
- Admit minimal payload: source + event_time + claim + 1 effect targeting AR
  admits with EV-S<wno>-<seq> alias + effect_id returned.
- Admit multiple effects: 2-effect event with both kinds (invalidates +
  confirms) admits per 1:N codex KNOT-1.
- Refuse missing source / event_time / claim: handler-side actionable
  refusal with E_VALIDATION naming the missing field.
- Refuse empty effects list: events without effects have no semantic content
  per D-S204-1 P-1 stance; E_VALIDATION.
- Refuse bad effect_kind enum: closed-2 enum at v1; E_VALIDATION.
- Refuse non-assumption target object_kind (handler): per-effect-kind
  allowlist refusal with E_VALIDATION.
- Refuse non-assumption target via T-43 SQL trigger: backstop fires when
  handler-side check is bypassed via direct SQL.
- Object-registration: row registers as object with alias EV-S<wno>-<seq>
  and object_kind='event' (drops _ledger suffix per DV-S198-1 P-1).
- Atom length refusals: source / event_time / claim / reason outside
  8-480 chars refused with E_ATOM_LENGTH.
- Unresolvable target alias: refused with E_REFUSAL_T01.
- UNIQUE(event_id, ord) refusal: explicit duplicate ord on multi-effect
  payload refused via SQL UNIQUE.
- Per-session seq: alias seq increments across events.
- Inert: invalidates-assumption does NOT auto-flip AR.status='invalidated'
  (D-S204-1 C-3 + codex named edit #4).
- Optional reason atom on effect: admits and pins reason atom.
"""
from __future__ import annotations

import json
import re
import sqlite3

from conftest import _run_cli


def _seed_assumption(statement: str = "Seed assumption for event-ledger tests target path coverage.") -> str:
    res = _run_cli([
        "submit", "assumption", "--payload", json.dumps({
            "statement": statement,
        }),
    ])
    return res["out"]["result"]["alias"]


def _seed_decision() -> str:
    res = _run_cli([
        "submit", "decision-record", "--payload", json.dumps({
            "title": "Seed decision-record for event-ledger non-allowlist target test.",
            "kind": "procedural",
            "outcome_type": "adopt",
            "target_kind": "process_rule",
            "target_key": "test-seed-rule-for-event-tests",
            "supports": [],
            "effects": [],
            "alternatives": [],
        }),
    ])
    return res["out"]["result"]["alias"]


def _submit_event(payload: dict, expect_ok: bool = True) -> dict:
    res = _run_cli([
        "submit", "event", "--payload", json.dumps(payload),
    ], expect_ok=expect_ok)
    if not expect_ok and res["out"] is None and res["err"]:
        try:
            res["out"] = json.loads(res["err"])
        except json.JSONDecodeError:
            pass
    return res


def test_admit_minimal_payload_returns_alias_and_one_effect(clean_substrate):
    ar = _seed_assumption()
    res = _submit_event({
        "source": "Ground team alpha radio report at T+34h checkpoint disaster-recovery scenario.",
        "event_time": "T+34h relative to disaster-recovery arc start; ISO equivalent 2026-05-05T10:00Z.",
        "claim": "City water main shut off — verified by ground team alpha at intersection 4th and Main.",
        "effects": [
            {
                "kind": "invalidates-assumption",
                "target": ar,
                "reason": "Water main shutoff invalidates the prior assumption that municipal water supply remained available.",
            },
        ],
    })
    assert res["rc"] == 0, res
    r = res["out"]["result"]
    assert re.match(r"^EV-S\d{3,}-\d+$", r["alias"]), r
    assert len(r["effects"]) == 1
    assert r["effects"][0]["kind"] == "invalidates-assumption"
    assert r["effects"][0]["target_object_id"] is not None


def test_admit_multiple_effects_with_both_kinds(clean_substrate):
    ar1 = _seed_assumption("First assumption seed for multi-effect event coverage.")
    ar2 = _seed_assumption("Second assumption seed for multi-effect event coverage.")
    res = _submit_event({
        "source": "Logistics lead status update T+92h covering convoy and supply assumptions in scenario.",
        "event_time": "T+92h from arc start; covers convoy ETA confirmation plus prior assumption status.",
        "claim": "Replacement fuel convoy ETA confirmed AND prior shortage assumption corroborated by report.",
        "effects": [
            {"kind": "invalidates-assumption", "target": ar1, "reason": "Convoy arrival invalidates the fuel-shortage holding assumption."},
            {"kind": "confirms-assumption", "target": ar2, "reason": "Logistics report corroborates assumption that supply chain remains intact."},
        ],
    })
    assert res["rc"] == 0, res
    r = res["out"]["result"]
    assert len(r["effects"]) == 2
    kinds = {e["kind"] for e in r["effects"]}
    assert kinds == {"invalidates-assumption", "confirms-assumption"}


def test_refuse_missing_source(clean_substrate):
    ar = _seed_assumption()
    res = _submit_event({
        "event_time": "T+34h relative time atom field for refusal-missing-source coverage path.",
        "claim": "Event claim atom for refusal-missing-source test path with sufficient atom length.",
        "effects": [{"kind": "invalidates-assumption", "target": ar}],
    }, expect_ok=False)
    assert res["rc"] != 0, res
    body = res["out"] or {}
    assert body.get("code") == "E_VALIDATION", body
    assert "source" in (body.get("detail") or ""), body


def test_refuse_missing_event_time(clean_substrate):
    ar = _seed_assumption()
    res = _submit_event({
        "source": "Source atom for refusal-missing-event-time coverage; sufficient atom length required.",
        "claim": "Event claim atom for refusal-missing-event-time test path with sufficient atom length.",
        "effects": [{"kind": "invalidates-assumption", "target": ar}],
    }, expect_ok=False)
    assert res["rc"] != 0, res
    body = res["out"] or {}
    assert body.get("code") == "E_VALIDATION", body
    assert "event_time" in (body.get("detail") or ""), body


def test_refuse_missing_claim(clean_substrate):
    ar = _seed_assumption()
    res = _submit_event({
        "source": "Source atom for refusal-missing-claim coverage; sufficient atom length required.",
        "event_time": "Event time atom for refusal-missing-claim coverage; sufficient atom length required.",
        "effects": [{"kind": "invalidates-assumption", "target": ar}],
    }, expect_ok=False)
    assert res["rc"] != 0, res
    body = res["out"] or {}
    assert body.get("code") == "E_VALIDATION", body
    assert "claim" in (body.get("detail") or ""), body


def test_refuse_empty_effects_list(clean_substrate):
    res = _submit_event({
        "source": "Source atom field for empty-effects refusal coverage path with sufficient atom length.",
        "event_time": "T+34h event time atom for empty-effects refusal coverage path with sufficient length.",
        "claim": "Event claim atom for empty-effects refusal coverage path with sufficient atom length.",
        "effects": [],
    }, expect_ok=False)
    assert res["rc"] != 0, res
    body = res["out"] or {}
    assert body.get("code") == "E_VALIDATION", body
    assert "effects" in (body.get("detail") or ""), body


def test_refuse_bad_effect_kind_enum(clean_substrate):
    ar = _seed_assumption()
    res = _submit_event({
        "source": "Source atom for effect-kind-enum-rejection refusal coverage path with sufficient length.",
        "event_time": "Event time atom for effect-kind-enum-rejection refusal coverage path; sufficient length.",
        "claim": "Event claim atom for effect-kind-enum-rejection refusal coverage path with sufficient length.",
        "effects": [{"kind": "invalidates-node", "target": ar}],
    }, expect_ok=False)
    assert res["rc"] != 0, res
    body = res["out"] or {}
    assert body.get("code") == "E_VALIDATION", body
    detail = body.get("detail") or ""
    assert "invalidates-node" in detail or "kind" in detail, body


def test_refuse_non_assumption_target_object_kind_handler(clean_substrate):
    """Non-assumption target refused at handler before T-43 SQL trigger fires."""
    dv = _seed_decision()
    res = _submit_event({
        "source": "Source atom for non-assumption-target refusal coverage path with sufficient atom length.",
        "event_time": "Event time atom for non-assumption-target refusal coverage path; sufficient length.",
        "claim": "Event claim atom for non-assumption-target refusal coverage path with sufficient atom length.",
        "effects": [{"kind": "invalidates-assumption", "target": dv}],
    }, expect_ok=False)
    assert res["rc"] != 0, res
    body = res["out"] or {}
    assert body.get("code") == "E_VALIDATION", body
    detail = body.get("detail") or ""
    assert ("assumption" in detail) and ("decision" in detail or "object_kind" in detail), body


def test_t43_sql_trigger_refuses_non_assumption_target_via_direct_insert(clean_substrate, db_path):
    """T-43 SQL trigger backstop fires when handler-side check is bypassed."""
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        # Find any non-assumption object_id in objects (e.g., session itself).
        row = conn.execute(
            "SELECT object_id, object_kind FROM objects "
            "WHERE object_kind != 'assumption' LIMIT 1"
        ).fetchone()
        assert row is not None, "no non-assumption object available for T-43 test"
        non_assumption_oid = row["object_id"]

        atom_row = conn.execute(
            "SELECT atom_id FROM text_atoms LIMIT 1"
        ).fetchone()
        if atom_row is None:
            sess_for_seed = conn.execute("SELECT session_id FROM sessions LIMIT 1").fetchone()[0]
            cur = conn.execute(
                "INSERT INTO text_atoms (atom_type, text, created_session_id) "
                "VALUES (?,?,?)",
                ("claim", "seed atom for T-43 trigger backstop test fixture body.", sess_for_seed),
            )
            atom_id = cur.lastrowid
        else:
            atom_id = atom_row["atom_id"]

        sess_row = conn.execute(
            "SELECT session_id FROM sessions ORDER BY session_id DESC LIMIT 1"
        ).fetchone()
        sess_id = sess_row["session_id"]

        # Insert event_ledger header directly (no trigger on header).
        cur = conn.execute(
            "INSERT INTO event_ledger "
            "(session_id, source_atom_id, event_time_atom_id, claim_atom_id) "
            "VALUES (?,?,?,?)",
            (sess_id, atom_id, atom_id, atom_id),
        )
        event_id = cur.lastrowid

        try:
            conn.execute(
                "INSERT INTO event_effects "
                "(event_id, ord, effect_kind, target_object_id) "
                "VALUES (?,?,?,?)",
                (event_id, 0, "invalidates-assumption", non_assumption_oid),
            )
            assert False, "T-43 trigger should have refused non-assumption target"
        except sqlite3.IntegrityError as e:
            assert "T43" in str(e) or "assumption" in str(e), str(e)
        finally:
            conn.rollback()
    finally:
        conn.close()


def test_object_registration_lands_in_objects_with_kind_event(clean_substrate, db_path):
    ar = _seed_assumption()
    res = _submit_event({
        "source": "Source atom for object-registration test path with sufficient atom length for support_claim.",
        "event_time": "Event time atom for object-registration test path; sufficient atom length for tier.",
        "claim": "Event claim atom for object-registration test path with sufficient atom length for support.",
        "effects": [{"kind": "invalidates-assumption", "target": ar}],
    })
    alias = res["out"]["result"]["alias"]
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute(
            "SELECT object_kind FROM objects WHERE alias=?", (alias,)
        ).fetchone()
        assert row is not None, "event alias not in objects"
        assert row["object_kind"] == "event"
    finally:
        conn.close()


def test_source_atom_too_short_refused(clean_substrate):
    ar = _seed_assumption()
    res = _submit_event({
        "source": "x",
        "event_time": "Event time atom field for source-too-short refusal coverage path with adequate length.",
        "claim": "Event claim atom for source-too-short refusal coverage path with sufficient atom length.",
        "effects": [{"kind": "invalidates-assumption", "target": ar}],
    }, expect_ok=False)
    assert res["rc"] != 0, res
    body = res["out"] or {}
    assert body.get("code") == "E_ATOM_LENGTH", body


def test_unresolvable_target_alias_refused(clean_substrate):
    res = _submit_event({
        "source": "Source atom for unresolvable-target refusal coverage path with sufficient atom length.",
        "event_time": "Event time atom for unresolvable-target refusal coverage path with sufficient length.",
        "claim": "Event claim atom for unresolvable-target refusal coverage path with sufficient atom length.",
        "effects": [{"kind": "invalidates-assumption", "target": "AR-S999-99"}],
    }, expect_ok=False)
    assert res["rc"] != 0, res


def test_unique_event_ord_refusal_via_explicit_collision(clean_substrate):
    """UNIQUE(event_id, ord) refuses duplicate-ord effects per same event."""
    ar1 = _seed_assumption("First seed for UNIQUE-ord collision test.")
    ar2 = _seed_assumption("Second seed for UNIQUE-ord collision test.")
    res = _submit_event({
        "source": "Source atom for UNIQUE-ord collision test path with sufficient atom length for support_claim.",
        "event_time": "Event time atom for UNIQUE-ord collision test path; sufficient atom length for tier.",
        "claim": "Event claim atom for UNIQUE-ord collision test path with sufficient atom length for support.",
        "effects": [
            {"kind": "invalidates-assumption", "target": ar1, "ord": 7},
            {"kind": "confirms-assumption", "target": ar2, "ord": 7},
        ],
    }, expect_ok=False)
    assert res["rc"] != 0, res


def test_per_session_seq_increments_across_events(clean_substrate):
    ar = _seed_assumption()
    r1 = _submit_event({
        "source": "Source atom event 1 for per-session-seq increment test path; sufficient atom length.",
        "event_time": "Event time atom event 1 for per-session-seq increment test; sufficient atom length.",
        "claim": "Event claim atom event 1 for per-session-seq increment test path; sufficient atom length.",
        "effects": [{"kind": "invalidates-assumption", "target": ar}],
    })["out"]["result"]
    r2 = _submit_event({
        "source": "Source atom event 2 for per-session-seq increment test path; sufficient atom length.",
        "event_time": "Event time atom event 2 for per-session-seq increment test; sufficient atom length.",
        "claim": "Event claim atom event 2 for per-session-seq increment test path; sufficient atom length.",
        "effects": [{"kind": "invalidates-assumption", "target": ar}],
    })["out"]["result"]
    seq1 = int(r1["alias"].split("-")[-1])
    seq2 = int(r2["alias"].split("-")[-1])
    assert seq2 == seq1 + 1, (r1, r2)


def test_inert_does_not_auto_flip_assumption_status(clean_substrate, db_path):
    """D-S204-1 C-3 + codex named edit #4: invalidates-assumption does NOT
    auto-set assumption_ledger.status='invalidated'."""
    ar = _seed_assumption()
    _submit_event({
        "source": "Source atom for inert-no-cascade test; event records claim but does not mutate AR.status.",
        "event_time": "Event time atom for inert-no-cascade test path; sufficient atom length for support_claim.",
        "claim": "Event claim invalidating an assumption; handler does not auto-flip AR.status='invalidated'.",
        "effects": [{"kind": "invalidates-assumption", "target": ar}],
    })
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute(
            "SELECT al.status FROM assumption_ledger al "
            "JOIN objects o ON o.object_id=al.object_id "
            "WHERE o.alias=?", (ar,)
        ).fetchone()
        # Default new assumption status is 'unverified'; the event must not
        # have flipped it to 'invalidated'.
        assert row is not None
        assert row["status"] != "invalidated", row["status"]
    finally:
        conn.close()


def test_refuse_confirms_assumption_non_assumption_target_handler(clean_substrate):
    """Reviewer F-2 fix: confirms-assumption against non-assumption target
    refused symmetrically with invalidates-assumption (both effect kinds bind
    target.object_kind=assumption at v1)."""
    dv = _seed_decision()
    res = _submit_event({
        "source": "Source atom for confirms-assumption non-assumption-target refusal symmetry coverage.",
        "event_time": "Event time atom for confirms-assumption non-assumption-target refusal symmetry test.",
        "claim": "Event claim atom for confirms-assumption non-assumption-target refusal symmetry coverage path.",
        "effects": [{"kind": "confirms-assumption", "target": dv}],
    }, expect_ok=False)
    assert res["rc"] != 0, res
    body = res["out"] or {}
    assert body.get("code") == "E_VALIDATION", body
    detail = body.get("detail") or ""
    assert "confirms-assumption" in detail and ("assumption" in detail or "object_kind" in detail), body


def test_refuse_implicit_default_ord_collision(clean_substrate):
    """Reviewer F-1 fix: mixed explicit-and-default ord refused at handler.

    Effect[0].ord=1 explicit + effect[1] no ord (defaults to i=1) collide;
    handler refuses with E_VALIDATION before SQL UNIQUE fires.
    """
    ar1 = _seed_assumption("First assumption seed for default-ord collision detection test path.")
    ar2 = _seed_assumption("Second assumption seed for default-ord collision detection test path.")
    res = _submit_event({
        "source": "Source atom for implicit-default-ord collision refusal path; sufficient atom length.",
        "event_time": "Event time atom for implicit-default-ord collision refusal path; sufficient length.",
        "claim": "Event claim atom for implicit-default-ord collision refusal coverage; sufficient length.",
        "effects": [
            {"kind": "invalidates-assumption", "target": ar1, "ord": 1},
            {"kind": "confirms-assumption", "target": ar2},  # default ord = i = 1, collides
        ],
    }, expect_ok=False)
    assert res["rc"] != 0, res
    body = res["out"] or {}
    assert body.get("code") == "E_VALIDATION", body
    assert "ord" in (body.get("detail") or ""), body


def test_refuse_empty_string_reason_atom(clean_substrate):
    """Reviewer F-4 fix: empty-string reason refused at handler with
    E_VALIDATION (mirrors cycle.py F-02 fix; not E_ATOM_LENGTH from atom layer)."""
    ar = _seed_assumption()
    res = _submit_event({
        "source": "Source atom for empty-string-reason refusal path; sufficient atom length for support_claim.",
        "event_time": "Event time atom for empty-string-reason refusal path; sufficient atom length for tier.",
        "claim": "Event claim atom for empty-string-reason refusal path; sufficient atom length for support_claim.",
        "effects": [{"kind": "invalidates-assumption", "target": ar, "reason": ""}],
    }, expect_ok=False)
    assert res["rc"] != 0, res
    body = res["out"] or {}
    assert body.get("code") == "E_VALIDATION", body
    assert "reason" in (body.get("detail") or ""), body


def test_optional_reason_atom_pinned(clean_substrate, db_path):
    ar = _seed_assumption()
    res = _submit_event({
        "source": "Source atom for optional-reason-pinned coverage path; sufficient atom length for support_claim.",
        "event_time": "Event time atom for optional-reason-pinned coverage path; sufficient atom length.",
        "claim": "Event claim atom for optional-reason-pinned coverage path; sufficient atom length for support.",
        "effects": [
            {
                "kind": "invalidates-assumption",
                "target": ar,
                "reason": "Optional reason atom should pin into text_atoms and link via reason_atom_id.",
            },
        ],
    })
    effect_id = res["out"]["result"]["effects"][0]["effect_id"]
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute(
            "SELECT reason_atom_id FROM event_effects WHERE effect_id=?",
            (effect_id,),
        ).fetchone()
        assert row is not None
        assert row["reason_atom_id"] is not None
    finally:
        conn.close()
