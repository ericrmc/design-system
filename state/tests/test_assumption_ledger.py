"""Tests for assumption-ledger v1 typed primitive (S198 DV-S198-1).

Coverage:
- Default-status admit: minimal payload {statement} admits with status=unverified.
- Status enum rejection: bad status value refused with E_VALIDATION.
- Sub-type without conflict refused: sub_type provided when status!=active-with-conflict
  refused via handler-side check before SQL CHECK.
- ACTIVE-WITH-CONFLICT four-field discipline: status=active-with-conflict requires
  sub_type AND four conflict atoms (action_commitment + both_source_citation +
  resolution_path + expiry_trigger) all NOT NULL.
- Sub-type enum rejection: bad sub_type refused with E_VALIDATION.
- Object-registration: row registers as object with alias AR-S<wno>-<seq> and
  object_kind='assumption' (no _ledger suffix per D-6 P-1 stance).
- Statement atom-length: outside 8-480 refused.
- Optional origin_decision alias resolves.
- Status-update transition admits: assumption-status-update mutates status and
  records last_transition_decision_object_id FK.
- Status-update without citing_decision refused with E_VALIDATION.
- Status-update transition TO active-with-conflict requires conflict atoms.
- Status-update transition OUT of active-with-conflict clears sub_type.
"""
from __future__ import annotations

import json
import re
import sqlite3

from conftest import _run_cli


def _seed_decision() -> str:
    """Submit a smallest-possible decision_v2 row so we have a DV alias to cite
    as origin_decision and as citing_decision in transitions."""
    res = _run_cli([
        "submit", "decision-record", "--payload", json.dumps({
            "title": "Seed decision-record for assumption-ledger tests citing path.",
            "kind": "procedural",
            "outcome_type": "adopt",
            "target_kind": "process_rule",
            "target_key": "test-seed-rule-for-assumption-tests",
            "supports": [],
            "effects": [],
            "alternatives": [],
        }),
    ])
    return res["out"]["result"]["alias"]


def _submit_assumption(payload: dict, expect_ok: bool = True) -> dict:
    res = _run_cli([
        "submit", "assumption", "--payload", json.dumps(payload),
    ], expect_ok=expect_ok)
    if not expect_ok and res["out"] is None and res["err"]:
        try:
            res["out"] = json.loads(res["err"])
        except json.JSONDecodeError:
            pass
    return res


def _submit_status_update(payload: dict, expect_ok: bool = True) -> dict:
    res = _run_cli([
        "submit", "assumption-status-update", "--payload", json.dumps(payload),
    ], expect_ok=expect_ok)
    if not expect_ok and res["out"] is None and res["err"]:
        try:
            res["out"] = json.loads(res["err"])
        except json.JSONDecodeError:
            pass
    return res


def test_admit_minimal_payload_returns_alias_and_default_status(clean_substrate):
    res = _submit_assumption({
        "statement": "Test minimal admit: statement-only payload admits with default unverified status.",
    })
    assert res["rc"] == 0, res
    r = res["out"]["result"]
    assert re.match(r"^AR-S\d{3,}-\d+$", r["alias"]), r
    assert r["status"] == "unverified"
    assert r["sub_type"] is None
    assert r["origin_decision_object_id"] is None


def test_object_registration_lands_in_objects(clean_substrate, db_path):
    res = _submit_assumption({
        "statement": "Object-registration test: row should appear in objects with kind=assumption (not _ledger suffix).",
    })
    alias = res["out"]["result"]["alias"]
    conn = sqlite3.connect(str(db_path))
    try:
        row = conn.execute(
            "SELECT object_kind, typed_row_id FROM objects WHERE alias=?", (alias,)
        ).fetchone()
    finally:
        conn.close()
    assert row is not None, f"alias {alias} not registered in objects"
    assert row[0] == "assumption"
    assert row[1] == res["out"]["result"]["assumption_id"]


def test_status_enum_rejection(clean_substrate):
    res = _submit_assumption({
        "statement": "Test status enum: 'monitored' is not in 6-value set per P-1 stance adopted at D-6.",
        "status": "monitored",
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_VALIDATION"
    assert "status" in res["out"]["detail"]


def test_sub_type_without_conflict_refused(clean_substrate):
    res = _submit_assumption({
        "statement": "Test that providing sub_type without status=active-with-conflict is refused.",
        "sub_type": "rolling-renewal",
        "status": "assumed",
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_VALIDATION"
    assert "sub_type" in res["out"]["detail"]


def test_sub_type_enum_rejection(clean_substrate):
    res = _submit_assumption({
        "statement": "Test sub_type enum rejection: 'invented-subtype' is not in 3-value set adopted at D-6.",
        "status": "active-with-conflict",
        "sub_type": "invented-subtype",
        "action_commitment": "Test action commitment under conflict; placeholder under disaster-recovery flavor.",
        "both_source_citation": "Source A says X; Source B says Y; divergence magnitude approximately N units.",
        "resolution_path": "Day-N reconciliation pass cross-matching A vs B; closure requires deduplicated count.",
        "expiry_trigger": "Day-N checkpoint or independent census team; whichever fires first.",
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_VALIDATION"
    assert "sub_type" in res["out"]["detail"]


def test_active_with_conflict_requires_four_fields(clean_substrate):
    # All four conflict atoms missing
    res = _submit_assumption({
        "statement": "Test conflict-discipline incomplete: status=active-with-conflict needs four atoms.",
        "status": "active-with-conflict",
        "sub_type": "plan-vs-resource",
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_VALIDATION"
    detail = res["out"]["detail"]
    for needed in ("action_commitment", "both_source_citation", "resolution_path", "expiry_trigger"):
        assert needed in detail, f"missing field name {needed!r} in refusal detail"


def test_active_with_conflict_requires_sub_type(clean_substrate):
    res = _submit_assumption({
        "statement": "Test conflict-discipline incomplete: sub_type also required when status=active-with-conflict.",
        "status": "active-with-conflict",
        "action_commitment": "Plan §1 adopts value X with envelope Y; under-budgeting is the asymmetric error.",
        "both_source_citation": "Source A reports X via method P; Source B reports Y via method Q; magnitude Z.",
        "resolution_path": "Day-N reconciliation step W cross-matches; closure requires aggregated deduplicated value.",
        "expiry_trigger": "Day-N checkpoint W; on no resolution, escalate per response-plan section.",
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_VALIDATION"
    assert "sub_type" in res["out"]["detail"]


def test_active_with_conflict_admits_with_full_discipline(clean_substrate):
    res = _submit_assumption({
        "statement": "Disaster-recovery-flavored A-018-style assumption with full four-field discipline at insert.",
        "status": "active-with-conflict",
        "sub_type": "rolling-renewal",
        "action_commitment": "Plan §F-4 adopts 3-passes-plus-6-hours-per-day envelope; rolling snapshot every cycle.",
        "both_source_citation": "Source A satellite logs Day-7 4 passes; Source B operator log Day-7 2.5 passes magnitude 1.5.",
        "resolution_path": "Cycle-3 evaluation; trend monitor active; closure path-(a) at 4-passes-plus-12-hours achieved.",
        "expiry_trigger": "Cycle-N checkpoint or operator-named-mandate; whichever fires first per rolling-renewal design.",
    })
    assert res["rc"] == 0, res
    r = res["out"]["result"]
    assert r["status"] == "active-with-conflict"
    assert r["sub_type"] == "rolling-renewal"


def test_atom_length_refused_short_statement(clean_substrate):
    res = _submit_assumption({"statement": "tiny"}, expect_ok=False)  # 4 chars, below 8
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_ATOM_LENGTH"


def test_optional_origin_decision_resolves(clean_substrate):
    dv_alias = _seed_decision()
    res = _submit_assumption({
        "statement": "Test that optional origin_decision alias resolves to objects.alias graph at insert time.",
        "origin_decision": dv_alias,
    })
    assert res["rc"] == 0, res
    assert res["out"]["result"]["origin_decision_object_id"] is not None


def test_unresolvable_origin_decision_refused(clean_substrate):
    res = _submit_assumption({
        "statement": "Test that an unresolvable origin_decision alias is refused with E_REFUSAL_T01.",
        "origin_decision": "DV-S999-99",
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_REFUSAL_T01"


def test_status_update_admit_basic(clean_substrate):
    dv_alias = _seed_decision()
    res = _submit_assumption({
        "statement": "Status-update target: register as unverified, transition to closed via citing_decision.",
    })
    alias = res["out"]["result"]["alias"]
    upd = _submit_status_update({
        "assumption": alias,
        "new_status": "closed",
        "citing_decision": dv_alias,
        "closure_shape": "completion",
    })
    assert upd["rc"] == 0, upd
    r = upd["out"]["result"]
    assert r["from_status"] == "unverified"
    assert r["to_status"] == "closed"
    assert r["citing_decision_object_id"] is not None
    assert r["closure_shape"] == "completion"


def test_status_update_requires_citing_decision(clean_substrate):
    res = _submit_assumption({
        "statement": "Status-update target: transition without citing_decision should be refused per D-6 reject-history-table synthesis.",
    })
    alias = res["out"]["result"]["alias"]
    upd = _submit_status_update({
        "assumption": alias,
        "new_status": "closed",
    }, expect_ok=False)
    assert upd["rc"] != 0
    assert upd["out"]["code"] == "E_VALIDATION"
    assert "citing_decision" in upd["out"]["detail"]


def test_status_update_to_active_with_conflict_requires_atoms(clean_substrate):
    dv_alias = _seed_decision()
    res = _submit_assumption({
        "statement": "Status-update target: transition TO active-with-conflict needs four conflict atoms.",
    })
    alias = res["out"]["result"]["alias"]
    upd = _submit_status_update({
        "assumption": alias,
        "new_status": "active-with-conflict",
        "citing_decision": dv_alias,
        "sub_type": "plan-vs-resource",
        # Conflict atoms missing — handler refuses
    }, expect_ok=False)
    assert upd["rc"] != 0
    assert upd["out"]["code"] == "E_VALIDATION"


def test_status_update_to_active_with_conflict_admit(clean_substrate):
    dv_alias = _seed_decision()
    res = _submit_assumption({
        "statement": "Status-update target: full transition to active-with-conflict with four atoms admits.",
    })
    alias = res["out"]["result"]["alias"]
    upd = _submit_status_update({
        "assumption": alias,
        "new_status": "active-with-conflict",
        "citing_decision": dv_alias,
        "sub_type": "contested-authority",
        "action_commitment": "Plan §X adopts dual-channel routing pending resolution; both channels operative.",
        "both_source_citation": "Authority A cites CPA §11 life-safety; Authority B cites Article X §3 non-life-safety.",
        "resolution_path": "Day-N final ruling from joint authority panel; dual-channel safety net retired on rule.",
        "expiry_trigger": "Day-N final ruling deadline T+302h or escalation to central government if no rule.",
    })
    assert upd["rc"] == 0, upd
    r = upd["out"]["result"]
    assert r["from_status"] == "unverified"
    assert r["to_status"] == "active-with-conflict"


def test_status_update_unresolvable_assumption_refused(clean_substrate):
    dv_alias = _seed_decision()
    upd = _submit_status_update({
        "assumption": "AR-S999-99",
        "new_status": "closed",
        "citing_decision": dv_alias,
    }, expect_ok=False)
    assert upd["rc"] != 0
    assert upd["out"]["code"] == "E_REFUSAL_T01"


def test_status_update_alias_not_assumption_refused(clean_substrate):
    """An alias that resolves to a non-assumption object (e.g., the decision itself)
    should refuse with E_NOT_FOUND from the assumption-row JOIN check."""
    dv_alias = _seed_decision()
    upd = _submit_status_update({
        "assumption": dv_alias,  # a DV alias, not AR
        "new_status": "closed",
        "citing_decision": dv_alias,
    }, expect_ok=False)
    assert upd["rc"] != 0
    assert upd["out"]["code"] == "E_NOT_FOUND"


def test_all_six_statuses_admit(clean_substrate):
    """Every value in the closed 6-status enum should admit at insert.

    DV-S201-1 closure-shape coupling: status='closed' requires closure_shape;
    status='superseded' admits NULL or 'supersession'; others forbid it.
    """
    payloads = [
        {"status": "unverified"},
        {"status": "assumed"},
        {"status": "closed", "closure_shape": "completion"},
        {"status": "superseded"},
        {"status": "invalidated"},
    ]
    # active-with-conflict tested separately because it requires four atoms
    for extra in payloads:
        st = extra["status"]
        res = _submit_assumption({
            "statement": f"Admit-test for status={st}: closed enum should admit this base value at insert per D-6 P-1.",
            **extra,
        })
        assert res["rc"] == 0, (st, res)
        assert res["out"]["result"]["status"] == st


def test_status_update_out_of_conflict_clears_sub_type(clean_substrate, db_path):
    """Reviewer RF-75 fix: transition OUT of active-with-conflict must clear sub_type
    (per CHECK sub_type IS NULL OR status='active-with-conflict'). The handler
    auto-clears sub_type when transitioning out and existing row had sub_type set."""
    dv_alias = _seed_decision()
    res = _submit_assumption({
        "statement": "Transition-out target: insert with status=active-with-conflict carrying sub_type then transition to closed.",
        "status": "active-with-conflict",
        "sub_type": "plan-vs-resource",
        "action_commitment": "Plan §X adopts envelope Y; under-budgeting is the asymmetric error this round.",
        "both_source_citation": "Source A reports value U via method P; Source B reports value V via method Q.",
        "resolution_path": "Day-N reconciliation pass W cross-matches; closure requires deduplicated count Z.",
        "expiry_trigger": "Day-N checkpoint W; on no resolution, escalate to central authority per response-plan.",
    })
    alias = res["out"]["result"]["alias"]
    assumption_id = res["out"]["result"]["assumption_id"]

    # Transition to closed; sub_type must auto-clear or SQL CHECK refuses.
    upd = _submit_status_update({
        "assumption": alias,
        "new_status": "closed",
        "citing_decision": dv_alias,
        "closure_shape": "convergence",
    })
    assert upd["rc"] == 0, upd
    r = upd["out"]["result"]
    assert r["from_status"] == "active-with-conflict"
    assert r["to_status"] == "closed"
    assert r["closure_shape"] == "convergence"

    # Verify sub_type was cleared at the row level.
    conn = sqlite3.connect(str(db_path))
    try:
        row = conn.execute(
            "SELECT status, sub_type FROM assumption_ledger WHERE assumption_id=?",
            (assumption_id,),
        ).fetchone()
    finally:
        conn.close()
    assert row[0] == "closed"
    assert row[1] is None, f"sub_type should be NULL after transition out of active-with-conflict; got {row[1]!r}"


def test_alias_sequence_per_session(clean_substrate):
    """Subsequent assumption submits in the same session should produce
    AR-S<wno>-1, AR-S<wno>-2, AR-S<wno>-3 sequence."""
    aliases = []
    for i in range(3):
        res = _submit_assumption({
            "statement": f"Sequence test row {i}: alias should land at AR-S<wno>-(i+1) per per-session COUNT discipline.",
        })
        aliases.append(res["out"]["result"]["alias"])
    seq_nums = [int(a.rsplit("-", 1)[1]) for a in aliases]
    assert seq_nums == [1, 2, 3], aliases


# ============================================================================
# DV-S201-1 closure-shape coupling tests (migration 051).
# ============================================================================


def test_init_closed_without_closure_shape_refused(clean_substrate):
    res = _submit_assumption({
        "statement": "Init with status=closed and no closure_shape should be refused per DV-S201-1.",
        "status": "closed",
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_VALIDATION"
    assert "closure_shape" in res["out"]["detail"]


def test_init_closed_with_closure_shape_admits(clean_substrate):
    for shape in ("convergence", "completion", "containment-resolved",
                  "supersession", "stable-held"):
        res = _submit_assumption({
            "statement": f"Init closed-with-shape={shape}: 5 canonical shapes all admit at insert per DV-S201-1.",
            "status": "closed",
            "closure_shape": shape,
        })
        assert res["rc"] == 0, (shape, res)
        assert res["out"]["result"]["closure_shape"] == shape


def test_closure_shape_enum_rejection(clean_substrate):
    res = _submit_assumption({
        "statement": "Bogus closure_shape value should be refused with E_VALIDATION naming the closed enum.",
        "status": "closed",
        "closure_shape": "rolling-cycle-fudge",
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_VALIDATION"
    assert "closure_shape" in res["out"]["detail"]


def test_unverified_with_closure_shape_refused(clean_substrate):
    res = _submit_assumption({
        "statement": "Unverified status with closure_shape should be refused (premature labelling).",
        "status": "unverified",
        "closure_shape": "convergence",
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_VALIDATION"
    assert "closure_shape" in res["out"]["detail"]


def test_assumed_with_closure_shape_refused(clean_substrate):
    res = _submit_assumption({
        "statement": "Assumed status with closure_shape should be refused (premature labelling per DV-S201-1).",
        "status": "assumed",
        "closure_shape": "completion",
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_VALIDATION"


def test_active_with_conflict_with_closure_shape_refused(clean_substrate):
    res = _submit_assumption({
        "statement": "active-with-conflict with closure_shape should be refused per DV-S201-1 status-shape coupling.",
        "status": "active-with-conflict",
        "sub_type": "plan-vs-resource",
        "action_commitment": "Plan §X adopts envelope Y; under-budgeting is the asymmetric error this round.",
        "both_source_citation": "Source A reports value U via method P; Source B reports value V via method Q.",
        "resolution_path": "Day-N reconciliation pass W cross-matches; closure requires deduplicated count Z.",
        "expiry_trigger": "Day-N checkpoint W; on no resolution, escalate to central authority per response-plan.",
        "closure_shape": "convergence",
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_VALIDATION"


def test_invalidated_with_closure_shape_refused(clean_substrate):
    res = _submit_assumption({
        "statement": "Invalidated status with closure_shape should be refused (ontologically distinct exit).",
        "status": "invalidated",
        "closure_shape": "completion",
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_VALIDATION"
    assert "invalidat" in res["out"]["detail"].lower()


def test_superseded_with_supersession_admits(clean_substrate):
    res = _submit_assumption({
        "statement": "Superseded status with closure_shape='supersession' should admit per DV-S201-1 narrowing.",
        "status": "superseded",
        "closure_shape": "supersession",
    })
    assert res["rc"] == 0, res
    assert res["out"]["result"]["closure_shape"] == "supersession"


def test_superseded_with_other_shape_refused(clean_substrate):
    res = _submit_assumption({
        "statement": "Superseded with non-supersession shape should be refused per DV-S201-1 superseded-narrowing.",
        "status": "superseded",
        "closure_shape": "convergence",
    }, expect_ok=False)
    assert res["rc"] != 0
    assert res["out"]["code"] == "E_VALIDATION"


def test_superseded_without_shape_admits(clean_substrate):
    res = _submit_assumption({
        "statement": "Superseded without closure_shape should admit (NULL is the legacy compatibility path).",
        "status": "superseded",
    })
    assert res["rc"] == 0, res
    assert res["out"]["result"]["closure_shape"] is None


def test_status_update_to_closed_requires_shape(clean_substrate):
    dv_alias = _seed_decision()
    res = _submit_assumption({
        "statement": "Transition target: register, transition to closed without closure_shape should refuse.",
    })
    alias = res["out"]["result"]["alias"]
    upd = _submit_status_update({
        "assumption": alias,
        "new_status": "closed",
        "citing_decision": dv_alias,
    }, expect_ok=False)
    assert upd["rc"] != 0
    assert upd["out"]["code"] == "E_VALIDATION"
    assert "closure_shape" in upd["out"]["detail"]


def test_status_update_to_closed_with_shape_admits(clean_substrate, db_path):
    dv_alias = _seed_decision()
    res = _submit_assumption({
        "statement": "Transition target: register, transition to closed with closure_shape=stable-held admits.",
    })
    alias = res["out"]["result"]["alias"]
    upd = _submit_status_update({
        "assumption": alias,
        "new_status": "closed",
        "citing_decision": dv_alias,
        "closure_shape": "stable-held",
    })
    assert upd["rc"] == 0, upd
    assert upd["out"]["result"]["closure_shape"] == "stable-held"

    conn = sqlite3.connect(str(db_path))
    try:
        row = conn.execute(
            "SELECT status, closure_shape FROM assumption_ledger "
            "WHERE assumption_id=?",
            (res["out"]["result"]["assumption_id"],),
        ).fetchone()
    finally:
        conn.close()
    assert row[0] == "closed"
    assert row[1] == "stable-held"


def test_status_update_out_of_closed_clears_shape(clean_substrate, db_path):
    """Transitioning OUT of closed back to a pre-closure status auto-clears
    closure_shape to satisfy the coupling CHECK."""
    dv_alias = _seed_decision()
    res = _submit_assumption({
        "statement": "Transition-out-of-closed target: insert closed-with-shape, transition to invalidated.",
        "status": "closed",
        "closure_shape": "completion",
    })
    alias = res["out"]["result"]["alias"]
    assumption_id = res["out"]["result"]["assumption_id"]

    upd = _submit_status_update({
        "assumption": alias,
        "new_status": "invalidated",
        "citing_decision": dv_alias,
    })
    assert upd["rc"] == 0, upd
    assert upd["out"]["result"]["closure_shape"] is None

    conn = sqlite3.connect(str(db_path))
    try:
        row = conn.execute(
            "SELECT status, closure_shape FROM assumption_ledger "
            "WHERE assumption_id=?",
            (assumption_id,),
        ).fetchone()
    finally:
        conn.close()
    assert row[0] == "invalidated"
    assert row[1] is None


def test_status_update_to_superseded_with_other_shape_refused(clean_substrate):
    dv_alias = _seed_decision()
    res = _submit_assumption({
        "statement": "Transition target for superseded with bad shape: should refuse non-supersession value.",
    })
    alias = res["out"]["result"]["alias"]
    upd = _submit_status_update({
        "assumption": alias,
        "new_status": "superseded",
        "citing_decision": dv_alias,
        "closure_shape": "completion",
    }, expect_ok=False)
    assert upd["rc"] != 0
    assert upd["out"]["code"] == "E_VALIDATION"


def test_status_update_to_invalidated_with_shape_refused(clean_substrate):
    dv_alias = _seed_decision()
    res = _submit_assumption({
        "statement": "Transition target for invalidated with shape: should refuse closure_shape.",
    })
    alias = res["out"]["result"]["alias"]
    upd = _submit_status_update({
        "assumption": alias,
        "new_status": "invalidated",
        "citing_decision": dv_alias,
        "closure_shape": "completion",
    }, expect_ok=False)
    assert upd["rc"] != 0
    assert upd["out"]["code"] == "E_VALIDATION"


def test_closed_to_superseded_with_carry_forward_refused(clean_substrate):
    """RF-86/RF-89: closed(convergence) to superseded without explicit closure_shape
    refuses because the carried-forward 'convergence' violates superseded narrowing
    (superseded admits NULL or 'supersession' only)."""
    dv_alias = _seed_decision()
    res = _submit_assumption({
        "statement": "Transition target: insert closed-with-convergence then transition to superseded without override.",
        "status": "closed",
        "closure_shape": "convergence",
    })
    alias = res["out"]["result"]["alias"]
    upd = _submit_status_update({
        "assumption": alias,
        "new_status": "superseded",
        "citing_decision": dv_alias,
    }, expect_ok=False)
    assert upd["rc"] != 0
    assert upd["out"]["code"] == "E_VALIDATION"
    assert "superseded" in upd["out"]["detail"].lower()


def test_closed_to_superseded_with_explicit_supersession_admits(clean_substrate, db_path):
    """RF-86/RF-89: closed(convergence) to superseded with explicit closure_shape=
    'supersession' admits (caller deliberately narrows)."""
    dv_alias = _seed_decision()
    res = _submit_assumption({
        "statement": "Transition target: closed-with-convergence then transition to superseded with explicit supersession.",
        "status": "closed",
        "closure_shape": "convergence",
    })
    alias = res["out"]["result"]["alias"]
    assumption_id = res["out"]["result"]["assumption_id"]

    upd = _submit_status_update({
        "assumption": alias,
        "new_status": "superseded",
        "citing_decision": dv_alias,
        "closure_shape": "supersession",
    })
    assert upd["rc"] == 0, upd
    assert upd["out"]["result"]["closure_shape"] == "supersession"

    conn = sqlite3.connect(str(db_path))
    try:
        row = conn.execute(
            "SELECT status, closure_shape FROM assumption_ledger "
            "WHERE assumption_id=?",
            (assumption_id,),
        ).fetchone()
    finally:
        conn.close()
    assert row[0] == "superseded"
    assert row[1] == "supersession"


def test_closed_to_superseded_with_explicit_null_admits(clean_substrate, db_path):
    """RF-86/RF-89: closed(convergence) to superseded with explicit closure_shape=
    null admits (legacy compat path; caller deliberately drops shape)."""
    dv_alias = _seed_decision()
    res = _submit_assumption({
        "statement": "Transition target: closed-with-convergence then transition to superseded with explicit null shape.",
        "status": "closed",
        "closure_shape": "convergence",
    })
    alias = res["out"]["result"]["alias"]
    assumption_id = res["out"]["result"]["assumption_id"]

    upd = _submit_status_update({
        "assumption": alias,
        "new_status": "superseded",
        "citing_decision": dv_alias,
        "closure_shape": None,
    })
    assert upd["rc"] == 0, upd
    assert upd["out"]["result"]["closure_shape"] is None

    conn = sqlite3.connect(str(db_path))
    try:
        row = conn.execute(
            "SELECT status, closure_shape FROM assumption_ledger "
            "WHERE assumption_id=?",
            (assumption_id,),
        ).fetchone()
    finally:
        conn.close()
    assert row[0] == "superseded"
    assert row[1] is None


def test_superseded_to_closed_carry_forward_supersession(clean_substrate, db_path):
    """RF-86: superseded(supersession) to closed without explicit closure_shape
    carries forward 'supersession' as the closed shape (admitted because
    'supersession' is in the closed-CHECK enum). Documents intentional
    carry-forward semantic; reviewer RF-87 mistakenly flagged this as a bug."""
    dv_alias = _seed_decision()
    res = _submit_assumption({
        "statement": "Transition target: superseded-with-supersession then transition to closed without override.",
        "status": "superseded",
        "closure_shape": "supersession",
    })
    alias = res["out"]["result"]["alias"]
    assumption_id = res["out"]["result"]["assumption_id"]

    upd = _submit_status_update({
        "assumption": alias,
        "new_status": "closed",
        "citing_decision": dv_alias,
    })
    assert upd["rc"] == 0, upd
    assert upd["out"]["result"]["closure_shape"] == "supersession"

    conn = sqlite3.connect(str(db_path))
    try:
        row = conn.execute(
            "SELECT status, closure_shape FROM assumption_ledger "
            "WHERE assumption_id=?",
            (assumption_id,),
        ).fetchone()
    finally:
        conn.close()
    assert row[0] == "closed"
    assert row[1] == "supersession"


def test_superseded_to_closed_with_override_shape_admits(clean_substrate, db_path):
    """RF-86: superseded(supersession) to closed with explicit closure_shape='completion'
    overrides the carry-forward."""
    dv_alias = _seed_decision()
    res = _submit_assumption({
        "statement": "Transition target: superseded-with-supersession then transition to closed-with-completion.",
        "status": "superseded",
        "closure_shape": "supersession",
    })
    alias = res["out"]["result"]["alias"]
    assumption_id = res["out"]["result"]["assumption_id"]

    upd = _submit_status_update({
        "assumption": alias,
        "new_status": "closed",
        "citing_decision": dv_alias,
        "closure_shape": "completion",
    })
    assert upd["rc"] == 0, upd
    assert upd["out"]["result"]["closure_shape"] == "completion"

    conn = sqlite3.connect(str(db_path))
    try:
        row = conn.execute(
            "SELECT status, closure_shape FROM assumption_ledger "
            "WHERE assumption_id=?",
            (assumption_id,),
        ).fetchone()
    finally:
        conn.close()
    assert row[0] == "closed"
    assert row[1] == "completion"
