#!/usr/bin/env python3
# /// script
# dependencies = ["pyyaml>=6.0"]
# ///
"""
Digest reconstructor — CM3 post-hoc bridge/comparator.

Per S073 D-276: secondary bridge/comparator at S075+ phase-3.1 implementation.
Used when CM1 hook unavailable OR for cross-validation of CM1-emitted records.
Per §10.4-M34 P4 z-laundering-1: every reconstructed record carries
producer_kind=post-hoc-reconstructed + authority_level=secondary; reconstructed
records cannot be promoted to harness-measured solely through digest shape.

Reconstruction sources at minimum-viable scope (S075 phase-3.1):
  (a) provenance/<NNN-session>/00-assessment.md frontmatter
      `substrate_session_open` + `substrate_evidence` fields per check 29
      β-phase declaration discipline.
  (b) prose mentions of `forward_references('S<NNN>')` and
      `mcp__selvedge-retrieval__*` tool names in 00-assessment.md, 02-decisions.md,
      03-close.md.

Output: provenance/<NNN-session>/harness-telemetry-digest.yaml. If a CM1-emitted
digest already exists, the reconstructor writes to
harness-telemetry-digest-cm3.yaml (sibling) for comparator role; otherwise
writes the primary digest path.

Future-arc extensions (S076+):
  - parse codex CLI transcripts when available
  - parse Claude Code transcripts (Claude Code does not currently expose them
    to userland in this workspace; deferred per portability discipline)

Engine-v15 per Session 075 phase-3.1 implementation.
"""

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
PROVENANCE_DIR = WORKSPACE_ROOT / "provenance"
ADAPTER_NAME = "post-hoc-reconstruction"
ADAPTER_VERSION = "v1"
SCHEMA_VERSION = "SCD-3"

SUBSTRATE_TOOL_RE = re.compile(r"mcp__selvedge-retrieval__(\w+)")
FORWARD_REF_RE = re.compile(r"forward_references\(\s*['\"]?(S\d{3})['\"]?\s*\)")
RESOLVE_ID_RE = re.compile(r"resolve_id\(\s*['\"]?([A-Z0-9_-]+)['\"]?\s*\)")
SEARCH_CALL_RE = re.compile(r"\bsearch\(\s*['\"]([^'\"]+)['\"]")


def session_number_from_dirname(name: str) -> str | None:
    if len(name) >= 3 and name[:3].isdigit():
        return name[:3]
    return None


def discover_session_dir(arg: str | None) -> Path | None:
    if arg:
        p = Path(arg).resolve()
        if p.is_dir():
            return p
        candidate = PROVENANCE_DIR / arg
        if candidate.is_dir():
            return candidate
        return None
    if not PROVENANCE_DIR.is_dir():
        return None
    candidates = [d for d in PROVENANCE_DIR.iterdir()
                  if d.is_dir() and session_number_from_dirname(d.name)]
    if not candidates:
        return None
    return max(candidates, key=lambda d: d.name)


def parse_assessment_frontmatter(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    block = text[3:end]
    out: dict[str, str] = {}
    current_key: str | None = None
    current_lines: list[str] = []
    for raw in block.splitlines():
        line = raw.rstrip()
        if not line:
            continue
        if line.startswith(" "):
            if current_key is not None:
                current_lines.append(line.strip())
            continue
        if current_key is not None and current_lines:
            out[current_key] = "\n".join(current_lines).strip()
            current_lines = []
        if ":" in line:
            k, _, v = line.partition(":")
            current_key = k.strip()
            v = v.strip()
            if v in ("|", ">"):
                current_lines = []
                continue
            if v:
                out[current_key] = v
                current_key = None
    if current_key is not None and current_lines:
        out[current_key] = "\n".join(current_lines).strip()
    return out


def find_substrate_mentions(session_dir: Path) -> list[dict[str, str]]:
    mentions: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for fname in ("00-assessment.md", "02-decisions.md", "03-close.md"):
        fpath = session_dir / fname
        if not fpath.exists():
            continue
        text = fpath.read_text(encoding="utf-8")
        for m in FORWARD_REF_RE.finditer(text):
            key = ("forward_references", m.group(1))
            if key in seen:
                continue
            seen.add(key)
            mentions.append({
                "tool": "mcp__selvedge-retrieval__forward_references",
                "input_summary": f"target={m.group(1)}",
                "source_file": fname,
            })
        for m in RESOLVE_ID_RE.finditer(text):
            key = ("resolve_id", m.group(1))
            if key in seen:
                continue
            seen.add(key)
            mentions.append({
                "tool": "mcp__selvedge-retrieval__resolve_id",
                "input_summary": f"alias={m.group(1)}",
                "source_file": fname,
            })
        for m in SEARCH_CALL_RE.finditer(text):
            key = ("search", m.group(1)[:40])
            if key in seen:
                continue
            seen.add(key)
            mentions.append({
                "tool": "mcp__selvedge-retrieval__search",
                "input_summary": f"query={m.group(1)[:80]}",
                "source_file": fname,
            })
    return mentions


def yaml_escape(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def build_digest(session_num: str, session_dir: Path) -> str:
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    fm = parse_assessment_frontmatter(session_dir / "00-assessment.md")
    substrate_open = fm.get("substrate_session_open", "")
    substrate_evidence = fm.get("substrate_evidence", "").replace("\n", " ").strip()

    mentions = find_substrate_mentions(session_dir)

    lines: list[str] = []
    lines.append("---")
    lines.append(f"session: {session_num}")
    lines.append("title: Harness-Telemetry Digest (post-hoc reconstruction)")
    lines.append(f"schema_version: {SCHEMA_VERSION}")
    lines.append(f"generated_at: {now}")
    lines.append(f"capture_adapter: {ADAPTER_NAME}")
    lines.append(f"capture_adapter_version: {ADAPTER_VERSION}")
    lines.append("capture_capabilities:")
    lines.append("  - tool_name")
    lines.append("  - input_summary_from_text")
    lines.append("  - source_file")
    lines.append("unobserved_fields:")
    lines.append("  - timestamp_iso8601")
    lines.append("  - status")
    lines.append("  - wall_clock_token_count")
    lines.append("  - reviewer_invocation_wall_clock_seconds")
    lines.append("# Per §10.4-M34 P4 z-laundering-1: file-level frontmatter declares ADAPTER")
    lines.append("# capabilities only. Each record below carries its own producer_kind +")
    lines.append("# authority_level annotation. Post-hoc reconstruction MUST NOT be promoted")
    lines.append("# to harness-measured via digest shape alone.")
    lines.append("---")
    lines.append("")

    lines.append("substrate_session_open_declaration:")
    if substrate_open:
        lines.append(f"  declared_state: {substrate_open}")
        lines.append("  producer_kind: agent-declared")
        lines.append("  authority_level: tertiary")
        if substrate_evidence:
            lines.append(f"  evidence_summary: {yaml_escape(substrate_evidence[:500])}")
    else:
        lines.append("  declared_state: absent")
        lines.append("  producer_kind: agent-declared")
        lines.append("  authority_level: tertiary")
    lines.append("")

    lines.append("substrate_calls:")
    if not mentions:
        lines.append("  []")
    else:
        for entry in mentions:
            lines.append(f"  - tool_name: {yaml_escape(entry['tool'])}")
            lines.append(f"    input_summary: {yaml_escape(entry['input_summary'])}")
            lines.append(f"    source_file: {yaml_escape(entry['source_file'])}")
            lines.append("    producer_kind: post-hoc-reconstructed")
            lines.append("    authority_level: secondary")
    lines.append("")

    lines.append("tool_calls: []")
    lines.append("")
    lines.append("reviewer_invocations: []")
    lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--session", help="Provenance directory name (e.g. 075-session) "
                                          "or absolute path. Defaults to most recent.")
    parser.add_argument("--out", help="Output file. Defaults to harness-telemetry-digest.yaml "
                                       "in the session dir, or harness-telemetry-digest-cm3.yaml if "
                                       "the primary digest already exists.")
    args = parser.parse_args()

    sess_dir = discover_session_dir(args.session)
    if sess_dir is None:
        print("digest_reconstructor: no session directory found", file=sys.stderr)
        return 1
    session_num = session_number_from_dirname(sess_dir.name) or "???"

    if args.out:
        out_path = Path(args.out).resolve()
    else:
        primary = sess_dir / "harness-telemetry-digest.yaml"
        if primary.exists():
            out_path = sess_dir / "harness-telemetry-digest-cm3.yaml"
        else:
            out_path = primary

    digest_text = build_digest(session_num, sess_dir)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(digest_text, encoding="utf-8")
    print(f"Wrote {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
