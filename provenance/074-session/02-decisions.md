---
session: 074
title: Session 074 decisions — Path-L per operator-directed substantive amendment; Gemini permanently excluded from reviewer roles + family-distinctness REMOVED per operator-directive at S074 open; engine-v13 → engine-v14 ratified
date: 2026-04-26
status: complete
---

# Decisions — Session 074

Seven decisions: D-286 Path-L per operator-directed substantive amendment ratified + D-287 EF-073 engine-feedback record filed and resolved same-session + D-288 validation-approach.md v7 → v8 substantive revision (family-distinctness REMOVED + google-provider EXCLUDED clause (d) added) + D-289 tools/validate.sh substantive update (EXCLUDED_REVIEWER_PROVIDERS constant + check 27 sub-clause) + D-290 workspace-structure.md v9 minor amendment (§10.4-M21 reopen-warrant (a) status update) + D-291 engine-v13 → engine-v14 ratified per substantive bump + D-292 housekeeping `[none]`.

## D-286: Path-L per operator-directed substantive amendment ratified

**Triggers met:** [d016_2]

**Triggers rationale:** d016_2 fires per substantive revision to `validation-approach.md` v7 → v8 (engine-definition spec) + substantive update to `tools/validate.sh` (engine-definition tool) per S074 D-288 + D-289. d016_3 NOT fired per operator-direct directive ("no further MAD discussion on the merits of keeping Gemini because it is gone"); single-perspective scope per operator-policy authority on reviewer-family selection.

**Single-agent reason:** operator-direct directive per §10.4-M10 written-warrant clause (c) operator-surfacing channel cumulative count n=10 → n=11 per S036/S057/S060/S061/S063/S064/S066/S068/S069/S072/**S074** chain. Subject matter is operator-policy authority (reviewer-family selection); engineering judgment per d023_3 trigger applies-but-overridden by operator-binding-directive. Per S048 D-154 first-of-record operator-directed inbox-record resolution precedent + S066 first-of-record Path L per operator-surfaced priority directive precedent, both extended to substantive-class engine-definition revision at S074. Operator-directed-substantive-engine-definition-revision pattern reified at n=2 (S066 minor-classified per OI-002 archive-pack-restructure + S074 substantive-classified per OI-002 substantive-arc).

**Non-Claude participation:** skipped per operator-directive ("no further MAD discussion"). Reason: operator-policy authority on reviewer-family selection. retry_in_session: not-applicable per operator-directive scope-bounding.

**Decision:** Path-L per operator-directed substantive amendment adopted at S074 per S066 precedent extended. S073 D-282 pre-ratification (Path-AS phase-3.1 implementation per (γ-6) staged hybrid) **DEFERRED to S075+** per operator-direct supersession. (γ-6) direction adopted at S073 D-275 remains binding for S075+ phase-3.1 execution.

**Path-justification per (z12)**: Path-L per operator-directive is the directly directed path per operator-surface at S074 open. Path-AS phase-3.1 implementation per S073 D-282 — DEFERRED per operator-direct supersession. Path A (Watch) — NOT APPLICABLE per substantive amendment scope. Path PD (operator-surfaced new spec class) — operator did not surface new spec class scope; just family-rule + provider-exclusion. Path T (triage) — engine-feedback inbox 0 new at session-open; EF-073 record filed AT S074 open per operator-directive (Path-T-as-secondary-not-primary scope).

**D-129 twenty-eighth-consecutive + D-138 twenty-eighth-consecutive** clean exercises.

## D-287: EF-073 engine-feedback record filed and resolved same-session

**Triggers met:** [none]

**Triggers rationale:** Per `engine-feedback/INDEX.md` triage discipline + S048 D-154 first-of-record operator-directed inbox-record resolution precedent extended to substantive-class engine-definition revision: filing + same-session resolution is procedural-recording per operator-directive substantive resolution.

**Non-Claude participation:** N/A per [none] triggers (procedural-recording).

**Decision:** Engine-feedback record `EF-073-gemini-excluded-and-reviewer-family-rule-relaxation` filed in `engine-feedback/inbox/` and triage record in `engine-feedback/triage/` at S074 session-open per operator-directive verbatim. Operator-directive content recorded in inbox §Operator-directive section. Status: resolved at S074 close per D-288 + D-289 + D-290 + D-291 substantive amendments. INDEX row added at engine-feedback/INDEX.md (resolved count 9 → 10; new count 0; triaged count 6 unchanged).

Cross-linkage: empirical basis recorded at `provenance/073-session/04-tier-2-audit-codex-cross-check.md` (1,447 words; codex `findings_count: 2` on identical evidence packet) + `provenance/073-session/04-tier-2-audit.md` (Gemini `findings_count: 0`); the cross-check is the load-bearing substrate for operator-directive at S074 open.

## D-288: validation-approach.md v7 → v8 substantive revision

**Triggers met:** [d016_2]

**Triggers rationale:** d016_2 fires per substantive revision to engine-definition spec touching semantic Tier 2 validation per `multi-agent-deliberation.md` v4 §When-Non-Claude-Required clause 3 ("Creates or substantively revises `validation-approach.md` in ways that touch semantic (Tier 2) validation"). The §Tier 2.5 reviewer-family rule revision touches reviewer mechanism semantics directly.

**Single-agent reason:** operator-direct directive per §10.4-M10 written-warrant clause (c) operator-surfacing channel cumulative count n=11 (per D-286 single-agent rationale carrying forward verbatim). Subject matter is operator-policy authority on reviewer-family selection; engineering judgment per d016_2 trigger applies-but-overridden by operator-binding-directive ("no further MAD discussion on the merits of keeping Gemini because it is gone"). Per S048 D-154 + S066 first-of-record operator-directed precedent extended to substantive-class engine-definition revision at S074. Operator-directed-substantive-engine-definition-revision pattern reified at n=2.

**Non-Claude participation:** skipped per operator-directive. Reason: operator-policy authority on reviewer-family selection; subject matter does not plausibly expose Claude-family blind spots — operator is the policy authority on reviewer family selection, and the empirical evidence (S073 codex cross-check; sustained Gemini findings_count=0 n=4) is workspace-internal not Claude-family-perspective-derived. retry_in_session: not-applicable per operator-directive scope-bounding.

**Decision:** Substantive revision `validation-approach.md` v7 → v8:

(a) **REMOVE** v7 §Tier 2.5 reviewer-family family-distinctness requirement (was: "The reviewer's family MUST differ from the orchestrator's family at the organisation level per `tools/validate.sh` PARTICIPANT_ORGANISATION_CLOSED_SET").

(b) **ADD** new clause (d) to v8 §Tier 2.5 reviewer-family rule: "a member of the `google` provider family. The `google` provider is permanently excluded from reviewer roles per operator-directive at S074. Existing S063+S067+S071+S073 Gemini audit records remain valid as historical artefacts; no future reviewer-role invocation of google is permitted. Acceptable reviewer providers: any in `tools/validate.sh` PARTICIPANT_ORGANISATION_CLOSED_SET except `google` (operationally: `{anthropic, openai, local, other-named}` plus future-named providers)."

(c) **PRESERVE** v7 reviewer-overlap-disclosure-with-counterweighting-check discipline verbatim at v8 (sole counter-pressure to family-overlap; mandatory `reviewer_overlap_with_recent_mad_perspectives:` field disclosure + scope-handling per (i) excluded items OR (ii) counterweighting check).

(d) **PRESERVE** v7 §Tier 2.5 reviewer-family clauses (a) orchestrator + (b) close-author/primary-implementer + (c) accountable-doer verbatim at v8 (unchanged; renumbered as (a)+(b)+(c) before new (d) addition).

(e) **PRESERVE** v7.

v7 preserved as `specifications/validation-approach-v7.md` `status: superseded`.

**Rejected alternatives:**

- **Status quo at v7** — REJECTED per operator-direct directive (binding; no MAD per §Opt-out).
- **Excluding google in `tools/validate.sh` PARTICIPANT_ORGANISATION_CLOSED_SET** rather than as separate constant — REJECTED per closed-set integrity for past audit attribution (S063+S067+S071+S073 Gemini audits remain valid historical artefacts; closed-set still includes google for participant_organisation field per check 19; only EXCLUDED for reviewer-role per new EXCLUDED_REVIEWER_PROVIDERS constant).
- **Template revision at S074** — REJECTED per operator-directive scope-bounding ("relax same-family limits as needed" + "Gemini is no longer to be used"); template v3 revision is separate scope deferred to future Path-AS / Path-PD per (z7) lock-in-after-n=2 explicit-deliberation-surface requirement.

## D-289: tools/validate.sh substantive update

**Triggers met:** [d016_2]

**Triggers rationale:** d016_2 fires per substantive update to engine-definition tool (new check sub-clause + new constants).

**Single-agent reason:** operator-direct directive per §10.4-M10 written-warrant clause (c) operator-surfacing channel cumulative count n=11 (per D-286 single-agent rationale carrying forward verbatim); the validate.sh update operationalises the v8 spec change adopted at D-288 per same operator-policy authority. Subject matter does not plausibly expose Claude-family blind spots — operator-direct policy authority on reviewer-family selection extends to validator enforcement of that policy. Per S048 D-154 + S066 first-of-record operator-directed precedent extended.

**Non-Claude participation:** skipped per operator-directive. Reason: operator-policy authority extends to tool-level operationalisation of the same policy; validate.sh update is mechanical implementation of D-288 v8 spec rule. retry_in_session: not-applicable per operator-directive scope-bounding.

**Decision:** Substantive update to `tools/validate.sh`:

(a) **NEW** constant `EXCLUDED_REVIEWER_PROVIDERS="google"` added at config-block (`readonly EXCLUDED_REVIEWER_PROVIDERS="google"`).

(b) **NEW** constant `EXCLUDED_REVIEWER_ADOPTION_SESSION=74` added at config-block (per session-number-gating discipline).

(c) **NEW** check 27 sub-clause: when `last_session_num >= EXCLUDED_REVIEWER_ADOPTION_SESSION` AND `audit_artefact` contains `^reviewer_provider:[[:space:]]*google` line, emit FAIL with rationale message naming `validation-approach.md` v8 §Tier 2.5 reviewer-family rule clause (d) per S074 D-288.

Implementation preserves existing v7 check 27 sub-clauses (§2 + §7 sections + scope_coverage_table + bootstrap-limited-confidence label) verbatim per v7 → v8 scope-bounded change.

## D-290: workspace-structure.md v9 minor amendment

**Triggers met:** [none]

**Triggers rationale:** Per OI-002 minor classification: §10.4-M21 reopen-warrant (a) status update is additive-only annotation (no removal; no revision to existing minority position text); preserves load-bearing minority-warrant text verbatim while annotating empirical vindication.

**Non-Claude participation:** N/A per [none] triggers.

**Decision:** Minor amendment to `specifications/workspace-structure.md` v9:

§10.4-M21 P2 prompt-template-first / defer-spec-revision-to-S067+ reopen-warrant (a) sustained-pattern threshold n≥3 **status update**: empirically vindicated at n=4 per S063+S067+S071+S073 Gemini findings_count=0 pattern + S073 codex cross-check produced findings_count=2 on identical input. Reviewer-prompt-template v3 revision deferred to future Path-AS / Path-PD scope per (z7) lock-in-after-n=2 explicit-deliberation-surface requirement (S074 operator-directive scope-bounded to family-rule + provider-exclusion, not template revision). The §10.4-M21 reopen-warrant (a) preservation continues forward as warrant for future template-revision scope.

v9 retained per OI-002 minor classification (additive annotation; no structural change).

## D-291: engine-v13 → engine-v14 ratified per substantive bump

**Triggers met:** [d016_2]

**Triggers rationale:** d016_2 fires per substantive revision to engine-definition file per `engine-manifest.md` §5 substantive-vs-minor heuristic. Substantive scope: validation-approach.md v7 → v8 (substantive per OI-002) + tools/validate.sh substantive update (substantive per OI-002) + workspace-structure.md v9 minor (additive only).

**Single-agent reason:** operator-direct directive per §10.4-M10 written-warrant clause (c) operator-surfacing channel cumulative count n=11 (per D-286 single-agent rationale carrying forward verbatim); engine-v14 ratification is the manifest-level recording of the substantive bump that D-288 + D-289 effected per same operator-policy authority. Subject matter does not plausibly expose Claude-family blind spots — engine-version increment is mechanical recording per `engine-manifest.md` §5 versioning discipline. Per S048 D-154 + S066 first-of-record operator-directed precedent extended.

**Non-Claude participation:** skipped per operator-directive. Reason: engine-v14 ratification is mechanical manifest update reflecting D-288 + D-289 substantive scope; no engineering judgment beyond what D-288 + D-289 already substantively decided. retry_in_session: not-applicable per operator-directive scope-bounding.

**Decision:** Engine-v13 → engine-v14 ratified at S074 close per substantive bump. New §7 engine-version history entry added to `specifications/engine-manifest.md` per engine-v14 entry shape (per S071 engine-v13 entry precedent + content-driven-bump precedent chain extension).

Engine-v13 preservation depth at S073 close: 2 (S071 ratified + S072 first preservation + S073 second preservation). Engine-v14 reset depth to 0 at S074. Per content-driven-bump precedent chain S028+S033+S036+S048+S050+S058+S062+S063+S064+S071+**S074**: cadence concern not violated; §5.4 cadence-runaway threshold not approached (3-session gap S071→S074 is engine-conventional). §10.4-M25 P2 cadence-depth concern at engine-v14 reset to depth-0; future engine-v15 bump preservation forecast is engine-conventional within engine-v9 depth-8 second-longest precedent.

Engine-v14 introduces **operator-directed-substantive-engine-definition-revision pattern reified at n=2** (S066 engine-manifest restructure per operator-surfaced priority directive minor-classified per OI-002 archive-pack-restructure-of-active-default-read-spec + **S074 validation-approach.md v7 → v8 substantive per operator-directive**). The S074 instance is the first-of-record substantive-class operator-directed engine-definition revision; S066 was minor-classified.

## D-292: Housekeeping `[none]` (15 sub-sections; forty-sixth-consecutive)

**Triggers met:** [none]

**Triggers rationale:** Per S041 D-126 + standing housekeeping discipline + forty-sixth-consecutive `[none]`-trigger pattern per S074 close.

**Non-Claude participation:** N/A per [none] triggers.

**Decision:** Housekeeping `[none]` at S074 close per standing discipline:

1. **§10.4-M10 written-warrant clause (c) operator-surfacing channel cumulative count** advances n=10 → **n=11** at S074 open (S036/S057/S060/S061/S063/S064/S066/S068/S069/S072/**S074** chain).

2. **WX-28-1 forty-fourth close-rotation S068 OUT S074 IN at S074 close** zero retention-exceptions per `read-contract.md` v6 §2c close-rotation rule. S068 03-close.md (5,151 words) rotates OUT; S074 03-close.md enters retention window.

3. **WX-24-1 MAD v4 forty-seventh-session no-growth streak preserved at S074 close** (32-session run from S042 reset; extends S073's 31-session record). MAD v4 spec unchanged at S074 (operator-directive scope-bounded to validation-approach.md + tools/validate.sh + workspace-structure.md + engine-manifest.md; no MAD v4 amendment).

4. **Forty-sixth-consecutive housekeeping `[none]`-trigger pattern** at S074 close per D-292. Pattern stable across forty-six consecutive close-time housekeeping decisions since D-126 Session 041.

5. **D-129 twenty-eighth-consecutive + D-138 twenty-eighth-consecutive clean exercises** at S074 open per 00-assessment §1 path-justification.

6. **§5.6 GPT-family-concentration window-ii** advances nine-consecutive → **ten-consecutive** at S074 phase-3.1-implementation-deferred operator-directed close per codex reviewer participation at S074 close (codex preferred per operator-directive; codex-family interrupts streak per S058+S062+S064+S071+S073 codex-family precedent).

7. **Engine-v14 ratified at preservation depth 0 at S074 close** per D-291. Engine-v13 preservation across S072+S073 = depth 2; engine-v14 reset to 0.

8. **engine-feedback/INDEX.md status update** at S074 close per D-287 (EF-073 row added at top; resolved count 9 → 10).

9. **validation-debt/index.md unchanged at S074** (VD-003 status remains in-progress per S073 D-284; review_by_session: S076 unchanged; no close/defer/escalate at S074).

10. **Periphrastic-form discipline applied throughout S074 artefacts** per S065 honest-limit 11 forward-direction reified at **n=7** (S068 + S069 + S070 + S071 + S072 + S073 + S074 close-narratives all applied; S074 preemptive). Check 27 keyword-matching heuristic over-fire surface avoided.

11. **Substrate-exercise pattern at S074 (n=4 in β-phase post-S071 D-264 codification window)** per S071+S072+S073+S074 chain (S074 inherits from S073 per same-conversation-continuation-from-S073 context). Per VD-003 gating condition (b): n=4 reaches first-triangulation-floor; n=5 across S075-S076 will complete first triangulation per existing review_by_session: S076.

12. **Operator-directed-substantive-engine-definition-revision pattern reified at n=2** (S066 minor-classified + S074 substantive-classified). First-of-record substantive-class operator-directed engine-definition revision at S074.

13. **First-of-record events at S074**: substantive-class operator-directed engine-definition revision per S066 minor-classified precedent extended; engine-v14 ratified per operator-directed substantive bump (engine-v13 was S071 cross-family-MAD-adopted; engine-v14 is operator-directed-without-MAD).

14. **EF-068-read-write-rebalance four-record-bundle reopen warrant per S069 D-255 NOT ACTIVATED at S074** (operator-directive scope-bounded to family-rule + provider-exclusion; close-rotation S068 OUT alone discharges aggregate-budget pressure per `read-contract.md` v6 §2b obligation). Reopen warrant remains preserved as standing operator-discretionary surface.

15. **`forward_references('S075')` substrate-required step at S075 session-open** per `prompts/development.md` engine-v13/v14 substantive amendment per S071 D-264 (β-phase discipline carries forward from S071 + S072 + S073 + S074 to S075). Structured declaration `substrate_session_open: exercised | unavailable | skipped` + `substrate_evidence:` required in S075 00-assessment per check 29 WARN-only enforcement.

## §Pre-ratifications carried into S075+

- **Path-AS phase-3.1 implementation per (γ-6) staged hybrid** (S073 D-282 pre-ratification): RECOVERED at S075+ per S074 operator-directive supersession-then-resumption discipline. (γ-6) direction adopted at S073 D-275 remains binding for S075+ phase-3.1 execution: CM1+CM3 capture + SCD-3 schema + check 26 substrate-aware branch + reviewer-prompt-template v3 minimum-viable extension; substantive `validation-approach.md` v8 → v9 codifying full §(z6) digest schema spec; engine-v14 → engine-v15 candidate at S075 phase-3.1 close per substantive bump.

- **VD-003 phase-3 activation gating conditions (a)+(b)+(c)** carry forward to S075+ per S073 D-284 + S074 (no change). (a) DISCHARGED at S073 D-276; (b) IN PROGRESS at n=4 (S074 inherits); (c) DISCHARGED at S073 D-277.

- **§10.4-M30 through §10.4-M35 reopen warrants** carry forward to S075-S077 retention window per S073 D-283 (no S074 status updates per operator-directive scope-bounding).

- **Reviewer-prompt-template v3 revision** deferred to future Path-AS / Path-PD scope per (z7) lock-in-after-n=2 explicit-deliberation-surface requirement.

- **EF-068-read-write-rebalance separate-scope at S075++ per S069 D-255** preserved; operator-discretionary four-record-bundle reopen warrant standing per §10.4-M35 reopen-warrant-activation-not-implementation-bundling discipline.

- **§10.4-M21 reopen-warrant (a) status update** per S074 D-290: empirically vindicated at n=4 per S063+S067+S071+S073 Gemini findings_count=0 + S073 codex cross-check; preservation continues forward as warrant for future template-revision scope.

- **Engine-v14 preservation depth at S074 close: 0** per D-291. Engine-v15 candidate at S075 phase-3.1 implementation close per substantive bump (γ-6 implementation).

## §Engine-feedback INDEX disposition

Per D-287:

**EF-073-gemini-excluded-and-reviewer-family-rule-relaxation**: status `resolved` at S074 close per D-288 + D-289 + D-290 + D-291 substantive amendments. Resolution chain: filed at S074 open per operator-directive verbatim → triaged at S074 open per substantive classification → resolved at S074 close per substantive engine-definition amendments. INDEX row added at top of records table.

## §First-class minorities preserved at S074 close

**No new first-class minorities at S074** per single-agent operator-directed scope (no MAD per §Opt-out; no genuine perspective dissent to preserve).

§10.4-M21 P2 prompt-template-first reopen-warrant (a) status update per D-290 (empirical vindication at n=4; preservation forward).

Engine-wide minority count: **60 unchanged at S074** (54 at S071/S072 + 6 new at S073 D-283; no new minorities at S074).

## §Engine-v14 ratification at S074 close

Engine-v13 → engine-v14 ratified per D-291 substantive bump. Engine-v13 preservation depth at S073 close: 2 (S071 ratified + S072 first preservation + S073 second preservation). Engine-v14 reset depth to 0 at S074. Engine-v15 candidate at S075 phase-3.1 implementation close per (γ-6) substantive bump per S073 D-282 pre-ratification.
