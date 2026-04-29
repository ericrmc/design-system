"""engine-feedback, engine-feedback-disposition, forward-reference-disposition."""

from __future__ import annotations

import sqlite3

from ..aliases import _alias_for_engine_feedback, _record_refs, _resolve_alias
from ..errors import SelvedgeError
from ._helpers import (
    _atom_session_id,
    _check_role_capability,
    _insert_atom,
    _link_object,
    _session_workspace_no,
)


def _submit_engine_feedback(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    """Insert one engine_feedback row + objects row + refs (engine-v26+)."""
    _check_role_capability(conn, role, "engine_feedback", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    wno = _session_workspace_no(conn, sess_id)
    flag = p["flag"]
    body_md = p["body_md"]
    disposition = p.get("disposition")
    cur = conn.execute(
        "INSERT INTO engine_feedback (session_id, flag, body_md, disposition) VALUES (?,?,?,?)",
        (sess_id, flag, body_md, disposition),
    )
    fid = cur.lastrowid
    idx = conn.execute(
        "SELECT COUNT(*) AS n FROM engine_feedback ef "
        "JOIN sessions s ON s.session_id=ef.session_id "
        "WHERE COALESCE(s.workspace_session_no, s.session_no)=?",
        (wno,),
    ).fetchone()["n"]
    alias = _alias_for_engine_feedback(wno, idx)
    oid = _link_object(conn, "engine_feedback", "feedback_id", fid, "engine_feedback", alias)
    _check_role_capability(conn, role, "refs", "insert")
    n_refs = _record_refs(conn, source_object_id=oid, body_md=body_md)
    return {"feedback_id": fid, "object_id": oid, "alias": alias, "flag": flag, "refs": n_refs}


def _submit_engine_feedback_disposition(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    """Update engine_feedback.disposition (engine-v27+, EF-S096-2 remedy)."""
    _check_role_capability(conn, role, "engine_feedback", "update")
    _atom_session_id(conn, p.get("session_no"))
    if "feedback_id" in p:
        fid = int(p["feedback_id"])
    elif "alias" in p:
        oid = _resolve_alias(conn, p["alias"])
        if oid is None:
            raise SelvedgeError("E_REFUSAL_T01", f"unresolved alias [{p['alias']}]")
        row = conn.execute(
            "SELECT feedback_id FROM engine_feedback WHERE object_id=?", (oid,)
        ).fetchone()
        if row is None:
            raise SelvedgeError("E_NOT_FOUND", f"alias {p['alias']} is not engine_feedback")
        fid = row["feedback_id"]
    else:
        raise SelvedgeError("E_VALIDATION", "engine-feedback-disposition requires feedback_id or alias")
    upd = conn.execute(
        "UPDATE engine_feedback SET disposition=? WHERE feedback_id=?",
        (p["disposition"], fid),
    )
    if upd.rowcount != 1:
        raise SelvedgeError("E_NOT_FOUND", f"feedback_id={fid}")
    return {"feedback_id": fid, "disposition": p["disposition"]}


def _submit_forward_reference_disposition(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    """Mark a close_state_items row with facet='next_session_should' as resolved
    (engine-v27+, EF-S096-1 strong remedy)."""
    _check_role_capability(conn, role, "forward_reference_dispositions", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    target_wno = int(p["target_session"])
    seq = int(p["seq"])
    row = conn.execute(
        "SELECT csi.state_item_id "
        "FROM close_state_items csi "
        "JOIN close_records cr ON cr.close_record_id=csi.close_record_id "
        "JOIN sessions s ON s.session_id=cr.session_id "
        "WHERE COALESCE(s.workspace_session_no, s.session_no)=? "
        "  AND csi.seq=? AND csi.facet='next_session_should'",
        (target_wno, seq),
    ).fetchone()
    if row is None:
        raise SelvedgeError(
            "E_NOT_FOUND",
            f"forward-reference target_session={target_wno} seq={seq} "
            f"(must be a next_session_should close_state_item)",
        )
    note_aid = None
    if p.get("note"):
        note_aid = _insert_atom(conn, role, sess_id, "claim", p["note"])
    cur = conn.execute(
        "INSERT INTO forward_reference_dispositions (state_item_id, resolved_session_id, note_atom_id) "
        "VALUES (?,?,?)",
        (row["state_item_id"], sess_id, note_aid),
    )
    return {
        "disposition_id": cur.lastrowid,
        "state_item_id": row["state_item_id"],
        "ref": f"FR-S{target_wno:03d}-{seq}",
    }
