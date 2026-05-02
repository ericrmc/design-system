"""`bin/selvedge submit-help` — print payload schemas from the submit registry.

Reads `selvedge.submit._schemas.SUBMIT_SCHEMAS` and renders one entry's
schema (when a kind is given) or a one-line summary of every kind. The
registry is documentation, not validation; handlers in `selvedge/submit/`
own the actual payload reads.
"""

from __future__ import annotations

import sys

from .submit._schemas import SUBMIT_SCHEMAS


def _format_kind(kind: str) -> str:
    entry = SUBMIT_SCHEMAS[kind]
    lines = [
        f"# `bin/selvedge submit {kind}`",
        "",
        entry["summary"],
        "",
    ]
    if entry.get("spec_ref"):
        lines.append(f"_See {entry['spec_ref']}._")
        lines.append("")
    lines.append("## Required")
    lines.append("")
    if entry["required"]:
        for name, desc in entry["required"]:
            lines.append(f"- `{name}` — {desc}")
    else:
        lines.append("(none)")
    lines.append("")
    any_of = entry.get("any_of") or []
    if any_of:
        lines.append("## One of")
        lines.append("")
        for group in any_of:
            field_list = " | ".join(f"`{f}`" for f in group["fields"])
            lines.append(f"- {field_list} — {group['description']}")
        lines.append("")
    if entry["optional"]:
        lines.append("## Optional")
        lines.append("")
        for name, desc in entry["optional"]:
            lines.append(f"- `{name}` — {desc}")
        lines.append("")
    else:
        lines.append("## Optional")
        lines.append("")
        lines.append("(none)")
        lines.append("")
    lines.append("## Example")
    lines.append("")
    lines.append("```sh")
    lines.append(f"bin/selvedge submit {kind} --payload '{entry['example']}'")
    lines.append("```")
    return "\n".join(lines)


def _format_index() -> str:
    lines = [
        "# `bin/selvedge submit` — kinds",
        "",
        "Run `bin/selvedge submit-help <kind>` for the payload schema of any kind.",
        "",
        "| Kind | Summary |",
        "|------|---------|",
    ]
    for kind in sorted(SUBMIT_SCHEMAS):
        summary = SUBMIT_SCHEMAS[kind]["summary"].replace("|", "\\|")
        lines.append(f"| `{kind}` | {summary} |")
    return "\n".join(lines)


def cmd_submit_help(args) -> int:
    if args.kind is None:
        print(_format_index())
        return 0
    if args.kind not in SUBMIT_SCHEMAS:
        suggestions = sorted(
            k for k in SUBMIT_SCHEMAS if args.kind in k or k.startswith(args.kind[:3])
        )
        msg = f"unknown submit kind: {args.kind!r}"
        if suggestions:
            msg += f"; did you mean one of: {', '.join(suggestions)}"
        else:
            msg += "; run `bin/selvedge submit-help` for the full list"
        print(msg, file=sys.stderr)
        return 2
    print(_format_kind(args.kind))
    return 0
