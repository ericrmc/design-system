---
feedback_id: EF-073-gemini-excluded-and-reviewer-family-rule-relaxation
source_workspace_id: selvedge-self-development
source_session: 073
created_at: 2026-04-26T09:00:00Z
reported_by: operator
target: methodology
target_files:
  - specifications/validation-approach.md
  - tools/validate.sh
  - specifications/workspace-structure.md
severity: blocker
status: resolved
---

## Observation

Operator-directive surfaced post-S073 close: the `google` provider (Gemini family) is permanently excluded from all engine reviewer roles. Empirical basis: sustained `findings_count: 0` pattern across all four prior Gemini Tier 2.5 reviewer audits (S063 + S067 + S071 + S073 = n=4); S073 close-time codex cross-check audit on the identical evidence packet + identical reviewer-prompt-template-v2 prompt produced `findings_count: 2` with substantive findings (VD-003 gating-discharge wording inconsistency between D-282 vs D-284/ledger; §7 5-condition self-test over-compresses inbox state and uses stale S065 retention-window reference). The cross-check is recorded at `provenance/073-session/04-tier-2-audit-codex-cross-check.md` (1,447 words; codex `findings_count: 2`) alongside the official Gemini audit at `provenance/073-session/04-tier-2-audit.md` (~981 words; Gemini `findings_count: 0`).

Operator-directive verbatim:

> File engine-feedback saying Gemini is no longer to be used for any reason. Update wording again to relax same-family limits as needed. We have established that Claude and ChatGPT are better reasoning models, and the validation is better done with one of those, even though there is overlap. This is a hard limit being applied and the engine needs to accommodate it immediately. There is no further MAD discussion on the merits of keeping Gemini because it is gone.

## Why It Matters

Two methodology-level implications:

1. **Reviewer-discipline reliability.** The `validation-approach.md` v6/v7 §Tier 2.5 reviewer mechanism was structurally designed for cross-family-distinct reviewer audits as the counter-pressure to noticing-failure (per §10.4-M23 P3 substrate-led reviewer-judged frame; per S062 D-221 + S063 D-228 phase-3 adoption). The empirical signal at n=4 is that a family-distinct Gemini reviewer using reviewer-prompt-template v2 produced ceremonial `findings_count: 0` audits where a family-overlapped codex reviewer using the identical prompt produced substantive findings. This falsifies the assumption that family-distinctness is the load-bearing property of reviewer discipline; reasoning capacity at the reviewer-prompt-template + minimum-evidence-packet evaluation surfaces is empirically the load-bearing property.

2. **Family-overlap as acceptable trade-off.** Operator-policy authority on reviewer family selection: Claude (anthropic) and codex (openai) are operationally preferred reviewers despite family-overlap with orchestrator/perspectives in MAD sessions. The existing v7 `reviewer_overlap_with_recent_mad_perspectives:` field disclosure + counterweighting check discipline is preserved verbatim at v8 as the sole counter-pressure to family-overlap.

## Suggested Change

Operator-directed substantive amendment to `specifications/validation-approach.md` v7 → v8:

(a) **REMOVE** the v7 §Tier 2.5 reviewer-family family-distinctness requirement: was "The reviewer's family MUST differ from the orchestrator's family at the organisation level". Family-overlap permitted at v8 with mandatory disclosure + counterweighting check (v7 disclosure discipline preserved verbatim).

(b) **ADD** an explicit provider-exclusion clause: clause (d) — `google` provider permanently excluded from reviewer roles. Existing S063+S067+S071+S073 Gemini audit records remain valid as historical artefacts; no future reviewer-role invocation of google is permitted. Acceptable reviewer providers: `tools/validate.sh` PARTICIPANT_ORGANISATION_CLOSED_SET except `google` (operationally `{anthropic, openai, local, other-named}` plus future-named providers).

Additional tooling support:

- `tools/validate.sh` substantive update: new `EXCLUDED_REVIEWER_PROVIDERS=google` constant + new `EXCLUDED_REVIEWER_ADOPTION_SESSION=74` constant + new check 27 sub-clause that emits FAIL when `reviewer_provider: google` appears in any session 74+ audit artefact.

- `specifications/workspace-structure.md` v9 minor amendment: §10.4-M21 P2 prompt-template-first / defer-spec-revision-to-S067+ reopen-warrant (a) sustained-pattern threshold n≥3 status update — Gemini `findings_count: 0` pattern at n=4 is empirical vindication of P2's reopen warrant (a) for reviewer-prompt-template revision; preserved as historical record. Reviewer-prompt-template v3 revision deferred to future Path-AS / Path-PD scope per (z7) lock-in-after-n=2 explicit-deliberation-surface requirement.

- `specifications/engine-manifest.md`: new engine-v14 entry per substantive `validation-approach.md` v7 → v8 + substantive `tools/validate.sh` update.

## Evidence

- Gemini reviewer audit S063: `provenance/063-session/04-tier-2-audit.md` (`findings_count: 0`).
- Gemini reviewer audit S067: `provenance/067-session/04-tier-2-audit.md` (`findings_count: 0`).
- Gemini reviewer audit S071: `provenance/071-session/04-tier-2-audit.md` (`findings_count: 0`).
- Gemini reviewer audit S073: `provenance/073-session/04-tier-2-audit.md` (`findings_count: 0`).
- Codex cross-check S073 (identical input): `provenance/073-session/04-tier-2-audit-codex-cross-check.md` (`findings_count: 2`).
  - Finding 1 (codex): VD-003 gating-discharge wording inconsistency between D-284/ledger ("discharged at S073") and D-282/EF-059-disposition ("discharged at S074").
  - Finding 2 (codex): §7 5-condition self-test over-compresses inbox state ("three records actively progressing" elides three non-γ long-deferred items: EF-068-read-write-rebalance + EF-058-claude-md-drift + EF-047-brief-slot-template) and uses stale S065 retention-window reference (S065 is outside the S068-S073 retention window; the conclusion stands but the citation is stale).

## Application-Scope Disposition

This is a self-development workspace observation; no external-application context. Resolved in same session (S074) per S048 D-154 + S066 first-of-record operator-directed inbox-record resolution precedent extended to substantive engine-definition amendment. Not deliberated via MAD per `multi-agent-deliberation.md` v4 §Opt-out — operator-directive is binding policy authority on reviewer-family selection per §10.4-M10 written-warrant clause (c) operator-surfacing channel cumulative count n=10 → n=11.
