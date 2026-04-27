#!/usr/bin/env python3
# /// script
# dependencies = ["pyyaml>=6.0"]
# ///
"""
Digest emitter — CM1 capture-adapter (Claude Code PostToolUse hook).

Reads a Claude Code hook event from stdin (JSON) and appends a substrate-call
record to provenance/<NNN-session>/harness-telemetry-digest.yaml per the SCD-3
schema codified in specifications/validation-approach.md v9 §(z6).

Hook configuration: PostToolUse only (per Session 075 D-296 + .claude/settings.json).
PreToolUse is intentionally NOT configured: PostToolUse fires after tool execution
and carries the tool_response field for status determination, so a PreToolUse pair
would only produce duplicate records.

Per `validation-approach.md` v9 §(z6) + S073 D-275 (γ-6) staged hybrid + S073
D-276 capture-mechanism CM1 + S073 D-277 SCD-3 schema + §10.4-M34 P4
z-laundering-1 measurement-authority-not-inherited reframe (per-section
field-level authority). The hook script writes harness-measured records with
producer_kind=harness-measured + authority_level=primary at the per-record
level; file-level frontmatter does not promote agent-declared records.

Capture capabilities (this adapter):
  - tool_name
  - tool_input_summary (truncated; not full transcript per privacy)
  - tool_result_status (success | error)
  - timestamp_iso8601 (harness clock at hook invocation)

Unobserved fields (not captured by this adapter; carried forward as
unobserved_fields per portability discipline):
  - wall_clock_token_count (Claude Code hook event does not surface tokens)
  - reviewer_invocation_wall_clock_seconds (out-of-scope for tool-call hook)

Engine-v15 per Session 075 D-296 + D-298 (γ-6) phase-3.1 implementation.

Idempotency: digest file is line-appended; concurrent hook firings are
serialised by single-writer assumption (Claude Code fires hooks
sequentially per session).

Failure mode: any exception is caught and the script exits 0 with a stderr
warning. Hook failures must NOT block the orchestrator's tool calls per
validator-as-evidence-consumer discipline (§10.4-M33 P3 z9): the digest is
evidence-when-present, not a precondition.
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
PROVENANCE_DIR = WORKSPACE_ROOT / "provenance"
ADAPTER_NAME = "claude-code-hook"
ADAPTER_VERSION = "v1"
SCHEMA_VERSION = "SCD-3"

SUBSTRATE_TOOL_PREFIXES = (
    "mcp__selvedge-retrieval__",
)


def current_session_dir() -> Path | None:
    """Return path to most-recent provenance/NNN-session/ directory, or None."""
    if not PROVENANCE_DIR.is_dir():
        return None
    candidates = [d for d in PROVENANCE_DIR.iterdir() if d.is_dir() and d.name[:3].isdigit()]
    if not candidates:
        return None
    return max(candidates, key=lambda d: d.name)


def truncate(s: str, limit: int = 200) -> str:
    if len(s) <= limit:
        return s
    return s[:limit] + "..."


def collapse_whitespace(s: str) -> str:
    """Collapse internal whitespace runs to single space — keep summaries one-line."""
    return " ".join(s.split())


def summarise_input(tool_name: str, tool_input: dict) -> str:
    """Build a small input summary; do not commit full file contents."""
    if not isinstance(tool_input, dict):
        return collapse_whitespace(truncate(str(tool_input)))
    keys = sorted(tool_input.keys())
    parts = []
    for k in keys:
        v = tool_input[k]
        if isinstance(v, str):
            parts.append(f"{k}={truncate(collapse_whitespace(v), 80)}")
        elif isinstance(v, (int, float, bool)) or v is None:
            parts.append(f"{k}={v}")
        else:
            parts.append(f"{k}=<{type(v).__name__}>")
    return truncate("; ".join(parts), 240)


def yaml_escape(s: str) -> str:
    """Single-line YAML scalar escape: wrap in double quotes, escape backslash, quote, newline, tab, CR."""
    out = (s.replace("\\", "\\\\")
            .replace('"', '\\"')
            .replace("\n", "\\n")
            .replace("\r", "\\r")
            .replace("\t", "\\t"))
    return '"' + out + '"'


def ensure_file_header(digest_path: Path, session_num: str) -> None:
    """Write SCD-3 frontmatter + section headers if file does not exist."""
    if digest_path.exists():
        return
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    digest_path.parent.mkdir(parents=True, exist_ok=True)
    header = (
        "---\n"
        f"session: {session_num}\n"
        "title: Harness-Telemetry Digest\n"
        f"schema_version: {SCHEMA_VERSION}\n"
        f"generated_at: {now}\n"
        f"capture_adapter: {ADAPTER_NAME}\n"
        f"capture_adapter_version: {ADAPTER_VERSION}\n"
        "capture_capabilities:\n"
        "  - tool_name\n"
        "  - tool_input_summary\n"
        "  - tool_result_status\n"
        "  - timestamp_iso8601\n"
        "unobserved_fields:\n"
        "  - wall_clock_token_count\n"
        "  - reviewer_invocation_wall_clock_seconds\n"
        "# Per §10.4-M34 P4 z-laundering-1: file-level frontmatter declares ADAPTER\n"
        "# capabilities only. Each record below carries its own producer_kind +\n"
        "# authority_level annotation; file-level header does NOT promote\n"
        "# agent-declared records to harness-measured via shape alone.\n"
        "---\n"
        "\n"
        "substrate_calls: []\n"
        "tool_calls: []\n"
        "reviewer_invocations: []\n"
    )
    digest_path.write_text(header, encoding="utf-8")


def append_record(digest_path: Path, section: str, record_yaml: str) -> None:
    """Append `record_yaml` (a YAML list-item block) under `section:` in digest_path.

    Strategy: read file, find the `<section>:` line, insert record before the
    next top-level `<key>:` or EOF. Replaces empty `[]` initialiser.
    """
    text = digest_path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    inserted = False
    while i < len(lines):
        line = lines[i]
        if not inserted and line.rstrip("\n") == f"{section}: []":
            out.append(f"{section}:\n")
            out.append(record_yaml)
            inserted = True
            i += 1
            continue
        if not inserted and line.rstrip("\n").startswith(f"{section}:") and line.rstrip("\n").endswith(":"):
            out.append(line)
            i += 1
            while i < len(lines) and (lines[i].startswith("  ") or lines[i].strip() == ""):
                out.append(lines[i])
                i += 1
            out.append(record_yaml)
            inserted = True
            continue
        out.append(line)
        i += 1
    if not inserted:
        out.append(f"{section}:\n")
        out.append(record_yaml)
    digest_path.write_text("".join(out), encoding="utf-8")


def main() -> int:
    try:
        raw = sys.stdin.read()
        if not raw.strip():
            return 0
        event = json.loads(raw)
    except Exception as e:
        print(f"digest_emitter: stdin parse error: {e}", file=sys.stderr)
        return 0

    hook_event = event.get("hook_event_name", "")
    tool_name = event.get("tool_name", "")
    tool_input = event.get("tool_input", {})
    tool_response = event.get("tool_response", {}) or {}

    sess_dir = current_session_dir()
    if sess_dir is None:
        return 0
    session_num = sess_dir.name[:3]
    digest_path = sess_dir / "harness-telemetry-digest.yaml"

    try:
        ensure_file_header(digest_path, session_num)
    except Exception as e:
        print(f"digest_emitter: header write failed: {e}", file=sys.stderr)
        return 0

    is_substrate_call = isinstance(tool_name, str) and any(
        tool_name.startswith(p) for p in SUBSTRATE_TOOL_PREFIXES
    )

    if hook_event == "PreToolUse":
        return 0

    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    input_summary = summarise_input(tool_name, tool_input)
    if isinstance(tool_response, dict):
        if tool_response.get("error"):
            status = "error"
        else:
            status = "success"
    else:
        status = "unknown"

    record_lines = [
        f"  - tool_name: {yaml_escape(tool_name)}\n",
        f"    input_summary: {yaml_escape(input_summary)}\n",
        f"    status: {status}\n",
        f"    timestamp_iso8601: {timestamp}\n",
        "    producer_kind: harness-measured\n",
        "    authority_level: primary\n",
    ]
    record_yaml = "".join(record_lines)

    section = "substrate_calls" if is_substrate_call else "tool_calls"
    try:
        append_record(digest_path, section, record_yaml)
    except Exception as e:
        print(f"digest_emitter: append failed: {e}", file=sys.stderr)
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
