---
session: 005
title: Deliberation — Schema Enforcement and First Operational Non-Claude Participation (synthesized)
date: 2026-04-18
status: complete
synthesizer: session-005 orchestrating agent (Claude Opus 4.7, same model family as 3 of 4 deliberators; not the Outsider's model family)
synthesizer-independence: did not play any of the four perspectives (Archivist, Implementer, Outsider, Skeptic)
deliberation-anchor-commit: 6e434ec876552b71ae4326a3787a83553276cfa9
perspective-order: alphabetical by role name (Archivist, Implementer, Outsider, Skeptic)
participants_family: cross-model
cross_model: true
non_claude_participants: 1
---

# Deliberation — Session 005: Schema Enforcement and First Operational Non-Claude Participation

## How This Deliberation Was Conducted

Four perspectives were convened. Three were parallel context-isolated Claude subagents (Claude Opus 4.7) launched via Claude Code's Agent tool: The Archivist, The Implementer, and The Skeptic (required adversarial). The fourth, The Outsider, was a non-Claude participant: OpenAI GPT-5 (model id `gpt-5.4`, OpenAI session id `019da073-c9ce-7361-922c-acf2362209d9`) invoked via the `codex` CLI in non-interactive (`exec`) mode, `sandbox: read-only`, `reasoning effort: xhigh`. All four received the shared brief committed at `6e434ec876552b71ae4326a3787a83553276cfa9`. None saw the others' outputs during the independent phase. The Outsider's response is committed verbatim — including the CLI banner, the prompt echo, and the end-of-stream duplicate response — per D-021's transport-faithfulness requirement. Raw outputs are preserved at:

- `01a-perspective-archivist.md` (Claude Opus 4.7)
- `01b-perspective-implementer.md` (Claude Opus 4.7)
- `01c-perspective-skeptic.md` (Claude Opus 4.7, required adversarial)
- `01d-perspective-outsider.md` (GPT-5 via Codex CLI)

Perspectives are presented alphabetically throughout this synthesis to reduce synthesizer-ordering bias (D-018).

**This is the methodology's first truly heterogeneous-participant deliberation.** Session 004 specified the mechanism; Session 005 operationalises it. The Outsider's response was committed before synthesis began (the halt-before-synthesis rule of D-021 was satisfied because the Outsider returned synchronously within the session).

## Synthesis Conventions

Following D-018 and reaffirmed in Session 004: claims attributing a position to a perspective cite the source file and question; claims not directly sourced are marked `[synth]`; load-bearing language is quoted rather than paraphrased; dissent is preserved as dissent; convergence (all perspectives independently reached a similar conclusion) is distinguished from coverage (only one perspective raised a point, others silent).

**Additional convention for this session**, in response to a synthesis-audit finding recorded in `00-assessment.md`: where the brief's own language has seeded a phrase used by multiple perspectives, the synthesis calls this out rather than treating lexical echo as independent convergence.

---

## Q1: Scope — which of the five candidate checks to implement

**Convergence.** All four perspectives agree to implement **check 3 (three-raw-output floor)** and **check 8 (schema well-formedness)**. All four defer **check 1 (trigger coverage for multi-agent)** and **check 2 (trigger coverage for non-Claude)**. The deferral reason converges across all four: the triggers are semantic prose, not machine-readable flags on decisions; a bash check would have to guess at semantic classification.

- Archivist: "Bash cannot classify a decision record as trigger-meeting without a human or model judgment. What's missing is a machine-readable trigger annotation on decision records — e.g., a frontmatter field `triggers_multi_agent: true | false | n/a`" [`01a-perspective-archivist.md`, Q1].
- Implementer: "Prerequisite missing: a `triggers_met:` field in decision frontmatter. Adding it is out of scope for this session" [`01b-perspective-implementer.md`, Q1].
- Outsider: "The trigger itself is not machine-addressable in the brief ... Without that, the validator would be pretending to read prose as policy" [`01d-perspective-outsider.md`, Q1].
- Skeptic: "Bash cannot reliably detect 'meets any trigger in When Multi-Agent Deliberation Is Required' — the triggers are prose, not structured flags on decision records. Implementing this as a grep over decision bodies invites false positives and false negatives; both are worse than no check" [`01c-perspective-skeptic.md`, Q1].

The convergence on *missing trigger-annotation schema* is genuine — four independent paragraphs arrive at the same concrete prerequisite. `[synth]` This is the session's clearest finding: a future session should decide whether to add a `triggers_met:` field (or equivalent) to decision frontmatter as a precondition for checks 1 and 2.

**Divergence on check 9.** The load-bearing question of the session.

- Include check 9 (Tier 1, Fail severity): **Implementer** [`01b`, Q1] and **Outsider** [`01d`, Q1].
- Defer check 9 entirely in Session 005: **Archivist** [`01a`, Q1].
- Include check 9 only as a Tier 2 question, not Tier 1; if forced to Tier 1, describe the honest-minimum form and insist its honest limits be documented inline: **Skeptic** [`01c`, Q1, Q2].

The Archivist's deferral reason is archivally interesting: "the check most designed to police cross-model honesty should not be authored in the session where cross-model participation was first operationalized" [`01a`, Meta-note]. The Skeptic's resistance is the standard adversarial critique: "Bash cannot verify honesty; a check that pretends to is worse than no check because it launders the claim" [`01c`, Q1].

The Implementer and Outsider both argue that an honestly-scoped check 9 is worth having now *because* its honest scope is narrow enough to be implementable. Implementer: "It catches the accidental-lie mode ... and the careless-copy mode. It does not catch the deliberate-lie mode" [`01b`, Q2]. Outsider: "A recorded-claim consistency check, not ... a truth detector" [`01d`, Q2].

**Divergence on check 8 severity.** The Skeptic alone argues Warning-severity, not Fail-severity: "Fail-severity would punish Session 005's own manifests if we've misjudged the schema" [`01c`, Q1]. The other three perspectives are Fail-compatible (Archivist and Implementer do not argue severity explicitly; Outsider implies Fail by treating 3/8/9 as one Tier 1 tier). `[synth]` The Skeptic's point is prudential: the first session to exercise a schema is also the session where schema-misjudgment is most likely to surface, and punishing-via-Fail creates the "silence the check by avoiding the field" failure mode.

**Coverage (raised by only one perspective).**

- Implementer: A quantitative budget for the implementation — `validate.sh` grows from ~240 to ~320 lines, not ~500; overrunning the budget is a signal of over-specification [`01b`, Meta-note].
- Skeptic: Implements *only* a check on `*synthesis*.md` files or decision records annotated multi-agent; "fewer than three files matching a raw-perspective glob is a failure" [`01c`, Q1]. The Skeptic's phrasing makes the trigger for check 3 explicit and operationalisable.
- Outsider: A sequencing rule — "Run schema well-formedness before cross-model honesty. If check 8 fails because manifests are missing, check 9 should be reported as blocked or skipped, not as a second independent failure" [`01d`, Q4]. This is architecture-level guidance about check ordering that others did not raise.

**`[synth]` Resolution direction on scope.** The emerging majority position is: **checks 3 and 8 now; check 9 now with honest scope and documented limit, under the sequencing rule the Outsider proposed**. The Skeptic's dissent on 9 is preserved as the minority position and must survive into the decision record; the Archivist's "defer 9 to a non-bootstrap session" argument is preserved as a minority position on timing. The Skeptic's Warning-vs-Fail concern for 8 is softened by the Outsider's sequencing proposal: if check 8 fails, check 9 is blocked not failed, which reduces the "silence-by-omission" pressure.

---

## Q2: Form of the cross-model-claim honesty check (#9)

**Convergence on the internal consistency framing.** Every perspective that engaged with check 9 (including the Archivist's hypothetical form and the Skeptic's grudging honest-minimum) arrives at the same framing: the check verifies *consistency of self-report*, not *truthfulness of self-report*.

- Archivist: "The check enforces *consistency of self-report*, not *truthfulness of self-report*" [`01a`, Q2].
- Implementer: "The check enforces *claim consistency*, not *claim truth*" [`01b`, Q2].
- Outsider: "A recorded-claim consistency check, not ... a truth detector" [`01d`, Q2].
- Skeptic: "The check verifies *internal consistency of a claim*, not the claim's truth" [`01c`, Q2].

`[synth]` The four phrasings are substantively identical. Because no equivalent phrase appears in the shared brief, this is not lexical echo; it is genuine cross-model convergence on the honest framing. This is the kind of signal the methodology hoped heterogeneous participation would produce.

**Convergence on the failure condition.** Three perspectives (Archivist hypothetical, Implementer, Outsider) specify near-identical failure conditions: synthesis declares `cross_model: true` AND every participant manifest has `training_lineage_overlap_with_claude: known-overlap` AND no manifest has `participant_kind: human`. The Skeptic's honest-minimum form matches. `[synth]` No material divergence on the failure logic.

**Divergence on placement (Tier 1 vs Tier 2).** The Skeptic is the only perspective arguing for Tier 2 primary placement: "make this a Tier 2 question phrased adversarially. ... A question the operator must answer in prose is harder to launder than a field a script reads" [`01c`, Q2]. The other three place it as Tier 1.

**Divergence on inclusion in Session 005.** Archivist defers; others include.

**Convergence on the documentation requirement.** Three perspectives (Archivist, Implementer, Skeptic) explicitly demand the check's honest-limit language be documented **inline alongside the check**, not in a footnote or separate spec. The Archivist offers specific verbatim language: "This check verifies the session's claim is internally consistent with its manifests. It does not and cannot verify that the manifests' lineage claims are themselves true" [`01a`, Q2]. The Skeptic: "That limit must be documented **inside the check's failure message and in the spec section describing the check**, not in a footnote" [`01c`, Q2]. The Implementer: "A one-paragraph comment above the check in `validate.sh` plus a line in the v2 spec's Validation section is enough" [`01b`, Q2]. `[synth]` This is strong triangulation: an implementation decision that omits the honest-limit documentation-inline would violate three independent perspectives' explicit demand.

**Gaming modes surfaced.**

- Implementer: "A dishonest operator can flip any manifest's `training_lineage_overlap_with_claude` from `known-overlap` to `independent-claim` and the check passes" [`01b`, Q2].
- Skeptic: "Trivial. I write `training_lineage_overlap_with_claude: independent-claim` in the manifest of a Claude subagent I invoked via the Task tool. The check passes" [`01c`, Q2].
- Outsider: "`unknown` laundering: a dishonest operator can label one participant `training_lineage_overlap_with_claude: unknown` and pass the check while still making a false cross-model claim. Another gaming mode is a paper human: adding a nominal human reviewer who did not substantively participate" [`01d`, Q2].

**Coverage.** The Outsider's "paper human" gaming mode is distinctive — not raised by any other perspective. It names a vector that the schema's `participant_kind: human` pass-through cannot itself detect: a human whose participation is nominal shortcut-passes the check.

**`[synth]` Resolution direction on check 9 form.** Adopt a Tier 1 check 9 with the convergent failure condition and the convergent internal-consistency framing. Document honest-limit language inline in `validate.sh` and in the relevant spec's Validation section, per the triangulated demand. Preserve the Skeptic's minority position (Tier 2 primary) and the paper-human gaming mode (Outsider-unique) in the decision record.

---

## Q3: Schema changes required

**Convergence: no new required fields for checks 3 and 8.** All four perspectives agree the D-024 schema is sufficient for checks 3 and 8 as written [`01a`, Q3; `01b`, Q3; `01c`, Q3; `01d`, Q3].

**Near-convergence on nice-to-haves.** Multiple perspectives independently name the same candidates:

- **Rename `training_lineage_overlap_with_claude`.** The Implementer ("rename to `lineage_overlap_claim`") [`01b`, Q3] and the Outsider ("rename to `training_lineage_overlap_with_claude_claim` would be cleaner") [`01d`, Q3] both propose renaming, explicitly for claim-honesty-signalling. The Archivist proposes the weaker form ("document as *claims*, not measurements, in D-024 itself") [`01a`, Q3]. The Skeptic opposes renaming: "The current three-value enum is adequate. Stricter values would invite more dishonest precision" [`01c`, Q3] — though note the Skeptic is opposing *value* renaming, not *field* renaming; it is unclear whether the Skeptic's opposition extends to the field rename.
- **Clarify `unknown` is a literal string, not missing data.** Outsider: "The validator should treat `unknown` as a literal string value, not as missing data. The brief already points that way, but the rule should be explicit in the schema language" [`01d`, Q3]. The Implementer implicitly relies on this when specifying failure conditions.
- **`raw_response_sha256` integrity field.** Archivist: "Not required for any Tier 1 check in Session 005, but its absence narrows what any future integrity check can do" [`01a`, Q3]. Implementer: "Do not add ... in this session. They are genuine Open Extensions and belong to a later decision" [`01b`, Q3]. Skeptic: "Adding them now ... builds verification infrastructure for a problem we've seen once" [`01c`, Q3]. All defer.

**Coverage.** The Outsider uniquely identifies that the **session-level participants index → manifest path mapping** may not be machine-readable yet: "The session-level participants index must have a defined, machine-readable way to enumerate participant manifest paths. If D-024 already defines that elsewhere, no new per-participant field is required. If it does not, that definition is required now" [`01d`, Q3]. The Archivist independently raises the adjacent concern: `participants_family`'s location (synthesis frontmatter vs `participants.yaml`) is ambiguous in the brief and needs to be pinned [`01a`, Q3].

**`[synth]` Resolution direction on schema.** No required field additions this session. One small clarification may be required for check 8 to run cleanly: the session-level `participants.yaml` should have an explicit `participants:` list naming each participant's manifest path (the Implementer's third nice-to-have and the Outsider's required prerequisite). This is minor — Session 004's `participants.yaml` already has this structure informally — and can be resolved by convention this session without a schema revision.

---

## Q4: Failure surface and backward compatibility

**Convergence on failure-surface format.** All four perspectives say: preserve the existing `FAIL:`/`WARN:`/`PASS:` format, one line per failure with path and reason, exit 1 on any Tier 1 failure. No new severity levels [`01a`, Q4; `01b`, Q4; `01c`, Q4; `01d`, Q4].

**Divergence on the retroactivity gating mechanism. This is the deliberation's sharpest cross-model disagreement.**

- **Presence-gating (majority, all three Claude perspectives):** check 8 and check 9 apply to any session directory containing `participants.yaml` (or a manifest file); sessions without such artefacts are skipped silently. Archivist: "an explicit exemption list in the check itself, not ... a date or session-number threshold" [`01a`, Q4]. Implementer: "the rule is 'if you claim schema, you meet schema.' Date- or number-based gates invite the 'we just missed the cutoff' excuse" [`01b`, Q4]. Skeptic: "a presence heuristic auto-migrates: any session with the artefact is checked, any without is not" [`01c`, Q4].
- **Session-number-gating (Outsider, alone):** "These checks should apply going forward from Session 005, keyed by session number, not by date and not by 'manifest-presence heuristic.' The methodology is session-based, and the brief explicitly says Session 004 had a bootstrap exemption while Session 005 does not. That makes `session >= 005` the right boundary" [`01d`, Q4].

`[synth]` **This is the deliberation's first genuine cross-model divergence.** Three Claude perspectives converge on presence-gating; the non-Claude perspective takes a distinct position. The Outsider's argument is not weaker — it ties the gating to the explicit rule-establishment event (Session 005 = first non-exempt, per D-023's bootstrap exemption language), which is more legible to a future reader than a file-presence heuristic. The Claude-majority argument is that presence-gating is auto-migrating and avoids maintenance churn; the Outsider's counter is that it invites the "omit the file to silence the check" failure mode, which session-number gating makes impossible.

This is exactly the kind of disagreement OI-004 exists to surface. Whether the Claude majority is correct because it is correct, or correct because three samples of the same training distribution found the same convenient answer, is a question this synthesis cannot settle. The decision step should explicitly engage this, not average it.

**Further divergence on Session 004 treatment.**

- Archivist: explicit exemption for Session 004 via inline comment in `validate.sh` pointing to D-027 [`01a`, Q4].
- Implementer: Session 004 "will be evaluated. If it fails, that is information — Session 004 was the bootstrap exemption for non-Claude participation but not for schema well-formedness, and we should see the result" [`01b`, Q4].
- Skeptic: "Session 004's minimal `participants.yaml` is the test case. ... Log the warnings; do not break the build" (under Warning-severity for check 8) [`01c`, Q4].
- Outsider: "I would not retroactively fail Sessions 001–004" [`01d`, Q4] — but implicitly via session-number gating rather than exemption list.

`[synth]` The Archivist and Outsider align on *not failing Session 004 retroactively*; the Implementer and Skeptic align on *evaluating it with the check's honest severity (Fail for Implementer, Warning for Skeptic)*. The distinction is whether Session 004's partial schema adoption should be a source of signal or protected as provenance. `[synth]` The protectability argument is stronger: Session 004 was explicitly the bootstrap-exemption session, and a Tier 1 failure on its minimal `participants.yaml` would read as the methodology contradicting its own D-023 bootstrap exemption.

**`[synth]` Resolution direction on Q4.** Adopt the majority presence-gating but honor the Outsider's concern by making the gating convention explicit in the spec's Validation section (not only in the bash script). Session 004's `participants.yaml` is a known-minimal artefact of the bootstrap exemption; rather than either failing it or silencing it, the check logic treats presence-gating at manifest-directory level (`manifests/`) — Session 004 has no `manifests/` directory, so it passes the schema well-formedness check by being out of scope, which aligns with its bootstrap exemption without requiring an inline exception list. The Outsider's concern about "omit the file to silence the check" becomes a Tier 2 guided-assessment question to the operator, which is the legitimate defense against intentional omission.

---

## Q5: OI-010 closure and OI-004 state

**Convergence on OI-010: close.** All four perspectives agree OI-010 closes on this session's evidence.

- Archivist: "Close now. ... The closure record should cite this deliberation's Outsider delivery via `codex exec` and name the manifest that documents it" [`01a`, Q5].
- Implementer: "Close it on this session's evidence" [`01b`, Q5].
- Outsider: "OI-010 should close on Session 005, but only once Session 005 is fully recorded" [`01d`, Q5].
- Skeptic: "Close. The issue asked for the first operational use; the first operational use is happening. ... Lowering the bar retroactively would be bad-faith goalpost-moving" [`01c`, Q5].

`[synth]` Strong four-way convergence. The Skeptic's phrasing is the most useful for the decision record because it pre-empts a revisionist objection: closing on single-data-point evidence is the explicit trigger D-027 set, and re-negotiating it now would be dishonest.

**Near-convergence on OI-004: narrow, do not close. Skeptic dissents softly.**

- Archivist: "Narrow, do not close. ... `narrowed-pending-sustained-practice` — the name itself tells a future reader what's still outstanding without requiring them to read the closure criteria" [`01a`, Q5].
- Implementer: "Narrowed-pending-sustained-practice. One session does not satisfy closure criterion 2 ... criterion 3 ... or criterion 4" [`01b`, Q5].
- Outsider: "My recommendation is `narrowed-pending-sustained-practice`" [`01d`, Q5].
- Skeptic: "Do not narrow beyond 'narrowed-pending-sustained-practice'. And I'd rather not even that — my preference is **unchanged**. ... I concede 'narrowed-pending-sustained-practice' as a tolerable compromise *only* if the narrowing note itself reads 'one session of practice; three more required; no evidence of impact yet' — i.e., the narrowing is itself a tally, not an endorsement. If the other perspectives want to narrow with warmer language, I dissent" [`01c`, Q5].

`[synth]` The OI-004 resolution is `narrowed-pending-sustained-practice` by 3-of-4 convergence, with the Skeptic's minority preference (`unchanged`) preserved and the Skeptic's conditional compromise (tally not endorsement) adopted as the *phrasing constraint* on the narrowing note. The decision record must state the narrowing as a tally — "one session of practice; three more required; no evidence of impact yet" — not as progress warmth.

**Convergence on the closure-criteria status.** All four perspectives independently enumerate which of the four OI-004 closure criteria are partially/plausibly met vs. unmet:

- Criterion 1 (participant independence): plausibly met by the Outsider's manifest if `training_lineage_overlap_with_claude: independent-claim` is recorded truthfully. All four flag this as conditional on the manifest.
- Criterion 2 (sustained practice ≥3 sessions): unmet; this is session 1 of 3.
- Criterion 3 (recorded impact): cannot be evaluated yet — synthesis has not been decided-upon yet; the impact of the Outsider's positions will be testable against the decisions.
- Criterion 4 (articulation of "substantively different training provenance"): unmet; not on this session's docket.

`[synth]` The methodology gains clarity here: the decision record should list all four criteria explicitly in the OI-004 status update, with their current state. This is a specific archival pattern the Archivist names: "enumerate the remaining closure criteria with their current status" [`01a`, Q5].

---

## Q6: Open Extensions to promote, or keep deferred

**Convergence: keep all Open Extensions deferred.** Three of four perspectives (Archivist, Outsider, Skeptic) explicitly promote nothing. The Implementer proposes one promotion: "`cross_model` honesty as a validation rule. We are implementing check 9; the rule it enforces should sit in the spec's Validation section as normative, not in Open Extensions. This is already half-done — the v2 spec lists check 9 as an automation candidate. Finish the move" [`01b`, Q6].

`[synth]` The Implementer's promotion is tautological if check 9 is implemented: implementing the check makes the rule normative in practice. It is not a separate Open Extension being promoted; it is the natural consequence of shipping the check. The other three are not *opposing* normativity-of-check-9; they are declining to promote any additional Open Extension. With this clarification, convergence is nearly total: no *additional* Open Extensions are promoted beyond the one already implicit in choosing to ship check 9.

**Convergence on deferral reasons.** Multiple perspectives link deferred extensions to future contingencies:

- Integrity hashing and convener attestation: deferred until a concrete failure mode surfaces (Archivist, Implementer, Skeptic).
- Cross-lineage-influence ratio: deferred until closure of OI-004 becomes actionable (Archivist, Implementer, Skeptic, Outsider).
- Structural cross-check for OI-004-narrowing honesty: deferred but *closer to the surface* because this session is the first to narrow OI-004 (Archivist explicitly; Implementer and Skeptic name the dependency on trigger-schema).

**Coverage.** The Archivist uniquely proposes linking deferred extensions to their future triggers *in the spec's Open Extensions section itself*: "Record this link in the Open Extensions entry so a future session knows why it matters" [`01a`, Q6]. This is a concrete archival pattern: an Open Extension entry records not only the idea but the concrete event or precondition that would make it worth revisiting.

**`[synth]` Resolution direction on Q6.** No net promotions. Adopt the Archivist's pattern of annotating Open Extensions with their activation preconditions, as a minor edit to `multi-agent-deliberation.md` v2's Open Extensions section.

---

## Points of Disagreement (preserved)

These are the positions not absorbed into consensus. Each is load-bearing and must survive into the decision record:

1. **Check 9 inclusion and form.** The Archivist defers it to a non-bootstrap session; the Skeptic demands Tier 2 placement primary, Tier 1 only grudgingly with explicit honest-limit documentation; the Implementer and Outsider include it as Tier 1 with honest-scope framing. The deliberation must choose; the dissenters' reasons should be cited in the decision's rejected-alternatives.

2. **Check 8 severity.** Skeptic alone argues Warning not Fail, on the prudential argument that first-exercise-of-schema is where schema-misjudgment surfaces and Fail creates silence-the-check pressure [`01c`, Q1].

3. **Retroactivity gating mechanism.** Three Claude perspectives → presence-gating. Outsider → session-number gating (`session >= 005`). This is the deliberation's first genuine cross-model divergence; it must not be averaged out in the decision.

4. **OI-004 narrowing phrasing.** Three of four adopt `narrowed-pending-sustained-practice` as the status. The Skeptic accepts this only as *compromise*, preferring `unchanged`, and conditions the compromise on the narrowing note reading as tally not endorsement. The decision must honor the phrasing constraint.

5. **Renaming `training_lineage_overlap_with_claude`.** Implementer and Outsider propose, Archivist weak-supports, Skeptic opposes. Not pursued in this session but worth recording as a live schema-evolution question.

---

## Limitations

This section is required content for multi-agent deliberation records (v2 spec's Limitations requirement):

- **Three of the four perspectives share the Claude Opus 4.7 model family.** The Outsider's distinct-lineage participation does not remove the Claude-majority in this deliberation; convergence that includes the Outsider is stronger evidence than convergence that does not. The synthesis has flagged cases where the Outsider converged with the three Claude perspectives (strong signal) and cases where it diverged (the retroactivity-gating question).
- **The Outsider was invoked via a CLI wrapper (`codex exec`), not a direct API.** Transport fidelity depends on convener integrity. The raw output is committed verbatim including banner and prompt echo; no automated integrity check verifies this.
- **Brief-writing had no adversary.** The shared brief was written by the synthesizer-orchestrator (a Claude Opus 4.7 agent). The phrases "security theatre" and "gaming mode" appear in the brief itself (in the Skeptic's stance section and the problem-statement sentence about check 9) — so their adoption by multiple perspectives is partially lexical echo, not independent coinage. Convergence on the *framing* (consistency-not-truthfulness) is genuine — the brief did not pre-announce that phrasing. This synthesis has tried to distinguish the two throughout.
- **The synthesis step is a single-agent re-entry point** (Claude Opus 4.7, matching three of four deliberators' model family). The synthesizer has not played any perspective, per D-018. This limitation is preserved from v2 spec's Limitations section and applies here identically.
- **The Outsider's single presence narrows OI-004 less than its presence suggests.** The v2 spec's Closure Criteria section is explicit: sustained practice requires ≥3 required-trigger deliberations. This session is session 1 of 3.
- **The Outsider was selected by the session operator (Claude Code orchestrating agent), not independently.** `participant_selection_method: self` or `pre-registered` is the most honest classification. This is a weaker form of independence than an externally-solicited participant would be.

## Structural honesty notes

- Every claim attributing a position to a perspective in this synthesis cites the source file (`01a-perspective-archivist.md`, etc.) and where relevant the question section.
- `[synth]` marks synthesizer-original claims (direction-setting moves, convergence identifications, resolution proposals not found verbatim in any raw output).
- Dissent is preserved in the "Points of Disagreement" section at its strongest form.
- Majority/minority structure is reported explicitly where the four perspectives diverged.
- Quote over paraphrase was applied for all load-bearing attributions.
