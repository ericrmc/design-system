---
session: 033
title: Deliberation — Kernel §7 revision per §9 trigger 7 mandate
date: 2026-04-23
status: synthesis-complete
synthesizer: Claude Opus 4.7 (1M context) — session orchestrating agent, not a perspective in this deliberation (per MAD v4 §Synthesis synthesiser-identity rule)
participants_family: cross-model
cross_model: true
non_claude_participants: 1
oi004_qualifying_participants: [Outsider]
---

# Deliberation — Kernel §7 Revision (Session 033)

Synthesis of four independent perspectives: Outsider (non-Claude GPT-5.4 via codex exec), Reviser (Claude subagent), Skeptic-preserver (Claude subagent, adversarial), Synthesiser (Claude subagent). Perspectives are presented in alphabetical order by role name per MAD v4 §Synthesis synthesis-order-anchoring rule. Each perspective answered five design questions (Q1 provisional framing; Q2 mandatory-dissent clause; Q3 scope-statement strengthening; Q4 cascading revisions; Q5 OI-016 disposition) from a byte-identical shared brief with role-specific stance blocks.

Citation convention: `[01a-reviser, Q#]` / `[01b-skeptic, Q#]` / `[01c-synthesiser, Q#]` / `[01d-outsider, Q#]`. Synthesizer-original claims marked `[synth]`.

## §1 Convergence matrix

| Question | Outsider | Reviser | Skeptic-preserver | Synthesiser | Majority |
|----------|----------|---------|-------------------|-------------|----------|
| Q1 Provisional framing | **Rename** (prefers "Provisional reference substitute" or "Constraint-derivation probe") | **Rename** to "Provisional reference substitute" | Minimal — one-word "provisional" insertion in scope-statement only; oppose rename | **Rename** (Option B+) to "Provisional reference substitute" + scope-restatement | **3-of-4 rename** (cross-family) |
| Q2 Mandatory-dissent clause | Include — short kernel sentence + operational detail in reference-validation.md §8 | Include — kernel-level clause with three-element citation requirement; scope = external-facing OR methodology-level claim | Place in reference-validation.md §8 ONLY, NOT kernel | Include — kernel one-sentence principle; operational mechanism in reference-validation.md v3 | **3-of-4 include kernel-level + spec-level split** (cross-family) |
| Q3 Scope-statement strengthening | Strengthen with "methodology-level vs methodology-consistent" distinction + cross-family-symmetric carve-out | Strengthen substantially (saturation-dependence; cross-family-symmetric carve-out; L1a-not-predicting-L1b) | Current sufficient; proposed language overstates n=2 evidence | Strengthen with RFC-2119-style MAY/MUST NOT/MUST + cross-family-symmetric clause | **3-of-4 strengthen** (cross-family) |
| Q4 Cascading revisions | kernel v6 + reference-validation v3 substantive + engine-manifest §2+§7 | kernel v6 + reference-validation v3 substantive + engine-manifest §2+§7 | kernel §7 one-word only + reference-validation §8 clause (NOT v3 bump); no engine-manifest beyond OI-016 reflection | kernel v6 + reference-validation v3 substantive + engine-manifest minimum + grandfather clause | **3-of-4 reference-validation v2→v3 substantive** (cross-family) |
| Q5 OI-016 disposition | Resolved-provisionally with explicit re-opening conditions | Resolved-provisionally-v2 with new trigger; consider opening OI-017 for detection-gap | Resolved with escalation-on-n=3 disposition | Resolved-provisionally-v2 with explicit re-opening thresholds (a/b/c) | **4-of-4 Resolved with escalation triggers** (shape convergence; label-specifics vary) |

**Headline:** 3-of-4 cross-family convergence on Q1–Q4 direction (Outsider + Reviser + Synthesiser converge; Skeptic-preserver dissents on each). 4-of-4 convergence on Q5 disposition shape (Resolved with explicit re-opening conditions) with minor label-specifics variation.

The 3-of-4 convergence crosses model families (Outsider is non-Claude GPT-5.4; Reviser + Synthesiser are Claude). The dissent is intra-Claude (Skeptic-preserver). This matches the Session 028 D-096 convergence shape (3-of-4 cross-family including Outsider; 1-of-4 Skeptic-preserver dissent).

## §2 Question-by-question treatment

### Q1. Provisional framing — Rename sense to "Provisional reference substitute"

**Convergence.** Three perspectives (Outsider, Reviser, Synthesiser) independently argue for renaming the third sense in kernel §7. The shared reasoning: the label carries semantic weight into citations, frontmatter, and cross-references; scope-paragraph disclaimers do not travel with citations; the Session 014 Skeptic minority's warrant names exactly this risk and Session 032 materialises it.

**Outsider load-bearing argument** [01d-outsider, Q1]:

> "The structural reason is not rhetorical overstatement but **claim mismatch**. The brief now shows two different failure modes: Session 018: family-asymmetric saturation. Session 032: **cross-family-symmetric saturation**. The first can be narrated as 'Claude has a canon blind spot.' The second cannot."

> "A label called `validation` implies a test that tells us *the thing we produced is fit for its intended use*. The scope paragraph already disclaims that, but the label does the rhetorical work that the paragraph tries to retract."

**Reviser load-bearing argument** [01a-reviser, Q1]:

> "A scope-paragraph qualifier alone leaves the sense-name load-bearing in citations, frontmatter, and session summaries; readers and downstream authors will refer to 'the reference-validation result' and drop the paragraph. Renaming the sense puts provisionality on the label that travels."

**Synthesiser load-bearing argument** [01c-synthesiser, Q1]:

> "The §10.1 Skeptic minority activated exactly because the name 'Reference validation' reads as validation of equal standing with Domain validation. A name is load-bearing metadata; it travels into citations, frontmatter labels, and cross-references."

**Minority — Skeptic-preserver** [01b-skeptic, Q1]:

> "The current kernel §7 already contains the load-bearing content the activated minority wanted... The word 'provisional' was absent in the v5 adoption, but the *content* the word encodes is present."

> "Ask the information-gain question directly: what operational behaviour changes if we add the word 'provisional'? A reader who understands the current scope-statement already knows reference-validation does not establish intended-use functioning and does not substitute for domain validation. Adding 'provisional' as a label may be cosmetic rather than structural."

> "n=2 does not justify this."

**Synthesis finding.** The Skeptic-preserver's information-gain challenge is load-bearing and must be addressed directly. The three-perspective response: information content is not just logical implication of the scope-statement — it is also the label's travel-behavior in citations. Per Outsider [01d-outsider, Q1]: "in field conditions — cited artefacts, external readers, downstream sessions — the label gets lifted out of its paragraph context." This is not speculation: Session 032 PD-A REJECT is the empirical instance of exactly that pattern (both model families reading the constraint-statement-without-reference produced the reference's distinctive labels, treating them as derivable-from-scratch; the scope-paragraph language did not travel to the subagents' training-time exposure). [synth]

The n=2 stability argument is preserved as Skeptic-preserver minority dissent. The 3-of-4 cross-family majority reads the evidence as type-change, not degree-change [01d-outsider, cross-question observations]: "Session 018 was a signal that Claude's canon overlaps with the reference pool. Session 032 is a signal that *the reference pool overlaps with the canon shared across pretraining families*." A type-change in the evidence warrants a type-change in the label; n=2 of structurally-different domains is sufficient for type-change inference per the pre-committed §9 trigger 7 conditions.

**Convergence direction for Q1:** rename the third sense to **"Provisional reference substitute."** Adopted per 3-of-4 cross-family majority. Frontmatter label `validation: reference-validated` transitions to `validation: reference-provisional`.

Alternative name "Constraint-derivation probe" proposed by Outsider [01d-outsider, Q1] is preserved as minority alternative; it names what the mechanism measures (capacity) rather than what it cannot measure (fitness). The 3-of-4 direction favors "Provisional reference substitute" because it preserves the `Reference` sense-family parallel to `Workspace` and `Domain`. "Constraint-derivation probe" preserved as §10-equivalent minority dissent pending future revision.

### Q2. Mandatory-dissent clause — Split kernel principle + spec operational detail

**Convergence.** Three perspectives (Outsider, Reviser, Synthesiser) converge on including a mandatory-dissent clause. They split on placement: Reviser proposes full kernel-level clause; Outsider and Synthesiser propose kernel one-sentence principle + reference-validation.md §8 operational detail. Skeptic-preserver dissents on kernel placement ("§8 only").

**Outsider argument for split placement** [01d-outsider, Q2]:

> "The kernel should state the principle; the clause should be mechanically checked by `validate.sh` against the two load-bearing surfaces above (labels on produced artefacts; methodology-level claims). Put the checker in `reference-validation.md` §8 and hook it from the kernel. This avoids the pattern where the kernel accumulates enforcement text it cannot itself test."

**Synthesiser argument for split placement** [01c-synthesiser, Q2]:

> "Kernel §7 should contain the principle ('a non-Claude-family divergence check is required'); the operational mechanism belongs in reference-validation.md where the three-cell protocol is specified. This respects the kernel's role as the principle-bearing document and reference-validation.md's role as the operational spec."

**Skeptic-preserver argument for spec-only placement** [01b-skeptic, Q2]:

> "If every trigger-firing adds a clause to kernel §7, the kernel grows heavy with exception-language and stops being the durable stable core it is meant to be. The kernel is the most-cited document in the workspace; each addition is re-baselined downstream."

**Synthesis finding.** Skeptic-preserver's stability-of-kernel argument is persuasive against heavy enforcement-text additions. The 2-of-4-cross-family compromise (Outsider + Synthesiser) — kernel states principle in one sentence; spec carries operational detail — honors stability concerns while giving the principle durability. Reviser's three-element enforcement checklist [01a-reviser, Q2] is more operational detail than principle; placing that in reference-validation.md v3 rather than kernel §7 matches the placement-discipline Skeptic-preserver argues for. [synth]

**Convergence direction for Q2:** kernel §7 adds one-sentence principle; reference-validation.md v3 adds operational detail per §8 label-discipline extension.

Proposed kernel sentence (integrated from [01d-outsider, Q2] and [01c-synthesiser, Q2]):

> *Any citation of reference-provisional evidence as support for a methodology-level claim must accompany the citation with at least one named contamination or scope-limitation risk (per `reference-validation.md` §8 label discipline).*

Proposed reference-validation.md v3 §8 operational detail (integrated from [01a-reviser, Q2] three-element checklist): any citation must carry (i) the `reference-provisional` label, (ii) a named dissenting view from the sealed record or explicit acknowledgement of contamination risk naming the saturation profile (copyrighted / public-domain; single-family / cross-family-symmetric), (iii) a pointer to the contamination audit. Enforcement via sealing gate, frontmatter propagation ("most-provisional label wins"), close-rotation check.

Skeptic-preserver dissent preserved as minority: the kernel should carry zero enforcement text; the §8 clause alone suffices.

### Q3. Scope-statement strengthening — Adopt with cross-family-symmetric carve-out

**Convergence.** Three perspectives (Outsider, Reviser, Synthesiser) converge on strengthening the scope-statement to address the Session 032 cross-family-symmetric finding. They propose different framings of the strengthening language (Outsider: methodology-level vs methodology-consistent; Reviser: saturation-dependence phrasing; Synthesiser: RFC-2119 MAY/MUST NOT/MUST). Skeptic-preserver dissents: current language is sufficient.

**Outsider load-bearing framing** [01d-outsider, Q3]:

> "A passing reference-provisional result in a domain where cross-family-symmetric reproduction was observed at any stage of §1 C3 is not methodology-level evidence; it is at most methodology-consistent evidence."

**Reviser load-bearing framing** [01a-reviser, Q3]:

> "Reference validation's evidence about the methodology's capacity to derive artefacts under stated constraints *in domains where the reference is not heavily represented in pretraining corpora*. It does not establish that the methodology is working, only that it can produce outputs satisfying stated constraints under conditions where pretraining contamination does not dominate."

**Synthesiser load-bearing framing** [01c-synthesiser, Q3]:

> "A Provisional-reference-substituted artefact MAY be cited as methodology-capacity evidence. It MUST NOT be cited as evidence of domain function. It MUST carry the `validation: reference-provisional` label."

**Skeptic-preserver objection** [01b-skeptic, Q3]:

> "Two rejections do not show 'the methodology is not working' — they show that the *saturation gate does not catch Claude-family-asymmetric and cross-family-symmetric reproductions at pre-seal*. Those are different claims. The narrower claim is already implicit in the current scope-statement. The broader claim ('the methodology is not working') is not supported by n=2 and risks mis-calibrating the reader."

**Synthesis finding.** Skeptic-preserver's narrow-vs-broad-claim distinction is correct and load-bearing. The adopted strengthening should target the narrow claim (saturation-gate has false-negative modes including cross-family-symmetric) rather than the broad claim ("methodology is not working"). Reviser's phrasing ("does not establish that the methodology is working, only that it can produce outputs satisfying stated constraints under conditions where pretraining contamination does not dominate") risks the mis-calibration Skeptic-preserver flags — "methodology is working" is too broad; "methodology can derive artefacts under these specific conditions" is the accurate claim. [synth]

Outsider's "methodology-level vs methodology-consistent" distinction is more portable than Reviser's phrasing; Synthesiser's RFC-2119 MAY/MUST NOT/MUST is enforceable in validator-layer (though introduces an external pretraining convention, flagged by Synthesiser [01c-synthesiser, Q3]). The convergence-integration preserves Outsider's portable distinction + Synthesiser's enforceable modal language, addressing Skeptic-preserver's mis-calibration objection by keeping the narrow saturation-gate claim rather than the broad "methodology-working" claim.

**Convergence direction for Q3:** strengthen scope-statement with (a) cross-family-symmetric carve-out, (b) methodology-level vs methodology-consistent distinction, (c) saturation-profile-dependent evidential value, (d) MAY/MUST NOT/MUST citation-discipline modals.

Proposed integrated scope-statement paragraph (draft; final text in D-106):

> *Reference-provisional evidence is qualified by the candidate's saturation profile. It supplies evidence about the methodology's capacity to derive an artefact under stated constraints **only to the extent that the reference is not recoverable from shared pretraining corpora across the Produce and judging families.** It does not establish that the artefact functioned in its intended use. It does not substitute for Domain validation when a domain-actor is available. A passing reference-provisional result in a domain where cross-family-symmetric reproduction was observed at any stage of §1 C3 is not methodology-level evidence; it is at most methodology-consistent evidence. A reference-provisional artefact MAY be cited as methodology-capacity evidence. It MUST NOT be cited as evidence of domain function. It MUST carry the `validation: reference-provisional` label; label transition to `validation: domain-validated` occurs only upon subsequent Domain validation.*

Skeptic-preserver dissent preserved: current language is sufficient; adopted strengthening risks over-correction.

### Q4. Cascading revisions — kernel v6 + reference-validation v3 substantive + engine-manifest §2/§7

**Convergence.** Three perspectives (Outsider, Reviser, Synthesiser) converge on a coordinated multi-file revision: kernel §7 revised (v5 → v6) + reference-validation.md substantive revision (v2 → v3) + engine-manifest.md update (§2 + §7 for engine-v5 → v6). Skeptic-preserver dissents: minimum is kernel one-word + reference-validation §8 clause without v3 bump.

**Outsider coherence argument** [01d-outsider, Q4]:

> "**The minimum coherent set is larger than v5-preserved + engine-manifest v6 bump.** I would do three things: 1. **Kernel §7 v5 → v6**, substantive... 2. **`reference-validation.md` v2 → v3**, substantive — because the kernel change renames a sense that `reference-validation.md` currently defines and labels. A v3 bump makes the spec-pair coherent."

**Reviser coherence argument** [01a-reviser, Q4]:

> "Why reference-validation.md v3 is required rather than deferrable. The label change and the saturation-profile audit requirement are load-bearing for the citation-discipline clause in Q2 to be enforceable. If reference-validation.md still names the output `reference-validated`, the kernel text and the spec conflict, and operators will default to the spec when producing frontmatter."

**Synthesiser ordered-revision-plan** [01c-synthesiser, Q4]:

> "1. **kernel v5 → v6**: rename third sense; add cross-family-symmetric clause; add MAY/MUST NOT/MUST citation-discipline sentence. ~80 words of change.
> 2. **reference-validation.md v2 → v3 (substantive)**: update L1b gate criteria to distinguish Claude-family-asymmetric from cross-family-symmetric saturation; update three-cell protocol record-fields to include `cross_family_symmetric_check` outcome; update frontmatter-label spec from `reference-validated` to `reference-provisional`; update §9 automatic re-opening trigger text to reference the revised sense name.
> 3. **engine-manifest.md**: §2 (current-version table) updates kernel to v6, reference-validation to v3, engine-v to v6. §7 (change-history) adds one row summarising Session 033 revision. No other §7 changes. Minimum surface."

**Skeptic-preserver narrow-coherence argument** [01b-skeptic, Q4]:

> "A v3 bump implies substantive revision. My argument: the cross-family-symmetric finding is n=1 (Session 032 PD-A only). One instance is not a pattern. Adding it to reference-validation.md as a specification-level finding over-commits the spec to a pattern we have not yet confirmed. Keep it as an open watchpoint in the session record and the OI-016 disposition, not as spec-level text."

**Synthesis finding.** The coherence argument (Reviser's "if reference-validation.md still names the output `reference-validated`, the kernel text and the spec conflict") is structurally load-bearing and cannot be dismissed by the n=1 argument. The label-rename alone forces the spec to update — operationally, any session producing a frontmatter label under v6 kernel needs the matching v3 spec to define that label. Skeptic-preserver's "keep cross-family-symmetric as watchpoint not spec-level text" is partially addressable: the v3 spec can reference the cross-family-symmetric pattern as a recorded observation (n=1 at Session 033 adoption) rather than as a characterized general pattern — preserving the honesty of the evidence base while still updating the operational fields. [synth]

**Convergence direction for Q4:** adopt the three-file coordinated revision (kernel v6 + reference-validation v3 substantive + engine-manifest §2/§7 engine-v6 entry). The reference-validation v3 minimum-viable content is per Synthesiser's enumeration [01c-synthesiser, Q4]: rename-sync + L1b cross-family-symmetric sub-check + frontmatter label rename + §9 trigger 7 re-fire condition clarification + grandfather clause. Estimated ~150–250 words of net change.

Grandfather clause (integrated from [01a-reviser, Q1] + [01d-outsider, Q4] + [01c-synthesiser, Q4]): existing artefacts labelled `validation: reference-validated` (Session 009/010 external artefacts; any other prior usage) are semantically-equivalent-to `validation: reference-provisional` without retroactive rewriting. Historical session records remain untouched per D-017 immutability.

Skeptic-preserver dissent preserved: the v3 bump is excess; a §8 clause-only non-version-bump addition would suffice.

### Q5. OI-016 disposition — Resolved with explicit re-opening conditions

**Convergence.** 4-of-4 on shape: OI-016 transitions Open → Resolved with new disposition that includes explicit re-opening conditions. Label specifics vary (Reviser/Synthesiser: "Resolved-provisionally-v2"; Skeptic-preserver: "Resolved with escalation-on-n=3"; Outsider: "Resolved-provisionally, with explicit re-opening conditions"). Re-opening conditions content is shared across perspectives (n=3 threshold; label-discipline violations; domain-actor contradiction).

**Outsider re-opening conditions** [01d-outsider, Q5]:

> "Re-opening conditions I would record alongside the re-resolution: Any third structurally-different-domain Cell 1 rejection with cross-family-symmetric reproduction (n=3 makes the observation-class a regularity, not a pair). Any use of the `reference-provisional` label in an external-facing citation without the mandatory-dissent clause. Any reduction of the §7 scope paragraph or rename of the sense back toward `validation` without a concurrent substantive justification."

**Reviser + Synthesiser re-opening conditions** [01a-reviser, Q5] + [01c-synthesiser, Q5]: both converge on n=3 threshold for further revision; both propose OI-017-like forward-tracking for cross-family-symmetric detection mechanism.

**Skeptic-preserver re-opening condition** [01b-skeptic, Q5]: single condition — third structurally-different-domain rejection fires §9 trigger 7 at n=3.

**Synthesiser infinite-loop framing** [01c-synthesiser, Q5]:

> "Infinite re-opening loop concern: yes, this is a real structural risk. If reference-validation is inherently limited by cross-family-symmetric saturation on public-domain inputs, then each Resolved-provisional → §9-fires → re-opens cycle is a sign the mechanism itself is the ceiling, not the policy around it. The threshold (a) caps the loop at n=3 — a third fire forces a deeper revision (possibly: retire reference validation as a sense, or constrain it to non-public-domain corpora only). This makes the loop finite-by-design."

**Synthesis finding.** 4-of-4 shape convergence. The label "Resolved-provisionally-v2" or "Resolved with explicit re-opening conditions" is equivalent in effect; choose the label that minimizes ambiguity. The re-opening-conditions set integrates Outsider's three conditions + Synthesiser's infinite-loop framing. The n=3 threshold cap is load-bearing: it makes the re-opening loop finite-by-design, which addresses the Synthesiser's structural concern. [synth]

Reviser's proposal to open a separate OI for the cross-family-symmetric detection-mechanism gap (Reviser's suggestion: "call it OI-017 — cross-family-symmetric saturation detection") [01a-reviser, Q5] is a separate question. Session 033 does not open this OI automatically; it is recorded as a watchpoint (WX-33-1 or equivalent) and subject to operator ratification at session close. [synth]

**Convergence direction for Q5:** OI-016 transitions Open → **Resolved — provisionally-v2** with three re-opening conditions: (a) third structurally-different-domain rejection with cross-family-symmetric reproduction fires (§9 trigger at n=3 equivalent); (b) any use of the `reference-provisional` label in external-facing citation without mandatory-dissent discipline; (c) reduction or reversal of scope-statement or sense-name without substantive justification. The cross-family-symmetric detection-mechanism gap tracked as new watchpoint (WX-33-1).

## §3 Preserved first-class minorities from this deliberation

Per MAD v4 §Synthesis preserve-dissent rule, the following minorities are preserved from Session 033 deliberation:

### §3.1 Skeptic-preserver minimal-revision minority (Session 033, adversarial perspective)

**Position.** Kernel §7 revision should be minimum-viable: one-word "provisional" insertion in scope-statement; no rename; no kernel-level mandatory-dissent clause (place in reference-validation.md §8 only); no reference-validation v3 substantive bump. The activated minority warrant is honored at minimum scope; n=2 does not justify broader revision.

**Quote** [01b-skeptic, Cross-question observations]:

> "The activated Session 014 minority warrant is vindicated on the scope-of-concern axis: reference-validation *is* producing false-negatives at the saturation gate, as the Skeptic feared. It is not yet vindicated on the revision-direction axis: n=2 supports minimal revision, not the broader 'provisional substitute' reframing."

> "The stability argument. Every session that fires a trigger will generate pressure to revise the kernel. The kernel survives if revisions are calibrated to evidence, not to trigger-activation. n=2 is the activation threshold, not the characterisation threshold. Reserve the larger revisions for n≥3."

**Operational warrant.** If Session 034+ demonstrates the broader v6 revision over-corrected (e.g., operators find the `reference-provisional` label cumbersome with no corresponding evidence-quality improvement; citation discipline failures do not decrease; kernel stability erodes), the minimum-revision path is the preferred revision direction. Concretely: if a v6 → v7 revision is proposed within 5 sessions post-v6 that rolls back scope-statement strengthening, the Skeptic-preserver's n=2-is-insufficient position is vindicated.

**Applies to Q1 (rename vs one-word), Q2 (kernel placement), Q3 (scope-statement strengthening), Q4 (v3 bump necessity).** Does not apply to Q5 (Skeptic-preserver converges with majority on Q5 shape).

### §3.2 Outsider "Constraint-derivation probe" naming minority (Session 033)

**Position.** The renamed sense could more accurately be called "Constraint-derivation probe" than "Provisional reference substitute," because it names what the mechanism measures (derivation capacity under blind conditions) rather than what it cannot measure (fitness validation). 3-of-4 direction favored "Provisional reference substitute" because it preserves parallel structure with `Workspace` and `Domain` senses, but the Outsider's alternative is methodologically sharper.

**Quote** [01d-outsider, Q1]:

> "I slightly prefer the second because it names what the mechanism actually measures (can the methodology derive a constraint-consistent artefact when a reference is hidden) rather than what it cannot measure (validation of fitness)."

**Operational warrant.** If future external readers misunderstand "Provisional reference substitute" (e.g., citing it as a "validated reference" anyway despite the provisional qualifier), the "Constraint-derivation probe" naming is the preferred revision direction for a v7+ kernel revision. Alternatively, if `reference-validation.md` v3+ operational practice reveals that the sense is used primarily as capacity-measurement rather than substitute-for-validation, the rename may be preferable on pure-naming-accuracy grounds.

### §3.3 Reviser separate-OI-for-detection-gap minority (Session 033)

**Position.** The cross-family-symmetric saturation finding surfaces a detection-mechanism gap (the Session 019 Reviser asymmetry-probe does not detect this pattern) that is analytically separate from the validation-pathway question OI-016 tracks. A separate OI (OI-017 or next-available number) should be opened to track the detection-mechanism gap as its own problem.

**Quote** [01a-reviser, Q5]:

> "A second OI (call it OI-017 — cross-family-symmetric saturation detection) may be appropriate to open now, separate from OI-016, to track the detection-mechanism gap (Reviser asymmetry-probe does not see it) as its own problem rather than folding it into the validation-pathway OI."

**Operational warrant.** If within 3 sessions post-033, the cross-family-symmetric detection gap surfaces material design questions that the OI-016 re-opening conditions do not adequately track (e.g., a structurally-separate detection mechanism is proposed that does not belong in the OI-016 validation-pathway scope), the separate-OI approach is vindicated. If no such material design question surfaces, the watchpoint-only approach is vindicated.

## §4 Recorded impact — non-Claude perspective shaping outcomes

Per OI-004 criterion 3 (recorded impact), the Outsider (non-Claude GPT-5.4 via codex exec) shaped two specific outcomes in this deliberation:

1. **Type-change framing** [01d-outsider, cross-question observations]. Outsider's "Session 018 was a signal that Claude's canon overlaps with the reference pool. Session 032 is a signal that *the reference pool overlaps with the canon shared across pretraining families*" provides the load-bearing distinction the synthesis uses to reject Skeptic-preserver's "n=2 is insufficient" objection. Without this framing, the synthesis would weigh n=2 as a numerical threshold; with it, the n=2 represents two instances of structurally-different evidence types and warrants type-change response. This framing is cross-lineage-originated — no Claude perspective independently produced the "reference pool overlaps with cross-family canon" framing (Reviser named cross-family-symmetric saturation but did not reach the "shared canon" structural framing).

2. **"Methodology-level vs methodology-consistent" distinction** [01d-outsider, Q3]. Outsider's adoption of experimental-science "consistent-with vs evidence-for" vocabulary (flagged as external pretraining import) provides the specific strengthened scope-statement language adopted in the convergence direction. No Claude perspective proposed this portable distinction — Reviser proposed saturation-dependence phrasing; Synthesiser proposed RFC-2119 modals. Outsider's contribution is the framing that downstream citations can mechanically adopt: a passing result is methodology-consistent, not methodology-level evidence, in saturation-vulnerable domains.

Both contributions are cross-lineage-distinct (no Claude perspective independently produced either framing) and the synthesis adopts both. This is OI-004 criterion 3 evidence-of-impact at the cross-lineage-originated level, comparable to Session 022 Outsider frame-completion contribution that shaped read-contract.md v1 and Session 028 Outsider "laundering the activation" critique that disambiguated Path G values choice.

## §5 Limitations

Per MAD v4 §Limitations required content for Claude-majority deliberations:

- **All three Claude perspectives share a model family** (Claude Opus 4.7 via Agent tool). Shared training produces shared blind spots on this question's substance (kernel revision drafting; specification integration; engine-v bump classification). The Outsider provided cross-family divergence-check but is a single non-Claude participant; sustained practice beyond this deliberation still required for OI-004 closure (currently state 3 "Articulated; awaiting closure-retrospective").
- **Parallel isolation prevents conversational anchoring, not training-distribution anchoring.** Three Claude instances given the brief reached high convergence on Q1 (rename), Q2 (split placement), Q3 (strengthen), Q4 (v3 bump); the Skeptic-preserver's adversarial role was instantiated by brief-instruction rather than by independent training — this may be weaker adversarial-discipline than an independently-motivated critic.
- **Brief-writing has no adversary.** The orchestrating agent's brief establishes the five questions and the framing; alternative framings (e.g., "is reference-validation the right mechanism at all," "should the methodology retire reference-validation," "should Session 033 defer the kernel revision to Session 034 pending domain-actor recruitment") were not offered as deliberation-space options.
- **The synthesis step is the pattern's highest-risk single-agent re-entry point.** The orchestrating agent (writing this synthesis) is a Claude subagent; synthesis conventions applied (per-perspective quote-over-paraphrase; dissent-preservation; `[synth]` markers on synthesizer-original claims; citation to raw-output files).
- **A single non-Claude participant narrows OI-004 less than its presence suggests.** Outsider's contribution shaped two outcomes (§4 above); both are preserved as evidence-of-impact. But sustained practice over many sessions is required for criterion-4 closure; Session 033 is the 10th session recording voluntary-or-required non-Claude participation (voluntary:required ratio 10:8 entering Session 033; advances to 11:9 post-Session 033 if counted).

## §6 Summary — Convergence direction for Session 033 decisions

| Question | Convergence direction |
|----------|----------------------|
| Q1 | Rename third sense to "Provisional reference substitute" |
| Q2 | Kernel §7 adds one-sentence mandatory-dissent principle; operational detail in reference-validation.md v3 §8 |
| Q3 | Strengthen scope-statement with saturation-profile-dependent evidential value + cross-family-symmetric carve-out + MAY/MUST NOT/MUST modals + methodology-level vs methodology-consistent distinction |
| Q4 | kernel v5 → v6 + reference-validation v2 → v3 substantive + engine-manifest.md §2/§7 engine-v6 entry + grandfather clause for existing labels |
| Q5 | OI-016 transitions Open → Resolved — provisionally-v2 with three re-opening conditions (n=3 threshold; label-discipline violations; scope-reversal) |

Decisions D-106 (kernel §7 revision + reference-validation v3 cascade), D-107 (engine-v5 → engine-v6 bump), D-108 (OI housekeeping incl. OI-016 disposition + Path L validator fix) are constructed on this convergence base in `02-decisions.md`.

Skeptic-preserver minimal-revision minority preserved as §3.1 per MAD v4 dissent-preservation rule. Outsider "Constraint-derivation probe" naming preserved as §3.2. Reviser separate-OI-for-detection-gap preserved as §3.3.
