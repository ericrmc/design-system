"""decision-record precheck handler (T-33 substrate-gate, engine-v49, DV-S179-1).

The precheck is the substrate-detectable form of the operator-named
SHOW-CONTEXT / LIMIT-ENTRY / FORCE-CHECKS triple. It records the agent's
exposure to relevant context (similar OIs, prior DV cites against same
target, active spec clauses, recent supersedes) for a specific decision-
record target, with single-use-nonce + context_sha256 + ttl-bound shape
that the decision-record submit handler verifies inside same write_tx.

Per D-28 synthesis: cognition is not substrate-detectable; only freshness,
target match, pack coverage, and single-use consumption are. The CLI emits
the rendered context body to stdout AND writes the receipt row; the receipt
is the substrate proof, the print is presentation. Read/write separation
per DV-S176-1 D-27: this is a write path; the export tool stays pure-read.
"""

from __future__ import annotations

import hashlib
import secrets
import sqlite3
from typing import List, Optional, Tuple

from .errors import SelvedgeError
from .paths import db_path

PRECHECK_WALKER_VERSION = "v1"
PRECHECK_DEFAULT_TTL = 1800
PRECHECK_TARGET_KINDS = ("decision_v2",)


def _open_session_id(conn: sqlite3.Connection) -> int:
    row = conn.execute("SELECT session_id FROM sessions WHERE status='open' LIMIT 1").fetchone()
    if row is None:
        raise SelvedgeError("E_VALIDATION", "no open session; precheck requires an active session")
    return row["session_id"]


def _gather_sources(
    conn: sqlite3.Connection,
    target_kind: str,
    target_key: str,
    exclude_decision_v2_id: Optional[int] = None,
) -> List[dict]:
    """Walk the substrate for relevant context. Deterministic SQL only;
    per P-2 codex stance, no model-judgment similarity. The returned list is
    ordered: similar_oi (by alias prefix match), prior_dv (target_key match),
    active_clause (spec_clauses where source_decision matches), supersedes
    (recent supersession edges).

    `exclude_decision_v2_id` excludes one in-flight decision_v2 row from the
    prior_dv and recent_supersede queries; verify_and_consume_precheck passes
    the just-inserted `did` so submit-time recompute matches precheck-time
    issue (DV-S180-1: the first kind=schema_migration outcome_type=supersede
    decision exposed the in-flight-row drift).
    """
    sources: List[dict] = []

    # 1. Similar OIs by alias-prefix or target-key fuzzy match.
    rows = conn.execute(
        "SELECT alias, priority, status FROM issues "
        "WHERE status IN ('open','in_progress','blocked') "
        "AND (alias LIKE ? OR alias LIKE ?) "
        "ORDER BY alias LIMIT 5",
        (f"%{target_key[:6]}%", f"%S{target_key[:3]}%"),
    ).fetchall()
    for r in rows:
        body = f"OI {r['alias']} priority={r['priority']} status={r['status']}"
        sources.append(
            {
                "source_kind": "similar_oi",
                "source_alias": r["alias"],
                "relation": "similar-target-key",
                "body": body,
            }
        )

    # 2. Recent prior DVs with target_key matching (last 30 sessions).
    if exclude_decision_v2_id is not None:
        rows = conn.execute(
            "SELECT o.alias AS dv_alias, dv.target_kind, dv.target_key, ta.text AS title "
            "FROM decisions_v2 dv "
            "JOIN objects o ON o.object_kind='decision_v2' AND o.typed_row_id=dv.decision_v2_id "
            "JOIN text_atoms ta ON ta.atom_id=dv.title_atom_id "
            "WHERE dv.target_kind=? AND dv.target_key=? AND dv.decision_v2_id <> ? "
            "ORDER BY dv.decision_v2_id DESC LIMIT 3",
            (target_kind, target_key, exclude_decision_v2_id),
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT o.alias AS dv_alias, dv.target_kind, dv.target_key, ta.text AS title "
            "FROM decisions_v2 dv "
            "JOIN objects o ON o.object_kind='decision_v2' AND o.typed_row_id=dv.decision_v2_id "
            "JOIN text_atoms ta ON ta.atom_id=dv.title_atom_id "
            "WHERE dv.target_kind=? AND dv.target_key=? "
            "ORDER BY dv.decision_v2_id DESC LIMIT 3",
            (target_kind, target_key),
        ).fetchall()
    for r in rows:
        body = f"DV {r['dv_alias']} target={r['target_kind']}/{r['target_key']} title={r['title']}"
        sources.append(
            {
                "source_kind": "prior_dv",
                "source_alias": r["dv_alias"],
                "relation": "same-target-key",
                "body": body,
            }
        )

    # 3. Active spec clauses (last 5 active spec versions).
    rows = conn.execute(
        "SELECT o.alias AS sv_alias, sv.spec_id, sv.version "
        "FROM spec_versions sv "
        "JOIN objects o ON o.object_kind='spec_version' AND o.typed_row_id=sv.spec_version_id "
        "WHERE sv.status='active' "
        "ORDER BY sv.spec_version_id DESC LIMIT 5",
    ).fetchall()
    for r in rows:
        body = f"SPEC {r['sv_alias']} active version={r['version']}"
        sources.append(
            {
                "source_kind": "active_spec",
                "source_alias": r["sv_alias"],
                "relation": "active-version",
                "body": body,
            }
        )

    # 4. Recent supersession DVs (last 3).
    if exclude_decision_v2_id is not None:
        rows = conn.execute(
            "SELECT o.alias AS dv_alias, ta.text AS title "
            "FROM decisions_v2 dv "
            "JOIN objects o ON o.object_kind='decision_v2' AND o.typed_row_id=dv.decision_v2_id "
            "JOIN text_atoms ta ON ta.atom_id=dv.title_atom_id "
            "WHERE dv.outcome_type='supersede' AND dv.decision_v2_id <> ? "
            "ORDER BY dv.decision_v2_id DESC LIMIT 3",
            (exclude_decision_v2_id,),
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT o.alias AS dv_alias, ta.text AS title "
            "FROM decisions_v2 dv "
            "JOIN objects o ON o.object_kind='decision_v2' AND o.typed_row_id=dv.decision_v2_id "
            "JOIN text_atoms ta ON ta.atom_id=dv.title_atom_id "
            "WHERE dv.outcome_type='supersede' "
            "ORDER BY dv.decision_v2_id DESC LIMIT 3",
        ).fetchall()
    for r in rows:
        body = f"SUPERSEDE {r['dv_alias']} title={r['title']}"
        sources.append(
            {
                "source_kind": "recent_supersede",
                "source_alias": r["dv_alias"],
                "relation": "supersedes",
                "body": body,
            }
        )

    return sources


def _render_context(sources: List[dict], target_kind: str, target_key: str) -> str:
    """Render a deterministic markdown body from the sources. The body is
    SHA-256-hashed and recorded as context_sha256; the submit handler
    re-renders and compares for hash equality at consumption time."""
    lines = [
        f"# Decision-record precheck context",
        f"",
        f"**target_kind:** {target_kind}",
        f"**target_key:** {target_key}",
        f"",
    ]
    by_kind: dict[str, list[dict]] = {}
    for s in sources:
        by_kind.setdefault(s["source_kind"], []).append(s)
    for kind in ("similar_oi", "prior_dv", "active_spec", "recent_supersede"):
        if not by_kind.get(kind):
            continue
        lines.append(f"## {kind}")
        for s in by_kind[kind]:
            lines.append(f"- {s['body']}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def cmd_precheck(args) -> int:
    """bin/selvedge precheck --target-kind <k> --target-key <key> [--print]

    Renders the precheck context body, computes context_sha256, generates
    a single-use nonce, inserts decision_prechecks + decision_precheck_sources
    rows for the open session, and prints the body + the nonce to stdout.

    The agent uses the nonce in the subsequent `bin/selvedge submit
    decision-record --payload {... "precheck_nonce": "..."}` call. The
    decision-record submit handler verifies the nonce + recomputes
    context_sha256; mismatch => E_REFUSAL_T33.
    """
    target_kind = args.target_kind
    target_key = args.target_key
    if target_kind not in PRECHECK_TARGET_KINDS:
        raise SelvedgeError(
            "E_VALIDATION",
            f"target_kind must be one of {PRECHECK_TARGET_KINDS}; got {target_kind!r}",
        )
    if not target_key or len(target_key) == 0:
        raise SelvedgeError("E_VALIDATION", "target_key required and non-empty")

    conn = sqlite3.connect(str(db_path()))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")

    try:
        session_id = _open_session_id(conn)
        sources = _gather_sources(conn, target_kind, target_key)
        body = _render_context(sources, target_kind, target_key)
        context_sha = hashlib.sha256(body.encode("utf-8")).hexdigest()
        nonce = secrets.token_hex(16)  # 32 chars

        conn.execute("BEGIN")
        cur = conn.execute(
            "INSERT INTO decision_prechecks "
            "(session_id, target_kind, target_key, context_sha256, nonce, "
            " ttl_seconds, walker_version) VALUES (?,?,?,?,?,?,?)",
            (
                session_id,
                target_kind,
                target_key,
                context_sha,
                nonce,
                PRECHECK_DEFAULT_TTL,
                PRECHECK_WALKER_VERSION,
            ),
        )
        precheck_id = cur.lastrowid
        for ord_i, s in enumerate(sources):
            digest = hashlib.sha256(s["body"].encode("utf-8")).hexdigest()
            source_oid = None
            if s.get("source_alias"):
                row = conn.execute(
                    "SELECT object_id FROM objects WHERE alias=?", (s["source_alias"],)
                ).fetchone()
                source_oid = row["object_id"] if row else None
            conn.execute(
                "INSERT INTO decision_precheck_sources "
                "(precheck_id, ord, source_kind, source_alias, source_object_id, "
                " relation, digest) VALUES (?,?,?,?,?,?,?)",
                (
                    precheck_id,
                    ord_i,
                    s["source_kind"],
                    s.get("source_alias"),
                    source_oid,
                    s.get("relation"),
                    digest,
                ),
            )
        conn.commit()
    finally:
        conn.close()

    if args.print_stdout:
        print(body)
    print(
        f"\nprecheck_id={precheck_id} nonce={nonce} target_kind={target_kind} "
        f"target_key={target_key} context_sha256={context_sha} "
        f"sources={len(sources)} ttl_seconds={PRECHECK_DEFAULT_TTL}"
    )
    return 0


def verify_and_consume_precheck(
    conn: sqlite3.Connection,
    session_id: int,
    target_kind: str,
    target_key: str,
    submitted_nonce: str,
    decision_v2_id: int,
) -> None:
    """T-33 enforcement: invoked by _submit_decision_v2 BEFORE other supports
    inserts so an early refusal does not leave a partial decision row.

    Reads decision_prechecks WHERE session_id=current AND nonce=submitted
    AND consumed_at IS NULL, validates ttl + target_kind + target_key,
    re-renders + compares context_sha256, then UPDATEs consumed_at +
    consumed_by_decision_v2_id atomically inside same write_tx.

    Refuses E_REFUSAL_T33 with refusal text naming the exact failure mode.
    """
    row = conn.execute(
        "SELECT precheck_id, target_kind, target_key, context_sha256, "
        "       ttl_seconds, created_at, consumed_at "
        "FROM decision_prechecks "
        "WHERE session_id=? AND nonce=?",
        (session_id, submitted_nonce),
    ).fetchone()
    if row is None:
        raise SelvedgeError(
            "E_REFUSAL_T33",
            f"no decision_prechecks row for session_id={session_id} nonce={submitted_nonce!r}; "
            f"run `bin/selvedge precheck --target-kind {target_kind} --target-key '{target_key}'` "
            f"and pass the returned nonce in the decision-record payload",
        )
    if row["consumed_at"] is not None:
        raise SelvedgeError(
            "E_REFUSAL_T33",
            f"precheck nonce {submitted_nonce!r} already consumed; "
            f"single-use receipts cannot service multiple decision-records",
        )
    if row["target_kind"] != target_kind:
        raise SelvedgeError(
            "E_REFUSAL_T33",
            f"precheck target_kind={row['target_kind']!r} but decision-record "
            f"target_kind={target_kind!r}; rerun precheck with matching target_kind",
        )
    if row["target_key"] != target_key:
        raise SelvedgeError(
            "E_REFUSAL_T33",
            f"precheck target_key={row['target_key']!r} but decision-record "
            f"target_key={target_key!r}; rerun precheck with matching target_key",
        )
    # TTL check.
    age_row = conn.execute(
        "SELECT (julianday(strftime('%Y-%m-%dT%H:%M:%fZ','now')) - julianday(?)) * 86400 AS secs",
        (row["created_at"],),
    ).fetchone()
    age_seconds = age_row["secs"] if age_row else 0
    if age_seconds is not None and age_seconds > row["ttl_seconds"]:
        raise SelvedgeError(
            "E_REFUSAL_T33",
            f"precheck nonce expired ({age_seconds:.0f}s old, ttl={row['ttl_seconds']}s); "
            f"rerun precheck",
        )
    # Re-render + hash compare. Exclude the just-inserted decision_v2_id so the
    # in-flight row (visible inside the same write_tx) does not drift the hash
    # between precheck-issue and submit-time. DV-S180-1 named this: the first
    # kind=schema_migration outcome_type=supersede DV exposed the rotation in
    # recent_supersede; prior schema_migration DVs all used outcome_type=adopt.
    sources = _gather_sources(
        conn, target_kind, target_key, exclude_decision_v2_id=decision_v2_id
    )
    body = _render_context(sources, target_kind, target_key)
    recomputed_sha = hashlib.sha256(body.encode("utf-8")).hexdigest()
    if recomputed_sha != row["context_sha256"]:
        raise SelvedgeError(
            "E_REFUSAL_T33",
            f"precheck context_sha256 mismatch (stored={row['context_sha256'][:12]}... "
            f"recomputed={recomputed_sha[:12]}...); substrate state changed since "
            f"precheck was issued; rerun precheck",
        )
    # Consume atomically. The UPDATE ... WHERE consumed_at IS NULL is a
    # CAS-style guard: if another transaction consumed this nonce between our
    # SELECT and our UPDATE, rowcount is 0 and we refuse — closing the race
    # window the reviewer identified at finding 194 (S179 iter1).
    cur = conn.execute(
        "UPDATE decision_prechecks SET consumed_at=strftime('%Y-%m-%dT%H:%M:%fZ','now'), "
        "consumed_by_decision_v2_id=? WHERE precheck_id=? AND consumed_at IS NULL",
        (decision_v2_id, row["precheck_id"]),
    )
    if cur.rowcount != 1:
        raise SelvedgeError(
            "E_REFUSAL_T33",
            f"precheck nonce {submitted_nonce!r} consumed by concurrent submit "
            f"between SELECT and UPDATE; rerun precheck and retry",
        )


T33_KIND_REQUIRED = ("substantive", "schema_migration")
T33_KIND_ADMITTED_ZERO = ("procedural", "calibration", "disposition")
