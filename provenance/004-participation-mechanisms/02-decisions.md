---
session: 004
title: Decisions — Non-Claude Participation Mechanism
date: 2026-04-18
status: complete
---

# Decisions — Session 004: Non-Claude Participation Mechanism

## D-021: Adopt a two-shape non-Claude participation mechanism

**Decision:** The methodology adopts a non-Claude participation mechanism with two legitimate shapes, either or both of which may appear in a given deliberation:

1. **Non-Claude participant as perspective** — a human or non-Anthropic model joins alongside the Claude perspectives. A brief is committed before launch (per D-017); the non-Claude participant receives it through whatever channel is available (text editor, web UI paste, email); the returned response is committed verbatim as a raw-output file. Where the non-Claude participant is a human and cannot respond synchronously, the session writes a `provenance/NNN/STATUS.md` file naming the awaited participant and halts; synthesis does not proceed until the awaited response is committed.

2. **Non-Claude participant as reviewer** — a named non-Claude participant (typically a human) reads the committed Claude raw outputs and writes a `provenance/NNN/human-review.md` file recording what they flagged and whether their input caused the synthesizer to change any decision. The reviewer is not a deliberator (they see the Claude outputs); they are a named auditor at synthesis-time.

Both shapes must declare participant identity in the manifest (see D-024), including `participant_kind` and `participant_selection_method`. A session may use either, both, or neither (subject to the trigger rules in D-023).

**Rationale:** The Archivist's brief-drop pattern ([`01a-perspective-archivist.md`, Q1]) and the Integrator's halt-before-synthesis ([`01b-perspective-integrator.md`, Q1]) are structurally compatible and together describe the *participant-as-perspective* shape. The Skeptic's human-reviewer-with-veto ([`01c-perspective-skeptic.md`, Q1]) is a distinct and defensible role — an auditor who reads the Claude outputs, not a voice arguing a stance. The deliberation preserved these as genuine alternatives rather than reconciled them; the specification recognises both. Both shapes share the critical property that the **record** is the guarantee (committed brief, verbatim response, attributable participant), not the **generation** (which depends on channels the workspace cannot automate).

**Rejected alternatives:**
- A non-Anthropic model via API wrapper — rejected as currently unimplementable; the workspace has no configured non-Anthropic API keys and adding them is a distinct infrastructure step with its own scope. The specification does not forbid this path; it simply does not rely on it.
- `TeamCreate`-based cross-model infrastructure — rejected for consistency with Session 003's deferral. Session 005+ may revisit.
- Synthesis-time human review without the human-as-perspective option — rejected because forcing all non-Claude participation into the synthesis layer (Skeptic's strict reading) loses the option to have a non-Claude voice shape the raw reasoning, which is where the deeper narrowing of OI-004 would actually happen.
- Participant-as-perspective without the halt enforcement — rejected because without halt, the deliberation can proceed without the non-Claude participant and the mechanism silently collapses to Claude-only.

**What remains open:**
- Operational details of channel-specific transport (email, web UI paste, etc.) — to be standardised as the mechanism accumulates use.
- Whether a session may simultaneously use participant-as-perspective and reviewer-as-auditor for the same deliberation — permitted by the spec; no guidance yet on when this double treatment is appropriate.

---

## D-022: Claude-only deliberations are not cross-model for OI-004 purposes

**Decision:** A deliberation whose participants are all members of the Claude model family — any mix of Opus, Sonnet, and Haiku, any combination of sizes, any combination of post-training runs — **does not constitute cross-model participation** for the purpose of OI-004. Such a deliberation's manifest must record `participants_family: claude-only` and `cross_model: false`.

A deliberation that wishes to claim cross-model participation must include at least one participant whose training provenance is not downstream of the Claude family (a non-Anthropic model or a human reviewer).

**Rationale:** The three perspectives were in explicit triple-convergence on this point. Quoting the Skeptic [`01c-perspective-skeptic.md`, Q2]: "Training-distribution theatre. Not narrowing. Not closure. Not even on the OI-004 scale." Quoting the Archivist [`01a`, Q2]: "training-distribution theatre for the purpose of OI-004 ... not closure, not narrowing." Quoting the Integrator [`01b`, Q2]: "Training-distribution theatre, with a small caveat. ... neither closure nor narrowing." The Limitations section of `multi-agent-deliberation.md` already states that shared training produces shared blind spots; this decision extends that principle into a structural manifest rule, preventing future sessions from (inadvertently or otherwise) recording intra-family size-mixing as OI-004 progress.

**Rejected alternatives:**
- Treating Opus+Sonnet+Haiku as cross-model — rejected per triple-convergence. Also rejected on the Skeptic's specific ground that it is "worse than running three Opus instances, because it creates the visual appearance of diversity ... while providing none of its substance" [`01c`, Q2].
- Permitting size-mixing to count as partial cross-model progress — rejected because partial-credit framing would create provenance dishonesty.

**What remains open:**
- Whether intra-family size-mixing has its own utility (all three perspectives conceded it does — capability stratification, cost-scaled deliberation, validation-band variance). **OI-011 is opened** to track this as a distinct concern (see D-027).

---

## D-023: Trigger rule for non-Claude participation

**Decision:** Non-Claude participation is **required** for any deliberation that produces a decision in one of the following categories:

1. Modifies `methodology-kernel.md`.
2. Creates or substantively revises `specifications/multi-agent-deliberation.md`.
3. Creates or substantively revises `specifications/validation-approach.md` in ways that touch semantic (Tier 2) validation.
4. Asserts a change in the state of OI-004.

Non-Claude participation is **recommended** for other D-016 triggers (new specifications; decisions with two plausible positions; load-bearing tag).

Non-Claude participation is **optional** for all other decisions.

**Opt-out.** A session may make a required-trigger decision without a non-Claude participant, but must record in the decision:

- `non_claude_participation: skipped`
- A reason. Acceptable reasons: "no non-Claude participant available within session timebox", "mechanism designer exempt" (the first-use bootstrap exemption, see below), "subject matter does not plausibly expose Claude-family blind spots" (must be argued in the decision record, not asserted).
- `retry_in_session: NNN` — the next session (or the session identifier under which the participation will be added).

Unstated skips on required-trigger decisions are a specification violation.

**Bootstrap exemption.** This session itself (Session 004, designing the mechanism) makes decisions that trigger the new rule (D-021 and this decision D-023 both substantively revise `multi-agent-deliberation.md`). The session is exempt because the rule it is establishing did not exist before this session; retroactive application is impossible. The Integrator's framing is adopted [`01b-perspective-integrator.md`, Q3]: "This session is an edge case — it is designing the escape hatch, so it is permitted to run entirely Claude-internal, but the *next* deliberation about the escape hatch must include one non-Claude voice." Future sessions revising this mechanism do not share the bootstrap exemption.

**Rationale:** The Archivist's and Skeptic's required-triggers were nearly identical [`01a`, Q3; `01c`, Q3]; the Integrator's narrower set [`01b`, Q3] is a subset. The adopted scope takes the Archivist/Skeptic scope (covers meta-deliberations about the methodology's self-assessment mechanisms) while adopting the Integrator's opt-out concession for operational fragility, with the Skeptic's `retry_in_session` enforcement making the opt-out accountable. The synthesis noted [`01-deliberation.md`, Q3]: "these resolve if we adopt Skeptic's retry_in_session field together with Integrator's opt-out mechanism."

**Rejected alternatives:**
- Universal requirement for all D-016 triggers — rejected because it would silently collapse to never-done when humans are unavailable, or produce rubber-stamp participation (Integrator's operational warning).
- Purely optional / judgment-only — rejected per Skeptic [`01c`, Q3]: "'recommended' will silently collapse to 'never done,' and the methodology will accumulate decisions about its own monoculture limit made entirely within the monoculture."
- Integrator-narrow required zone (only the mechanism itself) — rejected because it excludes kernel changes and validation-approach-semantic changes, both of which are exactly the self-assessment cases that warrant non-Claude input.
- Hard halt with no opt-out — rejected as operationally fragile; the recorded-reason + retry_in_session opt-out preserves the forcing function without blocking progress indefinitely.

**What remains open:**
- Whether "subject matter does not plausibly expose Claude-family blind spots" is a legitimate opt-out reason or a loophole to be removed in a future revision. Accepted for v2 with the Skeptic's requirement that it be argued, not asserted.
- Handling of the halt across Claude Code sessions when a session spans wall-clock time — the Integrator's STATUS.md file and the idea of `tools/check-human-slot.sh` are specified informally; a tooling session can formalise this.
- The 14-day timeout for halted sessions (Integrator's Q6 proposal) is not mandated by this decision; the spec says the halt is in place until the awaited response is committed or the session is formally closed with a recorded opt-out. Timeout policy may be added later.

---

## D-024: Heterogeneous-participant recording schema

**Decision:** Adopt a three-layer recording schema:

1. **Raw-output file frontmatter** — minimal: `session`, `title`, `date`, `status`, `perspective`, plus (in line with Archivist's boundary) `committed_at`. The response body is the payload. [Archivist's rule: `01a-perspective-archivist.md`, Q4.]

2. **Per-participant manifest** — one YAML file per participant at `provenance/NNN/manifests/<perspective>.manifest.yaml`, with the following normative fields:

   ```yaml
   perspective: <role name>
   participant_kind: claude-subagent | anthropic-other | non-anthropic-model | human | unknown
   participant_identity: <free text, canonicalized>
   model_family: <string or "unknown">
   model_id: <string or "n/a" for human or "unknown">
   model_version: <string or "unknown">
   provider: <anthropic | openai | google | local | human | unknown>
   endpoint: <string or "web-ui" | "in-person" | "unknown">
   invocation_method: <agent-tool | cli-wrapper | copy-paste | written-by-hand | unknown>
   sampling:
     temperature: <value or "unknown">
     top_p: <value or "unknown">
     max_tokens: <value or "unknown">
   training_lineage_overlap_with_claude: known-overlap | unknown | independent-claim
   participant_selected_by: <operator identity>
   participant_selection_method: self | solicited-from-graph | solicited-externally | pre-registered
   identity_known: true | false | partial
   context_source: <path to brief, or "verbal" for humans>
   delivered_at: <ISO-8601 or "unknown">
   received_at: <ISO-8601 or "unknown">
   raw_response_file: <path>
   transport_notes: <free text>
   output_edited_after_submission: true | false
   ```

3. **Session-level index** — `provenance/NNN/participants.yaml` or `provenance/NNN/participants.md` (YAML preferred for parseability; `.md` acceptable for small sessions) listing every participant perspective and pointing to their manifest.

**Unknown-field rule.** Unknown values are recorded as the literal string `unknown`. Empty strings are forbidden. Missing fields are a schema violation. `identity_known: partial` requires a `transport_notes` entry explaining what is and is not recorded.

**Composition field.** The session's synthesis file frontmatter records:

```yaml
participants_family: claude-only | mixed-anthropic | cross-model
cross_model: true | false
non_claude_participants: <integer, 0 if none>
```

`participants_family: mixed-anthropic` is permitted for intra-Claude-family size-mixing (addresses D-022 and OI-011). `cross_model: true` requires at least one participant with `training_lineage_overlap_with_claude` other than `known-overlap`.

**Rationale:** The Archivist proposed the three-layer separation [`01a`, Q4]; the Skeptic contributed the two most important dishonesty-auditing fields (`participant_selection_method`, `training_lineage_overlap_with_claude`) [`01c`, Q4]; the Integrator contributed the tri-valued `identity_known` [`01b`, Q4]. The synthesis noted the convergence on the unknown-field rule [`01-deliberation.md`, Q4] — all three perspectives require the literal `unknown` rather than omission.

The Skeptic's further demand [`01c`, Q4] — that `tools/validate.sh` should fail a session claiming OI-004 narrowing in a decision record while recording all-Claude provenance — is accepted in principle. Implementation is deferred to a future tooling session because `validate.sh` would need to parse decision-record text for OI-004-movement claims, which is beyond a bash-script structural check. This is noted in the specification's Open Extensions.

**Rejected alternatives:**
- Integrator's flatter schema (participants in session frontmatter only) — rejected because it conflates methodology-layer and archival-layer metadata, violating the Archivist's boundary argument.
- Skeptic's all-fields-in-raw-output-frontmatter — rejected because it would bloat raw-output frontmatter past the point where the file is cleanly "the payload" (though the specific fields are adopted into the manifest).
- Permitting empty strings or missing fields — rejected; `unknown` is signal, not noise.

**What remains open:**
- SHA-256 integrity hash (`raw_response_sha256`) and append-only raw files (Archivist's Q4/Q6) — accepted in principle, deferred to future tooling. The schema above does not include `raw_response_sha256` as a required field; a future revision may add it once `validate.sh` enforces it.
- Convener attestation field (Archivist's Q6) — deferred on the same grounds.
- The `participant_selected_by` identity granularity (git identity, real name, pseudonym?) — left to convener discretion with audit accountability.

---

## D-025: This session does not narrow OI-004 operationally; OI-010 narrows to "mechanism specified, awaiting first use"

**Decision:** The session records the following status changes:

- **OI-004** — remains open, with its full prior scope. This session does not narrow OI-004 operationally.
- **OI-010** — narrows substantially. OI-010 asked "what is the lightest path to incorporating a non-Claude participant"; the answer is now specified in `multi-agent-deliberation.md` v2. The issue is not closed because no non-Claude participant has actually been incorporated yet. OI-010's status becomes: "Mechanism specified; awaiting first operational use."

The session does **not** claim OI-004 narrowing, despite the specification work completed. The decision record explicitly honors the Skeptic's position [`01c`, Q5]: "Writing a spec that says 'future sessions should do X' does not narrow OI-004; it commits to maybe narrowing it later."

**Rationale:** The deliberation's sharpest preserved disagreement was whether this session narrows OI-004. Integrator said yes unconditionally (the specification narrows) [`01b`, Q5]; Archivist said yes conditionally on execution [`01a`, Q5]; Skeptic said no — only operational inclusion of a non-Claude participant narrows OI-004 [`01c`, Q5]. Session 004's three perspectives were all Claude Opus 4.7 (see `01-deliberation.md` header); no non-Claude participant joined the deliberation. The Archivist's condition is therefore unmet for this session's own work.

Adopting the Skeptic's position for OI-004 is the most honest record: the specification is meaningful progress, but crediting it as OI-004 narrowing would let the methodology write its way to resolution without ever doing the work. The Integrator's legitimate point — that the specification is concrete progress — is honored by narrowing OI-010 substantially, not by claiming OI-004 has moved.

**Future closure.** Closure of OI-004 requires (per convergence across all three perspectives in [`01-deliberation.md`, Q5]): (a) sustained non-Claude participation across a run of sessions, not a single instance; (b) evidence that non-Claude input changed decisions at least sometimes; (c) a separate decision defining what "substantively different training provenance" means. The Skeptic's concrete metric — the *cross-lineage-influence ratio* [`01c`, Q5] — is the most operational candidate for (b) and is listed as an Open Extension in the revised specification, not mandated at this stage.

**Rejected alternatives:**
- Integrator's unconditional narrowing — rejected because adopting it would over-credit the specification and set a precedent where spec-writing substitutes for practice. The Skeptic's minority position is specifically designed against this failure mode and is preserved.
- Archivist's conditional narrowing (applied as "narrows once used") — subsumed into the adopted decision: OI-010 narrows now (mechanism is specified); OI-004 will narrow on first operational use.
- Claiming partial narrowing on OI-004 — rejected as provenance dishonesty (D-022's spirit applied to the narrowing claim itself).

**What remains open:**
- Whether to formalise the cross-lineage-influence ratio as a validation metric (deferred to Open Extensions).
- When and how to revisit OI-004 — suggested review trigger (from Integrator's proposal [`01b`, Q5]): after three sessions where a required-trigger deliberation has successfully included non-Claude participation.

---

## D-026: Revision to `multi-agent-deliberation.md` is substantive, not minor

**Decision:** The revisions to `specifications/multi-agent-deliberation.md` produced by this session constitute a **substantive revision** under D-004. Accordingly:

- The existing `multi-agent-deliberation.md` (v1) is renamed to `multi-agent-deliberation-v1.md` and its frontmatter `status` is updated to `superseded`.
- A new `multi-agent-deliberation.md` (v2) takes the canonical filename, with `supersedes: multi-agent-deliberation-v1.md` in its frontmatter and `version: 2`.

**Rationale:** This is the third data point for OI-002 (threshold between minor correction and substantive revision). The earlier two data points (D-014 and D-020) both found minor-correction status because the changes made explicit what the specification's existing language already admitted or anticipated — a cross-reference pointer, an anticipated directory addition.

This session's changes are different in kind. Session 004 adds:

- A new **When Non-Claude Participation Is Required** subsection (new normative content, not previously present).
- A new **Non-Claude Participation Mechanism** subsection specifying two shapes (perspective and reviewer), a halt-before-synthesis enforcement, and explicit bootstrap exemption (new normative content).
- A new **Heterogeneous-Participant Recording Schema** subsection with required manifest fields and unknown-field rules (new normative content).
- Revisions to **Limitations** extending honest-acknowledgment language to the new mechanism's trust boundaries.
- Revisions to **Open Extensions** adding cross-lineage-influence ratio, integrity hashing, and convener attestation as future directions.

These are not elaborations of existing language — they add rules, required fields, and triggers that the v1 specification does not contain or anticipate structurally. Per D-004, this is substantive.

**OI-002 heuristic refinement.** The emerging three-point heuristic:

- If the change makes explicit what the specification's existing language **already contains or explicitly anticipates as a category of extension** → minor correction (D-014, D-020).
- If the change adds **new normative content** (new rules, new required fields, new triggers, new required artefacts) beyond what the existing language contains or specifies → substantive revision (D-026).

**Rejected alternatives:**
- Treating these additions as a minor correction because the v1 Limitations section anticipates "changes of mechanism, not of pattern" — rejected because the v1 language anticipates the *category* of extension but does not contain its *content*. Adopting this reading would trivialise the minor/substantive distinction; under it, any extension anticipated by generic framing would be minor, which empties the distinction.
- Issuing the changes as a new, separate specification (e.g., `non-claude-participation.md`) alongside v1 — rejected because the changes amend `multi-agent-deliberation.md`'s trigger rules, limitations, and schema; separating them would require bidirectional cross-references and fragment the mechanism specification across two files for no gain.

**What remains open:**
- None specific to this decision. The heuristic may be further refined by future data points.

---

## D-027: Open issues and continuing issues

**Decision:**

- **OI-004** — Open (unchanged scope). This session does not narrow OI-004 operationally (per D-025).
- **OI-010** — Open, scope narrowed to "mechanism specified (see `multi-agent-deliberation.md` v2); awaiting first operational use to begin narrowing OI-004." On first use of the mechanism in a required-trigger deliberation, OI-010 may be closed.
- **OI-009** — Open (unchanged). Session 004's audit of Session 003 found no drift-to-ritual signal. This session applied multi-agent to a decision meeting multiple D-016 triggers; the pattern is being used appropriately so far. Continue monitoring.
- **OI-002** — Open (third data point added via D-026). Heuristic refined; see D-026.
- **OI-011** (new) — "Intra-family model mixing as a deliberation-quality lever, distinct from cross-model independence." Per D-022, Opus/Sonnet/Haiku mixing does not touch OI-004, but all three perspectives noted residual utility (capability stratification, cost-scaled deliberation). The separate concern is tracked so it does not get conflated with OI-004 progress in future sessions. Opened per Archivist's proposal [`01a-perspective-archivist.md`, Q2].

**Rationale:** Keeps OI-004 honest (per D-025), records OI-010's structural progress without overreaching, and creates a distinct tracking line for the intra-family mixing question the triple-convergence raised.

**Rejected alternatives:**
- Closing OI-010 on specification alone — rejected; specification without operational use is the same failure mode the Skeptic named for OI-004.
- Closing OI-009 as "no drift observed in Session 004" — rejected; drift-to-ritual is a trend concern requiring multi-session observation, not a single-session audit.
- Opening a separate OI for cross-lineage-influence ratio or integrity hashing — rejected; these are future extensions of the revised specification, tracked in its Open Extensions section rather than as standalone open issues. Open issues are for active uncertainties; Open Extensions are for named future directions within a specific specification.

**What remains open:** The specific threshold for closing OI-010 (first use, successful first use, third use?) is left to the session that performs the first use.
