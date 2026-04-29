"""Structured error type and SQLite refusal classifier."""

from __future__ import annotations

import re
import sqlite3


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
