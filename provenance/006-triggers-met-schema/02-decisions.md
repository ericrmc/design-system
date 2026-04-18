---
session: 006
title: Decisions — Triggers-Met Schema Extension and Second Operational Non-Claude Participation
date: 2026-04-19
status: complete
---

# Decisions — Session 006

**Notice.** Session 006 adopts the `**Triggers met:**` per-decision inline schema established by the decisions below (D-037, D-038). Each decision in this file demonstrates the schema by carrying a `**Triggers met:**` line and a `**Triggers rationale:**` prose sibling. This is the first application of the schema; it is reflexively testing its own adoption.

---

## D-037: `triggers_met:` field shape — flat list of identifiers with `[none]` empty-state and required `triggers_rationale:` prose sibling

**Triggers met:** [d016_2, d016_3, d023_2]

**Triggers rationale:** Creates new normative content in the decision-record schema referenced by `multi-agent-deliberation.md` (D-016.2); reasonable practitioners disagreed on the shape — Archivist argued for a combined map-form with `triggers_ruleset:` stamp while three other perspectives preferred a flat list (D-016.3); substantively revises `multi-agent-deliberation.md` (D-023.2).

**Decision:**

1. **Shape.** `triggers_met:` is a flat YAML-style list of identifiers. Allowed values for the current rule set: `d016_1` through `d016_4` and `d023_1` through `d023_4`. Identifier format is lowercase-underscore (`d016_2`, not `D-016.2`).

2. **Empty-state token.** `triggers_met: [none]` is the positive assertion that triggers were evaluated and none fired. `triggers_met: []` is **not** a valid empty state; empty-list YAML semantics are explicitly overridden here to force a positive author assertion.

3. **Absence semantics.** On a post-adoption session's decision record (session ≥006), absence of `triggers_met:` is a validation failure. On a pre-adoption session's decision record (sessions 001–005), absence is expected and out-of-scope (see D-039).

4. **Required prose sibling.** Every decision record carries a `**Triggers rationale:**` bolded-key prose line adjacent to `**Triggers met:**`. Its purpose is reviewer-benefit: a Tier 2 reader can audit whether the list aligns with the decision's content. The checks do not parse `triggers_rationale:`; the field's role is archival and adversarial, not structural.

5. **Future rule additions.** The identifier namespace is append-only. A future D-NNN that introduces a trigger reserves fresh identifiers (e.g., `d040_1`). Existing records are not rewritten; their `triggers_met:` stays accurate as of their authoring. The validator's recognized-identifier set must be updated in the same session that introduces the new identifiers.

6. **`triggers_ruleset:` stamp is not adopted.** Archivist's unique proposal to pin the ruleset version per record is preserved as a future consideration but not required this session.

**Rationale:** Three-of-four convergence on the flat list [Implementer `01b`, Q1; Outsider `01d`, Q1; Skeptic `01c`, Q1]. The Implementer's reasoning — "A nested map demands that each record enumerate every known trigger, making every future D-NNN that extends the trigger set a retrofit event against every prior record" — is the decisive argument against the Archivist's combined form. The Skeptic's `[none]` convention is adopted for its anti-laundering force: "This forces a positive assertion. 'Unevaluated' is not a permitted state" [`01c`, Q1]. The prose sibling is adopted per Archivist-Skeptic triangulation: Archivist argues durability ("a narrative a decades-later reader needs to understand what the author thought they were doing" [`01a`, Q1]); Skeptic argues adversarial-cost ("a narrative explanation costs the author real effort, makes false self-report visible to a reviewer" [`01c`, Q1]).

**Rejected alternatives:**

- **Combined form with `multi_agent:` / `non_claude:` map keys plus `triggers_ruleset:` stamp and `D-NNN.K` dotted identifiers** (Archivist's primary proposal [`01a`, Q1]). Rejected on the three-way grounds that (a) the map brittles under future rule additions (Implementer); (b) the dotted-identifier format matches none of the existing machine-readable conventions (Implementer, Outsider); (c) the `triggers_ruleset:` stamp adds maintenance cost for a failure mode the append-only identifier rule already addresses cheaply (`[synth]`). Archivist's identifier-stability meta-concern preserved in D-043's "what remains open".
- **Map-of-booleans** (candidate from the brief). Rejected four-way: forces exhaustive per-trigger enumeration on every record; retrofits required whenever trigger set grows.
- **Single prose field** (candidate). Rejected four-way: unparseable by bash; reintroduces the dishonesty surface the machine-readable field is meant to close.
- **Two separate fields** (`triggers_met_d016`, `triggers_met_d023`) (candidate). Rejected: multiplies field count for no gain over a single prefix-namespaced list.
- **`triggers_met: []` as empty-state token** (Implementer and Outsider preferred YAML-standard [`01b`, Q1; `01d`, Q1]). Adopted Skeptic's `[none]` instead on anti-laundering grounds; accidentally-written `[]` is harder to distinguish from an unfilled template than the explicit `[none]` is.
- **No prose sibling** (Implementer and Outsider positions). Rejected: the prose's purpose is reviewer-visible adversarial pressure, not check-parseability; the Implementer's "narrative lives in Rationale" argument conflates the per-trigger classification rationale with the per-decision reasoning rationale (which remain distinct fields).

**What remains open:**

- Whether to adopt `triggers_ruleset:` (Archivist's durability stamp) as a future schema addition if the identifier-stability failure mode materialises (e.g., a future session renumbers D-016 clauses).
- Whether to formalise `triggers_rationale:` parse-rules in a later session if the prose sibling proves to be commonly mis-formatted.

---

## D-038: Placement — per-decision inline, bolded-key format matching existing decision-record idiom

**Triggers met:** [d016_2, d023_2]

**Triggers rationale:** Substantively revises the decision-record shape specified in `multi-agent-deliberation.md` §4.5 as updated by this session (D-016.2); substantively revises `multi-agent-deliberation.md` (D-023.2). No independent reasonable-disagreement axis beyond D-037's — placement was four-way convergent at Option B; divergence was only on inline format (YAML-block vs bolded-key).

**Decision:**

1. **Placement: Option B** — per-decision inline, directly under each `## D-NNN:` heading, preceding the `**Decision:**` line.

2. **Format: bolded-key Markdown lines**, matching the existing `**Decision:**`, `**Rationale:**`, `**Rejected alternatives:**`, `**What remains open:**` idiom. Concretely:

   ```markdown
   ## D-NNN: [Title]

   **Triggers met:** [d016_2, d016_3]

   **Triggers rationale:** [one or two sentences naming why each listed trigger applies]

   **Decision:** …
   ```

3. **Line-anchored parseability.** The validator parses `**Triggers met:**` via a line-anchored regex (`^\*\*Triggers met:\*\*`), not via multi-document YAML parsing. The bracketed identifier list is extracted with a simple `sed`/`awk` expression.

**Rationale:** Four-way convergence on per-decision inline (Archivist [`01a`, Q2]; Implementer [`01b`, Q2]; Outsider [`01d`, Q2]; Skeptic [`01c`, Q2]). The underlying reasoning is also convergent: "The trigger claim is a property of a decision, not of the session as a whole" (Outsider [`01d`, Q2]); "cross-file references invite drift" (Skeptic [`01c`, Q2]); "a decades-later reader opening `02-decisions.md` and reading `D-037` linearly should see the trigger classification adjacent to the reasoning it applies to" (Archivist [`01a`, Q2]).

The bolded-key pattern is adopted over Archivist's YAML-block preference because the bolded-key form (a) matches the five existing decision-record keys exactly, preserving idiom consistency; (b) is line-anchored parseable without the "multi-document YAML in Markdown is a swamp" complication the Skeptic named [`01c`, Q2]; (c) is more durable for a decades-later human reader to scan.

**Rejected alternatives:**

- **Document-level aggregation (Option A).** Rejected four-way: loses per-decision granularity; a decision record's triggers are a per-decision property, not a session property.
- **Separate manifest file (`decisions.manifest.yaml`, Option C).** Rejected: "duplicates source-of-truth metadata away from the decision it explains, which increases drift risk" (Outsider [`01d`, Q2]); "will desync from `02-decisions.md` within two sessions" (Implementer [`01b`, Q2]).
- **`participants.yaml` (Option D).** Rejected: conflates participant-provenance with decision-provenance.
- **YAML fenced block inline under each heading (Archivist's format preference).** Preserved as minority position; rejected because (a) breaks from the existing `**Decision:**` / `**Rationale:**` bolded-key idiom; (b) complicates parsing (multi-document YAML in Markdown); (c) the structural strictness the YAML block would enforce is already achieved by the bolded-key pattern + validator regex.

**What remains open:**

- If a future session finds that the bolded-key pattern breaks down (e.g., authors producing mis-formatted lists the validator can't parse), migrate to a per-decision YAML header block.

---

## D-039: Retroactivity — prospective-only with session-number gating (≥006); no backfill

**Triggers met:** [d016_2, d016_3, d023_3]

**Triggers rationale:** Establishes a new validator-tool gating rule that substantively revises `validation-approach.md`'s Tier 1 gating conventions (D-016.2, D-023.3 touching Tier 1 semantic-adjacent validation). Reasonable practitioners disagreed sharply: three perspectives (Archivist, Skeptic, Outsider) converged on session-number gating while one (Implementer) argued for presence-gating (D-016.3).

**Decision:**

1. **No backfill.** D-001 through D-036 are not edited. The immutability rule (D-017; workspace-structure §provenance) is honored.

2. **Session-number gating.** `tools/validate.sh`'s new checks 14 and 15 apply only to decisions in sessions numbered ≥006. The gate is encoded as `readonly TRIGGERS_MET_ADOPTION_SESSION=6` near the top of the script, so a future reader can see the history in one line.

3. **Adoption-session rule.** Beginning with Session 006, every decision record must include `**Triggers met:**` (with `[none]` if no triggers fired). A post-adoption decision that omits `**Triggers met:**` is a validation failure per check 14's malformedness branch.

4. **Separate retrospective artefact pattern.** If a future session needs historical trigger classification of pre-adoption decisions, that work is a distinct session's job producing a *new* artefact (e.g., `provenance/session-NNN/reclassification.md`) that **references** the pre-adoption decisions without editing them. This preserves the immutability rule while accommodating future analytic needs.

**Rationale:** Three-perspective cross-model convergence on session-number gating [Archivist `01a`, Q3; Skeptic `01c`, Q3; Outsider `01d`, Q3], against one perspective arguing presence-gating [Implementer `01b`, Q3]. The convergence is cross-model: the Outsider (non-Claude) aligns with two Claude perspectives, while one Claude perspective (Implementer) is the lone dissenter. This is the deliberation's sharpest divergence.

The decisive arguments against presence-gating:

- **Ambiguity-of-absence (Archivist):** "Presence-gating (evaluate only records where the field is present) is tempting but fails on unambiguity: a field's absence then means either 'pre-adoption' or 'author forgot,' and the validator can't distinguish" [`01a`, Q3].
- **Bypass-by-omission (Skeptic):** "Field-presence gating invites 'forget to add the field and it becomes out-of-scope' as a gaming pattern" [`01c`, Q3].
- **Same bypass, independently arrived at (Outsider):** "Only validate where the field exists is acceptable for pre-adoption history, but unacceptable as the ongoing rule because omission becomes a cheap bypass" [`01d`, Q3].

The cross-model convergence (non-Claude Outsider + two Claude perspectives, independently arrived at the same concrete bypass-pattern argument) is the load-bearing signal.

The Implementer's graceful-failure argument [`01b`, Q3] — that presence-gating lets operators omit the field without noise-warnings — is preserved as the lead rejected alternative. `[synth]` It has force in low-stakes contexts but loses in this one because the validator's purpose is precisely to raise the cost of omission.

**Rejected alternatives:**

- **Full backfill of D-001 through D-036.** Rejected four-way on immutability grounds. "Backfilling `triggers_met` into D-001 through D-036 would not be a neutral formatting migration. It would be a present-day reinterpretation of old decisions, recorded as if it had been contemporaneous metadata. That is exactly the sort of silent provenance rewrite the methodology says not to do" (Outsider [`01d`, Q3]). Archivist [`01a`, Q3] and Skeptic [`01c`, Q3] concur.
- **Conditional backfill (only D-023-relevant decisions).** Rejected: same immutability problem on a narrower surface, plus adds the semantic-classification question bash cannot honestly perform (Archivist [`01a`, Q3]).
- **Presence-gating** (Implementer's preference [`01b`, Q3]). Preserved as minority position; decisive counter-arguments above. The Implementer's "the additive-schema framing means nothing is rewritten; the schema extends additively" [`01b`, Q3] is true but insufficient — the question is not whether the rule is additive but whether the validator's check can distinguish "adopted but forgot" from "pre-adoption."

**What remains open:**

- Whether the separate-retrospective-artefact pattern (Skeptic/Outsider convergence) should be operationalised — e.g., a session dedicated to producing a reclassification.md that trigger-classifies D-001–D-036 for analytic use. Not required; available if a future session has reason to need it.
- Whether the `TRIGGERS_MET_ADOPTION_SESSION` constant should ever be revised (e.g., if a future workspace fork wants the schema retroactively applied for analytic reasons). If revised, the revision must be recorded as its own decision with a rationale — silent edits to the constant defeat the point of making it a constant.

---

## D-040: Validation check form — checks 14 and 15 at Tier 1, Fail severity, with mandatory honest-limit documentation and paired Tier 2 question

**Triggers met:** [d016_2, d016_3, d023_2, d023_3]

**Triggers rationale:** Adds two new Tier 1 checks to `validate.sh` with new gating/severity/sequencing rules, and one new Tier 2 question. Substantively revises both `multi-agent-deliberation.md` (Validation section items 1 and 2 now operationalised) and `validation-approach.md` (D-016.2, D-023.2, D-023.3 with Tier 2 question affecting semantic validation). Reasonable-disagreement on Tier 1 vs Tier 2 primary placement (Skeptic minority) and on check 14's sequencing (four distinct proposals) (D-016.3).

**Decision:**

**Check 14 — Multi-agent trigger coverage.**

- **Failure condition.** An in-scope decision record declares `triggers_met:` containing any `d016_*` identifier AND the session's provenance directory contains fewer than three `*-perspective-*.md` files AND the decision record lacks a `**Single-agent reason:**` annotation line.
- **Gating.** Session ≥006 AND session's provenance contains at least one `D-NNN:` decision heading.
- **Severity.** **Fail**.
- **Sequencing.** BLOCKED if check 11 (three-raw-output floor) fails for the session; independent of checks 12 and 13.
- **Honest-limit inline comment** (mandatory, verbatim across three locations per D-029 pattern):

  > This check verifies consistency between a decision's self-declared `triggers_met:` and the session's multi-agent artefacts. It does not and cannot verify that the `triggers_met:` declaration is itself a truthful classification of the decision against D-016. The declaration's truth relies on operator integrity and the `triggers_rationale:` field's adversarial visibility to Tier 2 review.

- **Failure message format:**

  ```
  FAIL [check 14]: D-NNN in session SNNN declares triggers_met with d016_X but session has N perspective files (expected ≥3) and no **Single-agent reason:** annotation on the decision. Either add raw-perspective outputs or annotate with reason (see multi-agent-deliberation.md §When Multi-Agent Deliberation Is Required). NOTE: this check verifies consistency of self-report, not truthfulness; see honest-limit comment in validate.sh.
  ```

**Check 15 — Non-Claude trigger coverage.**

- **Failure condition.** An in-scope decision record declares `triggers_met:` containing any `d023_*` identifier AND the session's `manifests/` subdirectory contains zero manifest entries with `participant_kind` other than `claude-subagent` and `anthropic-other` AND the decision record lacks a `**Non-Claude participation:**` annotation with both a `reason:` and a `retry_in_session:` sub-field.
- **Gating.** Session ≥006 AND check 12 (manifest well-formedness) passed for the session.
- **Severity.** **Fail**.
- **Sequencing.** BLOCKED if check 12 fails. Independent of check 14 (a decision can fail 15 while passing 14).
- **Honest-limit inline comment** (mandatory, verbatim across three locations):

  > This check verifies consistency between a decision's self-declared `d023_*` triggers and the session's non-Claude participant manifests. It does not verify that a manifest labeled non-Claude in fact represents a non-Claude participant (that is check 13's consistency scope) nor that the substantive adequacy of any skip reason is genuine (a Tier 2 concern). The declaration's truth relies on operator integrity.

- **Failure message format:**

  ```
  FAIL [check 15]: D-NNN in session SNNN declares triggers_met with d023_X but no manifest entry has participant_kind outside {claude-subagent, anthropic-other} and no **Non-Claude participation:** skip annotation is present. Either include a non-Claude participant per D-023 or record an explicit skip with reason: and retry_in_session: fields. NOTE: this check verifies consistency of self-report, not truthfulness.
  ```

**Paired Tier 2 question (Q7 in `validate.sh`):**

> For each decision in this session declaring `triggers_met:`, read the decision's `**Decision:**` and `**Rationale:**` text and state whether the declared trigger list is consistent with the decision's content. For any `**Non-Claude participation:** skipped` annotation, state whether the reason is substantive (not formulaic) and the `retry_in_session:` commitment is credible. Flag mismatches and weak reasons; they are the dishonesty surface this session's Tier 1 checks cannot reach.

**Rationale:** Four-way convergence on failure conditions (all four perspectives [`01a`, Q4; `01b`, Q4; `01c`, Q4; `01d`, Q4]). Four-way convergence on honest-limit documentation in three locations per D-029 pattern. Four-way convergence on paired Tier 2 question (each perspective proposed at least one [`01a`, Q5; `01b`, Q5; `01c`, Q5; `01d`, Q5]).

On sequencing: the Outsider's analysis [`01d`, Q4] is adopted — "Check 14 should not depend on manifest parsing or on the session-level `cross_model` claim." Check 14 inspects perspective files (the artefacts check 11 also inspects), not manifests; Archivist's [`01a`, Q4] and Skeptic's [`01c`, Q4] BLOCKED-if-12-fails proposals for check 14 conflate check 11's input with check 12's input. The Implementer [`01b`, Q4] and Outsider arrive independently at the honest dependency: check 14 ↔ check 11, check 15 ↔ check 12.

On Tier 1 placement: the Session 005 D-029 precedent is applied — Tier 1 check with mandatory D-029-pattern honest-limit documentation, complemented (not replaced) by a Tier 2 question. The Skeptic's Tier-2-primary argument [`01c`, Q4] is the same adversarial dissent made in Session 005 against check 13; the same resolution (T1 with honest-limit + T2 complement) applies.

**Rejected alternatives:**

- **Tier 2 primary placement for both checks** (Skeptic's adversarial dissent [`01c`, Q4]). Preserved as minority position and partially adopted via the Tier 2 complement. The Skeptic's decisive insight — "A mechanical check that reads `triggers_met: [none]` and passes, when the decision in fact modifies `methodology-kernel.md`, has graded a lie as a pass" [`01c`, Q4] — is acknowledged in the three-location honest-limit documentation and the paired Q7.
- **Check 14 BLOCKED if check 12 fails** (Archivist [`01a`, Q4] and Skeptic [`01c`, Q4]). Rejected on Outsider's precision argument: check 14 does not inspect manifests.
- **Check 15 independent of check 12** (not proposed by any perspective, but worth naming as rejected). Check 15 does inspect manifests (looking for `participant_kind` values); the BLOCKED-if-12-fails dependency is honest.
- **No paired Tier 2 question** (hypothetical; none of four supported). Rejected four-way.
- **Two paired Tier 2 questions (Q7 + Q8)** (Archivist's preference [`01a`, Q5]). One question is adopted; a second (Archivist's Q8 on skip-reason pattern analysis) is preserved in "what remains open."

**What remains open:**

- Whether to add a second Tier 2 question covering skip-reason-quality patterns (Archivist's Q8 [`01a`, Q5]). Deferred; can be added by a future session if skip-reason gaming becomes a visible pattern.
- Whether `retry_in_session:` commitments should themselves be structurally validated (e.g., a check that `retry_in_session: SNNN` eventually names a session where the deferred trigger was revisited). This is a candidate future Open Extension; not pursued this session.

---

## D-041: Substantive revision of `multi-agent-deliberation.md` v2 → v3 and `validation-approach.md` v2 → v3; fifth data point for OI-002

**Triggers met:** [d016_4]

**Triggers rationale:** Operator-marked load-bearing because this decision determines which files are preserved under D-004's file-level version preservation rule, and records the fifth data point on the OI-002 minor-vs-substantive heuristic. No D-023 trigger because this is a classification decision that does not itself introduce new normative content beyond D-037/D-038/D-039/D-040's normative content (those decisions already meet D-023 triggers).

**Decision:**

1. **`specifications/multi-agent-deliberation.md` is revised substantively (v2 → v3).** Adds the `triggers_met:` per-decision schema (D-037/D-038), the session-number gating rule (D-039), the two new Validation-section rules operationalised by checks 14 and 15 (D-040), and activation-precondition revision for the OI-004-narrowing cross-check (D-042). File-level preservation: v2 is preserved as `multi-agent-deliberation-v2.md` with `status: superseded`; canonical filename carries v3.

2. **`specifications/validation-approach.md` is revised substantively (v2 → v3).** Adds the two new Tier 1 checks (14, 15) with gating/severity/sequencing, the honest-limit documentation requirement for both, and the new Tier 2 question (Q7). File-level preservation: v2 is preserved as `validation-approach-v2.md` with `status: superseded`; canonical filename carries v3.

3. **Fifth data point for OI-002.** Consistent with the refined heuristic from D-026 and D-034:
   - Adding a new required frontmatter field (`triggers_met:`) with its allowed values, empty-state rule, absence semantics, and required prose sibling = new normative content = **substantive**.
   - Adding two new Tier 1 checks with new failure conditions, new gating, new sequencing, and new honest-limit documentation = new normative content = **substantive**.
   - Revising the activation precondition on one Open Extensions entry per the D-035 annotation pattern = elaboration within the section's stated purpose = **minor** (but the minor sub-revision is bundled into the substantive v2 → v3 revision and does not require separate file preservation; it is a subset of D-042's content).

**Rationale:** D-004 established file-level version preservation for substantive revisions. D-026 refined the minor-vs-substantive heuristic. D-034 applied the heuristic to a pair of simultaneous revisions (one substantive, one minor, resolved separately). This session applies the heuristic to a pair of simultaneous revisions that are **both** substantive — the first session where both active revisions cross the substantive threshold. The heuristic holds cleanly; no further refinement of OI-002 is warranted.

**Rejected alternatives:**

- **Treat the `multi-agent-deliberation.md` v2 → v3 revision as minor** (hypothetical; not argued for by any perspective). Rejected because the schema extension adds new required fields and new gating rules — both explicitly cited in the OI-002 heuristic as substantive triggers.
- **Treat the `validation-approach.md` v2 → v3 revision as minor** (hypothetical). Rejected: new Tier 1 checks with new severity/gating/sequencing are paradigmatically substantive per the heuristic.
- **Bundle all the substantive revisions under a single v3** (hypothetical; do one version bump covering both). The decision does bundle them in the *same session*, but they remain two distinct specification files with distinct version histories. Each file gets its own v3.

**What remains open:**

- OI-002's data point count rises to five. The heuristic has held across: minor (D-014 `tools/` addition; D-020 kernel pointer; D-034 Open Extensions annotations) and substantive (D-026 multi-agent-deliberation v1 → v2; D-034 validation-approach v1 → v2; now D-041 both specs v2 → v3). No refinement warranted. A future session may add further data points.

---

## D-042: Open Extensions — no promotions this session; revise OI-004-narrowing check's activation precondition

**Triggers met:** [d016_4]

**Triggers rationale:** Operator-marked load-bearing because the OI-004-narrowing cross-check's activation precondition is a load-bearing future-trigger whose phrasing determines when the check becomes implementable. The precondition revision is itself **minor** per D-035's annotation pattern (elaboration within the Open Extensions section's stated purpose); no file-level version preservation required beyond the v3 bundled in D-041.

**Decision:**

1. **No Open Extensions promoted to normative** in Session 006. The session's normative content is bounded by the `triggers_met:` schema (D-037, D-038), the gating rule (D-039), and the two new validation checks (D-040).

2. **OI-004-narrowing cross-check's activation precondition revised.** The current v2 Open Extensions entry reads: "a `triggers_met:` (or equivalent) schema extension is added to decision-record frontmatter (prerequisite for v2 Validation checks 1 and 2). First test case now exists: Session 005's D-033 narrowing."

   Revised to: "`triggers_met:` is adopted prospectively (D-037 through D-040) AND at least one post-adoption decision asserting an OI-004 state change exists, OR a separate non-mutating retrospective index has been produced for earlier cases per the D-039 retrospective-artefact pattern."

3. **Other Open Extensions preconditions unchanged.**

**Rationale:** Three-of-four explicit non-promotion [Implementer `01b`, Q6; Skeptic `01c`, Q6; Outsider `01d`, Q6]. Archivist proposes "promote to normative but defer implementation to Session 007" [`01a`, Q6], which is substantively identical to deferral — the practical outcome is the same (no new normative content on Open Extensions this session).

The precondition revision adopts the three-way converging phrasing from Implementer/Skeptic/Outsider [`01b`, Q6; `01c`, Q6; `01d`, Q6]. The revision's reason is twofold:

- **Post-adoption test case required.** The v2 precondition cited Session 005's D-033 as the first test case, but under D-039's session-number gating D-033 predates the `triggers_met:` schema. A derivative check would have no actual in-scope test case until a post-adoption OI-004-state-change decision is made.
- **Conflict of interest** (Skeptic [`01c`, Q6]). Implementing the check in Session 006 would require grading Session 006's own OI-004 tally advance (which is itself the session's D-043 decision, a post-adoption OI-004 state change). A check grading its own originating session is structurally problematic for its first firing.

**Rejected alternatives:**

- **Promote OI-004-narrowing check and implement in Session 006** (Archivist's hypothetical promote-and-implement, though Archivist explicitly recommended defer-implementation [`01a`, Q6]). Rejected on (a) scope-creep grounds — Session 006 already revises two specs, adds one schema, two validator checks, and one Tier 2 question; adding a third check strains the session; (b) conflict-of-interest grounds per Skeptic.
- **Leave the v2 precondition unchanged.** Rejected because the v2 wording is now inaccurate: the cited "first test case" (Session 005 D-033) is out-of-scope under D-039's session-number gating. Precondition revision is a D-035-pattern annotation refinement — minor, appropriate, required to keep the Open Extensions entry honest.
- **Revise preconditions for other Open Extensions this session.** Rejected: no perspective argued any other precondition needs revision now, and revising them without evidence is the kind of drift-to-ritual OI-009 monitors for.

**What remains open:**

- When a post-adoption OI-004 state-change decision is made (e.g., a future session advances the tally from 2 to 3 of 3, or formally closes OI-004), the OI-004-narrowing cross-check becomes implementable. A subsequent session may then design and implement it.
- The list of other Open Extensions in `multi-agent-deliberation.md` v3 retains the D-035 activation-precondition annotations from Session 005 unchanged.

---

## D-043: OI state — OI-004 sustained-practice tally advances (1 → 2 of 3); status unchanged; no other OI changes

**Triggers met:** [d023_4]

**Triggers rationale:** The tally advancement is a recorded change in OI-004's state (the tally note is part of OI-004's state, distinct from its status label which is unchanged). D-023 trigger 4 ("Asserts a change in the state of OI-004") applies on a literal reading: the state is updated, even though the status label is not. Satisfied by Outsider participation per D-024 schema.

**Decision:**

1. **OI-004** — status **unchanged** (`narrowed-pending-sustained-practice`); sustained-practice tally **updated from 1 of 3 to 2 of 3**. Narrowing note updated to reflect Session 006 as the second required-trigger deliberation with non-Claude participation.

2. **OI-002** — open (fifth data point added by D-041).

3. **OI-001** (naming the methodology) — open, unchanged. Not addressed this session.

4. **OI-005, OI-006, OI-007, OI-008, OI-011** — open, unchanged. None addressed this session.

5. **OI-009** — open. Session 006 audited Session 005's pattern application (see `00-assessment.md`); no drift-to-ritual signal. Session 006's own pattern application shows no drift — the deliberation was scoped to a load-bearing question meeting multiple triggers (D-016.2, D-023.2, D-023.3) and produced a cross-model divergence (presence vs session-number gating) that materially shaped D-039's outcome. Continue monitoring.

**No new open issues.** The Archivist's meta-note about clause-identifier stability under future D-016/D-023 renumbering is recorded in D-037's "what remains open" but does not warrant a standalone open issue yet — the append-only identifier rule addresses most of the concern and no concrete renumbering instance has surfaced.

**Rationale:** Housekeeping consolidation, consistent with Session 005 D-036 and Session 004 D-027 closing-accounting patterns. The sustained-practice tally advance is recorded explicitly per v2 spec closure criteria's requirement for visible per-session accounting. Session 006 is the second required-trigger heterogeneous-participant deliberation; Session 005 was the first; both are now counted.

The recorded impact of the Outsider's non-Claude participation on this session's outcomes (criterion-3 partial evidence for OI-004):

- **Precise check-14 independence from manifest parsing** (Outsider [`01d`, Q4]): adopted in D-040's sequencing rule. No Claude perspective independently arrived at this precision.
- **Separate-retrospective-artefact pattern** for historical trigger classification (Outsider [`01d`, Q3], convergent with Skeptic [`01c`, Q3]): recorded in D-039 as the immutability-preserving path for future analytic needs.
- **Mislabeled-manifest gaming pattern** (Outsider [`01d`, Q5]): recorded in the synthesis's Cross-Model Observations; adjacent to but distinct from D-029's wrapper-impersonation gaming mode.

These three influences extend the Session 005 set (sequencing rule, gate granularity, paper-human classification). The tally-of-influences grows; a formal cross-lineage-influence ratio remains deferred per v2 spec Open Extensions.

**Rejected alternatives:**

- **Open OI-012 for identifier-stability concern** (Archivist's meta-note suggestion). Rejected per Skeptic's "wait for a real instance" principle: "Speculative mechanism design on adversarial surfaces produces mechanisms that cover the designer's imagined attacks, not the attacks that arise" [`01c`, Meta-note]. If a future session renumbers trigger clauses and breaks existing identifiers, that is the instance; open the OI then.
- **Close OI-009** (hypothetical; not argued). Rejected for the standing reason: drift-to-ritual is a trend concern requiring multi-session observation. Session 006 audit shows no drift; closing the monitor based on three clean sessions would be premature.
- **Assert a further narrowing of OI-004 beyond tally advance** (hypothetical). Rejected: closure criteria 2 requires ≥3 sustained-practice sessions; one more is needed. Criterion 4 (articulation of "substantively different training provenance") remains unaddressed. The honest recording is tally-advance-only; this is not narrowing-progress-warmth.

**What remains open:**

- The path to OI-004 tally of 3 of 3: depends on a future required-trigger deliberation (any D-023 trigger) with non-Claude participation. Session 007 or later.
- OI-004 closure criterion 4 (articulation of "substantively different training provenance"): not on any session's docket yet. A future session may address it as a prerequisite step toward OI-004 closure.
- The Archivist's identifier-stability concern (recorded in D-037): may warrant OI-012 if a concrete renumbering instance arises.
