---
session: 033
title: Perspective — Synthesiser
date: 2026-04-23
status: independent-phase-complete
perspective: synthesiser
committed_at: 2026-04-23T00:00:00Z
---

# Perspective — Synthesiser

System-level coherence view. The revision must land as a minimum coherent set across kernel §7, reference-validation.md, engine-manifest.md, and OI-016 disposition, with activation-clock implications for the 18 preserved minorities properly handled. I treat this as one connected surgical change, not four parallel edits.

## Q1. Provisional framing

Recommend **Option B+**: rename the sense to **"Provisional reference substitute"** AND add a single scope-restatement bullet at the top of the sense body. Rationale: the §10.1 Skeptic minority activated exactly because the name "Reference validation" reads as validation of equal standing with Domain validation. A name is load-bearing metadata; it travels into citations, frontmatter labels, and cross-references. The current frontmatter token `validation: reference-validated` should become `validation: reference-provisional` to propagate the rename. This is a surface change with system-wide reach — downstream consumers see the rename even without reading §7 body text.

Why not rename-only (Option A): rename without body-text strengthening leaves the three-cell protocol reading the same way, so the scope creep that §10.2 Skeptic predicted re-emerges. Why not body-only (Option C): body-only without rename leaves the label `validation: reference-validated` still carrying asymmetric semantic weight into future sessions. The compound change is cheaper than two sequential changes because the rename and the scope-bullet share one engine-v bump.

Concrete language for the scope-bullet (place as first paragraph of the sense body):

> **Provisional reference substitute** applies when a session produces an external-intent artefact and no domain-actor is available. It is a provisional substitute that supplies evidence about methodology capacity; it does not and cannot establish domain function. When a domain-actor later becomes available, Domain validation supersedes and the artefact's label transitions.

## Q2. Mandatory-dissent clause

Include, at **reference-validation.md scope, not kernel §7 scope**. Kernel §7 should contain the principle ("a non-Claude-family divergence check is required"); the operational mechanism belongs in reference-validation.md where the three-cell protocol is specified. This respects the kernel's role as the principle-bearing document and reference-validation.md's role as the operational spec.

Proposed kernel §7 addition (one sentence, appended to the Provisional reference substitute paragraph):

> The protocol requires a non-Claude-family cross-family divergence check; cross-family-symmetric reproduction on a public-domain constraint is a rejection signal, not a convergence signal.

This sentence does two things: (1) mandates dissent structurally, (2) encodes the Session 032 finding that cross-family-symmetric reproduction inverts the previously-assumed "convergence = validity" reading. The word "public-domain" is important — it prevents a future lenient reading that treats any cross-family match as dispositive.

Corresponding reference-validation.md v3 operational detail: L1b gate criterion must specify that symmetric verbatim reproduction across families on a public-domain corpus fails the gate, distinct from Session 018's Claude-family-asymmetric pattern. Session 019 Reviser asymmetry-probe minority (partial-vindicated-asymmetric) is addressed by keeping the asymmetric-probe as one of two sub-checks, not by replacing it.

## Q3. Scope-statement strengthening

Current scope-statement paragraph is close but lacks teeth. Strengthen by adding the cross-family-symmetric clause proposed in Q2, plus a sentence making the provisional status textually explicit (not just implicit in the rename):

> A Provisional-reference-substituted artefact MAY be cited as methodology-capacity evidence. It MUST NOT be cited as evidence of domain function. It MUST carry the `validation: reference-provisional` label; label transition to `validation: domain-validated` occurs only upon subsequent Domain validation.

The MAY/MUST NOT/MUST phrasing (RFC-2119-style) is load-bearing for citation discipline. External input flag: RFC-2119 keyword convention is a pretraining-sourced idea; I note it explicitly as an external import. It is standard enough in spec documents that its use here is low-risk, but the Reviewer perspective should confirm it is consistent with the engine's existing drafting conventions.

## Q4. Cascading revisions — smallest coherent set

Propose the following **ordered revision plan**:

1. **kernel v5 → v6**: rename third sense; add cross-family-symmetric clause; add MAY/MUST NOT/MUST citation-discipline sentence. ~80 words of change.
2. **reference-validation.md v2 → v3 (substantive)**: update L1b gate criteria to distinguish Claude-family-asymmetric from cross-family-symmetric saturation; update three-cell protocol record-fields to include `cross_family_symmetric_check` outcome; update frontmatter-label spec from `reference-validated` to `reference-provisional`; update §9 automatic re-opening trigger text to reference the revised sense name. This is a v3 because the L1b gate change is operationally substantive — it will change Cell 1 verdicts in future sessions.
3. **engine-manifest.md**: §2 (current-version table) updates kernel to v6, reference-validation to v3, engine-v to v6. §7 (change-history) adds one row summarising Session 033 revision. No other §7 changes. Minimum surface.
4. **OI-016**: see Q5.
5. **Label-propagation pass**: no sweeping rewrite of past sessions. A single forward-looking note in reference-validation.md v3 stating that existing `reference-validated` labels are grandfathered semantically equivalent to `reference-provisional` for citation purposes; new sessions use the new label. This avoids a 30+ file historical rewrite that would not change engine behaviour.

Minimum-viable reference-validation.md v3 content (Q4 sub-question): (a) rename-sync, (b) L1b cross-family-symmetric sub-check added, (c) frontmatter label rename, (d) §9 trigger 7 text refreshed to clarify it has fired once and specify re-fire conditions, (e) grandfather clause. Estimated ~150–250 words of net change. Do not expand the protocol with new cells or new layers in this bump — that would exceed minimum coherent set and risk under-consulted additions.

## Q5. OI-016 disposition

Recommend **Resolved-provisionally-v2** with an explicit re-opening threshold. Keeping OI-016 Open pending reference-validation.md v3 is the alternative, but since v3 is part of this session's coherent revision bundle, the issue can close at session close with the rest of the bump.

Re-opening threshold language (to be placed in OI-016's disposition record):

> Re-opens automatically if: (a) §9 trigger 7 fires a third time (n=3) with cross-family-symmetric saturation on a public-domain corpus under the revised L1b gate; OR (b) a Cell 1 verdict is overturned by operator after strict-vs-lenient halt-and-surface at a rate exceeding one per eight sessions over any eight-session window; OR (c) a Domain-actor contradicts a Provisional-reference-substitute artefact's methodology-capacity claim.

Infinite re-opening loop concern: yes, this is a real structural risk. If reference-validation is inherently limited by cross-family-symmetric saturation on public-domain inputs, then each Resolved-provisional → §9-fires → re-opens cycle is a sign the mechanism itself is the ceiling, not the policy around it. The threshold (a) caps the loop at n=3 — a third fire forces a deeper revision (possibly: retire reference validation as a sense, or constrain it to non-public-domain corpora only). This makes the loop finite-by-design.

## Cross-question observations

**Engine-v bump classification.** Session 028 D-096 precedent (content-driven, not cadence-driven) holds. This revision is clearly content-driven: kernel §7 rename + cross-family clause + reference-validation.md substantive L1b change. §5.4 Session 022 cadence minority does not re-escalate. The bump is engine-v5 → v6, and the v6 designation is earned by kernel content change, not by the seven-session gap since v5.

**Minority-preservation accounting.** Session 033 creates at minimum: (1) activation-outcome record for §10.1 Skeptic provisional-framing; (2) vindication-outcome record for §10.2 Skeptic preemptive-activation; (3) potentially new first-class minorities from the four-perspective deliberation itself if any perspective disagrees with the majority direction. The 18 preserved minorities do not need re-escalation unless directly contradicted by v6 text. §10.2 Reviser asymmetry-probe (partial-vindicated-asymmetric, not-engaged-symmetric) is preserved as-is — the revised L1b keeps asymmetry-probe as one sub-check, so the minority remains live for its asymmetric-case relevance. No escalation needed.

**Coherence of revision direction.** The §10.1 activation (provisional framing) and §10.2 vindication (preemptive-activation) together form a two-part revision: rename the sense AND mandate dissent. These are not independent — the mandate-dissent clause operationalises what the provisional-framing rename signals. Treating them as one bundle is cheaper and clearer than sequencing them across two engine-v bumps.

**Sequencing risk.** The biggest system-level risk is under-specifying the cross-family-symmetric vs Claude-family-asymmetric distinction in L1b. If v3 under-specifies, the next session's Cell 1 operator will face the same strict-vs-lenient halt-and-surface ambiguity Session 032 hit. Recommend the L1b revision include at least one worked example from Session 018 (asymmetric) and one from Session 032 (symmetric) as reference cases embedded in the spec.

**External-input flags.** RFC-2119 keyword convention (MAY/MUST NOT/MUST) is pretraining-sourced; use is reasonable but Reviewer should confirm consistency with existing drafting conventions. No other external imports identified.
