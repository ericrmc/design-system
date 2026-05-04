"""close-record handler."""

from __future__ import annotations

import sqlite3

from ..errors import SelvedgeError
from ._helpers import (
    _atom_session_id,
    _check_role_capability,
    _insert_atom,
    _link_object,
    _session_workspace_no,
    _validate_atom,
)


_SCOPING_PASS_PREFIX = "scoping-pass:"
_SCOPING_PASS_NIL_PREFIX = "scoping-pass: 0"
_IMPLICATION_PATTERNS = ("schema-adjacency", "caller-implications", "migration-implications")


def _session_produced_substantive_artefact(conn: sqlite3.Connection, sess_id: int) -> bool:
    """Return True if the session produced any artefact that warrants a
    prospective-scoping receipt per T-41 (DV-S199-1 artefact-gated applicability).

    Substantive artefact = decision_v2 with kind in (substantive, schema_migration)
    OR any spec_versions row for this session. Pure-meta sessions whose only
    writes are FR/EF dispositions + close-ceremony rows admit close-record
    without a scoping-pass receipt.
    """
    row = conn.execute(
        "SELECT 1 FROM decisions_v2 WHERE session_id=? AND kind IN ('substantive','schema_migration') LIMIT 1",
        (sess_id,),
    ).fetchone()
    if row is not None:
        return True
    row = conn.execute(
        "SELECT 1 FROM spec_versions WHERE session_id=? LIMIT 1",
        (sess_id,),
    ).fetchone()
    return row is not None


def _scoping_pass_receipt_present(conn: sqlite3.Connection, sess_id: int) -> tuple[bool, str | None]:
    """Detect whether the session has a valid prospective-scoping receipt.

    Returns (present, refusal_hint). Present is True iff the gate is satisfied:
    either ≥1 assumption_ledger row whose origin_decision_object_id points to a
    DV from this session OR ≥1 engine_feedback row for this session whose
    body_md begins with 'scoping-pass:'. When the engine_feedback receipt is
    used, the body is checked for codex's two formulaic-compliance guards:
    (a) 'scoping-pass: 0' nil_attestation must contain 'exclusions applied:'
    (b) when the session produced a substantive DV or schema_migration, the
        body must mention ≥1 of the three implication patterns by name.

    Path (a) — an AR row attached to a session DV — does NOT trigger the body
    guards (the AR row IS the substantive lift; no nil-attestation prose).
    """
    ar_row = conn.execute(
        "SELECT 1 FROM assumption_ledger a "
        "JOIN objects o ON o.object_id = a.origin_decision_object_id "
        "JOIN decisions_v2 dv ON dv.object_id = o.object_id "
        "WHERE dv.session_id=? LIMIT 1",
        (sess_id,),
    ).fetchone()
    if ar_row is not None:
        return True, None

    ef_rows = conn.execute(
        "SELECT body_md FROM engine_feedback WHERE session_id=?",
        (sess_id,),
    ).fetchall()

    # RF-2 (S199 reviewer): scan every scoping-pass row; admit if any row passes
    # all guards. Track the most-relevant refusal hint from a failing row so the
    # operator gets actionable recovery text when no row passes. Spec says
    # "≥1 row whose body_md begins with scoping-pass:" admits; first-row-fails
    # short-circuit was a bug.
    last_hint: str | None = None
    substantive_dv: bool | None = None
    saw_scoping_pass = False
    for ef in ef_rows:
        # S200 surfaced: §8.6 spec example uses markdown-bold prefix
        # ("**scoping-pass: ..."); strip leading whitespace + leading
        # asterisks so the prefix check tolerates both **scoping-pass:
        # and bare scoping-pass:. Trailing asterisks are not stripped
        # (only the leading prefix region matters for detection).
        body = (ef["body_md"] or "").lstrip().lstrip("*").lstrip()
        body_lower = body.lower()
        if not body_lower.startswith(_SCOPING_PASS_PREFIX):
            continue
        saw_scoping_pass = True

        if body_lower.startswith(_SCOPING_PASS_NIL_PREFIX):
            if "exclusions applied:" not in body_lower:
                last_hint = (
                    "scoping-pass nil_attestation found but missing 'exclusions applied: <which artefact-classes>'; "
                    "cheap-exit must name what was reviewed or why no implications surfaced "
                    "(per DV-S199-1 codex guard #1 against formulaic compliance)."
                )
                continue  # try next row
            if substantive_dv is None:
                substantive_dv = conn.execute(
                    "SELECT 1 FROM decisions_v2 WHERE session_id=? AND kind IN ('substantive','schema_migration') LIMIT 1",
                    (sess_id,),
                ).fetchone() is not None
            if substantive_dv and not any(pat in body_lower for pat in _IMPLICATION_PATTERNS):
                last_hint = (
                    "scoping-pass nil_attestation for a session producing a substantive/schema_migration DV must mention "
                    "≥1 of the three engine-self implication patterns by name (schema-adjacency | caller-implications | "
                    "migration-implications) per DV-S199-1 codex guard #2."
                )
                continue  # try next row
        # row passed all applicable guards
        return True, None

    return False, last_hint if saw_scoping_pass else None


def _t41_close_record_gate(conn: sqlite3.Connection, sess_id: int) -> None:
    """Refuse close-record when the session produced substantive artefacts but
    has no prospective-scoping receipt. DV-S199-1 / OI-S196-5 closure.

    Receipt requirement: either an assumption_ledger row with origin_decision
    set to a session DV, or an engine_feedback row beginning 'scoping-pass:'
    (with codex's two formulaic-compliance guards on the body content).
    """
    if not _session_produced_substantive_artefact(conn, sess_id):
        return
    present, hint = _scoping_pass_receipt_present(conn, sess_id)
    if present:
        return
    if hint is None:
        hint = (
            "submit either a scoping-pass engine_feedback row "
            "(body starts 'scoping-pass: <count> — patterns considered: <named>; lifts: <AR aliases>' "
            "OR 'scoping-pass: 0 — exclusions applied: <which classes reviewed>'), "
            "OR an assumption_ledger row with origin_decision set to a DV from this session, "
            "before submitting close-record."
        )
    raise SelvedgeError(
        "E_REFUSAL_T41",
        f"close-record refused: session produced a substantive artefact but no prospective-scoping receipt is present. {hint}",
    )


def _submit_close_record(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "close_records", "insert")
    # Pre-validate every atom before the first INSERT so a malformed item
    # cannot leave half the close-record's atoms in text_atoms when the
    # transaction rolls back. DV-S134-1 (engine-v41).
    _validate_atom("close_summary", p["summary"], "summary")
    items = p.get("items") or []
    if not items:
        raise SelvedgeError(
            "E_VALIDATION",
            "close-record requires non-empty items[]; submit at least one close_state_item entry (T-41 will refuse session-close otherwise)",
        )
    for idx, item in enumerate(items):
        _validate_atom("close_state_item", item["text"], f"items[{idx}].text")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    _t41_close_record_gate(conn, sess_id)
    wno = _session_workspace_no(conn, sess_id)
    summary_aid = _insert_atom(conn, role, sess_id, "close_summary", p["summary"])
    cur = conn.execute(
        "INSERT INTO close_records (session_id, summary_atom_id) VALUES (?,?)",
        (sess_id, summary_aid),
    )
    crid = cur.lastrowid
    alias = f"C-S{wno:03d}"
    oid = _link_object(conn, "close_records", "close_record_id", crid, "close_record", alias)
    _check_role_capability(conn, role, "close_state_items", "insert")
    items_out = []
    for seq, item in enumerate(p.get("items", []), start=1):
        item_aid = _insert_atom(conn, role, sess_id, "close_state_item", item["text"])
        conn.execute(
            "INSERT INTO close_state_items (close_record_id, seq, facet, item_atom_id) VALUES (?,?,?,?)",
            (crid, seq, item["facet"], item_aid),
        )
        items_out.append({"seq": seq, "facet": item["facet"]})
    return {"close_record_id": crid, "object_id": oid, "alias": alias, "items": items_out}
