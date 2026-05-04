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


_HARVEST_PREFIX = "historical-harvest:"
_ANCHOR_ROLES = ("about", "descended_from", "calibrates", "supersedes_context")


def _submit_engine_feedback(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    """Insert one engine_feedback row + objects row + refs + anchors (DV-S194-1).

    Optional `anchors`: list of {"alias": <objects.alias>, "role": <enum>} dicts.
    Each anchor resolves the alias to objects.object_id and inserts one
    engine_feedback_anchors row inside the same write_tx.

    T-37 (handler-side, DV-S194-1): refuse with E_REFUSAL_T37 when body_md
    starts with `historical-harvest:` AND no anchors[] entry was provided.
    Trigger-side enforcement is structurally infeasible because anchors are
    inserted AFTER the engine_feedback row inside the same write_tx; SQLite
    has no DEFER trigger semantics. Same handler-dispatch shape as T-32
    chain-walks per DV-S194-1 schema-correctness threshold (P-3 M-3).
    """
    _check_role_capability(conn, role, "engine_feedback", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    wno = _session_workspace_no(conn, sess_id)
    flag = p["flag"]
    body_md = p["body_md"]
    disposition = p.get("disposition")
    anchors = p.get("anchors") or []

    is_harvest = body_md.lstrip().startswith(_HARVEST_PREFIX)
    if is_harvest and not anchors:
        raise SelvedgeError(
            "E_REFUSAL_T37",
            "engine-feedback body_md begins with 'historical-harvest:' but anchors[] is empty; "
            "harvest-prefixed rows MUST declare >=1 anchor per DV-S194-1 (typed-FK chain-walk reachability). "
            "Provide anchors=[{\"alias\": \"<DV-...|EF-...|SPEC-...|P-N-...|active-OI-or-FR-alias>\", "
            "\"role\": \"about|descended_from|calibrates|supersedes_context\"}, ...]",
        )

    resolved_anchors = []
    for a in anchors:
        alias = a.get("alias")
        anchor_role = a.get("role")
        if not alias or not anchor_role:
            raise SelvedgeError(
                "E_VALIDATION",
                f"anchors[] entry must have 'alias' and 'role' keys; got {a!r}",
            )
        if anchor_role not in _ANCHOR_ROLES:
            raise SelvedgeError(
                "E_VALIDATION",
                f"anchor role={anchor_role!r} not in {_ANCHOR_ROLES}",
            )
        oid = _resolve_alias(conn, alias)
        if oid is None:
            raise SelvedgeError(
                "E_REFUSAL_T01",
                f"unresolved anchor alias [{alias}]; anchors require objects.alias resolution per DV-S194-1 FK-only "
                f"(no synthetic alias creation per DV-S189-1). Drop the anchor or use a resolvable alias.",
            )
        resolved_anchors.append((oid, anchor_role))

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
    oid_self = _link_object(conn, "engine_feedback", "feedback_id", fid, "engine_feedback", alias)
    _check_role_capability(conn, role, "refs", "insert")
    n_refs = _record_refs(conn, source_object_id=oid_self, body_md=body_md)

    anchor_rows = []
    if resolved_anchors:
        _check_role_capability(conn, role, "engine_feedback_anchors", "insert")
        for anchor_oid, anchor_role in resolved_anchors:
            conn.execute(
                "INSERT INTO engine_feedback_anchors (feedback_id, anchor_object_id, anchor_role) "
                "VALUES (?,?,?)",
                (fid, anchor_oid, anchor_role),
            )
            anchor_rows.append({"anchor_object_id": anchor_oid, "anchor_role": anchor_role})

    return {
        "feedback_id": fid,
        "object_id": oid_self,
        "alias": alias,
        "flag": flag,
        "refs": n_refs,
        "anchors": anchor_rows,
    }


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


def _submit_engine_feedback_anchor(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    """Add anchor rows to an existing engine_feedback row (DV-S194-1 backfill path).

    The primary insert path admits anchors at submit time. This kind adds
    anchors to a previously-submitted row — primarily for the S194-and-S193
    backfill of historical-harvest EFs that landed before migration 045
    shipped. Inserting anchors here does NOT mutate the engine_feedback row;
    only engine_feedback_anchors rows are written.

    Each anchor entry: {alias: <objects.alias>, role: <about|descended_from|
    calibrates|supersedes_context>}. Unresolvable alias raises E_REFUSAL_T01
    per DV-S189-1 no-synthetic-rows. UNIQUE(feedback_id, anchor_object_id,
    anchor_role) guards against duplicate inserts.
    """
    _check_role_capability(conn, role, "engine_feedback_anchors", "insert")
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
        raise SelvedgeError("E_VALIDATION", "engine-feedback-anchor requires feedback_id or alias")

    anchors = p.get("anchors") or []
    if not anchors:
        raise SelvedgeError("E_VALIDATION", "engine-feedback-anchor requires anchors[] with >=1 entry")

    inserted = []
    for a in anchors:
        alias = a.get("alias")
        anchor_role = a.get("role")
        if not alias or not anchor_role:
            raise SelvedgeError("E_VALIDATION", f"anchors[] entry must have 'alias' and 'role' keys; got {a!r}")
        if anchor_role not in _ANCHOR_ROLES:
            raise SelvedgeError("E_VALIDATION", f"anchor role={anchor_role!r} not in {_ANCHOR_ROLES}")
        anchor_oid = _resolve_alias(conn, alias)
        if anchor_oid is None:
            raise SelvedgeError(
                "E_REFUSAL_T01",
                f"unresolved anchor alias [{alias}] per DV-S194-1 FK-only + DV-S189-1 no-synthetic-rows",
            )
        conn.execute(
            "INSERT INTO engine_feedback_anchors (feedback_id, anchor_object_id, anchor_role) VALUES (?,?,?)",
            (fid, anchor_oid, anchor_role),
        )
        inserted.append({"anchor_object_id": anchor_oid, "anchor_role": anchor_role, "alias": alias})

    return {"feedback_id": fid, "anchors_added": inserted}


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
