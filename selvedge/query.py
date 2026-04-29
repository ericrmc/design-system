"""`selvedge query` — read-only ad-hoc SQL for debugging."""

from __future__ import annotations

import json
import sqlite3

from .paths import db_path


def cmd_query(args) -> int:
    conn = sqlite3.connect(str(db_path()))
    conn.row_factory = sqlite3.Row
    rows = conn.execute(args.sql).fetchall()
    print(json.dumps([dict(r) for r in rows], indent=2 if args.pretty else None, default=str))
    conn.close()
    return 0
