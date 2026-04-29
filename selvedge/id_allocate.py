"""`selvedge id-allocate` — allocate an `objects` row for a typed-row pk."""

from __future__ import annotations

import json
import sys

from .connection import Conn
from .errors import SelvedgeError


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
