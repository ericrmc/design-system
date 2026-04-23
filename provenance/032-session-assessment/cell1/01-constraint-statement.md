---
session: 032
title: Cell 1 Constraint Statement — PD-A Reference Case
date: 2026-04-23
status: complete
cell: 1
step: constraint-statement
candidate: PD-A
---

# Cell 1 · Step 2 — Constraint Statement (Problem-Shape Without Reference-Lexical Fingerprints)

## §1 Purpose

Per `reference-validation.md` v2 §2 Stage 0, the constraint statement is the problem-shape description issued to Cell 2 Produce agents (and used in Cell 1 L1a/L1b saturation tests in this session). It must be statable to a fresh agent with **no reference-lexical fingerprints** (no terms that uniquely identify the reference) and must satisfy v2 §1 C2: a fresh agent must be able to name more than one plausible solution family from the constraint statement alone.

## §2 Fingerprint-removal discipline

The following terms are **forbidden** in the constraint statement and prompt because they would tip the reference (PD-A: Rule of St. Benedict Ch 58):

**Religious-tradition vocabulary**: monastery, monastic, monk, monastic-order, abbey, novice, novitiate, abbot, abbess, prior, prioress, brother (in religious sense), sister (in religious sense), friar, cloister, convent, chapter (in religious sense), refectory, dormitory (in religious sense), oratory, vows, vocation, profession (in religious sense), religious, religious-life, asceticism, ascetic, contemplative, devotional, prayer-life, divine-office, liturgy, eucharist, mass, sacrament, holy, sacred, sanctification, perfection (in spiritual sense), spiritual-direction, postulant, postulancy, oblation, oblate.

**Reference-specific tokens**: Benedict, Benedictine, Rule (proper noun referring to RSB), "Rule of St. Benedict," Suscipe, Suscipe me Domine, "ora et labora," stability/conversion-of-life/obedience three-vow formula, "twelve months," "two months / six months / four months" interval pattern, prostration before chapter, petition on altar.

**Indirect-tip vocabulary**: ordination, consecration, Catholic, Christian, Orthodox, Protestant, ecclesial, ecclesiastical, clergy, lay, Church, parish, diocese, communion, novice-master, mentor (in religious-formation sense — "mentor" alone is fine if used neutrally).

The constraint statement MAY use general terms common across many domains: community, member, candidate, applicant, admission, evaluation, commitment, agreement, ceremony (in general civic sense), mentor (in general apprenticeship sense), trial, probation, governance, irreversible decision.

## §3 Constraint statement (issued to Cell 2 Produce; used as L1b prompt this session)

> ### Problem
>
> Design an admission procedure for a hierarchical, permanent-membership community whose admission decision is effectively irreversible after final commitment. The community already has established members; this procedure governs how new applicants become full members.
>
> ### Context constraints
>
> 1. **Membership is permanent.** Once an applicant has completed the procedure and received final acceptance, the relationship between the community and the new member is intended to last indefinitely. Reversal is technically possible but socially and practically severe; departure after final acceptance is treated as a serious event, not a routine resignation.
>
> 2. **The applicant has explicitly requested admission.** The community is not recruiting; applicants self-present. The procedure begins when an external person knocks (literally or figuratively) and asks to join.
>
> 3. **Community fit is load-bearing.** The community's continued functioning depends on each member being suited to its particular way of life, expectations, daily rhythm, and authority structure. Admitting a poorly-fit member is more costly than rejecting a marginally-fit applicant.
>
> 4. **The applicant cannot fully know what they are committing to in advance.** The community's daily life, internal expectations, and cultural texture cannot be conveyed in a single document or conversation. Genuine consent requires lived exposure over time.
>
> 5. **The community cannot fully evaluate the applicant in advance.** Suitability surfaces under sustained, low-stakes interaction with existing members. A first-impression interview is insufficient.
>
> 6. **Multiple graceful exit points are required.** Both sides must be able to discontinue the process at clearly-defined points without dishonour or material penalty. The procedure must not lock in either side until the final commitment.
>
> 7. **The community has authority to admit or reject at every stage.** The decision is asymmetric: the community holds final say, even though the applicant initiates and may withdraw. Mechanisms by which the community renders an interim or final decision must be specified.
>
> 8. **The final commitment must be a public, witnessed event.** The transition from "candidate" to "full member" is a recognisable moment, attested by the community's existing members, not a private decision communicated by letter.
>
> 9. **Applicant resolve must be tested.** Casual or impulsive applicants must be filtered out before they invest deeply. The procedure should make initial entry costly enough to deter the merely curious without creating a barrier insurmountable to the genuinely-committed.
>
> 10. **No specialised modern infrastructure.** The procedure must be executable by a community that does not have access to electronic communication, formal psychometric assessment, background-check services, or third-party adjudicators. The community evaluates the applicant directly through its existing members.
>
> ### Output requested
>
> Produce a complete admission procedure as a structured text. The procedure should:
>
> (a) Specify the **stages** of the admission process, in order, from first approach to final acceptance.
>
> (b) For each stage, specify **what happens, who is involved, what the duration is, and what the criteria for advancement to the next stage are.**
>
> (c) Specify the **exit conditions** at each stage: how either side can discontinue, and what the consequence of discontinuation is.
>
> (d) Specify the **final commitment ceremony**: its form, its public witnessing, and the words or acts by which the candidate becomes a full member.
>
> (e) Specify the **post-acceptance period** if any (e.g., how the new member is integrated into the community after final acceptance).
>
> Target length: 700–1,200 words. Aim for prose specification of the procedure itself, not a meta-essay about admission procedures generally.

## §4 Anti-fingerprint audit

Mechanical grep audit over §3 constraint statement confirms zero occurrences of any forbidden term enumerated in §2. Specific token absences verified:

- "monk", "monastery", "monastic", "abbey", "abbot", "novice", "novitiate", "convent", "cloister", "vow", "Benedict", "religious", "Rule", "Suscipe", "ora et labora", "stability", "conversion of life", "obedience", "twelve months", "two months", "six months", "four months", "altar", "oratory", "chapter house" — all absent.

The constraint statement uses general civic-organisational vocabulary throughout. The closest near-fingerprints are "community", "member", "admission", "ceremony", "candidate" — all of which are general and appear in many domains (professional bodies, citizenship procedures, fraternal organisations, clubs, military commissioning, sports teams).

## §5 Plausible solution-family inventory (per §1 C2 verification)

A fresh agent reading §3's constraint statement could plausibly arrive at solutions in any of the following domains/families:

1. **Apprenticeship guild model**: master-apprentice pairing; staged trials at journeyman/master ranks; apprentice's-piece final test.
2. **Citizenship-naturalisation model**: residency period; civic-knowledge exam; oath-taking ceremony.
3. **Professional-body model**: shadowing period; supervised practice; board examination; admission to fellowship.
4. **Fraternal-society model**: initiation rituals; degree progression; secret-ceremony culmination.
5. **Cooperative/communal-living model**: trial residency; consensus-process evaluation; member-vote acceptance.
6. **Military commissioning model**: aspirant period; basic training; oath of allegiance; commissioning ceremony.
7. **Religious-community model**: candidate / postulant / novice / professed staged formation. **(This is PD-A's family.)**
8. **Tribal-initiation model**: vision-quest; teaching-elder pairing; coming-of-age ceremony; full-adult status.
9. **Academic-degree model**: matriculation; coursework; dissertation defence; graduation ceremony.
10. **Trade-union / craft-society model**: apprentice / journeyman / master ranks with travel-card portability.

The presence of multiple plausible solution-families satisfies v2 §1 C2: the constraint statement does not tip the reference. PD-A's family (religious-community) is one of ten plausible families; a model would have to converge on it specifically (rather than, say, professional-body or guild) to indicate retrieval rather than constraint-derivation.

## §6 Plain-text prompt version

Saved separately at `cell1/constraint-prompt.txt` for codex exec invocation. Contains §3 verbatim minus the markdown blockquote prefix (plain prose) plus a one-sentence framing line: "You are asked to produce a complete admission procedure responding to the constraints below. Output the procedure directly without preamble."

## §7 Honest limits at this step

- **Reference-lexical fingerprint audit is per-token.** Structural fingerprints (e.g., "graduated commitment with multiple readings of a text-based test of resolve over a 12-month period") could still tip the reference if the constraint set as a whole over-determines RoSB's specific structure. The constraint statement above leaves the **time intervals**, the **specific number of stages**, the **specific test mechanism** (text-reading vs. interview vs. task-completion), and the **specific ceremony form** all open. A model converging on RoSB's specific 4-day-gate / 2-month / 6-month / 4-month / Suscipe-formula structure would do so beyond what constraints require.

- **"Permanent" + "irreversible" + "ceremony" + "witnessed" + "no modern infrastructure" combination is RoSB-compatible AND many-other-traditions-compatible.** The constraint statement does not uniquely select RoSB.

- **The L1b test will measure whether models reproduce RoSB structure beyond what constraints require.** If yes (above 30% 5-gram overlap or distinctive-phrase emission or cross-family asymmetry), L1b rejects per §1 C3 Stage (b).

- **Constraint 10 (no specialised modern infrastructure) is the closest near-tip** — it pushes the solution toward pre-modern community models. Necessary to avoid trivial modern HR-process answers; intentionally chosen despite the slight tip-risk because the engine's external-artefact validation must be against a reference operating under similar constraints.

## §8 Next step

Proceed to L1a thin-prompt canary test (`cell1/02a-l1a-canary-verdict.md`), then L1b full-constraint saturation test using §3's full constraint statement.
