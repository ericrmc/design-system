"""Selvedge CLI — single-writer SQLite substrate.

Implements the engine-v20 substrate per 078 D-1/D-3/D-8/D-9 plus S084 Path A.

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
  monitor-external     Read a peer Selvedge workspace (status, next-input) and
                       harvest its engine_feedback rows substrate-direct into
                       THIS substrate (engine-v31, DV-S106-3; engine-v33 / S110
                       D-1 substrate-direct read replaces md-files transport).

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
  E_PEER_BUSY      monitor-external: peer substrate locked or busy after busy_timeout.
  E_PEER_OPEN_FAILED  monitor-external: peer DB open failed for non-busy reason (corrupt, wrong path, perms).
  E_PEER_QUERY_FAILED monitor-external: peer query failed for non-busy reason.
  E_PEER_SCHEMA_UNSUPPORTED monitor-external: peer DB lacks engine_feedback table or workspace_id metadata.

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
import urllib.parse
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

# Issue-alias regex used by orient FR-rot annotation. Matches the three
# alias shapes in current use: OI-NNN, OI-NNN-NNN, OI-S<wno>-<seq>.
FR_ISSUE_CITE_RE = re.compile(r"\bOI-(?:S\d{3}-\d+|\d{3}(?:-\d+)?)\b")


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


# Per S084 D-1 (operator-ratified): a calibrated marker pair admits non-destructive
# CHECK-relaxation table-recreation. The block must be bounded by literal markers
# `-- T-15-CALIBRATED-BEGIN: <reason>` and `-- T-15-CALIBRATED-END`, the reason
# must be present, and the body must contain at most one CREATE...new + INSERT
# SELECT + DROP + RENAME sequence per block. The marker is preserved verbatim
# in the migration; the runner's regex check exempts only what is between the
# markers.
_CALIBRATED_BLOCK_RE = re.compile(
    r"--\s*T-15-CALIBRATED-BEGIN\s*:\s*(?P<reason>[^\n]+)\n(?P<body>.*?)\n\s*--\s*T-15-CALIBRATED-END",
    re.DOTALL,
)

# Statements admitted inside a calibrated block (per S084 reviewer F1: structural
# validation of block contents). Anything else inside a calibrated block is a
# violation. The pattern is anchored to the start of a (possibly indented)
# statement after stripping comments.
_CALIBRATED_ALLOWED_STMT_RE = re.compile(
    r"^\s*(CREATE\s+TABLE|INSERT\s+INTO|DROP\s+TABLE|ALTER\s+TABLE\s+\S+\s+RENAME\s+TO|"
    r"CREATE\s+(UNIQUE\s+)?INDEX|CREATE\s+TRIGGER)\b",
    re.IGNORECASE,
)


def _validate_calibrated_block(body: str) -> list[str]:
    """Return a list of violations: statements inside a calibrated block that are
    not the admitted recreation primitives. Comments are stripped first."""
    cleaned = _strip_sql_comments(body)
    violations: list[str] = []
    # SQLite statements end at ";" outside string literals; for migration files
    # we accept naive split because none of our DDL embeds semicolons in strings.
    for raw in cleaned.split(";"):
        stmt = raw.strip()
        if not stmt:
            continue
        if not _CALIBRATED_ALLOWED_STMT_RE.match(stmt):
            # Truncate to ~80 chars for the violation message.
            snippet = " ".join(stmt.split())[:80]
            violations.append(f"non-recreation statement in calibrated block: {snippet}")
    return violations


def _strip_calibrated_blocks(sql: str) -> tuple[str, list[str], list[str]]:
    """Remove calibrated blocks from sql; return (stripped_sql, reasons, violations).

    Per S084 D-2 (operator-ratified) the calibrated marker pair admits ONLY a
    non-destructive table-recreation block (CREATE TABLE x_new + INSERT SELECT
    + DROP TABLE x + ALTER TABLE x_new RENAME TO x, plus admitted index/trigger
    creations). Other statements inside the block are violations and are
    surfaced via the violations list.
    """
    reasons: list[str] = []
    violations: list[str] = []

    def _take(m: re.Match) -> str:
        reasons.append(m.group("reason").strip())
        violations.extend(_validate_calibrated_block(m.group("body")))
        return " "

    return _CALIBRATED_BLOCK_RE.sub(_take, sql), reasons, violations


def _t15_violations(sql: str) -> list[str]:
    # Strip calibrated blocks BEFORE comments so block markers (themselves --
    # comments) survive long enough to be detected. Surface block-content
    # violations alongside ordinary T-15 violations.
    sql_minus_calibrated, _reasons, block_violations = _strip_calibrated_blocks(sql)
    cleaned = _strip_sql_comments(sql_minus_calibrated)
    found: list[str] = list(block_violations)
    for pat, label in T15_FORBIDDEN_PATTERNS:
        if pat.search(cleaned):
            found.append(label)
    return found


def _calibrated_reasons(sql: str) -> list[str]:
    _stripped, reasons, _violations = _strip_calibrated_blocks(sql)
    return reasons


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
                cur = conn.execute(
                    "UPDATE schema_migrations SET sha256 = ? WHERE name = ?",
                    (sha, name),
                )
                if cur.rowcount != 1:
                    raise RuntimeError(
                        f"schema_migrations row absent for {name} after apply; "
                        f"migration SQL must include "
                        f"INSERT INTO schema_migrations (name, sha256) VALUES (?, 'COMPUTED-AT-APPLY-TIME')"
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
            "INSERT INTO objects (object_kind, typed_row_id, alias) VALUES (?,?,?)",
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
        "SELECT object_id FROM objects WHERE alias = ?",
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


def _meta(conn: sqlite3.Connection, key: str, default: Optional[str] = None) -> Optional[str]:
    row = conn.execute("SELECT value FROM workspace_metadata WHERE key=?", (key,)).fetchone()
    if row is None:
        return default
    return row["value"]


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
    engine_version_at_close. An override may still be passed if a session
    actually closed under a different engine version (rare).
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
        raise SelvedgeError("E_VALIDATION", "engine_version_at_close not provided and workspace_metadata.current_engine_version missing")
    conn.execute(
        "UPDATE sessions SET status='closed', engine_version_at_close=?, "
        "closed_at=strftime('%Y-%m-%dT%H:%M:%fZ','now') WHERE session_id=?",
        (eng_ver, sid),
    )
    return {"session_id": sid, "engine_version_at_close": eng_ver}


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
        "INSERT INTO objects (object_kind, typed_row_id, alias) VALUES ('decision', ?, ?)",
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
        "INSERT INTO objects (object_kind, typed_row_id, alias) VALUES ('deliberation', ?, NULL)",
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
        "INSERT INTO objects (object_kind, typed_row_id, alias) VALUES ('perspective', ?, ?)",
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
        "INSERT INTO objects (object_kind, typed_row_id, alias) VALUES ('synthesis_point', ?, NULL)",
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
    real_path = workspace_root() / body_path
    # Path-traversal guard (applies to both authoring branches): refuse a
    # body_path that escapes workspace_root. Path.resolve(strict=False)
    # collapses '..' segments without requiring the file to exist.
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
        # Encode once, write bytes-for-bytes — avoids any newline translation
        # the platform open()-text-mode might otherwise introduce.
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
        # T-04 application-layer: hash the file and refuse on mismatch.
        if not real_path.exists():
            raise SelvedgeError("E_REFUSAL_T04", f"spec body not found at {body_path}")
        real_sha = hashlib.sha256(real_path.read_bytes()).hexdigest()
        if real_sha != body_sha256:
            raise SelvedgeError("E_REFUSAL_T04", f"body_sha256 mismatch: declared {body_sha256[:8]}…, file is {real_sha[:8]}…")

    # OI-S090-4: flip prev active to superseded BEFORE inserting the new active row.
    # T-03 (unique index t03_spec_versions_one_active) refuses two simultaneously-active
    # rows for the same spec_id. The previous order (insert-then-flip) tripped on every
    # supersession in S087/S088/S089.
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
    cur2 = conn.execute(
        "INSERT INTO objects (object_kind, typed_row_id, alias) VALUES ('spec_version', ?, ?)",
        (svid, alias),
    )
    oid = cur2.lastrowid
    conn.execute("UPDATE spec_versions SET object_id=? WHERE spec_version_id=?", (oid, svid))

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
    # the metadata had drifted four versions behind. The handler now updates
    # atomically inside the same transaction as the insert. Migration 011
    # seeded the __cli__ UPDATE capability on workspace_metadata.
    if p["spec_id"] == "engine-manifest":
        _check_role_capability(conn, role, "workspace_metadata", "update")
        upd = conn.execute(
            "UPDATE workspace_metadata SET value = ? WHERE key = 'current_engine_version'",
            (f"engine-v{p['version']}",),
        )
        # Assert the invariant migration 007 is supposed to maintain. If the
        # row is absent the UPDATE silently affects 0 rows, which would
        # reproduce the exact silent-drift bug this handler change was written
        # to prevent.
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


# ---------------------------------------------------------------------------
# Path A handlers (engine-v20+): atom + typed-link writers. Per S084 D-1,
# new sessions write via these kinds; the legacy `decision` / `perspective`
# kinds remain admitted for read/replay-test only.
# ---------------------------------------------------------------------------


def _current_session(conn: sqlite3.Connection) -> sqlite3.Row:
    """Return the unique open session row. Raises if none or multiple are open.

    Engine-v20+: handlers default to the current open session so callers do
    not need to pass session_no. There should normally be exactly one open
    session at a time.
    """
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
    """Resolve session_no -> session_id (or default to the current open session).

    Per S084 reviewer F9: handlers should fail-fast with E_REFUSAL_T06 rather
    than relying on the T-06 trigger to surface a raw constraint violation.

    Per operator at S084 close: if `session_no` is None, default to the
    unique open session so the caller does not need to know the number.
    """
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


def _insert_atom(conn: sqlite3.Connection, role: str, session_id: int, atom_type: str, text: str) -> int:
    _check_role_capability(conn, role, "text_atoms", "insert")
    cur = conn.execute(
        "INSERT INTO text_atoms (atom_type, text, created_session_id) VALUES (?,?,?)",
        (atom_type, text, session_id),
    )
    aid = cur.lastrowid
    cur2 = conn.execute(
        "INSERT INTO objects (object_kind, typed_row_id, alias) VALUES ('text_atom', ?, NULL)",
        (aid,),
    )
    return aid


def _resolve_alias_to_object_id(conn: sqlite3.Connection, alias: str) -> int:
    row = conn.execute("SELECT object_id FROM objects WHERE alias=?", (alias,)).fetchone()
    if row is None:
        raise SelvedgeError("E_REFUSAL_T01", f"unresolved alias [{alias}]")
    return row["object_id"]


def _submit_assessment(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "assessments", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    wno = _session_workspace_no(conn, sess_id)
    state_aid = _insert_atom(conn, role, sess_id, "assessment_item", p["state"])
    cur = conn.execute(
        "INSERT INTO assessments (session_id, state_atom_id) VALUES (?,?)",
        (sess_id, state_aid),
    )
    aid = cur.lastrowid
    alias = f"A-S{wno:03d}"
    cur2 = conn.execute(
        "INSERT INTO objects (object_kind, typed_row_id, alias) VALUES ('assessment', ?, ?)",
        (aid, alias),
    )
    oid = cur2.lastrowid
    conn.execute("UPDATE assessments SET object_id=? WHERE assessment_id=?", (oid, aid))
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


def _submit_decision_v2(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "decisions_v2", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    wno = _session_workspace_no(conn, sess_id)
    next_no = conn.execute(
        "SELECT COALESCE(MAX(decision_no),0)+1 AS n FROM decisions_v2 WHERE session_id=?",
        (sess_id,),
    ).fetchone()["n"]
    title_aid = _insert_atom(conn, role, sess_id, "title", p["title"])
    cur = conn.execute(
        "INSERT INTO decisions_v2 (session_id, decision_no, kind, title_atom_id, outcome_type, target_kind, target_key) "
        "VALUES (?,?,?,?,?,?,?)",
        (sess_id, next_no, p["kind"], title_aid, p["outcome_type"], p["target_kind"], p["target_key"]),
    )
    did = cur.lastrowid
    alias = f"DV-S{wno:03d}-{next_no}"
    cur2 = conn.execute(
        "INSERT INTO objects (object_kind, typed_row_id, alias) VALUES ('decision_v2', ?, ?)",
        (did, alias),
    )
    oid = cur2.lastrowid
    conn.execute("UPDATE decisions_v2 SET object_id=? WHERE decision_v2_id=?", (oid, did))

    # supports
    _check_role_capability(conn, role, "decision_supports", "insert")
    for seq, s in enumerate(p.get("supports", []), start=1):
        claim_aid = _insert_atom(conn, role, sess_id, "support_claim", s["claim"])
        cited_oid = _resolve_alias_to_object_id(conn, s["cite"]) if s.get("cite") else None
        conn.execute(
            "INSERT INTO decision_supports (decision_v2_id, seq, basis, claim_atom_id, cited_object_id) "
            "VALUES (?,?,?,?,?)",
            (did, seq, s["basis"], claim_aid, cited_oid),
        )

    # effects
    _check_role_capability(conn, role, "decision_effects", "insert")
    for e in p.get("effects", []):
        target_oid: Optional[int] = None
        target_iid: Optional[int] = None
        if e["effect_kind"] == "closes_issue":
            # DV-S098-1 / engine-v28: closes_issue dispatches the issue
            # disposition before the decision_effects row is inserted, so
            # t28_closes_issue_target_resolved sees status='resolved' and
            # passes. Identity is conveyed via target (issue alias) → target_issue_id.
            if not e.get("target"):
                raise SelvedgeError(
                    "E_VALIDATION",
                    "closes_issue effect requires target naming the issue alias (e.g. OI-016)",
                )
            descriptor = e.get("target_descriptor")
            if not descriptor:
                raise SelvedgeError(
                    "E_VALIDATION",
                    "closes_issue effect requires target_descriptor as the closure reason (becomes the disposition reason atom)",
                )
            if not (8 <= len(descriptor) <= 120):
                # decision_effects.target_descriptor CHECK is 2-120; reason_atom CHECK is 8-240.
                # The intersection (8-120) is the operative range; fail fast with a clearer message
                # than the column-level CHECK violation.
                raise SelvedgeError(
                    "E_VALIDATION",
                    "closes_issue target_descriptor must be 8-120 characters (becomes the disposition reason atom)",
                )
            target_iid = _resolve_issue_alias(conn, e["target"])
            cur_status = conn.execute(
                "SELECT status FROM issues WHERE issue_id=?", (target_iid,)
            ).fetchone()
            if cur_status["status"] not in ("resolved", "superseded"):
                _submit_issue_disposition(
                    conn,
                    {
                        "alias": e["target"],
                        "to_status": "resolved",
                        "reason": descriptor,
                        "session_no": p.get("session_no"),
                    },
                    role,
                )
        elif e.get("target"):
            target_oid = _resolve_alias_to_object_id(conn, e["target"])
        conn.execute(
            "INSERT INTO decision_effects (decision_v2_id, effect_kind, target_object_id, target_issue_id, target_descriptor) "
            "VALUES (?,?,?,?,?)",
            (did, e["effect_kind"], target_oid, target_iid, e.get("target_descriptor")),
        )

    # alternatives + rejections
    _check_role_capability(conn, role, "alternatives_v2", "insert")
    _check_role_capability(conn, role, "alternative_rejections", "insert")
    alts_out = []
    for a in p.get("alternatives", []):
        opt_aid = _insert_atom(conn, role, sess_id, "alternative_option", a["option"])
        cur3 = conn.execute(
            "INSERT INTO alternatives_v2 (decision_v2_id, label, option_atom_id) VALUES (?,?,?)",
            (did, a["label"], opt_aid),
        )
        avid = cur3.lastrowid
        alt_alias = f"{alias}-{a['label']}"
        cur4 = conn.execute(
            "INSERT INTO objects (object_kind, typed_row_id, alias) VALUES ('alternative_v2', ?, ?)",
            (avid, alt_alias),
        )
        a_oid = cur4.lastrowid
        conn.execute("UPDATE alternatives_v2 SET object_id=? WHERE alternative_v2_id=?", (a_oid, avid))
        for seq, r in enumerate(a.get("rejections", []), start=1):
            rej_aid = _insert_atom(conn, role, sess_id, "rejection_reason", r["reason"])
            cited_oid = _resolve_alias_to_object_id(conn, r["cite"]) if r.get("cite") else None
            conn.execute(
                "INSERT INTO alternative_rejections (alternative_v2_id, seq, basis, rejection_atom_id, cited_object_id) "
                "VALUES (?,?,?,?,?)",
                (avid, seq, r["basis"], rej_aid, cited_oid),
            )
        alts_out.append({"alternative_v2_id": avid, "alias": alt_alias})

    return {"decision_v2_id": did, "object_id": oid, "alias": alias, "decision_no": next_no, "alternatives": alts_out}


def _submit_perspective_position(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "perspective_positions", "insert")
    delib = conn.execute(
        "SELECT d.session_id FROM perspectives pe JOIN deliberations d ON d.deliberation_id = pe.deliberation_id "
        "WHERE pe.perspective_id=?",
        (p["perspective_id"],),
    ).fetchone()
    if delib is None:
        raise SelvedgeError("E_NOT_FOUND", f"perspective_id={p['perspective_id']}")
    sess_id = delib["session_id"]
    pos_aid = _insert_atom(conn, role, sess_id, "perspective_position", p["position"])
    cur = conn.execute(
        "INSERT INTO perspective_positions (perspective_id, position_atom_id) VALUES (?,?)",
        (p["perspective_id"], pos_aid),
    )
    pid = cur.lastrowid
    cur2 = conn.execute(
        "INSERT INTO objects (object_kind, typed_row_id, alias) VALUES ('perspective_position', ?, NULL)",
        (pid,),
    )
    oid = cur2.lastrowid
    conn.execute("UPDATE perspective_positions SET object_id=? WHERE position_id=?", (oid, pid))
    return {"position_id": pid, "object_id": oid}


def _submit_perspective_claim(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "perspective_claims", "insert")
    delib = conn.execute(
        "SELECT d.session_id FROM perspectives pe JOIN deliberations d ON d.deliberation_id = pe.deliberation_id "
        "WHERE pe.perspective_id=?",
        (p["perspective_id"],),
    ).fetchone()
    if delib is None:
        raise SelvedgeError("E_NOT_FOUND", f"perspective_id={p['perspective_id']}")
    sess_id = delib["session_id"]
    next_seq = conn.execute(
        "SELECT COALESCE(MAX(seq),0)+1 AS n FROM perspective_claims WHERE perspective_id=?",
        (p["perspective_id"],),
    ).fetchone()["n"]
    claim_aid = _insert_atom(conn, role, sess_id, "perspective_claim", p["claim"])
    cited_oid = _resolve_alias_to_object_id(conn, p["cite"]) if p.get("cite") else None
    cur = conn.execute(
        "INSERT INTO perspective_claims (perspective_id, seq, section_kind, claim_atom_id, cited_object_id) "
        "VALUES (?,?,?,?,?)",
        (p["perspective_id"], next_seq, p["section_kind"], claim_aid, cited_oid),
    )
    pcid = cur.lastrowid
    cur2 = conn.execute(
        "INSERT INTO objects (object_kind, typed_row_id, alias) VALUES ('perspective_claim', ?, NULL)",
        (pcid,),
    )
    oid = cur2.lastrowid
    conn.execute("UPDATE perspective_claims SET object_id=? WHERE claim_id=?", (oid, pcid))
    return {"claim_id": pcid, "seq": next_seq, "object_id": oid}


def _submit_review_finding(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "review_findings", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    wno = _session_workspace_no(conn, sess_id)
    finding_aid = _insert_atom(conn, role, sess_id, "finding", p["finding"])
    target_oid = _resolve_alias_to_object_id(conn, p["target"]) if p.get("target") else None
    disp_aid = None
    if p.get("disposition_text"):
        disp_aid = _insert_atom(conn, role, sess_id, "finding", p["disposition_text"])
    cur = conn.execute(
        "INSERT INTO review_findings (session_id, iteration, severity, finding_atom_id, target_object_id, disposition, disposition_atom_id) "
        "VALUES (?,?,?,?,?,?,?)",
        (sess_id, p["iteration"], p["severity"], finding_aid, target_oid, p.get("disposition", "open"), disp_aid),
    )
    rfid = cur.lastrowid
    cur2 = conn.execute(
        "INSERT INTO objects (object_kind, typed_row_id, alias) VALUES ('review_finding', ?, ?)",
        (rfid, f"RF-S{wno:03d}-{p['iteration']}-{rfid}"),
    )
    oid = cur2.lastrowid
    conn.execute("UPDATE review_findings SET object_id=? WHERE review_finding_id=?", (oid, rfid))
    return {"review_finding_id": rfid, "object_id": oid}


def _submit_review_pass(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    """Record a terminal review-pass row (engine-v31, S104 D-2/D-4).

    Required: iteration (1-4), outcome ('clean' | 'findings' | 'nonconverged'),
    head_sha (operator-asserted; substrate format-checks but cannot verify
    truth), summary (one-line atom).

    For outcome='nonconverged' the caller must also pass halt_issue_alias
    (resolved to issue_id), per t_review_pass_nonconverged_requires_halt_issue.

    The close-gate (t30) inspects the LATEST iteration's outcome per session;
    submit successive iterations as the loop runs (1, 2, 3, 4 max).
    """
    _check_role_capability(conn, role, "review_passes", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    wno = _session_workspace_no(conn, sess_id)
    iteration = int(p["iteration"])
    if not (1 <= iteration <= 4):
        raise SelvedgeError(
            "E_VALIDATION",
            f"review-pass iteration must be 1-4 (the methodology halts the loop at iter 4); got {iteration}",
        )
    outcome = p["outcome"]
    if outcome not in ("clean", "findings", "nonconverged"):
        raise SelvedgeError(
            "E_VALIDATION",
            f"review-pass outcome must be one of clean, findings, nonconverged; got {outcome!r}",
        )
    head_sha = p.get("head_sha", "").strip()
    if not (7 <= len(head_sha) <= 64):
        raise SelvedgeError(
            "E_VALIDATION",
            "review-pass head_sha must be 7-64 chars (typically the abbreviated or full git HEAD sha at the moment the reviewer ran)",
        )
    if not all(c in "0123456789abcdefABCDEF" for c in head_sha):
        raise SelvedgeError(
            "E_VALIDATION",
            f"review-pass head_sha must be hex characters; got {head_sha!r}",
        )
    if outcome == "nonconverged" and not p.get("halt_issue_alias"):
        raise SelvedgeError(
            "E_VALIDATION",
            "review-pass outcome=nonconverged requires halt_issue_alias (the OI-... issue tracking the unresolved findings per methodology halt-state)",
        )
    summary_aid = _insert_atom(conn, role, sess_id, "finding", p["summary"])
    halt_issue_id = None
    if p.get("halt_issue_alias"):
        halt_issue_id = _resolve_issue_alias(conn, p["halt_issue_alias"])
    cur = conn.execute(
        "INSERT INTO review_passes (session_id, iteration, outcome, head_sha, summary_atom_id, halt_issue_id) "
        "VALUES (?,?,?,?,?,?)",
        (sess_id, iteration, outcome, head_sha, summary_aid, halt_issue_id),
    )
    rpid = cur.lastrowid
    return {
        "review_pass_id": rpid,
        "session_workspace_no": wno,
        "iteration": iteration,
        "outcome": outcome,
    }


def _submit_finding_disposition(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "review_findings", "update")
    rf = conn.execute(
        "SELECT session_id FROM review_findings WHERE review_finding_id=?",
        (p["review_finding_id"],),
    ).fetchone()
    if rf is None:
        raise SelvedgeError("E_NOT_FOUND", f"review_finding_id={p['review_finding_id']}")
    disp_aid = _insert_atom(conn, role, rf["session_id"], "finding", p["disposition_text"])
    conn.execute(
        "UPDATE review_findings SET disposition=?, disposition_atom_id=? WHERE review_finding_id=?",
        (p["disposition"], disp_aid, p["review_finding_id"]),
    )
    return {"review_finding_id": p["review_finding_id"], "disposition": p["disposition"]}


def _submit_close_record(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "close_records", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    wno = _session_workspace_no(conn, sess_id)
    summary_aid = _insert_atom(conn, role, sess_id, "close_summary", p["summary"])
    cur = conn.execute(
        "INSERT INTO close_records (session_id, summary_atom_id) VALUES (?,?)",
        (sess_id, summary_aid),
    )
    crid = cur.lastrowid
    alias = f"C-S{wno:03d}"
    cur2 = conn.execute(
        "INSERT INTO objects (object_kind, typed_row_id, alias) VALUES ('close_record', ?, ?)",
        (crid, alias),
    )
    oid = cur2.lastrowid
    conn.execute("UPDATE close_records SET object_id=? WHERE close_record_id=?", (oid, crid))
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
    cur2 = conn.execute(
        "INSERT INTO objects (object_kind, typed_row_id, alias) VALUES ('spec_section', ?, NULL)",
        (ssid,),
    )
    oid = cur2.lastrowid
    conn.execute("UPDATE spec_sections SET object_id=? WHERE spec_section_id=?", (oid, ssid))
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
    cur2 = conn.execute(
        "INSERT INTO objects (object_kind, typed_row_id, alias) VALUES ('spec_clause', ?, NULL)",
        (scid,),
    )
    oid2 = cur2.lastrowid
    conn.execute("UPDATE spec_clauses SET object_id=? WHERE spec_clause_id=?", (oid2, scid))
    return {"spec_clause_id": scid, "object_id": oid2}


def _resolve_issue_alias(conn: sqlite3.Connection, alias: str) -> int:
    row = conn.execute(
        "SELECT issue_id FROM issues WHERE alias=?", (alias,)
    ).fetchone()
    if row is None:
        raise SelvedgeError("E_NOT_FOUND", f"issue alias [{alias}] not registered")
    return row["issue_id"]


def _submit_issue(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "issues", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    surfaced_id = _atom_session_id(conn, p.get("surfaced_session_no"), require_open=False) \
        if p.get("surfaced_session_no") is not None else sess_id
    if p.get("status") not in (None, "open"):
        raise SelvedgeError(
            "E_VALIDATION",
            "issue must be created with status='open'; transitions to other statuses go through submit issue-disposition",
        )
    title_aid = _insert_atom(conn, role, sess_id, "title", p["title"])
    summary_aid = None
    if p.get("summary"):
        summary_aid = _insert_atom(conn, role, sess_id, "claim", p["summary"])
    body_aid = None
    if p.get("body"):
        body_aid = _insert_atom(conn, role, sess_id, "legacy_import", p["body"])
    cur = conn.execute(
        "INSERT INTO issues (alias, surfaced_session_id, title_atom_id, summary_atom_id, body_atom_id, priority, status) "
        "VALUES (?,?,?,?,?,?, 'open')",
        (
            p["alias"],
            surfaced_id,
            title_aid,
            summary_aid,
            body_aid,
            p["priority"],
        ),
    )
    iid = cur.lastrowid
    return {"issue_id": iid, "alias": p["alias"]}


def _submit_issue_disposition(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "issue_dispositions", "insert")
    _check_role_capability(conn, role, "issues", "update")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    if "issue_id" in p:
        iid = int(p["issue_id"])
    else:
        iid = _resolve_issue_alias(conn, p["alias"])
    cur_row = conn.execute(
        "SELECT status FROM issues WHERE issue_id=?", (iid,)
    ).fetchone()
    if cur_row is None:
        raise SelvedgeError("E_NOT_FOUND", f"issue_id={iid}")
    from_status = cur_row["status"]
    to_status = p["to_status"]
    if from_status == to_status:
        raise SelvedgeError("E_VALIDATION", f"to_status equals from_status ({from_status}); no-op refused")
    reason_aid = _insert_atom(conn, role, sess_id, "rejection_reason", p["reason"])
    next_seq = conn.execute(
        "SELECT COALESCE(MAX(seq),0)+1 AS n FROM issue_dispositions WHERE issue_id=?", (iid,)
    ).fetchone()["n"]
    cur = conn.execute(
        "INSERT INTO issue_dispositions (issue_id, seq, from_status, to_status, reason_atom_id, session_id) "
        "VALUES (?,?,?,?,?,?)",
        (iid, next_seq, from_status, to_status, reason_aid, sess_id),
    )
    did = cur.lastrowid
    if to_status in ("resolved", "superseded"):
        conn.execute(
            "UPDATE issues SET status=?, resolved_session_id=?, resolved_at=strftime('%Y-%m-%dT%H:%M:%fZ','now') "
            "WHERE issue_id=?",
            (to_status, sess_id, iid),
        )
    else:
        conn.execute(
            "UPDATE issues SET status=?, resolved_session_id=NULL, resolved_at=NULL WHERE issue_id=?",
            (to_status, iid),
        )
    return {"disposition_id": did, "issue_id": iid, "from_status": from_status, "to_status": to_status}


def _submit_issue_link(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "issue_links", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    src = int(p["source_issue_id"]) if "source_issue_id" in p else _resolve_issue_alias(conn, p["source_alias"])
    tgt = int(p["target_issue_id"]) if "target_issue_id" in p else _resolve_issue_alias(conn, p["target_alias"])
    reason_aid = None
    if p.get("reason"):
        reason_aid = _insert_atom(conn, role, sess_id, "rejection_reason", p["reason"])
    cur = conn.execute(
        "INSERT INTO issue_links (source_issue_id, target_issue_id, relation, reason_atom_id, session_id) "
        "VALUES (?,?,?,?,?)",
        (src, tgt, p["relation"], reason_aid, sess_id),
    )
    return {"link_id": cur.lastrowid, "source_issue_id": src, "target_issue_id": tgt, "relation": p["relation"]}


def _submit_issue_note(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "issue_notes", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    iid = int(p["issue_id"]) if "issue_id" in p else _resolve_issue_alias(conn, p["alias"])
    note_aid = _insert_atom(conn, role, sess_id, "claim", p["note"])
    next_seq = conn.execute(
        "SELECT COALESCE(MAX(seq),0)+1 AS n FROM issue_notes WHERE issue_id=?", (iid,)
    ).fetchone()["n"]
    cur = conn.execute(
        "INSERT INTO issue_notes (issue_id, seq, note_atom_id, session_id) VALUES (?,?,?,?)",
        (iid, next_seq, note_aid, sess_id),
    )
    return {"note_id": cur.lastrowid, "issue_id": iid, "seq": next_seq}


def _submit_engine_feedback_disposition(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    """Update engine_feedback.disposition (engine-v27+, EF-S096-2 remedy).

    Closes the substrate-only-writes loop on engine_feedback that engine-v26
    only half-closed: the insert path landed at S094, but transitioning a
    feedback row's disposition still required raw SQL until this handler.
    """
    _check_role_capability(conn, role, "engine_feedback", "update")
    _atom_session_id(conn, p.get("session_no"))
    if "feedback_id" in p:
        fid = int(p["feedback_id"])
    elif "alias" in p:
        oid = _resolve_alias(conn, p["alias"])
        if oid is None:
            raise SelvedgeError("E_REFUSAL_T01", f"unresolved alias [{p['alias']}]")
        row = conn.execute(
            "SELECT feedback_id FROM engine_feedback WHERE object_id=?", (oid,)
        ).fetchone()
        if row is None:
            raise SelvedgeError("E_NOT_FOUND", f"alias {p['alias']} is not engine_feedback")
        fid = row["feedback_id"]
    else:
        raise SelvedgeError("E_VALIDATION", "engine-feedback-disposition requires feedback_id or alias")
    upd = conn.execute(
        "UPDATE engine_feedback SET disposition=? WHERE feedback_id=?",
        (p["disposition"], fid),
    )
    if upd.rowcount != 1:
        raise SelvedgeError("E_NOT_FOUND", f"feedback_id={fid}")
    return {"feedback_id": fid, "disposition": p["disposition"]}


def _submit_forward_reference_disposition(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    """Mark a close_state_items row with facet='next_session_should' as resolved
    (engine-v27+, EF-S096-1 strong remedy).

    Target identified by (target_session, seq) where target_session is the
    workspace_session_no of the session whose close-record carries the item.
    Rejected by T-26 if the target's facet isn't next_session_should.
    """
    _check_role_capability(conn, role, "forward_reference_dispositions", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    target_wno = int(p["target_session"])
    seq = int(p["seq"])
    row = conn.execute(
        "SELECT csi.state_item_id "
        "FROM close_state_items csi "
        "JOIN close_records cr ON cr.close_record_id=csi.close_record_id "
        "JOIN sessions s ON s.session_id=cr.session_id "
        "WHERE COALESCE(s.workspace_session_no, s.session_no)=? "
        "  AND csi.seq=? AND csi.facet='next_session_should'",
        (target_wno, seq),
    ).fetchone()
    if row is None:
        raise SelvedgeError(
            "E_NOT_FOUND",
            f"forward-reference target_session={target_wno} seq={seq} "
            f"(must be a next_session_should close_state_item)",
        )
    note_aid = None
    if p.get("note"):
        note_aid = _insert_atom(conn, role, sess_id, "claim", p["note"])
    cur = conn.execute(
        "INSERT INTO forward_reference_dispositions (state_item_id, resolved_session_id, note_atom_id) "
        "VALUES (?,?,?)",
        (row["state_item_id"], sess_id, note_aid),
    )
    return {
        "disposition_id": cur.lastrowid,
        "state_item_id": row["state_item_id"],
        "ref": f"FR-S{target_wno:03d}-{seq}",
    }


def _submit_engine_feedback(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    """Insert one engine_feedback row + objects row + refs (engine-v26+).

    Replaces the raw-SQL pattern used for EF-S092-1..4 (which the surfacing
    feedback flagged as a substrate-only-writes violation). Alias is
    `EF-S<wno>-<idx>` where idx is the next ordinal among feedback rows
    surfaced under the same workspace_session_no.
    """
    _check_role_capability(conn, role, "engine_feedback", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    wno = _session_workspace_no(conn, sess_id)
    flag = p["flag"]
    body_md = p["body_md"]
    disposition = p.get("disposition")
    cur = conn.execute(
        "INSERT INTO engine_feedback (session_id, flag, body_md, disposition) VALUES (?,?,?,?)",
        (sess_id, flag, body_md, disposition),
    )
    fid = cur.lastrowid
    idx = conn.execute(
        "SELECT COUNT(*) AS n FROM engine_feedback ef "
        "JOIN sessions s ON s.session_id=ef.session_id "
        "WHERE COALESCE(s.workspace_session_no, s.session_no)=?",
        (wno,),
    ).fetchone()["n"]
    alias = _alias_for_engine_feedback(wno, idx)
    cur2 = conn.execute(
        "INSERT INTO objects (object_kind, typed_row_id, alias) VALUES ('engine_feedback', ?, ?)",
        (fid, alias),
    )
    oid = cur2.lastrowid
    conn.execute("UPDATE engine_feedback SET object_id=? WHERE feedback_id=?", (oid, fid))
    _check_role_capability(conn, role, "refs", "insert")
    n_refs = _record_refs(conn, source_object_id=oid, body_md=body_md)
    return {"feedback_id": fid, "object_id": oid, "alias": alias, "flag": flag, "refs": n_refs}


def _submit_issue_work_item(conn: sqlite3.Connection, p: dict, role: str) -> dict:
    _check_role_capability(conn, role, "issue_work_items", "insert")
    sess_id = _atom_session_id(conn, p.get("session_no"))
    iid = int(p["issue_id"]) if "issue_id" in p else _resolve_issue_alias(conn, p["alias"])
    if "issue_id" in p and conn.execute(
        "SELECT 1 FROM issues WHERE issue_id=?", (iid,)
    ).fetchone() is None:
        raise SelvedgeError("E_NOT_FOUND", f"issue_id={iid}")
    wid = int(p["work_item_id"])
    if conn.execute("SELECT 1 FROM work_items WHERE work_item_id=?", (wid,)).fetchone() is None:
        raise SelvedgeError("E_NOT_FOUND", f"work_item_id={wid}")
    relation = p.get("relation", "resolves")
    cur = conn.execute(
        "INSERT INTO issue_work_items (issue_id, work_item_id, relation, created_session_id) "
        "VALUES (?,?,?,?)",
        (iid, wid, relation, sess_id),
    )
    return {
        "issue_work_item_id": cur.lastrowid,
        "issue_id": iid,
        "work_item_id": wid,
        "relation": relation,
    }


SUBMIT_HANDLERS = {
    "session-open": _submit_session_open,
    "session-close": _submit_session_close,
    "decision": _submit_decision,
    "spec-version": _submit_spec_version,
    "deliberation-open": _submit_deliberation_open,
    "perspective": _submit_perspective,
    "deliberation-seal": _submit_deliberation_seal,
    "synthesis-point": _submit_synthesis_point,
    # Path A (engine-v20+):
    "assessment": _submit_assessment,
    "decision-record": _submit_decision_v2,
    "perspective-position": _submit_perspective_position,
    "perspective-claim": _submit_perspective_claim,
    "review-finding": _submit_review_finding,
    "review-pass": _submit_review_pass,
    "finding-disposition": _submit_finding_disposition,
    "close-record": _submit_close_record,
    "legacy-import": _submit_legacy_import,
    "spec-section": _submit_spec_section,
    "spec-clause": _submit_spec_clause,
    # Issues (engine-v22+):
    "issue": _submit_issue,
    "issue-disposition": _submit_issue_disposition,
    "issue-link": _submit_issue_link,
    "issue-note": _submit_issue_note,
    "issue-work-item": _submit_issue_work_item,
    "engine-feedback": _submit_engine_feedback,
    "engine-feedback-disposition": _submit_engine_feedback_disposition,
    "forward-reference-disposition": _submit_forward_reference_disposition,
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
# export — materialise markdown views from substrate rows (engine-v20+).
# ---------------------------------------------------------------------------


def _atom_text(conn: sqlite3.Connection, atom_id: Optional[int]) -> str:
    if atom_id is None:
        return ""
    row = conn.execute("SELECT text FROM text_atoms WHERE atom_id=?", (atom_id,)).fetchone()
    return row["text"] if row else ""


def _export_session_provenance(conn: sqlite3.Connection, session_ref: int, write: bool = False) -> dict:
    """Export a session by EITHER substrate session_no OR workspace_session_no.

    Looks up the session row via either column; uses workspace_session_no for
    the provenance directory name (e.g. provenance/084-<slug>/) so the file
    layout matches workspace conventions, not substrate counters.
    """
    sess = conn.execute(
        "SELECT session_id, session_no, workspace_session_no, slug, mode, "
        "       engine_version_at_open, engine_version_at_close, "
        "       opened_at, closed_at, status FROM sessions "
        "WHERE workspace_session_no=? OR session_no=? LIMIT 1",
        (session_ref, session_ref),
    ).fetchone()
    if sess is None:
        raise SelvedgeError("E_NOT_FOUND", f"session ref={session_ref} (tried workspace_session_no and session_no)")
    sid = sess["session_id"]
    workspace_no = sess["workspace_session_no"] or sess["session_no"]
    session_no = sess["session_no"]
    out_dir = Path("provenance") / f"{workspace_no:03d}-{sess['slug']}"
    files: dict[str, str] = {}

    # 00-assessment.md
    asm = conn.execute(
        "SELECT assessment_id, state_atom_id FROM assessments WHERE session_id=?",
        (sid,),
    ).fetchone()
    if asm:
        items = conn.execute(
            "SELECT ord, item_atom_id FROM assessment_agenda_items WHERE assessment_id=? ORDER BY ord",
            (asm["assessment_id"],),
        ).fetchall()
        lines = [
            "---",
            f"session: {workspace_no:03d}",
            f"title: {sess['slug']} — assessment",
            f"engine_version_at_open: {sess['engine_version_at_open']}",
            f"mode: {sess['mode']}",
            "generated_by: selvedge export",
            "---",
            "",
            "# Assessment",
            "",
            "## State at open",
            "",
            _atom_text(conn, asm["state_atom_id"]),
            "",
            "## Agenda",
            "",
        ]
        for it in items:
            lines.append(f"{it['ord']}. {_atom_text(conn, it['item_atom_id'])}")
        lines.append("")
        files["00-assessment.md"] = "\n".join(lines)

    # 01-deliberation.md (one section per deliberation in this session)
    delibs = conn.execute(
        "SELECT deliberation_id, topic, sealed_at, synthesis_md FROM deliberations WHERE session_id=? ORDER BY deliberation_id",
        (sid,),
    ).fetchall()
    if delibs:
        lines = [
            "---",
            f"session: {workspace_no:03d}",
            f"title: {sess['slug']} — deliberation",
            "generated_by: selvedge export",
            "---",
            "",
            "# Deliberation",
            "",
        ]
        for d in delibs:
            lines.append(f"## D-{d['deliberation_id']} — {d['topic']}")
            lines.append("")
            lines.append(f"sealed_at: {d['sealed_at']}")
            lines.append("")
            persp = conn.execute(
                "SELECT perspective_id, label, family FROM perspectives WHERE deliberation_id=? ORDER BY perspective_id",
                (d["deliberation_id"],),
            ).fetchall()
            for pe in persp:
                lines.append(f"### {pe['label']} ({pe['family']})")
                lines.append("")
                pos = conn.execute(
                    "SELECT position_atom_id FROM perspective_positions WHERE perspective_id=?",
                    (pe["perspective_id"],),
                ).fetchone()
                if pos:
                    lines.append(f"**Position.** {_atom_text(conn, pos['position_atom_id'])}")
                    lines.append("")
                claims = conn.execute(
                    "SELECT seq, section_kind, claim_atom_id FROM perspective_claims WHERE perspective_id=? ORDER BY seq",
                    (pe["perspective_id"],),
                ).fetchall()
                if claims:
                    cur_section = None
                    for c in claims:
                        if c["section_kind"] != cur_section:
                            cur_section = c["section_kind"]
                            lines.append(f"**{cur_section}.**")
                        lines.append(f"- {_atom_text(conn, c['claim_atom_id'])}")
                    lines.append("")
            if d["synthesis_md"]:
                lines.append("### Synthesis")
                lines.append("")
                lines.append(d["synthesis_md"])
                lines.append("")
            sps = conn.execute(
                "SELECT kind, label, summary FROM synthesis_points WHERE deliberation_id=? ORDER BY synthesis_point_id",
                (d["deliberation_id"],),
            ).fetchall()
            if sps:
                lines.append("### Synthesis points")
                lines.append("")
                for sp in sps:
                    lines.append(f"- **{sp['kind']} {sp['label']}.** {sp['summary']}")
                lines.append("")
        files["01-deliberation.md"] = "\n".join(lines)

    # 02-decisions.md (decisions_v2 first, then legacy decisions for backwards-readability)
    dvs = conn.execute(
        "SELECT decision_v2_id, decision_no, kind, title_atom_id, outcome_type, target_kind, target_key "
        "FROM decisions_v2 WHERE session_id=? ORDER BY decision_no",
        (sid,),
    ).fetchall()
    legacy_ds = conn.execute(
        "SELECT decision_no, kind, title, body_md FROM decisions WHERE session_id=? ORDER BY decision_no",
        (sid,),
    ).fetchall()
    if dvs or legacy_ds:
        lines = [
            "---",
            f"session: {workspace_no:03d}",
            f"title: {sess['slug']} — decisions",
            "generated_by: selvedge export",
            "---",
            "",
            "# Decisions",
            "",
        ]
        for d in dvs:
            lines.append(f"## D-{d['decision_no']}. {_atom_text(conn, d['title_atom_id'])}")
            lines.append("")
            lines.append(f"**Kind:** {d['kind']}.  **Outcome:** {d['outcome_type']} {d['target_kind']} `{d['target_key']}`.")
            lines.append("")
            sups = conn.execute(
                "SELECT seq, basis, claim_atom_id, cited_object_id FROM decision_supports WHERE decision_v2_id=? ORDER BY seq",
                (d["decision_v2_id"],),
            ).fetchall()
            if sups:
                lines.append("**Why.**")
                lines.append("")
                for s in sups:
                    cite = ""
                    if s["cited_object_id"]:
                        c = conn.execute("SELECT alias FROM objects WHERE object_id=?", (s["cited_object_id"],)).fetchone()
                        if c and c["alias"]:
                            cite = f" [{c['alias']}]"
                    lines.append(f"- ({s['basis']}) {_atom_text(conn, s['claim_atom_id'])}{cite}")
                lines.append("")
            effs = conn.execute(
                "SELECT effect_kind, target_object_id, target_issue_id, target_descriptor FROM decision_effects WHERE decision_v2_id=? "
                "ORDER BY effect_id",
                (d["decision_v2_id"],),
            ).fetchall()
            if effs:
                lines.append("**Effects.**")
                lines.append("")
                for e in effs:
                    descriptor = e["target_descriptor"] or ""
                    alias = ""
                    if e["target_object_id"]:
                        c = conn.execute("SELECT alias FROM objects WHERE object_id=?", (e["target_object_id"],)).fetchone()
                        if c and c["alias"]:
                            alias = c["alias"]
                    elif e["target_issue_id"]:
                        c = conn.execute("SELECT alias FROM issues WHERE issue_id=?", (e["target_issue_id"],)).fetchone()
                        if c and c["alias"]:
                            alias = c["alias"]
                    if alias and descriptor:
                        lines.append(f"- {e['effect_kind']} {alias} — {descriptor}")
                    elif alias:
                        lines.append(f"- {e['effect_kind']} {alias}")
                    else:
                        lines.append(f"- {e['effect_kind']} {descriptor}")
                lines.append("")
            alts = conn.execute(
                "SELECT alternative_v2_id, label, option_atom_id FROM alternatives_v2 WHERE decision_v2_id=? ORDER BY alternative_v2_id",
                (d["decision_v2_id"],),
            ).fetchall()
            if alts:
                lines.append("**Rejected alternatives.**")
                lines.append("")
                for a in alts:
                    lines.append(f"- **{a['label']}.** {_atom_text(conn, a['option_atom_id'])}")
                    rejs = conn.execute(
                        "SELECT seq, basis, rejection_atom_id FROM alternative_rejections WHERE alternative_v2_id=? ORDER BY seq",
                        (a["alternative_v2_id"],),
                    ).fetchall()
                    for r in rejs:
                        lines.append(f"  - ({r['basis']}) {_atom_text(conn, r['rejection_atom_id'])}")
                lines.append("")
        if legacy_ds:
            lines.append("## Legacy decisions (pre-v20)")
            lines.append("")
            for d in legacy_ds:
                lines.append(f"### D-{d['decision_no']}. {d['title']}")
                lines.append("")
                lines.append(d["body_md"])
                lines.append("")
        files["02-decisions.md"] = "\n".join(lines)

    # 04-review.md
    rfs = conn.execute(
        "SELECT iteration, severity, finding_atom_id, target_object_id, disposition, disposition_atom_id "
        "FROM review_findings WHERE session_id=? ORDER BY iteration, review_finding_id",
        (sid,),
    ).fetchall()
    rps = conn.execute(
        "SELECT iteration, outcome, head_sha, summary_atom_id, halt_issue_id "
        "FROM review_passes WHERE session_id=? ORDER BY iteration",
        (sid,),
    ).fetchall()
    if rfs or rps:
        lines = [
            "---",
            f"session: {workspace_no:03d}",
            f"title: {sess['slug']} — review",
            "generated_by: selvedge export",
            "---",
            "",
            "# Reviewer audit",
            "",
        ]
        cur_iter = None
        for rf in rfs:
            if rf["iteration"] != cur_iter:
                cur_iter = rf["iteration"]
                lines.append(f"## Iteration {cur_iter}")
                lines.append("")
            cite = ""
            if rf["target_object_id"]:
                c = conn.execute("SELECT alias FROM objects WHERE object_id=?", (rf["target_object_id"],)).fetchone()
                if c and c["alias"]:
                    cite = f" against `{c['alias']}`"
            lines.append(f"- **{rf['severity']}**{cite}: {_atom_text(conn, rf['finding_atom_id'])}")
            disp_text = _atom_text(conn, rf["disposition_atom_id"]) if rf["disposition_atom_id"] is not None else "(no disposition recorded)"
            lines.append(f"  - **{rf['disposition']}.** {disp_text}")
        if rps:
            lines.append("")
            lines.append("## Terminal passes")
            lines.append("")
            for rp in rps:
                halt = ""
                if rp["halt_issue_id"]:
                    h = conn.execute("SELECT alias FROM issues WHERE issue_id=?", (rp["halt_issue_id"],)).fetchone()
                    if h and h["alias"]:
                        halt = f" (halt issue `{h['alias']}`)"
                lines.append(f"- **iteration {rp['iteration']}** — {rp['outcome']}{halt} @ `{rp['head_sha'][:12]}`")
                lines.append(f"  - {_atom_text(conn, rp['summary_atom_id'])}")
        lines.append("")
        files["04-review.md"] = "\n".join(lines)

    # 03-close.md
    cr = conn.execute(
        "SELECT close_record_id, summary_atom_id FROM close_records WHERE session_id=?",
        (sid,),
    ).fetchone()
    if cr:
        items = conn.execute(
            "SELECT seq, facet, item_atom_id FROM close_state_items WHERE close_record_id=? ORDER BY seq",
            (cr["close_record_id"],),
        ).fetchall()
        lines = [
            "---",
            f"session: {workspace_no:03d}",
            f"title: {sess['slug']} — close",
            f"engine_version_at_close: {sess['engine_version_at_close']}",
            f"mode: {sess['mode']}",
            "generated_by: selvedge export",
            "---",
            "",
            "# Close",
            "",
            "## Summary",
            "",
            _atom_text(conn, cr["summary_atom_id"]),
            "",
        ]
        cur_facet = None
        facet_titles = {
            "what_was_done": "What was done",
            "state_at_close": "State at close",
            "open_issues": "Open issues",
            "next_session_should": "What the next session should address",
            "engine_version": "Engine version",
            "validator_summary": "Validator at close",
        }
        for it in items:
            if it["facet"] != cur_facet:
                cur_facet = it["facet"]
                lines.append(f"## {facet_titles.get(cur_facet, cur_facet)}")
                lines.append("")
            lines.append(f"- {_atom_text(conn, it['item_atom_id'])}")
        lines.append("")
        files["03-close.md"] = "\n".join(lines)

    if write:
        out_dir.mkdir(parents=True, exist_ok=True)
        for name, content in files.items():
            (out_dir / name).write_text(content)
        return {
            "dry_run": False,
            "session_no": session_no,
            "workspace_session_no": workspace_no,
            "out_dir": str(out_dir),
            "files_written": list(files.keys()),
        }
    return {
        "dry_run": True,
        "session_no": session_no,
        "workspace_session_no": workspace_no,
        "out_dir": str(out_dir),
        "files_planned": list(files.keys()),
    }


def _export_issues(conn: sqlite3.Connection, write: bool = False) -> dict:
    """Materialise open-issues/<alias>.md from the issues substrate table.

    One file per issue. Open issues land in `open-issues/`; resolved/superseded
    in `open-issues/resolved/`. Frontmatter mirrors the pre-S088 markdown shape
    so callers (and humans browsing git) see a familiar surface; body is the
    body atom if present, else the summary atom, else empty.
    """
    rows = conn.execute(
        "SELECT i.issue_id, i.alias, i.priority, i.status, "
        "       i.surfaced_session_id, i.resolved_session_id, i.resolved_at, "
        "       ta_t.text AS title, ta_s.text AS summary, ta_b.text AS body, "
        "       sf.workspace_session_no AS surfaced_wno, "
        "       sr.workspace_session_no AS resolved_wno "
        "FROM issues i "
        "JOIN text_atoms ta_t ON ta_t.atom_id=i.title_atom_id "
        "LEFT JOIN text_atoms ta_s ON ta_s.atom_id=i.summary_atom_id "
        "LEFT JOIN text_atoms ta_b ON ta_b.atom_id=i.body_atom_id "
        "JOIN sessions sf ON sf.session_id=i.surfaced_session_id "
        "LEFT JOIN sessions sr ON sr.session_id=i.resolved_session_id "
        "ORDER BY i.alias"
    ).fetchall()

    files: dict[str, str] = {}
    for r in rows:
        is_terminal = r["status"] in ("resolved", "superseded")
        rel = "resolved" if is_terminal else ""
        path = Path("open-issues") / rel / f"{r['alias']}.md" if rel else \
               Path("open-issues") / f"{r['alias']}.md"
        lines = ["---",
                 f"id: {r['alias']}",
                 f"status: {r['status']}",
                 f"priority: {r['priority']}",
                 f"surfaced-in-session: {r['surfaced_wno'] or ''}"]
        if r["resolved_wno"]:
            lines.append(f"resolved-in-session: {r['resolved_wno']}")
        if r["resolved_at"]:
            lines.append(f"resolved-at: {r['resolved_at']}")
        lines.append("generated_by: selvedge export --issues")
        lines.append("---")
        lines.append("")
        lines.append(f"# {r['title']}")
        lines.append("")
        if r["summary"]:
            lines.append(r["summary"])
            lines.append("")
        if r["body"]:
            lines.append(r["body"])
            lines.append("")
        # Footer flagging substrate compression. Bodies authored by the S088
        # backfill subagent are compressed canonical summaries (4000-char cap);
        # bodies of issues created post-engine-v22 reflect the author's intent
        # at submit time. Either way, the substrate is canonical and git
        # history holds any pre-substrate prose.
        lines.append("---")
        lines.append("*Substrate-canonical: regenerated from `issues` row by `selvedge export --issues`. "
                     "Body atoms are capped at 4000 chars; if this issue predates engine-v22 (pre-S088) the body "
                     "is a compressed canonical summary and the verbatim pre-substrate prose is in git history.*")
        files[str(path)] = "\n".join(lines).rstrip() + "\n"

    # Index: top-level pointer regenerated alongside the per-issue files.
    idx_lines = ["# Open issues — substrate-canonical (regenerated by `selvedge export --issues`)",
                 "",
                 "Issues live in the `issues` substrate table. The files below are a",
                 "deterministic export from substrate rows; do not hand-edit. Use",
                 "`bin/selvedge submit issue` and `submit issue-disposition` to mutate.",
                 ""]
    open_rows = [r for r in rows if r["status"] not in ("resolved", "superseded")]
    closed_rows = [r for r in rows if r["status"] in ("resolved", "superseded")]
    if open_rows:
        idx_lines.append("## Open")
        idx_lines.append("")
        idx_lines.append("| Alias | Priority | Status | Title |")
        idx_lines.append("|-------|----------|--------|-------|")
        for r in open_rows:
            idx_lines.append(f"| [{r['alias']}]({r['alias']}.md) | {r['priority']} | {r['status']} | {r['title']} |")
        idx_lines.append("")
    if closed_rows:
        idx_lines.append("## Resolved")
        idx_lines.append("")
        idx_lines.append("| Alias | Resolved-in | Title |")
        idx_lines.append("|-------|-------------|-------|")
        for r in closed_rows:
            idx_lines.append(f"| [{r['alias']}](resolved/{r['alias']}.md) | S{r['resolved_wno']:03d} | {r['title']} |")
        idx_lines.append("")
    files["open-issues/index.md"] = "\n".join(idx_lines).rstrip() + "\n"

    # Compute reconciliation: files currently on disk under open-issues/ that
    # are not in the substrate's target set must be deleted (or, in dry-run,
    # reported as `files_to_delete`). Without this, an open->resolved
    # transition leaves the stale top-level path next to the new resolved/
    # path — flagged in EF-S092-2.
    target_paths = {Path(pp).resolve() for pp in files.keys()}
    on_disk: list[Path] = []
    oi = Path("open-issues")
    if oi.exists():
        on_disk.extend(p for p in oi.glob("*.md"))
        resolved_dir = oi / "resolved"
        if resolved_dir.exists():
            on_disk.extend(p for p in resolved_dir.glob("*.md"))
    stale = sorted(str(p) for p in on_disk if p.resolve() not in target_paths)

    if write:
        for path_str, content in files.items():
            p = Path(path_str)
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content)
        for s in stale:
            Path(s).unlink()
        return {
            "dry_run": False,
            "issues_exported": len(rows),
            "files_written": sorted(files.keys()),
            "files_deleted": stale,
        }
    return {
        "dry_run": True,
        "issues_exported": len(rows),
        "files_planned": sorted(files.keys()),
        "files_to_delete": stale,
    }


def _orient_sections(conn: sqlite3.Connection) -> dict:
    """Gather the orientation packet as a dict of named sections.

    Used by cmd_orient. Each section is a list of dicts (or scalar) so the
    output can be rendered as either markdown or JSON without losing structure.
    """
    out: dict = {}
    out["workspace"] = {
        r["key"]: r["value"]
        for r in conn.execute("SELECT key, value FROM workspace_metadata").fetchall()
    }
    out["recent_close_records"] = [
        dict(r) for r in conn.execute(
            "SELECT s.workspace_session_no, s.slug, s.engine_version_at_close, s.closed_at, "
            "       cr.close_record_id "
            "FROM close_records cr JOIN sessions s ON s.session_id=cr.session_id "
            "ORDER BY s.session_no DESC LIMIT 3"
        ).fetchall()
    ]
    # Forward references: every undisposed close_state_item with
    # facet='next_session_should' across the full history. Disposition rows
    # in forward_reference_dispositions (migration 013, engine-v27 / EF-S096-1)
    # remove the item from the queue. Capped at 30 with truncation flag, in
    # parallel to open_issues/engine_feedback.
    fr_rows = conn.execute(
        "SELECT csi.seq, csi.state_item_id, ta.text AS text, "
        "       COALESCE(s.workspace_session_no, s.session_no) AS wno "
        "FROM close_state_items csi "
        "JOIN text_atoms ta ON ta.atom_id=csi.item_atom_id "
        "JOIN close_records cr ON cr.close_record_id=csi.close_record_id "
        "JOIN sessions s ON s.session_id=cr.session_id "
        "WHERE csi.facet='next_session_should' "
        "  AND NOT EXISTS (SELECT 1 FROM forward_reference_dispositions frd "
        "                  WHERE frd.state_item_id=csi.state_item_id) "
        "ORDER BY s.session_no DESC, csi.seq"
    ).fetchall()
    out["next_session_should_total"] = len(fr_rows)
    out["next_session_should"] = [
        {
            "from_session": f"S{r['wno']:03d}",
            "seq": r["seq"],
            "ref": f"FR-S{r['wno']:03d}-{r['seq']}",
            "text": r["text"],
        }
        for r in fr_rows[:30]
    ]
    out["next_session_should_truncated"] = len(fr_rows) > 30
    # Rot annotation: each FR text is scanned for OI- issue aliases via
    # regex; cites whose target issue is resolved/superseded or absent
    # become a `rot` list on the FR. Live cites (open/in_progress/blocked)
    # produce no annotation. No structured-citation table — annotation is
    # a derivation of the FR text, computed at orient time only. (DV-S101-1.)
    fr_cite_aliases: list[str] = []
    fr_cites: list[list[str]] = []
    for item in out["next_session_should"]:
        item["rot"] = []
        seen: list[str] = []
        for m in FR_ISSUE_CITE_RE.findall(item["text"]):
            if m not in seen:
                seen.append(m)
            if m not in fr_cite_aliases:
                fr_cite_aliases.append(m)
        fr_cites.append(seen)
    if fr_cite_aliases:
        placeholders = ",".join("?" * len(fr_cite_aliases))
        status_rows = conn.execute(
            f"SELECT alias, status FROM issues WHERE alias IN ({placeholders})",
            tuple(fr_cite_aliases),
        ).fetchall()
        status_by_alias = {r["alias"]: r["status"] for r in status_rows}
        LIVE_STATUSES = {"open", "in_progress", "blocked"}
        for item, cites in zip(out["next_session_should"], fr_cites):
            for alias in cites:
                status = status_by_alias.get(alias)
                if status is None:
                    item["rot"].append({"alias": alias, "status": "absent"})
                elif status not in LIVE_STATUSES:
                    item["rot"].append({"alias": alias, "status": status})
    open_issues_rows = conn.execute(
        "SELECT i.alias, i.priority, i.status, ta.text AS title "
        "FROM issues i JOIN text_atoms ta ON ta.atom_id=i.title_atom_id "
        "WHERE i.status IN ('open','in_progress','blocked') "
        "ORDER BY CASE i.priority WHEN 'HIGH' THEN 0 WHEN 'MEDIUM' THEN 1 ELSE 2 END, "
        "         i.surfaced_session_id"
    ).fetchall()
    out["open_issues_total"] = len(open_issues_rows)
    out["open_issues"] = [dict(r) for r in open_issues_rows[:30]]
    out["open_issues_truncated"] = len(open_issues_rows) > 30
    out["in_flight_work_items"] = [
        dict(r) for r in conn.execute(
            "SELECT work_item_id, kind, status, leased_by, lease_expires_at "
            "FROM work_items WHERE status IN ('queued','leased','failed') ORDER BY work_item_id"
        ).fetchall()
    ]
    out["active_specs"] = [
        dict(r) for r in conn.execute(
            "SELECT spec_id, version, body_canonical_in_substrate FROM spec_versions "
            "WHERE status='active' ORDER BY spec_id"
        ).fetchall()
    ]
    out["deferred_decisions"] = [
        dict(r) for r in conn.execute(
            "SELECT s.workspace_session_no, dv.decision_no, ta.text AS title "
            "FROM decisions_v2 dv JOIN sessions s ON s.session_id=dv.session_id "
            "JOIN text_atoms ta ON ta.atom_id=dv.title_atom_id "
            "WHERE dv.outcome_type='defer' ORDER BY dv.decision_v2_id DESC LIMIT 10"
        ).fetchall()
    ]
    out["open_findings"] = [
        dict(r) for r in conn.execute(
            "SELECT review_finding_id, severity, ta.text AS finding "
            "FROM review_findings rf JOIN text_atoms ta ON ta.atom_id=rf.finding_atom_id "
            "WHERE rf.disposition='open' AND rf.severity IN ('critical','high','medium') "
            "ORDER BY review_finding_id"
        ).fetchall()
    ]
    feedback_rows = conn.execute(
        "SELECT ef.feedback_id, ef.flag, ef.body_md, "
        "       o.alias, "
        "       s.workspace_session_no AS surfaced_in "
        "FROM engine_feedback ef "
        "LEFT JOIN objects o ON o.object_id=ef.object_id "
        "JOIN sessions s ON s.session_id=ef.session_id "
        "WHERE ef.disposition IS NULL "
        "ORDER BY ef.feedback_id DESC"
    ).fetchall()
    out["untriaged_feedback_total"] = len(feedback_rows)
    def _first_nonempty_line(text: str) -> str:
        for line in (text or "").splitlines():
            stripped = line.strip()
            if stripped:
                return stripped[:120]
        return ""

    out["untriaged_feedback"] = [
        {
            "alias": r["alias"] or f"feedback_id={r['feedback_id']}",
            "flag": r["flag"],
            "surfaced_in": r["surfaced_in"],
            "head": _first_nonempty_line(r["body_md"]),
        }
        for r in feedback_rows[:20]
    ]
    out["untriaged_feedback_truncated"] = len(feedback_rows) > 20
    out["unapplied_migrations"] = []  # filled lazily below if needed
    return out


def _orient_markdown(packet: dict) -> str:
    lines = ["# Workspace orientation", "", "Generated by `bin/selvedge orient`. "
             "Substrate is canonical; this packet is a live read.", ""]
    ws = packet["workspace"]
    lines.append("## Workspace")
    lines.append("")
    for k, v in ws.items():
        lines.append(f"- **{k}**: {v}")
    lines.append("")

    lines.append("## Recent sessions (last 3)")
    lines.append("")
    if packet["recent_close_records"]:
        lines.append("| Session | Slug | Engine | Closed at |")
        lines.append("|---------|------|--------|-----------|")
        for r in packet["recent_close_records"]:
            lines.append(f"| S{r['workspace_session_no']:03d} | {r['slug']} | "
                         f"{r['engine_version_at_close']} | {r['closed_at']} |")
        lines.append("")
    else:
        lines.append("(no closed sessions)")
        lines.append("")

    fr_total = packet.get("next_session_should_total", len(packet["next_session_should"]))
    lines.append(f"## Forward references ({len(packet['next_session_should'])} of {fr_total} undisposed)")
    lines.append("")
    if packet["next_session_should"]:
        for item in packet["next_session_should"]:
            suffix = ""
            if item.get("rot"):
                parts = [f"{r['alias']}: {r['status']}" for r in item["rot"]]
                suffix = f" [rot: {', '.join(parts)}]"
            lines.append(f"- {item['ref']} {item['text']}{suffix}")
        if packet.get("next_session_should_truncated"):
            lines.append("")
            lines.append(f"_{fr_total - len(packet['next_session_should'])} more elided. Dispose via `bin/selvedge submit forward-reference-disposition --payload '{{\"target_session\": <wno>, \"seq\": <n>, \"note\": \"...\"}}'`._")
    else:
        lines.append("(none)")
    lines.append("")

    total = packet.get("open_issues_total", len(packet["open_issues"]))
    lines.append(f"## Open issues ({len(packet['open_issues'])} of {total})")
    lines.append("")
    if packet["open_issues"]:
        lines.append("| Alias | Priority | Status | Title |")
        lines.append("|-------|----------|--------|-------|")
        for r in packet["open_issues"]:
            lines.append(f"| {r['alias']} | {r['priority']} | {r['status']} | {r['title']} |")
        if packet.get("open_issues_truncated"):
            lines.append("")
            lines.append(f"_{total - len(packet['open_issues'])} more issues elided. Run `bin/selvedge query \"SELECT alias, priority, status FROM issues WHERE status IN ('open','in_progress','blocked')\"` for the full list._")
    else:
        lines.append("(none)")
    lines.append("")

    lines.append(f"## In-flight work_items ({len(packet['in_flight_work_items'])})")
    lines.append("")
    if packet["in_flight_work_items"]:
        lines.append("| ID | Kind | Status | Leased by | Lease expires |")
        lines.append("|----|------|--------|-----------|---------------|")
        for r in packet["in_flight_work_items"]:
            lines.append(f"| {r['work_item_id']} | {r['kind']} | {r['status']} | "
                         f"{r['leased_by'] or ''} | {r['lease_expires_at'] or ''} |")
    else:
        lines.append("(none)")
    lines.append("")

    lines.append("## Active specs")
    lines.append("")
    lines.append("| Spec | Version | Canonical-in-substrate |")
    lines.append("|------|---------|------------------------|")
    for r in packet["active_specs"]:
        lines.append(f"| {r['spec_id']} | {r['version']} | {r['body_canonical_in_substrate']} |")
    lines.append("")

    lines.append(f"## Deferred decisions ({len(packet['deferred_decisions'])})")
    lines.append("")
    if packet["deferred_decisions"]:
        for r in packet["deferred_decisions"]:
            lines.append(f"- DV-S{r['workspace_session_no']:03d}-{r['decision_no']}: {r['title']}")
    else:
        lines.append("(none)")
    lines.append("")

    lines.append(f"## Open review findings ({len(packet['open_findings'])})")
    lines.append("")
    if packet["open_findings"]:
        for r in packet["open_findings"]:
            lines.append(f"- [{r['severity']}] {r['finding']}")
    else:
        lines.append("(none)")
    lines.append("")

    fb_total = packet.get("untriaged_feedback_total", len(packet.get("untriaged_feedback", [])))
    fb = packet.get("untriaged_feedback", [])
    lines.append(f"## Untriaged engine feedback ({len(fb)} of {fb_total})")
    lines.append("")
    if fb:
        lines.append("| Alias | Flag | Surfaced | Head |")
        lines.append("|-------|------|----------|------|")
        for r in fb:
            surfaced = f"S{r['surfaced_in']:03d}" if r["surfaced_in"] is not None else ""
            head = (r["head"] or "").replace("|", "\\|")
            lines.append(f"| {r['alias']} | {r['flag']} | {surfaced} | {head} |")
        if packet.get("untriaged_feedback_truncated"):
            lines.append("")
            lines.append(f"_{fb_total - len(fb)} more untriaged feedback rows elided. Run `bin/selvedge query \"SELECT feedback_id, flag, body_md FROM engine_feedback WHERE disposition IS NULL\"` for the full list._")
        lines.append("")
        lines.append("_Triage via `bin/selvedge submit engine-feedback-disposition --payload '{\"alias\": \"EF-...\", \"disposition\": \"...\"}'`._")
    else:
        lines.append("(none)")
    lines.append("")
    return "\n".join(lines)


def cmd_orient(args) -> int:
    conn = sqlite3.connect(str(db_path()))
    conn.row_factory = sqlite3.Row
    try:
        packet = _orient_sections(conn)
    finally:
        conn.close()
    if args.as_json:
        print(json.dumps(packet, indent=2, default=str))
    else:
        print(_orient_markdown(packet))
    return 0


def _schema_summary(conn: sqlite3.Connection, table: str | None = None) -> str:
    """Return a formatted, table-by-table schema summary derived from sqlite_master."""
    where = "name=?" if table else "1=1"
    args_: tuple = (table,) if table else ()
    tables = conn.execute(
        f"SELECT name, sql FROM sqlite_master WHERE type='table' AND {where} ORDER BY name",
        args_,
    ).fetchall()
    if not tables:
        return f"(no table named {table!r})" if table else "(no tables)"
    lines: list[str] = []
    for t in tables:
        lines.append(f"## {t['name']}")
        lines.append("")
        cols = conn.execute(f"PRAGMA table_info({t['name']})").fetchall()
        lines.append("| Column | Type | NotNull | Default | PK |")
        lines.append("|--------|------|---------|---------|----|")
        for c in cols:
            lines.append(f"| {c['name']} | {c['type']} | {c['notnull']} | "
                         f"{c['dflt_value'] or ''} | {c['pk']} |")
        lines.append("")
        # CHECK enums extracted with a regex over the CREATE TABLE statement.
        sql = t["sql"] or ""
        for m in re.finditer(
            r"\b(\w+)\s+TEXT[^,]*?CHECK\s*\([^)]*?\1\s+IN\s*\(([^)]+)\)",
            sql, flags=re.IGNORECASE | re.DOTALL,
        ):
            col, vals = m.group(1), m.group(2)
            enum_vals = [v.strip().strip("'\"") for v in vals.split(",")]
            lines.append(f"- **{col}** admits: {', '.join(enum_vals)}")
        # Foreign keys.
        fks = conn.execute(f"PRAGMA foreign_key_list({t['name']})").fetchall()
        for fk in fks:
            lines.append(f"- FK `{fk['from']}` → `{fk['table']}({fk['to']})`")
        # Indexes (skip the implicit sqlite_autoindex_*).
        idx = conn.execute(
            "SELECT name, sql FROM sqlite_master WHERE type='index' AND tbl_name=? "
            "AND name NOT LIKE 'sqlite_autoindex_%' ORDER BY name",
            (t["name"],),
        ).fetchall()
        for i in idx:
            lines.append(f"- index `{i['name']}`")
        # Triggers.
        trg = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='trigger' AND tbl_name=? ORDER BY name",
            (t["name"],),
        ).fetchall()
        for tr in trg:
            lines.append(f"- trigger `{tr['name']}`")
        lines.append("")
    return "\n".join(lines)


def cmd_schema(args) -> int:
    conn = sqlite3.connect(str(db_path()))
    conn.row_factory = sqlite3.Row
    try:
        if args.raw:
            where = "name=?" if args.table else "1=1"
            params: tuple = (args.table,) if args.table else ()
            for r in conn.execute(
                f"SELECT sql FROM sqlite_master WHERE sql IS NOT NULL AND {where} "
                "ORDER BY type, name",
                params,
            ).fetchall():
                print(r["sql"] + ";")
        else:
            print(_schema_summary(conn, args.table))
    finally:
        conn.close()
    return 0


def cmd_export(args) -> int:
    conn = sqlite3.connect(str(db_path()))
    conn.row_factory = sqlite3.Row
    try:
        if args.issues:
            result = _export_issues(conn, write=args.write)
            print(json.dumps(result, indent=2))
        elif args.session is not None:
            result = _export_session_provenance(conn, args.session, write=args.write)
            print(json.dumps(result, indent=2))
        else:
            print("export: pass --session <N> or --issues", file=sys.stderr)
            return 2
    finally:
        conn.close()
    return 0


# ---------------------------------------------------------------------------
# monitor-external (engine-v31 origin; engine-v33 substrate-direct ef per S110 D-1)
#
# Three subcommands operate against a peer Selvedge workspace given by
# --workspace <path>. `status` and `next-input` read the peer's substrate
# read-only via SQLite URI. `harvest-ef` reads engine_feedback rows directly
# from the peer's substrate (engine-v26+ substrate-only-writes) and copies
# them into THIS workspace's substrate via the existing `submit
# engine-feedback` handler, recording per-row provenance in a
# harvested_engine_feedback ledger so re-runs are idempotent at row
# precision. The tool is generic across external workspaces; per DV-S106-3
# if next-input or harvest-ef goes unused at the S009 retrospective, the
# unused subcommands are deleted rather than deprecated.
# ---------------------------------------------------------------------------


def _me_validate_external(workspace_arg: str) -> tuple[Path, Path]:
    """Resolve and validate an external workspace path. Refuse if it points at
    THIS workspace (so harvest-ef cannot accidentally write to its source).

    Per S108 review F-87, the self-vs-peer guard uses inode equality
    (`Path.samefile`) so it survives macOS case-insensitive filesystems and
    symlinks where two distinct path strings refer to the same directory.
    """
    if not workspace_arg:
        raise SelvedgeError("E_BAD_ARG", "--workspace is required")
    root = Path(workspace_arg).expanduser().resolve()
    if not root.exists():
        raise SelvedgeError("E_NO_WORKSPACE", f"path does not exist: {root}")
    if not root.is_dir():
        raise SelvedgeError("E_NO_WORKSPACE", f"not a directory: {root}")
    if not (root / "MODE.md").exists():
        raise SelvedgeError("E_NO_WORKSPACE", f"missing MODE.md: {root}")
    db = root / "state" / "selvedge.sqlite"
    if not db.exists():
        raise SelvedgeError("E_NO_WORKSPACE", f"missing substrate: {db}")
    try:
        self_root = workspace_root()
    except SelvedgeError:
        self_root = None
    if self_root is not None and self_root.exists() and root.samefile(self_root):
        raise SelvedgeError(
            "E_REFUSAL_SELF",
            f"--workspace points at this workspace ({root}); "
            "monitor-external requires a peer workspace",
        )
    return root, db


def _me_open_external_ro(db: Path) -> sqlite3.Connection:
    """Open the external substrate read-only via a SQLite URI.

    Per S108 review F-83, the path component is URL-quoted because SQLite's
    URI parser treats `?`, `#`, and `&` as URI delimiters; a peer workspace
    whose absolute path contains those characters would otherwise fail to
    open with a misleading "no such table" error.

    Per S110 D-1, set busy_timeout (covers transient WAL contention without an
    explicit Python sleep loop) and query_only (defence-in-depth against any
    accidental write attempt against the peer connection).
    """
    quoted = urllib.parse.quote(str(db), safe="/")
    conn = sqlite3.connect(f"file:{quoted}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA busy_timeout = 1000")
    conn.execute("PRAGMA query_only = 1")
    return conn


def _me_iso_utc(ts: float) -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(ts))


def _me_collect_close(conn: sqlite3.Connection) -> dict:
    """Read the latest close_record's summary + next_session_should atoms."""
    row = conn.execute(
        "SELECT cr.close_record_id, "
        "       COALESCE(s.workspace_session_no, s.session_no) AS wno, "
        "       ta_sum.text AS summary "
        "FROM close_records cr "
        "JOIN sessions s ON s.session_id=cr.session_id "
        "JOIN text_atoms ta_sum ON ta_sum.atom_id=cr.summary_atom_id "
        "ORDER BY s.session_no DESC LIMIT 1"
    ).fetchone()
    if row is None:
        return {"workspace_session_no": None, "summary": None, "next_session_should": []}
    next_should = [
        r["text"] for r in conn.execute(
            "SELECT ta.text FROM close_state_items csi "
            "JOIN text_atoms ta ON ta.atom_id=csi.item_atom_id "
            "WHERE csi.close_record_id=? AND csi.facet='next_session_should' "
            "ORDER BY csi.seq",
            (row["close_record_id"],),
        ).fetchall()
    ]
    return {
        "workspace_session_no": row["wno"],
        "summary": row["summary"],
        "next_session_should": next_should,
    }


def _me_status(args) -> int:
    root, db = _me_validate_external(args.workspace)
    conn = _me_open_external_ro(db)
    try:
        meta = {r["key"]: r["value"] for r in conn.execute(
            "SELECT key, value FROM workspace_metadata"
        ).fetchall()}
        sessions = [dict(r) for r in conn.execute(
            "SELECT session_no, workspace_session_no, slug, kind, status, "
            "engine_version_at_open, engine_version_at_close, opened_at, closed_at "
            "FROM sessions ORDER BY session_no DESC LIMIT 5"
        ).fetchall()]
        oi_counts = {r["priority"]: r["n"] for r in conn.execute(
            "SELECT priority, COUNT(*) AS n FROM issues "
            "WHERE status='open' GROUP BY priority"
        ).fetchall()}
        latest_close = _me_collect_close(conn)
        # Engine-v33 (S110 D-1): peer engine_feedback lives in the substrate,
        # not engine-feedback/*.md. Read directly. If the peer schema lacks the
        # table, surface ef_rows=None so the renderer can distinguish "no feedback
        # yet" from "this peer is too old to read feedback from".
        ef_rows: list[dict] | None
        if conn.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name='engine_feedback'"
        ).fetchone():
            ef_rows = [dict(r) for r in conn.execute(
                "SELECT ef.feedback_id, ef.flag, ef.disposition, "
                "       COALESCE(s.workspace_session_no, s.session_no) AS wno "
                "FROM engine_feedback ef "
                "JOIN sessions s ON s.session_id = ef.session_id "
                "ORDER BY ef.feedback_id DESC LIMIT 10"
            ).fetchall()]
        else:
            ef_rows = None
    finally:
        conn.close()

    spp = max(1, args.sessions_per_phase)
    latest_local_no = sessions[0]["session_no"] if sessions else 0
    phase_idx = max(0, latest_local_no - 1) // spp if latest_local_no else 0

    pkt = {
        "workspace_path": str(root),
        "workspace_metadata": meta,
        "recent_sessions": sessions,
        "open_issues_total": sum(oi_counts.values()),
        "open_issues_by_priority": oi_counts,
        "ef_rows": ef_rows,
        "latest_close": latest_close,
        "phase_heuristic": {
            "value": f"P{phase_idx}",
            "sessions_per_phase": spp,
            "method": (
                "floor((latest_substrate_session_no - 1) / sessions_per_phase); "
                "uses local session_no so init_session_offset does not skew arc-phase"
            ),
        },
    }
    if args.as_json:
        print(json.dumps(pkt, indent=2, default=str))
    else:
        print(_me_render_status_md(pkt))
    return 0


def _me_render_status_md(pkt: dict) -> str:
    lines: list[str] = []
    lines.append("# monitor-external status")
    lines.append("")
    lines.append(f"- **workspace_path**: {pkt['workspace_path']}")
    for k in ("workspace_id", "mode", "current_engine_version"):
        if k in pkt["workspace_metadata"]:
            lines.append(f"- **{k}**: {pkt['workspace_metadata'][k]}")
    lines.append("")
    lines.append(f"## Recent sessions ({len(pkt['recent_sessions'])})")
    lines.append("")
    if pkt["recent_sessions"]:
        lines.append("| Session | Slug | Kind | Status | Engine open | Engine close | Closed at |")
        lines.append("|---------|------|------|--------|-------------|--------------|-----------|")
        for s in pkt["recent_sessions"]:
            wno = s.get("workspace_session_no") or s["session_no"]
            lines.append(
                f"| S{wno:03d} | {s['slug']} | {s['kind']} | {s['status']} | "
                f"{s['engine_version_at_open']} | {s.get('engine_version_at_close') or ''} | "
                f"{s.get('closed_at') or ''} |"
            )
    else:
        lines.append("(no sessions yet)")
    lines.append("")
    lines.append(f"## Open issues ({pkt['open_issues_total']})")
    lines.append("")
    if pkt["open_issues_by_priority"]:
        for prio in ("HIGH", "MEDIUM", "LOW"):
            n = pkt["open_issues_by_priority"].get(prio)
            if n:
                lines.append(f"- {prio}: {n}")
    else:
        lines.append("(none)")
    lines.append("")
    lines.append("## Engine-feedback (peer substrate, last 10)")
    lines.append("")
    rows = pkt.get("ef_rows")
    if rows is None:
        lines.append("(peer schema does not expose engine_feedback table)")
    elif rows:
        for r in rows:
            disp = f" — disposed: {r['disposition']}" if r.get("disposition") else ""
            lines.append(
                f"- feedback_id={r['feedback_id']} S{r['wno']:03d} "
                f"flag={r['flag']}{disp}"
            )
    else:
        lines.append("(no engine_feedback rows in peer substrate)")
    lines.append("")
    lines.append("## Latest close-record next_session_should")
    lines.append("")
    lc = pkt["latest_close"]
    if lc["next_session_should"]:
        lines.append(f"- close from S{lc['workspace_session_no']:03d}")
        for item in lc["next_session_should"]:
            lines.append(f"  - {item}")
    else:
        lines.append("(no closed session with next_session_should yet)")
    lines.append("")
    lines.append("## Phase heuristic")
    lines.append("")
    ph = pkt["phase_heuristic"]
    lines.append(f"- **value**: {ph['value']} (sessions_per_phase={ph['sessions_per_phase']})")
    lines.append(f"- method: {ph['method']}")
    lines.append("")
    return "\n".join(lines)


def _me_next_input(args) -> int:
    root, db = _me_validate_external(args.workspace)

    def _read_optional(path_arg: str | None, label: str) -> tuple[str | None, str | None]:
        if not path_arg:
            return None, None
        p = Path(path_arg).expanduser().resolve()
        if not p.exists():
            raise SelvedgeError("E_NO_FILE", f"{label} not found: {p}")
        return str(p), p.read_text()

    arc_plan_path, arc_plan_excerpt = _read_optional(args.arc_plan, "arc-plan")
    ledger_path, ledger_excerpt = _read_optional(args.assumption_ledger, "assumption-ledger")

    conn = _me_open_external_ro(db)
    try:
        latest_session = conn.execute(
            "SELECT session_no, workspace_session_no, slug, kind, status, closed_at "
            "FROM sessions ORDER BY session_no DESC LIMIT 1"
        ).fetchone()
        latest_close = _me_collect_close(conn)
        open_oi = [r["alias"] for r in conn.execute(
            "SELECT alias FROM issues WHERE status='open' "
            "ORDER BY CASE priority WHEN 'HIGH' THEN 0 WHEN 'MEDIUM' THEN 1 ELSE 2 END, alias"
        ).fetchall()]
    finally:
        conn.close()

    if latest_session is None:
        next_session_no = 1
        next_workspace_session_no = 1
    else:
        next_session_no = latest_session["session_no"] + 1
        next_workspace_session_no = (
            latest_session["workspace_session_no"] or latest_session["session_no"]
        ) + 1

    out = {
        "external_workspace": str(root),
        "phase": args.phase,
        "next_external_session_no": next_session_no,
        "next_external_workspace_session_no": next_workspace_session_no,
        "latest_close": latest_close,
        "open_issue_aliases": open_oi,
        "arc_plan_path": arc_plan_path,
        "arc_plan_excerpt": arc_plan_excerpt,
        "assumption_ledger_path": ledger_path,
        "assumption_ledger_excerpt": ledger_excerpt,
        "draft_session_input": {
            "phase": args.phase,
            "carry_forward_from_close": latest_close["next_session_should"],
            "operator_must_fill": [
                "reveal_axis",
                "domain_facts",
                "specific_assumption_ids_to_revise",
                "session_input_md_body",
            ],
            "note": (
                "This is a JSON drafting buffer per DV-S106-3. The operator reviews and "
                "edits before placing the final session-input markdown in the external "
                "workspace's applications/<slug>/session-inputs/ directory."
            ),
        },
    }
    payload = json.dumps(out, indent=2, default=str)
    if args.out:
        out_path = Path(args.out).expanduser().resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(payload)
        print(json.dumps({"ok": True, "wrote": str(out_path), "bytes": len(payload)}))
    else:
        print(payload)
    return 0


def _me_read_peer_ef(peer_db: Path) -> tuple[str, list[dict]]:
    """Read the peer's engine_feedback rows substrate-direct.

    Returns (peer_workspace_id, rows). Each row dict has feedback_id, peer_wno,
    peer_slug, flag, body_md, peer_alias (or None if peer schema lacks objects
    or the row has no object_id).

    Raises:
      E_PEER_OPEN_FAILED if peer DB cannot be opened for non-busy reasons.
      E_PEER_BUSY if SQLite returns busy/locked after busy_timeout expiry.
      E_PEER_QUERY_FAILED if any peer query fails for non-busy reasons.
      E_PEER_SCHEMA_UNSUPPORTED if the peer DB lacks engine_feedback table or
      its workspace_metadata.workspace_id is missing.

    Per S110 D-1: capability-based detection over migration-version gating.
    The contract is the columns, not the engine version. Reads happen on a
    short-lived RO connection and complete before opening any self-dev write
    transaction (prevents holding the peer DB locked across slow self-dev work).

    Reviewer iter-2 NEW-1 (S110): every peer query is wrapped in the same
    OperationalError categorisation (E_PEER_BUSY for transient, E_PEER_QUERY_FAILED
    otherwise). Schema-validation queries are not exempt.
    """
    try:
        conn = _me_open_external_ro(peer_db)
    except sqlite3.OperationalError as e:
        # Reviewer F-HIGH-1 (S110 iter-1): distinguish transient busy from
        # permanent open failures. Pattern matches _refusal_from_sqlite.
        msg = str(e)
        if "database is locked" in msg or "database is busy" in msg:
            raise SelvedgeError("E_PEER_BUSY", f"peer substrate busy: {e}")
        raise SelvedgeError("E_PEER_OPEN_FAILED", f"could not open peer substrate: {e}")

    def _peer_exec(sql: str, params: tuple = ()):
        """Execute a peer query with the same OperationalError categorisation
        used by open + main-query paths. Per iter-2 NEW-1."""
        try:
            return conn.execute(sql, params).fetchall()
        except sqlite3.OperationalError as e:
            msg = str(e)
            if "database is locked" in msg or "database is busy" in msg:
                raise SelvedgeError("E_PEER_BUSY", f"peer substrate query busy: {e}")
            raise SelvedgeError("E_PEER_QUERY_FAILED", f"peer substrate query failed: {e}")

    try:
        if not _peer_exec(
            "SELECT 1 FROM sqlite_master "
            "WHERE type='table' AND name='engine_feedback'"
        ):
            raise SelvedgeError(
                "E_PEER_SCHEMA_UNSUPPORTED",
                "peer substrate has no engine_feedback table; harvest-ef requires "
                "engine-v17+ with the engine_feedback table present",
            )
        meta_rows = _peer_exec(
            "SELECT value FROM workspace_metadata WHERE key='workspace_id'"
        )
        if not meta_rows or not meta_rows[0]["value"]:
            raise SelvedgeError(
                "E_PEER_SCHEMA_UNSUPPORTED",
                "peer workspace_metadata.workspace_id is missing; required to key "
                "the harvested_engine_feedback ledger uniquely",
            )
        peer_ws_id = str(meta_rows[0]["value"])
        # Capability-based detection of objects.alias (engine-v30) vs the older
        # citable_alias (pre-engine-v30). Per S110 deliberation P-2 catch.
        has_objects_alias = bool(_peer_exec(
            "SELECT 1 FROM pragma_table_info('objects') WHERE name='alias'"
        ))
        has_objects_citable = bool(_peer_exec(
            "SELECT 1 FROM pragma_table_info('objects') WHERE name='citable_alias'"
        ))
        alias_col_sql: str | None
        if has_objects_alias:
            alias_col_sql = "o.alias"
        elif has_objects_citable:
            alias_col_sql = "o.citable_alias"
        else:
            alias_col_sql = None  # peer too old to expose object aliases

        if alias_col_sql:
            sql = (
                "SELECT ef.feedback_id, "
                "       COALESCE(s.workspace_session_no, s.session_no) AS peer_wno, "
                "       s.slug AS peer_slug, "
                "       ef.flag, ef.body_md, "
                f"       {alias_col_sql} AS peer_alias "
                "FROM engine_feedback ef "
                "JOIN sessions s ON s.session_id = ef.session_id "
                "LEFT JOIN objects o ON o.object_id = ef.object_id "
                "ORDER BY ef.feedback_id"
            )
        else:
            sql = (
                "SELECT ef.feedback_id, "
                "       COALESCE(s.workspace_session_no, s.session_no) AS peer_wno, "
                "       s.slug AS peer_slug, "
                "       ef.flag, ef.body_md, "
                "       NULL AS peer_alias "
                "FROM engine_feedback ef "
                "JOIN sessions s ON s.session_id = ef.session_id "
                "ORDER BY ef.feedback_id"
            )
        rows = [dict(r) for r in _peer_exec(sql)]
    finally:
        conn.close()
    return peer_ws_id, rows


def _me_harvest_ef(args) -> int:
    # Pin the write target to THIS workspace before validating the peer; the
    # `--workspace <peer>` argument tells us where to *read* from but writes
    # always land in self-dev. Two guards together make the write target
    # unambiguous:
    #
    # (1) Iter-3 F-92: require SELVEDGE_WORKSPACE to be set so the self-dev
    #     workspace is operator-explicit, not inferred by cwd walk. Without
    #     this, a third-workspace cwd (cwd inside peer1 while --workspace
    #     names peer2) would route writes to peer1's substrate via
    #     workspace_root()'s upward MODE.md search.
    #
    # (2) Iter-2 F-90: even with SELVEDGE_WORKSPACE set, refuse if cwd is
    #     inside the peer being monitored — that is operator confusion and
    #     deserves an explicit error rather than a silently-correct write.
    if WORKSPACE_ROOT_ENV not in os.environ:
        raise SelvedgeError(
            "E_REFUSAL_SELF",
            f"harvest-ef requires {WORKSPACE_ROOT_ENV} to be set so the self-dev "
            "write target is unambiguous; cwd-based workspace inference is too "
            "ambiguous for write operations across peer workspaces",
        )
    self_root = workspace_root()
    self_db = self_root / "state" / "selvedge.sqlite"
    if not self_db.exists():
        raise SelvedgeError("E_NO_WORKSPACE", f"missing self-dev substrate: {self_db}")
    root, peer_db = _me_validate_external(args.workspace)
    cwd_resolved = Path.cwd().resolve()
    if cwd_resolved == root or cwd_resolved.is_relative_to(root):
        raise SelvedgeError(
            "E_REFUSAL_SELF",
            f"refusing harvest-ef: current directory {cwd_resolved} is inside the peer "
            f"workspace {root}; run from the self-dev workspace so the write target is "
            "unambiguous",
        )

    # Read all peer rows substrate-direct before opening the self-dev write
    # transaction (P-2 deliberation: read all peer rows first; never hold the
    # peer connection open across slow self-dev work).
    peer_ws_id, peer_rows = _me_read_peer_ef(peer_db)

    # Build the plan: for each peer row, look up the ledger to decide harvest
    # vs already-harvested. --since-session is preserved as an optional
    # operator-coarse filter on top of the per-row ledger.
    self_conn = sqlite3.connect(str(self_db))
    self_conn.row_factory = sqlite3.Row
    try:
        ledger_existing: set[int] = {
            int(r["peer_feedback_id"])
            for r in self_conn.execute(
                "SELECT peer_feedback_id FROM harvested_engine_feedback "
                "WHERE peer_workspace_id=?",
                (peer_ws_id,),
            ).fetchall()
        }
    finally:
        self_conn.close()

    plan: list[dict] = []
    for r in peer_rows:
        fid = int(r["feedback_id"])
        wno = int(r["peer_wno"]) if r.get("peer_wno") is not None else None
        flag = r["flag"]
        entry: dict = {
            "peer_feedback_id": fid,
            "peer_wno": wno,
            "peer_slug": r.get("peer_slug"),
            "peer_alias": r.get("peer_alias"),
            "flag": flag,
        }
        if fid in ledger_existing:
            entry["action"] = "skip"
            entry["reason"] = "already-harvested (per peer_workspace_id, peer_feedback_id)"
            plan.append(entry)
            continue
        if (
            args.since_session is not None
            and wno is not None
            and wno <= args.since_session
        ):
            entry["action"] = "skip"
            entry["reason"] = f"session {wno} <= --since-session {args.since_session}"
            plan.append(entry)
            continue
        entry["action"] = "harvest"
        plan.append(entry)

    if args.dry_run:
        out = {
            "ok": True, "dry_run": True,
            "peer_workspace_id": peer_ws_id,
            "peer_rows_total": len(peer_rows),
            "plan": plan,
        }
        if not peer_rows:
            # Reviewer F-MEDIUM-3 (S110 iter-1): explicit signal so an operator
            # does not mistake silent success for harvest having work to do.
            out["note"] = "peer substrate has no engine_feedback rows"
        print(json.dumps(out, indent=2))
        return 0

    # Build a body-by-feedback_id map so the write loop has the prose without
    # re-querying the peer (peer connection is already closed).
    bodies: dict[int, str] = {int(r["feedback_id"]): r["body_md"] for r in peer_rows}

    role = args.role or "__cli__"
    results: list[dict] = []
    c = Conn.open(self_db)
    try:
        for entry in plan:
            if entry["action"] != "harvest":
                results.append({**entry, "status": "skipped"})
                continue
            fid = entry["peer_feedback_id"]
            body = bodies[fid]
            wno = entry["peer_wno"]
            peer_alias = entry.get("peer_alias")
            preface_alias = f"alias `{peer_alias}`, " if peer_alias else ""
            preface = (
                f"_Harvested from peer substrate `{peer_ws_id}` "
                f"(peer feedback_id {fid}, {preface_alias}"
                f"external session S{wno:03d})._\n\n"
                if wno is not None
                else f"_Harvested from peer substrate `{peer_ws_id}` "
                f"(peer feedback_id {fid}, {preface_alias}external session unknown)._\n\n"
            )
            payload = {"flag": entry["flag"], "body_md": preface + body}
            try:
                # Reviewer F-MEDIUM-4 (S110 iter-1): pass `role` as a default-arg
                # for closure-capture consistency with other args (loop-invariant
                # but the explicit form rules out late-binding surprises).
                def _do_harvest(conn, p=payload, fid=fid, peer_ws_id=peer_ws_id,
                                 peer_alias=peer_alias, role=role):
                    res = SUBMIT_HANDLERS["engine-feedback"](conn, p, role)
                    sess_id = _atom_session_id(conn, None)
                    _check_role_capability(
                        conn, role, "harvested_engine_feedback", "insert"
                    )
                    conn.execute(
                        "INSERT INTO harvested_engine_feedback "
                        "(peer_workspace_id, peer_feedback_id, peer_alias, "
                        " imported_object_id, session_id) "
                        "VALUES (?,?,?,?,?)",
                        (peer_ws_id, fid, peer_alias, res["object_id"], sess_id),
                    )
                    return res
                result = c.write_tx(_do_harvest)
                results.append({
                    **entry,
                    "status": "success",
                    "self_alias": result["alias"],
                    "self_object_id": result["object_id"],
                })
            except SelvedgeError as e:
                # Reviewer F-MEDIUM-2 (S110 iter-1): label race-window UNIQUE
                # collisions explicitly so the operator distinguishes "another
                # harvest grabbed this row first" from real errors.
                if e.code == "E_REFUSAL_UNIQUE" and "harvested_engine_feedback" in e.detail:
                    results.append({
                        **entry,
                        "status": "skipped",
                        "reason": "concurrent harvest already imported this peer row",
                    })
                else:
                    results.append({
                        **entry,
                        "status": "error",
                        "error": e.code,
                        "detail": e.detail,
                    })
            except Exception as e:  # noqa: BLE001 — surface to operator, never silent
                results.append({
                    **entry,
                    "status": "error",
                    "error": type(e).__name__,
                    "detail": str(e),
                })
    finally:
        c.close()
    out = {
        "ok": True, "dry_run": False,
        "peer_workspace_id": peer_ws_id,
        "peer_rows_total": len(peer_rows),
        "results": results,
    }
    if not peer_rows:
        out["note"] = "peer substrate has no engine_feedback rows"
    print(json.dumps(out, indent=2))
    return 0


def cmd_monitor_external(args) -> int:
    sub = args.monitor_sub
    if sub == "status":
        return _me_status(args)
    if sub == "next-input":
        return _me_next_input(args)
    if sub == "harvest-ef":
        return _me_harvest_ef(args)
    print(f"unknown monitor-external subcommand: {sub}", file=sys.stderr)
    return 2


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="selvedge", description="Selvedge substrate CLI (engine-v20)")
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

    p_exp = sub.add_parser("export", help="Materialise markdown views from substrate rows (engine-v20+).")
    p_exp.add_argument("--session", type=int, help="Session number to export.")
    p_exp.add_argument("--issues", action="store_true", help="Export the issues table to open-issues/<alias>.md (engine-v22+).")
    p_exp.add_argument("--write", action="store_true", help="Write files to disk (default: dry-run, print plan).")
    p_exp.set_defaults(fn=cmd_export)

    p_orient = sub.add_parser("orient", help="Print the workspace orientation packet (engine-v23+).")
    p_orient.add_argument("--json", dest="as_json", action="store_true", help="Emit JSON instead of markdown.")
    p_orient.set_defaults(fn=cmd_orient)

    p_schema = sub.add_parser("schema", help="Print substrate schema (live read from sqlite_master).")
    p_schema.add_argument("table", nargs="?", default=None, help="Optional table name to focus on.")
    p_schema.add_argument("--raw", action="store_true", help="Emit raw .schema DDL instead of formatted view.")
    p_schema.set_defaults(fn=cmd_schema)

    p_me = sub.add_parser(
        "monitor-external",
        help="Read a peer Selvedge workspace and harvest its engine-feedback (engine-v31, DV-S106-3).",
    )
    me_sub = p_me.add_subparsers(dest="monitor_sub", required=True)

    p_me_st = me_sub.add_parser("status", help="Print external workspace status (read-only).")
    p_me_st.add_argument("--workspace", required=True, help="Path to peer workspace root (must contain MODE.md and state/selvedge.sqlite).")
    p_me_st.add_argument("--json", dest="as_json", action="store_true", help="Emit JSON instead of markdown.")
    p_me_st.add_argument("--sessions-per-phase", type=int, default=3, help="Heuristic phase divisor (default 3).")
    p_me_st.set_defaults(fn=cmd_monitor_external)

    p_me_ni = me_sub.add_parser("next-input", help="Emit a JSON draft of the next session-input file.")
    p_me_ni.add_argument("--workspace", required=True, help="Path to peer workspace root.")
    p_me_ni.add_argument("--arc-plan", default=None, help="Path to the arc-plan markdown (optional, embedded in output).")
    p_me_ni.add_argument("--assumption-ledger", default=None, help="Path to assumption-ledger markdown (optional, embedded in output).")
    p_me_ni.add_argument("--phase", default=None, help="Phase identifier (operator-supplied).")
    p_me_ni.add_argument("--out", default=None, help="Write JSON to file path instead of stdout.")
    p_me_ni.set_defaults(fn=cmd_monitor_external)

    p_me_he = me_sub.add_parser(
        "harvest-ef",
        help="Read peer engine_feedback rows substrate-direct and copy into THIS workspace's engine_feedback rows (idempotent via harvested_engine_feedback ledger).",
    )
    p_me_he.add_argument("--workspace", required=True, help="Path to peer workspace root.")
    p_me_he.add_argument("--since-session", type=int, default=None, help="Optional coarse filter: skip rows whose peer workspace_session_no is <= N.")
    p_me_he.add_argument("--dry-run", action="store_true", help="Print harvest plan without writing rows.")
    p_me_he.add_argument("--role", default="__cli__")
    p_me_he.set_defaults(fn=cmd_monitor_external)

    args = parser.parse_args(argv)
    try:
        return args.fn(args)
    except SelvedgeError as e:
        print(json.dumps({"ok": False, "code": e.code, "detail": e.detail}), file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
