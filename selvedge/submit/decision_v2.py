"""decision-record handler (decision_v2 + supports + effects + alternatives).

Engine-v34 enforces opens_issue/closes_issue target_issue_id at submit time
(T-27, T-31). closes_issue dispatches `_submit_issue_disposition` in-band so
the dependent issue's status flips to 'resolved' before the t28 trigger fires.

Engine-v48 (DV-S176-1, migration 031) ships T-32 substrate-gate: the handler
computes the cited-alias union from supports + alternatives.rejections +
effects.target, dispatches the existing `_export_provenance_anchor` walker
in-band per alias, and inserts decision_chain_walks receipt rows inside the
same write_tx. Walker exceptions, unresolved aliases, and count mismatches
raise E_REFUSAL_T32 with refusal text naming the offending alias. Zero-cite
decisions admit zero receipts (initial spec-version, no supersedes, no DV
cites). Walk-everything per D-27 C-1+D-1 synthesis (P-1 walk-everything
adopted over P-2 predicate-detected obligations).
"""

from __future__ import annotations

import hashlib
import sqlite3
from typing import Optional

from ..aliases import _resolve_alias_to_object_id, _resolve_issue_alias
from ..errors import SelvedgeError
from ..export.anchor import WALKER_VERSION, _export_provenance_anchor
from ..paths import ANCHOR_TRACE_DEFAULT_DEPTH
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

    # T-32 substrate-gate (engine-v48, DV-S176-1, migration 031).
    # Walk every cited alias in supports + alternatives.rejections + effects.target;
    # insert one decision_chain_walks receipt per unique alias inside this write_tx.
    # P-1 walk-everything per D-27 C-1+D-1 synthesis (P-2 predicate-detect preserved
    # as M-1 minority graduation path). Refuses E_REFUSAL_T32 on walker exception or
    # unresolved alias; refusal text names the offending alias per P-3 D-27 defense.
    _check_role_capability(conn, role, "decision_chain_walks", "insert")
    cited: list[str] = []
    seen: set[str] = set()
    for s in p.get("supports", []):
        c = s.get("cite")
        if c and c not in seen:
            seen.add(c)
            cited.append(c)
    for a in p.get("alternatives", []):
        for r in a.get("rejections", []):
            c = r.get("cite")
            if c and c not in seen:
                seen.add(c)
                cited.append(c)
    for e in p.get("effects", []):
        t = e.get("target")
        if t and t not in seen:
            seen.add(t)
            cited.append(t)
    walks_out: list[dict] = []
    for anchor_alias in cited:
        try:
            walk = _export_provenance_anchor(
                conn, anchor_alias, max_depth=ANCHOR_TRACE_DEFAULT_DEPTH, write=False
            )
        except SelvedgeError as exc:
            raise SelvedgeError(
                "E_REFUSAL_T32",
                f"chain-walk failed for cited alias [{anchor_alias}]: {exc.code}: {exc.detail}",
            )
        body = walk["preview"]
        sha = hashlib.sha256(body.encode("utf-8")).hexdigest()
        anchor_oid_row = conn.execute(
            "SELECT object_id FROM objects WHERE alias=?", (anchor_alias,)
        ).fetchone()
        anchor_oid = anchor_oid_row["object_id"] if anchor_oid_row else None
        cur4 = conn.execute(
            "INSERT INTO decision_chain_walks "
            "(decision_v2_id, anchor_alias, anchor_object_id, max_depth, walker_version, "
            " nodes_visited, edges_traversed, truncation_status, result_text, result_sha256) "
            "VALUES (?,?,?,?,?,?,?,?,?,?)",
            (
                did,
                anchor_alias,
                anchor_oid,
                walk["max_depth"],
                walk["walker_version"],
                walk["nodes_visited"],
                walk["edges_traversed"],
                walk["truncation_status"],
                body,
                sha,
            ),
        )
        walks_out.append(
            {
                "chain_walk_id": cur4.lastrowid,
                "anchor_alias": anchor_alias,
                "nodes_visited": walk["nodes_visited"],
                "edges_traversed": walk["edges_traversed"],
                "truncation_status": walk["truncation_status"],
            }
        )
    if len(walks_out) != len(cited):
        raise SelvedgeError(
            "E_REFUSAL_T32",
            f"decision-record cited {len(cited)} aliases but only {len(walks_out)} chain-walk receipts inserted",
        )

    return {
        "decision_v2_id": did,
        "object_id": oid,
        "alias": alias,
        "decision_no": next_no,
        "alternatives": alts_out,
        "chain_walks": walks_out,
    }
