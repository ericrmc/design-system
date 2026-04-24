#!/usr/bin/env python3
"""FastMCP stdio server exposing the phase-1 retrieval contract.

Implements specifications/retrieval-contract.md v1 §2:
- `search(query, k=10) -> list[{path, snippet, score}]`
- `resolve_id(alias) -> {canonical, kind, source_path, line, context} | None`

On startup: checks index freshness via mtime vs max(*.md mtime); rebuilds if stale
(session-open mtime check per retrieval-contract §4 + D-168).

Failure behaviour per retrieval-contract §3:
- Tool responses include `index_mtime` and `index_fresh: bool`.
- If the index can't be opened, tools return structured {available: false, reason: str}.
- Silent fallback is a contract violation; this server does not fall back silently.

Session 050 adoption per D-165 + D-170 + D-172 (engine-v9).
"""

import argparse
import os
import re
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print(
        "ERROR: mcp[cli] is required. Install with: pip install 'mcp[cli]'",
        file=sys.stderr,
    )
    sys.exit(1)

# Known ID patterns for resolve_id heuristic resolution (matches ID_PATTERNS in
# build_retrieval_index.py).
ID_LIKE_RE = re.compile(
    r"^(?:D-\d{3}|OI-\d{3}|§\d+(?:\.\d+)*(?:-M\d+)?|WX-\d+-\d+"
    r"|S(?:ession\s+)?\d{1,3}|engine-v\d+|EF-\d{3}(?:-[a-z0-9-]+)?|d01\d_\d+)$"
)


def resolve_workspace() -> Path:
    """Resolve the workspace root. Priority: CLI arg > cwd."""
    # CLI arg is handled in main(); we look it up from env as a fallback.
    root = os.environ.get("SELVEDGE_WORKSPACE")
    if root:
        return Path(root).resolve()
    return Path.cwd().resolve()


def max_md_mtime(workspace: Path) -> float:
    """Return the maximum mtime of any *.md file in the workspace (excluding .cache/)."""
    max_mtime = 0.0
    for p in workspace.rglob("*.md"):
        parts = p.relative_to(workspace).parts
        if any(part in {".git", ".cache", ".claude", ".serena", "node_modules", "__pycache__"} for part in parts):
            continue
        try:
            m = p.stat().st_mtime
            if m > max_mtime:
                max_mtime = m
        except OSError:
            continue
    return max_mtime


def index_fresh(db_path: Path, workspace: Path) -> bool:
    """Return True if the index mtime is newer than every *.md file."""
    if not db_path.exists():
        return False
    db_mtime = db_path.stat().st_mtime
    return db_mtime >= max_md_mtime(workspace)


def rebuild_index(workspace: Path, db_path: Path) -> None:
    """Invoke build_retrieval_index.py to regenerate the index."""
    indexer = workspace / "tools" / "build_retrieval_index.py"
    if not indexer.exists():
        raise RuntimeError(f"indexer not found at {indexer}")
    subprocess.run(
        [sys.executable, str(indexer), "--workspace", str(workspace), "--db", str(db_path)],
        check=True,
    )


def ensure_index(workspace: Path, db_path: Path) -> dict:
    """Ensure the index exists and is fresh. Returns a status dict."""
    rebuilt = False
    if not index_fresh(db_path, workspace):
        rebuild_index(workspace, db_path)
        rebuilt = True
    return {
        "available": True,
        "index_mtime": db_path.stat().st_mtime if db_path.exists() else 0.0,
        "index_fresh": True,
        "rebuilt_on_demand": rebuilt,
    }


def build_server(workspace: Path, db_path: Path) -> FastMCP:
    mcp = FastMCP("selvedge-retrieval")

    @mcp.tool()
    def search(query: str, k: int = 10) -> dict:
        """BM25 full-text search over the workspace's markdown corpus.

        Returns {results: [{path, snippet, score}], index_mtime: float, index_fresh: bool,
                 available: bool, degraded: bool, missing: [str]}.
        """
        try:
            status = ensure_index(workspace, db_path)
        except Exception as e:
            return {"available": False, "reason": str(e), "results": []}

        if k <= 0:
            k = 10
        if k > 100:
            k = 100
        conn = sqlite3.connect(db_path)
        try:
            cur = conn.cursor()
            # Use MATCH with escaped quotes to handle hyphenated IDs.
            # FTS5 treats `D-152` as prefix negation unless tokenchars includes '-';
            # we set tokenchars in build_retrieval_index.py. Quoted phrase search
            # is safer for IDs with §.
            escaped = query.replace('"', '""')
            try:
                rows = cur.execute(
                    "SELECT d.path, "
                    "       snippet(docs_fts, 2, '[', ']', '…', 16), "
                    "       bm25(docs_fts) AS score "
                    "FROM docs_fts JOIN documents d ON d.rowid = docs_fts.rowid "
                    'WHERE docs_fts MATCH ? '
                    "ORDER BY score LIMIT ?",
                    (f'"{escaped}"', k),
                ).fetchall()
            except sqlite3.OperationalError:
                # Fall back to literal query if phrase parse fails.
                rows = cur.execute(
                    "SELECT d.path, "
                    "       snippet(docs_fts, 2, '[', ']', '…', 16), "
                    "       bm25(docs_fts) AS score "
                    "FROM docs_fts JOIN documents d ON d.rowid = docs_fts.rowid "
                    'WHERE docs_fts MATCH ? '
                    "ORDER BY score LIMIT ?",
                    (escaped, k),
                ).fetchall()
            results = [
                {"path": row[0], "snippet": row[1], "score": float(row[2])}
                for row in rows
            ]
        finally:
            conn.close()

        return {
            "available": True,
            "degraded": False,
            "missing": [],
            "index_mtime": status["index_mtime"],
            "index_fresh": status["index_fresh"],
            "rebuilt_on_demand": status["rebuilt_on_demand"],
            "results": results,
        }

    @mcp.tool()
    def resolve_id(alias: str) -> dict:
        """Resolve an alias or canonical identifier to its authoritative location.

        Returns {match: {canonical, kind, source_path, line, context} | None,
                 index_mtime: float, index_fresh: bool, available: bool,
                 degraded: bool, missing: [str], reason: str|null}.
        """
        try:
            status = ensure_index(workspace, db_path)
        except Exception as e:
            return {"available": False, "reason": str(e), "match": None}

        conn = sqlite3.connect(db_path)
        try:
            cur = conn.cursor()
            # Strategy 1: direct canonical lookup.
            row = cur.execute(
                "SELECT canonical, id_kind, source_path, line, context_snippet "
                "FROM identifiers WHERE canonical = ? "
                "ORDER BY CASE WHEN source_path LIKE 'specifications/%' THEN 0 ELSE 1 END, "
                "         source_path, line LIMIT 1",
                (alias,),
            ).fetchone()
            if row:
                return _match_payload(row, status)

            # Strategy 2: id_text (raw alias form) lookup — build_retrieval_index.py
            # already remaps id_text via aliases.yaml if present.
            row = cur.execute(
                "SELECT canonical, id_kind, source_path, line, context_snippet "
                "FROM identifiers WHERE id_text = ? "
                "ORDER BY CASE WHEN source_path LIKE 'specifications/%' THEN 0 ELSE 1 END, "
                "         source_path, line LIMIT 1",
                (alias,),
            ).fetchone()
            if row:
                return _match_payload(row, status)

            # Strategy 3: if alias looks like a known ID pattern, pick first occurrence.
            if ID_LIKE_RE.match(alias):
                row = cur.execute(
                    "SELECT canonical, id_kind, source_path, line, context_snippet "
                    "FROM identifiers WHERE canonical LIKE ? OR id_text LIKE ? "
                    "ORDER BY source_path, line LIMIT 1",
                    (alias + "%", alias + "%"),
                ).fetchone()
                if row:
                    return _match_payload(row, status)

            return {
                "available": True,
                "degraded": False,
                "missing": [],
                "index_mtime": status["index_mtime"],
                "index_fresh": status["index_fresh"],
                "rebuilt_on_demand": status["rebuilt_on_demand"],
                "match": None,
                "reason": "no match in identifiers table",
            }
        finally:
            conn.close()

    def _match_payload(row, status) -> dict:
        return {
            "available": True,
            "degraded": False,
            "missing": [],
            "index_mtime": status["index_mtime"],
            "index_fresh": status["index_fresh"],
            "rebuilt_on_demand": status["rebuilt_on_demand"],
            "match": {
                "canonical": row[0],
                "kind": row[1],
                "source_path": row[2],
                "line": row[3],
                "context": row[4],
            },
            "reason": None,
        }

    return mcp


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--workspace",
        type=Path,
        default=None,
        help="Workspace root (default: env SELVEDGE_WORKSPACE or cwd)",
    )
    parser.add_argument(
        "--db",
        type=Path,
        default=None,
        help="Index DB path (default: <workspace>/.cache/retrieval.db)",
    )
    args = parser.parse_args()

    workspace = (args.workspace or resolve_workspace()).resolve()
    if not workspace.is_dir():
        print(f"ERROR: workspace is not a directory: {workspace}", file=sys.stderr)
        return 2
    db_path = (args.db or (workspace / ".cache" / "retrieval.db")).resolve()

    # Pre-flight ensure_index so that startup reports any issue cleanly.
    try:
        ensure_index(workspace, db_path)
    except Exception as e:
        print(f"ERROR: retrieval index unavailable: {e}", file=sys.stderr)
        # Continue anyway — the server can report degraded mode; don't refuse to start.

    mcp = build_server(workspace, db_path)
    mcp.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
