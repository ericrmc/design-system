"""spec-version, spec-section, spec-clause handlers."""

from __future__ import annotations

import hashlib
import os
import sqlite3

from ..aliases import _alias_for_spec, _resolve_alias, _resolve_alias_to_object_id
from ..errors import SelvedgeError
from ..paths import workspace_root
from ._helpers import (
    _atom_session_id,
    _check_role_capability,
    _insert_atom,
    _link_object,
)


def _submit_spec_version(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "spec_versions", "insert")
    sess = conn.execute(
        "SELECT session_id FROM sessions WHERE session_no=? AND status='open'",
        (p["session_no"],),
    ).fetchone()
    if sess is None:
        raise SelvedgeError("E_NOT_FOUND", f"open session_no={p['session_no']}")
    body_path = p["body_path"]
    real_path = workspace_root() / body_path
    ws = workspace_root().resolve()
    try:
        real_path.resolve(strict=False).relative_to(ws)
    except (ValueError, OSError) as e:
        raise SelvedgeError(
            "E_VALIDATION",
            f"body_path escapes workspace: {body_path} ({e})",
        )
    body_md = p.get("body_md")
    pending_write_bytes: bytes | None = None
    if body_md is not None:
        # OI-S090-5: substrate-driven authoring path. Handler writes body_path
        # in-process from the inline content. In-process Python file IO is
        # outside the PreToolUse hook scope, so this avoids the Bash heredoc
        # bypass prior sessions used.
        if not isinstance(body_md, str) or not body_md.strip():
            raise SelvedgeError(
                "E_VALIDATION",
                "body_md must be a non-empty string with non-whitespace content",
            )
        body_bytes = body_md.encode("utf-8")
        computed_sha = hashlib.sha256(body_bytes).hexdigest()
        if (declared := p.get("body_sha256")) and declared != computed_sha:
            raise SelvedgeError(
                "E_REFUSAL_T04",
                f"body_md sha mismatch: declared {declared[:8]}…, body_md is {computed_sha[:8]}…",
            )
        body_sha256 = computed_sha
        pending_write_bytes = body_bytes
    else:
        body_sha256 = p["body_sha256"]
        if not real_path.exists():
            raise SelvedgeError("E_REFUSAL_T04", f"spec body not found at {body_path}")
        real_sha = hashlib.sha256(real_path.read_bytes()).hexdigest()
        if real_sha != body_sha256:
            raise SelvedgeError(
                "E_REFUSAL_T04",
                f"body_sha256 mismatch: declared {body_sha256[:8]}…, file is {real_sha[:8]}…",
            )

    # OI-S090-4: flip prev active to superseded BEFORE inserting the new active row.
    # T-03 (unique index t03_spec_versions_one_active) refuses two simultaneously-active
    # rows for the same spec_id; insert-then-flip tripped on every supersession in S087/S088/S089.
    prev_oid = None
    prev_row = None
    if prev := p.get("supersedes"):
        _check_role_capability(conn, role, "refs", "insert")
        _check_role_capability(conn, role, "spec_versions", "update")
        prev_oid = _resolve_alias(conn, prev)
        if prev_oid is None:
            raise SelvedgeError("E_REFUSAL_T01", f"unresolved supersedes alias [{prev}]")
        prev_row = conn.execute(
            "SELECT sv.spec_version_id FROM spec_versions sv JOIN objects o ON o.object_id = sv.object_id WHERE o.object_id=?",
            (prev_oid,),
        ).fetchone()
        if prev_row:
            conn.execute(
                "UPDATE spec_versions SET status='superseded' WHERE spec_version_id=?",
                (prev_row["spec_version_id"],),
            )

    cur = conn.execute(
        "INSERT INTO spec_versions (spec_id, version, body_path, body_sha256, status, session_id) "
        "VALUES (?,?,?,?, 'active', ?)",
        (p["spec_id"], p["version"], body_path, body_sha256, sess["session_id"]),
    )
    svid = cur.lastrowid
    alias = _alias_for_spec(p["spec_id"], p["version"])
    oid = _link_object(conn, "spec_versions", "spec_version_id", svid, "spec_version", alias)

    n_refs = 0
    if prev_oid is not None:
        conn.execute(
            "INSERT INTO refs (source_object_id, target_object_id, relation, allow_superseded, reason_md) "
            "VALUES (?,?, 'supersedes', 1, ?)",
            (oid, prev_oid, p.get("supersedes_reason_md") or "spec_version supersession"),
        )
        n_refs += 1

    # OI-S091: keep workspace_metadata.current_engine_version coherent with the
    # active engine-manifest spec_version. Migration 007 seeded the metadata at
    # engine-v20; bumps in S087/S088/S089/S090 did not propagate, so by S091
    # the metadata had drifted four versions behind. Updates atomically inside
    # the same transaction as the insert. Migration 011 seeded the __cli__
    # UPDATE capability on workspace_metadata.
    if p["spec_id"] == "engine-manifest":
        _check_role_capability(conn, role, "workspace_metadata", "update")
        upd = conn.execute(
            "UPDATE workspace_metadata SET value = ? WHERE key = 'current_engine_version'",
            (f"engine-v{p['version']}",),
        )
        if upd.rowcount != 1:
            raise SelvedgeError(
                "E_VALIDATION",
                f"workspace_metadata.current_engine_version row missing or duplicated "
                f"(rowcount={upd.rowcount}); migrations may be incomplete",
            )

    # Inline body authoring (OI-S090-5): write the file only after every DB
    # constraint above has cleared. If a constraint refuses, the rollback in
    # write_tx leaves no row — and now leaves no orphaned file either. If the
    # FS write itself raises, the same rollback unwinds the row insert.
    if pending_write_bytes is not None:
        real_path.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = real_path.with_suffix(real_path.suffix + ".tmp")
        tmp_path.write_bytes(pending_write_bytes)
        os.replace(tmp_path, real_path)

    return {"spec_version_id": svid, "object_id": oid, "alias": alias, "refs": n_refs}


def _submit_spec_section(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "spec_sections", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    head_aid = _insert_atom(conn, role, sess_id, "title", p["heading"])
    intent_aid = None
    if p.get("intent"):
        intent_aid = _insert_atom(conn, role, sess_id, "spec_section_intent", p["intent"])
    cur = conn.execute(
        "INSERT INTO spec_sections (spec_version_id, ord, heading_atom_id, intent_atom_id) "
        "VALUES (?,?,?,?)",
        (p["spec_version_id"], p["ord"], head_aid, intent_aid),
    )
    ssid = cur.lastrowid
    oid = _link_object(conn, "spec_sections", "spec_section_id", ssid, "spec_section", None)
    return {"spec_section_id": ssid, "object_id": oid}


def _submit_spec_clause(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "spec_clauses", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    aid = _insert_atom(conn, role, sess_id, "spec_clause", p["clause"])
    src_did = None
    if p.get("source_decision_alias"):
        oid = _resolve_alias_to_object_id(conn, p["source_decision_alias"])
        row = conn.execute(
            "SELECT decision_v2_id FROM decisions_v2 WHERE object_id=?", (oid,)
        ).fetchone()
        if row:
            src_did = row["decision_v2_id"]
    cur = conn.execute(
        "INSERT INTO spec_clauses (spec_section_id, ord, clause_type, normative_level, clause_atom_id, source_decision_v2_id) "
        "VALUES (?,?,?,?,?,?)",
        (p["spec_section_id"], p["ord"], p["clause_type"], p["normative_level"], aid, src_did),
    )
    scid = cur.lastrowid
    oid2 = _link_object(conn, "spec_clauses", "spec_clause_id", scid, "spec_clause", None)
    return {"spec_clause_id": scid, "object_id": oid2}
