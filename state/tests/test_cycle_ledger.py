"""Tests for cycle-ledger v1 typed primitive (S203 DV-S203-1, OI-S196-6 close).

Coverage:
- Admit minimal payload: subject + snapshot + classification=non-substantial
  admits with auto cycle_no=0 + alias CYC-S<wno>-<seq>.
- Admit substantial-with-reason: classification=substantial requires
  classification_reason atom (D-9 D-2 synthesis).
- Refuse substantial-without-reason: handler-side actionable refusal naming
  the missing field (E_VALIDATION) before SQL CHECK fires.
- Classification enum rejection: bad classification refused with E_VALIDATION.
- Subject allowlist v1 (handler): non-assumption subject (e.g. DV alias)
  refused with E_VALIDATION naming the v1 allowlist.
- Subject allowlist v1 (T-42 SQL trigger backstop): the SQL-layer trigger
  fires when handler-side check is bypassed by direct SQL.
- Auto cycle_no monotonic: successive cycles for same subject get cycle_no
  0, 1, 2 via _next_cycle_no_for_subject (max+1).
- UNIQUE(subject, cycle_no) refusal: explicit cycle_no override colliding
  with existing row refused via SQL UNIQUE.
- Optional citing_supersession alias resolves; unresolvable alias refused
  with E_REFUSAL_T01.
- Snapshot atom-length: outside 8-480 chars refused with E_ATOM_LENGTH.
- Object-registration: row registers as object with alias CYC-S<wno>-<seq>
  and object_kind='cycle' (drops _ledger suffix per D-9 C-5).
- Subject alias unresolvable: refused with E_REFUSAL_T01.
- Cycle_no override admits: explicit cycle_no=5 lands at 5 (no strict +1).
- Per-session seq: alias seq increments across cycles regardless of subject.
"""
from __future__ import annotations

import json
import re
import sqlite3

from conftest import PRIMARY_DB, _run_cli


def _seed_assumption(statement: str = "Seed assumption for cycle_ledger tests subject path.") -> str:
    """Create an assumption_ledger row to use as a cycle subject; returns AR alias."""
    res = _run_cli([
        "submit", "assumption", "--payload", json.dumps({
            "statement": statement,
        }),
    ])
    return res["out"]["result"]["alias"]


def _seed_decision() -> str:
    """Create a procedural decision_v2 to use as a non-allowlist subject for refusal tests."""
    res = _run_cli([
        "submit", "decision-record", "--payload", json.dumps({
            "title": "Seed decision-record for cycle_ledger non-allowlist subject test.",
            "kind": "procedural",
            "outcome_type": "adopt",
            "target_kind": "process_rule",
            "target_key": "test-seed-rule-for-cycle-tests",
            "supports": [],
            "effects": [],
            "alternatives": [],
        }),
    ])
    return res["out"]["result"]["alias"]


def _seed_supersession(source_alias: str, target_alias: str) -> str:
    """Create a supersession_ledger row for citing_supersession path tests."""
    res = _run_cli([
        "submit", "supersession-ledger", "--payload", json.dumps({
            "source": source_alias,
            "target": target_alias,
            "relation_kind": "supersedes-fully",
            "reason": "Seed supersession for cycle_ledger citing_supersession path test coverage.",
        }),
    ])
    return res["out"]["result"]["alias"]


def _submit_cycle(payload: dict, expect_ok: bool = True) -> dict:
    res = _run_cli([
        "submit", "cycle", "--payload", json.dumps(payload),
    ], expect_ok=expect_ok)
    if not expect_ok and res["out"] is None and res["err"]:
        try:
            res["out"] = json.loads(res["err"])
        except json.JSONDecodeError:
            pass
    return res


def test_admit_minimal_payload_non_substantial_returns_alias_and_cycle_no_zero(clean_substrate):
    ar = _seed_assumption()
    res = _submit_cycle({
        "subject": ar,
        "snapshot": "Day-1 cycle observation: allocation steady at baseline; no movement vs prior cycle.",
        "classification": "non-substantial",
    })
    assert res["rc"] == 0, res
    r = res["out"]["result"]
    assert re.match(r"^CYC-S\d{3,}-\d+$", r["alias"]), r
    assert r["cycle_no"] == 0
    assert r["classification"] == "non-substantial"


def test_admit_substantial_with_reason_succeeds(clean_substrate):
    ar = _seed_assumption()
    res = _submit_cycle({
        "subject": ar,
        "snapshot": "Cycle 1: allocation increased from 1+4h to 3+6h satellite-uplink; provincial demand stabilising.",
        "classification": "substantial",
        "classification_reason": "Allocation moved closure-path-(a) eligibility candidate; trigger-counter improvement-cycle 1 of 3.",
    })
    assert res["rc"] == 0, res
    r = res["out"]["result"]
    assert r["classification"] == "substantial"


def test_refuse_substantial_without_reason_with_actionable_validation(clean_substrate):
    ar = _seed_assumption()
    res = _submit_cycle({
        "subject": ar,
        "snapshot": "Cycle 1 substantial movement: allocation increased; demand pattern shifting.",
        "classification": "substantial",
    }, expect_ok=False)
    assert res["rc"] != 0, res
    body = res["out"] or {}
    assert body.get("code") == "E_VALIDATION", body
    assert "classification_reason" in (body.get("detail") or ""), body


def test_classification_enum_rejection(clean_substrate):
    ar = _seed_assumption()
    res = _submit_cycle({
        "subject": ar,
        "snapshot": "Cycle observation with bad classification value to test enum rejection path.",
        "classification": "rolling-renewal",
    }, expect_ok=False)
    assert res["rc"] != 0, res
    body = res["out"] or {}
    assert body.get("code") == "E_VALIDATION", body
    assert "classification" in (body.get("detail") or ""), body


def test_subject_allowlist_v1_refuses_decision_subject(clean_substrate):
    """Non-assumption subject refused at handler before T-42 SQL trigger fires."""
    dv = _seed_decision()
    res = _submit_cycle({
        "subject": dv,
        "snapshot": "Cycle pointing at decision_v2 subject to test v1 allowlist refusal path.",
        "classification": "non-substantial",
    }, expect_ok=False)
    assert res["rc"] != 0, res
    body = res["out"] or {}
    assert body.get("code") == "E_VALIDATION", body
    detail = body.get("detail") or ""
    assert "allowlist" in detail or "assumption" in detail, body


def test_t42_sql_trigger_refuses_non_allowlist_subject_via_direct_insert():
    """T-42 SQL trigger backstop fires when handler-side check is bypassed."""
    conn = sqlite3.connect(str(PRIMARY_DB))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        # Find any non-assumption object_id in objects (e.g. session itself).
        row = conn.execute(
            "SELECT object_id, object_kind FROM objects "
            "WHERE object_kind != 'assumption' LIMIT 1"
        ).fetchone()
        assert row is not None, "no non-assumption object available for T-42 test"
        non_assumption_oid = row["object_id"]

        # Atomize a snapshot so we have a valid FK target.
        atom_row = conn.execute(
            "SELECT atom_id FROM text_atoms LIMIT 1"
        ).fetchone()
        assert atom_row is not None
        atom_id = atom_row["atom_id"]

        # Find the current open session for the FK.
        sess_row = conn.execute(
            "SELECT session_id FROM sessions ORDER BY session_id DESC LIMIT 1"
        ).fetchone()
        sess_id = sess_row["session_id"]

        try:
            conn.execute(
                "INSERT INTO cycle_ledger "
                "(session_id, subject_object_id, cycle_no, snapshot_atom_id, "
                " classification) VALUES (?,?,?,?,?)",
                (sess_id, non_assumption_oid, 0, atom_id, "non-substantial"),
            )
            assert False, "T-42 trigger should have refused non-allowlist subject"
        except sqlite3.IntegrityError as e:
            assert "T42" in str(e) or "allowlist" in str(e), str(e)
    finally:
        conn.close()


def test_auto_cycle_no_monotonic_per_subject(clean_substrate):
    ar = _seed_assumption()
    for n in range(3):
        res = _submit_cycle({
            "subject": ar,
            "snapshot": f"Cycle {n} observation: state snapshot for monotonic-cycle-no auto-increment test path.",
            "classification": "non-substantial",
        })
        assert res["out"]["result"]["cycle_no"] == n, res


def test_unique_subject_cycle_no_refusal_via_explicit_override(clean_substrate):
    ar = _seed_assumption()
    _submit_cycle({
        "subject": ar,
        "snapshot": "Cycle 0 first-write: establishes the (subject, cycle_no=0) unique row for collision test.",
        "classification": "non-substantial",
    })
    res = _submit_cycle({
        "subject": ar,
        "snapshot": "Cycle 0 collision-attempt: explicit cycle_no=0 override should refuse via UNIQUE.",
        "classification": "non-substantial",
        "cycle_no": 0,
    }, expect_ok=False)
    assert res["rc"] != 0, res


def test_optional_citing_supersession_resolves(clean_substrate):
    ar1 = _seed_assumption("First assumption seed for citing_supersession test path.")
    ar2 = _seed_assumption("Second assumption seed for citing_supersession test path.")
    sl = _seed_supersession(ar2, ar1)
    res = _submit_cycle({
        "subject": ar1,
        "snapshot": "Cycle 0 substantial: assumption superseded by AR2; SL alias cited for traceability.",
        "classification": "substantial",
        "classification_reason": "AR1 was superseded by AR2 via SL row; closure-by-supersession event recorded.",
        "citing_supersession": sl,
    })
    assert res["rc"] == 0, res


def test_unresolvable_citing_supersession_refused(clean_substrate):
    ar = _seed_assumption()
    res = _submit_cycle({
        "subject": ar,
        "snapshot": "Cycle with citing_supersession pointing at unresolvable alias for refusal path coverage.",
        "classification": "substantial",
        "classification_reason": "Substantial cycle citing nonexistent SL alias to force E_REFUSAL_T01.",
        "citing_supersession": "SL-S999-99",
    }, expect_ok=False)
    assert res["rc"] != 0, res


def test_snapshot_atom_length_refused(clean_substrate):
    ar = _seed_assumption()
    res = _submit_cycle({
        "subject": ar,
        "snapshot": "x",  # too short
        "classification": "non-substantial",
    }, expect_ok=False)
    assert res["rc"] != 0, res
    body = res["out"] or {}
    assert body.get("code") == "E_ATOM_LENGTH", body


def test_object_registration_lands_in_objects_with_kind_cycle(clean_substrate):
    ar = _seed_assumption()
    res = _submit_cycle({
        "subject": ar,
        "snapshot": "Cycle for object-registration test path; alias should register with object_kind=cycle.",
        "classification": "non-substantial",
    })
    alias = res["out"]["result"]["alias"]
    conn = sqlite3.connect(str(PRIMARY_DB))
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute(
            "SELECT object_kind FROM objects WHERE alias=?", (alias,)
        ).fetchone()
        assert row is not None, "cycle alias not in objects"
        assert row["object_kind"] == "cycle"
    finally:
        conn.close()


def test_unresolvable_subject_refused(clean_substrate):
    res = _submit_cycle({
        "subject": "AR-S999-99",
        "snapshot": "Cycle with unresolvable subject AR alias to force E_REFUSAL_T01 path.",
        "classification": "non-substantial",
    }, expect_ok=False)
    assert res["rc"] != 0, res


def test_explicit_cycle_no_override_admits(clean_substrate):
    ar = _seed_assumption()
    res = _submit_cycle({
        "subject": ar,
        "snapshot": "Cycle with explicit cycle_no=5 override; first row, no collision; admits non-strict.",
        "classification": "non-substantial",
        "cycle_no": 5,
    })
    assert res["rc"] == 0, res
    assert res["out"]["result"]["cycle_no"] == 5


def test_non_substantial_cannot_cite_supersession_handler(clean_substrate):
    """D-9 C-1 synthesis: non-substantial NEVER cites SL (auto-SR suppression).

    Reviewer F-03 fix: handler-side actionable refusal mirroring SQL CHECK
    in migration 053. Tests the handler-layer guard before the SQL CHECK
    backstop fires.
    """
    ar1 = _seed_assumption("First assumption seed for F-03 fix non-substantial-cant-cite-SL test.")
    ar2 = _seed_assumption("Second assumption seed for F-03 fix non-substantial-cant-cite-SL test.")
    sl = _seed_supersession(ar2, ar1)
    res = _submit_cycle({
        "subject": ar1,
        "snapshot": "Cycle 0 non-substantial that incorrectly tries to cite SL; should be refused per D-9 C-1.",
        "classification": "non-substantial",
        "citing_supersession": sl,
    }, expect_ok=False)
    assert res["rc"] != 0, res
    body = res["out"] or {}
    assert body.get("code") == "E_VALIDATION", body
    detail = body.get("detail") or ""
    assert "non-substantial" in detail and ("citing_supersession" in detail or "SL" in detail), body


def test_substantial_with_empty_string_reason_refused_handler(clean_substrate):
    """Reviewer F-02 fix: empty-string classification_reason refused at handler
    layer with E_VALIDATION (not E_ATOM_LENGTH from atom layer)."""
    ar = _seed_assumption()
    res = _submit_cycle({
        "subject": ar,
        "snapshot": "Cycle 0 substantial with empty-string reason should refuse at handler before atom layer.",
        "classification": "substantial",
        "classification_reason": "",
    }, expect_ok=False)
    assert res["rc"] != 0, res
    body = res["out"] or {}
    assert body.get("code") == "E_VALIDATION", body


def test_per_session_seq_increments_across_subjects(clean_substrate):
    ar1 = _seed_assumption("First seed for per-session seq test.")
    ar2 = _seed_assumption("Second seed for per-session seq test.")
    r1 = _submit_cycle({
        "subject": ar1,
        "snapshot": "Cycle for AR1 establishing seq=1 in CYC-S<wno>-1 alias bucket.",
        "classification": "non-substantial",
    })["out"]["result"]
    r2 = _submit_cycle({
        "subject": ar2,
        "snapshot": "Cycle for AR2 establishing seq=2 in CYC-S<wno>-2 alias bucket; per-session seq.",
        "classification": "non-substantial",
    })["out"]["result"]
    seq1 = int(r1["alias"].split("-")[-1])
    seq2 = int(r2["alias"].split("-")[-1])
    assert seq2 == seq1 + 1, (r1, r2)
