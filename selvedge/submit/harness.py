"""reference_harness submit handlers (engine-v35+, S125 closing OI-S124-2).

The harness is a workspace-experimental substrate kind commissioned by
DV-S124-2 for the disaster-response arc stage-2-onward pilot. It is NOT a
kernel third validation sense; methodology v6 keeps the kernel at two
senses (workspace, domain). Kernel-promotion is deferred to arc-close
re-evaluation per OI-S124-1.

Lifecycle:
    open -> sealed -> {expired, reopened}

Handlers:
    harness-open      Create a new harness (status=open).
    harness-target    Add a target_artifact entry.
    harness-claim     Add a claim_set entry.
    harness-stress    Add a stress_protocol entry.
    harness-result    Record a claim-level result.
    harness-dissent   Preserve a minority surrogate objection.
    harness-trigger   Register a falsification_trigger.
    harness-seal      Transition open -> sealed.

P-2 epistemic guardrail is structural: reference_harness_results.result
admits exactly {survived, strained, broken, untestable, deferred}. The
absence of `domain_validated` from the CHECK enum is the substrate-level
guarantee that a passing harness cannot upgrade an artefact's epistemic
status.
"""

from __future__ import annotations

import sqlite3

from ..errors import SelvedgeError
from ._helpers import (
    _atom_session_id,
    _check_role_capability,
    _insert_atom,
    _session_workspace_no,
)


def _resolve_harness_id(conn: sqlite3.Connection, p: dict) -> int:
    if "harness_id" in p and p["harness_id"] is not None:
        hid = int(p["harness_id"])
        row = conn.execute(
            "SELECT 1 FROM reference_harnesses WHERE harness_id=?", (hid,)
        ).fetchone()
        if row is None:
            raise SelvedgeError("E_NOT_FOUND", f"reference_harness harness_id={hid} not found")
        return hid
    if "alias" in p and p["alias"]:
        row = conn.execute(
            "SELECT harness_id FROM reference_harnesses WHERE alias=?", (p["alias"],)
        ).fetchone()
        if row is None:
            raise SelvedgeError("E_NOT_FOUND", f"reference_harness alias [{p['alias']}] not found")
        return row["harness_id"]
    raise SelvedgeError("E_VALIDATION", "harness-* requires harness_id or alias")


def _next_harness_seq(conn: sqlite3.Connection, wno: int) -> int:
    return conn.execute(
        "SELECT COUNT(*)+1 AS n "
        "FROM reference_harnesses rh "
        "JOIN sessions s ON s.session_id=rh.session_id "
        "WHERE COALESCE(s.workspace_session_no, s.session_no)=?",
        (wno,),
    ).fetchone()["n"]


def _next_child_ord(
    conn: sqlite3.Connection, table: str, harness_id: int
) -> int:
    return conn.execute(
        f"SELECT COALESCE(MAX(ord),0)+1 AS n FROM {table} WHERE harness_id=?",
        (harness_id,),
    ).fetchone()["n"]


def _submit_harness_open(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "reference_harnesses", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    wno = _session_workspace_no(conn, sess_id)
    arc_slug = p["arc_slug"]
    stage_n = int(p["stage_n"])
    expiry_sessions = int(p["expiry_sessions"])
    decl_aid = _insert_atom(conn, role, sess_id, "claim", p["absence_declaration"])
    seq = _next_harness_seq(conn, wno)
    alias = p.get("alias") or f"RH-S{wno:03d}-{seq}"
    cur = conn.execute(
        "INSERT INTO reference_harnesses "
        "(alias, session_id, arc_slug, stage_n, absence_declaration_atom_id, expiry_sessions, status) "
        "VALUES (?,?,?,?,?,?, 'open')",
        (alias, sess_id, arc_slug, stage_n, decl_aid, expiry_sessions),
    )
    hid = cur.lastrowid
    return {
        "harness_id": hid,
        "alias": alias,
        "arc_slug": arc_slug,
        "stage_n": stage_n,
        "status": "open",
    }


def _submit_harness_target(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "reference_harness_targets", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    hid = _resolve_harness_id(conn, p)
    desc_aid = _insert_atom(conn, role, sess_id, "claim", p["descriptor"])
    ord_ = _next_child_ord(conn, "reference_harness_targets", hid)
    cur = conn.execute(
        "INSERT INTO reference_harness_targets "
        "(harness_id, ord, descriptor_atom_id, artifact_path, artifact_sha256) "
        "VALUES (?,?,?,?,?)",
        (hid, ord_, desc_aid, p.get("artifact_path"), p.get("artifact_sha256")),
    )
    return {"target_id": cur.lastrowid, "harness_id": hid, "ord": ord_}


def _submit_harness_claim(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "reference_harness_claims", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    hid = _resolve_harness_id(conn, p)
    claim_aid = _insert_atom(conn, role, sess_id, "claim", p["claim"])
    wc_aid = (
        _insert_atom(conn, role, sess_id, "claim", p["world_constraint"])
        if p.get("world_constraint")
        else None
    )
    sf_aid = (
        _insert_atom(conn, role, sess_id, "claim", p["surrogate_frame"])
        if p.get("surrogate_frame")
        else None
    )
    load_bearing = 1 if p.get("load_bearing") else 0
    ord_ = _next_child_ord(conn, "reference_harness_claims", hid)
    cur = conn.execute(
        "INSERT INTO reference_harness_claims "
        "(harness_id, ord, claim_atom_id, world_constraint_atom_id, surrogate_frame_atom_id, load_bearing) "
        "VALUES (?,?,?,?,?,?)",
        (hid, ord_, claim_aid, wc_aid, sf_aid, load_bearing),
    )
    return {
        "claim_id": cur.lastrowid,
        "harness_id": hid,
        "ord": ord_,
        "load_bearing": bool(load_bearing),
    }


def _submit_harness_stress(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "reference_harness_stresses", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    hid = _resolve_harness_id(conn, p)
    desc_aid = _insert_atom(conn, role, sess_id, "claim", p["description"])
    ord_ = _next_child_ord(conn, "reference_harness_stresses", hid)
    cur = conn.execute(
        "INSERT INTO reference_harness_stresses "
        "(harness_id, ord, protocol_kind, description_atom_id) "
        "VALUES (?,?,?,?)",
        (hid, ord_, p["protocol_kind"], desc_aid),
    )
    return {
        "stress_id": cur.lastrowid,
        "harness_id": hid,
        "ord": ord_,
        "protocol_kind": p["protocol_kind"],
    }


def _submit_harness_result(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "reference_harness_results", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    claim_id = int(p["claim_id"])
    row = conn.execute(
        "SELECT harness_id FROM reference_harness_claims WHERE claim_id=?",
        (claim_id,),
    ).fetchone()
    if row is None:
        raise SelvedgeError("E_NOT_FOUND", f"reference_harness_claims claim_id={claim_id}")
    evidence_aid = _insert_atom(conn, role, sess_id, "finding", p["evidence"])
    cur = conn.execute(
        "INSERT INTO reference_harness_results "
        "(claim_id, result, evidence_atom_id) "
        "VALUES (?,?,?)",
        (claim_id, p["result"], evidence_aid),
    )
    return {
        "result_id": cur.lastrowid,
        "claim_id": claim_id,
        "harness_id": row["harness_id"],
        "result": p["result"],
    }


def _submit_harness_dissent(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "reference_harness_dissent", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    hid = _resolve_harness_id(conn, p)
    source_claim_id = (
        int(p["source_claim_id"]) if p.get("source_claim_id") is not None else None
    )
    if source_claim_id is not None:
        row = conn.execute(
            "SELECT harness_id FROM reference_harness_claims WHERE claim_id=?",
            (source_claim_id,),
        ).fetchone()
        if row is None:
            raise SelvedgeError(
                "E_NOT_FOUND", f"reference_harness_claims claim_id={source_claim_id}"
            )
        if row["harness_id"] != hid:
            raise SelvedgeError(
                "E_VALIDATION",
                f"source_claim_id={source_claim_id} belongs to harness_id={row['harness_id']}, not {hid}",
            )
    dissent_aid = _insert_atom(conn, role, sess_id, "claim", p["dissent"])
    conflict_kind_aid = (
        _insert_atom(conn, role, sess_id, "claim", p["conflict_kind"])
        if p.get("conflict_kind")
        else None
    )
    ord_ = _next_child_ord(conn, "reference_harness_dissent", hid)
    cur = conn.execute(
        "INSERT INTO reference_harness_dissent "
        "(harness_id, ord, dissent_atom_id, source_claim_id, conflict_kind_atom_id) "
        "VALUES (?,?,?,?,?)",
        (hid, ord_, dissent_aid, source_claim_id, conflict_kind_aid),
    )
    return {"dissent_id": cur.lastrowid, "harness_id": hid, "ord": ord_}


def _submit_harness_trigger(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "reference_harness_triggers", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    hid = _resolve_harness_id(conn, p)
    trigger_aid = _insert_atom(conn, role, sess_id, "claim", p["trigger"])
    ord_ = _next_child_ord(conn, "reference_harness_triggers", hid)
    cur = conn.execute(
        "INSERT INTO reference_harness_triggers "
        "(harness_id, ord, trigger_atom_id) "
        "VALUES (?,?,?)",
        (hid, ord_, trigger_aid),
    )
    return {"trigger_id": cur.lastrowid, "harness_id": hid, "ord": ord_}


def _submit_harness_assumption(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "reference_harness_assumptions", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    hid = _resolve_harness_id(conn, p)
    assumption_aid = _insert_atom(conn, role, sess_id, "claim", p["assumption"])
    if "origin_session_no" in p and p["origin_session_no"] is not None:
        origin_id = _atom_session_id(
            conn, p["origin_session_no"], require_open=False
        )
    else:
        origin_id = sess_id
    status = p.get("status", "active")
    if status not in ("active", "invalidated", "deferred"):
        raise SelvedgeError(
            "E_VALIDATION",
            f"harness-assumption status must be active|invalidated|deferred, got {status!r}",
        )
    ord_ = _next_child_ord(conn, "reference_harness_assumptions", hid)
    cur = conn.execute(
        "INSERT INTO reference_harness_assumptions "
        "(harness_id, ord, assumption_atom_id, origin_session_id, status) "
        "VALUES (?,?,?,?,?)",
        (hid, ord_, assumption_aid, origin_id, status),
    )
    return {
        "assumption_id": cur.lastrowid,
        "harness_id": hid,
        "ord": ord_,
        "origin_session_id": origin_id,
        "status": status,
    }


def _submit_harness_trigger_fire(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    """Fire a falsification trigger on a sealed harness.

    Cascades via T-37 to set parent harness.status='reopened'. Refuses if
    the trigger has already fired (T-32 admits only NULL→NOT NULL).
    """
    _check_role_capability(conn, role, "reference_harness_triggers", "update")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    trigger_id = int(p["trigger_id"])
    row = conn.execute(
        "SELECT harness_id, fired_at FROM reference_harness_triggers WHERE trigger_id=?",
        (trigger_id,),
    ).fetchone()
    if row is None:
        raise SelvedgeError(
            "E_NOT_FOUND", f"reference_harness_triggers trigger_id={trigger_id}"
        )
    if row["fired_at"] is not None:
        raise SelvedgeError(
            "E_VALIDATION",
            f"trigger_id={trigger_id} has already fired; firing is one-shot per trigger row",
        )
    upd = conn.execute(
        "UPDATE reference_harness_triggers "
        "SET fired_at=strftime('%Y-%m-%dT%H:%M:%fZ','now'), "
        "    reopened_session_id=? "
        "WHERE trigger_id=?",
        (sess_id, trigger_id),
    )
    if upd.rowcount != 1:
        raise SelvedgeError("E_NOT_FOUND", f"trigger_id={trigger_id}")
    return {
        "trigger_id": trigger_id,
        "harness_id": row["harness_id"],
        "reopened_session_id": sess_id,
        "harness_status_now": "reopened",
    }


def _submit_harness_seal(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "reference_harnesses", "update")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    hid = _resolve_harness_id(conn, p)
    row = conn.execute(
        "SELECT status FROM reference_harnesses WHERE harness_id=?", (hid,)
    ).fetchone()
    if row["status"] != "open":
        raise SelvedgeError(
            "E_VALIDATION",
            f"harness_id={hid} status is {row['status']}; only open harnesses can be sealed",
        )
    closure_kind_aid = (
        _insert_atom(conn, role, sess_id, "claim", p["closure_kind"])
        if p.get("closure_kind")
        else None
    )
    upd = conn.execute(
        "UPDATE reference_harnesses "
        "SET status='sealed', "
        "    sealed_at=strftime('%Y-%m-%dT%H:%M:%fZ','now'), "
        "    sealed_session_id=?, "
        "    closure_kind_atom_id=COALESCE(?, closure_kind_atom_id) "
        "WHERE harness_id=?",
        (sess_id, closure_kind_aid, hid),
    )
    if upd.rowcount != 1:
        raise SelvedgeError("E_NOT_FOUND", f"harness_id={hid}")
    return {"harness_id": hid, "status": "sealed", "sealed_session_id": sess_id}
