---
session: 093
title: orient-surfaces-engine-feedback — assessment
engine_version_at_open: engine-v25
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

Engine at v25; S092 closed shipping operator-recommended cleanup. EF-S092-1..4 filed via raw SQL highlight that orient does not surface engine_feedback so triage signal is lost.

## Agenda

1. Extend bin/selvedge orient to surface undisposed engine_feedback rows under a new section so operators see them at session-open and triage into issues or decisions.
2. Filter on disposition IS NULL; order by feedback_id DESC; cap with elision footer matching the open-issues pattern.
3. Update both JSON shape (_orient_sections) and markdown formatter; add pytest coverage; T-20 review loop.
4. Triage EF-S092-1..4 by disposition pointing at the closing decision so they do not re-surface in subsequent orient packets.
5. Close, export, validate, commit, push.
