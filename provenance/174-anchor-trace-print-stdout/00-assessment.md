---
session: 174
title: anchor-trace-print-stdout — assessment
engine_version_at_open: engine-v47
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

S174 actions FR-S173-1 HIGH coding session: ship --print stdout mode on bin/selvedge export --provenance --anchor per S173 D-26 synthesis.

## Agenda

1. Add --print argparse flag to export subparser in selvedge/cli.py.
2. In selvedge/export/__init__.py cmd_export, when --print is set emit markdown body to stdout without JSON wrapper.
3. Add pytest covering --print emits markdown body and produces no provenance/ files.
4. Run reviewer subagent (Explore) over the diff and address findings.
5. Dispose FR-S173-10 (FR-S173-1) citing the resolving DV; close session.
