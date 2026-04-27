#!/usr/bin/env python3
"""PreToolUse hook: refuse Edit/Write to substrate-canonical markdown.

Resolves OI-085-002 (engine-v24): structural restriction of markdown authoring.

Path A (engine-v20+) makes the SQLite substrate the canonical source for
session state, specifications, issues, and prompts. The corresponding
markdown files under provenance/, specifications/, prompts/, open-issues/
are generated exports — editing them directly bypasses the substrate and
silently desynchronises.

This hook reads Claude Code's PreToolUse JSON event from stdin, inspects
the tool name and tool_input.file_path, and refuses (exit 2 with stderr
explaining why) when a tracked path is targeted. The escape hatch is
SELVEDGE_EXPORT_CONTEXT=1 in the environment: an authorised exporter sets
this so generated writes still land. The four CLI-driven export paths
(`bin/selvedge export`) write via in-process Python file IO, not via
Claude's Edit/Write tools, so they are unaffected by this hook.

Exit codes:
  0 — allow (path not tracked, or escape flag set, or non-Edit/Write tool)
  2 — refuse (Claude is shown the stderr message)
  1 — internal error parsing input (allow with stderr warning)

## Scope and known gaps

The hook intercepts Edit, Write, MultiEdit, and NotebookEdit. It cannot
intercept Bash-mediated writes (`echo > path`, `sed -i`, `python -c`,
etc.): the Bash `tool_input` is an opaque command string, and matching
every Bash invocation would defeat its scalability. Operator-policed
discipline applies for Bash. A future Bash-side guard would need to live
in a different surface (shell wrapper or sandboxed exec).

The escape flag is not workspace-scoped — if `SELVEDGE_EXPORT_CONTEXT=1`
is exported globally in the user's shell, the hook is silently disabled
for all sessions. To make accidental global export visible, the hook
prints a one-line stderr notice when the flag activates.

Outbound symlinks (a tracked-name path that resolves outside the
workspace) bypass the hook because `relative_to(WORKSPACE)` raises and
the path is treated as out-of-scope. This is acceptable: the hook
prevents Claude from accidentally writing tracked paths, not from a
deliberately-compromised working tree.
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]

# Substrate-canonical patterns (workspace-relative POSIX paths, fnmatch syntax).
# Use ** for recursive directories, * for a single segment.
TRACKED_PATTERNS: tuple[str, ...] = (
    "provenance/**/*.md",
    "specifications/*.md",
    "prompts/*.md",
    "open-issues/**/*.md",
)

# Tools the hook intercepts. Other tool calls fall through.
GUARDED_TOOLS: frozenset[str] = frozenset({"Edit", "Write", "MultiEdit", "NotebookEdit"})


def _glob_to_regex(pattern: str) -> re.Pattern[str]:
    """Translate a glob with `**` (zero-or-more path segments) and `*`
    (zero-or-more chars within a segment) into an anchored regex over POSIX
    paths. No other glob metacharacters are supported; the pattern set is
    closed (TRACKED_PATTERNS), not user input."""
    out: list[str] = []
    i = 0
    while i < len(pattern):
        c = pattern[i]
        if c == "*":
            if pattern[i:i + 3] == "**/":
                # ** as a directory segment: match zero or more segments
                # including the trailing slash, e.g. '', 'a/', 'a/b/'.
                out.append(r"(?:.*/)?")
                i += 3
                continue
            if pattern[i:i + 2] == "**":
                out.append(r".*")
                i += 2
                continue
            # single * matches anything except '/'
            out.append(r"[^/]*")
            i += 1
            continue
        out.append(re.escape(c))
        i += 1
    return re.compile("^" + "".join(out) + "$")


_COMPILED_PATTERNS = tuple(_glob_to_regex(p) for p in TRACKED_PATTERNS)


def _matches_tracked(rel_posix: str) -> bool:
    """Return True if a workspace-relative POSIX path is substrate-canonical."""
    return any(rx.match(rel_posix) for rx in _COMPILED_PATTERNS)


def _resolve_relative(file_path: str) -> str | None:
    """Resolve a tool-supplied file_path to a workspace-relative POSIX path,
    or None if the path is outside the workspace. Tool inputs may be
    absolute or relative; callers normalise either form."""
    p = Path(file_path)
    if not p.is_absolute():
        p = (WORKSPACE / p)
    try:
        rel = p.resolve().relative_to(WORKSPACE)
    except ValueError:
        return None
    return rel.as_posix()


def main() -> int:
    # Escape hatch: authorised exporter sets SELVEDGE_EXPORT_CONTEXT=1.
    # Log to stderr so accidental global export of the flag is visible in
    # transcripts; without this, the guard would be silently disabled.
    if os.environ.get("SELVEDGE_EXPORT_CONTEXT") == "1":
        print(
            "refuse-substrate-md: SELVEDGE_EXPORT_CONTEXT=1; bypassing substrate-md guard",
            file=sys.stderr,
        )
        return 0

    raw = sys.stdin.read()
    if not raw:
        return 0
    try:
        event = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"refuse-substrate-md: malformed PreToolUse JSON ({exc}); allowing", file=sys.stderr)
        return 0

    tool_name = event.get("tool_name", "")
    if tool_name not in GUARDED_TOOLS:
        return 0

    tool_input = event.get("tool_input") or {}
    # Edit/Write/MultiEdit/NotebookEdit all use file_path / notebook_path.
    file_path = tool_input.get("file_path") or tool_input.get("notebook_path")
    if not file_path:
        return 0

    rel = _resolve_relative(file_path)
    if rel is None:
        return 0

    if not _matches_tracked(rel):
        return 0

    print(
        f"refuse-substrate-md: refusing {tool_name} on {rel}\n"
        f"  This file is a substrate-canonical export. Direct authoring desynchronises\n"
        f"  the markdown from the SQLite substrate (Path A, engine-v20+). Resolve via:\n"
        f"    - submit the change through bin/selvedge (e.g., spec-version, issue, decision-record)\n"
        f"    - regenerate via `bin/selvedge export ... --write`\n"
        f"  Bypass (only when materialising from substrate): set SELVEDGE_EXPORT_CONTEXT=1.\n"
        f"  Provenance: OI-085-002 (engine-v24).",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
