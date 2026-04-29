"""Workspace layout, environment overrides, and shared regex/constants."""

from __future__ import annotations

import os
import re
from pathlib import Path


WORKSPACE_ROOT_ENV = "SELVEDGE_WORKSPACE"
DEFAULT_BUSY_TIMEOUT_MS = 5000
DEFAULT_RETRY_BUDGET = 5
DEFAULT_RETRY_BASE_MS = 50
DEFAULT_LEASE_SECONDS = 300

# Citable-alias parser (T-01 source). Recognised forms:
#   [D-S<NNN>-<N>]            decision N in session NNN
#   [SPEC-<spec_id>-v<N>]     spec_version
#   [P-<deliberation>-<label>] perspective
#   [C-S<NNN>-<N>]            commitment
#   [EF-S<NNN>-<N>]           engine_feedback
ALIAS_RE = re.compile(
    r"\[("
    r"D-S\d+-\d+"
    r"|SPEC-[A-Za-z0-9_\-]+-v\d+"
    r"|P-\d+-[A-Za-z0-9_\-]+"
    r"|C-S\d+-\d+"
    r"|EF-S\d+-\d+"
    r")\]"
)

# Issue-alias regex used by orient FR-rot annotation. Matches the three
# alias shapes in current use: OI-NNN, OI-NNN-NNN, OI-S<wno>-<seq>.
FR_ISSUE_CITE_RE = re.compile(r"\bOI-(?:S\d{3}-\d+|\d{3}(?:-\d+)?)\b")

# Anchor-trace alias parsing for derived FR-S<wno>-<seq> identifiers
# (close_state_items.facet='next_session_should' rows have no objects.alias).
ANCHOR_FR_RE = re.compile(r"^FR-S(\d+)-(\d+)$")
ANCHOR_DELIB_RE = re.compile(r"^DELIB-(\d+)$")
# Generic alias-citation scanner used to follow forward-reference disposition
# notes ("addressed by DV-S116-1 (...)") into the trace.
ANCHOR_CITE_RE = re.compile(
    r"\b("
    r"DV-S\d+-\d+"
    r"|D-S\d+-\d+"
    r"|EF-S\d+-\d+"
    r"|OI-(?:S\d+-\d+|\d+(?:-\d+)?)"
    r"|SPEC-[A-Za-z0-9_\-]+-v\d+"
    r"|FR-S\d+-\d+"
    r"|S\d{3}"
    r")\b"
)

ANCHOR_TRACE_DEFAULT_DEPTH = 3
ANCHOR_TRACE_HARD_CAP_DEPTH = 5


def workspace_root() -> Path:
    from .errors import SelvedgeError
    if root := os.environ.get(WORKSPACE_ROOT_ENV):
        return Path(root).resolve()
    here = Path.cwd().resolve()
    for candidate in [here, *here.parents]:
        if (candidate / "MODE.md").exists():
            return candidate
    raise SelvedgeError("E_NO_WORKSPACE", f"no MODE.md found from {here} upward; set ${WORKSPACE_ROOT_ENV}")


def db_path() -> Path:
    if override := os.environ.get("SELVEDGE_DB_PATH"):
        return Path(override).resolve()
    return workspace_root() / "state" / "selvedge.sqlite"


def migrations_dir() -> Path:
    if override := os.environ.get("SELVEDGE_MIGRATIONS_DIR"):
        return Path(override).resolve()
    return workspace_root() / "state" / "migrations"
