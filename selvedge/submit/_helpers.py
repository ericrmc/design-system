"""Shared helpers for submit handlers.

Three patterns get extracted here:

1. Role-capability check (T-12 application-layer).
2. Resolve a session_id from an optional session_no, defaulting to the
   current open session.
3. Insert a typed row's `objects` row and back-link `<table>.object_id` —
   the four-line "INSERT objects … UPDATE table SET object_id" sequence
   that every typed handler repeats.
"""

from __future__ import annotations

import contextvars
import sqlite3
from typing import Optional

from ..errors import SelvedgeError


# Communicates --dry-run intent from cmd_submit into individual handlers
# without changing every handler signature. Most handlers do not consult
# this; only handlers with side-effects outside the SQL transaction
# (currently just _submit_spec_version's body file write) need to read it
# so they can suppress those side-effects when the transaction will be
# rolled back. The contextvar is set by cmd_submit before write_tx and
# reset in finally.
_dry_run_var: contextvars.ContextVar[bool] = contextvars.ContextVar(
    "selvedge_submit_dry_run", default=False
)


def is_dry_run() -> bool:
    return _dry_run_var.get()


def _check_role_capability(conn: sqlite3.Connection, role: str, table: str, op: str) -> None:
    """T-12 application-layer (substrate downgrade documented in migration)."""
    row = conn.execute(
        "SELECT 1 FROM role_write_capabilities WHERE role=? AND table_name=? AND write_op=?",
        (role, table, op),
    ).fetchone()
    if row is None:
        raise SelvedgeError("E_REFUSAL_T12", f"role {role!r} not permitted to {op} {table}")


def _meta(conn: sqlite3.Connection, key: str, default: Optional[str] = None) -> Optional[str]:
    row = conn.execute("SELECT value FROM workspace_metadata WHERE key=?", (key,)).fetchone()
    if row is None:
        return default
    return row["value"]


def _current_session(conn: sqlite3.Connection) -> sqlite3.Row:
    """Return the unique open session row. Raises if none or multiple are open."""
    rows = conn.execute(
        "SELECT session_id, session_no, workspace_session_no, status FROM sessions WHERE status='open'"
    ).fetchall()
    if not rows:
        raise SelvedgeError("E_NO_OPEN_SESSION", "no open session; submit session-open first")
    if len(rows) > 1:
        raise SelvedgeError(
            "E_MULTIPLE_OPEN_SESSIONS",
            f"{len(rows)} open sessions; close all but one before submitting writes",
        )
    return rows[0]


def _atom_session_id(conn: sqlite3.Connection, session_no: int | None = None, require_open: bool = True) -> int:
    """Resolve session_no -> session_id (or default to the current open session)."""
    if session_no is None:
        return _current_session(conn)["session_id"]
    sess = conn.execute(
        "SELECT session_id, status FROM sessions WHERE session_no=? OR workspace_session_no=?",
        (session_no, session_no),
    ).fetchone()
    if sess is None:
        raise SelvedgeError("E_NOT_FOUND", f"session ref={session_no}")
    if require_open and sess["status"] != "open":
        raise SelvedgeError("E_REFUSAL_T06", f"session {session_no} is {sess['status']}; writes refused")
    return sess["session_id"]


def _session_workspace_no(conn: sqlite3.Connection, session_id: int) -> int:
    """Look up workspace_session_no for alias formatting; falls back to
    session_no if workspace_session_no is NULL (pre-005 historical rows)."""
    row = conn.execute(
        "SELECT COALESCE(workspace_session_no, session_no) AS wno FROM sessions WHERE session_id=?",
        (session_id,),
    ).fetchone()
    if row is None:
        raise SelvedgeError("E_NOT_FOUND", f"session_id={session_id}")
    return row["wno"]


def _session_open_or_die(conn: sqlite3.Connection, session_no: int) -> sqlite3.Row:
    sess = conn.execute(
        "SELECT session_id, status FROM sessions WHERE session_no=?",
        (session_no,),
    ).fetchone()
    if sess is None:
        raise SelvedgeError("E_NOT_FOUND", f"session_no={session_no}")
    if sess["status"] != "open":
        raise SelvedgeError(
            "E_REFUSAL_T06",
            f"session {session_no} is {sess['status']}; deliberation work requires an open session",
        )
    return sess


def _insert_atom(conn: sqlite3.Connection, role: str, session_id: int, atom_type: str, text: str) -> int:
    _check_role_capability(conn, role, "text_atoms", "insert")
    cur = conn.execute(
        "INSERT INTO text_atoms (atom_type, text, created_session_id) VALUES (?,?,?)",
        (atom_type, text, session_id),
    )
    aid = cur.lastrowid
    conn.execute(
        "INSERT INTO objects (object_kind, typed_row_id, alias) VALUES ('text_atom', ?, NULL)",
        (aid,),
    )
    return aid


def _link_object(
    conn: sqlite3.Connection,
    table: str,
    pk_col: str,
    pk_value: int,
    object_kind: str,
    alias: Optional[str] = None,
) -> int:
    """Insert an `objects` row for a typed-row pk and back-link via UPDATE.

    Encapsulates the four-line "INSERT objects … UPDATE <table> SET object_id"
    sequence repeated by ~20 typed-row handlers. The table/pk_col are
    interpolated into the UPDATE; both come from constant strings at every
    call site, so this is not a SQL-injection vector.
    """
    cur = conn.execute(
        "INSERT INTO objects (object_kind, typed_row_id, alias) VALUES (?, ?, ?)",
        (object_kind, pk_value, alias),
    )
    oid = cur.lastrowid
    conn.execute(f"UPDATE {table} SET object_id=? WHERE {pk_col}=?", (oid, pk_value))
    return oid


def _next_no(conn: sqlite3.Connection, table: str, col: str, where_col: str, where_val) -> int:
    """COALESCE(MAX(<col>),0)+1 — reused by every per-parent counter."""
    return conn.execute(
        f"SELECT COALESCE(MAX({col}),0)+1 AS n FROM {table} WHERE {where_col}=?",
        (where_val,),
    ).fetchone()["n"]
