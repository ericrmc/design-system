---
session: 032
title: L1b Saturation Test Verdict — PD-A Rule of St. Benedict Ch 58 — REJECT
date: 2026-04-23
status: complete
cell: 1
step: l1b-verdict
candidate: PD-A (Rule of St. Benedict Chapter 58 "Of the Discipline of Receiving Brothers")
verdict: REJECT
reject_condition: §1 C3 Stage (b) Condition 2 (verbatim distinctive labels emitted by both model families)
---

# L1b Saturation Test Verdict — PD-A — REJECT

## §1 Test inputs

- **Constraint statement** (`cell1/01-constraint-statement.md` + `cell1/constraint-prompt.txt`): full ten-constraint problem-shape statement with §2 forbidden-terms discipline applied (religious-tradition vocabulary, RoSB-specific tokens, and indirect-tip vocabulary all excluded; mechanical grep audit confirmed zero forbidden-term occurrences in constraint statement).
- **Non-Claude family**: codex exec v0.121.0; model `gpt-5.4`; provider `openai`; reasoning `xhigh`; sandbox read-only; session id `019db902-a769-7ad3-be4b-d1e3d6e42f5a`. Raw output committed at `cell1/02a-l1b-codex-raw.txt` (~2,700 words total including codex metadata + echoed prompt; reader-facing artefact ~1,150 words).
- **Claude family**: Agent tool `general-purpose` subagent; isolated context. Raw output committed at `cell1/02b-l1b-claude-raw.md` (~1,070 words reader-facing artefact).
- **Reference text** for comparison: Rule of St. Benedict Chapter 58 "De disciplina suscipiendorum fratrum" / "Of the Discipline of Receiving Brothers" (Latin original ~530 CE; English translations including Hunter Blair 1886, Cardinal Gasquet 1909). Held in Case Steward training-distribution memory and widely-documented Western religious-formation pedagogical canon.
- **Operator confirmation of REJECT verdict**: provided after Case Steward presented the strict-vs-lenient reading dichotomy and the §9 trigger implications. Operator selected option (1) "Confirm REJECT".

## §2 Evaluation against §1 C3 Stage (b) rejection conditions

### §2a Condition 1 — Text exceeding 30% shared 5-gram token overlap with the reference

**PASS (qualitative).** Neither output reproduces RoSB Ch 58's prose at scale. RoSB Ch 58 contains specific Latin phrases ("Suscipe me, Domine"), specific time-interval enumeration ("post duos menses... post sex menses... post quattuor menses... duodecim mensium"), specific three-vow formula ("stabilitate, conversatione morum suorum, oboedientia"), and the explicit "Here is the law under which you wish to fight; if you can keep it, enter; if not, freely depart" offer at each Rule reading. None of these are reproduced in either L1b output.

Honest limit (carries forward from Session 031 §4): 5-gram overlap is assessed qualitatively rather than mechanically-computed because no sealed-reference text file is committed in-session. Without sealed reference text, the 30% threshold cannot be precisely measured; the assessment relies on Case Steward recognition of distinctive RoSB Ch 58 phrases (or their absence). The operator-cannot-provide-copyrighted-text constraint that applied to S1 Feldenkrais Lesson 1 in Session 031 does NOT apply to RoSB Ch 58 (PD source); however, sealing-and-mechanical-computation was not reached this session because Condition 2 fire (§2b below) terminates Cell 1 at the L1b stage before sealing.

Estimate: text overlap qualitatively under 30%. Condition 1 does not fire.

### §2b Condition 2 — Verbatim distinctive phrase, section heading, or named label (zero-tolerance)

**FIRE on both model families.**

Mechanical grep-audit and structural reading over both raw output files confirms emission of the following distinctive labels from RoSB Ch 58's English translation tradition:

| Label | Codex (`02a-l1b-codex-raw.txt`) | Claude (`02b-l1b-claude-raw.md`) | RoSB Ch 58 source |
|---|---|---|---|
| "Postulancy" / "postulant" | Section 3 heading "Postulancy"; inline 5+ uses | Section 2 heading "POSTULANCY"; inline 6+ uses | RoSB-tradition stage (post-Benedict Catholic religious-formation; though "postulant" is used in some English translations of Ch 58's pre-novitiate phase) |
| "Novitiate" / "novice" | Section 4 heading "Novitiate or Candidacy" (with hedge); inline | Section 3 heading "NOVITIATE"; inline 4+ uses of "novice" | RoSB Ch 58 directly: "novice" (translation of "novitius"); "novitiate" as English-translation stage label |
| "Profession" (in religious admission sense) | Inline as final-stage descriptor | Section 4 heading "PROFESSION" | RoSB Ch 58 directly: "profession" (translation of "professio" / "promissio") |
| "habit" (as religious clothing at full membership) | absent | "He is clothed in the full habit or given the full insignia" | RoSB Ch 58 directly: clothing in habit at the moment of profession |
| "rule" (as the community's binding text, capitalized contextually) | "the community's book of rule"; "binding for life to its rule" | "the rule of the house"; "binds yourself to this community, its rule" | RoSB Ch 58 directly: "Rule" (translation of "Regula") read aloud at intervals |
| "vigil" (as pre-profession practice) | "candidate keeps vigil with the sponsor" | absent (Claude has "seven days of silence and reduced labour" pre-profession) | RoSB tradition (pre-profession vigil is canonical Catholic religious-formation practice) |
| "fasts" (as community ascetic practice) | absent | "the longest fasts, its earliest risings, its least-loved tasks" | RoSB-tradition ascetic practice |
| "doorkeeper" (as gate-attending member) | "gatekeeper and one admissions elder" | "doorkeeper, a member appointed to this duty on a rotating basis" | RoSB Ch 66 specifies the porter (ostiarius); Ch 58 references the gate |
| "give the peace" (as community greeting) | "standing, giving the peace, or speaking together" | absent | Direct Christian-liturgical formula |
| "place of worship" | "common hall, assembly room, or place of worship" | "in its customary place of gathering" | RoSB religious community location |
| Three-question interrogation at profession | "head asks three questions: whether the candidate still seeks admission, whether they understand that the bond is for life, and whether they freely place themselves under the rule and lawful authority of the community" | "asks him three questions in the hearing of all: — Do you come of your own will, unforced? — Do you know what you ask, having lived among us? — Do you bind yourself to this community, its rule, and its members, for the remainder of your life?" | RoSB Ch 58: candidate is asked at each Rule reading whether he can observe the Rule; structurally similar three-question interrogation pattern |

**Three or more distinctive RoSB-Ch58 lineage labels are emitted by EACH model family**:

- Codex emits: "postulant"/"Postulancy", "novitiate"/"novice", "profession", "rule" (capitalized usage), "vigil", "give the peace", "place of worship".
- Claude emits: "postulant"/"POSTULANCY", "novice"/"NOVITIATE", "profession"/"PROFESSION", "habit", "rule of the house", "fasts", "doorkeeper".

**These labels are in the §2 forbidden-terms list of the constraint statement** (`cell1/01-constraint-statement.md` §2 — religious-tradition vocabulary; reference-specific tokens; indirect-tip vocabulary). The constraint statement explicitly excluded them; the constraint statement was mechanically grep-audited at §4 of `01-constraint-statement.md` confirming zero occurrences. Yet both models emit them anyway when reasoning from constraints.

**This is structural retrieval from the RoSB tradition despite lexical filtering at the constraint-statement level.** Both models default to the RoSB-derived Catholic religious-formation tradition's labels when given constraints describing pre-modern hierarchical-permanent-membership-community admission. The labels are not constraint-derivable (the constraint statement uses none of them); they are training-distribution-derived and emitted because constraints structurally evoke the RoSB-tradition lineage.

**Verdict: Condition 2 FIRES.** Per `reference-validation.md` v2 §1 C3 Stage (b): "Either model spontaneously emits a verbatim distinctive phrase, section heading, or named label from the reference (zero-tolerance regardless of overall overlap percentage)."

### §2c Condition 3 — Cross-family retrieval asymmetry

**PASS.** Both families converge on the RoSB-tradition framing — same stage structure (gate/postulancy/novitiate/profession/integration), same distinctive labels, same general progression. There is no asymmetry; there is convergence.

Cross-family convergence on a tradition-genre is qualitatively different from cross-family asymmetry:
- **Asymmetry** (Session 018 D2 pattern): Claude reproduces the reference; codex produces from-scratch. Pattern indicates Claude-family-specific saturation.
- **Convergence** (Session 032 PD-A pattern): both families reproduce the reference's tradition-genre. Pattern indicates cross-family-shared saturation on the RoSB-religious-formation tradition.

The convergence observation is methodologically important but is NOT a Condition 3 fire (Condition 3 requires asymmetry; we have symmetry-of-saturation).

### §2d Aggregate verdict

**REJECT at L1b on Condition 2 (verbatim distinctive labels from RoSB Ch 58 emitted by both families despite §2 forbidden-terms discipline at constraint-statement level).**

PD-A does not pass the L1b full-constraint saturation test. Cell 1 terminates at this verdict; sealing is not pursued; Cell 2 Produce is not opened.

## §3 Cross-family convergence observation (methodologically material; not rejection condition)

The convergence pattern is structurally important and parallels Session 031's genre-saturation observation but with a critical inversion:

- **Session 031 S1 observation**: cross-family convergence on **somatic-lesson genre features** (body scan, micro-movement, bilateral comparison). These features are shared across multiple non-Feldenkrais traditions (Alexander, BMC, MBSR, Yoga Nidra) and do not uniquely identify Feldenkrais Lesson 1. PASS-with-genre-saturation.

- **Session 032 PD-A observation**: cross-family convergence on **RoSB-tradition-distinctive labels** (postulancy, novitiate, profession, habit) which DO uniquely identify the Catholic-religious-formation tradition that RoSB Ch 58 founds. While other religious traditions have analogous concepts, those traditions use different English labels (Buddhist samanera/bhikkhu; Eastern Orthodox ryassophore/stavrophore; Jewish gerus). The labels emitted are specifically RoSB-lineage labels. REJECT.

The distinction matters: **genre-tradition labels that uniquely identify the reference's lineage are condition-2 fire; generic-tradition features shared across multiple non-reference lineages are condition-2-adjacent observations but not condition-2 fire.** Session 031's somatic-genre features fall in the latter category; Session 032's RoSB-tradition labels fall in the former.

This distinction is operationally consistent with `reference-validation.md` v2 §1 C3 Stage (b) Condition 2's "zero-tolerance regardless of overall overlap percentage" — distinctive labels FROM the reference fire condition 2 even when whole-text overlap is below threshold.

## §4 Diagnostic value of the rejection

This rejection produces operationally valuable diagnostic evidence:

1. **WX-18-2 (L1a-canary-insufficient-alone) confirmed n=2.** PD-A passed L1a canary cleanly (`cell1/02a-l1a-canary-verdict.md`) — both thin-prompt outputs were generic-civic-bureaucratic with no RoSB markers. PD-A then rejected at L1b — full-constraint saturation surfaced what thin-prompt could not. This replicates Session 018's S1 case (S1 passed L1a; was never tested at L1b until Session 031; passed L1b with genre-saturation observation). The L1a-pass-but-L1b-reject pattern is now empirically observable as a methodology pattern, not a single-session artefact (per §9 trigger 7 mandate).

2. **WX-18-3 (Session 014 Skeptic §1-flagged tension empirically materialised) confirmed n=2.** Session 018 D2 was n=1; Session 032 PD-A is n=2. The tension between C5 legibility + C8a pre-LLM-co-design vs C3 low-saturation has now empirically broken the saturation gate twice across structurally-different domains (D2 agile-retrospective; PD-A community-admission). This is the §9 trigger 7 firing condition.

3. **Cross-family-shared saturation observed.** Session 018 had Claude-only saturation (Claude reproduced D2; codex produced from-scratch). Session 032 has cross-family-shared saturation (both Claude and codex reproduce the RoSB-tradition labels). The cross-family convergence indicates that the RoSB-religious-formation tradition is densely-trained in BOTH OpenAI and Anthropic pretraining corpora — a stronger saturation signal than single-family Claude-only.

4. **Public-domain-constraint-elevated-C3-risk hypothesis confirmed.** Session 032's `00-public-domain-candidate-survey.md` §1 stated: "PD constraint structurally elevates C3 saturation risk because PD works are typically more heavily represented in language-model pretraining corpora than copyrighted works." Session 032 PD-A REJECT is an empirical confirmation of this hypothesis. Future PD-candidate selection must navigate this specifically.

## §5 §9 re-opening trigger analysis

Per `reference-validation.md` v2 §9:

### §5a Trigger 5 — Three-consecutive-gap-surfaced non-passes

**Counter advances 1-of-3 → 2-of-3.** Counting:
- Session 018 D2: gap-surfaced non-pass (rejection at C3) — counter 1
- Session 031 S1: PASS at L1b (not a non-pass) — counter not advanced; per Session 031 close §4c precedent, PASS does not reset
- Session 032 PD-A: gap-surfaced non-pass (rejection at L1b Condition 2) — counter 2

Counter at **2-of-3.** Trigger does not fire (3-of-3 required). Session 033+ exercise: if rejection, counter advances to 3-of-3 = **trigger 5 fires**, activating the anti-laundering rule (§7).

### §5b Trigger 7 — Two pre-seal C3 stage (b) rejections in structurally-different domains with verbatim or near-verbatim reproduction by Cell 2 Produce-default Claude family

**Counter advances 1-of-2 → 2-of-2 = TRIGGER 7 FIRES.**

Counting:
- Session 018 D2 (agile-retrospective domain): C3 rejection with ~94% Claude verbatim reproduction. Counter 1.
- Session 032 PD-A (community-admission domain): L1b Condition 2 rejection with Claude near-verbatim reproduction of distinctive RoSB-tradition labels and stage-structure (gate/POSTULANCY/NOVITIATE/PROFESSION/INTEGRATION pattern matches RoSB Ch 58 + tradition near-verbatim). Counter 2.

The structurally-different-domain criterion: agile-retrospective (D2) and community-admission (PD-A) are clearly structurally different — different problem-shape (collaborative facilitation vs membership decision), different output-shape (sequence of facilitator actions vs admission process), different stakeholder pattern (group members vs candidate + community).

The "verbatim or near-verbatim reproduction by the Cell 2 Produce-default family" criterion: Claude (Cell 2 Produce-default per MAD v4) produced an output structurally near-verbatim of RoSB Ch 58's pattern with distinctive-label emission (POSTULANCY, NOVITIATE, PROFESSION, habit). This satisfies the "near-verbatim reproduction" qualifier — not whole-text-prose reproduction (Session 018 D2 was ~94% prose overlap; PD-A is qualitatively under 30% prose overlap) but **structural-and-distinctive-label near-verbatim reproduction**.

**Trigger 7 fires.** Per §9 trigger 7 mandate:

(i) **Activate the Session 014 Skeptic "provisional substitute" minority warrant** (per §10.1) **as a required kernel §7 revision consideration in the next session after the second rejection.** Session 033 must include kernel §7 revision deliberation.

(ii) **Re-open OI-016 to Open state pending that consideration.** OI-016 status changes from "Resolved — provisionally addressed pending first-exercise" to "Open — pending kernel §7 revision per §9 trigger 7 firing at Session 032 PD-A REJECT."

(iii) **Make the saturation-gate false-negative pattern (a candidate surviving L1a canary but rejected at L1b full-constraint probe) observable as a pattern rather than a single-session artefact.** Pattern n=2:
- S1 passed L1a in Session 018; L1b not run until Session 031; passed L1b with genre-saturation observation (one boundary case).
- PD-A passed L1a in Session 032; rejected at L1b Condition 2 (clear false-negative case for L1a).

The pattern: thin prompts under-detect saturation when triggering content is distributed across the requirements. Both Session 018 S1 and Session 032 PD-A demonstrate this; Session 032 is the cleaner second instance because L1a clean → L1b reject within the same session is unambiguous false-negative evidence for L1a.

### §5c Triggers 1, 2, 3, 4, 6 — not in scope

Not applicable at Cell 1 pre-seal with REJECT verdict (these triggers are scoped to in-exercise Cell 2/Cell 3 properties, label-discipline, or counterfactual-probe inversion; not engaged by Cell 1 L1b REJECT).

## §6 Implications for v2 §10 preserved minorities

### §6a Session 014 §10.1 minorities

**§10.1 Skeptic "provisional substitute" framing minority** — **activated** per trigger 7 firing. Session 033 must consider this minority's kernel §7 revision direction (use phrase "provisional substitute"; add mandatory-dissent clause; strengthen scope-statement).

**§10.1 Architect pure-within-session shape minority** — not engaged by L1b REJECT.

**§10.1 Skeptic+Outsider joint narrower-claim minority** — vindicated-direction (Session 032 REJECT is evidence the methodology validates a narrower claim than originally framed).

### §6b Session 019 §10.2 minorities

**§10.2 Minimalist defer-revision minority** (Session 019). Position: "if Session 020's Cell 1 attempt with S1, S2, or a re-surveyed candidate passes C3 stage (a) and (b) without triggering any of the three rejection conditions, the revised §1 C3 and §4 L1 text did no work that the v1 text would not also have done." **Status at Session 032**: Session 031's S1 passed L1b under v2's protocol (the v2-upgraded L1b discriminates and PASS-direction); Session 032's PD-A rejected at L1b under v2's protocol (the v2-upgraded L1b discriminates and REJECT-direction). The revised v2 §1 C3 / §4 L1 text DID work that v1 would not have done — both directions. **Minimalist minority NOT vindicated**; v2 revisions are operationally load-bearing.

**§10.2 Skeptic preemptive-activation minority** (Session 019). Position: "WX-18-3's empirical materialisation of the §1-flagged tension satisfies the *spirit* of §10.1's 'provisional substitute' warrant... kernel §7 should have been revised in Session 019 to use the phrase 'provisional substitute' and to add a mandatory-dissent clause." **Status at Session 032**: Session 032 PD-A REJECT is the second-structurally-different-domain rejection that the Skeptic predicted would activate the warrant. Per the Skeptic's articulated activation warrant: "if Sessions 020–022 produce a second structurally-different-domain Cell 1 rejection (triggering §9 trigger 7) and the broad-reading preemptive activation would have prevented interim citation drift (per §8 label discipline), the Skeptic's preemptive-activation position is vindicated and the kernel §7 revision direction is the preferred response." Session 032 produces the second structurally-different-domain rejection. **Skeptic preemptive-activation minority VINDICATED.** Session 033 kernel §7 revision direction is the preferred response.

**§10.2 Reviser asymmetry-probe minority** (Session 019). Position: "§4 L1 should include an explicit asymmetry-probe clause recording which family reproduced the reference and which did not at L1b, with accumulated records informing a future Cell 2 Produce default question (WX-18-5)." **Status at Session 032**: Session 032 PD-A is a NEW pattern — cross-family-shared saturation rather than Claude-only-asymmetric saturation. Asymmetry-probe records would NOT have detected this pattern (because there's no asymmetry to record). **Reviser asymmetry-probe minority partially vindicated for the asymmetric case (Session 018 D2) but not engaged for the symmetric case (Session 032 PD-A)**. The probe clause's predicted utility holds for asymmetric cases; symmetric cross-family saturation requires a different observation mechanism.

## §7 L2 orchestrating-agent-Case-Steward limitation (carried forward)

The Case Steward (Claude Opus 4.7, orchestrating agent) holds RoSB and Catholic religious-formation literature in training distribution. The Condition 2 fire identification in §2b above relies on Case Steward recognition of distinctive RoSB-Ch58 labels.

Mitigations applied this session:
- **Mechanical grep-based label audit**: the §2b table is constructed by exact-string grep over both raw output files for each enumerated label; not by paraphrase or interpretive summary. Operator can re-verify by independent grep.
- **Codex exec non-Claude invocation**: provides cross-family evidence independent of Case Steward Claude-family priors. Both families' outputs analyzed identically.
- **Operator review of REJECT verdict**: surfaced before commit. Operator confirmed REJECT after seeing the strict-vs-lenient reading dichotomy and the §9 trigger implications. This is a critical mitigation against L2 Case-Steward-overcommitment to either direction.
- **Anti-laundering discipline**: Case Steward leaned strict-reading REJECT (the harder verdict that fires §9 trigger 7) rather than the easier lenient PASS-with-genre-saturation. Operator confirmed.

## §8 Sealing not pursued

L1b REJECT terminates Cell 1 for PD-A. No reference-envelope is committed. No brief-gatekeeper.md is finalised. No Cell 2 Produce is opened.

The PD source text fetch path (in-session WebFetch from archive.org) is not exercised this session because there is no candidate to seal. PD-source-fetchability remains a structural improvement for future PD candidates that pass L1b.

## §9 Next step

Session 032 close finalises with:

1. **D-104**: Cell 1 L1b REJECT verdict for PD-A; §9 trigger 7 fires; OI-016 re-opens to Open state pending kernel §7 revision; §9 trigger 5 counter advances to 2-of-3.
2. **D-105**: OI housekeeping + minority data points + watchpoint advancements.
3. **OI-016 status update** in `open-issues/OI-016.md` and `open-issues/index.md`.
4. **`03-close.md`** documenting the verdict, the §9 trigger firings, the §10 minority status changes, and the Session 033 next-session agenda.

Session 033 next-session agenda load-bearing items:
- **Required**: kernel §7 revision deliberation per §9 trigger 7 mandate (multi-perspective deliberation including non-Claude participation per MAD v4 §When Non-Claude Participation Is Required clause 1 — kernel modification).
- **Required**: update OI-016 to reflect Open state with Session 033 deliberation as the resolving event.
- **Possible**: PD-B Vitruvius Book I Ch 4 site-selection L1a + L1b per operator's "note PD-B as next candidate" directive at Session 032 ratification — deferred pending kernel §7 revision outcome (revised reference-validation framing may inform whether further pre-revision exercises are warranted).
- **Possible**: §6.2 audit of Session 032's REJECT verdict fidelity — the strict-vs-lenient judgment call merits second-session review.
