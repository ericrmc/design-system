---
session: 020
title: Decisions — Workspace Scaling Deliberation
date: 2026-04-22
status: complete
---

# Decisions — Session 020

## D-080: Adopt R1, R2, R3 minimum-change set — `workspace-structure.md` §SESSION-LOG minor amendment; OI-007 monitoring annotation; CLAUDE.md mempalace orchestrator-convenience paragraph; engine-v1 preserved

**Triggers met:** `[d016_3]`

**Triggers rationale:** R1 amends `workspace-structure.md` §SESSION-LOG.md classified as **minor** per OI-002 heuristic (elaboration making explicit what existing practice already contains; points at canonical detail already in provenance `03-close.md`; no new rules, required fields, triggers, or required artefacts). Per Sessions 005/006/017 precedent, minor revisions do NOT fire `d016_2` — only substantive revisions do. `d016_3` fires because the adoption text synthesises four-perspective positions into revised content per reasonable-disagreement deliberation rubric. R2 is an `open-issues.md` annotation (development-provenance) — not a spec revision — so no `d016_*` fires for R2 alone. R3 amends `CLAUDE.md` which is not an engine-definition file per `engine-manifest.md` §3 — not a spec revision in the d016_2 sense. No `d023_*` fires: no kernel revision, no multi-agent-deliberation.md revision, no validation-approach.md Tier 2 revision, no OI-004 state change asserted. Voluntary non-Claude participation per v3 §When Non-Claude Participation Is Required (Outsider included without trigger requirement).

**Decision.**

Adopt R1, R2, R3 as specified in `01-deliberation.md` §4. Summary:

**R1 — Minor amendment to `workspace-structure.md` §SESSION-LOG.md.** Replace current text with expanded text that (a) retains the "one line per entry" form (Markdown table row), (b) replaces "brief note" with "summary", (c) names variance scaling to session complexity, (d) points to provenance `03-close.md` as canonical detail location. Classification: minor per OI-002 heuristic. Engine-v1 preserved (no engine-manifest.md §5 version bump).

**R2 — OI-007 monitoring-dimension annotation in `open-issues.md`.** Append Session 020 annotation adding per-OI-annotation-size as second monitoring dimension for OI-007 (previous dimension: OI count). Defer structural directory-split per "unless unwieldy" clause; preserve Splitter per-OI-directory minority with specific operational warrants. No workspace-structure.md change. No engine-version impact.

**R3 — CLAUDE.md orchestrator-convenience mempalace paragraph.** Add paragraph under §Tools classifying `mempalace` v3.1.0 as orchestrator-convenience (not engine-definition). Paragraph explicitly records three hands-on-grounded caveats (search is semantic not exact-words; wake-up is not recency-weighted; mine does not dedupe versioned specs) and the candidate-discovery-only framing. `mempalace.yaml` and `entities.json` added to `.gitignore` if mempalace init is run. engine-manifest.md §3 unchanged — mempalace is NOT in the engine-definition set.

**Rationale (condensed from `01-deliberation.md`).**

Four perspectives converged on 3-of-4 cross-family agreement against engine-v2 bump (Tooler Claude + Skeptic Claude + Outsider non-Claude vs Splitter Claude), 3-of-4 cross-family against immediate structural split (Tooler orthogonal + Skeptic defer + Outsider defer-after-restore vs Splitter split-now), and 4-of-4 against mempalace as engine-definition. The adopted set is the minimum-viable change that (a) addresses the operator-named friction by (i) ratifying the observed summary-drift pattern, (ii) making the canonical-detail location explicit, (iii) providing an optional retrieval tool as orchestrator convenience, and (b) preserves engine-v1 until actual external-application exercise produces evidence that larger changes are warranted.

Outsider's frame-challenge contribution — "indexes drifted to dossiers" type-drift diagnosis — is the session's strongest cross-family signal (second frame-replacement after Session 017 H4). The restoration-direction (rewrite historical entries back to index brevity) is preserved as a first-class minority with operational warrant rather than adopted, because (a) retrospective rewrite of 19 session entries is not minimum-viable-change, (b) R1's pointer to `03-close.md` operationalises the type-role separation the Outsider named without the rewrite, (c) the Outsider minority's activation warrant enables Session 022+ to adopt restoration-direction if R1 amendment's variance-clause bounding proves insufficient.

Tooler's hands-on empirical finding — `D-074` query returned zero D-074 results, contradicting mempalace's "exact words" self-description — is load-bearing for R3's caveat text. Without this finding, R3 would have described mempalace differently; the hands-on testing produced the specific honest-limits framing now in the CLAUDE.md paragraph.

Skeptic's minimum-change set (R1 minor + R2 annotation, no mempalace) is the floor of the adoption. The deliberation adopted this floor plus R3 (Tooler's orchestrator-convenience proposal) as the ceiling-short-of-engine-change.

**Adoption classification per OI-002 heuristic.**

- R1: **minor revision** to `workspace-structure.md`. Makes explicit what existing practice already contains. No new normative content. v3 preserved in place; no v-bump (no `workspace-structure-v3.md` copy needed since the current file retains its v3 designation with the minor amendment in place, per precedent for minor amendments in Sessions 005/006/009/017). `last-updated: 2026-04-22` + `updated-by-session: 020` frontmatter fields updated.
- R2: open-issues.md annotation, not a spec revision. No OI-002 classification needed (OI-002 heuristic is for spec revisions).
- R3: CLAUDE.md amendment. CLAUDE.md is not an engine-definition spec (per engine-manifest.md §3); OI-002 heuristic does not apply. Precedent: Session 016 recorded `uv tool` authorisation in CLAUDE.md without spec-level consequence.

**Anti-laundering verification.** The aggregate of R1+R2+R3 does not: lower any threshold; drop any check; soften any mechanism-failure criterion; widen any validation label; remove any pre-existing rule. R1 widens "brief note" → "summary" with a bounded variance clause; bounding is operationalised via the §5.3 Outsider minority activation warrant (restoration-direction vindicated if bounding fails within 5 sessions). R3 introduces a new orchestrator-convenience path with explicit candidate-discovery-only framing and §5.4 Skeptic minority activation warrant (defer-entirely vindicated on any search-laundering incident). R2 is additive monitoring only.

**Rejected alternatives.**

- **Splitter full proposal** (split both files into directories; engine-v1 → engine-v2; new required frontmatter fields + directory shapes for both `open-issues/` and `session-log/`): rejected 3-of-4 cross-family. engine-v2 bump before first external-application exercise of engine-v1 is premature per Skeptic's Q6 argument; per-OI-directory structure reduces whole-set visibility per Skeptic's Q2 argument; retrospective rewrite of 19 entries exceeds minimum-viable-change. **Preserved as first-class minorities §5.1 (open-issues directory) and §5.2 (SESSION-LOG per-session files)** with concrete operational warrants.

- **Outsider restoration-direction** (rewrite SESSION-LOG entries back to brief one-line index; treat provenance 03-close.md as canonical detail layer; aggressive content-normalisation): not adopted as main direction despite being the strongest single cross-family diagnostic contribution. R1 operationalises the type-role separation the Outsider named (via the "canonical detail lives in 03-close.md" pointer) without requiring the aggressive rewrite. **Preserved as first-class minority §5.3** with activation warrant on R1 bounding failure.

- **Skeptic defer-entirely on tools** (no mempalace adoption in any form including CLAUDE.md): not adopted. R3 adopts orchestrator-convenience use with explicit hands-on caveats; 2-of-4 cross-family (Tooler + Outsider) for permissive use outweighs 1-of-4 (Skeptic) for no-use. **Preserved as first-class minority §5.4** with activation warrant on any search-laundering incident.

- **Tooler CLAUDE.md paragraph without hands-on caveats**: reshaped to include hands-on findings as mandatory caveat section. Tooler's own proposal already contained these caveats per the 01b Q4 "This proposal does NOT claim..." section.

- **No action**: not adopted. 3-of-4 agree the friction is at least somewhat real (Skeptic dissents). The no-action option reduces to "Skeptic strong-defer" which is preserved as R3-rejection-direction via §5.4 only; the structural questions have the minimum-viable-change response via R1+R2.

## D-081: OI state housekeeping — OI-002 ninth data point; OI-004 tally unchanged at 6-of-3 (voluntary non-advancing; ratio 7:6); OI-007 annotated per D-080 R2; four first-class minorities preserved; WX-20-1 watchpoint

**Triggers met:** `[none]`

**Triggers rationale:** D-073 / D-077 / D-079 housekeeping-decision precedent. Records OI consequences of D-080 without adding new normative content. No kernel revision (no d016_1); no spec creation or substantive revision (no d016_2); no reasonable-disagreement deliberation (d016_3 is on D-080 only; D-081 is housekeeping reflection); no operator-marked load-bearing (no d016_4); no D-023 spec-list revisions (no d023_1/2/3); no OI-004 state change (no d023_4). All clauses clean; `[none]` is consistent with content per Q7.

**Decision.**

- **OI-002 gains 9th data point.** Session 020 D-080 R1 classified minor ("brief note" → "summary" + variance clause + canonical-detail pointer). The five-point heuristic continues to hold stable. The n=3 narrow-single-purpose-spec-creation pattern (identity.md, reference-validation.md, engine-manifest.md) from Session 017 is unchanged by Session 020. No formal OI-002 heuristic update this session; monitor.

- **OI-004 tally unchanged at 6-of-3.** Session 020 is voluntary non-Claude participation (Outsider included without D-023 trigger firing on D-080). Sixth voluntary non-advancing non-Claude session after Sessions 007, 008, 010, 012, 013, 019. Voluntary-to-required ratio rebalances from 6:6 to **7:6** (voluntary advances by 1; voluntary now exceeds required for first time since Session 013 and Session 019's brief rebalance). Criterion-3 gains **five concrete Outsider-sourced data points from Session 020** (see §7 of `01-deliberation.md`): (1) frame-challenge "indexes drifted to dossiers" diagnosis; (2) scan-surface-vs-detail-surface separation principle shaping R1's canonical-detail pointer; (3) strict-sequential minimum-viable-change ordering shaping minority activation warrants; (4) portability-loss argument against engine-definition tool adoption (cross-family independent from Skeptic); (5) semantic-retrieval staleness pretraining-sourced concern corroborated by Tooler hands-on. Criterion-3 cumulative **55** across Sessions 005–020 (50 through Session 019; 5 added in Session 020). Criterion 4 (articulation of "substantively different training provenance") remains **unmet**.

- **OI-004 note on Outsider contribution genre.** Session 017 introduced frame-replacement as a new Outsider contribution kind (H4 layered model) beyond the prior third-way split-resolution pattern from Sessions 009/010/011. Session 020 is the **second frame-replacement** contribution (type-drift diagnosis) — establishing a pattern of two instances across sessions. For any future criterion-4-articulation deliberation, the frame-replacement pattern is evidence that non-Claude perspectives' training-distribution-difference produces distinctively valuable contributions beyond within-frame synthesis. Noted for that future deliberation.

- **OI-007 annotated per D-080 R2.** Per-OI annotation-size added as second monitoring dimension. Count remains 12 active, 5 resolved. No count change this session; no new OI opened or resolved. Splitter per-OI-directory minority recorded as §5.1 of `01-deliberation.md` with three-item operational warrant (segment-read OI-housekeeping failure; count-tally disagreement with git; 50K-token file ceiling).

- **OI-009 G/O/K/S evaluation of Session 020 self-work.** Session 020 is Path (E) operator-directed agenda (deliberation topic proposed by operator, not agent-selected). G (translation to external frame): passes — the scaling friction is visible to external applications as they accumulate provenance. O (narrows external-action decision space): passes — orchestrator-convenience tool path explicit; minorities with activation warrants enable future sessions to navigate unambiguously. K (external-reader visibility): passes — file-size friction and orchestrator-convenience classification are both reader-visible concerns. S (specific-obstacle resolution): passes — operator-named blocker (both files exceed ceiling) has three concrete mitigations (R1/R2/R3). OI-009 not activated.

- **OI-015 laundering-gap.** Session 020 surfaced operator input explicitly per brief §2; perspectives treated it as input not fact. Kernel §1 domain-reading reconciliation clause operated as intended. No laundering detected. OI-015 not activated; positive example of the reconciliation working analogous to Session 013 annotation.

- **OI-016 unchanged.** No re-opening triggers activate from Session 020 actions. Trigger 5 counter remains at 1 (Session 018 count). Trigger 6 not softened. Trigger 7 at 0 of 2 structurally-different-domain rejections. No action affects reference-validation.md v2.

- **OI-005, OI-006, OI-008, OI-011, OI-012, OI-013, OI-014 unchanged.**

- **Four new first-class minorities preserved** at `01-deliberation.md` §5 (Splitter per-OI directory; Splitter per-session SESSION-LOG files; Outsider restore-to-brief-index; Skeptic defer-entirely on tools). Each has operational warrant. Not opened as new OIs per Session 015/016/019 precedent (OI-007 scaling pressure argues against redundant OI proliferation when the concern is held in spec/deliberation minorities).

- **WX-20-1 watchpoint recorded.** Session 020's R3 relies on orchestrator discipline to treat mempalace output as candidate-discovery only. This is the session's weakest-bonded mitigation per synthesis §11. Activation trigger: first session in which the orchestrator cites mempalace output that is not verifiable against source via Read (i.e., a search-laundering incident). On activation, the §5.4 Skeptic defer-entirely minority is vindicated and R3's CLAUDE.md paragraph becomes candidate for removal.

**Rejected alternatives.**

- **Open new OI for tool adoption discipline.** Considered but rejected per Session 015/016/019 precedent. OI-007 scaling pressure (12 active OIs) argues against proliferation. Concern is held in §5.4 Skeptic minority + WX-20-1 watchpoint. Sufficient.

- **Activate OI-015 (laundering-gap).** Considered for R3's orchestrator-discipline dependency. Rejected: R3 is orchestrator-convenience use of optional tooling, not a pretrained-intuition-laundered-as-domain-reading pattern. The OI-015 activation trigger is specifically "laundering pattern observed and recorded" which has not occurred; the risk of such a pattern is prospective (addressed via WX-20-1).

- **Declare D-080 triggers as `[none]`.** Considered. Rejected: D-080 adopts text synthesised from four-perspective deliberation with preserved minorities, satisfying d016_3 per Session 019 D-078 precedent (d016_3 fires on reasonable-disagreement deliberation producing spec amendment text). The R1 amendment text exists because four perspectives produced distinct positions; that is exactly d016_3's trigger condition.
