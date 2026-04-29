"""issue, issue-disposition, issue-link, issue-note, issue-work-item handlers."""

from __future__ import annotations

import sqlite3

from ..aliases import _resolve_issue_alias
from ..errors import SelvedgeError
from ._helpers import (
    _atom_session_id,
    _check_role_capability,
    _insert_atom,
    _next_no,
)


def _submit_issue(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "issues", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    surfaced_id = (
        _atom_session_id(conn, p.get("surfaced_session_no"), require_open=False)
        if p.get("surfaced_session_no") is not None
        else sess_id
    )
    if p.get("status") not in (None, "open"):
        raise SelvedgeError(
            "E_VALIDATION",
            "issue must be created with status='open'; transitions to other statuses go through submit issue-disposition",
        )
    title_aid = _insert_atom(conn, role, sess_id, "title", p["title"])
    summary_aid = None
    if p.get("summary"):
        summary_aid = _insert_atom(conn, role, sess_id, "claim", p["summary"])
    body_aid = None
    if p.get("body"):
        body_aid = _insert_atom(conn, role, sess_id, "legacy_import", p["body"])
    cur = conn.execute(
        "INSERT INTO issues (alias, surfaced_session_id, title_atom_id, summary_atom_id, body_atom_id, priority, status) "
        "VALUES (?,?,?,?,?,?, 'open')",
        (
            p["alias"],
            surfaced_id,
            title_aid,
            summary_aid,
            body_aid,
            p["priority"],
        ),
    )
    iid = cur.lastrowid
    return {"issue_id": iid, "alias": p["alias"]}


def _submit_issue_disposition(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "issue_dispositions", "insert")
    _check_role_capability(conn, role, "issues", "update")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    if "issue_id" in p:
        iid = int(p["issue_id"])
    else:
        iid = _resolve_issue_alias(conn, p["alias"])
    cur_row = conn.execute(
        "SELECT status FROM issues WHERE issue_id=?", (iid,)
    ).fetchone()
    if cur_row is None:
        raise SelvedgeError("E_NOT_FOUND", f"issue_id={iid}")
    from_status = cur_row["status"]
    to_status = p["to_status"]
    if from_status == to_status:
        raise SelvedgeError("E_VALIDATION", f"to_status equals from_status ({from_status}); no-op refused")
    reason_aid = _insert_atom(conn, role, sess_id, "rejection_reason", p["reason"])
    next_seq = _next_no(conn, "issue_dispositions", "seq", "issue_id", iid)
    cur = conn.execute(
        "INSERT INTO issue_dispositions (issue_id, seq, from_status, to_status, reason_atom_id, session_id) "
        "VALUES (?,?,?,?,?,?)",
        (iid, next_seq, from_status, to_status, reason_aid, sess_id),
    )
    did = cur.lastrowid
    if to_status in ("resolved", "superseded"):
        conn.execute(
            "UPDATE issues SET status=?, resolved_session_id=?, resolved_at=strftime('%Y-%m-%dT%H:%M:%fZ','now') "
            "WHERE issue_id=?",
            (to_status, sess_id, iid),
        )
    else:
        conn.execute(
            "UPDATE issues SET status=?, resolved_session_id=NULL, resolved_at=NULL WHERE issue_id=?",
            (to_status, iid),
        )
    return {"disposition_id": did, "issue_id": iid, "from_status": from_status, "to_status": to_status}


def _submit_issue_link(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "issue_links", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    src = int(p["source_issue_id"]) if "source_issue_id" in p else _resolve_issue_alias(conn, p["source_alias"])
    tgt = int(p["target_issue_id"]) if "target_issue_id" in p else _resolve_issue_alias(conn, p["target_alias"])
    reason_aid = None
    if p.get("reason"):
        reason_aid = _insert_atom(conn, role, sess_id, "rejection_reason", p["reason"])
    cur = conn.execute(
        "INSERT INTO issue_links (source_issue_id, target_issue_id, relation, reason_atom_id, session_id) "
        "VALUES (?,?,?,?,?)",
        (src, tgt, p["relation"], reason_aid, sess_id),
    )
    return {"link_id": cur.lastrowid, "source_issue_id": src, "target_issue_id": tgt, "relation": p["relation"]}


def _submit_issue_note(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "issue_notes", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    iid = int(p["issue_id"]) if "issue_id" in p else _resolve_issue_alias(conn, p["alias"])
    note_aid = _insert_atom(conn, role, sess_id, "claim", p["note"])
    next_seq = _next_no(conn, "issue_notes", "seq", "issue_id", iid)
    cur = conn.execute(
        "INSERT INTO issue_notes (issue_id, seq, note_atom_id, session_id) VALUES (?,?,?,?)",
        (iid, next_seq, note_aid, sess_id),
    )
    return {"note_id": cur.lastrowid, "issue_id": iid, "seq": next_seq}


def _submit_issue_work_item(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "issue_work_items", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    iid = int(p["issue_id"]) if "issue_id" in p else _resolve_issue_alias(conn, p["alias"])
    if "issue_id" in p and conn.execute(
        "SELECT 1 FROM issues WHERE issue_id=?", (iid,)
    ).fetchone() is None:
        raise SelvedgeError("E_NOT_FOUND", f"issue_id={iid}")
    wid = int(p["work_item_id"])
    if conn.execute("SELECT 1 FROM work_items WHERE work_item_id=?", (wid,)).fetchone() is None:
        raise SelvedgeError("E_NOT_FOUND", f"work_item_id={wid}")
    relation = p.get("relation", "resolves")
    cur = conn.execute(
        "INSERT INTO issue_work_items (issue_id, work_item_id, relation, created_session_id) "
        "VALUES (?,?,?,?)",
        (iid, wid, relation, sess_id),
    )
    return {
        "issue_work_item_id": cur.lastrowid,
        "issue_id": iid,
        "work_item_id": wid,
        "relation": relation,
    }
