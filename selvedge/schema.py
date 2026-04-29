"""`selvedge schema` — live-read DDL summary from sqlite_master."""

from __future__ import annotations

import re
import sqlite3

from .paths import db_path


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
            lines.append(
                f"| {c['name']} | {c['type']} | {c['notnull']} | "
                f"{c['dflt_value'] or ''} | {c['pk']} |"
            )
        lines.append("")
        sql = t["sql"] or ""
        for m in re.finditer(
            r"\b(\w+)\s+TEXT[^,]*?CHECK\s*\([^)]*?\1\s+IN\s*\(([^)]+)\)",
            sql,
            flags=re.IGNORECASE | re.DOTALL,
        ):
            col, vals = m.group(1), m.group(2)
            enum_vals = [v.strip().strip("'\"") for v in vals.split(",")]
            lines.append(f"- **{col}** admits: {', '.join(enum_vals)}")
        fks = conn.execute(f"PRAGMA foreign_key_list({t['name']})").fetchall()
        for fk in fks:
            lines.append(f"- FK `{fk['from']}` → `{fk['table']}({fk['to']})`")
        idx = conn.execute(
            "SELECT name, sql FROM sqlite_master WHERE type='index' AND tbl_name=? "
            "AND name NOT LIKE 'sqlite_autoindex_%' ORDER BY name",
            (t["name"],),
        ).fetchall()
        for i in idx:
            lines.append(f"- index `{i['name']}`")
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
