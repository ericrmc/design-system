"""review-finding, review-pass, finding-disposition handlers (T-30 surface)."""

from __future__ import annotations

import sqlite3

from ..aliases import _resolve_alias_to_object_id, _resolve_issue_alias
from ..errors import SelvedgeError
from ._helpers import (
    _atom_session_id,
    _check_role_capability,
    _insert_atom,
    _link_object,
    _session_workspace_no,
)


def _submit_review_finding(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "review_findings", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    wno = _session_workspace_no(conn, sess_id)
    finding_aid = _insert_atom(conn, role, sess_id, "finding", p["finding"])
    target_oid = _resolve_alias_to_object_id(conn, p["target"]) if p.get("target") else None
    disp_aid = None
    if p.get("disposition_text"):
        disp_aid = _insert_atom(conn, role, sess_id, "finding", p["disposition_text"])
    cur = conn.execute(
        "INSERT INTO review_findings (session_id, iteration, severity, finding_atom_id, target_object_id, disposition, disposition_atom_id) "
        "VALUES (?,?,?,?,?,?,?)",
        (sess_id, p["iteration"], p["severity"], finding_aid, target_oid, p.get("disposition", "open"), disp_aid),
    )
    rfid = cur.lastrowid
    alias = f"RF-S{wno:03d}-{p['iteration']}-{rfid}"
    oid = _link_object(conn, "review_findings", "review_finding_id", rfid, "review_finding", alias)
    return {"review_finding_id": rfid, "object_id": oid}


def _submit_review_pass(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    """Record a terminal review-pass row (engine-v31, S104 D-2/D-4).

    Required: iteration (1-4), outcome ('clean' | 'findings' | 'nonconverged'),
    head_sha (operator-asserted; substrate format-checks but cannot verify
    truth), summary (one-line atom).
    """
    _check_role_capability(conn, role, "review_passes", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    wno = _session_workspace_no(conn, sess_id)
    iteration = int(p["iteration"])
    if not (1 <= iteration <= 4):
        raise SelvedgeError(
            "E_VALIDATION",
            f"review-pass iteration must be 1-4 (the methodology halts the loop at iter 4); got {iteration}",
        )
    outcome = p["outcome"]
    if outcome not in ("clean", "findings", "nonconverged"):
        raise SelvedgeError(
            "E_VALIDATION",
            f"review-pass outcome must be one of clean, findings, nonconverged; got {outcome!r}",
        )
    head_sha = p.get("head_sha", "").strip()
    if not (7 <= len(head_sha) <= 64):
        raise SelvedgeError(
            "E_VALIDATION",
            "review-pass head_sha must be 7-64 chars (typically the abbreviated or full git HEAD sha at the moment the reviewer ran)",
        )
    if not all(c in "0123456789abcdefABCDEF" for c in head_sha):
        raise SelvedgeError(
            "E_VALIDATION",
            f"review-pass head_sha must be hex characters; got {head_sha!r}",
        )
    if outcome == "nonconverged" and not p.get("halt_issue_alias"):
        raise SelvedgeError(
            "E_VALIDATION",
            "review-pass outcome=nonconverged requires halt_issue_alias (the OI-... issue tracking the unresolved findings per methodology halt-state)",
        )
    summary_aid = _insert_atom(conn, role, sess_id, "finding", p["summary"])
    halt_issue_id = None
    if p.get("halt_issue_alias"):
        halt_issue_id = _resolve_issue_alias(conn, p["halt_issue_alias"])
    cur = conn.execute(
        "INSERT INTO review_passes (session_id, iteration, outcome, head_sha, summary_atom_id, halt_issue_id) "
        "VALUES (?,?,?,?,?,?)",
        (sess_id, iteration, outcome, head_sha, summary_aid, halt_issue_id),
    )
    rpid = cur.lastrowid
    return {
        "review_pass_id": rpid,
        "session_workspace_no": wno,
        "iteration": iteration,
        "outcome": outcome,
    }


def _submit_finding_disposition(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "review_findings", "update")
    rf = conn.execute(
        "SELECT session_id FROM review_findings WHERE review_finding_id=?",
        (p["review_finding_id"],),
    ).fetchone()
    if rf is None:
        raise SelvedgeError("E_NOT_FOUND", f"review_finding_id={p['review_finding_id']}")
    disp_aid = _insert_atom(conn, role, rf["session_id"], "finding", p["disposition_text"])
    conn.execute(
        "UPDATE review_findings SET disposition=?, disposition_atom_id=? WHERE review_finding_id=?",
        (p["disposition"], disp_aid, p["review_finding_id"]),
    )
    return {"review_finding_id": p["review_finding_id"], "disposition": p["disposition"]}
