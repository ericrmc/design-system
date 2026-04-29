"""Deliberation, perspective, synthesis-point handlers (engine-v20+ Path A)."""

from __future__ import annotations

import json
import sqlite3

from ..aliases import _record_refs, _resolve_alias_to_object_id
from ..errors import SelvedgeError
from ._helpers import (
    _atom_session_id,
    _check_role_capability,
    _insert_atom,
    _link_object,
    _next_no,
    _session_open_or_die,
)


def _submit_deliberation_open(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "deliberations", "insert")
    sess = _session_open_or_die(conn, p["session_no"])
    cur = conn.execute(
        "INSERT INTO deliberations (session_id, topic, sealed_at, synthesis_md) VALUES (?,?,NULL,NULL)",
        (sess["session_id"], p["topic"]),
    )
    did = cur.lastrowid
    oid = _link_object(conn, "deliberations", "deliberation_id", did, "deliberation", None)
    return {"deliberation_id": did, "object_id": oid, "session_id": sess["session_id"]}


def _submit_perspective(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "perspectives", "insert")
    delib = conn.execute(
        "SELECT d.deliberation_id, d.session_id, d.sealed_at, s.status "
        "FROM deliberations d JOIN sessions s ON s.session_id = d.session_id "
        "WHERE d.deliberation_id=?",
        (p["deliberation_id"],),
    ).fetchone()
    if delib is None:
        raise SelvedgeError("E_NOT_FOUND", f"deliberation_id={p['deliberation_id']}")
    if delib["status"] != "open":
        raise SelvedgeError("E_REFUSAL_T06", f"deliberation belongs to a {delib['status']} session")
    cur = conn.execute(
        "INSERT INTO perspectives (deliberation_id, label, family, body_md) VALUES (?,?,?,?)",
        (p["deliberation_id"], p["label"], p["family"], p["body_md"]),
    )
    pid = cur.lastrowid
    alias = f"P-{p['deliberation_id']}-{p['label']}"
    oid = _link_object(conn, "perspectives", "perspective_id", pid, "perspective", alias)
    _check_role_capability(conn, role, "refs", "insert")
    n_refs = _record_refs(conn, source_object_id=oid, body_md=p["body_md"], extra_refs=p.get("refs", []) or [])
    return {"perspective_id": pid, "object_id": oid, "alias": alias, "refs": n_refs}


def _submit_deliberation_seal(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "deliberations", "update")
    delib = conn.execute(
        "SELECT d.deliberation_id, d.sealed_at, s.status "
        "FROM deliberations d JOIN sessions s ON s.session_id = d.session_id "
        "WHERE d.deliberation_id=?",
        (p["deliberation_id"],),
    ).fetchone()
    if delib is None:
        raise SelvedgeError("E_NOT_FOUND", f"deliberation_id={p['deliberation_id']}")
    if delib["status"] != "open":
        raise SelvedgeError("E_REFUSAL_T06", f"deliberation belongs to a {delib['status']} session")
    if delib["sealed_at"] is not None:
        raise SelvedgeError(
            "E_ALREADY_SEALED",
            f"deliberation {p['deliberation_id']} already sealed at {delib['sealed_at']}",
        )
    conn.execute(
        "UPDATE deliberations SET sealed_at=strftime('%Y-%m-%dT%H:%M:%fZ','now'), synthesis_md=? "
        "WHERE deliberation_id=?",
        (p.get("synthesis_md"), p["deliberation_id"]),
    )
    sealed = conn.execute(
        "SELECT sealed_at FROM deliberations WHERE deliberation_id=?",
        (p["deliberation_id"],),
    ).fetchone()
    return {"deliberation_id": p["deliberation_id"], "sealed_at": sealed["sealed_at"]}


def _submit_synthesis_point(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "synthesis_points", "insert")
    delib = conn.execute(
        "SELECT d.deliberation_id, d.sealed_at, s.status "
        "FROM deliberations d JOIN sessions s ON s.session_id = d.session_id "
        "WHERE d.deliberation_id=?",
        (p["deliberation_id"],),
    ).fetchone()
    if delib is None:
        raise SelvedgeError("E_NOT_FOUND", f"deliberation_id={p['deliberation_id']}")
    if delib["status"] != "open":
        raise SelvedgeError("E_REFUSAL_T06", f"deliberation belongs to a {delib['status']} session")
    if delib["sealed_at"] is None:
        raise SelvedgeError(
            "E_NOT_SEALED",
            f"synthesis points require a sealed deliberation; {p['deliberation_id']} is open",
        )
    sources = p.get("source_perspectives") or []
    sources_json = json.dumps([int(x) for x in sources])
    cur = conn.execute(
        "INSERT INTO synthesis_points (deliberation_id, kind, label, summary, source_perspectives, body_md) "
        "VALUES (?,?,?,?,?,?)",
        (p["deliberation_id"], p["kind"], p["label"], p["summary"], sources_json, p.get("body_md")),
    )
    spid = cur.lastrowid
    oid = _link_object(conn, "synthesis_points", "synthesis_point_id", spid, "synthesis_point", None)
    n_refs = 0
    if p.get("body_md"):
        _check_role_capability(conn, role, "refs", "insert")
        n_refs = _record_refs(conn, source_object_id=oid, body_md=p["body_md"])
    return {"synthesis_point_id": spid, "object_id": oid, "refs": n_refs}


def _submit_perspective_position(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "perspective_positions", "insert")
    delib = conn.execute(
        "SELECT d.session_id FROM perspectives pe JOIN deliberations d ON d.deliberation_id = pe.deliberation_id "
        "WHERE pe.perspective_id=?",
        (p["perspective_id"],),
    ).fetchone()
    if delib is None:
        raise SelvedgeError("E_NOT_FOUND", f"perspective_id={p['perspective_id']}")
    sess_id = delib["session_id"]
    pos_aid = _insert_atom(conn, role, sess_id, "perspective_position", p["position"])
    cur = conn.execute(
        "INSERT INTO perspective_positions (perspective_id, position_atom_id) VALUES (?,?)",
        (p["perspective_id"], pos_aid),
    )
    pid = cur.lastrowid
    oid = _link_object(conn, "perspective_positions", "position_id", pid, "perspective_position", None)
    return {"position_id": pid, "object_id": oid}


def _submit_perspective_claim(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "perspective_claims", "insert")
    delib = conn.execute(
        "SELECT d.session_id FROM perspectives pe JOIN deliberations d ON d.deliberation_id = pe.deliberation_id "
        "WHERE pe.perspective_id=?",
        (p["perspective_id"],),
    ).fetchone()
    if delib is None:
        raise SelvedgeError("E_NOT_FOUND", f"perspective_id={p['perspective_id']}")
    sess_id = delib["session_id"]
    next_seq = _next_no(conn, "perspective_claims", "seq", "perspective_id", p["perspective_id"])
    claim_aid = _insert_atom(conn, role, sess_id, "perspective_claim", p["claim"])
    cited_oid = _resolve_alias_to_object_id(conn, p["cite"]) if p.get("cite") else None
    cur = conn.execute(
        "INSERT INTO perspective_claims (perspective_id, seq, section_kind, claim_atom_id, cited_object_id) "
        "VALUES (?,?,?,?,?)",
        (p["perspective_id"], next_seq, p["section_kind"], claim_aid, cited_oid),
    )
    pcid = cur.lastrowid
    oid = _link_object(conn, "perspective_claims", "claim_id", pcid, "perspective_claim", None)
    return {"claim_id": pcid, "seq": next_seq, "object_id": oid}
