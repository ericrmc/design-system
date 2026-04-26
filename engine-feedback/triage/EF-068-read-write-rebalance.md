---
feedback_ref: engine-feedback/inbox/EF-068-read-write-rebalance.md
triage_session: 069
status: deferred
classification: substantive-arc-blocked-on-sibling
---

# Triage — EF-068 Read/Write Rebalance

## Triage classification

**Classification: substantive-arc-blocked-on-sibling**.

EF-068-read-write-rebalance admits two coupled architectural directions (groups iii + iv per intake §Suggested Change). Both are substantive-arc-class scope:

- **Direction 3 (group iii): demote default-read surface; promote query-driven read** (the §10.4-M10 Substrate-N2 minority direction). Phase-2 records-substrate maturity (`records/minorities/M-NNN.md` + `records/watchpoints/WX-NNN.md` + `records/validation-debt/VD-NNN.md`); cross-spec mirrors collapse to single-source records-substrate; default-read surface shrinks to ~10-12 files (specs + dispatcher + per-family thin indexes).

- **Direction 4 (group iv): reduce forced-write rate**. Specifically the housekeeping-15-sub-section-per-close pattern. Move stable-state housekeeping to records-substrate frontmatter; close-narrative becomes substantively-loaded not scaffolding-loaded; trigger-based housekeeping (fires only when sub-section changes substantively); periodic preservation-claim verification cadence (every-10-sessions substantive minorities/watchpoints/OIs engagement).

Both directions are substantive (engine-definition revision + multi-spec coordination) and warrant substantive deliberation per `multi-agent-deliberation.md` v4 §When Multi-Agent Deliberation Is Required.

**Per intake's explicit "blocked-on sibling" framing**: the intake itself sequences this record's directions as **dependent on sibling EF-068-substrate-load-bearing's harness-side enforcement adoption succeeding first**. Direction 3 (records-substrate maturity) requires query-driven read; query-driven read requires substrate-as-default; substrate-as-default requires harness-side enforcement (the sibling's Direction 1). Direction 4 (reduced forced-write) requires substrate maturity (Direction 3) for the records-shift to be tractable.

**Sequencing per intake**:
- S070+ Path-AS Shape-1: primary scope is sibling EF-068-substrate-load-bearing (three-record bundle with EF-067 + EF-059 per S069 D-256).
- **S070++ Path-AS Shape-1: this record's scope** (deferred until sibling's harness-side enforcement is operational).
- S070+++ Path-AS-MAD-execution: this record's phase-2.
- S070++++ implementation arc: multi-session phase-3.

**Operator-discretionary alternative sequencing per intake**: bundle this record with sibling in **single S070+ four-record design-space**. Cost: design-space scope increases significantly (4 records × 4+ directions each); MAD lineup may need more than 4 perspectives. Tradeoff: the records are conceptually coupled (read-discipline asymmetry is the meta-frame; sibling addresses near-term enforcement; this addresses architectural rebalance) so bundling may be appropriate. **Operator did not surface four-record-bundle preference at S069 open**; default per intake = separate-scope (S070++ defer).

## Triage disposition

**Disposition**: substantive-arc-blocked-on-sibling; deferred to **S070++ Path-AS Shape-1 phase-1 synthesis** as separate-scope (own design-space, separate from the sibling's three-record bundle at S070+).

**Operator-discretionary four-record-bundle reopen warrant preserved**: at any S070+ session open, operator may surface preference to expand the S069 D-256 three-record joint-scope to a four-record bundle including this record. The expansion would require:
- S070+ Path-AS Shape-1 design-space.md scope expansion to four records.
- Phase-2 MAD lineup possible expansion beyond 4 perspectives.
- Bundle-vs-defer question explicitly surfaced in design-space per intake's "phase-1 design-space at S070+ could include explicit 'bundle-vs-defer' question for MAD deliberation" framing.

If operator does not surface four-record preference and S070+ Path-AS Shape-1 proceeds with three-record scope, this record's S070++ scope is the sequencing default per intake.

**Resolution path forecast** (default sequencing per intake):
- **S070++ Path-AS Shape-1**: phase-1 synthesis on this record's two directions (Direction 3 records-substrate maturity / Direction 4 reduced forced-write). Produces own `provenance/<NNN-session>/design-space.md` surveying:
  - Direction 3 sub-options: phase-2 minorities migration / phase-3 watchpoints + (z5) ledger + decisions migration / default-read surface shrink target (10-12 files).
  - Direction 4 sub-options: stable-state housekeeping → records-substrate frontmatter / per-session-delta-only close-narrative / trigger-based housekeeping / preservation-claim verification cadence.
  - Pre-condition gate: confirmation that sibling EF-068-substrate-load-bearing's harness-side enforcement is operational (substrate adoption rate measurable; Direction 1 (a)+(b) shipped; check 26 substrate-aware activated; check 29 candidate evaluated).
  - Q1-Q10 design questions including: which Direction 3 phase to prioritise; which Direction 4 sub-option to ship first; coupling-tradeoff between Direction 3 and Direction 4 (sequential vs parallel); minimum-viable per S062 §10.4-M16 P2 precedent.
  - Pre-ratification of phase-2 MAD per S057 D-196 precedent.
- **S070+++ Path-AS-MAD-execution**: 4-perspective two-family MAD per S058 + S062 lineup precedent.
- **S070++++ implementation arc**: multi-session phase-3 (potentially spanning multiple sessions due to records-substrate migration scope per Substrate-N3.5 phase-1 + phase-2 + phase-3 pattern from `records-contract.md` v1 §6).

**Alternative dispositions considered and rejected**:

1. **Four-record-bundle adoption at S069 D-256 (without operator preference surfaced)**: rejected. The intake explicitly defaults to three-record at S070+ + this record at S070++; the four-record-bundle option is operator-discretionary per intake. Adopting four-record without operator preference would override the intake's own sequencing recommendation. The four-record reopen warrant is preserved per disposition above.

2. **Same-session-resolution at S069**: rejected. Direction 3 + Direction 4 are both substantive-arc-class architectural revisions (records-substrate phase-2 + multi-spec coordination); single-orchestrator implementation at S069 would skip design-space-then-decide discipline + skip the prerequisite of sibling's harness-side enforcement being operational.

3. **Indefinite deferral until sibling Direction 1 ships**: rejected because indefinite deferral is not principled; the intake names a specific sequencing (S070++ post-sibling-resolution) that ties activation to operationally-observable signals (sibling harness-side enforcement operational + substrate adoption measurable). The sequencing-blocked-on-sibling classification is principled-deferral, not deferral-without-rationale.

4. **Reject EF-068-read-write-rebalance (no action warranted)**: rejected because operator surfaced concrete substantive concern; the architectural pattern is real (forced-write outpaces encouraged-read; cumulative housekeeping monotonic growth; passive maintenance debt accumulation per intake §Why It Matters); workspace has discipline for addressing operator-surfaced concerns.

## Cross-linkage with EF-068-substrate-load-bearing sibling

**Coupling**: this record's directions are blocked-on the sibling's harness-side enforcement adoption. The intake explicitly sequences this dependency:
- Direction 3 (records-substrate maturity) requires query-driven read.
- Query-driven read requires substrate-as-default.
- Substrate-as-default requires harness-side enforcement (sibling Direction 1).
- Without sibling Direction 1 operational, this record's Direction 3 produces records-as-write-only (writable-but-not-readable failure mode).
- Direction 4 (reduced forced-write) makes Direction 3 operationally valuable (once close-narrative stops replicating state, agents must query records to access state, exercising substrate).

**Joint-adoption rationale (intake's framing)**:
- Direction 3 (records-substrate maturity) makes Direction 4 (reduced forced-write) tractable.
- Direction 4 (reduced forced-write) makes Direction 3 (records-substrate) operationally valuable.
- Joint adoption produces virtuous cycle; sequential adoption (without coupling) risks records-as-write-only (D3 without D4) or close-as-stub (D4 without D3).

**Within-record coupling**: Direction 3 and Direction 4 are coupled within this record (joint-scope at S070++ Shape-1 design-space).

**Cross-record coupling with sibling**: this record is coupled with sibling at the sequencing level (this record blocks-on sibling's success). The intake's "phase-1 design-space at S070+ could include explicit 'bundle-vs-defer' question" framing is the operator-discretionary route for evaluating four-record bundle if operator surfaces preference.

## Cross-linkage with §10.4-M10 Substrate-N2 minority + §10.4-M14 P1 broader-phase-1 minority

EF-068-read-write-rebalance Direction 3 directly implements the §10.4-M10 Substrate-N2 minority direction (records-as-source-of-truth applied broadly; records-substrate phase-2 + phase-3). Per `workspace-structure.md` v9 §10.4-M10:
- Originating session: S050 (per `workspace-structure.md` v6 first M-class minority record).
- Activation warrant: phase-2+ maintenance cost exceeds projection 2× across 3 consecutive sessions; multi-hop cross-reference query class dominates 5× prose-search over 5-session window.
- Empirically: neither warrant has fired (because substrate is not used; non-use prevents data accumulation).

EF-068-read-write-rebalance Direction 3 articulates **why** the §10.4-M10 activation warrants haven't fired: substrate non-adoption is itself the blocker. The coupling with sibling EF-068-substrate-load-bearing (harness-side enforcement) addresses the substrate-non-adoption blocker; once addressed, §10.4-M10's underlying direction becomes operationally tractable.

EF-068-read-write-rebalance Evidence cites §10.4-M14 P1 broader-phase-1 minority (Session 058): "position that phase-1 should have included §10.4 minority block migration alongside SESSION-LOG.md; rejected at S058 in favour of narrow phase-1. Reopen warrant: §10.4 minority block crosses 1,500 words (currently ~1,800). **Warrant fired empirically.**" This minority's reopen warrant is now firing per evidence; EF-068-read-write-rebalance Direction 3 phase-2 minorities migration is the structural response.

The triage classification preserves these cross-references for S070++ Shape-1 design-space input.

## Forward-recommendation

S070++ Path-AS Shape-1 phase-1 synthesis on this record's two directions, deferred until sibling EF-068-substrate-load-bearing's harness-side enforcement is operational per intake's blocked-on-sibling sequencing.

**Operator-discretionary four-record-bundle reopen warrant preserved**: at S070+ session open (or any subsequent session), operator may surface preference to expand the S069 D-256 three-record joint-scope to a four-record bundle including this record. Bundle-vs-defer question may be explicitly surfaced in S070+ design-space if scope-coherence is unclear.

EF-068-read-write-rebalance triage record will be updated to `status: resolved` when phase-3 implementation lands (per resolution chain analogous to EF-058-tier-2-validation resolved-via-multi-session-arc).

## Notes

The intake's structural critique — engine passivity with laundering and maintenance; forced-write artefact-richness vs encouraged-read engagement-shallowness; cumulative housekeeping monotonic growth — is at architectural depth. Direction 3 + Direction 4 are larger arcs than the sibling's near-term harness-side enforcement directions. The principled deferral preserves the workspace's design-space-then-decide-then-implement discipline + acknowledges the intake's own sequencing recommendation.

The fourth-of-record operator-audit-catches-what-in-session-discipline-missed event (paired with sibling) per intake §Application-Scope Disposition is itself direct evidence for the architectural pattern this record names. The triage classification preserves that evidence for S070++ Shape-1 design-space input + makes the architectural arc operationally activatable when sibling's prerequisite is met.
