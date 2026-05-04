"""assessment + legacy-import handlers.

T-38 (S195 DV-S195-1): assessment-submit refuses without precheck_nonce
when the assessment_prechecks table exists in the substrate (i.e., from
post-migration-047 onward; sessions opened before that migration are
exempt by ordering-not-by-hardcoded-session-id-check). Mirrors T-33
decision-record precheck shape (engine-v49). Substrate-presented
context-pack via bin/selvedge context; operator-named-mandate at S194-
close: agents avoid the substrate; auto-generation mandatory.
"""

from __future__ import annotations

import calendar
import hashlib
import sqlite3
import time

from ..errors import SelvedgeError
from ._helpers import (
    _atom_session_id,
    _check_role_capability,
    _insert_atom,
    _link_object,
    _session_workspace_no,
)


def _table_exists(conn: sqlite3.Connection, name: str) -> bool:
    row = conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)
    ).fetchone()
    return row is not None


def _verify_and_consume_assessment_precheck(
    conn: sqlite3.Connection, session_id: int, nonce: str
) -> int:
    """T-38: verify the precheck nonce + sha256 + freshness + single-use; mark
    consumed. Returns precheck_id. Raises SelvedgeError on any failure."""
    row = conn.execute(
        "SELECT precheck_id, context_sha256, context_md, ttl_seconds, "
        "       created_at, consumed_at "
        "FROM assessment_prechecks "
        "WHERE session_id=? AND nonce=?",
        (session_id, nonce),
    ).fetchone()
    if row is None:
        raise SelvedgeError(
            "E_REFUSAL_T38",
            f"assessment-submit nonce {nonce!r} does not match any "
            f"assessment_prechecks row for session_id={session_id}; rerun "
            f"`bin/selvedge context [--target <alias>]* --print` to obtain "
            f"a valid nonce, then retry submit with the new nonce.",
        )
    if row["consumed_at"] is not None:
        raise SelvedgeError(
            "E_REFUSAL_T38",
            f"assessment-submit nonce {nonce!r} already consumed at "
            f"{row['consumed_at']}; nonces are single-use. Rerun "
            f"`bin/selvedge context --print` for a fresh nonce.",
        )
    # Freshness: created_at within ttl_seconds of now. Parse as UTC via
    # calendar.timegm (DST-safe, unlike time.mktime - time.timezone which
    # uses fixed standard offset and miscalculates by 3600s during DST).
    # Review-finding S195 iter-1 critical fix.
    created_iso = row["created_at"]
    try:
        # SQLite created_at format: YYYY-MM-DDTHH:MM:SS.mmmZ (UTC).
        created_epoch = calendar.timegm(time.strptime(created_iso[:19], "%Y-%m-%dT%H:%M:%S"))
    except (ValueError, IndexError):
        created_epoch = 0
    age = time.time() - created_epoch
    if age > row["ttl_seconds"]:
        raise SelvedgeError(
            "E_REFUSAL_T38",
            f"assessment-submit nonce {nonce!r} expired (age={age:.0f}s > "
            f"ttl={row['ttl_seconds']}s); rerun `bin/selvedge context --print` "
            f"for a fresh nonce.",
        )
    # sha256 verification: recompute over stored context_md (per codex caution
    # against verifying against current substrate state — substrate drift
    # would otherwise invalidate receipts harmlessly).
    recomputed = hashlib.sha256(row["context_md"].encode("utf-8")).hexdigest()
    if recomputed != row["context_sha256"]:
        raise SelvedgeError(
            "E_REFUSAL_T38",
            f"assessment-submit context_sha256 mismatch on stored pack "
            f"(corruption?); rerun `bin/selvedge context --print` for a fresh receipt.",
        )
    # Atomic single-use consume.
    cur = conn.execute(
        "UPDATE assessment_prechecks SET consumed_at = strftime('%Y-%m-%dT%H:%M:%fZ','now') "
        "WHERE precheck_id=? AND consumed_at IS NULL",
        (row["precheck_id"],),
    )
    if cur.rowcount != 1:
        raise SelvedgeError(
            "E_REFUSAL_T38",
            f"assessment-submit nonce {nonce!r} race-consumed by another writer; "
            f"rerun `bin/selvedge context --print` for a fresh nonce.",
        )
    return row["precheck_id"]


def _submit_assessment(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "assessments", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    wno = _session_workspace_no(conn, sess_id)

    # T-38: assessment-precheck gate (S195 DV-S195-1). Sessions opened
    # before migration 047 are exempt by table-absence; once the table
    # exists the gate fires for every assessment-submit regardless of
    # session.kind per operator-named-mandate at S194-close (no kind=meta
    # admit-zero — triage-only meta still modifies durable state).
    consumed_precheck_id = None
    if _table_exists(conn, "assessment_prechecks"):
        nonce = p.get("precheck_nonce")
        if not nonce:
            raise SelvedgeError(
                "E_REFUSAL_T38",
                "assessment-submit requires precheck_nonce per S195 DV-S195-1 "
                "(operator-named-mandate: substrate-presented context at "
                "assessment-time). Run `bin/selvedge context [--target <alias>]* "
                "--print` to render the substrate-presented pack, write the "
                "receipt row, and emit a single-use nonce; include the nonce "
                "in this submit's payload as `precheck_nonce`.",
            )
        consumed_precheck_id = _verify_and_consume_assessment_precheck(conn, sess_id, nonce)

    state_aid = _insert_atom(conn, role, sess_id, "assessment_item", p["state"])
    cur = conn.execute(
        "INSERT INTO assessments (session_id, state_atom_id) VALUES (?,?)",
        (sess_id, state_aid),
    )
    aid = cur.lastrowid
    alias = f"A-S{wno:03d}"
    oid = _link_object(conn, "assessments", "assessment_id", aid, "assessment", alias)
    if consumed_precheck_id is not None:
        _check_role_capability(conn, role, "assessment_prechecks", "update")
        conn.execute(
            "UPDATE assessment_prechecks SET consumed_by_assessment_id=? WHERE precheck_id=?",
            (aid, consumed_precheck_id),
        )
    _check_role_capability(conn, role, "assessment_agenda_items", "insert")
    items_out = []
    for ord_, item_text in enumerate(p.get("agenda", []), start=1):
        item_aid = _insert_atom(conn, role, sess_id, "assessment_item", item_text)
        conn.execute(
            "INSERT INTO assessment_agenda_items (assessment_id, ord, item_atom_id) VALUES (?,?,?)",
            (aid, ord_, item_aid),
        )
        items_out.append({"ord": ord_, "atom_id": item_aid})
    return {"assessment_id": aid, "object_id": oid, "alias": alias, "agenda": items_out}


def _submit_legacy_import(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "legacy_imports", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    aid = _insert_atom(conn, role, sess_id, "legacy_import", p["text"])
    cur = conn.execute(
        "INSERT INTO legacy_imports (old_table, old_pk, atom_id, decomposition_status, decomposed_in_session_id) "
        "VALUES (?,?,?,?,?)",
        (p["old_table"], p["old_pk"], aid, p.get("decomposition_status", "unratified"), sess_id),
    )
    return {"legacy_import_id": cur.lastrowid, "atom_id": aid}
