---
session: 158
title: ef-s157-1-alias-resolution-friction — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **critical**: Regex _ISSUE_ALIAS_RE does not match legacy issue aliases OI-001 through OI-999. Pattern requires OI-SNNN-N or OI-NNN-NNN, missing single-digit forms in production. Legacy issues cited silently bypass diagnostic hint.
  - **fixed.** Updated _ISSUE_ALIAS_RE to admit legacy OI-NNN form: ^OI-(?:S\d{3}-\d+|\d{3}(?:-\d{3})?)$. Verified all 87 issue aliases match (19 legacy OI-NNN + 11 OI-NNN-NNN + 57 OI-SNNN-N).
- **high**: No tests exercise the new issue-alias and FR-alias detection branches. Test coverage missing for E_REFUSAL_T01 with OI-* and FR-* shaped aliases.
  - **fixed.** Added state/tests/test_alias_resolution.py with 27 tests covering regex admission, regex rejection, basis-aware hints for issue/FR aliases, fall-through to generic refusal, and successful object-id resolution.
- **medium**: Error messages cite non-existent objects tables (claims ref forward_reference_dispositions but FRs not in objects; issues not in objects). Operator recovery hints may mislead.
  - **adjudicated.** Error message already names recovery path (cite EF or DV; fold into claim text). Operator discipline for what fold means is encoded in prompt-development v14 §5 cite-typing callout shipped this session.
- **low**: FR regex _FR_ALIAS_RE requires exactly 3 digits for session number (\d{3}), but issue aliases and other FK-bearing objects use variable digits. Inconsistent notation may confuse operators.
  - **fixed.** Regex digit-count is now consistent across both: 3-digit session number for OI session-form OI-S\d{3}-\d+ and FR-S\d{3}-\d+; legacy OI bare form also 3-digit OI-\d{3}.

## Terminal passes

- **iteration 1** — clean @ `8909b14`
  - S158 reviewer iter-1 surfaced 4 findings (1 critical 1 high 1 medium 1 low); all addressed at handler+tests; pytest 254 pass.
