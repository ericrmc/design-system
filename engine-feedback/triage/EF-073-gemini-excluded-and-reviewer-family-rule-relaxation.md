---
feedback_ref: engine-feedback/inbox/EF-073-gemini-excluded-and-reviewer-family-rule-relaxation.md
triage_session: 074
status: accepted
classification: substantive
resolved_by: provenance/074-session/
---

## Triage disposition

**Accepted at S074 open** per operator-direct directive at session-open. Classified `substantive` per substantive amendment to engine-definition spec (`validation-approach.md` v7 → v8 substantive) + substantive update to `tools/validate.sh` (new EXCLUDED_REVIEWER_PROVIDERS constant + check 27 sub-clause). No MAD per `multi-agent-deliberation.md` v4 §Opt-out — operator-directive binding policy authority on reviewer-family selection.

## Resolution

Resolved in same session (S074) via Path-L per operator-directed substantive amendment per S066 precedent extended to substantive-class engine-definition revision:

- D-287 EF-073 engine-feedback record filed and resolved same session per S048 D-154 first-of-record operator-directed inbox-record resolution precedent extended to substantive engine-definition amendment.
- D-288 `validation-approach.md` v7 → v8 substantive revision: family-distinctness requirement REMOVED; google provider EXCLUDED from reviewer roles via new clause (d). v7 preserved as `validation-approach-v7.md` `status: superseded`.
- D-289 `tools/validate.sh` substantive update: new `EXCLUDED_REVIEWER_PROVIDERS=google` + `EXCLUDED_REVIEWER_ADOPTION_SESSION=74` constants + check 27 sub-clause emits FAIL when `reviewer_provider: google` appears in any session 74+ audit artefact.
- D-290 `specifications/workspace-structure.md` v9 minor amendment: §10.4-M21 reopen-warrant (a) sustained-pattern threshold n≥3 status update per Gemini `findings_count: 0` n=4 empirical vindication.
- D-291 `specifications/engine-manifest.md` new engine-v14 entry per substantive bump.

## Cross-linkage

This record is the operationalisation of the empirical signal surfaced by the S073 close-time codex cross-check audit. The cross-check itself is preserved as `provenance/073-session/04-tier-2-audit-codex-cross-check.md` per S073 immutability discipline (D-017); the official S073 Gemini audit at `provenance/073-session/04-tier-2-audit.md` remains the official record per D-017 immutability. The S074 amendments operate forward: existing pre-S074 Gemini audit records are valid historical artefacts; only future reviewer-role invocations are excluded.

## Engine-version impact

Engine-v13 → engine-v14 ratified at S074 close per substantive `validation-approach.md` v7 → v8 + substantive `tools/validate.sh` update. Engine-v13 preservation depth at S073 close: 2 (S071 ratified + S072 first preservation + S073 second preservation). Engine-v14 reset depth to 0 at S074. Per content-driven-bump precedent chain S028+S033+S036+S048+S050+S058+S062+S063+S064+S071+S074: cadence concern not violated; §5.4 cadence-runaway threshold not approached (3-session gap S071→S074 is engine-conventional).
