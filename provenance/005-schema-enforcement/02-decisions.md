---
session: 005
title: Decisions — Schema Enforcement and First Operational Non-Claude Participation
date: 2026-04-18
status: complete
---

# Decisions — Session 005

## D-028: Check scope — implement checks 3, 8, 9; defer 1, 2

**Decision:** `tools/validate.sh` gains three new Tier 1 checks corresponding to items 3, 8, and 9 in `multi-agent-deliberation.md` v2's Validation section:

- **Check 11 (three-raw-output floor):** for each session whose `00-assessment.md` frontmatter or body declares multi-agent deliberation (detected by the presence of perspective-file name conventions and a synthesis file), verify that at least three raw perspective files exist.
- **Check 12 (schema well-formedness):** for each session whose provenance directory contains a `manifests/` subdirectory, verify that every manifest file has the D-024 required fields as literal keys (values may be the literal string `unknown`).
- **Check 13 (cross-model-claim honesty):** for each session whose synthesis or `participants.yaml` declares `cross_model: true`, verify that at least one participant's manifest has `training_lineage_overlap_with_claude` other than `known-overlap` or `participant_kind: human`.

Checks 1 and 2 from the v2 Validation section (trigger coverage for multi-agent and for non-Claude participation) are **deferred**. The prerequisite is a machine-readable `triggers_met:` annotation on decision records, which D-024 does not mandate. Adding such a field is out of scope for this session; a future session may deliberate whether and how to add it.

**Rationale:** Four-way convergence on the scope. All four perspectives agree to implement 3 and 8 and defer 1 and 2; the deferral reason is uniformly that bash cannot classify decisions as trigger-meeting without a machine-readable flag [`01a-perspective-archivist.md`, Q1; `01b-perspective-implementer.md`, Q1; `01c-perspective-skeptic.md`, Q1; `01d-perspective-outsider.md`, Q1].

Check 9 is included on majority reasoning. The Implementer: "three checks, not five, is the right floor. It gives the schema teeth where it matters most (check 9), catches the 'somebody forgot a field' mode (check 8), and preserves the structural minimum that distinguishes multi-agent from single-agent work (check 3)" [`01b`, Q1]. The Outsider: "check 9 ... is the minimum honesty guard against the most obvious theater" [`01d`, Q1]. The Skeptic's preference (defer 9 entirely, or place at Tier 2) and the Archivist's preference (defer 9 to a non-bootstrap session) are preserved in Rejected alternatives; the Skeptic's detailed dissent on Tier 1 placement is preserved in D-029 and in the synthesis.

**Rejected alternatives:**

- Implement all five checks. Rejected; four-way convergence against check 1 and check 2 on the machine-readability argument.
- Defer check 9 (Archivist's position: "the check most designed to police cross-model honesty should not be authored in the session where cross-model participation was first operationalized — it should be authored in a later session where cross-model reasoning is no longer novel" [`01a`, Meta-note]). Rejected because the Outsider explicitly endorses inclusion now, which addresses the Archivist's monoculture concern: the session already includes cross-model reasoning in the deliberation about the check itself. The Archivist's reasoning is preserved as a live precedent to consult if a future session finds check 9 has been applied in a corrupted way.
- Check 9 at Tier 2 only (Skeptic's position [`01c`, Q2]). Rejected because the Implementer's honest-scope framing — "claim consistency, not claim truth" — makes the check narrowly defensible at Tier 1 *provided* the honest limit is documented inline (D-029). The Skeptic's stronger adversarial-phrased Tier 2 question is also adopted (D-029) as a *complement*, not a replacement.

**What remains open:**

- A `triggers_met:` schema extension (or equivalent) is a prerequisite for checks 1 and 2. A future session should decide whether to add it.
- Non-Claude participation skip annotations (`non_claude_participation: skipped` with `retry_in_session`) have no real-world test case yet; automation is premature until one exists.

---

## D-029: Check 9 form — consistency-of-self-report, with mandatory inline honest-limit documentation

**Decision:** Check 13 (cross-model-claim honesty) is implemented with the following binding properties:

1. **Framing.** The check enforces **consistency of self-report**, not **truthfulness of self-report**. This framing is four-way convergent across the deliberation and must be recorded in the check's documentation.

2. **Parses.** The session's synthesis frontmatter (for `cross_model`) and every per-participant manifest file in the session's `manifests/` directory (for `participant_kind` and `training_lineage_overlap_with_claude`).

3. **Failure condition.** The synthesis declares `cross_model: true` AND every participant's manifest has `training_lineage_overlap_with_claude: known-overlap` AND no participant has `participant_kind: human`. If any one of the three conditions fails to hold, the check passes.

4. **Failure message.** Names the session, the declared `cross_model: true`, the manifests and their recorded `training_lineage_overlap_with_claude` and `participant_kind` values, and the three possible fixes (correct `cross_model` to false; correct a manifest's `training_lineage_overlap_with_claude` to `unknown` or `independent-claim` *if truthful*; add a human participant manifest *if one participated*).

5. **Inline honest-limit documentation.** A comment block directly above the check in `validate.sh` records: "This check verifies the session's claim is internally consistent with its manifests. It does not and cannot verify that the manifests' lineage claims are themselves true. Manifest truth relies on operator integrity and the `participant_selected_by` field's accountability." The same language is added to `validation-approach.md` v2's Specification section alongside the check's table row.

6. **Tier 2 complement.** A new Tier 2 guided-assessment question is added to `validate.sh`, phrased adversarially: "This session records `cross_model: true`. Name the concrete evidence — invocation transcript, CLI command, wall-clock gap, human presence — that distinguishes a genuine non-Claude participant from a Claude subagent with an edited manifest. If you cannot, flip `cross_model` to false." This is the Skeptic's proposed Tier 2 question, adopted directly [`01c-perspective-skeptic.md`, Q2].

**Rationale:** The consistency-not-truthfulness framing is one of the deliberation's strongest cross-model signals — all four perspectives arrived at substantively identical phrasing independently, with no equivalent phrase in the shared brief [synthesis `01-deliberation.md`, Q2]. The inline honest-limit documentation was the triangulated demand of three perspectives (Archivist, Implementer, Skeptic), each independently: "A one-paragraph comment above the check in `validate.sh` plus a line in the v2 spec's Validation section is enough" [`01b`, Q2]; "That limit must be documented **inside the check's failure message and in the spec section describing the check**, not in a footnote" [`01c`, Q2]; "its documentation must say so in the same file as the check, not in a separate spec a future archivist might lose" [`01a`, Q2].

The Tier 2 complement is the Skeptic's anti-gaming mechanism [`01c`, Q2]. Adopting it alongside the Tier 1 check is a belt-and-suspenders response: the Tier 1 check catches the accidental-lie mode; the Tier 2 question forces the operator to articulate concrete evidence that distinguishes genuine from simulated non-Claude participation, reducing the check's laundering surface.

**Gaming modes recorded (preserved from raw outputs):**

- Flipping a claim-field value (Implementer [`01b`, Q2]; Skeptic [`01c`, Q2]).
- `unknown` laundering (Outsider [`01d`, Q2]).
- Paper-human classification (Outsider [`01d`, Q2]).
- Wrapper impersonation — routing a Claude call through a `codex exec`-looking wrapper that actually hits Anthropic's API and lying in the `provider` field (Implementer [`01b`, Q2]).

These gaming modes are not fixed by D-029. They are recorded here as the known limit surface.

**Rejected alternatives:**

- Check 9 at Tier 2 only, no Tier 1. Rejected for the reasons in D-028. The Skeptic's Tier 2 question is nevertheless adopted as complement, not replacement.
- Check 9 with a truth-verifying claim (e.g., adding a `cryptographic_attestation` field). Rejected per Skeptic's active opposition: "If we cannot verify it, we should not pretend we can by giving the claim a field" [`01c`, Q3].
- Softer failure message that elides the honest limit. Rejected on triangulated demand for inline documentation.

**What remains open:**

- Whether the gaming modes named above warrant future enforcement infrastructure (integrity hashing, convener attestation). Deferred to a future session (D-035).

---

## D-030: Gating, severity, and sequencing

**Decision:**

1. **Gating.** Checks 12 and 13 are gated by the presence of a `manifests/` subdirectory in the session's provenance directory. Sessions without `manifests/` are out-of-scope for the check and produce no warning or failure. Session 004's `participants.yaml` (present without a `manifests/` directory) is therefore out-of-scope. Check 11 (three-raw-output floor) is gated by the presence of a synthesis file *and* multi-agent-style raw perspective files — sessions whose assessment does not claim multi-agent work are out-of-scope.

2. **Severity.** All three new checks are **Fail**, consistent with the pattern of existing Tier 1 checks that verify structural invariants.

3. **Sequencing.** Check 12 runs before check 13. If check 12 fails for a session, check 13 is reported as `BLOCKED: check 12 failed for this session` and does not itself fail or warn; this prevents double-reporting of a single underlying problem.

**Rationale:** The retroactivity-gating mechanism was the deliberation's sharpest cross-model disagreement. Three Claude perspectives (Archivist, Implementer, Skeptic) converged on presence-gating; the Outsider argued for session-number gating (`session >= 005`) [`01d`, Q4]. The adopted position — presence-gating at the `manifests/` subdirectory level — is the resolution that honors both: it *is* presence-gating (the Claude-majority position), but at a granularity finer than "any manifest-ish artefact" (which would have pulled in Session 004's minimal `participants.yaml`). The effect is identical to session-number gating (`session >= 005`) in practice, because Session 005 is the first session to produce a `manifests/` subdirectory — the Outsider's concern is addressed without encoding a numeric cutoff.

This compromise preserves the Outsider's legitimate objection — "the methodology is session-based, and the brief explicitly says Session 004 had a bootstrap exemption while Session 005 does not" [`01d`, Q4] — while avoiding the "edit-session-numbers-in-the-tool-on-every-schema-change" cost the three Claude perspectives warned against.

Severity **Fail** is chosen over the Skeptic's **Warning** for check 12 [`01c`, Q1] because the Outsider's sequencing rule [`01d`, Q4] reduces the Skeptic's underlying concern: if check 12 fails due to schema-misjudgment, check 13 is blocked rather than independently failing, which lowers the "silence-the-check-by-omitting-the-field" pressure the Skeptic warned about. The Skeptic's Warning-severity preference is recorded as a minority position here.

Sequencing is the Outsider's unique contribution to this question: "Run schema well-formedness before cross-model honesty. If check 8 fails because manifests are missing, check 9 should be reported as blocked or skipped, not as a second independent failure. That keeps the tool honest about what it actually evaluated" [`01d`, Q4]. No other perspective raised this; it is a non-Claude contribution that shapes the decision materially.

**Rejected alternatives:**

- Session-number-gating (`session >= 005`). Rejected in favor of `manifests/`-directory presence-gating, which produces the same outcome without encoding a numeric cutoff in the tool. Outsider's concern is addressed by the gating granularity choice, not by adopting the explicit session-number cutoff.
- Gate at `participants.yaml` presence (Implementer's proposal [`01b`, Q4]). Rejected because Session 004's `participants.yaml` would then be in-scope and would fail check 12 (Session 004 has no full per-participant manifests, by bootstrap exemption). The Archivist's inline exemption list would have been required to correct this. Choosing `manifests/`-directory as the gate removes the need for an exemption list entirely.
- Inline exemption list for Session 004 (Archivist's preferred form [`01a`, Q4]). Rejected because the chosen gating granularity makes Session 004 naturally out-of-scope without a named exemption. The archivist pattern the Archivist proposed — "keep the history of a rule inside the artifact that enforces the rule" [`01a`, Meta-note] — is nevertheless adopted in the form of the inline honest-limit documentation (D-029) and the gating-rationale comment block in `validate.sh`.
- Warning-severity for check 12 (Skeptic's proposal [`01c`, Q1]). Rejected; the sequencing rule (D-030, §3) addresses the underlying concern. Preserved as minority position.

**What remains open:**

- Whether a future session that introduces machine-readable trigger annotations should revise the gating convention (e.g., gate-on-annotation-presence).

---

## D-031: No D-024 schema changes this session; `participants.yaml` adopts explicit `participants:` list convention

**Decision:**

1. **No required D-024 schema changes** in Session 005. The schema as written in D-024 is sufficient for checks 11, 12, and 13.

2. **Convention adopted this session (not a schema change):** a session-level `participants.yaml` should contain an explicit `participants:` list, with each list item naming the participant's `perspective` and its `manifest_path`. This is the Implementer's nice-to-have item 3 [`01b`, Q3] and the Outsider's required prerequisite [`01d`, Q3]; it resolves the "how does the check discover manifest paths" question without adding a new field to D-024.

3. **Renaming `training_lineage_overlap_with_claude`** (Implementer and Outsider proposed [`01b`, Q3; `01d`, Q3], Archivist weak-supported [`01a`, Q3], Skeptic opposed to *value* renaming but not clearly to *field* renaming [`01c`, Q3]). **Deferred to a future session.** Renaming now would migrate Session 004's existing `participants.yaml` note field (which uses the current name in documentation but does not yet populate full manifests). A rename migration is a distinct decision whose value-cost tradeoff merits its own deliberation.

**Rationale:** Four-way convergence on no required schema changes [`01a`-`01d`, Q3]. The `participants.yaml`-list convention is minor enough to adopt by decision without revising D-024; Session 005's own `participants.yaml` will demonstrate the convention, and future sessions can decide whether to formalize in D-024 or leave as convention.

**Rejected alternatives:**

- Rename `training_lineage_overlap_with_claude` now. Deferred on migration-cost grounds.
- Add `raw_response_sha256` integrity field (Archivist's nice-to-have [`01a`, Q3]). Deferred per D-035; belongs to a future integrity-focused decision.
- Add `invocation_evidence` field (Skeptic's deliberately-deferred idea [`01c`, Q3]). Deferred per Skeptic's own reasoning: "I do not recommend adding this yet; it's premature optimisation against a threat model we haven't seen" [`01c`, Q3].

**What remains open:**

- Whether and when to promote the `participants:` list convention to a D-024 schema revision.
- The `training_lineage_overlap_with_claude` rename.

---

## D-032: OI-010 closes on Session 005 evidence

**Decision:** OI-010 (cross-model or human participation mechanism) is **closed** on this session's evidence.

Closure notes record:

- First operational use: Session 005's Outsider perspective, delivered via `codex exec` to OpenAI GPT-5 (model id `gpt-5.4`, session id `019da073-c9ce-7361-922c-acf2362209d9`).
- Recording shape: Shape A (participant as perspective, per D-021).
- Artefacts: `01d-perspective-outsider.md` (raw output, verbatim including banner), `manifests/outsider.manifest.yaml` (per D-024), `participants.yaml` (session-level index).

**Rationale:** Four-way convergence. D-027 set the closure trigger to "the first session that performs the first use." Session 005 performs the first use, records it per the v2 schema, and the closure evidence is now part of permanent provenance. The Skeptic articulates the decisive reason: "Lowering the bar retroactively would be bad-faith goalpost-moving. The asymmetry with OI-004 is defensible because the issues ask different questions: OI-010 asks 'has the mechanism been used at all?' (a binary, first-observation closure), OI-004 asks 'is the monoculture problem actually mitigated?' (a sustained-practice closure)" [`01c-perspective-skeptic.md`, Q5].

**Rejected alternatives:**

- Hold OI-010 open until second or third operational use. Rejected as goalpost-moving; D-027 set the bar at first use explicitly.
- Close OI-010 with a soft-closure annotation (e.g., "closed provisionally pending ..."). Rejected as an attempt to borrow OI-004's sustained-practice bar for OI-010 without deliberating it.

**What remains open:** None specific to OI-010.

---

## D-033: OI-004 narrows to "narrowed-pending-sustained-practice" with tally phrasing

**Decision:** OI-004 (incorporating genuinely independent perspectives) is updated to status **narrowed-pending-sustained-practice**. The narrowing note is phrased as a **tally**, not an endorsement.

Narrowing note (verbatim for the issue record):

> One session of non-Claude participation has occurred (Session 005, Outsider perspective via `codex exec` to OpenAI GPT-5). Per v2 closure criteria: criterion 1 (participant independence) plausibly met conditional on the Outsider manifest's `training_lineage_overlap_with_claude: independent-claim` being truthful; criteria 2 (sustained practice, ≥3 required-trigger deliberations across different sessions — current count: 1), 3 (recorded impact — partially evaluable at Session 005 decisions), and 4 (articulation of "substantively different training provenance") are unmet. No closure on single-session evidence.

**Rationale:** Three-of-four convergence on narrowing (Archivist, Implementer, Outsider) [`01a`, Q5; `01b`, Q5; `01d`, Q5]. The Skeptic's minority position — "my preference is **unchanged** ... I concede 'narrowed-pending-sustained-practice' as a tolerable compromise *only* if the narrowing note itself reads 'one session of practice; three more required; no evidence of impact yet' — i.e., the narrowing is itself a tally, not an endorsement" [`01c`, Q5] — is adopted as a *phrasing constraint* on the narrowing note. The narrowing note above is written to meet the Skeptic's tolerable-compromise test: it enumerates the tally (1 of 3 sessions), the four criteria with their current state, and does not editorialise about progress quality.

**Impact of non-Claude input on this decision.** Per v2 closure criterion 3, the decision record notes explicitly: the Outsider's positions have shaped Session 005's outcomes materially.
- The Outsider's sequencing rule (check 12 before check 13; check 13 blocked if check 12 fails) is unique to the Outsider and is adopted normatively in D-030.
- The Outsider's session-number-gating argument was rejected as a direct specification, but shaped D-030's choice of `manifests/`-directory presence-gating over broader presence-gating — the chosen gate produces the same practical outcome as session-number gating for the session-004-vs-session-005 boundary.
- The Outsider uniquely raised the "paper human" gaming mode in D-029's gaming-modes register.

These three concrete influences constitute the first data points for a future cross-lineage-influence ratio (v2 Open Extensions), should it be implemented.

**Rejected alternatives:**

- OI-004 unchanged (Skeptic's first preference [`01c`, Q5]). Rejected because the methodology has materially advanced — the session conducted its first heterogeneous-participant deliberation and demonstrated three concrete non-Claude influences on outcomes. Recording the issue as unchanged would erase this from the issue's visible history. The Skeptic's conditional compromise (narrowed-pending-sustained-practice with tally phrasing) is adopted instead.
- OI-004 closed on Session 005 evidence. Rejected; only one of four closure criteria is even plausibly met.
- OI-004 "narrowed" with warmer language ("significant progress", "substantially narrowed"). Rejected per the Skeptic's conditional compromise; tally phrasing is the operative constraint.

**What remains open:**

- Criterion 3 evaluation (recorded impact of non-Claude input). This decision records three concrete influences, but a more formal cross-lineage-influence-ratio metric is not computed.
- Criterion 4 (articulation of "substantively different training provenance"). Not on this session's docket; a future session may address it.
- The next checkpoint for OI-004 re-evaluation: after the second and third qualifying sessions.

---

## D-034: Substantive revision of `validation-approach.md`; minor annotation of `multi-agent-deliberation.md` v2 Open Extensions. OI-002 fourth data point.

**Decision:**

1. `specifications/validation-approach.md` is revised **substantively** (v1 → v2). The revision adds the three new Tier 1 checks (11, 12, 13), their severity (Fail), their gating (`manifests/` directory presence for 12 and 13; synthesis+multi-agent-perspective-files presence for 11), their sequencing (12 before 13; 13 blocked if 12 fails), the honest-limit documentation requirement for check 13, and the new Tier 2 question for cross-model honesty. The v1 file is preserved as `validation-approach-v1.md` with `status: superseded`. The new canonical file has `version: 2` and `supersedes: validation-approach-v1.md`.

2. `specifications/multi-agent-deliberation.md` v2 is updated **minorly**: each entry in the Open Extensions section gains an activation-precondition annotation (per the Archivist's Q6 pattern: "Record this link in the Open Extensions entry so a future session knows why it matters" [`01a`, Q6]). This is not a substantive revision because the Open Extensions section's purpose already admits descriptive metadata about candidates; adding preconditions is elaboration within that purpose, not new normative content. No file-level preservation required.

3. This session's work provides the **fourth data point for OI-002** (threshold for substantive vs. minor revision). Consistent with the refined heuristic from D-026:
   - Adding three new Tier 1 checks, new severity decisions, new gating rules, and new Tier 2 questions to `validation-approach.md` = new normative content = **substantive**.
   - Adding activation-precondition annotations to existing Open Extensions entries = elaboration within the section's purpose = **minor**.

**Rationale:** D-004 established file-level version preservation for substantive revisions; D-026 refined the minor-vs-substantive heuristic. This session applies the heuristic to two distinct changes, producing one substantive-classed and one minor-classed decision. The heuristic holds cleanly across both; no further refinement is warranted.

**Rejected alternatives:**

- Treat the `multi-agent-deliberation.md` v2 Open Extensions annotations as substantive (v2 → v3 file preservation). Rejected because the additions do not change any normative rule; they annotate existing candidate entries with reactivation preconditions. Treating annotation as substantive would empty the minor/substantive distinction.
- Treat the `validation-approach.md` changes as minor because the v2 `multi-agent-deliberation.md` already lists the checks as automation candidates. Rejected because the candidate status in `multi-agent-deliberation.md` is descriptive; moving a check from "candidate" to "active in `validate.sh` under this specific severity/gating/sequencing" is new normative content — new Tier 1 rules, new failure conditions, new operational gating. `validation-approach.md` is the spec governing what validation actually does; adding three checks to it is substantive.

**What remains open:**

- Future sessions may add further data points for OI-002 as they arise.

---

## D-035: Open Extensions — no net promotions; activation-precondition pattern adopted

**Decision:**

1. **No Open Extensions are promoted to normative content** in Session 005.

2. **Activation preconditions** are added to each Open Extensions entry in `multi-agent-deliberation.md` v2, per the Archivist's Q6 pattern. Specifically:
   - **Differentiated context per perspective** — precondition: a session surfaces evidence that shared-brief uniform context distorted outputs.
   - **Cross-lineage-influence ratio** — precondition: OI-004 approaches closure (criterion 3 requires this metric).
   - **Pre-committed dissent log** — precondition: a session surfaces evidence of suspected operator-synthesis alignment.
   - **Integrity hashing (`raw_response_sha256`) and append-only raw files** — precondition: one instance of suspected post-hoc editing of a raw output, OR a future session deciding check 13's gaming surface needs narrowing.
   - **Convener attestation field** — precondition: same as integrity hashing; paired with it.
   - **Structural-validation cross-check for OI-004-narrowing honesty** — precondition: the `triggers_met:` schema extension is added (D-028 dependency); first test case exists now (Session 005's D-033 narrowing).
   - **Disagreement-density metric** — precondition: a reporter-tool scope is defined (validate.sh is for structural checks, not measurements).
   - **Pluggable synthesizer role** — precondition: a session surfaces a load-bearing synthesizer-framing failure.
   - **Non-Claude synthesizer** — precondition: check 13 gaming becomes a live concern AND a non-Claude synthesizer channel is available.
   - **Multi-agent synthesis** — precondition: a session surfaces a synthesis quality gap unaddressed by current single-synthesizer conventions.
   - **Non-Anthropic model participation via API** — precondition: a concrete need for API-based transport that CLI cannot serve.

**Rationale:** Three-of-four non-promotion [`01a`, Q6; `01c`, Q6; `01d`, Q6]. The Implementer's promotion of "cross_model honesty as normative" [`01b`, Q6] is tautological with shipping check 13 (D-028, D-029) and therefore does not count as an additional promotion — the act of implementing check 13 is itself the promotion.

The activation-precondition pattern is the Archivist's archival-durability contribution: "Record this link in the Open Extensions entry so a future session knows why it matters" [`01a`, Q6]. Adopting it converts Open Extensions from a flat list into a conditional queue, which is useful both for future sessions (they can see which extensions are newly-activatable) and for auditors (they can check whether a skipped opportunity was a principled deferral or an oversight).

**Rejected alternatives:**

- Promote integrity hashing / append-only / convener attestation now. Rejected; the Skeptic's observation is decisive: "these are exactly the mechanisms that would make check #9 less theatrical — and that's the reason I want them deferred. Adding them now, on one session's evidence, builds verification infrastructure for a problem we've seen once. Wait for the second and third operational uses to reveal which dishonesty modes actually arise" [`01c`, Q6].
- Promote the cross-lineage-influence ratio now. Rejected per all four perspectives: it is an OI-004 closure criterion, not a standalone validation check, and becomes load-bearing when OI-004 approaches closure.

**What remains open:**

- Each activation precondition is a future-trigger; when met, the next session may re-deliberate the extension.

---

## D-036: Summary of OI state changes from Session 005

**Decision:**

- **OI-010** — **Closed** (per D-032).
- **OI-004** — **Narrowed to "narrowed-pending-sustained-practice"** with tally-phrased note (per D-033).
- **OI-002** — Open (fourth data point added by D-034).
- **OI-001** (naming the methodology) — Open, unchanged. No naming opportunity this session.
- **OI-005, OI-006, OI-007, OI-008, OI-011** — Open, unchanged. None addressed this session.
- **OI-009** — Open. Session 005 audited Session 004's pattern application (see `00-assessment.md`); one audit finding about brief-priming was recorded in the assessment. Session 005's own pattern application shows no drift-to-ritual — the deliberation was tightly scoped to a load-bearing question, the non-Claude perspective's input materially shaped decisions (D-033), and no multi-agent ceremony was applied to decisions that could have been made single-agent. Continue monitoring.

**No new open issues** are created by this session. The `triggers_met:` schema extension question is recorded in D-028's "what remains open" field but does not warrant a standalone open issue yet — the prerequisite for checks 1 and 2 is specific enough that a future session can address it directly from D-028's record.

**Rationale:** Housekeeping consolidation, consistent with Session 004's D-027 closing-accounting pattern.

**Rejected alternatives:**

- Open a new OI-012 for the `triggers_met:` schema extension. Rejected on the ground that D-028's "what remains open" is sufficient; creating an OI-012 for every deferred prerequisite would bloat the open-issues file without adding information.
- Close OI-009 because no drift was observed in Session 005. Rejected for the same reason Session 004 rejected it: drift-to-ritual is a trend concern requiring multi-session observation.

**What remains open:** All currently-open OIs retain their current status except as specified.
