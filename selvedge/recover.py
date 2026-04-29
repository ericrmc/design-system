"""`selvedge recover` — reclaim expired work_item leases (T-16 cleanup)."""

from __future__ import annotations

import json
import sys

from .connection import Conn
from .errors import SelvedgeError


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
