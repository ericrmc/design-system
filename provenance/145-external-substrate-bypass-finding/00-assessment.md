---
session: 145
title: external-substrate-bypass-finding — assessment
engine_version_at_open: engine-v43
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

External workspace substrate has 2-session gap: operator S014/S015 bypassed substrate via SELVEDGE_EXPORT_CONTEXT=1; agent at S016 surfaced gap in close-record but did not author EF.

## Agenda

1. Document the bypass mechanism: SELVEDGE_EXPORT_CONTEXT=1 is engine-v24 escape hatch in tools/hooks/refuse-substrate-md.py intended only for bin/selvedge export; agent misused for direct authoring.
2. Document the substrate gap concretely: sessions table jumps S013 to S014 with S014 slug day11-chase-results which is operator S016; ~14 decisions DV-S014-1..5 DV-S015-1..9 markdown-only.
3. Document harness-pilot impact: RH-S143-1 cited DV-S014-N and DV-S015-N as substrate evidence but rows do not exist in peer substrate; sha256 anchor valid file content; cross-references partial.
4. Author blocker engine-feedback EF-S145-1 with full detail; propose remediation directions (backfill vs accept-gap); flag SELVEDGE_EXPORT_CONTEXT narrower-scope kernel question.
5. Open OI for substrate-bypass detection / remediation tooling at MEDIUM priority.
6. Recommend operator-side remediation choice for the external workspace integrity question.
