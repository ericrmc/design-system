"""decision-record handler (decision_v2 + supports + effects + alternatives).

Engine-v34 enforces opens_issue/closes_issue target_issue_id at submit time
(T-27, T-31). closes_issue dispatches `_submit_issue_disposition` in-band so
the dependent issue's status flips to 'resolved' before the t28 trigger fires.
"""

from __future__ import annotations

import sqlite3
from typing import Optional

from ..aliases import _resolve_alias_to_object_id, _resolve_issue_alias
from ..errors import SelvedgeError
from ._helpers import (
    _atom_session_id,
    _check_role_capability,
    _insert_atom,
    _link_object,
    _next_no,
    _session_workspace_no,
)
from .issue import _submit_issue_disposition


def _submit_decision_v2(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "decisions_v2", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    wno = _session_workspace_no(conn, sess_id)
    next_no = _next_no(conn, "decisions_v2", "decision_no", "session_id", sess_id)
    title_aid = _insert_atom(conn, role, sess_id, "title", p["title"])
    cur = conn.execute(
        "INSERT INTO decisions_v2 (session_id, decision_no, kind, title_atom_id, outcome_type, target_kind, target_key) "
        "VALUES (?,?,?,?,?,?,?)",
        (sess_id, next_no, p["kind"], title_aid, p["outcome_type"], p["target_kind"], p["target_key"]),
    )
    did = cur.lastrowid
    alias = f"DV-S{wno:03d}-{next_no}"
    oid = _link_object(conn, "decisions_v2", "decision_v2_id", did, "decision_v2", alias)

    _check_role_capability(conn, role, "decision_supports", "insert")
    for seq, s in enumerate(p.get("supports", []), start=1):
        claim_aid = _insert_atom(conn, role, sess_id, "support_claim", s["claim"])
        cited_oid = _resolve_alias_to_object_id(conn, s["cite"]) if s.get("cite") else None
        conn.execute(
            "INSERT INTO decision_supports (decision_v2_id, seq, basis, claim_atom_id, cited_object_id) "
            "VALUES (?,?,?,?,?)",
            (did, seq, s["basis"], claim_aid, cited_oid),
        )

    _check_role_capability(conn, role, "decision_effects", "insert")
    for e in p.get("effects", []):
        target_oid: Optional[int] = None
        target_iid: Optional[int] = None
        if e["effect_kind"] == "closes_issue":
            # DV-S098-1 / engine-v28: closes_issue dispatches the issue
            # disposition before the decision_effects row is inserted, so
            # t28_closes_issue_target_resolved sees status='resolved' and
            # passes. Identity is conveyed via target (issue alias) → target_issue_id.
            if not e.get("target"):
                raise SelvedgeError(
                    "E_VALIDATION",
                    "closes_issue effect requires target naming the issue alias (e.g. OI-016)",
                )
            descriptor = e.get("target_descriptor")
            if not descriptor:
                raise SelvedgeError(
                    "E_VALIDATION",
                    "closes_issue effect requires target_descriptor as the closure reason (becomes the disposition reason atom)",
                )
            if not (8 <= len(descriptor) <= 120):
                # decision_effects.target_descriptor CHECK is 2-120; reason_atom CHECK is 8-240.
                # The intersection (8-120) is the operative range; fail fast with a clearer message.
                raise SelvedgeError(
                    "E_VALIDATION",
                    "closes_issue target_descriptor must be 8-120 characters (becomes the disposition reason atom)",
                )
            target_iid = _resolve_issue_alias(conn, e["target"])
            cur_status = conn.execute(
                "SELECT status FROM issues WHERE issue_id=?", (target_iid,)
            ).fetchone()
            if cur_status is None:
                raise SelvedgeError(
                    "E_NOT_FOUND",
                    f"closes_issue effect target [{e['target']}] vanished between resolve and status check",
                )
            if cur_status["status"] not in ("resolved", "superseded"):
                _submit_issue_disposition(
                    conn,
                    {
                        "alias": e["target"],
                        "to_status": "resolved",
                        "reason": descriptor,
                        "session_no": p.get("session_no"),
                    },
                    role,
                )
        elif e["effect_kind"] == "opens_issue":
            # DV-S118-1 / engine-v34: opens_issue requires target naming an
            # issue alias that already exists; identity is conveyed via
            # target (issue alias) → target_issue_id, mirroring closes_issue
            # (T-27) at the substrate layer (T-31). Unlike closes_issue,
            # which folds the disposition transition in-band, opens_issue
            # does NOT dispatch issue creation — operators register the
            # issue first via `submit issue`, then reference it here.
            if not e.get("target"):
                raise SelvedgeError(
                    "E_VALIDATION",
                    "opens_issue effect requires target naming the issue alias (create the issue first via `submit issue` if needed)",
                )
            target_iid = _resolve_issue_alias(conn, e["target"])
            cur_status = conn.execute(
                "SELECT status FROM issues WHERE issue_id=?", (target_iid,)
            ).fetchone()
            if cur_status is None or cur_status["status"] != "open":
                cur_text = cur_status["status"] if cur_status else "DELETED"
                raise SelvedgeError(
                    "E_VALIDATION",
                    f"opens_issue effect must reference an issue with status='open', but [{e['target']}] has status={cur_text!r}",
                )
        elif e.get("target"):
            target_oid = _resolve_alias_to_object_id(conn, e["target"])
        conn.execute(
            "INSERT INTO decision_effects (decision_v2_id, effect_kind, target_object_id, target_issue_id, target_descriptor) "
            "VALUES (?,?,?,?,?)",
            (did, e["effect_kind"], target_oid, target_iid, e.get("target_descriptor")),
        )

    _check_role_capability(conn, role, "alternatives_v2", "insert")
    _check_role_capability(conn, role, "alternative_rejections", "insert")
    alts_out = []
    for a in p.get("alternatives", []):
        opt_aid = _insert_atom(conn, role, sess_id, "alternative_option", a["option"])
        cur3 = conn.execute(
            "INSERT INTO alternatives_v2 (decision_v2_id, label, option_atom_id) VALUES (?,?,?)",
            (did, a["label"], opt_aid),
        )
        avid = cur3.lastrowid
        alt_alias = f"{alias}-{a['label']}"
        _link_object(conn, "alternatives_v2", "alternative_v2_id", avid, "alternative_v2", alt_alias)
        for seq, r in enumerate(a.get("rejections", []), start=1):
            rej_aid = _insert_atom(conn, role, sess_id, "rejection_reason", r["reason"])
            cited_oid = _resolve_alias_to_object_id(conn, r["cite"]) if r.get("cite") else None
            conn.execute(
                "INSERT INTO alternative_rejections (alternative_v2_id, seq, basis, rejection_atom_id, cited_object_id) "
                "VALUES (?,?,?,?,?)",
                (avid, seq, r["basis"], rej_aid, cited_oid),
            )
        alts_out.append({"alternative_v2_id": avid, "alias": alt_alias})

    return {"decision_v2_id": did, "object_id": oid, "alias": alias, "decision_no": next_no, "alternatives": alts_out}
