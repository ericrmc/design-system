"""close-record handler."""

from __future__ import annotations

import sqlite3

from ._helpers import (
    _atom_session_id,
    _check_role_capability,
    _insert_atom,
    _link_object,
    _session_workspace_no,
    _validate_atom,
)


def _submit_close_record(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "close_records", "insert")
    # Pre-validate every atom before the first INSERT so a malformed item
    # cannot leave half the close-record's atoms in text_atoms when the
    # transaction rolls back. DV-S134-1 (engine-v41).
    _validate_atom("close_summary", p["summary"], "summary")
    for idx, item in enumerate(p.get("items", [])):
        _validate_atom("close_state_item", item["text"], f"items[{idx}].text")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    wno = _session_workspace_no(conn, sess_id)
    summary_aid = _insert_atom(conn, role, sess_id, "close_summary", p["summary"])
    cur = conn.execute(
        "INSERT INTO close_records (session_id, summary_atom_id) VALUES (?,?)",
        (sess_id, summary_aid),
    )
    crid = cur.lastrowid
    alias = f"C-S{wno:03d}"
    oid = _link_object(conn, "close_records", "close_record_id", crid, "close_record", alias)
    _check_role_capability(conn, role, "close_state_items", "insert")
    items_out = []
    for seq, item in enumerate(p.get("items", []), start=1):
        item_aid = _insert_atom(conn, role, sess_id, "close_state_item", item["text"])
        conn.execute(
            "INSERT INTO close_state_items (close_record_id, seq, facet, item_atom_id) VALUES (?,?,?,?)",
            (crid, seq, item["facet"], item_aid),
        )
        items_out.append({"seq": seq, "facet": item["facet"]})
    return {"close_record_id": crid, "object_id": oid, "alias": alias, "items": items_out}
