---
session: 205
title: test-infra-tmp-db-isolation-calibration — engine-feedback
generated_by: selvedge export --session
---

# Engine feedback

## EF-S205-1

- **flag.** calibration
- **disposition.** (none)

**S204 §8.5 audit-gap retrospective: pytest-touches-PRIMARY_DB failure mode missed in-session.** During S204 ship of event_ledger v1, two failure modes surfaced but were not lifted as AR rows or OIs at close: (1) S204 pytest run mid-session caused substrate-clobber requiring ad-hoc recovery from L3 snapshot 20260505T092315620202Z-migrate_apply-pid16465.sqlite (state/selvedge.sqlite vanished after teardown; .pre-migrate-backup was 131KB stale; recovery succeeded but cost ~10min); (2) validate.sh-driven pytest run produced intermittent 3-4 errors across S203 + S204 sessions with E_MIGRATION_FAILED no-such-table during init --force in test_top_level_commands or test_assessment_precheck. Failure modes are material (substrate destruction risk) but were treated as transient during S204 close and not surfaced. Recovery path now: this calibration EF + AR-S205-1+2+3+4 + OI-S205-1 (MEDIUM) opening refactor scope. Per DV-S152-1 typed-observation→gate progression: if next pytest substrate-clobber lands without OI-S205-1 ship, gate-promotion to higher-priority OI.

## EF-S205-2

- **flag.** observation
- **disposition.** (none)

**audit-step:** 1 load-bearing interpretive choice. 1. Treating the S204 substrate-clobber as material-enough-to-calibrate vs. transient-flake: lifted-to AR-S205-1 + AR-S205-2 (snapshot/restore-fragility + clean_substrate-fixture-reinit-on-prod-path); the clobber happened mid-session and required L3-snapshot recovery; this is the 2nd recurrence pattern (S203 already showed validate.sh pytest flakes); per DV-S152-1 typed-observation pathway 2 occurrences across recent sessions warrants substrate-resident binding.

## EF-S205-3

- **flag.** observation
- **disposition.** (none)

**scoping-pass: 0 — exclusions applied: meta-session-no-substantive-artefact** — S205 produced no kind=substantive | schema_migration decision_v2 and no spec_version; T-41 gate does not fire on close. Patterns considered: schema-adjacency (no schema change), caller-implications (no new handler/CLI surface), migration-implications (no migration). All 4 AR rows lifted are session-scoped diagnostic-substrate not artefact-implication.
