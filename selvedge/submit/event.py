"""event-ledger submit kind (engine-v59, DV-S204-1).

OI-S196-4 close: typed C-4 stakeholder-event F-N row primitive that the
disaster-recovery 21-session arc surfaced as the missing typed input-event
seam (system-model 33-43; T+Nh timestamp + named source + N effects).

Schema (migration 054):
    event_ledger(event_id PK, session_id FK, source_atom_id FK NOT NULL,
        event_time_atom_id FK NOT NULL, claim_atom_id FK NOT NULL,
        sealed_at TEXT default now, object_id FK objects NULL,
        created_at TEXT)
    event_effects(effect_id PK, event_id FK NOT NULL, ord INTEGER DEFAULT 0,
        effect_kind TEXT closed-2 enum, target_object_id FK objects NOT NULL,
        reason_atom_id FK text_atoms NULL, created_at TEXT,
        UNIQUE (event_id, ord))

Effect-kind enum at v1 (D-S204-1 D-1 P-1+P-2 over P-3 codex; 2-value tight
per AR-S203-1 polymorphism-shape-without-substance lesson):
    'invalidates-assumption' — event-claim contradicts a registered
                                 assumption; target.object_kind=assumption.
    'confirms-assumption'    — event-claim corroborates a registered
                                 assumption; counters DR-bias per AR-S202-1
                                 cross-app generalization.

Codex 6-value enum (KNOT-2 named edit) preserved as M-2 forward-direction:
v2 widens to {invalidates-node, opens-risk, blocks-resolution-path,
advances-resolution-path} when target object_kinds (node, risk,
resolution_path) ship as Selvedge primitives or external-app substrates.

Per-effect-kind target object_kind allowlist (T-43 SQL trigger + handler-
side actionable refusal at v1): both effect kinds bind target to
object_kind='assumption'. Handler resolves target alias and validates
object_kind before INSERT for actionable refusal text; T-43 is the SQL
backstop per AR-S203-2 synthesis-vs-CHECK lesson.

Object-registration: every event_ledger row registers as a first-class
object with alias EV-S<wno>-<seq> per D-S204-1 C-5 (mirrors AR/SL/CYC
pattern). object_kind='event' (drops _ledger suffix per DV-S198-1 P-1
stance precedent). event_effects child rows do NOT register as objects
(mirrors decision_supports + decision_effects + cycle_trigger precedent).

Inert at v1 (D-S204-1 C-3 universal + codex named edit #4): events do
NOT auto-cascade. invalidates-assumption does NOT auto-set
assumption_ledger.status='invalidated'. Mirrors S203 cycle no-auto-SR
precedent. Codex M-3 watch-trigger preserved if external-app demand
surfaces.

Defer supersession_ledger.origin_event_id to v2 (D-S204-1 C-4 + codex
named edit #5; S197 deferral preserved).
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


_EFFECT_KIND_ENUM = (
    "invalidates-assumption",
    "confirms-assumption",
)

# Per-effect-kind target object_kind allowlist (D-S204-1 D-2 + T-43 trigger).
# At v1 both effect kinds bind to assumption. Map shape persists for v2
# widening per M-2 watch-trigger.
_EFFECT_KIND_TARGET_ALLOWLIST = {
    "invalidates-assumption": ("assumption",),
    "confirms-assumption": ("assumption",),
}


def _alias_for_event(session_no: int, idx: int) -> str:
    return f"EV-S{session_no:03d}-{idx}"


def _validate_effect_kind_target_coupling(
    conn: sqlite3.Connection,
    effect_kind: str,
    target_object_id: int,
) -> None:
    """Enforce per-effect-kind target object_kind coupling at handler layer.

    Fires before INSERT with an actionable error message naming the
    effect_kind, the resolved target object_kind, and the allowed
    target_kinds for the effect_kind. T-43 SQL trigger is the canonical
    refusal (per AR-S203-2 synthesis-vs-CHECK lesson); this is the
    earlier actionable layer.
    """
    row = conn.execute(
        "SELECT object_kind FROM objects WHERE object_id=?",
        (target_object_id,),
    ).fetchone()
    if row is None:
        raise SelvedgeError(
            "E_NOT_FOUND",
            f"target_object_id={target_object_id} not found in objects",
        )
    kind = row["object_kind"]
    allowed = _EFFECT_KIND_TARGET_ALLOWLIST.get(effect_kind, ())
    if kind not in allowed:
        raise SelvedgeError(
            "E_VALIDATION",
            f"event_effects.effect_kind={effect_kind!r} requires target.object_kind "
            f"in {allowed} at v1 (got object_kind={kind!r}); v2 extends per-"
            f"effect-kind allowlist when node/risk/resolution-path primitives "
            f"ship per M-2 watch-trigger.",
        )


def _submit_event(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    """Insert one event_ledger row + N event_effects rows + register objects row.

    Required payload:
        source       (atom)        — 8-480 char source identifier (who reported).
        event_time   (atom)        — 8-480 char observed-time atom (free-text;
                                       admits T+Nh, ISO, domain-specific).
        claim        (atom)        — 8-480 char event claim.
        effects      (list)        — non-empty list of effect dicts; each:
            kind     (enum)        — 'invalidates-assumption' | 'confirms-assumption'.
            target   (alias)       — object alias (must resolve to assumption-
                                       kind at v1 per T-43 + handler allowlist).
            reason   (atom, opt)   — 8-480 char rationale atom.

    Optional:
        session_no   (int)         — defaults to currently-open session.

    Refusals:
        E_VALIDATION    — missing required field, bad effect_kind enum,
                          empty effects list, target object_kind not in
                          per-effect-kind v1 allowlist (handler-side; T-43
                          is SQL backstop).
        E_NOT_FOUND     — target_object_id from alias not found in objects.
        E_REFUSAL_T01   — target alias unresolvable.
        E_REFUSAL_T43   — SQL trigger backstop refusing per-effect-kind
                          target object_kind coupling violation.
        E_REFUSAL_CHECK — UNIQUE(event_id, ord) violation.
        E_ATOM_LENGTH   — atom outside 8-480 chars (support_claim bound).
    """
    _check_role_capability(conn, role, "event_ledger", "insert")
    _check_role_capability(conn, role, "event_effects", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    wno = _session_workspace_no(conn, sess_id)

    source = p.get("source")
    if not source:
        raise SelvedgeError(
            "E_VALIDATION",
            "event requires 'source' atom (8-480 chars per support_claim "
            "bound); the named source of the event-claim per D-S204-1 C-6 + "
            "codex KNOT-8 universal convergence.",
        )

    event_time = p.get("event_time")
    if not event_time:
        raise SelvedgeError(
            "E_VALIDATION",
            "event requires 'event_time' atom (8-480 chars); the observed "
            "time of the event (free-text admitting T+Nh, ISO, or domain-"
            "specific formats; typed temporal column deferred to v2).",
        )

    claim = p.get("claim")
    if not claim:
        raise SelvedgeError(
            "E_VALIDATION",
            "event requires 'claim' atom (8-480 chars); the event-claim "
            "itself per D-S204-1 C-6.",
        )

    effects = p.get("effects")
    if not effects or not isinstance(effects, list):
        raise SelvedgeError(
            "E_VALIDATION",
            "event requires non-empty 'effects' list (each effect: kind, "
            "target, optional reason). An event without effects has no "
            "semantic content per D-S204-1 P-1 stance.",
        )

    # Pre-validate every effect before any INSERT (atomic refusal: nothing
    # lands if any effect is malformed). Resolves target aliases up front.
    # Reviewer F-1 fix: ord collision detection up-front (handler-side
    # E_VALIDATION before SQL UNIQUE refusal) so mixed explicit-and-default
    # ords surface a clean error instead of opaque IntegrityError.
    # Reviewer F-4 fix: empty-string reason treated as missing per F-02
    # cycle.py precedent; refuses at handler before atom-layer
    # E_ATOM_LENGTH fires.
    resolved_effects = []
    for i, eff in enumerate(effects):
        if not isinstance(eff, dict):
            raise SelvedgeError(
                "E_VALIDATION",
                f"effects[{i}] must be a dict with kind, target, optional reason.",
            )
        kind = eff.get("kind")
        if kind not in _EFFECT_KIND_ENUM:
            raise SelvedgeError(
                "E_VALIDATION",
                f"effects[{i}].kind={kind!r} not in {_EFFECT_KIND_ENUM}; "
                f"closed enum per DV-S204-1 D-1 + codex KNOT-2 (P-1+P-2 over "
                f"P-3 6-value at v1; v2 widens per M-2 watch-trigger).",
            )
        target_alias = eff.get("target")
        if not target_alias:
            raise SelvedgeError(
                "E_VALIDATION",
                f"effects[{i}] requires 'target' alias resolving to an "
                f"assumption-kind object at v1 (per-effect-kind allowlist).",
            )
        target_oid = _resolve_alias_to_object_id(conn, target_alias)
        _validate_effect_kind_target_coupling(conn, kind, target_oid)
        reason = eff.get("reason")
        # Reviewer F-4: empty-string reason refused at handler with
        # E_VALIDATION (not E_ATOM_LENGTH at atom-insert layer).
        if reason is not None and not reason:
            raise SelvedgeError(
                "E_VALIDATION",
                f"effects[{i}].reason cannot be empty string; pass non-empty "
                f"8-480 char rationale atom or omit field entirely.",
            )
        resolved_effects.append({
            "kind": kind,
            "target_oid": target_oid,
            "reason": reason,
            "ord": eff.get("ord", i),
        })

    # Reviewer F-1 fix: detect ord collisions up-front. Mixed explicit-and-
    # default ord can collide (e.g. effect[0].ord=1 explicit + effect[1] no
    # ord defaulting to i=1). Refuse with actionable E_VALIDATION naming
    # the duplicate ord before SQL UNIQUE(event_id, ord) fires.
    seen_ords = {}
    for j, eff in enumerate(resolved_effects):
        o = eff["ord"]
        if o in seen_ords:
            raise SelvedgeError(
                "E_VALIDATION",
                f"effects[{j}].ord={o} collides with effects[{seen_ords[o]}].ord={o}; "
                f"per-effect ord must be unique within an event (UNIQUE(event_id, ord)). "
                f"Pass explicit non-colliding ord on every effect, or omit ord on all "
                f"effects to use sequential defaults.",
            )
        seen_ords[o] = j

    # Pin the header atoms.
    source_atom_id = _insert_atom(conn, role, sess_id, "support_claim", source)
    event_time_atom_id = _insert_atom(conn, role, sess_id, "support_claim", event_time)
    claim_atom_id = _insert_atom(conn, role, sess_id, "support_claim", claim)

    # Insert event_ledger header.
    cur = conn.execute(
        "INSERT INTO event_ledger "
        "(session_id, source_atom_id, event_time_atom_id, claim_atom_id) "
        "VALUES (?,?,?,?)",
        (sess_id, source_atom_id, event_time_atom_id, claim_atom_id),
    )
    event_id = cur.lastrowid

    # Insert N effects.
    inserted_effects = []
    for eff in resolved_effects:
        reason_atom_id = (
            _insert_atom(conn, role, sess_id, "support_claim", eff["reason"])
            if eff["reason"] is not None
            else None
        )
        ec = conn.execute(
            "INSERT INTO event_effects "
            "(event_id, ord, effect_kind, target_object_id, reason_atom_id) "
            "VALUES (?,?,?,?,?)",
            (event_id, eff["ord"], eff["kind"], eff["target_oid"], reason_atom_id),
        )
        inserted_effects.append({
            "effect_id": ec.lastrowid,
            "ord": eff["ord"],
            "kind": eff["kind"],
            "target_object_id": eff["target_oid"],
        })

    # Register the event_ledger row as an object with alias EV-S<wno>-<seq>.
    n_for_session = conn.execute(
        "SELECT COUNT(*) AS n FROM event_ledger WHERE session_id=?",
        (sess_id,),
    ).fetchone()["n"]
    alias = _alias_for_event(wno, n_for_session)
    oid = _link_object(conn, "event_ledger", "event_id", event_id, "event", alias)

    return {
        "event_id": event_id,
        "object_id": oid,
        "alias": alias,
        "effects": inserted_effects,
    }
