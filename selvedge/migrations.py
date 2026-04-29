"""Migration parsing, T-15 enforcement, and the `migrate` subcommand."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import sqlite3
import sys
from pathlib import Path

from .errors import SelvedgeError
from .paths import db_path, migrations_dir


# T-15 forbids destructive DDL in migrations. ADD-only schema discipline; trigger,
# index, and view drops are admitted (they re-shape enforcement, not data).
T15_FORBIDDEN_PATTERNS = [
    (re.compile(r"\bDROP\s+TABLE\b", re.IGNORECASE), "DROP TABLE"),
    (re.compile(r"\bDROP\s+COLUMN\b", re.IGNORECASE), "DROP COLUMN"),
    (re.compile(r"\bALTER\s+TABLE\b[^;]*\bDROP\b", re.IGNORECASE | re.DOTALL), "ALTER TABLE … DROP"),
]

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
    for raw in cleaned.split(";"):
        stmt = raw.strip()
        if not stmt:
            continue
        if not _CALIBRATED_ALLOWED_STMT_RE.match(stmt):
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
    """Inspect the substrate's schema_migrations against files on disk."""
    if not path.exists():
        raise SelvedgeError("E_NO_SUBSTRATE", f"no substrate at {path}; run `selvedge init` first")
    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    try:
        applied_rows = conn.execute(
            "SELECT name, sha256 FROM schema_migrations ORDER BY migration_id"
        ).fetchall()
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
                try:
                    conn.close()
                except Exception:
                    pass
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
