"""cycle-ledger submit kind (engine-v57, DV-S203-1).

OI-S196-6 close: typed C-6 rolling-renewal cycle primitive that the disaster-
recovery arc (A-018 satellite uplink, A-020 medevac) surfaced as a missing
substrate seam. DV-S011-5 design pattern named 24h-rolling-renewal with body-
field snapshots and N-consecutive-cycles trigger conditions.

Schema (migration 052):
    cycle_ledger(cycle_id PK, session_id FK sessions, subject_object_id FK
        objects NOT NULL, cycle_no INTEGER NOT NULL, observed_at TEXT default
        now, snapshot_atom_id FK text_atoms NOT NULL, classification TEXT
        closed-2 enum, classification_reason_atom_id FK text_atoms NULL,
        citing_supersession_object_id FK objects NULL, object_id FK objects
        NULL, created_at TEXT, UNIQUE (subject, cycle_no), CHECK substantial
        requires reason atom).

Classification enum (D-9 D-2 P-1+P-3-simpler stance adopted; P-2+P-3-hybrid
preserved as forward-direction):
    'substantial'     — cycle moves closure-path eligibility, trigger-counter
                          advance, or underlying conflict shape; reason atom
                          required.
    'non-substantial' — rolling-renewal continues; reason atom admits NULL.

Subject allowlist (D-9 D-1 P-3 stance adopted; P-1 AR-only as M-1 watch-
trigger; P-2 broader [issue, decision_v2] as M-2 watch-trigger):
    Allowlist at v1 = {'assumption'} only. T-42 SQL trigger refuses non-
    allowlist subject_kind on insert. v2 extends allowlist via gate-promotion
    OI when calibration-EFs surface cross-app cycle attempts.

Object-registration: every cycle_ledger row registers as a first-class object
with alias CYC-S<wno>-<seq> per D-9 C-5 (mirrors S197 SL/S198 AR pattern).
object_kind='cycle' (drops _ledger suffix per DV-S198-1 P-1 stance precedent).

Auto-SR suppression (D-9 C-1): cycle row IS the substrate proof of observation;
non-substantial cycles emit zero supersession_ledger rows. Substantial cycles
MAY optionally cite an SL row via citing_supersession when a real supersession
relation exists; handler does NOT auto-emit SL (operator/agent decides).

Closure-path reuse (D-9 C-2): cycle_ledger does not carry own closure_shape
column; closure semantics flow via parent assumption_ledger.closure_shape per
DV-S201-1 no-premature-unification binding (CF-3 nilled-by-exclusion).
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


_CLASSIFICATION_ENUM = (
    "substantial",
    "non-substantial",
)

_SUBJECT_ALLOWLIST = ("assumption",)


def _alias_for_cycle(session_no: int, idx: int) -> str:
    return f"CYC-S{session_no:03d}-{idx}"


def _maybe_resolve_alias(conn: sqlite3.Connection, alias: str | None) -> int | None:
    if not alias:
        return None
    return _resolve_alias_to_object_id(conn, alias)


def _validate_subject_kind(conn: sqlite3.Connection, subject_object_id: int) -> str:
    """Enforce v1 allowlist at handler layer ahead of T-42 SQL trigger.

    Fires before INSERT with an actionable error message naming the
    allowlist + recovery path. The SQL trigger T-42 is the canonical
    refusal; this is the early actionable layer.
    """
    row = conn.execute(
        "SELECT object_kind FROM objects WHERE object_id=?",
        (subject_object_id,),
    ).fetchone()
    if row is None:
        raise SelvedgeError(
            "E_NOT_FOUND",
            f"subject_object_id={subject_object_id} not found in objects",
        )
    kind = row["object_kind"]
    if kind not in _SUBJECT_ALLOWLIST:
        raise SelvedgeError(
            "E_VALIDATION",
            f"cycle_ledger subject must be in {_SUBJECT_ALLOWLIST} at v1 "
            f"(got object_kind={kind!r}); v2 extends allowlist via gate-promotion "
            f"OI when calibration-EFs surface cross-app cycle attempts per M-2 "
            f"watch-trigger.",
        )
    return kind


def _validate_classification_discipline(
    classification: str,
    classification_reason: str | None,
    citing_supersession_alias: str | None,
) -> None:
    """Enforce D-9 D-2 + D-9 C-1 synthesis at handler layer.

    D-9 D-2: substantial requires classification_reason atom.
    D-9 C-1: non-substantial NEVER cites SL; auto-SR suppression mechanism.

    Mirrors SQL CHECKs in migrations 052 + 053; this handler-side check fires
    earlier with actionable error messages naming the constraint violation.
    Empty-string reason treated as missing (vs. relying on _insert_atom's
    E_ATOM_LENGTH refusal at the atom layer; reviewer F-02 fix).
    """
    if classification == "substantial" and not classification_reason:
        raise SelvedgeError(
            "E_VALIDATION",
            "classification='substantial' requires non-empty classification_reason "
            "atom (8-480 chars per support_claim bound); per D-9 D-2 synthesis "
            "substantial cycles must name what moved (closure-path eligibility / "
            "trigger-counter advance / conflict-shape change).",
        )
    if classification == "non-substantial" and citing_supersession_alias:
        raise SelvedgeError(
            "E_VALIDATION",
            "classification='non-substantial' cannot carry citing_supersession; "
            "per D-9 C-1 synthesis non-substantial cycles NEVER cite SL "
            "(auto-SR suppression mechanism: cycle row IS proof of observation). "
            "Mark cycle as 'substantial' if the supersession relation is real.",
        )


def _next_cycle_no_for_subject(conn: sqlite3.Connection, subject_object_id: int) -> int:
    """Next cycle_no per subject (max+1 or 0 if none yet).

    Cycles are monotonic via UNIQUE(subject, cycle_no); strict +1 not
    enforced (codex stance + P-1+P-2+P-3 convergence; agents may pass
    explicit cycle_no override e.g. for migration of legacy data).
    """
    row = conn.execute(
        "SELECT COALESCE(MAX(cycle_no), -1) AS max_no FROM cycle_ledger "
        "WHERE subject_object_id=?",
        (subject_object_id,),
    ).fetchone()
    return int(row["max_no"]) + 1


def _submit_cycle(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    """Insert one cycle_ledger row + register objects row.

    Required payload:
        subject        (alias) — object alias of the cycle's subject (must
                                  resolve to an assumption-kind object at v1
                                  per T-42 + handler allowlist).
        snapshot       (atom)  — 8-480 char observed-state snapshot.
        classification (enum)  — 'substantial' | 'non-substantial'.

    Optional:
        classification_reason (atom)  — required when classification=
                                         'substantial' (D-9 D-2 + SQL CHECK).
        citing_supersession   (alias) — optional SL alias when substantial
                                         cycle records a supersession relation.
        cycle_no              (int)   — optional explicit cycle_no; defaults
                                         to max(existing)+1 per subject.
        observed_at           (str)   — optional ISO timestamp; defaults to
                                         now() at SQL layer.
        session_no            (int)   — defaults to currently-open session.

    Refusals:
        E_VALIDATION    — missing required field, bad classification enum,
                          substantial without reason, subject not in v1
                          allowlist (handler-side; T-42 is SQL backstop).
        E_NOT_FOUND     — subject_object_id from alias not found in objects.
        E_REFUSAL_T01   — subject/citing_supersession alias unresolvable.
        E_REFUSAL_T42   — SQL trigger backstop refusing non-allowlist subject.
        E_REFUSAL_CHECK — UNIQUE(subject, cycle_no) violation, or substantial
                          without reason atom (SQL CHECK).
        E_ATOM_LENGTH   — atom outside 8-480 chars (support_claim bound).
    """
    _check_role_capability(conn, role, "cycle_ledger", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    wno = _session_workspace_no(conn, sess_id)

    subject_alias = p.get("subject")
    if not subject_alias:
        raise SelvedgeError(
            "E_VALIDATION",
            "cycle requires 'subject' alias resolving to an assumption-kind "
            "object at v1 (allowlist={'assumption'} per T-42 + DV-S203-1 D-1).",
        )

    snapshot = p.get("snapshot")
    if not snapshot:
        raise SelvedgeError(
            "E_VALIDATION",
            "cycle requires 'snapshot' atom (8-480 chars per support_claim "
            "bound); the observed-state snapshot at this cycle iteration.",
        )

    classification = p.get("classification")
    if classification is None or classification not in _CLASSIFICATION_ENUM:
        raise SelvedgeError(
            "E_VALIDATION",
            f"classification={classification!r} not in {_CLASSIFICATION_ENUM}; "
            f"closed enum per DV-S203-1 D-9 D-2 (P-1+P-3-simpler stance adopted; "
            f"P-2+P-3-hybrid preserved as forward-direction).",
        )

    classification_reason = p.get("classification_reason")
    citing_supersession_alias = p.get("citing_supersession")
    cycle_no_override = p.get("cycle_no")

    _validate_classification_discipline(classification, classification_reason, citing_supersession_alias)

    subject_object_id = _resolve_alias_to_object_id(conn, subject_alias)
    _validate_subject_kind(conn, subject_object_id)

    citing_supersession_oid = _maybe_resolve_alias(conn, citing_supersession_alias)

    if cycle_no_override is None:
        cycle_no = _next_cycle_no_for_subject(conn, subject_object_id)
    else:
        cycle_no = int(cycle_no_override)

    snapshot_atom_id = _insert_atom(conn, role, sess_id, "support_claim", snapshot)
    reason_atom_id = (
        _insert_atom(conn, role, sess_id, "support_claim", classification_reason)
        if classification_reason is not None
        else None
    )

    cur = conn.execute(
        "INSERT INTO cycle_ledger "
        "(session_id, subject_object_id, cycle_no, snapshot_atom_id, "
        " classification, classification_reason_atom_id, "
        " citing_supersession_object_id) "
        "VALUES (?,?,?,?,?,?,?)",
        (
            sess_id, subject_object_id, cycle_no, snapshot_atom_id,
            classification, reason_atom_id, citing_supersession_oid,
        ),
    )
    cycle_id = cur.lastrowid

    n_for_session = conn.execute(
        "SELECT COUNT(*) AS n FROM cycle_ledger WHERE session_id=?",
        (sess_id,),
    ).fetchone()["n"]
    alias = _alias_for_cycle(wno, n_for_session)

    oid = _link_object(conn, "cycle_ledger", "cycle_id", cycle_id, "cycle", alias)

    return {
        "cycle_id": cycle_id,
        "object_id": oid,
        "alias": alias,
        "subject_object_id": subject_object_id,
        "cycle_no": cycle_no,
        "classification": classification,
    }
