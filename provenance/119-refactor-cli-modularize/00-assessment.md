---
session: 119
title: refactor-cli-modularize — assessment
engine_version_at_open: engine-v34
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

selvedge/cli.py is a 4507-line monolith mixing argparse, errors, connection, aliases, migrations, ~30 submit handlers, export, anchor-trace, orient, schema, monitor-external.

## Agenda

1. Operator-led: split cli.py into selvedge/ submodules so cli.py holds only argparse + main dispatch.
2. Operator-led: extract submit-handler helpers to collapse repeated payload-validate / role-check / atom-insert patterns.
3. Preserve behavior exactly: no semantic change, no new features, no removed paths.
4. Defer FR-S118-10 (dry-run/sandbox harness for write-path submits) to a follow-up session against the modular surface.
