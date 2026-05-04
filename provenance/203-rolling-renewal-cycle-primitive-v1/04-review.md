---
session: 203
title: rolling-renewal-cycle-primitive-v1 — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **high**: No SPEC amendment filed for S203 cycle_ledger v1 ship; S197/S198/S201 precedent requires spec amendment in-session per migration header pattern.
  - **fixed.** Fixed via SPEC-prompt-development-v8 in-session per S197/S198/S201 ship pattern; surfaces cycle submit kind + classification enum + subject allowlist + auto-SR suppression + watch-triggers + cross-app generalization.
- **medium**: Handler does not validate empty-string classification_reason for substantial cycles; _validate_atom will refuse it, but validation order sends E_ATOM_LENGTH rather than E_VALIDATION per spec discipline.
  - **fixed.** Fixed via _validate_classification_discipline empty-string guard (not classification_reason vs is None) plus test_substantial_with_empty_string_reason_refused_handler exercising path.
- **high**: Handler admits citing_supersession on non-substantial cycles without refusal; SQL migration defines only CHECK (classification != 'substantial' OR classification_reason_atom_id IS NOT NULL) but has NO CHECK preventing non-substantial + non-NULL citing_supersession_object_id. D-9 C-1 states non-substantial NEVER cites SL; enforcement must be handler-layer guard or SQL CHECK (missing).
  - **fixed.** Fixed via migration 053 SQL CHECK plus handler-side actionable refusal in _validate_classification_discipline plus test_non_substantial_cannot_cite_supersession_handler; engine-v57 to v58 bump within-session strengthening of D-9 C-1 synthesis.
- **medium**: Test suite does not cover non-substantial cycle with non-NULL citing_supersession (violation of D-9 C-1 constraint). test_optional_citing_supersession_resolves uses substantial + reason; no negative test for non-substantial + citing_supersession.
  - **fixed.** Fixed via test_non_substantial_cannot_cite_supersession_handler covering D-9 C-1 synthesis path; bundled with F-03 fix.
- **low**: Test suite does not cover cycle_no_override with negative or very large integers. Handler calls int(cycle_no_override) without bounds checking; SQL UNIQUE(subject,cycle_no) allows any valid INTEGER but no test exercises these edge cases.
  - **adjudicated.** Codex stance permits non-strict-monotonic cycle_no per D-9 P-3 explicit position; explicit override is operator-judgment for legacy data migration; negative integer is degenerate but not breaks-invariant per UNIQUE constraint enforcement; defensive bounds added at v1.1 if calibration-EF surfaces misuse.
- **low**: Alias sequence generation uses COUNT(*) AFTER insert to determine the per-session index; this makes CYC-S<wno>-1 the first cycle (n_for_session=1 after first INSERT). Semantically correct but the docstring comment at line 30 ('CYC-S<wno>-<seq>') does not clarify whether <seq> is 0-indexed or 1-indexed. Consistent with assumption pattern but undocumented convention.
  - **adjudicated.** Alias seq convention matches assumption.py + supersession.py + closure_shape.py precedent (per-session COUNT-based); no docstring drift since pattern is uniform across all ledger handlers; cosmetic doc improvement deferred.
- **low**: T-42 trigger uses WHEN subquery returning NULL if object_id missing; while subject_object_id NOT NULL FK prevents missing objects, the trigger's WHEN clause documents NULL-coalescing subquery pattern without explicit safeguard (defensive programming). Compare against 049/051 T-n trigger patterns for consistency in NULL-guards at SQL-trigger layer.
  - **adjudicated.** subject_object_id NOT NULL FK; T-42 WHEN subquery NULL only if FK referent missing which fires E_REFUSAL_T01 at handler before insert; defensive NULL-guard preserved as v1.1 hardening if calibration-EF surfaces FK race; T-42 pattern matches handler-side allowlist precedent in 048+049+051.

## Terminal passes

- **iteration 2** — clean @ `be61b04`
  - Iter-2 clean: 4 fixed (F-01 spec amendment SPEC-prompt-development-v8 + F-02 empty-string handler check + F-03 migration 053 SQL CHECK + handler validation + F-04 test coverage); 3 adjudicated low-severity (F-05 codex non-strict-monotonic stance + F-06 alias-seq doc precedent-uniform + F-07 T-42 NULL semantics defensive-v1.1).
