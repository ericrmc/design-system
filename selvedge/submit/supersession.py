"""supersession-ledger submit kind (engine-v53, DV-S197-1).

OI-S196-2 close: typed cross-artefact supersession primitive with objects-FK
polymorphism + 5-value relation enum + soft-deprecation of
decision_effects.supersedes channel.

Schema (migration 048):
    supersession_ledger(ledger_id PK, source_object_id FK objects,
        target_object_id FK objects, relation_kind TEXT CHECK closed-enum,
        sealed_at_session_id FK sessions, reason_atom_id FK text_atoms,
        cite_object_id FK objects NULL, sealed_at TEXT, object_id FK objects).

Polymorphism via objects.object_id FK reaches all 31 typed-row classes;
no source_kind/target_kind discriminator columns (D-S197-1 C-1 convergence).

Relation enum (D-S197-1 D-1 P-1 stance adopted; P-3 4-value preserved as
M-1 minority + watch-trigger if dead-channel persists):
    'supersedes-fully'    — new fully replaces old; old's authority migrated.
    'supersedes-partial'  — new replaces some scope; old retains other scope.
    'bounded-by'          — new bounds the old's interpretation; old still
                            applies in its now-bounded shape (e.g. EF-S196-2
                            bounds DV-S190-2 graduation-discipline scope).
    'replaces-mechanism'  — new replaces a specific mechanism; old's broader
                            frame preserved.
    'retracted-by'        — old withdrawn entirely; new is the retraction
                            record (no replacement substantive content).

Object-registration: every supersession_ledger row registers as a first-class
object with alias SL-S<wno>-<seq> per D-S197-1 D-2 P-2-stance (chain-walks
T-32 reachability requires object-registration).
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


_RELATION_KINDS = (
    "supersedes-fully",
    "supersedes-partial",
    "bounded-by",
    "replaces-mechanism",
    "retracted-by",
)


def _alias_for_supersession_ledger(session_no: int, idx: int) -> str:
    return f"SL-S{session_no:03d}-{idx}"


def _submit_supersession_ledger(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    """Insert one supersession_ledger row + register objects row.

    Required payload:
        source         (alias) — the superseding entity (the new).
        target         (alias) — the superseded entity (the old).
        relation_kind  (enum)  — one of _RELATION_KINDS.
        reason         (atom)  — 8-480 char reason; atom_type=support_claim per OI-S177-1 widening.

    Optional:
        cite           (alias) — authoring decision_v2 or other authority.
        session_no     (int)   — defaults to currently-open session.

    Refusals:
        E_VALIDATION         — missing required payload field, bad relation_kind.
        E_REFUSAL_T01        — source/target/cite alias unresolvable.
        E_ATOM_LENGTH        — reason outside 8-480 chars (support_claim bound).
        E_REFUSAL_CHECK      — source==target (CHECK source!=target),
                               or duplicate (source,target,relation_kind) UNIQUE.
    """
    _check_role_capability(conn, role, "supersession_ledger", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    wno = _session_workspace_no(conn, sess_id)

    source_alias = p.get("source")
    target_alias = p.get("target")
    relation_kind = p.get("relation_kind")
    reason = p.get("reason")
    cite_alias = p.get("cite")

    if not source_alias:
        raise SelvedgeError("E_VALIDATION", "supersession-ledger requires 'source' alias (the superseding entity)")
    if not target_alias:
        raise SelvedgeError("E_VALIDATION", "supersession-ledger requires 'target' alias (the superseded entity)")
    if not relation_kind:
        raise SelvedgeError("E_VALIDATION", "supersession-ledger requires 'relation_kind' (one of " + str(_RELATION_KINDS) + ")")
    if relation_kind not in _RELATION_KINDS:
        raise SelvedgeError(
            "E_VALIDATION",
            f"relation_kind={relation_kind!r} not in {_RELATION_KINDS}; "
            f"closed enum per DV-S197-1 D-1 (P-1 5-value stance adopted, P-3 4-value preserved as M-1 minority).",
        )
    if not reason:
        raise SelvedgeError("E_VALIDATION", "supersession-ledger requires 'reason' atom (8-480 chars per support_claim bound)")

    source_oid = _resolve_alias_to_object_id(conn, source_alias)
    target_oid = _resolve_alias_to_object_id(conn, target_alias)

    if source_oid == target_oid:
        raise SelvedgeError(
            "E_VALIDATION",
            f"source [{source_alias}] and target [{target_alias}] resolve to the same object_id={source_oid}; "
            f"self-supersession refused per CHECK source_object_id!=target_object_id (DV-S197-1 C-5).",
        )

    cite_oid = None
    if cite_alias:
        cite_oid = _resolve_alias_to_object_id(conn, cite_alias)

    reason_atom_id = _insert_atom(conn, role, sess_id, "support_claim", reason)

    cur = conn.execute(
        "INSERT INTO supersession_ledger "
        "(source_object_id, target_object_id, relation_kind, sealed_at_session_id, reason_atom_id, cite_object_id) "
        "VALUES (?,?,?,?,?,?)",
        (source_oid, target_oid, relation_kind, sess_id, reason_atom_id, cite_oid),
    )
    ledger_id = cur.lastrowid

    n_for_session = conn.execute(
        "SELECT COUNT(*) AS n FROM supersession_ledger WHERE sealed_at_session_id=?",
        (sess_id,),
    ).fetchone()["n"]
    alias = _alias_for_supersession_ledger(wno, n_for_session)

    oid = _link_object(conn, "supersession_ledger", "ledger_id", ledger_id, "supersession_ledger", alias)

    return {
        "ledger_id": ledger_id,
        "object_id": oid,
        "alias": alias,
        "source_object_id": source_oid,
        "target_object_id": target_oid,
        "relation_kind": relation_kind,
        "cite_object_id": cite_oid,
    }
