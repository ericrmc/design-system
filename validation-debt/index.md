---
title: Validation-Debt Lifecycle Ledger
authoritative: true
last-updated: 2026-04-26
updated-by-session: 067
---

# Validation-Debt Lifecycle Ledger

This file is the (z5) validation-debt lifecycle ledger per `specifications/validation-approach.md` v7 §(z5) Validation-Debt Lifecycle.

**Authoritative semantics (v7 per S064 D-233 §10.4-M24)**: this ledger is the **source-of-truth** for validation-debt lifecycle state. Frontmatter declares `authoritative: true`. Reviewers audit ledger as authoritative; close-narrative claims about debt MUST be checkable against ledger; ledger-vs-narrative mismatch is a Tier 2.5 finding unless close explains why ledger is stale or superseded with substantive rationale.

It is **engine-adjacent** per `engine-manifest.md` §3 boundary (required by the engine; implementation-not-engine-definition; analogous to `tools/validate.sh`).

Validator check 28 enforces row well-formedness: required fields present per row, `status` enum membership (`open | in-progress | resolved | deferred-with-rationale | escalated`), `review_by_session` well-formedness (`S<NNN>` or numeric), no rows past `review_by_session` with `escalation_disposition: n/a` while status is `open` or `in-progress`. **At v7**: check 28 additionally verifies frontmatter `authoritative: true` declaration when ledger is read by Tier 2.5 reviewer.

Records-family promotion (creating `records/validation-debt/` per `records-contract.md` v1 phase-N) deferred to post-records-substrate phase-2/3 stabilisation per S062 §10.4-M18 reopen warrants. Lightweight-table is the initial implementation per S063 D-228 phase-3 adoption; authoritative-not-witness semantics adopted at S064 per D-233.

Created S063 per D-228 + D-230 housekeeping bootstrap. Authoritative semantics adopted S064 per D-233.

## Lifecycle items

| id | introduced_session | owner_or_surface | next_action | review_by_session | status | escalation_disposition |
|----|---------------------|-------------------|-------------|---------------------|--------|------------------------|
| VD-001 | S051 | engine-substrate-runtime (resolved via uv-migration at S059 D-207 + D-210 + D-211 per EF-058-substrate-runtime-uv-migration-recommended-path) | check 26 mechanism deployed at S063 will detect future MCP-stdio-transport recurrence; substrate-aware variant validates cross-paraphrase robustness; first triggered application at S063 close confirms operational closure | S066 | resolved | n/a — chain closed operationally at S061 finding 13 + structurally addressed at S062 D-221 + check 26 mechanism deployed at S063 |
| VD-002 | S064 | tools/validate.sh check 26 implementation — surfaced by S064 Tier 2.5 reviewer audit Finding 2 (codex CLI sandbox=read-only) | Refactor check 26 grep-fallback to write tempfiles only when invoked outside read-only sandbox, OR provide pre-computed check 26 output that reviewer can read without re-execution. The reviewer needs check 26 output for (α)-flag-coverage per check 27 sub-clause; in read-only sandbox the current `mktemp -d` + per-close text-extraction implementation cannot run. Option A: refactor to use in-memory awk + array-based n-gram comparison (no tempfiles). Option B: write check 26 results to `provenance/<NNN-session>/check-26-output.txt` during normal validate.sh run; reviewer reads pre-computed file. Option B is simpler but requires write access during validate.sh which is currently read-only by design. | S067 | resolved | Resolved at S067 per D-244 (Path L single-orchestrator implementation): Option A adopted; `tools/validate.sh` check 26 grep-fallback refactored to in-memory bash indexed arrays + here-string substring matching (no tempfile creation; preserves validate.sh read-only design property; preserves algorithmic equivalence). Bash 3.2 compatible. Validator post-refactor PASS at S067 close (1555 PASS / 0 FAIL post-records-row-write / 32 WARN; check 26 emits identical no-clusters-detected result vs pre-refactor). Reviewer at S067 close (Tier 2.5 (γ) audit per Layer 2 trigger (a)+(d) fire) verifies the refactor preserves semantics + closes VD-002 substantively. |

## Conventions

- **id format**: `VD-NNN` append-only numbering; no reuse.
- **introduced_session**: session number (S<NNN> form) where the debt was first surfaced (typically the session whose §8 honest-limit caused check 26 to emit WARN/FAIL, OR the session where the operator surfaced the gap, OR the session that triaged an `engine-feedback/inbox/EF-*` record producing a debt entry).
- **owner_or_surface**: who or what is responsible for the debt's resolution. Acceptable values: a person/role identifier (e.g., "case-steward", "operator"); "this session's reviewer" (reviewer dispositioned the item); "engine-feedback record EF-NNN" (debt is captured in an inbox record); a tooling identifier (e.g., "engine-substrate-runtime").
- **next_action**: substantive description of what the next concrete step is. Avoid formulaic "review again" or "consider further"; name the artefact, decision, or operation that would advance the lifecycle item.
- **review_by_session**: the session number by which the next_action should be re-evaluated. Lifecycle items past their review_by_session without escalation_disposition rationale fail check 28.
- **status**: enum `open | in-progress | resolved | deferred-with-rationale | escalated`. Status enum is enforced by check 28.
- **escalation_disposition**: rationale text. Required when status is `deferred-with-rationale` or `escalated`; "n/a" or brief closure-rationale when status is `resolved`. Empty/missing fails check 28.

## Lifecycle operations

- **Introduce a row** when check 26 emits WARN/FAIL OR the operator surfaces a gap OR a session's §8 honest-limit names a gap not yet in the ledger. The (γ) reviewer at the introducing session (when triggered) verifies the row's well-formedness via Audit Disposition.
- **Update a row** by appending a new edit (git history preserves prior values). Status transitions: `open` → `in-progress` → `resolved | deferred-with-rationale | escalated`. Escalation may also happen directly from `open` to `escalated` (e.g., scope exceeds engine).
- **Close a row** by changing status to `resolved` and updating escalation_disposition to "n/a" or a brief closure-rationale citing the resolving session's decisions. Layer 2 trigger (d) fires at the closing session.
- **Defer a row** by changing status to `deferred-with-rationale` and providing substantive rationale in escalation_disposition. Layer 2 trigger (d) fires at the deferring session.
- **Escalate a row** when review_by_session has lapsed without progress, owner_or_surface is unavailable, or the gap exceeds engine-scope. Status changes to `escalated`; escalation_disposition names the escalation target (typically operator-attention or a new engine-feedback inbox record).

## Bootstrap rationale

VD-001 documents the S051-S058 MCP-stdio-transport honest-limit chain, which was the operational pattern that motivated EF-058-tier-2-validation. The chain was closed operationally at S061 (substrate uv-migration via S059 D-207 + verified at S061 finding 13) and structurally addressed at S062 D-221 (the layered structural mechanism adopted in this v6). VD-001 enters the ledger at `status: resolved` to demonstrate the lifecycle pattern + provide check 28's first integrity-validation surface; it is also the operational-closure record for the chain itself.

The bootstrap is a precedent for future lifecycle entries: when a debt is fully resolved by the time it enters the ledger, the row is created at `status: resolved` with closure-rationale in escalation_disposition. When a debt is in-progress at entry, the row is created at `status: open` with the next concrete action and an explicit `review_by_session`.
