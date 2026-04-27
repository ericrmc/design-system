---
session: 088
title: issues-table — assessment
engine_version_at_open: engine-v21
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

S087 closed OI-085-001 + bumped engine v21; deferred (DV-S087-1 R-1.3) was an issues substrate table to migrate the 25 markdown OIs and provide a substrate-native dispatch surface.

## Agenda

1. Convene three-perspective deliberation on issues-table schema: identity scheme, status enum, body storage, relations, backfill strategy. At least one cross-family.
2. Capture-subagent decomposes perspectives into perspective-position + perspective-claim rows.
3. Synthesise; record synthesis-points (convergence + dissent preserved).
4. Decision-record adopting the schema; alternatives + rejections.
5. Migration 009 ships the issues table + indexes + T-trigger refusals; coding-review loop on the SQL.
6. Add submit issue + submit issue-disposition CLI kinds to selvedge/cli.py; coding-review loop on the Python.
7. Backfill subagent reads the 25 markdown OIs (active + resolved) and submits one issue row per file; verify counts.
8. Bump engine v21 to v22; update engine-manifest.md; submit spec-version + decompose v22.
9. Close, export, validate, commit.
