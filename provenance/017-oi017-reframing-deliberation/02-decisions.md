---
session: 017
title: Decisions — OI-017 Resolved via H4 (Layered Model); Engine Manifest Created; PROMPT.md Split
date: 2026-04-22
status: complete
---

# Decisions — Session 017

**Notice.** Per D-037/D-038/D-039 (adopted Session 006), every decision in a post-adoption session (≥006) carries `**Triggers met:**` and `**Triggers rationale:**` inline. Session 017 is a post-adoption session; decisions below follow the schema.

Session 017 contains **two decisions**: D-074 (H4 adoption + authorised revisions) and D-075 (OI state housekeeping).

---

## D-074: Adopt H4 layered model (methodology → engine → application); create `engine-manifest.md`; split `PROMPT.md`; revise `identity.md`, `workspace-structure.md`, and `methodology-kernel.md`

**Triggers met:** [d016_1, d016_2, d016_3, d023_1]

**Triggers rationale:** `d016_1` fires — D-074 modifies `methodology-kernel.md` (one-sentence scope clarification in §Purpose; file stays v4 by content decision but per D-016_1 wording any modification fires the trigger). `d016_2` fires — D-074 creates new `engine-manifest.md` v1 and substantively revises `identity.md` v1 → v2 (layered-denotation content is new normative material, not elaboration of existing text) and `workspace-structure.md` v2 → v3 (three file-class distinction is new normative content). `d016_3` fires — the deliberation surfaced a genuine 2-2 cross-perspective split on PROMPT.md-split (Architect+Outsider for; Operationalist+Skeptic against); reasonable practitioners genuinely disagreed. `d023_1` fires — kernel modification per D-016_1. Multi-agent cross-model deliberation with non-Claude participation (Outsider = OpenAI GPT-5.4 via `codex exec`) satisfies the d023_1 requirement. Full D-024 manifests committed for all four participants. Four raw perspective files committed before synthesis (`01a-perspective-architect.md`, `01b-perspective-operationalist.md`, `01c-perspective-skeptic.md`, `01d-perspective-outsider.md`) satisfy the three-raw-output floor (check 11) with margin. Deliberation-anchor commit: `f3e003b`.

**Decision:** Adopt H4 layered model per Outsider's fourth-hypothesis proposal [01d Q1], honoured by synthesis [`01-deliberation.md` §6]. Concretely:

1. **Denotation layering.** Selvedge names the methodology (abstract-approach sense). "Selvedge engine" denotes the current executable implementation defined by `engine-manifest.md`. "Application of the Selvedge engine" denotes any specific run (self-development or external-problem). Three layers, explicit.

2. **`methodology-kernel.md` v4 unchanged by filename; one-sentence scope clarification added to §Purpose.** Filename stays `methodology-kernel.md`; v4 stays v4; the scope clarification sentence reads (per Outsider [01d Q2]): *"This specification defines the Selvedge methodology kernel: the abstract execution semantics that a conforming engine must realise. `engine-manifest.md` enumerates the files that constitute the current engine."* The scope clarification is a **modification** (triggering d016_1 and d023_1) but is **minor-not-substantive** under the OI-002 heuristic (elaboration that makes existing kernel-vs-engine semantics explicit without adding new normative rules). No v-bump; no `-v4.md` preservation.

3. **`identity.md` v1 → v2 (substantive).** Adds Outsider's denotation language; preserves original name-origin content, three-properties metaphor, and all four Reopening conditions verbatim. v1 preserved as `identity-v1.md`. New v2 adds §"Layered denotation" or similar near top of §Specification with the language: *"Selvedge names the methodology. 'Selvedge engine' denotes the current executable implementation defined by `engine-manifest.md`. Each session is an application of that engine — either the self-development application (what this workspace has been; what `prompts/development.md` drives) or an external-problem application (what `prompts/application.md` drives)."*

4. **`workspace-structure.md` v2 → v3 (substantive).** Adds §File classes section distinguishing:
   - **Engine-definition files** (the loadable Selvedge engine): `PROMPT.md`, `prompts/development.md`, `prompts/application.md`, `specifications/*.md` (all six current + new engine-manifest), `tools/validate.sh`.
   - **Development-provenance files** (the workspace's own development history; not part of the engine): `SESSION-LOG.md`, `open-issues.md`, `provenance/`.
   - **Application-scope files** (per-application; mutable per `applications/` rules): `applications/NNN-*/`.
   - Normative rule: an external application workspace may load the engine-definition set without inheriting development-provenance; the self-development application (this workspace) has both.
   v2 preserved as `workspace-structure-v2.md`.

5. **New: `specifications/engine-manifest.md` v1.** Narrow single-purpose specification per OI-002 Session 012/Session 014 precedent. Five content blocks per Outsider [01d Q4] and cross-model convergence:
   - **§1 Purpose** — names the engine as the current loadable implementation of the Selvedge methodology.
   - **§2 Current engine version** — `engine-v1` initial; versioning discipline (§5).
   - **§3 Engine-definition file set** — enumerated per §4 above.
   - **§4 Exclusion list** — SESSION-LOG, open-issues, provenance, existing applications, this manifest's own version history.
   - **§5 Versioning discipline** — engine version increments on substantive change to any enumerated file; typo/minor fixes do not increment.
   - **§6 Loading the engine / minimal external-application initialisation contract** — per Outsider [01d Q6]: copy engine-definition set; fresh SESSION-LOG, open-issues, provenance; `applications/001-<slug>/brief.md` carrying problem, constraints, stakeholders, success condition.

6. **`PROMPT.md` restructured as thin dispatcher** per Outsider's pattern [01d Q3]. Original `PROMPT.md` content split into:
   - `PROMPT.md` (short): defines the three layers, names the two operating modes (self-development and external-application), points to the two mode-specific prompts.
   - `prompts/development.md` (current workspace's entry point): contains the existing `PROMPT.md` executable content, framed as the self-development application. Substantive framing changes: remove "This workspace is building a design methodology" opening; replace with "This is the self-development application of the Selvedge engine; each session evolves the engine's own specifications by running the engine on its own outputs."
   - `prompts/application.md` (template for external applications): loads the engine by reference (engine-manifest reference); names the slots an external application fills (problem, constraints, stakeholders, success condition); declares that development-provenance is NOT part of the application's context unless explicitly imported.

   **PROMPT.md is a significant event per `workspace-structure.md` §PROMPT.md**; the change is recorded in this decision. Session 017's provenance records the split; no v-bump on PROMPT.md itself (PROMPT.md does not use the spec-versioning discipline).

7. **`multi-agent-deliberation.md` v3 — minor edit (no v-bump).** Add one-sentence scope clarification near top stating the rules apply to both self-development and external-application runs. Minor per OI-002 heuristic (elaboration within the mechanism-neutrality language of v3 §Mechanism; no new rules, required fields, or triggers added).

8. **`validation-approach.md` v3 — minor edit (no v-bump).** Add one-sentence scope clarification stating the Tier 1 checks and Tier 2 questions apply to both self-development and external-application runs. Minor per OI-002 heuristic.

9. **`reference-validation.md` v1 unchanged.** Per Outsider [01d Q2]: no concrete inconsistency with H4 requires revision.

**Why:** The four-perspective deliberation produced a cross-model-weighted synthesis recommendation [`01-deliberation.md` §6] that threads between H2 and H3 via Outsider's novel H4 layered model. Three-of-four perspectives converge against Architect's H2-specific rename of `methodology-kernel.md` and against Architect's Selvedge-names-engine reading. Two-of-four perspectives (cross-model: Architect+Outsider) support the PROMPT.md split, which is the cross-model-weighted majority per `multi-agent-deliberation.md` v3 §Limitations (shared-family convergence is weak evidence). Three-of-four perspectives support `engine-manifest.md` creation with high convergence on content. The synthesis therefore adopts the Outsider-originated layered model as the substantive shape, honouring operator-preference direction (reframe, not H1) while refining the specific shape away from the under-supported H2-rename detail.

No operator-preference-priming drift detected (3-of-4 perspectives diverged from operator-stated H2 preference; Architect matched as assigned-role). Brief-priming-absent streak extends to eight consecutive sessions (Sessions 010–017).

Preserves three first-class minorities per `01-deliberation.md` §4: Skeptic's H1 no-reframing warrant (Reopening condition 1); Operationalist's H3 cosmetic-reframing warrant (merge-back if prompts duplicate); Architect's H2 kernel-rename warrant (stronger-restructure direction if layered distinction collapses in practice).

### Rejected alternatives (preserved)

- **Rejected: H1 (no reframing).** Skeptic's sole advocacy [01c all Q]. Preserved as first-class minority with operational warrant: if three consecutive Sessions 018+ revise H4's adopted shape without external-adoption evidence, Skeptic's position becomes the preferred revision direction toward H1.
- **Rejected: H2 (full reframing as specified in Session 016 §4).** Architect's sole advocacy [01a]. Cross-model 3-of-4 rejection of two H2-specific details: kernel rename and Selvedge-names-engine reading. H2 elements adopted in H4 form: PROMPT.md split, engine-manifest creation, workspace-structure file-class distinction, layered denotation. Full-H2 preserved as warrant for stronger-restructure direction.
- **Rejected: H3 (partial reframing as specified in Session 016 §4).** Operationalist's sole advocacy [01b]. Cross-model 3-of-4 rejection of H3-specific detail: no PROMPT.md split (Architect+Outsider cross-model argue split is necessary to address load-boundary ambiguity). H3 elements adopted in H4 form: engine-manifest creation, identity.md light revision, no kernel rename. H3 preserved as warrant with merge-back condition.
- **Rejected: renaming `methodology-kernel.md` to `engine-kernel.md`.** Architect's proposal [01a Q2]. 3-of-4 cross-model against (Operationalist, Skeptic, Outsider).
- **Rejected: "Selvedge names the engine" (identity.md scope change).** Architect's proposal [01a Q5]. 3-of-4 cross-model against.
- **Rejected: branched single-file PROMPT.md.** Architect [01a Q3] and Outsider [01d Q3] both argue against in favour of split; Outsider is explicit: "A branched monolith is exactly where silent import happens."
- **Rejected: deferring PROMPT.md split until first external application.** Operationalist [01b Q3] and Skeptic [01c Q3] arguments. Cross-model-weighted against per §2.3 reasoning; preserved as minority with merge-back operational condition.
- **Rejected: halt-for-user-ratification before executing PROMPT.md split.** The Session 017 assessment proposed this as default if deliberation departed materially from H2 [§3.7]. The deliberation adopted H4, which departs in shape but not in direction from H2 (reframe direction preserved; H2-rename detail rejected). Operator's Session 016 framing ("for the engine to determine"; "no stake in specific shape") explicitly authorises this departure. If the user objects to any H4 detail, a subsequent session can revise per the preserved first-class minorities.

### What remains open

- **OI-017 state change.** Recorded in D-075 below.
- **First external application of the Selvedge engine.** Not executed this session; enabled by H4's infrastructure. The `applications/001-<slug>/brief.md` pattern is specified in `engine-manifest.md` §6; the `prompts/application.md` template is drafted; an external-application-opening session in future can load them.
- **First-exercise of reference-validation** (carried forward from D-072). H4 does not block Cell 1 execution; the Case Steward role is engine-level per `reference-validation.md` and runs unchanged under H4.
- **Session 011 OI-015 laundering-enforcement gap.** H4's prompt split introduces explicit development-vs-application framing; Session 018+ can examine whether this naturally addresses OI-015's concern (explicit context boundaries reduce laundering surface).

### Pre-commitment

- H4's adopted shape carries the three first-class minorities forward as preserved warrants. Any future session seeking to abandon part of H4 should cite the specific warrant that activates and the specific observable condition that has materialised.
- PROMPT.md revision is a "significant event" per `workspace-structure.md`; this decision records it.

---

## D-075: OI state housekeeping — OI-017 resolved; OI-004 tally advances 5 → 6 of 3; OI-007 count 13 → 12; OI-002 new data point

**Triggers met:** [d023_4, d016_3]

**Triggers rationale:** `d023_4` fires — D-075 asserts an OI-004 state change (tally advance from 5-of-3 to 6-of-3 per sixth required-trigger deliberation with non-Claude participation). Non-Claude participation (Outsider) is present in the deliberation; full D-024 manifest committed; d023_4 requirement satisfied. `d016_3` fires — the underlying reframing question had 2-2 and 3-1 perspective splits on multiple sub-questions; reasonable practitioners genuinely disagreed. Multi-agent deliberation supports this decision (the same deliberation that supported D-074).

**Decision:**

1. **OI-017 resolved** — "Resolved — H4 layered model adopted via D-074; specifications revised per D-074 detail 2–8." The operator's Session 016 reframing observation is acted on via H4; the three hypotheses H1/H2/H3 originally framed have been superseded by H4 per cross-model synthesis. Three first-class minorities preserved operationally within `01-deliberation.md` §4 with specific Reopening conditions.

2. **OI-004 tally advances 5-of-3 → 6-of-3.** Session 017 is the sixth required-trigger deliberation with non-Claude participation (after Sessions 005, 006, 009, 011, 014). D-074 fires d023_1 (kernel modification); D-075 fires d023_4 (OI-004 state change). Non-Claude Outsider (OpenAI GPT-5.4 via `codex exec`, session id `019db36d-14a0-7d10-863e-179677eef35b`, reasoning effort xhigh, 19,120 tokens) participated with full D-024 manifest. Tally extends further beyond satisfied threshold. Closure criteria: (1) participant independence — satisfied (Outsider carries `training_lineage_overlap_with_claude: independent-claim`); (2) sustained practice ≥3 required-trigger deliberations — satisfied (now 6 of 3); (3) recorded impact on outcomes — satisfied (cumulative **45** concrete Outsider-sourced contributions across Sessions 005–017, up from 40 through Session 014; five new contributions this session per `01-deliberation.md` §3); (4) articulated definition of "substantively different training provenance" — **still unmet**. Closable pending criterion-4 articulation.

   Voluntary-to-required ratio: previously 5:5 after Session 014 (Session 015 single-perspective, no non-Claude; Session 016 single-perspective, no non-Claude); now **5:6 after Session 017** (first session where required count exceeds voluntary count). Watchable pattern: the methodology's cross-model discipline is concentrated in required-trigger contexts at slightly higher rate than voluntary; informative for any future criterion-2-robustness review.

3. **OI-007 count 13 → 12.** OI-017 opened in Session 016 (count 12 → 13); now resolved (count 13 → 12). Count returns to post-Session-014 level.

4. **OI-002 new data point.** Session 017 executed substantive revisions to `identity.md` v1 → v2 and `workspace-structure.md` v2 → v3 (both substantive per OI-002 heuristic: new normative content beyond existing scope). Session 017 also created `engine-manifest.md` v1 as a new single-purpose specification — **third creation** of a narrow single-purpose spec after Session 012's `identity.md` and Session 014's `reference-validation.md`. Per prior heuristic-development observation, narrow-single-purpose-spec creation is now n=3; formalising creation as a third category (distinct from substantive revision and minor revision) is increasingly warranted. No formal OI-002 heuristic update this session; monitor.

   Session 017 also executed **minor edits** to `multi-agent-deliberation.md` v3, `validation-approach.md` v3, and `methodology-kernel.md` v4 (scope clarification sentences; no v-bumps). All three are minor per OI-002 heuristic (elaboration within existing language; no new rules, required fields, triggers, severity decisions, gating rules, or required artefacts). Eighth OI-002 data point on the substantive-vs-minor distinction heuristic.

5. **OI-005, OI-006, OI-008, OI-009, OI-011, OI-012, OI-013, OI-014, OI-015, OI-016 unchanged.**

   - OI-016 (reference-validation mechanism, provisional) remains Resolved — provisionally addressed pending first-exercise. H4 adoption does not change reference-validation's design; the Case Steward / Produce / Validation three-cell structure is engine-level and runs unchanged.
   - OI-015 (laundering enforcement gap) — H4's explicit prompt split plausibly reduces laundering surface (clean context-boundary between development and application); any Session 018+ observation of laundering pattern under H4 is new evidence about whether the gap narrowed.

**Why:** D-075 records the OI consequences of D-074's adoption. OI-017 was opened Session 016 specifically to host this deliberation; the deliberation concluded; the OI resolves. OI-004 advances as required by the session's D-023-triggering decisions. OI-007 decrements. OI-002 accumulates its eighth data point.

### Rejected alternatives (preserved)

- **Rejected: leaving OI-017 open as "Partially resolved via H4."** H4 addresses both operator-observed structural consequences (engine separability; distinct execution prompts); the three hypotheses originally framed are superseded by the adopted H4 shape. Partial-resolution framing would be accurate but confusing; preserved first-class minorities within `01-deliberation.md` carry any unresolved reasoning forward.
- **Rejected: declining to advance OI-004 tally on the grounds that Outsider proposed a novel hypothesis (H4) rather than advocating one of H1/H2/H3.** The tally advance is tied to required-trigger deliberation with non-Claude participation, not to which hypothesis the Outsider advocates. Outsider's H4 contribution is the strongest cross-model signal of the session; treating it as disqualifying would invert the incentive structure.

### OI state after this decision

- **Open issues: 12 active** (OI-002, OI-004, OI-005, OI-006, OI-007, OI-008, OI-009, OI-011, OI-012, OI-013, OI-014, OI-015). OI-017 resolved.
- **Resolved: 5** (OI-001, OI-003, OI-010, OI-016, OI-017).
- **OI-004 status:** Closable pending criterion-4 articulation (tally 6-of-3; voluntary:required 5:6).
