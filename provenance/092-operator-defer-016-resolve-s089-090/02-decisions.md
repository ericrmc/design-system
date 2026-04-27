---
session: 092
title: operator-defer-016-resolve-s089-090 — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Defer OI-016 (domain-validation pathway under user unavailability) until new signal warrants reopening.

**Kind:** disposition.  **Outcome:** defer issue `OI-016`.

**Why.**

- (operator_directive) Operator recommended deferring OI-016 for this session; no new domain-validation signal has surfaced since S033 re-resolution.
- (prior_decision) S014 D-069 designed the reference-validation mechanism; S033 D-106/D-107/D-108 re-resolved provisionally to reference-validation v3 / kernel v6.

**Effects.**

- modifies OI-016 remains open with deferred status flagged via this decision; status field unchanged.

**Rejected alternatives.**

- **R-1.1.** Reopen OI-016 this session and run a multi-agent deliberation on whether the provisional reference-substitute should be promoted or retired.
  - (no_feedback_loop) No external workspace has exercised the reference-validation pathway since S033 to produce new evidence; deliberation now would replay 2026-Q1 reasoning without ground.

## D-2. Add T-25 trigger making work_items lease renewal strictly forward in lease_expires_at.

**Kind:** schema_migration.  **Outcome:** adopt migration `012-t25-lease-renewal`.

**Why.**

- (prior_decision) DV-S089-1 adopted issue_work_items M:N and T-24 orphan-on-resolve; T-25 closes the renewal-monotonicity gap explicit in OI-S089-2. [DV-S089-1]
- (constraint) T-16 covers expired-lease insertion/transition only; renewal monotonicity was unenforced and a leaseholder could trim a live window.

**Effects.**

- adds_migration Migration 012 adds trigger t25_work_items_lease_renewal_monotonic
- closes_issue OI-S089-2

**Rejected alternatives.**

- **R-1.1.** Encode lease-renewal monotonicity in application-layer code rather than a trigger.
  - (violates_gate) Substrate-only-writes discipline prefers structural enforcement over application-layer guards; trigger is the engine-level invariant.

## D-3. Implement submit issue-work-item CLI handler closing the M:N issue<->work_item surface.

**Kind:** substantive.  **Outcome:** adopt process_rule `submit-issue-work-item`.

**Why.**

- (prior_decision) DV-S089-1 adopted issue_work_items table; submit handler completes the CLI surface so M:N linkage can be authored without raw SQL. [DV-S089-1]

**Effects.**

- creates _submit_issue_work_item handler in selvedge/cli.py registered as kind=issue-work-item
- closes_issue OI-S089-1

**Rejected alternatives.**

- **R-1.1.** Defer to a future session and expose the M:N linkage via direct SQL through __cli__ role for now.
  - (redundant_with_existing) Direct SQL bypasses _check_role_capability and atom-typed write discipline; the handler is a 25-line addition that closes the surface within the operator-recommended scope.

## D-4. Reject decomposition_status column on issues; LEFT JOIN dispatch query is sufficient.

**Kind:** substantive.  **Outcome:** reject open_question `issues-decomposition-status-column`.

**Why.**

- (prior_decision) DV-S089-1 adopted derived state via LEFT JOIN over issue_work_items + work_items; orient query in S091 already uses this shape and produces a usable dispatch packet. [DV-S089-1]

**Effects.**

- closes_issue OI-S089-3

**Rejected alternatives.**

- **R-1.1.** Add a denormalised decomposition_status column on issues and update it from triggers as work_items move through queued/leased/completed.
  - (redundant_with_existing) Two sources of truth (column plus join) invite drift; the join query is one statement and ran clean across S089-S091 orient packets.

## D-5. Harden migrate runner with post-apply rowcount check on schema_migrations row presence.

**Kind:** substantive.  **Outcome:** adopt process_rule `migrate-runner-post-apply-check`.

**Why.**

- (constraint) A migration that forgot its INSERT INTO schema_migrations line would silently re-apply on every invocation; the runner UPDATE rowcount check surfaces this at apply time and rolls back via the existing backup-restore path.

**Effects.**

- modifies _apply_pending: rowcount check after schema_migrations UPDATE, raises RuntimeError caught by E_MIGRATION_FAILED
- closes_issue OI-S090-3

**Rejected alternatives.**

- **R-1.1.** Have the migrate runner itself INSERT the schema_migrations row instead of expecting the migration body to do it.
  - (preserves_legacy_path) Existing migrations 001-012 all carry the INSERT line; flipping this convention would invert the contract for every authored migration. The rowcount check enforces the existing convention without rewriting it.

## D-6. Defer OI-S090-1, OI-S090-2, OI-S090-5 to dedicated subsequent sessions; out of scope here.

**Kind:** disposition.  **Outcome:** defer issue `S090-residual`.

**Why.**

- (constraint) Each remaining S090 issue (cross-ref linking pass, pytest build-out, substrate-driven spec authoring) carries multi-session scope and cannot share a session with the four resolutions already shipped here without ceremony or quality loss.
- (operator_directive) Operator recommendation framed scope as defer-016 plus S089/S090 cleanup; honoured by clearing OI-S089-1/2/3 and OI-S090-3 within budget.

**Effects.**

- modifies OI-S090-1, OI-S090-2, OI-S090-5 remain open; this session records the defer rationale

**Rejected alternatives.**

- **R-1.1.** Force all three into this session by accepting partial coverage (e.g., a token spec_clause_links seed pass).
  - (inferior_tradeoff) A token pass would leave the table partially populated and undercut the felt friction that justifies a focused session for each.
