---
session: 033
title: Decisions — Kernel §7 revision + engine-v5 → engine-v6 + OI housekeeping + Path L validator fix
date: 2026-04-23
status: complete
---

# Decisions — Session 033

## D-106: Kernel §7 revision per §9 trigger 7 mandate; reference-validation.md v2 → v3 cascade

**Triggers met:** [d016_1, d016_2, d016_3, d023_1]

**Triggers rationale:** d016_1 — decision modifies `methodology-kernel.md` (v5 → v6 substantive). d016_2 — decision substantively revises `specifications/reference-validation.md` (v2 → v3 substantive cascade per §9 trigger 7 activated-minority adoption). d016_3 — multi-way genuine disagreement surfaced in the deliberation (3-of-4 cross-family convergence on revision direction vs Skeptic-preserver minimal-revision dissent on Q1/Q2/Q3/Q4). d023_1 — decision modifies `methodology-kernel.md`; non-Claude participation required and satisfied (Outsider GPT-5.4 via codex exec per §Acceptable Participant Kinds non-Anthropic-LLM-via-own-provider-endpoint).

**Decision.** Revise `methodology-kernel.md` v5 → v6 substantive, adopting the activated Session 014 §10.1 Skeptic "provisional substitute" framing minority direction per `reference-validation.md` v2 §9 trigger 7 firing mandate (Session 032 PD-A REJECT). Cascading substantive revision of `reference-validation.md` v2 → v3 to maintain kernel-spec coherence. Revision content per 3-of-4 cross-family deliberation convergence (Outsider GPT-5.4 + Reviser Claude + Synthesiser Claude; Skeptic-preserver Claude dissent preserved as `reference-validation.md` v3 §10.3 first-class minority).

### Kernel §7 revision content (v5 → v6)

Five substantive changes to §7:

1. **Third-sense rename.** "Reference validation" → "**Provisional reference substitute**." Reasoning: per Outsider [01d, Q1] "a label called `validation` implies a test that tells us the thing we produced is fit for its intended use. The scope paragraph already disclaims that, but the label does the rhetorical work that the paragraph tries to retract." Session 032 cross-family-symmetric saturation on PD-A (both Claude + codex GPT-5.4 emitted RoSB distinctive labels) is the type-change empirical signal that warrants type-change label response. 3-of-4 cross-family support (Outsider, Reviser, Synthesiser); Skeptic-preserver minority dissent preserved.

2. **Mandatory-dissent citation-discipline principle.** One-sentence addition to §7 third-sense paragraph: *"Any citation of reference-provisional evidence as support for a methodology-level claim must accompany the citation with at least one named contamination or scope-limitation risk (per `reference-validation.md` §8 label discipline)."* Operational detail pushed to `reference-validation.md` v3 §8 per placement-discipline convergence (2-of-4 cross-family Outsider + Synthesiser proposed split placement; Reviser proposed full kernel-level; Skeptic-preserver argued for spec-only).

3. **Scope-statement strengthening (Q3).** Integrated language per 3-of-4 convergence: saturation-profile-dependent evidential value (Reviser contribution) + cross-family-symmetric carve-out (Outsider contribution) + methodology-level vs methodology-consistent distinction (Outsider contribution) + MAY/MUST NOT/MUST citation-discipline modals (Synthesiser contribution, RFC-2119 convention flagged as external input). Skeptic-preserver's narrow-vs-broad-claim objection addressed by targeting the narrow claim (saturation-gate has false-negative modes) rather than the broad claim ("methodology is not working").

4. **Label grandfathering.** Pre-v6 artefacts carrying `validation: reference-validated` are semantically-equivalent-to `validation: reference-provisional` for citation purposes; no retroactive rewriting of sealed session records per D-017 immutability. New artefacts from engine-v6 onward use `validation: reference-provisional`.

5. **Preamble update.** §7 first line revised from "Three senses apply" to "Three senses apply: two primary (Workspace, Domain) and one provisional substitute (Provisional reference substitute)." Signals the re-categorisation.

### Reference-validation.md v2 → v3 substantive cascade

Six substantive changes to `reference-validation.md`:

1. **Rename-sync throughout.** Sense-name updated to "Provisional reference substitute" in Purpose section; Version 3 summary added; v2 preserved as `reference-validation-v2.md` with `status: superseded` and `superseded-by: reference-validation.md (v3)`.

2. **§1 C3 Stage (b) Condition 3 split into sub-cases 3a/3b.** Sub-case 3a preserves the original v2 cross-family-asymmetric-retrieval framing (Session 018 D2 pattern). Sub-case 3b adds cross-family-symmetric-reproduction (Session 032 PD-A pattern) as methodologically distinct observation class. Both reject; sub-case recording is load-bearing because 3a/3b inform different downstream remediations.

3. **§4 L1b sub-case recording.** L1b verdict file MUST record which sub-case applies when Condition 3 fires (3a asymmetric vs 3b symmetric); retained asymmetry-probe for 3a (Session 019 Reviser asymmetry-probe minority partial-vindicated).

4. **§8 label rename + three-element citation-discipline clause.** `validation: reference-validated` → `validation: reference-provisional`; grandfather clause for pre-v3 artefacts. Mandatory-dissent clause with three elements: explicit label + named-dissent-or-contamination-risk + contamination-audit pointer. Enforcement via session-scoped sealing gate + frontmatter propagation ("most-provisional label wins") + close-rotation check. Cross-family-symmetric caveat added for 3b cases.

5. **§9 trigger 7 text refreshed.** "FIRED once at Session 032 per D-104" annotation added; three re-fire conditions specified: (a) n=3 rejection threshold; (b) label-discipline violation; (c) scope-reversal without substantive justification.

6. **§10 extended with three new Session 033 first-class minorities.** §10.3 Skeptic-preserver minimal-revision minority (preferred rollback direction if v6 over-corrects); §10.3 Outsider "Constraint-derivation probe" naming minority (alternative rename preferred on methodological-sharpness grounds); §10.3 Reviser separate-OI-for-detection-gap minority (preferred if cross-family-symmetric detection-mechanism gap surfaces material design questions within 3 sessions post-033). Also added Session 033 annotations to §10.1 (activation-and-adoption event for Session 014 Skeptic) and §10.2 (vindication for Session 019 Skeptic preemptive-activation; partial-vindication-asymmetric for Session 019 Reviser asymmetry-probe).

### Rejected alternatives

**Alternative 1 — Skeptic-preserver minimal-revision (one-word "provisional" insertion only; no rename; no v3 bump).** Rejected per 3-of-4 cross-family majority. Reasoning: the cross-family-symmetric finding (Session 032 PD-A) is a type-change in evidence, not a degree-change; a type-change warrants a type-change in label (rename), not just a degree-change (one-word insertion). The label travels into citations, frontmatter, and cross-references in ways the scope-paragraph language does not — per Outsider [01d, Q1] "in field conditions... the label gets lifted out of its paragraph context." Preserved as `reference-validation.md` v3 §10.3 first-class minority with explicit rollback-direction operational warrant (if v6 over-corrects within 5 sessions, minority vindicates).

**Alternative 2 — Outsider "Constraint-derivation probe" naming.** Considered and preserved as minority. The 3-of-4 direction chose "Provisional reference substitute" to preserve parallel structure with `Workspace` and `Domain` senses, but the Outsider's alternative is methodologically sharper (names what the mechanism measures rather than what it cannot measure). Preserved as `reference-validation.md` v3 §10.3 first-class minority with explicit operational warrant for v7+ revision if external readers misunderstand the "Provisional reference substitute" framing.

**Alternative 3 — Open OI-019 (or next-available) for cross-family-symmetric detection-mechanism gap, separate from OI-016.** Reviser's suggestion [01a, Q5]. Not adopted this session; tracked as watchpoint WX-33-1 instead, per 2-of-3 Claude-perspective preference against OI-proliferation (Outsider did not take a position; Synthesiser implicitly tracked it under the infinite-loop-cap framing). Preserved as `reference-validation.md` v3 §10.3 first-class minority with explicit operational warrant for opening the OI within 3 sessions if material design questions surface.

**Alternative 4 — Defer kernel revision to Session 034 pending further PD-candidate testing.** Not considered seriously. §9 trigger 7 textual mandate ("next session after the second rejection") names Session 033 specifically; deferral is a soft violation of pre-committed trigger semantics.

**Alternative 5 — Retire reference-validation as a sense entirely and replace with a different mechanism.** Outsider raised this indirectly ("narrower claimed operating envelope than v2 assumed" [01d, Q5]) but did not propose as primary action. Not adopted this session; preserved for future consideration if re-fire condition (a) n=3 threshold triggers a deeper revision.

## D-107: Engine-v5 → engine-v6 bump declaration

**Triggers met:** [d016_1, d016_2]

**Triggers rationale:** d016_1 — decision modifies engine version enumerated in `engine-manifest.md` §2 (engine-v5 → engine-v6), which is a substantive modification to `engine-manifest.md`. d016_2 — this decision records the engine-v bump that D-106's substantive kernel + reference-validation revisions trigger per `engine-manifest.md` §5 versioning discipline.

**Decision.** Declare engine-v5 → engine-v6 per `engine-manifest.md` §5 versioning discipline. Update `engine-manifest.md` frontmatter (`last-updated: 2026-04-23`; `updated-by-session: 033`), §2 (current version `engine-v6`), §3 heading (engine-definition files at `engine-v6`), and §7 (add engine-v6 history entry documenting the bump's content-driven nature, activated-minority-adoption-precedent status, five-session preservation window 028→033, and §5.4 non-re-escalation per Session 028 D-096 precedent). Do not revise `engine-manifest.md` §5 bump-trigger criteria this session — OI-018 carries forward, per Session 028 D-096 precedent (content-driven bump; cadence question separate). The v6 entry references both substantive files changed (kernel v5 → v6; reference-validation v2 → v3) and the minor tool-side repair to `tools/validate.sh` check 22 (D-108 Path L).

**Fifth engine-v bump overall** (021 v1→v2; 022 v2→v3; 023 v3→v4; 028 v4→v5; 033 v5→v6). **Second post-cadence-maturation content-driven bump** (v5 Session 028; v6 Session 033). **First end-to-end preserved-minority-activation-and-adoption event** (Session 014 §10.1 Skeptic preserved → Session 032 §9 trigger 7 activated → Session 033 adopted).

### Rejected alternatives

**Alternative 1 — Treat Session 033 revisions as minor and preserve engine-v5.** Rejected; changes to `methodology-kernel.md` §7 (rename; strengthened scope-paragraph; mandatory-dissent principle sentence; grandfather clause) are substantive per OI-002 heuristic — they change a load-bearing kernel section, change downstream-enforced frontmatter labels, and change the kernel's rhetorical claim about reference-validation's status. `reference-validation.md` v3's §8 three-element citation clause + §1 C3 sub-case split are substantive per the same heuristic. Bundled session is substantive.

**Alternative 2 — Defer the engine-v bump to Session 034 and execute spec revisions without version bump.** Rejected; would leave `engine-manifest.md` out of sync with substantive revisions already executed, violating the §5 versioning discipline and creating a documentary drift OI.

## D-108: OI housekeeping + Path L validator fix + watchpoint advancement

**Triggers met:** [none]

**Single-agent reason:** Routine OI housekeeping + minor tool-side bug repair per Session 024 D-088 R6 / Session 030 D-100 precedent. No new normative content beyond what D-106/D-107 already record. OI state updates follow from D-106/D-107 adoption; watchpoint data-point recording follows session-close convention; validator repair is classified minor per OI-002 heuristic (bug-fix with no semantic change to what check 22 validates).

**Decisions.**

### OI-016 state transition (per D-106 adoption)

OI-016 transitions from **Open — pending kernel §7 revision per §9 trigger 7 firing at Session 032 PD-A REJECT** (Session 032 state) → **Resolved — provisionally-v2** (Session 033 state per D-106 adoption).

Disposition text (canonical): *"Resolved at Session 033 by kernel §7 v5 → v6 substantive revision (rename + mandatory-dissent principle + scope-statement strengthening) and reference-validation.md v2 → v3 substantive cascade (rename-sync + §1 C3 3a/3b split + §8 three-element citation clause + §10 three new minorities). Adopted the Session 014 §10.1 Skeptic 'provisional substitute' framing minority per §9 trigger 7 firing at Session 032. Re-opens automatically if: (a) §9 trigger 7 re-fires at n=3 with cross-family-symmetric saturation; (b) any use of `validation: reference-provisional` label in external-facing citation without the §8 mandatory-dissent three-element discipline; (c) scope-statement reduction or sense-name reversal toward `validation` without substantive justification."*

State history entry (to be added to OI-016.md):

> Session 033 per D-108: re-resolved to Resolved — provisionally-v2. Kernel §7 revised v5 → v6 (rename "Reference validation" → "Provisional reference substitute"; added mandatory-dissent citation-discipline principle; strengthened scope-statement). reference-validation.md cascaded v2 → v3 substantive (rename-sync; §1 C3 sub-case 3a/3b split; §8 three-element citation clause with `reference-validated` → `reference-provisional` label rename + grandfather clause; §10 extended with three new Session 033 minorities). engine-v5 → engine-v6 declared per D-107. Re-opening conditions specified: (a) §9 trigger 7 re-fires at n=3 with cross-family-symmetric saturation; (b) label-discipline violation; (c) scope-reversal. First end-to-end preserved-minority-activation-and-adoption event in engine history.

### OI-004 state

Unchanged at state 3 "Articulated; awaiting closure-retrospective." Session 033 advances tallies:
- Voluntary:required 10:8 → 11:9 (Session 033 is a required-trigger session via d023_1; Outsider qualifies per §Acceptable Participant Kinds non-Anthropic-LLM-via-own-provider-endpoint with `independence_basis: organization-distinct`).
- Criterion-3 cumulative count: 68 → 69 (Outsider's "type-change framing" per `01-deliberation.md` §4 shaped the synthesis's response to Skeptic-preserver's n=2 objection; this is cross-lineage-originated contribution that no Claude perspective independently produced).

### OI-002 state

No new data point specifically for OI-002 heuristic. The D-106 substantive + D-108 minor classifications are both consistent with the established heuristic; no sharpening needed. OI-002 data-point count unchanged at 13 (last data point Session 028 substantive-spec-revision).

### OI-007, OI-005, OI-006, OI-008, OI-009, OI-011, OI-012, OI-013, OI-014, OI-015, OI-018

No state change. OI-018 continues to carry forward per Session 028 D-096 precedent (cadence question separate from substantive bump; §5.4 Session 022 cadence minority does not re-escalate at v6 bump).

### Path L — validate.sh check 22 loop-bug repair

Per OI-002 heuristic + Session 024 D-088 R6 / Session 030 D-100 precedent, the Path L repair is **minor tool-side bug fix**, no engine-v bump in its own right (the v6 bump is driven by D-106/D-107 content, not by this repair). Repair content: check 22 loop restructured to iterate per-match via `grep -rHoE` rather than per-line of `grep -rn` with inner `grep -oE` that concatenated multiple archive tokens on a single source line. Placeholder-skip logic extended beyond original angle-bracket + literal-"path" cases to also skip literal-"slug" + non-`provenance/`-rooted paths (catching regex-character fragments and illustrative short-forms).

Verification. Pre-repair validator state (Session 033 open): 768 pass / 1 fail / 1 warn. Post-repair validator state (Session 033 close projected): 793 pass / 0 fail / 2 warn (new `reference-validation.md` 7,160-word soft-warn from v3 substantive content; designed soft-warn mechanism; under 8K hard ceiling). Root-cause WX-27-1 structurally-addressed, though WX-27-1 continues as forward discipline to catch future author-side patterns not yet anticipated.

### Minority activation-clock data points

Session 033 records:
- **§5.7 Pacer-advocate 85K/95K** (Session 028): 4-of-5 vindication-direction at Session 032; **5-of-5 vindication-direction at Session 033 close** (aggregate still within v3 90K/100K thresholds; projected ~68-72K post-close; well under 85K Pacer value). **§5.7 VINDICATED-COMPLETE at Session 033 close.** Fifth minority-vindication event in engine history (§5.2 Session 027; §5.6 Session 031; §5.8 Session 031; §10.2-Skeptic-preemptive Session 032; §5.7 Session 033).
- **§5.9 Synthesiser-integrator 10-session retention-window** (Session 028): 4-of-6 vindication-direction at Session 032; **5-of-6 vindication-direction at Session 033 close**. Window continues one more session.
- **§5.10 Pacer-advocate 3-session retention-window** (Session 028): 4-of-6 vindication-direction at Session 032; **5-of-6 vindication-direction at Session 033 close**. Window continues one more session.
- **§5.11 Skeptic-preserver pressure-signal-audit**: no budget-firing event this session; no data point.

**Three new first-class minorities added** to `reference-validation.md` v3 §10.3 per D-106 (Skeptic-preserver minimal-revision; Outsider "Constraint-derivation probe" naming; Reviser separate-OI-for-detection-gap).

**Engine-wide minority count.** 18 preserved at Session 032 close + 3 new Session 033 = **21 first-class minorities preserved total.** Resolution-status summary (6 of 21 affected):
- **Vindicated-complete**: §5.2 Session 027; §5.6 Session 031; §5.8 Session 031; §10.2-Skeptic-preemptive Session 032; §5.7 Session 033 (5 total).
- **Converted-to-active-spec**: §5.3 Session 028 (1).
- **Activated-and-adopted**: §10.1 Skeptic provisional-substitute (Session 032 activation; Session 033 adoption) (1; first-ever activation-and-adoption event).
- **Vindicated-direction (not-complete)**: §10.1-Skeptic+Outsider-joint-narrower-claim Session 032 (1).
- **Continued preservation** (no activation event): 12 pre-033 minorities + 3 new Session 033 minorities = 15 minorities.

### Watchpoint advancement

- **WX-22-1** witness-dumping: no new data.
- **WX-24-1** MAD growth: MAD unchanged at 6,386 (11-session no-growth streak Sessions 023–033; new longest in watchpoint history extending Session 032's 10-session record by one).
- **WX-24-2** budget-literal drift: no exercise; forward discipline continues.
- **WX-24-3** Outsider workspace-read pattern: advances to n=6 at Session 033 (required-trigger Outsider perspective for kernel §7 revision per MAD v4 §When Non-Claude Participation Is Required clause 1). Pattern remains stable across n=6 data points.
- **WX-27-1** archive-token citation fragility: **structurally addressed** by D-108 Path L validator repair + extended placeholder-skip logic. Root-cause (per-line-loop concatenating multiple matches) fixed. Watchpoint continues as forward discipline to catch unanticipated future author-side patterns, but no new firing expected under the repaired loop.
- **WX-28-1** close-rotation-exception-frequency: fifth steady-state data point at zero exceptions (0-of-5 in 10-session window; Sessions 029/030/031/032/033).
- **WX-33-1** [NEW] cross-family-symmetric detection-mechanism gap. Originating Session 033 kernel §7 revision deliberation per Reviser 01a Q5 minority. The Session 019 Reviser asymmetry-probe clause was never adopted at v2 and remains preserved as §10.2 minority (partial-vindicated-asymmetric Session 032); the cross-family-symmetric pattern (Session 032 PD-A) is not detected by any current mechanism, only recorded as pattern-observation. WX-33-1 tracks whether this detection-mechanism gap surfaces material design questions within 3 sessions post-033. If yes, Reviser separate-OI-for-detection-gap minority (`reference-validation.md` v3 §10.3) vindicates and a new OI should be opened. If no within 3 sessions, the watchpoint-only approach is vindicated.

### Close-rotation fifth steady-state rotation

Per `read-contract.md` v3 §2c close-rotation rule, at Session 033 close the default-read enumeration updates: top 6 session closes by NNN prefix = Sessions 028, 029, 030, 031, 032, 033. **Session 027 close rotates OUT of default-read** (moves to archive-surface-by-exclusion per §3); Session 033's own close enters the window. Net default-read close-file count: 6, unchanged. Physical paths unchanged. No retention-exception decisions recorded (WX-28-1 counter fifth data point at zero exceptions).

This is the fifth steady-state rotation event since Session 028 close initial exercise.

**Rejected alternatives for D-108.**

**Alternative 1 — Open OI-019 for cross-family-symmetric detection-mechanism gap.** Considered and rejected per 2-of-3 Claude-perspective preference against OI-proliferation (Reviser proposed; Skeptic-preserver and Synthesiser implicitly against). Tracked as WX-33-1 watchpoint with explicit 3-session review window; Reviser minority preserved as first-class minority in `reference-validation.md` v3 §10.3.

**Alternative 2 — Defer Path L validator fix to Session 034 as minor housekeeping.** Rejected. Validator FAIL at Session 033 open is live operational issue; leaving it uncorrected violates "leave the workspace in a coherent state at the end of every application" per PROMPT.md.

**Alternative 3 — Classify Path L as substantive (no-semantic-change-to-check but new-filter-logic).** Considered. The check's pass/fail criterion is unchanged (paths resolve or they don't); the additions are defensive filtering of non-archive-reference strings that the previous loop happened to accept by artefact of its concatenation bug. Classified minor per OI-002 heuristic (clarifies existing intent; no new validator semantics). Session 024 D-088 R6 + Session 030 D-100 precedent.
