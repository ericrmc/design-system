"""Legacy `decision` handler (pre-engine-v20). Read/replay-only in modern sessions;
the active path is decision-record (decision_v2)."""

from __future__ import annotations

import sqlite3

from ..aliases import _alias_for_decision, _record_refs
from ..errors import SelvedgeError
from ._helpers import _check_role_capability, _link_object


def _submit_decision(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "decisions", "insert")
    sess = conn.execute(
        "SELECT session_id, session_no, status FROM sessions WHERE session_no = ?",
        (p["session_no"],),
    ).fetchone()
    if sess is None:
        raise SelvedgeError("E_NOT_FOUND", f"session_no={p['session_no']}")
    if sess["status"] == "closed":
        raise SelvedgeError("E_REFUSAL_T06", f"session {sess['session_no']} is closed")
    next_no = conn.execute(
        "SELECT COALESCE(MAX(decision_no),0)+1 AS n FROM decisions WHERE session_id=?",
        (sess["session_id"],),
    ).fetchone()["n"]
    cur = conn.execute(
        "INSERT INTO decisions (session_id, decision_no, kind, title, body_md) VALUES (?,?,?,?,?)",
        (sess["session_id"], next_no, p["kind"], p["title"], p["body_md"]),
    )
    did = cur.lastrowid
    alias = _alias_for_decision(sess["session_no"], next_no)
    oid = _link_object(conn, "decisions", "decision_id", did, "decision", alias)

    for a in p.get("alternatives", []) or []:
        _check_role_capability(conn, role, "decision_alternatives", "insert")
        conn.execute(
            "INSERT INTO decision_alternatives (decision_id, label, summary, rejection_reason_md) "
            "VALUES (?,?,?,?)",
            (did, a["label"], a["summary"], a["rejection_reason_md"]),
        )

    _check_role_capability(conn, role, "refs", "insert")
    n_refs = _record_refs(conn, source_object_id=oid, body_md=p["body_md"], extra_refs=p.get("refs", []) or [])

    return {"decision_id": did, "object_id": oid, "alias": alias, "decision_no": next_no, "refs": n_refs}
