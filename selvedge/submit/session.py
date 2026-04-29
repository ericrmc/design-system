"""session-open / session-close handlers."""

from __future__ import annotations

import sqlite3

from ..errors import SelvedgeError
from ._helpers import _check_role_capability, _current_session, _meta


def _submit_session_open(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    """Open a session in the substrate.

    Engine-v20+: the caller passes `slug` (kebab-case session name) and `kind`
    (one of coding, spec_only, meta — DV-S105-2 removed the kind=coding default
    so operators must declare intent at open). workspace_id, mode,
    engine_version_at_open are read from workspace_metadata; session_no is
    computed as MAX(existing)+1; workspace_session_no is session_no +
    init_session_offset. The substrate refuses session-open while another
    session is still open (E_SESSION_ALREADY_OPEN).
    """
    _check_role_capability(conn, role, "sessions", "insert")
    open_row = conn.execute("SELECT session_no FROM sessions WHERE status='open'").fetchone()
    if open_row is not None:
        raise SelvedgeError(
            "E_SESSION_ALREADY_OPEN",
            f"session_no={open_row['session_no']} is open; close it before opening another",
        )
    if "slug" not in p or not p["slug"]:
        raise SelvedgeError("E_VALIDATION", "session-open requires slug")
    if "kind" not in p or not p["kind"]:
        raise SelvedgeError(
            "E_VALIDATION",
            "session-open requires kind: one of coding, spec_only, meta",
        )
    kind = p["kind"]
    if kind not in ("coding", "spec_only", "meta"):
        raise SelvedgeError(
            "E_VALIDATION",
            f"session-open kind must be one of coding, spec_only, meta; got {kind!r}",
        )
    workspace_id = _meta(conn, "workspace_id")
    mode = _meta(conn, "mode")
    eng_ver = _meta(conn, "current_engine_version")
    if not (workspace_id and mode and eng_ver):
        raise SelvedgeError(
            "E_VALIDATION",
            "workspace_metadata missing one of: workspace_id, mode, current_engine_version",
        )
    sno_row = conn.execute("SELECT COALESCE(MAX(session_no),0)+1 AS n FROM sessions").fetchone()
    sno = sno_row["n"]
    offset = int(_meta(conn, "init_session_offset", "0"))
    wno = sno + offset
    cur = conn.execute(
        "INSERT INTO sessions (session_no, workspace_session_no, slug, mode, workspace_id, engine_version_at_open, status, kind) "
        "VALUES (?,?,?,?,?,?, 'open', ?)",
        (sno, wno, p["slug"], mode, workspace_id, eng_ver, kind),
    )
    sid = cur.lastrowid
    cur2 = conn.execute(
        "INSERT INTO objects (object_kind, typed_row_id, alias) VALUES ('session', ?, ?)",
        (sid, f"S{wno:03d}"),
    )
    oid = cur2.lastrowid
    return {
        "session_id": sid,
        "object_id": oid,
        "workspace_session_no": wno,
        "session_no": sno,
        "slug": p["slug"],
        "mode": mode,
        "workspace_id": workspace_id,
        "engine_version_at_open": eng_ver,
        "kind": kind,
    }


def _submit_session_close(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    """Close the open session.

    Engine-v20+: caller passes nothing. The handler routes to the unique open
    session and reads `current_engine_version` from workspace_metadata for
    engine_version_at_close.
    """
    _check_role_capability(conn, role, "sessions", "update")
    if "session_no" in p:
        row = conn.execute(
            "SELECT session_id FROM sessions WHERE session_no=? OR workspace_session_no=? LIMIT 1",
            (p["session_no"], p["session_no"]),
        ).fetchone()
        if row is None:
            raise SelvedgeError("E_NOT_FOUND", f"session ref={p['session_no']}")
        sid = row["session_id"]
    else:
        sid = _current_session(conn)["session_id"]
    eng_ver = p.get("engine_version_at_close") or _meta(conn, "current_engine_version")
    if not eng_ver:
        raise SelvedgeError(
            "E_VALIDATION",
            "engine_version_at_close not provided and workspace_metadata.current_engine_version missing",
        )
    conn.execute(
        "UPDATE sessions SET status='closed', engine_version_at_close=?, "
        "closed_at=strftime('%Y-%m-%dT%H:%M:%fZ','now') WHERE session_id=?",
        (eng_ver, sid),
    )
    return {"session_id": sid, "engine_version_at_close": eng_ver}
