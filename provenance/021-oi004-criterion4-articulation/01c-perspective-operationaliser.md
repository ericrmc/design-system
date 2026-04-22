---
session: 021
title: Perspective — Operationaliser (Q1-Q8 + Honest-limits)
date: 2026-04-22
status: complete
perspective: operationaliser
committed_at: 2026-04-22
---

# Operationaliser Perspective — OI-004 Criterion-4 Articulation

I am the Operationaliser. My charge per [brief §8.3] is testability: an articulated criterion that cannot be machine-verified or systematically audited is decorative. My contribution to the synthesis is concrete schema deltas and `validate.sh` check pseudocode, not abstract endorsement of one articulation shape over another. Where the articulation surface unavoidably reaches into human judgement, I name that boundary explicitly rather than disguising it.

The Session 005/006 Archivist's "machine-verifiability is the audit guarantee" inheritance binds me to a particular discipline: the spec must not require subjective judgement *at audit time*. Subjective judgement at *articulation time* is unavoidable and proper; the test is whether someone reading provenance years later can mechanically distinguish a criterion-satisfying record from a criterion-violating one without having to re-litigate the substance.

My method below: I work bottom-up from "what would `validate.sh` need to parse?" to "what manifest fields would carry that signal?" to "what articulation text in the spec would license those fields?" This is the inverse of the Articulator's drafting direction and the synthesis should benefit from the cross-check.

---

## Q1 — Definition surface

I propose criterion-4's "substantively different training provenance" be defined as a **conjunction of three machine-verifiable manifest predicates plus one human-judgement empirical predicate**. The conjunction shape is load-bearing: any single predicate alone is gameable; the four together raise the floor without requiring any single predicate to bear the full weight.

The four predicates:

**P1 (organisational origin, machine-verifiable):** the participant's `provider` manifest field is a value in a closed set distinct from `anthropic`. The closed set is enumerated by the spec and updated by named decisions, so audit can mechanically check membership.

**P2 (Claude-distillation disclosure, manifest-self-report):** the participant's manifest carries a new field `claude_output_in_training: known-yes | known-no | unknown` with required-rationale-when-unknown. This is self-reported (and therefore subject to the same operator-integrity caveat as `training_lineage_overlap_with_claude` per check 13's honest limit), but the field's *presence* is machine-verifiable, and `unknown` is itself a signal (per the §Heterogeneous-Participant Recording Schema "Unknown-field rule").

**P3 (selection-process auditability, machine-verifiable):** the participant's `participant_selection_method` is in a closed set distinct from `self`. The current schema already enumerates `self | solicited-from-graph | solicited-externally | pre-registered`; criterion-4 articulation closes the set against `self` for OI-004-narrowing purposes and may further constrain (e.g., excluding `solicited-from-graph` for human participants per §3.2 Limitations note).

**P4 (operational corroboration, human-judgement-irreducible):** at the OI-004 *closure* moment, a session has filed a one-shot retrospective artefact (specified shape below in Q4) tallying criterion-3 data points and asserting that at least one cross-lineage divergence-from-Claude-consensus is recorded in committed synthesis files. This is the irreducibility I address head-on in Q4.

The *test* for whether two participants have substantively different training provenance: at deliberation time, P1+P2+P3 must hold for the non-Claude participant. At closure time, P4 must additionally hold for the cumulative record.

I am explicit: this is a **definitional-with-empirical-floor** shape. It is *not* the [brief §5.1] permissive draft (which requires only P1 and a partial P2), *not* the [brief §5.2] strict draft (which adds public-corpus and behavioural-distinction predicates I argue are not machine-verifiable in practice — see Q4), and *not* the [brief §5.3] pure-empirical draft (which has no upstream manifest predicate and therefore no per-deliberation gate). It is closest to a hybrid of §5.1 and §5.3, with the strictness of §5.2's *intent* but the testability of structural manifest fields rather than pretraining-corpus inspection.

**From my pretraining, I recall** the N-version programming literature distinguishes "design diversity" (independent design teams) from "version diversity" (different implementations from the same team) and that the former is empirically much harder to verify. The methodology should not pretend it can verify pretraining-corpus distinctness through manifest text; it should verify the *operational signature* of design diversity (P4) and accept self-report on the rest with `unknown`-as-signal.

---

## Q2 — Enumeration surface

Working from [brief §4.4] candidates A–G:

**Acceptable alone (count toward OI-004 narrowing without requiring combination):**

- **A. Non-Anthropic LLM via own provider's endpoint.** The dominant pattern Sessions 005–020. Manifest predicates P1, P2, P3 verifiable; P4 accumulates over sessions. *No new schema needed beyond what Q4 proposes.*
- **C. Open-source LLM, locally hosted.** Same predicate verifiability as A. The `provider: local` value is already in the schema.
- **D. Human reviewer recruited externally.** Predicate P3 verifiable via `participant_selection_method: solicited-externally`; P1 maps to `provider: human`; P2 is `claude_output_in_training: n/a` for humans (a new allowed value).

**Acceptable only with disclosed weakening (count, but with mandatory annotation):**

- **B. Non-Anthropic LLM via aggregator API (e.g., OpenRouter).** Same predicates as A, but with a new required manifest field `aggregator_intermediary: <string or n/a>` so the aggregator becomes a named third party in the audit chain. Without this annotation, the audit cannot tell whether B-shape participation is being silently used.
- **E. Human reviewer from operator's social graph.** Per [brief §3.2] the v3 Limitations note already flags this as weaker. Articulation should permit but require `participant_selection_method: solicited-from-graph` and a `selection_proximity_to_operator: <free-text>` annotation. Audit can mechanically detect *that* this category is being used; the *quality* of the selection-proximity rationale is Tier 2.
- **G. Mechanical cross-family invocation outside perspective-deliberation frame.** The Session 018 pattern. This is currently un-theorised by v3; Q4 proposes adding it as a distinct manifest layer (`mechanical_cross_family_invocation:` block in the session-level participants index).

**Acceptable only in combination:**

- **F. Panel of multiple non-Claude participants.** Articulation should not *require* a panel for criterion-4, but the panel configuration should be a recordable signal (a new synthesis-frontmatter field `non_claude_panel: true | false`) for future analyses (e.g., the cross-lineage-influence ratio computed over panels vs single non-Claude participants).

**Excluded:**

- An "Anthropic-other" participant (e.g., an Anthropic-trained but non-Claude-branded model) is **not acceptable** for OI-004 narrowing. The current schema permits `participant_kind: anthropic-other` precisely to record this category honestly; criterion-4 articulation should make explicit that this category does *not* count for OI-004 narrowing. (This is the affirmative complement to the existing Claude-Only-Is-Not-Cross-Model rule.)

**Draft spec text for the enumeration (Q2 contribution to the eventual amendment):**

```markdown
### Acceptable Participant Kinds for OI-004 Narrowing

For purposes of OI-004 narrowing/closure, the following participant categories
are **acceptable** when their per-participant manifest satisfies P1, P2, P3 of
the criterion-4 definition:

- Non-Anthropic LLM accessed via its provider's endpoint (`provider` ∈
  {openai, google, meta, xai, mistral, ...}, closed set updated by named
  decision; `participant_kind: non-anthropic-model`).
- Open-source LLM locally hosted (`provider: local`,
  `participant_kind: non-anthropic-model`, with `model_family` and `model_id`
  identifying the upstream weights).
- Human reviewer recruited externally (`participant_kind: human`,
  `participant_selection_method: solicited-externally`).

The following are **acceptable with mandatory disclosure annotation**:

- Non-Anthropic LLM via aggregator API (requires manifest field
  `aggregator_intermediary:` naming the aggregator).
- Human reviewer from the operator's social graph (requires
  `participant_selection_method: solicited-from-graph` plus
  `selection_proximity_to_operator:` annotation).
- Mechanical cross-family invocation outside the perspective-deliberation
  frame (Session 018 precedent; recorded via the
  `mechanical_cross_family_invocation:` block in the session-level participants
  index per the schema below).

The following are **excluded**:

- Any participant with `participant_kind: claude-subagent` or
  `participant_kind: anthropic-other`. The Claude-Only-Is-Not-Cross-Model rule
  applies to anthropic-other equivalently; intra-Anthropic mixing does not
  satisfy OI-004 even with model-branding distinctions.
```

---

## Q3 — Sufficiency surface

From the testability angle: **adopting the Q1 articulation is *not by itself* sufficient to close OI-004.** The articulation makes the criterion machine-verifiable, but criteria 1–3 were already satisfied per [brief §2]. What's missing for closure-eligibility is the **operational corroboration retrospective artefact (P4)**: a one-time committed file that mechanically tallies the existing record against the now-articulated criteria.

Closure requires *both*: (a) articulation adopted (this session's amendment), and (b) the retrospective artefact filed in this session or a successor, mechanically demonstrating that criteria 1–4 hold for the cumulative Sessions 005–020 record under the articulated definition.

Why the retrospective artefact is required: without it, the closure decision rests on an assertion that "criteria 1–3 are satisfied per accumulated record" — a claim that is *currently* in OI-004's record as prose but is *not* mechanically auditable. The articulation creates the schema fields and predicates; the retrospective applies them to the existing record. Skipping the retrospective is the laundering route Q8 will name.

This pushes me toward **Q6 sub-option (b)** "keep open with named blockers" — see Q6 below.

**Draft spec text for the retrospective requirement (added to Closure Criteria):**

```markdown
### Closure Procedure for OI-004

In addition to satisfying criteria 1–4, OI-004 closure requires a one-time
retrospective artefact at `provenance/<NNN-closure-session>/oi-004-retrospective.md`
containing:

- A table of all qualifying deliberations (one row per deliberation) with
  columns: session number, decision id(s), participant kinds, P1/P2/P3
  predicate satisfaction (boolean per row), criterion-3 data points
  contributed, frame-replacement-or-novel-mechanism flag (boolean).
- A summary tally: total qualifying deliberations, total non-Claude
  participants, total criterion-3 data points, total frame-replacement-or-
  novel-mechanism instances.
- An explicit assertion of P4 satisfaction: at least one cross-lineage
  divergence-from-Claude-consensus is cited with `[provenance/<NNN>/<file>, §X]`
  citation.
- A `validate.sh` check 16 (defined below) confirms the table's structural
  well-formedness; the substantive judgement of "frame-replacement-or-novel-
  mechanism" remains a Tier 2 concern (the "cannot reach" surface this
  perspective acknowledges).
```

---

## Q4 — Testability surface (PRIMARY CONTRIBUTION)

This is my distinguishing contribution. I propose four schema additions and two new `validate.sh` checks.

### Schema addition 1: Tighten `training_lineage_overlap_with_claude`

The current field admits three values (`known-overlap | unknown | independent-claim`). The value `independent-claim` is currently a bare assertion with no evidentiary anchor. Tighten as follows.

**Revised field (replaces existing):**

```yaml
training_lineage_overlap_with_claude: known-overlap | unknown | independent-claim
training_lineage_evidence_pointer: <provenance-relative path or URL or "n/a">
```

Where `training_lineage_evidence_pointer` is **required** when the overlap value is `independent-claim`, and is `"n/a"` otherwise. The pointer must resolve to one of:

- A model card or training-data card published by the provider (URL).
- A provider-public statement on Claude-distillation policy (URL).
- A workspace-internal note explaining what evidence the operator inspected (provenance-relative path).
- The literal string `"unknown-but-asserted"` with mandatory `transport_notes` explanation — this is the laundering-honesty escape hatch (analogous to `unknown-as-signal`).

**`validate.sh` check 16 (new):** for each manifest with `training_lineage_overlap_with_claude: independent-claim`, verify `training_lineage_evidence_pointer:` is present and non-empty. Pseudocode:

```bash
# [16] Independent-claim evidence-pointer presence
echo "[16] Independent-claim evidence pointer"
for dir in "${provdirs[@]}"; do
  manifests_dir="${dir}manifests"
  [[ -d "$manifests_dir" ]] || continue
  for mf in "$manifests_dir"/*.manifest.yaml; do
    [[ -f "$mf" ]] || continue
    if grep -qE '^training_lineage_overlap_with_claude:[[:space:]]*independent-claim' "$mf"; then
      if grep -qE '^training_lineage_evidence_pointer:[[:space:]]*\S+' "$mf"; then
        pass "$(basename "$mf") — evidence pointer present"
      else
        fail "$(basename "$mf") — independent-claim without training_lineage_evidence_pointer"
      fi
    fi
  done
done
```

Honest limit (mandatory inline-documented per the precedent of checks 13/14/15): this check verifies the *presence* of the evidence pointer, not the *truthfulness* of the evidence it points to. A pointer to a fabricated note passes. The Tier 2 question paired with check 16 is the designed counter-pressure.

### Schema addition 2: New field `claude_output_in_training`

Distinct from training-corpus overlap (which is about pretraining data), this field captures the question "was Claude's output in this model's training set?" — a question that has become operationally significant as more providers train on synthetic data including LLM outputs.

```yaml
claude_output_in_training: known-yes | known-no | unknown | n/a
```

Where `n/a` is permitted only when `participant_kind: human`.

**`validate.sh` check 17 (new):** field-presence check; out-of-scope for `participant_kind: claude-subagent | anthropic-other`. Pseudocode:

```bash
# [17] Claude-output-in-training disclosure presence
echo "[17] Claude-output-in-training disclosure"
for dir in "${provdirs[@]}"; do
  manifests_dir="${dir}manifests"
  [[ -d "$manifests_dir" ]] || continue
  for mf in "$manifests_dir"/*.manifest.yaml; do
    [[ -f "$mf" ]] || continue
    pkind=$(grep -E '^participant_kind:' "$mf" | head -1 | sed -E 's/^participant_kind:[[:space:]]*//')
    case "$pkind" in
      claude-subagent|anthropic-other) continue ;;  # out-of-scope
    esac
    if grep -qE '^claude_output_in_training:[[:space:]]*(known-yes|known-no|unknown|n/a)' "$mf"; then
      pass "$(basename "$mf") — claude_output_in_training disclosed"
    else
      fail "$(basename "$mf") — missing claude_output_in_training field"
    fi
  done
done
```

Honest limit: this check verifies disclosure-of-self-report, not truth. A `known-no` claim by a provider that secretly trained on Claude outputs passes; this is the same operator-integrity floor as check 13. The value of the check is that `unknown` (or absence) becomes mechanically visible, raising the cost of silently treating opaque-distillation participants as fully independent.

### Schema addition 3: Aggregator-intermediary disclosure

For [brief §4.4] candidate B (aggregator API access).

```yaml
aggregator_intermediary: <string or "n/a">
```

`"n/a"` for direct provider access; otherwise the aggregator name (e.g., `"openrouter"`). No new check required — the field's presence is enforced by extending the existing check 12 D-024 required-fields list (gated on `participant_kind: non-anthropic-model`).

### Schema addition 4: Mechanical cross-family invocation block

For [brief §4.4] candidate G (Session 018 pattern). Currently the v3 schema covers participants as deliberation perspectives; mechanical cross-family invocation in validation gates is unmodeled.

Proposed: a new top-level section in `provenance/NNN/participants.yaml` (or `participants.md`):

```yaml
mechanical_cross_family_invocation:
  - purpose: <free text, e.g. "C3 5-gram overlap test", "L1 contamination canary">
    invoked_model: <model id>
    provider: <provider id>
    invocation_method: <cli-wrapper | api | other>
    decision_shaped: <D-NNN id or "none">
    evidence_pointer: <provenance-relative path>
```

This makes Session 018-style mechanical invocations a first-class recorded category, distinct from deliberation participation, with a machine-parseable record. No new check needed at criterion-4 articulation time; a future check 18 could verify this block's well-formedness when it is present.

### `validate.sh` check 18 (new): closure-retrospective well-formedness

For Q3's required closure-retrospective artefact. Pseudocode:

```bash
# [18] OI-004 closure-retrospective well-formedness
echo "[18] OI-004 closure-retrospective"
shopt -s nullglob
retrospectives=("$WORKSPACE_ROOT"/provenance/*/oi-004-retrospective.md)
shopt -u nullglob
for r in "${retrospectives[@]}"; do
  # Verify required sections: Table, Summary tally, P4 assertion
  missing=""
  for section in "## Qualifying Deliberations Table" \
                 "## Summary Tally" \
                 "## P4 Assertion"; do
    if ! grep -qF "$section" "$r"; then
      missing="${missing} ${section}"
    fi
  done
  if [[ -z "$missing" ]]; then
    pass "$(basename "$(dirname "$r")")/oi-004-retrospective.md — well-formed"
  else
    fail "$(basename "$(dirname "$r")")/oi-004-retrospective.md — missing:${missing}"
  fi
done
```

### Honest acknowledgement of irreducibility

[Brief §8.3] flags my weakest argument: *some* criteria — notably "qualitatively distinct contribution" or "frame-replacement" per [brief §5.3] — are inherently human-judgement-dependent and resist machine verification. I address this directly.

**My position:** the methodology should *accept* the irreducibility for predicate P4 (operational corroboration), but contain it within an artefact (the retrospective per Q3) that a machine *can* well-formedness-check, even though the *substance* of the P4 assertion remains a human judgement at the moment of writing the retrospective.

This is the same shape as the existing Tier 1 / Tier 2 split: structural checks verify form; semantic adequacy is a Tier 2 question. Check 18 is well-formedness only; the substantive question "is the cited cross-lineage divergence genuine?" is paired Tier 2 question Q8 (new — proposed below).

**Proposed new Tier 2 question Q8 (added to validation-approach.md §Tier 2):**

> **Q8. OI-004 closure-retrospective substantive adequacy (new; paired with check 18):** If this session contains an `oi-004-retrospective.md`, read its Qualifying Deliberations Table and P4 Assertion. For each row marked frame-replacement-or-novel-mechanism, verify the cited synthesis section actually contains a non-Claude-originated reframing (not paraphrase or restatement of a Claude perspective's argument). For the P4 assertion, verify the cited divergence shows the synthesis adopted a position that contradicts the Claude consensus, not merely supplemented it. Flag rows where the substantive claim is weaker than the structural claim suggests.

This is consistent with the methodology's existing discipline: do not pretend to verify what cannot be verified mechanically, but make the unverifiable surface visible to a Tier 2 reviewer.

---

## Q5 — Self-application surface

Does the Outsider's participation in *this* deliberation satisfy the Q1 criterion-4 articulation?

Mechanically: **yes for predicates P1, P2, P3** (per the [brief §2] participant statement and the Session 020 outsider manifest pattern at `/Users/ericmccowan/Development/complex-systems-engine/provenance/020-workspace-scaling-deliberation/manifests/outsider.manifest.yaml`):

- **P1:** `provider: openai` — distinct from `anthropic`, in the closed set.
- **P2:** would require this session's outsider manifest to fill `claude_output_in_training:` (currently no schema field exists; would be `unknown` truthfully — GPT-5.4's training data is not publicly disclosed). The `unknown` value is permitted and is itself signal per the unknown-field rule.
- **P3:** `participant_selection_method: pre-registered` (continuing the Sessions 005–020 pattern of consistent codex-exec invocation; pre-registered against the Session 004 mechanism design and reaffirmed every session since).

For **P4**: the Outsider's participation in *this* deliberation does not by itself satisfy P4 — P4 is *cumulative* and requires the closure-retrospective artefact. But the cumulative record across Sessions 005–020 (per [brief §2]: 50 criterion-3 data points; per [brief §3.3]: frame-replacement instances at Sessions 011, 014, 017, 020) plausibly satisfies P4 when the retrospective is written.

Is the self-applying convenience a flag? Partially. The articulation I propose has two anti-self-serving features that the Articulator's draft might lack:

1. **The retrospective requirement (Q3) defers the closure decision** to a future session that must explicitly apply the criteria to the cumulative record. This session adopts articulation but does not unilaterally close.
2. **The P4 substantive adequacy is a Tier 2 question (Q8)**, not a Tier 1 check. The closure decision will be reviewable by future sessions or external auditors who can re-examine whether the cited frame-replacements are genuine.

But I should be honest: the articulation *does* include the participant kind that argued for it. There is no escape from this — any criterion-4 articulation produced by a deliberation that includes a non-Claude participant has this property. The mitigation is procedural (retrospective + Tier 2 review), not structural.

If the Outsider were *excluded* by the proposed articulation, that would be a clearer signal of non-self-serving design. Proposing an articulation that includes the participant arguing for it is a soft flag the synthesis should weight.

---

## Q6 — Closure decision

I argue **sub-option (b): articulate-and-keep-open-with-named-blockers**.

Specifically: Session 021 should adopt the Q1 articulation and the Q4 schema additions as a substantive `multi-agent-deliberation.md` v3 → v4 revision, *and* leave OI-004 in a new state "Articulated; awaiting closure-retrospective" with the named blocker being the retrospective artefact per Q3.

**Why not (a) close-on-adoption:** sub-option (a) would close OI-004 in the same session that articulates the criterion that allows closure. This is the laundering pattern Q8 below names — a closeable gate that the articulation itself opens. The retrospective requirement (Q3) is the structural defence.

**Why not (c) defer-articulation-entirely:** sub-option (c) preserves the 12-session "Closable pending" status that is itself a quiet form of laundering — the OI is described as nearly-closed without ever being made adversarially closeable. The Skeptic's defer-revision posture has merit on the engine-version-bump question (Q7) but does not justify perpetually deferring articulation as such.

Sub-option (b) is testably distinct from both: a future session writes the retrospective, runs check 18 mechanically, and either passes (justifying closure) or fails (justifying continued open status). The closure decision becomes auditable rather than asserted.

**Draft spec text for the new OI-004 state:**

```markdown
### Closure Criteria for OI-004 (revised)

OI-004 has four ordered states:

1. **Open.** Default until criteria 1–3 are satisfied.
2. **Closable pending criterion-4 articulation.** Criteria 1–3 satisfied;
   criterion 4 not yet articulated. (Sessions 009–020 held this state.)
3. **Articulated; awaiting closure-retrospective.** All four criteria
   articulated as machine-verifiable predicates (P1–P3 manifest-checked,
   P4 retrospective-checked). The Closure Procedure (see above) requires
   a one-time `oi-004-retrospective.md` artefact applying P1–P4 to the
   cumulative record.
4. **Closed.** The retrospective artefact is committed, check 18 passes,
   Tier 2 Q8 has been answered substantively, and a successor session
   has decided on OI-004 closure with explicit citation to the
   retrospective.

States are advanced by named decisions, not asserted by prose annotation.
A state advance from Articulated to Closed requires the closure-retrospective
artefact to exist in the deciding session's provenance and a `validate.sh`
check 18 PASS for that artefact.
```

---

## Q7 — Engine-version impact

The Q1 articulation, Q2 enumeration, Q3 closure-procedure, and Q4 schema additions are collectively a **substantive revision to `multi-agent-deliberation.md`** and would bump `engine-v1` → `engine-v2` per `engine-manifest.md` §5.

**From the testability angle specifically:** the new `validate.sh` checks 16, 17, 18 (and the extended check 12 required-fields list) **are themselves changes to a file in `engine-manifest.md` §3** (`tools/validate.sh` is engine-definition). Even setting aside the spec revision, the validator changes alone might independently warrant an engine-version bump per `engine-manifest.md` §5's criteria.

This is a precedent-setting moment. Two questions:

**(a) Is the bump warranted *now*?** Yes, on the testability ground specifically. The articulation without the schema additions is the documentation-vs-discipline gap [brief §8.3] warns me to argue against. The schema additions without articulation are mechanical without referent. Adopting them together is the only coherent path. Deferring articulation to "soft text within OI-004's record without spec amendment" creates exactly the gap the Operationaliser exists to close.

**(b) What precedent does engine-v2 set?** This is the methodology's first engine-version bump. The precedent should be: an engine-version bump is warranted when the *engine surface* (what external workspaces inherit) substantively changes, and `multi-agent-deliberation.md` v3→v4 plus three new Tier 1 checks plus one new manifest-required field plus tightening of an existing manifest field is unambiguously substantive.

**A weaker engine-bump alternative:** adopt the articulation *only* in soft form (Q1 plus Q2 prose) without the Q4 schema deltas, deferring the schema additions and `validate.sh` checks 16/17/18 to a follow-on session. This would be **engine-bump-warranted but smaller** — closer to the boundary of "substantive revision." I argue *against* this alternative because it reproduces the documentation-vs-discipline gap: the spec would say what counts but provide no machine check that the saying matches the doing. The articulation's anti-laundering teeth come from check 16+17+18 enforcement; without them the articulation is decorative.

**A stronger engine-bump alternative:** also adopt the closure-retrospective artefact-creation in this session (not just the schema for it). This is procedurally available — Session 021 could write the retrospective, run check 18, and advance OI-004 to Closed. I argue *against* this stronger alternative because it collapses Q6 sub-option (b) into (a) and creates the self-serving timing the Outsider's presence in this deliberation already strains.

So: bump engine-v1 → engine-v2 with the articulation + schema deltas + checks 16/17/18; defer the closure-retrospective and OI-004 closure decision to a future session.

---

## Q8 — Anti-laundering check

Apply the Session 014 Skeptic Q7 test to my own proposal:

**Does my articulation make it *easier* to claim OI-004 narrowing for a participant that wouldn't actually narrow it (false positive)?**

The risk surface: P1 (`provider` ∈ closed-non-Anthropic-set) is satisfied by any non-Anthropic LLM, including ones that may have been distilled from Claude or trained on Anthropic-published data. P2 (`claude_output_in_training`) catches the explicit case but admits `unknown` as a legitimate value, so a participant whose distillation history is opaque can pass. The closed-set discipline of P1 raises the floor compared to status-quo (which has no closed set at all), but does not eliminate the false-positive risk.

Mitigations I propose: (a) `unknown` is mandatory-disclosed and visible to Tier 2 review; (b) the cumulative P4 retrospective requires *operational corroboration* — a participant whose contributions are indistinguishable from Claude perspectives' (same arguments, same blind spots) will not satisfy P4 even if P1+P2+P3 mechanically pass. P4 is the load-bearing filter against false positives; P1–P3 raise the structural floor.

**Does my articulation make it *harder* to recognise legitimate OI-004 narrowing the methodology is already getting (false negative)?**

The risk: P3 excludes `participant_selection_method: self`, which would exclude a hypothetical case where the operator self-selected a non-Anthropic model for genuine reasons (e.g., domain expertise) and the participation produced legitimate criterion-3 data points. Sessions 005–020's `pre-registered` selection method is a mitigation, but a stricter criterion may exclude future legitimate variations.

Mitigation: the enumeration in Q2 explicitly admits `solicited-from-graph` with annotation, recognising that not all weakened-selection cases are illegitimate. I am not closing the door on legitimate narrowing; I am requiring it be visibly recorded.

**Does my articulation have a route by which the methodology could close OI-004 without genuinely improving the cross-model discipline?**

This is the load-bearing question. The route would be: (i) adopt articulation in Session 021; (ii) write the closure-retrospective in Session 022 by mechanically citing existing manifests; (iii) check 18 passes on well-formedness; (iv) close OI-004 without anyone substantively re-examining whether the cumulative record's "frame-replacements" are genuine.

The countermeasures embedded in my proposal:

1. **The retrospective itself must be deliberated** — it is a substantive new artefact, not a routine annotation, and writing it should arguably trigger non-Claude participation per the v3 §Non-Claude Participation Required clause 4 (asserts a change in OI-004 state) and possibly clause 2 (depends on whether the retrospective is a substantive revision to `multi-agent-deliberation.md`'s closure section).
2. **Tier 2 Q8 (new) is paired with check 18** explicitly to surface the substantive-vs-structural gap. A closure-retrospective that mechanically passes check 18 but cannot survive Q8 substantive review should not justify OI-004 closure.
3. **The retrospective requires citation** of cross-lineage divergence-from-Claude-consensus. This is checkable: a reviewer can read the cited synthesis section and verify whether the cited divergence is genuine. Vague citations or self-confirming citations should fail Q8.

But I should name the residual laundering risk honestly: **a future session that wants to close OI-004 has every procedural opportunity to do so with my proposal.** The procedural defences (deliberated retrospective, Tier 2 Q8) require operator integrity at exactly the same surface as check 13's honest limit. I have not solved that surface; I have raised the visibility cost.

**Falsifier threshold:** *If I argued for the four-predicate definitional-with-empirical-floor articulation plus checks 16/17/18, the threshold to move me off would be:*

- Demonstration that the closed-set `provider` enumeration in P1 creates a maintenance burden that produces silent failures (e.g., a legitimate new provider is rejected because the closed set was not updated, causing operators to route through misclassification rather than update the set).
- Demonstration that `claude_output_in_training: unknown` becomes the dominant value in practice, hollowing out P2's signal.
- Demonstration that the closure-retrospective check 18 either (i) is too easy to pass (mechanical citations of weak frame-replacements), or (ii) is too hard to pass (legitimate cumulative records cannot be retrospectively documented to the standard).
- Articulator or Outsider proposing a fourth-shape articulation that has equivalent or better testability without the cumulative-retrospective requirement.

Two of these falsifiers are operational (would emerge from running the checks for 5+ sessions); two are deliberative (would emerge from this synthesis or a successor). I should be moveable on operational evidence; I should be cautious about being moved by deliberative argument that does not engage the testability surface specifically.

---

## Honest-limits

Things I know but did not address:

1. **The `validate.sh` checks 16/17/18 pseudocode I drafted is bash-3.2-compatible by intent but I have not actually executed it.** A real implementation session would discover edge cases (manifest files with windows line endings, multi-document YAML, fields with surprising whitespace). My pseudocode is design-level, not implementation-validated.

2. **The closed-set `provider` enumeration creates a versioning question I did not resolve.** When a new provider needs to be added (e.g., a future Cohere or DeepSeek participant), is that a `multi-agent-deliberation.md` revision triggering an engine-bump, or a non-substantive validator-data-update? My instinct is "non-substantive validator-data-update with a named decision and a session-log entry," but I did not propose specific text.

3. **I did not engage [brief §4.2] external-methodology survey items** (N-version programming, Cohen's kappa, cross-validation, citizen-assembly diversity). I gestured at N-version in Q1 with the required pretraining disclosure. The other three are arguably more relevant to the Articulator's draft text than to the testability surface; a fuller engagement would have proposed specific borrowings (e.g., is there a kappa-style inter-model-agreement metric that could be computed from the criterion-3 record?). I mention this as a known gap.

4. **I did not address [brief §4.5] recursive question depth.** The Outsider in this deliberation is reasoning about its own qualifying status. My P4-via-cumulative-record proposal puts the qualifying-status decision at the closure-retrospective artefact, not at this deliberation, which I think is the right answer. But I did not explore whether the recursive structure has any pathology that the retrospective doesn't catch (e.g., a future closure-retrospective written by a session that *also* includes a non-Claude participant with the same self-applying property).

5. **My Q7 engine-version analysis treated `tools/validate.sh` as engine-definition without recomputing whether the precedent from `engine-manifest.md` §5 is unambiguous on what counts as a substantive revision to the validator.** I asserted the engine-bump is warranted; a stricter reading might treat new check additions as "extension within the existing validator surface" rather than substantive revision. I think the bump is correct, but I am noting the asserted-vs-derived gap.

6. **I did not propose a manifest field for the Session 018 mechanical-cross-family invocation case beyond the `mechanical_cross_family_invocation:` block in Q4.** A fuller treatment would specify whether mechanical invocations contribute to criterion-3 data point counts at the same weight as deliberation-perspective invocations. I lean toward "yes with mandatory annotation" but did not draft the rule.

### Anti-laundering check applied to my own proposal (per [brief §7 Q8] requirement)

Already covered in Q8 above. To restate the residual risk: the procedural defences I propose (retrospective requires deliberation, Tier 2 Q8 paired with check 18, citation requirement) do not eliminate the operator-integrity floor. A future session whose orchestrator wants to close OI-004 can write a retrospective that mechanically passes check 18 with citations that survive a perfunctory Tier 2 Q8 answer. The proposal raises the visibility cost of laundering; it does not make laundering structurally impossible. This is the same floor as check 13's honest limit, and I am content with the parallel — but synthesis should not characterise my proposal as solving the laundering problem. It moves the laundering surface from "asserted prose in OI-004's record" to "deliberated retrospective with mechanical well-formedness check + paired Tier 2 question." Both surfaces remain.

The strongest version of my proposal would add a **second-pass external review requirement**: the closure-retrospective must be reviewed by a non-Claude participant in a deliberation distinct from the one that wrote it. I did not include this because (a) it stacks deferral on top of deferral and may make closure operationally impossible; (b) the Skeptic perspective in this deliberation is positioned to argue this stronger version if the synthesis finds it warranted. I mention it as a known contingent extension.
