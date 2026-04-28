---
session: 105
title: oi-016-scope-check — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **medium**: Stale docstring on _submit_session_open: said caller passes ONLY slug, but kind is now required.
  - **fixed.** Updated docstring to mention required kind enum and DV-S105-2 reference.
- **low**: Falsy values (empty string, 0, False) bypass first kind check, only caught by enum check.
  - **fixed.** Switched first check to falsy-rejection (not p["kind"]) matching the slug check style.

## Terminal passes

- **iteration 2** — clean @ `9acc017cdd`
  - Iteration 1 surfaced one medium (stale docstring) and one low (falsy edge); both fixed. Iteration 2 clean.
