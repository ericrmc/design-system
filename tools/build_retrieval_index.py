#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Build the retrieval index at .cache/retrieval.db for the current workspace.

Implements the phase-1 contract in specifications/retrieval-contract.md v1:
- `documents` table (one row per *.md file; body + title + frontmatter_json).
- `identifiers` table (one row per ID occurrence).
- `docs_fts` FTS5 virtual table over documents.body + title.

Session 050 adoption per D-165 + D-172 (engine-v9).

Standalone: python3 tools/build_retrieval_index.py [--workspace PATH]
"""

import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

# ID extraction patterns. Centralised registry; phase-2 may extend.
ID_PATTERNS = {
    "decision": re.compile(r"\bD-\d{3}\b"),
    "open-issue": re.compile(r"\bOI-\d{3}\b"),
    "minority": re.compile(r"§\d+(?:\.\d+)*(?:-M\d+)?"),
    "watchpoint": re.compile(r"\bWX-\d+-\d+\b"),
    "session": re.compile(r"\bS(?:ession\s+)?(\d{3})\b"),
    "engine-version": re.compile(r"\bengine-v\d+\b"),
    "feedback": re.compile(r"\bEF-\d{3}(?:-[a-z0-9-]+)?\b"),
    "trigger": re.compile(r"\bd01\d_\d+\b"),
}

# Directory exclusions (relative to workspace root).
EXCLUDE_DIRS = {".git", ".cache", ".claude", ".serena", "node_modules", "__pycache__", ".git-hooks"}

# File exclusions (filename patterns).
SUPERSEDED_SPEC_RE = re.compile(r".*-v\d+\.md$")


def classify_kind(path: Path, workspace: Path) -> str:
    """Classify a markdown file by its path within the workspace."""
    rel = path.relative_to(workspace)
    parts = rel.parts
    if parts[0] == "specifications":
        return "spec"
    if parts[0] == "provenance":
        return "provenance"
    if parts[0] == "open-issues":
        return "open-issue"
    if parts[0] == "engine-feedback":
        return "engine-feedback"
    if parts[0] == "applications":
        return "application"
    if parts[0] == "prompts":
        return "prompt"
    if parts[0] == "tools":
        return "tool"
    # Records substrate (added engine-v10 per S058 D-200; records-contract.md v1).
    # Per-family records are first-class retrieval objects: kind = "record-<family>".
    if parts[0] == "records" and len(parts) >= 2:
        family = parts[1]
        return f"record-{family}"
    return "root"


SESSION_PATH_RE = re.compile(r"provenance/(\d{3})-")
RECORDS_SESSION_PATH_RE = re.compile(r"records/sessions/S(\d{3})\.md$")


def extract_session(path: Path, workspace: Path) -> int | None:
    """Extract session number from path, if applicable."""
    rel_str = str(path.relative_to(workspace))
    m = SESSION_PATH_RE.search(rel_str)
    if m:
        return int(m.group(1))
    # Records substrate session records (added engine-v10 per S058 D-200).
    m2 = RECORDS_SESSION_PATH_RE.search(rel_str)
    if m2:
        return int(m2.group(1))
    return None


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)", re.DOTALL)


def parse_markdown(path: Path) -> tuple[dict, str, str]:
    """Parse frontmatter + body from a markdown file. Returns (frontmatter, title, body)."""
    text = path.read_text(encoding="utf-8", errors="replace")
    frontmatter: dict = {}
    body = text
    title = ""
    m = FRONTMATTER_RE.match(text)
    if m:
        try:
            frontmatter = yaml.safe_load(m.group(1)) or {}
            if not isinstance(frontmatter, dict):
                frontmatter = {}
        except yaml.YAMLError:
            frontmatter = {}
        body = m.group(2)
    # Title: frontmatter['title'] if present, else first H1, else empty.
    if isinstance(frontmatter.get("title"), str):
        title = frontmatter["title"]
    else:
        for line in body.splitlines():
            line = line.strip()
            if line.startswith("# "):
                title = line[2:].strip()
                break
    return frontmatter, title, body


def extract_identifiers(body: str, source_path: str) -> list[tuple[str, str, str, str, int, str]]:
    """Extract all ID occurrences. Returns [(id_text, id_kind, canonical, source_path, line, context)]."""
    rows: list[tuple[str, str, str, str, int, str]] = []
    lines = body.splitlines()
    for idx, line in enumerate(lines, start=1):
        for kind, pattern in ID_PATTERNS.items():
            for match in pattern.finditer(line):
                id_text = match.group(0)
                # Session kind normalises to three-digit canonical
                if kind == "session":
                    num = match.group(1)
                    canonical = f"S{num}"
                else:
                    canonical = id_text
                context = line.strip()[:120]
                rows.append((id_text, kind, canonical, source_path, idx, context))
    return rows


def load_aliases(workspace: Path) -> list[tuple[str, str, str]]:
    """Load specifications/aliases.yaml. Returns [(alias, canonical, kind)]."""
    aliases_path = workspace / "specifications" / "aliases.yaml"
    if not aliases_path.exists():
        return []
    try:
        data = yaml.safe_load(aliases_path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError:
        return []
    rows: list[tuple[str, str, str]] = []
    for entry in data.get("aliases", []) or []:
        if not isinstance(entry, dict):
            continue
        canonical = entry.get("canonical")
        kind = entry.get("kind", "other")
        aliases_list = entry.get("aliases", []) or []
        if not canonical:
            continue
        for a in aliases_list:
            if isinstance(a, str):
                rows.append((a, canonical, kind))
    return rows


def walk_markdown(workspace: Path) -> list[Path]:
    """Walk workspace for *.md, excluding configured dirs and superseded specs."""
    files: list[Path] = []
    for p in workspace.rglob("*.md"):
        if any(part in EXCLUDE_DIRS for part in p.relative_to(workspace).parts):
            continue
        if SUPERSEDED_SPEC_RE.match(p.name):
            continue
        files.append(p)
    return sorted(files)


def build_index(workspace: Path, db_path: Path) -> dict:
    """Build the index. Returns a stats dict."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.executescript("""
        CREATE TABLE documents (
          path TEXT PRIMARY KEY,
          kind TEXT NOT NULL,
          session INTEGER,
          mtime REAL NOT NULL,
          title TEXT,
          frontmatter_json TEXT,
          body TEXT NOT NULL
        );
        CREATE INDEX idx_docs_kind ON documents(kind);
        CREATE INDEX idx_docs_session ON documents(session);

        CREATE TABLE identifiers (
          id_text TEXT NOT NULL,
          id_kind TEXT NOT NULL,
          canonical TEXT NOT NULL,
          source_path TEXT NOT NULL,
          line INTEGER,
          context_snippet TEXT,
          PRIMARY KEY (id_text, id_kind, source_path, line)
        );
        CREATE INDEX idx_ids_canonical ON identifiers(canonical, id_kind);
        CREATE INDEX idx_ids_source ON identifiers(source_path);

        CREATE VIRTUAL TABLE docs_fts USING fts5(
          path UNINDEXED, title, body,
          content='documents', content_rowid='rowid',
          tokenize='porter unicode61 tokenchars ''-_§'''
        );

        CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
    """)

    files = walk_markdown(workspace)
    id_rows: list[tuple[str, str, str, str, int, str]] = []
    for path in files:
        rel = str(path.relative_to(workspace))
        frontmatter, title, body = parse_markdown(path)
        kind = classify_kind(path, workspace)
        session = extract_session(path, workspace)
        mtime = path.stat().st_mtime
        fm_json = json.dumps(frontmatter, default=str)
        cur.execute(
            "INSERT INTO documents(path, kind, session, mtime, title, frontmatter_json, body) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (rel, kind, session, mtime, title, fm_json, body),
        )
        id_rows.extend(extract_identifiers(body, rel))

    # Dedupe identifiers by primary key to avoid integrity errors.
    seen: set[tuple[str, str, str, int]] = set()
    for row in id_rows:
        key = (row[0], row[1], row[3], row[4])
        if key in seen:
            continue
        seen.add(key)
        cur.execute(
            "INSERT INTO identifiers(id_text, id_kind, canonical, source_path, line, context_snippet) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            row,
        )

    # Apply alias overrides to canonical form.
    alias_rows = load_aliases(workspace)
    for alias, canonical, _kind in alias_rows:
        cur.execute(
            "UPDATE identifiers SET canonical = ? WHERE id_text = ?",
            (canonical, alias),
        )

    # Rebuild FTS from the content table.
    cur.execute("INSERT INTO docs_fts(docs_fts) VALUES('rebuild')")

    # Record meta.
    workspace_root = str(workspace.resolve())
    cur.execute("INSERT INTO meta(key, value) VALUES('schema_version', '1')")
    cur.execute("INSERT INTO meta(key, value) VALUES('workspace_root', ?)", (workspace_root,))
    cur.execute("INSERT INTO meta(key, value) VALUES('built_by', 'tools/build_retrieval_index.py')")

    conn.commit()
    cur.execute("VACUUM")
    cur.execute("PRAGMA integrity_check")

    # Stats.
    doc_count = cur.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
    id_count = cur.execute("SELECT COUNT(*) FROM identifiers").fetchone()[0]
    conn.close()

    return {
        "workspace": workspace_root,
        "db_path": str(db_path),
        "documents": doc_count,
        "identifiers": id_count,
        "files_scanned": len(files),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--workspace",
        type=Path,
        default=Path.cwd(),
        help="Workspace root (default: current working directory)",
    )
    parser.add_argument(
        "--db",
        type=Path,
        default=None,
        help="Output DB path (default: <workspace>/.cache/retrieval.db)",
    )
    args = parser.parse_args()

    workspace = args.workspace.resolve()
    if not workspace.is_dir():
        print(f"ERROR: workspace is not a directory: {workspace}", file=sys.stderr)
        return 2
    db_path = (args.db or (workspace / ".cache" / "retrieval.db")).resolve()

    stats = build_index(workspace, db_path)
    print(
        f"Retrieval index built: {stats['db_path']}\n"
        f"  documents: {stats['documents']}\n"
        f"  identifiers: {stats['identifiers']}\n"
        f"  files scanned: {stats['files_scanned']}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
