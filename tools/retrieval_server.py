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

try:
    import yaml
except ImportError:
    yaml = None  # aliases.yaml support becomes degraded if pyyaml is absent

# Known ID patterns for resolve_id heuristic resolution (matches ID_PATTERNS in
# build_retrieval_index.py).
ID_LIKE_RE = re.compile(
    r"^(?:D-\d{3}|OI-\d{3}|§\d+(?:\.\d+)*(?:-M\d+)?|WX-\d+-\d+"
    r"|S(?:ession\s+)?\d{1,3}|engine-v\d+|EF-\d{3}(?:-[a-z0-9-]+)?|d01\d_\d+)$"
)

# ID patterns recognised inside a search() query string. Used by _sanitize_query
# to wrap hyphenated identifiers in phrase quotes before FTS5 sees them, so
# `D-129` tokenises atomically rather than being parsed as `D NOT 129`.
# Per Session 054 D-186 (EF-053 resolution, Direction A).
_ID_TOKEN_RE = re.compile(
    r'(?<!")'
    r"("
    r"D-\d{3}"
    r"|OI-\d{3}"
    r"|WX-\d+-\d+"
    r"|EF-\d{3}(?:-[a-z0-9-]+)?"
    r"|engine-v\d+"
    r"|§\d+(?:\.\d+)*(?:-M\d+)?"
    r"|d01\d_\d+"
    r")"
    r'(?!")'
)


def _sanitize_query(query: str) -> str:
    """Wrap recognised hyphenated identifier patterns in FTS5 phrase quotes.

    SQLite FTS5's query parser treats unquoted hyphens as the NOT operator,
    so `D-129 standing` is parsed as `D NOT 129 standing` and crashes with
    `no such column: 129`. Wrapping recognised ID patterns in phrase quotes
    sidesteps this without forcing the entire query into a single phrase
    (which would lose multi-word BM25 ranking).

    Idempotent: identifiers already adjacent to `"` are left alone via
    lookbehind/lookahead. Identifiers outside the curated pattern set are
    not wrapped; the caller can phrase-quote them manually if needed.

    Per `specifications/retrieval-contract.md` v1 §2.1: "Tokenisation MUST
    treat hyphen, underscore, and § as word-internal so that IDs ...
    tokenise atomically rather than splitting." Per Session 054 D-186
    (EF-053 resolution, Direction A: query-sanitization at server level).
    """
    return _ID_TOKEN_RE.sub(r'"\1"', query)


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


def load_aliases_map(workspace: Path) -> dict:
    """Load specifications/aliases.yaml into {alias: canonical} for query-time resolution.

    Implements retrieval-contract.md v1 §2.2 clause:
      "If `alias` matches an `aliases[]` entry in `specifications/aliases.yaml`,
       resolves to the corresponding canonical."

    Per Session 052 D-181 (EF-051 resolution, Direction B: query-time aliases
    consultation). Returns empty dict if aliases.yaml is absent, malformed, or
    pyyaml is unavailable (degraded mode; surface via resolve_id payload).
    """
    if yaml is None:
        return {}
    aliases_path = workspace / "specifications" / "aliases.yaml"
    if not aliases_path.exists():
        return {}
    try:
        data = yaml.safe_load(aliases_path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError:
        return {}
    out: dict = {}
    for entry in data.get("aliases", []) or []:
        if not isinstance(entry, dict):
            continue
        canonical = entry.get("canonical")
        if not canonical:
            continue
        for a in entry.get("aliases", []) or []:
            if isinstance(a, str) and a:
                out[a] = canonical
    return out


def build_server(workspace: Path, db_path: Path) -> FastMCP:
    mcp = FastMCP("selvedge-retrieval")

    # Alias map loaded once at startup per retrieval-contract.md v1 §2.2 +
    # Session 052 D-181 (Direction B). `resolve_id` consults this before
    # id_text lookup so aliases.yaml is authoritative at query time without
    # requiring index rebuild when the file changes. Re-load requires server
    # restart (consistent with mtime-rebuild semantics for the DB itself).
    aliases_map = load_aliases_map(workspace)
    aliases_available = yaml is not None
    aliases_path = workspace / "specifications" / "aliases.yaml"
    aliases_present = aliases_path.exists()

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
            # FTS5 treats unquoted `-` as the NOT operator, so a query like
            # `D-129 standing` would be parsed as `D NOT 129 standing` and
            # raise "no such column: 129". _sanitize_query wraps recognised
            # ID patterns in phrase quotes so they tokenise atomically.
            # Per Session 054 D-186 (EF-053 resolution, Direction A).
            sanitized = _sanitize_query(query)
            try:
                rows = cur.execute(
                    "SELECT d.path, "
                    "       snippet(docs_fts, 2, '[', ']', '…', 16), "
                    "       bm25(docs_fts) AS score "
                    "FROM docs_fts JOIN documents d ON d.rowid = docs_fts.rowid "
                    'WHERE docs_fts MATCH ? '
                    "ORDER BY score LIMIT ?",
                    (sanitized, k),
                ).fetchall()
            except sqlite3.OperationalError:
                # Last-ditch: wrap the original query as a single phrase. May
                # lose multi-word BM25 ranking but avoids hard crash for
                # hyphenated forms not covered by _ID_TOKEN_RE.
                escaped = query.replace('"', '""')
                rows = cur.execute(
                    "SELECT d.path, "
                    "       snippet(docs_fts, 2, '[', ']', '…', 16), "
                    "       bm25(docs_fts) AS score "
                    "FROM docs_fts JOIN documents d ON d.rowid = docs_fts.rowid "
                    'WHERE docs_fts MATCH ? '
                    "ORDER BY score LIMIT ?",
                    (f'"{escaped}"', k),
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

        # Degraded-mode disclosure per retrieval-contract.md v1 §3 clause 3.
        missing: list[str] = []
        if not aliases_available:
            missing.append("pyyaml")
        if not aliases_present:
            missing.append("specifications/aliases.yaml")
        degraded = bool(missing)

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
                return _match_payload(row, status, degraded, missing)

            # Strategy 1.5: query-time aliases.yaml consultation (D-181, Direction B).
            # If the alias is declared in aliases.yaml, resolve its canonical via
            # the same direct-canonical lookup as Strategy 1. Implements
            # retrieval-contract.md v1 §2.2 second clause.
            resolved_canonical = aliases_map.get(alias)
            if resolved_canonical and resolved_canonical != alias:
                row = cur.execute(
                    "SELECT canonical, id_kind, source_path, line, context_snippet "
                    "FROM identifiers WHERE canonical = ? "
                    "ORDER BY CASE WHEN source_path LIKE 'specifications/%' THEN 0 ELSE 1 END, "
                    "         source_path, line LIMIT 1",
                    (resolved_canonical,),
                ).fetchone()
                if row:
                    return _match_payload(row, status, degraded, missing)

            # Strategy 2: id_text (raw alias form) lookup — build_retrieval_index.py
            # UPDATE only remaps rows whose id_text already matches an ID_PATTERNS
            # regex, so non-regex aliases (handled by Strategy 1.5 above) never
            # land here. Kept for canonicals whose surface form matches regex but
            # not the canonical column directly.
            row = cur.execute(
                "SELECT canonical, id_kind, source_path, line, context_snippet "
                "FROM identifiers WHERE id_text = ? "
                "ORDER BY CASE WHEN source_path LIKE 'specifications/%' THEN 0 ELSE 1 END, "
                "         source_path, line LIMIT 1",
                (alias,),
            ).fetchone()
            if row:
                return _match_payload(row, status, degraded, missing)

            # Strategy 3: if alias looks like a known ID pattern, pick first occurrence.
            if ID_LIKE_RE.match(alias):
                row = cur.execute(
                    "SELECT canonical, id_kind, source_path, line, context_snippet "
                    "FROM identifiers WHERE canonical LIKE ? OR id_text LIKE ? "
                    "ORDER BY source_path, line LIMIT 1",
                    (alias + "%", alias + "%"),
                ).fetchone()
                if row:
                    return _match_payload(row, status, degraded, missing)

            return {
                "available": True,
                "degraded": degraded,
                "missing": missing,
                "index_mtime": status["index_mtime"],
                "index_fresh": status["index_fresh"],
                "rebuilt_on_demand": status["rebuilt_on_demand"],
                "match": None,
                "reason": "no match in identifiers table or aliases.yaml",
            }
        finally:
            conn.close()

    def _match_payload(row, status, degraded: bool = False, missing: list | None = None) -> dict:
        return {
            "available": True,
            "degraded": degraded,
            "missing": missing or [],
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

    @mcp.tool()
    def forward_references(target: str) -> dict:
        """Return every line-precise occurrence of `target` in the identifiers index.

        Unlike `resolve_id` (returns the first occurrence; §2.2) and `search`
        (BM25-ranked over document bodies; §2.1), this tool returns the full
        line-precise list of occurrences across the corpus. Useful for
        session-open commitment audit ("what did prior sessions schedule for
        this session?"), forward-reference enumeration, and any "all
        occurrences" query that the §2.1/§2.2 surface cannot answer.

        Returns `{results: [{path, line, context, kind}], count, ...}`,
        sorted by `source_path` then `line` for deterministic output. Empty
        results (count=0) for unindexed targets — never raises on unknown
        target.

        Per Session 054 D-187 (EF-054 resolution, Direction A:
        forward_references MCP tool). Phase-1-compatible additive extension;
        the contract names `search` + `resolve_id` as required minimum at
        phase-1 (§2) and additional tools are permitted.
        """
        try:
            status = ensure_index(workspace, db_path)
        except Exception as e:
            return {
                "available": False,
                "reason": str(e),
                "results": [],
                "count": 0,
            }

        conn = sqlite3.connect(db_path)
        try:
            cur = conn.cursor()
            rows = cur.execute(
                "SELECT source_path, line, context_snippet, id_kind "
                "FROM identifiers WHERE id_text = ? OR canonical = ? "
                "ORDER BY source_path, line",
                (target, target),
            ).fetchall()
            results = [
                {
                    "path": row[0],
                    "line": row[1],
                    "context": row[2],
                    "kind": row[3],
                }
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
            "count": len(results),
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
