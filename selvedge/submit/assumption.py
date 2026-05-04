"""assumption-ledger submit kinds (engine-v54, DV-S198-1).

OI-S196-1 close: typed workspace-scope assumption-register primitive that
the §8.5 close-time audit-step (DV-S155-1) has been referencing as A-NNN
since the audit-step shipped.

Schema (migration 049):
    assumption_ledger(assumption_id PK, session_id FK sessions,
        statement_atom_id FK text_atoms NOT NULL, status TEXT closed-6 enum,
        sub_type TEXT closed-3 enum NULL, four conflict atoms FK text_atoms
        NULL, basis_atom_id FK text_atoms NULL, origin_decision_object_id
        FK objects NULL, last_transition_decision_object_id FK objects NULL,
        object_id FK objects NULL, created_at TEXT).

Status enum (D-6 D-1 P-1 stance adopted; P-2 9-engine-self preserved as
M-2 minority + watch-trigger; P-3 9-disaster-recovery preserved as M-3
minority + watch-trigger):
    'unverified'           — registered, pending verification action.
    'assumed'              — taken on faith; no active verification planned.
    'active-with-conflict' — load-bearing; multi-source disagreement;
                              four-field discipline mandatory (sub_type +
                              four conflict atoms NOT NULL via SQL CHECK).
    'closed'               — verified/resolved; closure-by-convergence/
                              completion/etc.
    'superseded'           — replaced by newer assumption (chain via
                              supersession_ledger SL alias).
    'invalidated'          — disproven by direct evidence.

Sub-type enum (D-6 D-2 P-1 stance adopted; P-2 use-case-discriminator
preserved as M-1 minority + watch-trigger):
    'plan-vs-resource'     — plan-side commitment vs resource-side capacity
                              disagreement (disaster-recovery A-018 / A-020).
    'contested-authority'  — multi-actor authority claims contested
                              (disaster-recovery A-022).
    'rolling-renewal'      — rolling-snapshot status with explicit non-
                              SR-emitting refresh discipline (disaster-
                              recovery A-018 cycle pattern).

Object-registration: every assumption_ledger row registers as a first-class
object with alias AR-S<wno>-<seq> per D-6 C-1 (mirrors S197 SL-S<wno>-<seq>
pattern). object_kind='assumption' (drops _ledger suffix per P-1 + my
synthesis convergence).

Transitions: assumption-status-update kind mutates status in-place AND
records last_transition_decision_object_id FK. Replay walks decisions_v2
+ decision_supports + effects against assumption.object_id for full
status history. M-3 minority preserved (P-3 dedicated history table) as
v2 promotion-trigger if replay-via-decisions proves insufficient.
"""

from __future__ import annotations

import sqlite3

from ..aliases import _resolve_alias_to_object_id
from ..errors import SelvedgeError
from ._helpers import (
    _atom_session_id,
    _check_role_capability,
    _insert_atom,
    _link_object,
    _session_workspace_no,
)


_STATUS_ENUM = (
    "unverified",
    "assumed",
    "active-with-conflict",
    "closed",
    "superseded",
    "invalidated",
)

_SUB_TYPE_ENUM = (
    "plan-vs-resource",
    "contested-authority",
    "rolling-renewal",
)

_CLOSURE_SHAPE_ENUM = (
    "convergence",
    "completion",
    "containment-resolved",
    "supersession",
    "stable-held",
)


def _validate_closure_shape_for_status(status: str, closure_shape: str | None) -> None:
    """Enforce DV-S201-1 status-shape coupling at handler layer.

    The SQL CHECKs are the canonical refusal; this handler-side check fires
    earlier with an actionable error message naming the status-shape mismatch.
    Mirrors _validate_conflict_discipline shape.
    """
    if closure_shape is not None and closure_shape not in _CLOSURE_SHAPE_ENUM:
        raise SelvedgeError(
            "E_VALIDATION",
            f"closure_shape={closure_shape!r} not in {_CLOSURE_SHAPE_ENUM}; "
            f"closed enum per DV-S201-1 (5 canonical shapes from disaster-recovery arc).",
        )

    if status == "closed":
        if closure_shape is None:
            raise SelvedgeError(
                "E_VALIDATION",
                "status='closed' requires closure_shape (one of "
                f"{_CLOSURE_SHAPE_ENUM}); no anonymous closure per DV-S201-1.",
            )
        return

    if status in ("unverified", "assumed", "active-with-conflict"):
        if closure_shape is not None:
            raise SelvedgeError(
                "E_VALIDATION",
                f"closure_shape={closure_shape!r} forbidden for status={status!r} "
                f"(pre-closure status); set closure_shape=null per DV-S201-1 status-shape coupling.",
            )
        return

    if status == "superseded":
        if closure_shape is not None and closure_shape != "supersession":
            raise SelvedgeError(
                "E_VALIDATION",
                f"closure_shape={closure_shape!r} forbidden for status='superseded'; "
                f"only NULL or 'supersession' admissible per DV-S201-1 superseded-narrowing.",
            )
        return

    if status == "invalidated":
        if closure_shape is not None:
            raise SelvedgeError(
                "E_VALIDATION",
                f"closure_shape={closure_shape!r} forbidden for status='invalidated' "
                f"(invalidation is ontologically distinct from closure per DV-S201-1).",
            )
        return


def _alias_for_assumption(session_no: int, idx: int) -> str:
    return f"AR-S{session_no:03d}-{idx}"


def _maybe_atom(conn: sqlite3.Connection, role: str, sess_id: int, text: str | None) -> int | None:
    if text is None:
        return None
    return _insert_atom(conn, role, sess_id, "support_claim", text)


def _maybe_resolve_alias(conn: sqlite3.Connection, alias: str | None) -> int | None:
    if not alias:
        return None
    return _resolve_alias_to_object_id(conn, alias)


def _validate_conflict_discipline(
    status: str,
    sub_type: str | None,
    action_commitment: str | None,
    both_source_citation: str | None,
    resolution_path: str | None,
    expiry_trigger: str | None,
) -> None:
    """Enforce DV-S008-1 four-field discipline at handler layer.

    The SQL CHECK is the canonical refusal; this handler-side check fires
    earlier with a more actionable error message naming exactly which fields
    are missing.
    """
    if status != "active-with-conflict":
        if sub_type is not None:
            raise SelvedgeError(
                "E_VALIDATION",
                f"sub_type is only meaningful when status='active-with-conflict' "
                f"(got status={status!r}); refused per CHECK (sub_type IS NULL OR status='active-with-conflict').",
            )
        return

    missing: list[str] = []
    if sub_type is None:
        missing.append("sub_type")
    if action_commitment is None:
        missing.append("action_commitment")
    if both_source_citation is None:
        missing.append("both_source_citation")
    if resolution_path is None:
        missing.append("resolution_path")
    if expiry_trigger is None:
        missing.append("expiry_trigger")
    if missing:
        raise SelvedgeError(
            "E_VALIDATION",
            f"status='active-with-conflict' requires sub_type AND four conflict atoms "
            f"(action_commitment + both_source_citation + resolution_path + expiry_trigger); "
            f"missing: {', '.join(missing)} per DV-S008-1 four-field discipline.",
        )


def _submit_assumption(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    """Insert one assumption_ledger row + register objects row.

    Required payload:
        statement      (atom)  — 8-480 char assumption statement.

    Optional:
        status         (enum)  — defaults to 'unverified'.
        sub_type       (enum)  — required when status='active-with-conflict'.
        action_commitment      (atom) — required when status='active-with-conflict'.
        both_source_citation   (atom) — required when status='active-with-conflict'.
        resolution_path        (atom) — required when status='active-with-conflict'.
        expiry_trigger         (atom) — required when status='active-with-conflict'.
        basis          (atom)  — optional basis citation.
        origin_decision (alias) — optional DV alias that lifted this assumption.
        closure_shape  (enum)  — DV-S201-1 closure-shape coupling: required
                                 when status='closed'; admitted as NULL or
                                 'supersession' when status='superseded';
                                 refused for unverified/assumed/active-with-
                                 conflict/invalidated. Closed 5-value enum.
        session_no     (int)   — defaults to currently-open session.

    Refusals:
        E_VALIDATION         — missing 'statement', bad status/sub_type/
                               closure_shape enum, four-field discipline
                               incomplete when status='active-with-conflict',
                               status-shape coupling violated (DV-S201-1).
        E_REFUSAL_T01        — origin_decision alias unresolvable.
        E_ATOM_LENGTH        — atom outside 8-480 chars (support_claim bound).
    """
    _check_role_capability(conn, role, "assumption_ledger", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    wno = _session_workspace_no(conn, sess_id)

    statement = p.get("statement")
    if not statement:
        raise SelvedgeError("E_VALIDATION", "assumption requires 'statement' atom (8-480 chars per support_claim bound)")

    status = p.get("status", "unverified")
    if status not in _STATUS_ENUM:
        raise SelvedgeError(
            "E_VALIDATION",
            f"status={status!r} not in {_STATUS_ENUM}; "
            f"closed enum per DV-S198-1 D-1 (P-1 6-value stance adopted; P-2/P-3 9-value preserved as M-2/M-3 minority).",
        )

    sub_type = p.get("sub_type")
    if sub_type is not None and sub_type not in _SUB_TYPE_ENUM:
        raise SelvedgeError(
            "E_VALIDATION",
            f"sub_type={sub_type!r} not in {_SUB_TYPE_ENUM} (or NULL); "
            f"closed enum per DV-S198-1 D-2 (P-1 disaster-recovery 3-value stance adopted; P-2 use-case-discriminator preserved as M-1 minority).",
        )

    action_commitment = p.get("action_commitment")
    both_source_citation = p.get("both_source_citation")
    resolution_path = p.get("resolution_path")
    expiry_trigger = p.get("expiry_trigger")
    basis = p.get("basis")
    origin_decision_alias = p.get("origin_decision")
    closure_shape = p.get("closure_shape")

    _validate_conflict_discipline(
        status, sub_type, action_commitment, both_source_citation, resolution_path, expiry_trigger
    )
    _validate_closure_shape_for_status(status, closure_shape)

    statement_atom_id = _insert_atom(conn, role, sess_id, "support_claim", statement)
    action_aid = _maybe_atom(conn, role, sess_id, action_commitment)
    bsc_aid = _maybe_atom(conn, role, sess_id, both_source_citation)
    rp_aid = _maybe_atom(conn, role, sess_id, resolution_path)
    et_aid = _maybe_atom(conn, role, sess_id, expiry_trigger)
    basis_aid = _maybe_atom(conn, role, sess_id, basis)
    origin_decision_oid = _maybe_resolve_alias(conn, origin_decision_alias)

    cur = conn.execute(
        "INSERT INTO assumption_ledger "
        "(session_id, statement_atom_id, status, sub_type, "
        " action_commitment_atom_id, both_source_citation_atom_id, "
        " resolution_path_atom_id, expiry_trigger_atom_id, "
        " basis_atom_id, origin_decision_object_id, closure_shape) "
        "VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        (
            sess_id, statement_atom_id, status, sub_type,
            action_aid, bsc_aid, rp_aid, et_aid,
            basis_aid, origin_decision_oid, closure_shape,
        ),
    )
    assumption_id = cur.lastrowid

    n_for_session = conn.execute(
        "SELECT COUNT(*) AS n FROM assumption_ledger WHERE session_id=?",
        (sess_id,),
    ).fetchone()["n"]
    alias = _alias_for_assumption(wno, n_for_session)

    oid = _link_object(conn, "assumption_ledger", "assumption_id", assumption_id, "assumption", alias)

    return {
        "assumption_id": assumption_id,
        "object_id": oid,
        "alias": alias,
        "status": status,
        "sub_type": sub_type,
        "closure_shape": closure_shape,
        "origin_decision_object_id": origin_decision_oid,
    }


def _submit_assumption_status_update(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    """Transition an existing assumption_ledger row's status.

    Required payload:
        assumption       (alias) — AR-S<wno>-<seq> alias of the assumption.
        new_status       (enum)  — new status from the closed enum.
        citing_decision  (alias) — DV alias that justifies the transition.
                                   Recorded as last_transition_decision_object_id;
                                   the audit trail is the cited decision's
                                   effects, not a separate history table.

    Optional (required when new_status='active-with-conflict' and the
    existing row does not already carry the four conflict atoms):
        sub_type, action_commitment, both_source_citation,
        resolution_path, expiry_trigger.

    Optional (DV-S201-1 closure-shape coupling):
        closure_shape (enum) — required when new_status='closed'; admitted
            as NULL or 'supersession' when new_status='superseded'; refused
            for unverified/assumed/active-with-conflict/invalidated.

    Refusals:
        E_VALIDATION         — bad new_status / closure_shape enum, four-
                               field discipline incomplete when transitioning
                               TO active-with-conflict, missing required
                               field, status-shape coupling violated.
        E_REFUSAL_T01        — assumption / citing_decision alias unresolvable
                               (or alias does not resolve to an assumption row).
        E_NOT_FOUND          — assumption alias resolves to non-assumption object.
        E_ATOM_LENGTH        — atom outside 8-480 chars.

    Transition-out-of-conflict semantics (reviewer RF-78 clarification):
        When transitioning OUT of 'active-with-conflict' and the existing row
        carries sub_type IS NOT NULL, the handler auto-clears sub_type to
        satisfy the CHECK (sub_type IS NULL OR status='active-with-conflict').
        Caller may pass sub_type=null explicitly via the payload to be
        explicit; the auto-clear is convenience for the common case.
        The four conflict atoms are NOT auto-cleared on transition-out
        (they remain as historical artefacts; the conflict-discipline
        CHECK is vacuous when status != 'active-with-conflict').

    Transition-into-closure semantics (DV-S201-1):
        Transitioning to status='closed' requires closure_shape NOT NULL
        on the resulting row. The validator carries the existing row's
        closure_shape forward when the payload omits closure_shape; if
        the carried value is NULL the handler refuses with a missing-field
        message. Carry-forward of 'supersession' from status='superseded'
        to status='closed' is admitted because 'supersession' is in the
        closed CHECK enum (closure_shape names HOW the assumption left
        active state; supersession-as-closure is the meaning when status
        moves from superseded to closed without override).

    Transition-out-of-closure auto-clear (DV-S201-1):
        Transitioning from any status carrying closure_shape to
        'unverified' / 'assumed' / 'active-with-conflict' / 'invalidated'
        auto-clears closure_shape because those statuses forbid the column.
        Transitions to 'superseded' do NOT auto-clear: superseded narrows
        to NULL or 'supersession' only, so a carried-forward value other
        than those refuses with an actionable error naming the offending
        shape. Caller passes closure_shape explicitly (NULL or
        'supersession') to transition into 'superseded' from a row whose
        prior shape was something else (e.g., closed→superseded).
    """
    _check_role_capability(conn, role, "assumption_ledger", "update")
    sess_id = _atom_session_id(conn, p.get("session_no"))

    assumption_alias = p.get("assumption")
    new_status = p.get("new_status")
    citing_decision_alias = p.get("citing_decision")

    if not assumption_alias:
        raise SelvedgeError("E_VALIDATION", "assumption-status-update requires 'assumption' alias (AR-S<wno>-<seq>)")
    if not new_status:
        raise SelvedgeError("E_VALIDATION", "assumption-status-update requires 'new_status' enum value")
    if new_status not in _STATUS_ENUM:
        raise SelvedgeError(
            "E_VALIDATION",
            f"new_status={new_status!r} not in {_STATUS_ENUM}; closed enum per DV-S198-1 D-1.",
        )
    if not citing_decision_alias:
        raise SelvedgeError(
            "E_VALIDATION",
            "assumption-status-update requires 'citing_decision' alias (DV-S<wno>-<n>); "
            "the cited decision IS the audit trail per DV-S198-1 reject-history-table synthesis.",
        )

    assumption_oid = _resolve_alias_to_object_id(conn, assumption_alias)
    citing_decision_oid = _resolve_alias_to_object_id(conn, citing_decision_alias)

    row = conn.execute(
        "SELECT a.assumption_id, a.status, a.sub_type, "
        "       a.action_commitment_atom_id, a.both_source_citation_atom_id, "
        "       a.resolution_path_atom_id, a.expiry_trigger_atom_id, "
        "       a.closure_shape "
        "FROM assumption_ledger a JOIN objects o ON o.object_id=a.object_id "
        "WHERE o.object_id=? AND o.object_kind='assumption'",
        (assumption_oid,),
    ).fetchone()
    if row is None:
        raise SelvedgeError(
            "E_NOT_FOUND",
            f"alias {assumption_alias!r} did not resolve to an assumption row "
            f"(object_kind != 'assumption' or no back-pointer); refusing transition.",
        )

    sub_type_explicit = "sub_type" in p
    sub_type_payload = p.get("sub_type")
    action_commitment = p.get("action_commitment")
    both_source_citation = p.get("both_source_citation")
    resolution_path = p.get("resolution_path")
    expiry_trigger = p.get("expiry_trigger")
    closure_shape_explicit = "closure_shape" in p
    closure_shape_payload = p.get("closure_shape")

    # DV-S201-1 closure-shape coupling: compute the post-transition value
    # (what will land in the row after UPDATE) and validate that against
    # new_status. Auto-clear fires when transitioning to a status that
    # forbids closure_shape and the payload does not override.
    if closure_shape_explicit:
        effective_closure_shape = closure_shape_payload
    elif row["closure_shape"] is not None and new_status in (
        "unverified", "assumed", "active-with-conflict", "invalidated"
    ):
        effective_closure_shape = None
    else:
        effective_closure_shape = row["closure_shape"]
    _validate_closure_shape_for_status(new_status, effective_closure_shape)

    if new_status == "active-with-conflict":
        existing_action = row["action_commitment_atom_id"]
        existing_bsc = row["both_source_citation_atom_id"]
        existing_rp = row["resolution_path_atom_id"]
        existing_et = row["expiry_trigger_atom_id"]

        # When transitioning TO conflict, the four atoms must be present
        # either via payload or already on the row. sub_type must be present
        # via payload OR via existing row value.
        effective_sub_type = sub_type_payload if sub_type_explicit else row["sub_type"]
        new_action = action_commitment if action_commitment is not None else (None if existing_action is None else "<existing>")
        new_bsc = both_source_citation if both_source_citation is not None else (None if existing_bsc is None else "<existing>")
        new_rp = resolution_path if resolution_path is not None else (None if existing_rp is None else "<existing>")
        new_et = expiry_trigger if expiry_trigger is not None else (None if existing_et is None else "<existing>")

        _validate_conflict_discipline(
            new_status, effective_sub_type, new_action, new_bsc, new_rp, new_et
        )
    elif sub_type_explicit and sub_type_payload is not None:
        # Caller explicitly passed sub_type for a non-conflict status — refuse.
        raise SelvedgeError(
            "E_VALIDATION",
            f"sub_type={sub_type_payload!r} provided for new_status={new_status!r} "
            f"(transition would violate CHECK sub_type IS NULL OR status='active-with-conflict'); "
            f"set sub_type=null when transitioning out of active-with-conflict.",
        )

    update_fragments = ["status=?", "last_transition_decision_object_id=?"]
    params: list = [new_status, citing_decision_oid]

    if sub_type_explicit:
        update_fragments.append("sub_type=?")
        params.append(sub_type_payload)
    elif new_status != "active-with-conflict" and row["sub_type"] is not None:
        update_fragments.append("sub_type=NULL")

    # DV-S201-1 closure-shape coupling: write payload value when explicit;
    # auto-clear when transitioning to a status that forbids closure_shape
    # and the existing row carries one. Auto-narrow when transitioning to
    # 'superseded' with an existing non-supersession shape is NOT done — the
    # validator above refuses that case so we never reach here.
    if closure_shape_explicit:
        update_fragments.append("closure_shape=?")
        params.append(closure_shape_payload)
    elif row["closure_shape"] is not None and new_status in (
        "unverified", "assumed", "active-with-conflict", "invalidated"
    ):
        update_fragments.append("closure_shape=NULL")

    if action_commitment is not None:
        aid = _insert_atom(conn, role, sess_id, "support_claim", action_commitment)
        update_fragments.append("action_commitment_atom_id=?")
        params.append(aid)
    if both_source_citation is not None:
        aid = _insert_atom(conn, role, sess_id, "support_claim", both_source_citation)
        update_fragments.append("both_source_citation_atom_id=?")
        params.append(aid)
    if resolution_path is not None:
        aid = _insert_atom(conn, role, sess_id, "support_claim", resolution_path)
        update_fragments.append("resolution_path_atom_id=?")
        params.append(aid)
    if expiry_trigger is not None:
        aid = _insert_atom(conn, role, sess_id, "support_claim", expiry_trigger)
        update_fragments.append("expiry_trigger_atom_id=?")
        params.append(aid)

    params.append(row["assumption_id"])
    conn.execute(
        f"UPDATE assumption_ledger SET {', '.join(update_fragments)} WHERE assumption_id=?",
        params,
    )

    if closure_shape_explicit:
        result_closure_shape = closure_shape_payload
    elif row["closure_shape"] is not None and new_status in (
        "unverified", "assumed", "active-with-conflict", "invalidated"
    ):
        result_closure_shape = None
    else:
        result_closure_shape = row["closure_shape"]

    return {
        "assumption_id": row["assumption_id"],
        "alias": assumption_alias,
        "object_id": assumption_oid,
        "from_status": row["status"],
        "to_status": new_status,
        "citing_decision_object_id": citing_decision_oid,
        "closure_shape": result_closure_shape,
    }
