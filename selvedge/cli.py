"""Selvedge CLI — single-writer SQLite substrate.

Implements the engine-v18 substrate per 078 D-1, D-3, D-8, D-9.

Subcommands:
  init                 Initialise a fresh substrate. Applies migration 001 + any
                       additive migrations beyond it (002, …) via the migrate runner.
  migrate              Apply pending migrations against an existing substrate.
                       --status   list applied + pending
                       --dry-run  parse + T-15 check, no writes
                       --apply    apply each pending in lex order, in-transaction
  id-allocate          Allocate an object_id in-transaction (typed).
  submit               Write a row to the substrate; refuses on T-01..T-16.
                       Kinds: session-open, session-close, decision, spec-version,
                       deliberation-open, perspective, deliberation-seal, synthesis-point.
  validate --precommit Run substrate integrity checks + spec hashes + ref resolution.
  subtract-eligibility Deterministic eligibility report for the human reviewer-subtractor.
  recover              Reset expired work_item leases to 'queued'.
  query                Read-only convenience query for round-trip / debugging.

Single-writer: every write opens its own connection, BEGIN IMMEDIATE, short tx.
Structured errors:
  E_WRITE_BUSY     SQLite lock contention; retry per --retry-budget.
  E_REFUSAL_T<NN>  Substrate refusal (raised by trigger or application-layer parse).
  E_REFUSAL_T15    Migration contains DROP TABLE / DROP COLUMN / ALTER ... DROP.
  E_MIGRATION_DRIFT  Migration file sha256 differs from the row in schema_migrations.
  E_MIGRATION_FAILED Migration apply errored; substrate restored from .pre-migrate-backup.
  E_STALE_SCHEMA   submit's schema_version doesn't match current migration.
  E_SCHEMA_MIGRATING  in-flight migration; queue the write.
  E_NOT_FOUND      referenced object_id / alias does not resolve.

The CLI never surfaces a raw `sqlite3.OperationalError("database is locked")` to its
caller; it converts to E_WRITE_BUSY with retry budget.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sqlite3
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Optional


# ---------------------------------------------------------------------------
# Layout & constants
# ---------------------------------------------------------------------------

WORKSPACE_ROOT_ENV = "SELVEDGE_WORKSPACE"
DEFAULT_BUSY_TIMEOUT_MS = 5000
DEFAULT_RETRY_BUDGET = 5
DEFAULT_RETRY_BASE_MS = 50
DEFAULT_LEASE_SECONDS = 300

# Citable-alias parser (T-01 source). Recognised forms:
#   [D-S<NNN>-<N>]            decision N in session NNN
#   [SPEC-<spec_id>-v<N>]     spec_version
#   [P-<deliberation>-<label>] perspective
#   [C-S<NNN>-<N>]            commitment
#   [EF-S<NNN>-<N>]           engine_feedback
ALIAS_RE = re.compile(
    r"\[("
    r"D-S\d+-\d+"               # decision
    r"|SPEC-[A-Za-z0-9_\-]+-v\d+"
    r"|P-\d+-[A-Za-z0-9_\-]+"
    r"|C-S\d+-\d+"
    r"|EF-S\d+-\d+"
    r")\]"
)


def workspace_root() -> Path:
    if root := os.environ.get(WORKSPACE_ROOT_ENV):
        return Path(root).resolve()
    here = Path.cwd().resolve()
    for candidate in [here, *here.parents]:
        if (candidate / "MODE.md").exists():
            return candidate
    raise SelvedgeError("E_NO_WORKSPACE", f"no MODE.md found from {here} upward; set ${WORKSPACE_ROOT_ENV}")


def db_path() -> Path:
    if override := os.environ.get("SELVEDGE_DB_PATH"):
        return Path(override).resolve()
    return workspace_root() / "state" / "selvedge.sqlite"


def migrations_dir() -> Path:
    if override := os.environ.get("SELVEDGE_MIGRATIONS_DIR"):
        return Path(override).resolve()
    return workspace_root() / "state" / "migrations"


# ---------------------------------------------------------------------------
# Errors
# ---------------------------------------------------------------------------


class SelvedgeError(Exception):
    def __init__(self, code: str, detail: str = "") -> None:
        super().__init__(f"{code}: {detail}" if detail else code)
        self.code = code
        self.detail = detail


def _refusal_from_sqlite(err: sqlite3.IntegrityError | sqlite3.OperationalError | sqlite3.DatabaseError) -> SelvedgeError:
    msg = str(err)
    m = re.search(r"E_REFUSAL_T\d+", msg)
    if m:
        return SelvedgeError(m.group(0), msg)
    if "database is locked" in msg or "database is busy" in msg:
        return SelvedgeError("E_WRITE_BUSY", msg)
    if "CHECK constraint failed" in msg:
        return SelvedgeError("E_REFUSAL_CHECK", msg)
    if "UNIQUE constraint failed" in msg:
        return SelvedgeError("E_REFUSAL_UNIQUE", msg)
    if "FOREIGN KEY constraint failed" in msg:
        return SelvedgeError("E_REFUSAL_FK", msg)
    return SelvedgeError("E_DB", msg)


# ---------------------------------------------------------------------------
# Connection
# ---------------------------------------------------------------------------


@dataclass
class Conn:
    conn: sqlite3.Connection

    @classmethod
    def open(cls, path: Optional[Path] = None) -> "Conn":
        path = path or db_path()
        if not path.parent.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(str(path), isolation_level=None, timeout=DEFAULT_BUSY_TIMEOUT_MS / 1000)
        conn.row_factory = sqlite3.Row
        conn.execute(f"PRAGMA busy_timeout = {DEFAULT_BUSY_TIMEOUT_MS}")
        conn.execute("PRAGMA foreign_keys = ON")
        return cls(conn)

    def close(self) -> None:
        self.conn.close()

    # Single short write transaction with retry on E_WRITE_BUSY.
    def write_tx(self, fn, *, retry_budget: int = DEFAULT_RETRY_BUDGET, retry_base_ms: int = DEFAULT_RETRY_BASE_MS):
        attempt = 0
        while True:
            try:
                self.conn.execute("BEGIN IMMEDIATE")
                try:
                    result = fn(self.conn)
                    self.conn.execute("COMMIT")
                    return result
                except Exception:
                    try:
                        self.conn.execute("ROLLBACK")
                    except sqlite3.OperationalError:
                        pass
                    raise
            except (sqlite3.OperationalError, sqlite3.DatabaseError) as e:
                err = _refusal_from_sqlite(e)
                if err.code == "E_WRITE_BUSY" and attempt < retry_budget:
                    sleep_ms = retry_base_ms * (2 ** attempt)
                    time.sleep(sleep_ms / 1000)
                    attempt += 1
                    continue
                raise err from e
            except sqlite3.IntegrityError as e:
                raise _refusal_from_sqlite(e) from e


# ---------------------------------------------------------------------------
# init
# ---------------------------------------------------------------------------


def cmd_init(args) -> int:
    path = db_path()
    if path.exists() and not args.force:
        print(f"refused: {path} already exists; use --force to overwrite", file=sys.stderr)
        return 2
    if path.exists():
        path.unlink()
    for sidecar in [path.with_suffix(".sqlite-wal"), path.with_suffix(".sqlite-shm")]:
        if sidecar.exists():
            sidecar.unlink()
    migration = migrations_dir() / "001-initial.sql"
    if not migration.exists():
        print(f"missing migration: {migration}", file=sys.stderr)
        return 2
    sql = migration.read_text()
    sha = hashlib.sha256(sql.encode()).hexdigest()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path))
    try:
        conn.executescript(sql)
        # Replace the placeholder sha with the real one.
        conn.execute(
            "UPDATE schema_migrations SET sha256 = ? WHERE name = ?",
            (sha, "001-initial.sql"),
        )
        conn.commit()
    finally:
        conn.close()
    print(f"initialised {path}")
    print(f"migration: 001-initial.sql sha256={sha}")

    # Apply any additive migrations beyond 001 (engine-v18+: 002, …).
    pending = _migration_state(path)["pending"]
    if pending:
        applied_now = _apply_pending(path, pending)
        for name, sha_applied in applied_now:
            print(f"migration: {name} sha256={sha_applied}")
    return 0


# ---------------------------------------------------------------------------
# migrate (079 EF-079-002 / 078 D-3 T-15 / 078 D-8 tier-1 rollback)
# ---------------------------------------------------------------------------

# T-15 forbids destructive DDL in migrations. ADD-only schema discipline; trigger,
# index, and view drops are admitted (they re-shape enforcement, not data).
T15_FORBIDDEN_PATTERNS = [
    (re.compile(r"\bDROP\s+TABLE\b", re.IGNORECASE), "DROP TABLE"),
    (re.compile(r"\bDROP\s+COLUMN\b", re.IGNORECASE), "DROP COLUMN"),
    (re.compile(r"\bALTER\s+TABLE\b[^;]*\bDROP\b", re.IGNORECASE | re.DOTALL), "ALTER TABLE … DROP"),
]

# Strip SQL comments so DDL keywords inside comments don't trip T-15.
_LINE_COMMENT_RE = re.compile(r"--[^\n]*")
_BLOCK_COMMENT_RE = re.compile(r"/\*.*?\*/", re.DOTALL)


def _strip_sql_comments(sql: str) -> str:
    return _BLOCK_COMMENT_RE.sub(" ", _LINE_COMMENT_RE.sub(" ", sql))


def _t15_violations(sql: str) -> list[str]:
    cleaned = _strip_sql_comments(sql)
    found: list[str] = []
    for pat, label in T15_FORBIDDEN_PATTERNS:
        if pat.search(cleaned):
            found.append(label)
    return found


_PLACEHOLDER_SHA = "COMPUTED-AT-APPLY-TIME"


def _migration_state(path: Path) -> dict:
    """Inspect the substrate's schema_migrations against files on disk.

    Returns a dict with:
      applied:  list of {name, sha256_recorded} from schema_migrations
      pending:  list of {name, path, sha256_file, sql} for files not yet applied
      drift:    list of {name, sha256_recorded, sha256_file} for mismatches
    """
    if not path.exists():
        raise SelvedgeError("E_NO_SUBSTRATE", f"no substrate at {path}; run `selvedge init` first")
    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    try:
        applied_rows = conn.execute("SELECT name, sha256 FROM schema_migrations ORDER BY migration_id").fetchall()
    finally:
        conn.close()
    applied_by_name = {r["name"]: r["sha256"] for r in applied_rows}
    files = sorted(migrations_dir().glob("*.sql"))
    applied: list[dict] = [{"name": r["name"], "sha256_recorded": r["sha256"]} for r in applied_rows]
    pending: list[dict] = []
    drift: list[dict] = []
    for f in files:
        sql = f.read_text()
        sha = hashlib.sha256(sql.encode()).hexdigest()
        recorded = applied_by_name.get(f.name)
        if recorded is None:
            pending.append({"name": f.name, "path": f, "sha256_file": sha, "sql": sql})
            continue
        if recorded == _PLACEHOLDER_SHA or recorded == sha:
            continue
        drift.append({"name": f.name, "sha256_recorded": recorded, "sha256_file": sha})
    return {"applied": applied, "pending": pending, "drift": drift}


def _apply_pending(path: Path, pending: list[dict]) -> list[tuple[str, str]]:
    """Apply each pending migration in order. Returns list of (name, sha256).

    Raises SelvedgeError on T-15 violation or apply failure. On apply failure,
    restores the substrate from a pre-migrate backup (078 D-8 tier-1 rollback)
    and re-raises with E_MIGRATION_FAILED.
    """
    if not pending:
        return []
    backup = path.with_suffix(".sqlite.pre-migrate-backup")
    if backup.exists():
        backup.unlink()
    shutil.copy(path, backup)

    applied: list[tuple[str, str]] = []
    for m in pending:
        name = m["name"]
        sql = m["sql"]
        sha = m["sha256_file"]
        violations = _t15_violations(sql)
        if violations:
            raise SelvedgeError(
                "E_REFUSAL_T15",
                f"{name}: contains forbidden DDL ({', '.join(violations)})",
            )
        conn = sqlite3.connect(str(path))
        try:
            try:
                conn.executescript(sql)
                conn.execute(
                    "UPDATE schema_migrations SET sha256 = ? WHERE name = ?",
                    (sha, name),
                )
                conn.commit()
            except Exception as e:
                # Pre-close failure: restore from backup (D-8 tier 1).
                try:
                    conn.close()
                except Exception:
                    pass
                # Drop WAL/SHM sidecars before restoring the file.
                for sidecar in [path.with_suffix(".sqlite-wal"), path.with_suffix(".sqlite-shm")]:
                    if sidecar.exists():
                        sidecar.unlink()
                shutil.copy(backup, path)
                raise SelvedgeError("E_MIGRATION_FAILED", f"{name}: {e}; substrate restored from backup") from e
        finally:
            try:
                conn.close()
            except Exception:
                pass
        applied.append((name, sha))
    return applied


def cmd_migrate(args) -> int:
    path = db_path()
    if not path.exists():
        print(f"no substrate at {path}; run `selvedge init` first", file=sys.stderr)
        return 2
    try:
        state = _migration_state(path)
    except SelvedgeError as e:
        print(json.dumps({"ok": False, "code": e.code, "detail": e.detail}), file=sys.stderr)
        return 3

    if state["drift"]:
        print(
            json.dumps(
                {
                    "ok": False,
                    "code": "E_MIGRATION_DRIFT",
                    "detail": "migration file sha256 differs from schema_migrations row(s)",
                    "drift": state["drift"],
                }
            ),
            file=sys.stderr,
        )
        return 3

    if args.status:
        print(
            json.dumps(
                {
                    "ok": True,
                    "applied": state["applied"],
                    "pending": [{"name": m["name"], "sha256": m["sha256_file"]} for m in state["pending"]],
                },
                indent=2,
            )
        )
        return 0

    # Both --dry-run and --apply check T-15 first.
    parse_errors: list[dict] = []
    for m in state["pending"]:
        violations = _t15_violations(m["sql"])
        if violations:
            parse_errors.append({"name": m["name"], "violations": violations})
    if parse_errors:
        print(
            json.dumps(
                {"ok": False, "code": "E_REFUSAL_T15", "errors": parse_errors},
                indent=2,
            ),
            file=sys.stderr,
        )
        return 3

    if args.dry_run:
        print(
            json.dumps(
                {
                    "ok": True,
                    "dry_run": True,
                    "would_apply": [
                        {"name": m["name"], "sha256": m["sha256_file"]} for m in state["pending"]
                    ],
                },
                indent=2,
            )
        )
        return 0

    # apply
    try:
        applied_now = _apply_pending(path, state["pending"])
    except SelvedgeError as e:
        print(json.dumps({"ok": False, "code": e.code, "detail": e.detail}), file=sys.stderr)
        return 3
    print(
        json.dumps(
            {"ok": True, "applied": [{"name": n, "sha256": s} for n, s in applied_now]},
            indent=2,
        )
    )
    return 0


# ---------------------------------------------------------------------------
# id-allocate (allocates a row in `objects` for a typed row already inserted)
# ---------------------------------------------------------------------------


def cmd_id_allocate(args) -> int:
    if not args.kind or not args.typed_row_id:
        print("usage: selvedge id-allocate --kind <kind> --typed-row-id <N> [--alias A]", file=sys.stderr)
        return 2
    c = Conn.open()

    def do(conn):
        conn.execute(
            "INSERT INTO objects (object_kind, typed_row_id, citable_alias) VALUES (?,?,?)",
            (args.kind, args.typed_row_id, args.alias),
        )
        return conn.execute("SELECT last_insert_rowid() AS rid").fetchone()["rid"]

    try:
        oid = c.write_tx(do)
    except SelvedgeError as e:
        print(e, file=sys.stderr)
        return 3
    finally:
        c.close()
    print(json.dumps({"object_id": oid, "kind": args.kind, "alias": args.alias}))
    return 0


# ---------------------------------------------------------------------------
# submit (parses payload JSON, opens tx, writes row + objects + refs)
# ---------------------------------------------------------------------------


def _resolve_alias(conn: sqlite3.Connection, alias: str) -> Optional[int]:
    row = conn.execute(
        "SELECT object_id FROM objects WHERE citable_alias = ?",
        (alias,),
    ).fetchone()
    return row["object_id"] if row else None


def _alias_for_decision(session_no: int, decision_no: int) -> str:
    return f"D-S{session_no:03d}-{decision_no}"


def _alias_for_spec(spec_id: str, version: int) -> str:
    return f"SPEC-{spec_id}-v{version}"


def _alias_for_commitment(session_no: int, idx: int) -> str:
    return f"C-S{session_no:03d}-{idx}"


def _alias_for_engine_feedback(session_no: int, idx: int) -> str:
    return f"EF-S{session_no:03d}-{idx}"


def _parse_refs(body_md: str) -> list[str]:
    return [m.group(1) for m in ALIAS_RE.finditer(body_md or "")]


def _check_role_capability(conn: sqlite3.Connection, role: str, table: str, op: str) -> None:
    """T-12 application-layer (substrate downgrade documented in migration)."""
    row = conn.execute(
        "SELECT 1 FROM role_write_capabilities WHERE role=? AND table_name=? AND write_op=?",
        (role, table, op),
    ).fetchone()
    if row is None:
        raise SelvedgeError("E_REFUSAL_T12", f"role {role!r} not permitted to {op} {table}")


def _record_refs(
    conn: sqlite3.Connection,
    *,
    source_object_id: int,
    body_md: str,
    extra_refs: Iterable[dict] = (),
) -> int:
    """T-01: parse aliases out of body_md; insert refs rows; refuse if any alias unresolved."""
    aliases = _parse_refs(body_md)
    n = 0
    for alias in aliases:
        target_oid = _resolve_alias(conn, alias)
        if target_oid is None:
            raise SelvedgeError("E_REFUSAL_T01", f"unresolved alias [{alias}] in body_md")
        conn.execute(
            "INSERT INTO refs (source_object_id, target_object_id, relation, allow_superseded, reason_md) "
            "VALUES (?,?,?,?,?)",
            (source_object_id, target_oid, "cites", 0, None),
        )
        n += 1
    for r in extra_refs:
        target_alias = r.get("target_alias")
        target_oid = r.get("target_object_id") or (
            _resolve_alias(conn, target_alias) if target_alias else None
        )
        if target_oid is None:
            raise SelvedgeError("E_REFUSAL_T01", f"unresolved ref target {r!r}")
        conn.execute(
            "INSERT INTO refs (source_object_id, target_object_id, relation, allow_superseded, reason_md) "
            "VALUES (?,?,?,?,?)",
            (
                source_object_id,
                target_oid,
                r.get("relation", "cites"),
                int(r.get("allow_superseded", 0)),
                r.get("reason_md"),
            ),
        )
        n += 1
    return n


def _submit_session_open(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "sessions", "insert")
    cur = conn.execute(
        "INSERT INTO sessions (session_no, slug, mode, workspace_id, engine_version_at_open, status) "
        "VALUES (?,?,?,?,?, 'open')",
        (p["session_no"], p["slug"], p["mode"], p["workspace_id"], p["engine_version_at_open"]),
    )
    sid = cur.lastrowid
    cur2 = conn.execute(
        "INSERT INTO objects (object_kind, typed_row_id, citable_alias) VALUES ('session', ?, ?)",
        (sid, f"S{p['session_no']:03d}"),
    )
    oid = cur2.lastrowid
    return {"session_id": sid, "object_id": oid}


def _submit_session_close(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "sessions", "update")
    sid = conn.execute(
        "SELECT session_id FROM sessions WHERE session_no = ?",
        (p["session_no"],),
    ).fetchone()
    if sid is None:
        raise SelvedgeError("E_NOT_FOUND", f"session_no={p['session_no']}")
    sid = sid["session_id"]
    conn.execute(
        "UPDATE sessions SET status='closed', engine_version_at_close=?, "
        "closed_at=strftime('%Y-%m-%dT%H:%M:%fZ','now') WHERE session_id=?",
        (p["engine_version_at_close"], sid),
    )
    return {"session_id": sid}


def _submit_decision(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "decisions", "insert")
    sess = conn.execute(
        "SELECT session_id, session_no, status FROM sessions WHERE session_no = ?",
        (p["session_no"],),
    ).fetchone()
    if sess is None:
        raise SelvedgeError("E_NOT_FOUND", f"session_no={p['session_no']}")
    if sess["status"] == "closed":
        raise SelvedgeError("E_REFUSAL_T06", f"session {sess['session_no']} is closed")
    next_no = conn.execute(
        "SELECT COALESCE(MAX(decision_no),0)+1 AS n FROM decisions WHERE session_id=?",
        (sess["session_id"],),
    ).fetchone()["n"]
    cur = conn.execute(
        "INSERT INTO decisions (session_id, decision_no, kind, title, body_md) VALUES (?,?,?,?,?)",
        (sess["session_id"], next_no, p["kind"], p["title"], p["body_md"]),
    )
    did = cur.lastrowid
    alias = _alias_for_decision(sess["session_no"], next_no)
    cur2 = conn.execute(
        "INSERT INTO objects (object_kind, typed_row_id, citable_alias) VALUES ('decision', ?, ?)",
        (did, alias),
    )
    oid = cur2.lastrowid
    conn.execute("UPDATE decisions SET object_id=? WHERE decision_id=?", (oid, did))

    # Alternatives
    for a in p.get("alternatives", []) or []:
        _check_role_capability(conn, role, "decision_alternatives", "insert")
        conn.execute(
            "INSERT INTO decision_alternatives (decision_id, label, summary, rejection_reason_md) "
            "VALUES (?,?,?,?)",
            (did, a["label"], a["summary"], a["rejection_reason_md"]),
        )

    # Refs (parsed from body_md + explicit extras).
    _check_role_capability(conn, role, "refs", "insert")
    n_refs = _record_refs(conn, source_object_id=oid, body_md=p["body_md"], extra_refs=p.get("refs", []) or [])

    return {"decision_id": did, "object_id": oid, "alias": alias, "decision_no": next_no, "refs": n_refs}


def _session_open_or_die(conn: sqlite3.Connection, session_no: int) -> sqlite3.Row:
    sess = conn.execute(
        "SELECT session_id, status FROM sessions WHERE session_no=?",
        (session_no,),
    ).fetchone()
    if sess is None:
        raise SelvedgeError("E_NOT_FOUND", f"session_no={session_no}")
    if sess["status"] != "open":
        raise SelvedgeError("E_REFUSAL_T06", f"session {session_no} is {sess['status']}; deliberation work requires an open session")
    return sess


def _submit_deliberation_open(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "deliberations", "insert")
    sess = _session_open_or_die(conn, p["session_no"])
    cur = conn.execute(
        "INSERT INTO deliberations (session_id, topic, sealed_at, synthesis_md) VALUES (?,?,NULL,NULL)",
        (sess["session_id"], p["topic"]),
    )
    did = cur.lastrowid
    cur2 = conn.execute(
        "INSERT INTO objects (object_kind, typed_row_id, citable_alias) VALUES ('deliberation', ?, NULL)",
        (did,),
    )
    oid = cur2.lastrowid
    conn.execute("UPDATE deliberations SET object_id=? WHERE deliberation_id=?", (oid, did))
    return {"deliberation_id": did, "object_id": oid, "session_id": sess["session_id"]}


def _submit_perspective(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "perspectives", "insert")
    delib = conn.execute(
        "SELECT d.deliberation_id, d.session_id, d.sealed_at, s.status "
        "FROM deliberations d JOIN sessions s ON s.session_id = d.session_id "
        "WHERE d.deliberation_id=?",
        (p["deliberation_id"],),
    ).fetchone()
    if delib is None:
        raise SelvedgeError("E_NOT_FOUND", f"deliberation_id={p['deliberation_id']}")
    if delib["status"] != "open":
        raise SelvedgeError("E_REFUSAL_T06", f"deliberation belongs to a {delib['status']} session")
    # T-05 will fire at INSERT-time if sealed; we let the trigger raise rather than pre-checking.
    cur = conn.execute(
        "INSERT INTO perspectives (deliberation_id, label, family, body_md) VALUES (?,?,?,?)",
        (p["deliberation_id"], p["label"], p["family"], p["body_md"]),
    )
    pid = cur.lastrowid
    alias = f"P-{p['deliberation_id']}-{p['label']}"
    cur2 = conn.execute(
        "INSERT INTO objects (object_kind, typed_row_id, citable_alias) VALUES ('perspective', ?, ?)",
        (pid, alias),
    )
    oid = cur2.lastrowid
    conn.execute("UPDATE perspectives SET object_id=? WHERE perspective_id=?", (oid, pid))
    _check_role_capability(conn, role, "refs", "insert")
    n_refs = _record_refs(conn, source_object_id=oid, body_md=p["body_md"], extra_refs=p.get("refs", []) or [])
    return {"perspective_id": pid, "object_id": oid, "alias": alias, "refs": n_refs}


def _submit_deliberation_seal(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "deliberations", "update")
    delib = conn.execute(
        "SELECT d.deliberation_id, d.sealed_at, s.status "
        "FROM deliberations d JOIN sessions s ON s.session_id = d.session_id "
        "WHERE d.deliberation_id=?",
        (p["deliberation_id"],),
    ).fetchone()
    if delib is None:
        raise SelvedgeError("E_NOT_FOUND", f"deliberation_id={p['deliberation_id']}")
    if delib["status"] != "open":
        raise SelvedgeError("E_REFUSAL_T06", f"deliberation belongs to a {delib['status']} session")
    if delib["sealed_at"] is not None:
        raise SelvedgeError("E_ALREADY_SEALED", f"deliberation {p['deliberation_id']} already sealed at {delib['sealed_at']}")
    conn.execute(
        "UPDATE deliberations SET sealed_at=strftime('%Y-%m-%dT%H:%M:%fZ','now'), synthesis_md=? "
        "WHERE deliberation_id=?",
        (p.get("synthesis_md"), p["deliberation_id"]),
    )
    sealed = conn.execute(
        "SELECT sealed_at FROM deliberations WHERE deliberation_id=?",
        (p["deliberation_id"],),
    ).fetchone()
    return {"deliberation_id": p["deliberation_id"], "sealed_at": sealed["sealed_at"]}


def _submit_synthesis_point(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "synthesis_points", "insert")
    delib = conn.execute(
        "SELECT d.deliberation_id, d.sealed_at, s.status "
        "FROM deliberations d JOIN sessions s ON s.session_id = d.session_id "
        "WHERE d.deliberation_id=?",
        (p["deliberation_id"],),
    ).fetchone()
    if delib is None:
        raise SelvedgeError("E_NOT_FOUND", f"deliberation_id={p['deliberation_id']}")
    if delib["status"] != "open":
        raise SelvedgeError("E_REFUSAL_T06", f"deliberation belongs to a {delib['status']} session")
    if delib["sealed_at"] is None:
        raise SelvedgeError("E_NOT_SEALED", f"synthesis points require a sealed deliberation; {p['deliberation_id']} is open")
    sources = p.get("source_perspectives") or []
    sources_json = json.dumps([int(x) for x in sources])
    cur = conn.execute(
        "INSERT INTO synthesis_points (deliberation_id, kind, label, summary, source_perspectives, body_md) "
        "VALUES (?,?,?,?,?,?)",
        (p["deliberation_id"], p["kind"], p["label"], p["summary"], sources_json, p.get("body_md")),
    )
    spid = cur.lastrowid
    cur2 = conn.execute(
        "INSERT INTO objects (object_kind, typed_row_id, citable_alias) VALUES ('synthesis_point', ?, NULL)",
        (spid,),
    )
    oid = cur2.lastrowid
    conn.execute("UPDATE synthesis_points SET object_id=? WHERE synthesis_point_id=?", (oid, spid))
    n_refs = 0
    if p.get("body_md"):
        _check_role_capability(conn, role, "refs", "insert")
        n_refs = _record_refs(conn, source_object_id=oid, body_md=p["body_md"])
    return {"synthesis_point_id": spid, "object_id": oid, "refs": n_refs}


def _submit_spec_version(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "spec_versions", "insert")
    sess = conn.execute(
        "SELECT session_id FROM sessions WHERE session_no=? AND status='open'",
        (p["session_no"],),
    ).fetchone()
    if sess is None:
        raise SelvedgeError("E_NOT_FOUND", f"open session_no={p['session_no']}")
    body_path = p["body_path"]
    body_sha256 = p["body_sha256"]
    # T-04 application-layer: hash the file and refuse on mismatch.
    real_path = workspace_root() / body_path
    if not real_path.exists():
        raise SelvedgeError("E_REFUSAL_T04", f"spec body not found at {body_path}")
    real_sha = hashlib.sha256(real_path.read_bytes()).hexdigest()
    if real_sha != body_sha256:
        raise SelvedgeError("E_REFUSAL_T04", f"body_sha256 mismatch: declared {body_sha256[:8]}…, file is {real_sha[:8]}…")

    cur = conn.execute(
        "INSERT INTO spec_versions (spec_id, version, body_path, body_sha256, status, session_id) "
        "VALUES (?,?,?,?, 'active', ?)",
        (p["spec_id"], p["version"], body_path, body_sha256, sess["session_id"]),
    )
    svid = cur.lastrowid
    alias = _alias_for_spec(p["spec_id"], p["version"])
    cur2 = conn.execute(
        "INSERT INTO objects (object_kind, typed_row_id, citable_alias) VALUES ('spec_version', ?, ?)",
        (svid, alias),
    )
    oid = cur2.lastrowid
    conn.execute("UPDATE spec_versions SET object_id=? WHERE spec_version_id=?", (oid, svid))

    # Optional: supersedes ref to a prior spec_version alias.
    n_refs = 0
    if prev := p.get("supersedes"):
        _check_role_capability(conn, role, "refs", "insert")
        prev_oid = _resolve_alias(conn, prev)
        if prev_oid is None:
            raise SelvedgeError("E_REFUSAL_T01", f"unresolved supersedes alias [{prev}]")
        # Mark the prior version superseded.
        _check_role_capability(conn, role, "spec_versions", "update")
        prev_row = conn.execute(
            "SELECT sv.spec_version_id FROM spec_versions sv JOIN objects o ON o.object_id = sv.object_id WHERE o.object_id=?",
            (prev_oid,),
        ).fetchone()
        if prev_row:
            conn.execute(
                "UPDATE spec_versions SET status='superseded' WHERE spec_version_id=?",
                (prev_row["spec_version_id"],),
            )
        conn.execute(
            "INSERT INTO refs (source_object_id, target_object_id, relation, allow_superseded, reason_md) "
            "VALUES (?,?, 'supersedes', 1, ?)",
            (oid, prev_oid, p.get("supersedes_reason_md") or "spec_version supersession"),
        )
        n_refs += 1
    return {"spec_version_id": svid, "object_id": oid, "alias": alias, "refs": n_refs}


SUBMIT_HANDLERS = {
    "session-open": _submit_session_open,
    "session-close": _submit_session_close,
    "decision": _submit_decision,
    "spec-version": _submit_spec_version,
    "deliberation-open": _submit_deliberation_open,
    "perspective": _submit_perspective,
    "deliberation-seal": _submit_deliberation_seal,
    "synthesis-point": _submit_synthesis_point,
}


def cmd_submit(args) -> int:
    if args.kind not in SUBMIT_HANDLERS:
        print(f"unknown kind: {args.kind}; known: {sorted(SUBMIT_HANDLERS)}", file=sys.stderr)
        return 2
    if args.payload == "-":
        payload = json.load(sys.stdin)
    elif args.payload.startswith("@"):
        payload = json.loads(Path(args.payload[1:]).read_text())
    else:
        payload = json.loads(args.payload)
    role = args.role or "__cli__"
    c = Conn.open()
    try:
        result = c.write_tx(lambda conn: SUBMIT_HANDLERS[args.kind](conn, payload, role))
    except SelvedgeError as e:
        print(json.dumps({"ok": False, "code": e.code, "detail": e.detail}), file=sys.stderr)
        return 3
    finally:
        c.close()
    print(json.dumps({"ok": True, "result": result}))
    return 0


# ---------------------------------------------------------------------------
# validate --precommit
# ---------------------------------------------------------------------------


def cmd_validate(args) -> int:
    path = db_path()
    if not path.exists():
        print(f"no substrate at {path} (run `selvedge init` first)", file=sys.stderr)
        return 2
    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    failures: list[str] = []

    # Integrity
    if (row := conn.execute("PRAGMA integrity_check").fetchone()) and row[0] != "ok":
        failures.append(f"integrity_check: {row[0]}")
    fk = conn.execute("PRAGMA foreign_key_check").fetchall()
    if fk:
        failures.append(f"foreign_key_check: {len(fk)} violations: {[dict(r) for r in fk[:5]]}")

    # Spec hashes (T-04)
    rows = conn.execute(
        "SELECT spec_id, version, body_path, body_sha256 FROM spec_versions WHERE status='active'"
    ).fetchall()
    for r in rows:
        p = workspace_root() / r["body_path"]
        if not p.exists():
            failures.append(f"spec hash: missing file {r['body_path']}")
            continue
        sha = hashlib.sha256(p.read_bytes()).hexdigest()
        if sha != r["body_sha256"]:
            failures.append(f"spec hash mismatch: {r['spec_id']}-v{r['version']} {sha[:8]} != {r['body_sha256'][:8]}")

    # Ref resolution (every refs row resolves to a known object)
    bad_refs = conn.execute(
        "SELECT ref_id FROM refs WHERE source_object_id NOT IN (SELECT object_id FROM objects) "
        "OR target_object_id NOT IN (SELECT object_id FROM objects)"
    ).fetchall()
    if bad_refs:
        failures.append(f"refs: {len(bad_refs)} unresolved")

    # Active session has at most one (workspace invariant in 079)
    n_open = conn.execute("SELECT COUNT(*) AS n FROM sessions WHERE status='open'").fetchone()["n"]
    if n_open > 1:
        failures.append(f"more than one open session: {n_open}")

    # Migration recorded
    last_mig = conn.execute(
        "SELECT name, sha256 FROM schema_migrations ORDER BY migration_id DESC LIMIT 1"
    ).fetchone()
    if last_mig is None:
        failures.append("no schema_migrations rows; substrate appears uninitialised")

    conn.close()
    if failures:
        for f in failures:
            print(f"FAIL  {f}", file=sys.stderr)
        return 1
    print("validate --precommit: ok")
    return 0


# ---------------------------------------------------------------------------
# subtract-eligibility
# ---------------------------------------------------------------------------


def cmd_subtract_eligibility(args) -> int:
    """Deterministic eligibility report. Per 078 D-6: the report is rule-based; the human
    reviewer-subtractor reads it and acts. 079 ships the rule scaffold; numbers are
    operator-tunable in 080+."""
    K_UNCITED = args.uncited_threshold
    M_STALE = args.stale_threshold
    P_TRIAGE = args.untriaged_threshold

    conn = sqlite3.connect(str(db_path()))
    conn.row_factory = sqlite3.Row

    last_session_no = conn.execute(
        "SELECT COALESCE(MAX(session_no),0) AS n FROM sessions"
    ).fetchone()["n"]

    # Specs uncited in K sessions (from active rows only)
    uncited = conn.execute(
        """
        SELECT sv.spec_id, sv.version,
               (SELECT MAX(s.session_no) FROM refs r
                  JOIN objects o_target ON o_target.object_id = r.target_object_id
                  JOIN spec_versions sv2 ON sv2.object_id = o_target.object_id
                  JOIN objects o_source ON o_source.object_id = r.source_object_id
                  JOIN sessions s ON s.session_id = (
                    SELECT CASE o_source.object_kind
                        WHEN 'decision' THEN (SELECT session_id FROM decisions WHERE decision_id = o_source.typed_row_id)
                        ELSE NULL END
                  )
                WHERE sv2.spec_version_id = sv.spec_version_id) AS last_cite_session_no
          FROM spec_versions sv
         WHERE sv.status='active'
        """
    ).fetchall()
    uncited_eligible = []
    for r in uncited:
        last = r["last_cite_session_no"]
        gap = last_session_no - (last or 0)
        if last is None or gap >= K_UNCITED:
            uncited_eligible.append({"spec": f"{r['spec_id']}-v{r['version']}", "last_cite_session_no": last, "gap": gap})

    # Stale commitments (open ≥ M sessions)
    stale = conn.execute(
        """
        SELECT c.commitment_id, c.summary_md, s.session_no AS opened_in
          FROM commitments c
          JOIN decisions d ON d.decision_id = c.decision_id
          JOIN sessions s ON s.session_id = d.session_id
         WHERE c.status='open'
        """
    ).fetchall()
    stale_eligible = [
        {"commitment_id": r["commitment_id"], "summary": r["summary_md"], "opened_in": r["opened_in"], "gap": last_session_no - r["opened_in"]}
        for r in stale
        if last_session_no - r["opened_in"] >= M_STALE
    ]

    # Untriaged engine_feedback (no disposition for ≥ P sessions)
    untri = conn.execute(
        """
        SELECT ef.feedback_id, ef.flag, ef.body_md, s.session_no AS opened_in
          FROM engine_feedback ef
          JOIN sessions s ON s.session_id = ef.session_id
         WHERE ef.disposition IS NULL
        """
    ).fetchall()
    untri_eligible = [
        {"feedback_id": r["feedback_id"], "flag": r["flag"], "summary": (r["body_md"] or "")[:80], "opened_in": r["opened_in"], "gap": last_session_no - r["opened_in"]}
        for r in untri
        if last_session_no - r["opened_in"] >= P_TRIAGE
    ]

    conn.close()
    report = {
        "last_session_no": last_session_no,
        "thresholds": {"uncited": K_UNCITED, "stale": M_STALE, "untriaged": P_TRIAGE},
        "uncited_active_specs": uncited_eligible,
        "stale_open_commitments": stale_eligible,
        "untriaged_engine_feedback": untri_eligible,
    }
    print(json.dumps(report, indent=2))
    return 0


# ---------------------------------------------------------------------------
# recover (T-16 cleanup)
# ---------------------------------------------------------------------------


def cmd_recover(args) -> int:
    c = Conn.open()

    def do(conn):
        cur = conn.execute(
            "UPDATE work_items SET status='queued', leased_by=NULL, leased_at=NULL, lease_expires_at=NULL "
            "WHERE status='leased' AND lease_expires_at < strftime('%Y-%m-%dT%H:%M:%fZ','now')"
        )
        return cur.rowcount

    try:
        n = c.write_tx(do)
    except SelvedgeError as e:
        print(e, file=sys.stderr)
        return 3
    finally:
        c.close()
    print(json.dumps({"reclaimed_leases": n}))
    return 0


# ---------------------------------------------------------------------------
# query (read-only)
# ---------------------------------------------------------------------------


def cmd_query(args) -> int:
    conn = sqlite3.connect(str(db_path()))
    conn.row_factory = sqlite3.Row
    rows = conn.execute(args.sql).fetchall()
    print(json.dumps([dict(r) for r in rows], indent=2 if args.pretty else None, default=str))
    conn.close()
    return 0


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="selvedge", description="Selvedge substrate CLI (engine-v17)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init", help="Initialise a fresh substrate (apply 001 + any later migrations).")
    p_init.add_argument("--force", action="store_true", help="Overwrite existing substrate.")
    p_init.set_defaults(fn=cmd_init)

    p_mig = sub.add_parser("migrate", help="Apply pending migrations against an existing substrate.")
    mode = p_mig.add_mutually_exclusive_group(required=True)
    mode.add_argument("--status", action="store_true", help="List applied + pending migrations.")
    mode.add_argument("--dry-run", action="store_true", help="Parse migrations + T-15 check, no writes.")
    mode.add_argument("--apply", dest="apply_", action="store_true", help="Apply pending migrations in lex order.")
    p_mig.set_defaults(fn=cmd_migrate)

    p_idalloc = sub.add_parser("id-allocate", help="Allocate an objects row.")
    p_idalloc.add_argument("--kind", required=True)
    p_idalloc.add_argument("--typed-row-id", type=int, required=True)
    p_idalloc.add_argument("--alias", default=None)
    p_idalloc.set_defaults(fn=cmd_id_allocate)

    p_submit = sub.add_parser("submit", help="Write a row to the substrate.")
    p_submit.add_argument("kind", help=f"one of: {sorted(SUBMIT_HANDLERS)}")
    p_submit.add_argument("--payload", required=True, help="JSON payload, '@file', or '-' for stdin.")
    p_submit.add_argument("--role", default="__cli__")
    p_submit.set_defaults(fn=cmd_submit)

    p_validate = sub.add_parser("validate", help="Validate substrate integrity.")
    p_validate.add_argument("--precommit", action="store_true")
    p_validate.set_defaults(fn=cmd_validate)

    p_elig = sub.add_parser("subtract-eligibility", help="Eligibility report for human reviewer-subtractor.")
    p_elig.add_argument("--uncited-threshold", type=int, default=10)
    p_elig.add_argument("--stale-threshold", type=int, default=5)
    p_elig.add_argument("--untriaged-threshold", type=int, default=3)
    p_elig.set_defaults(fn=cmd_subtract_eligibility)

    p_rec = sub.add_parser("recover", help="Reclaim expired work_item leases.")
    p_rec.set_defaults(fn=cmd_recover)

    p_q = sub.add_parser("query", help="Read-only SQL query (debugging).")
    p_q.add_argument("sql")
    p_q.add_argument("--pretty", action="store_true")
    p_q.set_defaults(fn=cmd_query)

    args = parser.parse_args(argv)
    try:
        return args.fn(args)
    except SelvedgeError as e:
        print(json.dumps({"ok": False, "code": e.code, "detail": e.detail}), file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
