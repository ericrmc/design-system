"""Single-writer connection wrapper with BEGIN IMMEDIATE write_tx + retry."""

from __future__ import annotations

import sqlite3
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from .errors import SelvedgeError, _refusal_from_sqlite
from .paths import DEFAULT_BUSY_TIMEOUT_MS, DEFAULT_RETRY_BASE_MS, DEFAULT_RETRY_BUDGET, db_path


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
