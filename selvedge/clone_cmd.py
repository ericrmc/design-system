"""`selvedge clone-substrate` — create a transient substrate clone for subagent dispatch.

L2b layer of substrate-loss-defense (DV-S081-1, OI-S081-2). The orchestrator
runs this before dispatching a subagent that needs substrate access; the
emitted path is then handed to the subagent via SELVEDGE_DB_PATH=<path> in
the subagent prompt. Destructive ops the subagent runs (e.g. an accidental
``selvedge init --force --really-force``) affect the clone, never the primary.

The clone is a complete, transaction-consistent copy via
``sqlite3.Connection.backup()`` — the same page-aware machinery the L3
boundary snapshots use. The clone is NOT recorded in ``snapshot_catalog``
because it is a transient scratch surface, not a durable recovery artefact.

**Cleanup posture.** Clones land in the system tempdir by default. The
orchestrator should ``rm -f $CLONE`` immediately after the subagent
returns. The default tempdir IS subject to OS-level reclamation policies
(macOS purges /var/folders periodically; Linux reclaims /tmp on tmpfs
remount or per ``systemd-tmpfiles``) — a clone left behind is therefore
durability-undefined. If a clone must survive across an OS reboot or a
long subagent window, pass ``--to <persistent-path>`` to land the clone
under an orchestrator-controlled directory instead.

Refusal shape mirrors ``selvedge restore``:

- ``--to`` resolving to the live primary is refused (E_LIVE_PRIMARY).
- A missing source primary is refused (E_NO_SOURCE).
- A symlinked ``--to`` that resolves to the primary is refused via
  ``Path.resolve()`` canonicalisation.

Output: the clone path on stdout (one line, suitable for command substitution
``CLONE=$(bin/selvedge clone-substrate)``), human-readable detail on stderr.
"""

from __future__ import annotations

import os
import sqlite3
import sys
import tempfile
from pathlib import Path

from .paths import db_path


def cmd_clone_substrate(args) -> int:
    src = db_path().resolve()
    if not src.exists():
        print(
            f"refused: E_NO_SOURCE — primary substrate {src} does not exist; "
            f"run `bin/selvedge init` first.",
            file=sys.stderr,
        )
        return 2

    if args.to:
        dst = Path(args.to).resolve()
        if dst == src:
            print(
                f"refused: E_LIVE_PRIMARY — refusing to clone over the live "
                f"primary substrate at {dst}. The clone must land at a "
                f"distinct path.",
                file=sys.stderr,
            )
            return 2
        dst.parent.mkdir(parents=True, exist_ok=True)
    else:
        # Use mkstemp to atomically reserve a unique path. Close the fd
        # immediately; sqlite3.connect() reopens the file. The file remains
        # on disk under the orchestrator's responsibility for cleanup.
        fd, dst_str = tempfile.mkstemp(
            prefix="selvedge-subagent-clone-",
            suffix=".sqlite",
        )
        os.close(fd)
        dst = Path(dst_str).resolve()

    # Unlink any stale WAL/SHM sidecars at dst so the clone is not blended
    # with leftover bytes from a prior connection at the same path. Mirrors
    # the same defence in `restore`.
    for sidecar in [
        dst.with_name(dst.name + "-wal"),
        dst.with_name(dst.name + "-shm"),
    ]:
        if sidecar.exists():
            try:
                sidecar.unlink()
            except OSError as e:
                print(
                    f"warning: could not unlink stale sidecar {sidecar}: {e}",
                    file=sys.stderr,
                )

    try:
        src_conn = sqlite3.connect(f"file:{src}?mode=ro", uri=True)
    except sqlite3.Error as e:
        print(f"refused: cannot open source {src}: {e}", file=sys.stderr)
        return 2
    try:
        try:
            dst_conn = sqlite3.connect(str(dst))
            try:
                src_conn.backup(dst_conn)
            finally:
                dst_conn.close()
        except sqlite3.Error as e:
            print(f"refused: clone failed {src} -> {dst}: {e}", file=sys.stderr)
            if dst.exists():
                try:
                    dst.unlink()
                except OSError:
                    pass
            return 2
    finally:
        src_conn.close()

    size = dst.stat().st_size
    print(str(dst))
    print(
        f"cloned: {src} -> {dst} ({size} bytes)\n"
        f"  hand to subagent via: SELVEDGE_DB_PATH={dst} bin/selvedge ...\n"
        f"  cleanup: orchestrator should `rm -f` after subagent returns;\n"
        f"           default tempdir is subject to OS-level reclamation,\n"
        f"           pass --to <persistent-path> if durability matters.",
        file=sys.stderr,
    )
    return 0
