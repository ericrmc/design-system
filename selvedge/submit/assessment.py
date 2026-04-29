"""assessment + legacy-import handlers."""

from __future__ import annotations

import sqlite3

from ._helpers import (
    _atom_session_id,
    _check_role_capability,
    _insert_atom,
    _link_object,
    _session_workspace_no,
)


def _submit_assessment(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "assessments", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    wno = _session_workspace_no(conn, sess_id)
    state_aid = _insert_atom(conn, role, sess_id, "assessment_item", p["state"])
    cur = conn.execute(
        "INSERT INTO assessments (session_id, state_atom_id) VALUES (?,?)",
        (sess_id, state_aid),
    )
    aid = cur.lastrowid
    alias = f"A-S{wno:03d}"
    oid = _link_object(conn, "assessments", "assessment_id", aid, "assessment", alias)
    _check_role_capability(conn, role, "assessment_agenda_items", "insert")
    items_out = []
    for ord_, item_text in enumerate(p.get("agenda", []), start=1):
        item_aid = _insert_atom(conn, role, sess_id, "assessment_item", item_text)
        conn.execute(
            "INSERT INTO assessment_agenda_items (assessment_id, ord, item_atom_id) VALUES (?,?,?)",
            (aid, ord_, item_aid),
        )
        items_out.append({"ord": ord_, "atom_id": item_aid})
    return {"assessment_id": aid, "object_id": oid, "alias": alias, "agenda": items_out}


def _submit_legacy_import(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "legacy_imports", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    aid = _insert_atom(conn, role, sess_id, "legacy_import", p["text"])
    cur = conn.execute(
        "INSERT INTO legacy_imports (old_table, old_pk, atom_id, decomposition_status, decomposed_in_session_id) "
        "VALUES (?,?,?,?,?)",
        (p["old_table"], p["old_pk"], aid, p.get("decomposition_status", "unratified"), sess_id),
    )
    return {"legacy_import_id": cur.lastrowid, "atom_id": aid}
