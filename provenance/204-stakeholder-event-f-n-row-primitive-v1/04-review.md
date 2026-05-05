---
session: 204
title: stakeholder-event-f-n-row-primitive-v1 — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **critical**: F-1 Default ord collision defect: handler eff.get(ord, i) allows explicit+default mix to collide via SQL UNIQUE not handler E_VALIDATION
  - **fixed.** fixed-this-iteration via up-front seen_ords loop refusing duplicate ord with actionable E_VALIDATION before INSERT; new test test_refuse_implicit_default_ord_collision
- **critical**: F-2 confirms-assumption against non-assumption target untested; symmetric refusal path missing from test_event_ledger
  - **fixed.** fixed-this-iteration via test_refuse_confirms_assumption_non_assumption_target_handler covering symmetric path
- **high**: F-3 T-43 trigger WHEN clause enumerates kinds inline; future enum drift silently weakens validation if migration not synced
  - **adjudicated.** adjudicated-defer with watch-trigger; closed CHECK enum at v1 makes drift impossible without migration; M-1 + M-2 + M-3 minorities preserve enum-extension paths via gate-promotion OI per DV-S204-1; matches cycle.py 052 inline-enum precedent
- **high**: F-4 empty-string reason atom bypasses handler validation; F-02 cycle.py vulnerability not replicated as F-04 event.py fix
  - **fixed.** fixed-this-iteration via if reason is not None and not reason refuse E_VALIDATION; new test test_refuse_empty_string_reason_atom mirrors cycle.py F-02 fix
- **high**: F-5 default ord test gap (paired with F-1 above)
  - **fixed.** fixed-this-iteration bundled with F-1 fix via test_refuse_implicit_default_ord_collision
- **medium**: F-6 T-15 compliance comment terse vs cycle.py 052+053 precedent; trigger-recreate chain not documented for newcomers
  - **adjudicated.** adjudicated-cosmetic; existing comment names both triggers and precedent migrations; deferred to future migration touching same surface
- **medium**: F-7 alias seq COUNT race assumption documented in cycle.py; same pattern in event.py without explicit comment
  - **adjudicated.** adjudicated-defer; harness-level invariant single-threaded write_tx; matches cycle.py + supersession.py pattern; surfaces as future OI if multi-threaded harness ever lands
- **low**: F-8 inert semantics docstring depth less than cycle.py
  - **adjudicated.** adjudicated-cosmetic; handler docstring + migration comment + spec clause all describe inert semantics; depth difference does not affect behaviour
- **low**: F-10 confirms-assumption-without-reason test asymmetry vs invalidates-assumption-with-reason
  - **adjudicated.** adjudicated-defer; reason is optional at SQL with no kind-coupling; test_optional_reason_atom_pinned covers reason-pinned path; symmetric coverage nice-to-have not material

## Terminal passes

- **iteration 2** — clean @ `0b06a780164d`
  - S204 event-ledger v1 review-pass iter-2 clean: iter-1 surfaced 9 findings (2 CRIT + 3 HIGH + 2 MED + 2 LOW); 2 CRIT + 1 HIGH fixed-this-iteration via handler ord-collision detection + symmetric confirms-assumption test + empty-string reason guard; iter-2 clean.
