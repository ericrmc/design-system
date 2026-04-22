---
session: 017
title: Synthesis — OI-017 Deliberation (H1 / H2 / H3 / H4 with Cross-Model Outsider-Originated Fourth Hypothesis)
date: 2026-04-22
status: complete
participants_family: cross-model
cross_model: true
non_claude_participants: 1
synthesizer: Claude Opus 4.7 (orchestrating agent; not one of the four deliberation perspectives)
---

# Synthesis — Session 017 OI-017 Deliberation

Synthesizer identity: Claude Opus 4.7 (1M context), acting as the orchestrating agent for Session 017. The synthesizer is not one of the deliberation's four perspectives (Architect, Operationalist, Skeptic, Outsider) — the kernel's synthesizer-distinctness rule (`multi-agent-deliberation.md` v3 §Synthesis) is honoured.

Deliberation-anchor commit: `f3e003b` (brief committed before perspective launch).

## 1. Summary of perspective positions

| Q | Architect (H2) | Operationalist (H3) | Skeptic (H1 adv.) | Outsider (H4 novel) |
|---|---|---|---|---|
| Q1 reframe? | Full, now | Partial, now | No | Layered, now |
| Q2 files to change | 5 specs + new manifest + rename kernel | 3 files (manifest + identity.md v2 + PROMPT.md para) | 0 files | 4 scope-bearing files (PROMPT.md, kernel, workspace-structure, identity) + light edits on 2 others + new manifest |
| Q3 PROMPT.md | Split into 3 files; original replaced | No split; add paragraph | No change | Split: thin dispatcher + `prompts/development.md` + `prompts/application.md` |
| Q4 new spec? | Yes — `engine-manifest.md` | Yes — `engine-manifest.md` | No | Yes — `engine-manifest.md` (minimal) |
| Q5 identity.md | Selvedge names **the engine** | Selvedge names both; manifest names engine | No change | **Selvedge names the methodology; "Selvedge engine" denotes the implementation** |
| Q6 external path | Copy template, fill slots, execute | Clone, read manifest, read `PROMPT.md`, adapt | Designed when first needed | Copy engine-definition set, fresh provenance, `applications/001-<slug>/brief.md` |
| Q7 dissent-from-self | H3-at-20%-cost is the strongest counter | Cosmetic-reframing charge is strongest | Ambiguity may itself block adoption | May be premature architecture; H3 is lighter if prompts duplicate |

Citations: [Architect, 01a, all Q]; [Operationalist, 01b, all Q]; [Skeptic, 01c, all Q]; [Outsider, 01d, all Q].

## 2. Convergence analysis

### 2.1 — On renaming `methodology-kernel.md` → `engine-kernel.md`

**3-of-4 against the rename** [Operationalist 01b Q2, Skeptic 01c Q2, Outsider 01d Q2]. Only Architect [01a Q2] advocates the rename. The against-rename position is cross-model (Operationalist + Skeptic Claude + Outsider non-Claude). Rename is **not adopted**.

Outsider's exact language [01d Q2]: *"In `specifications/methodology-kernel.md`, I would keep the filename and add an opening scope clarification. The key sentence should be something like: 'This specification defines the Selvedge methodology kernel: the abstract execution semantics that a conforming engine must realise.'"* Operationalist's convergent language [01b Q2]: *"`methodology-kernel.md` (not renamed, not revised)."* Skeptic's convergent language [01c Q2]: *"`methodology-kernel.md` v4 stays."*

### 2.2 — On creating `engine-manifest.md`

**3-of-4 for the manifest** [Architect 01a Q4, Operationalist 01b Q4, Outsider 01d Q4]. Only Skeptic [01c Q4] argues against, on grounds that *"A specification is earned by having something downstream of it."*

Cross-model convergence (Architect + Operationalist + Outsider) includes one Claude H2 advocate, one Claude H3 advocate, and one non-Claude H4 advocate — the convergence spans the three reframing-favouring positions. Skeptic's H1-grounded objection is preserved as first-class minority.

Manifest content convergence: all three advocates agree it should (a) define the engine, (b) enumerate engine-definition files, (c) name what is explicitly NOT part of the engine, (d) specify versioning discipline. Outsider adds "minimal initialisation contract for a fresh external application workspace" [01d Q4] as fifth content item — Architect implicitly agrees via Q6 template [01a Q6]; Operationalist notes the content as [uncertain] [01b Q4].

### 2.3 — On splitting `PROMPT.md`

**2-of-4 for split, 2-of-4 against.** For-split: Architect [01a Q3] + Outsider [01d Q3] (cross-model: Claude + non-Claude). Against-split: Operationalist [01b Q3] + Skeptic [01c Q3] (same-family: two Claude).

Per `multi-agent-deliberation.md` v3 §Limitations: *"All Claude-subagent perspectives share a model family. Shared training produces shared blind spots."* The cross-model-supported split position has greater epistemic weight than the same-family against position under this rubric. But a 2-2 count is not trivially dismissible; Operationalist and Skeptic's arguments are operationally specific.

**Structural convergence on split shape** between Architect and Outsider [01a Q3 + 01d Q3]: both propose a thin top-level entry point (Architect: `development-prompt.md` that "loads `engine-prompt.md` by reference"; Outsider: `PROMPT.md` as short dispatcher pointing to `prompts/development.md` and `prompts/application.md`) + separate mode prompts. Outsider's dispatcher pattern is structurally cleaner than Architect's because it preserves `PROMPT.md` as the canonical entry point without renaming.

**Adopted:** split, per Outsider's dispatcher-plus-two-mode-prompts shape. This honours the cross-model convergence on splitting while using the cleaner structural pattern. Against-split arguments preserved as first-class minority (see §4).

### 2.4 — On identity.md language

**3-of-4 preserve "Selvedge names the methodology" in some form** [Operationalist 01b Q5, Skeptic 01c Q5, Outsider 01d Q5]. Only Architect [01a Q5] changes the referent ("Selvedge names **the engine**").

Cross-model convergence (Operationalist + Skeptic + Outsider; Claude + Claude + non-Claude) strongly against Architect's "Selvedge names the engine" reading. Architect is isolated.

**Outsider's language adopted** [01d Q5]: *"Selvedge names the methodology. 'Selvedge engine' denotes the current executable implementation defined by `engine-manifest.md`."* This is the cleanest layered-denotation formulation; preserves identity-continuity (Reopening condition 1 argument) while resolving scope ambiguity.

### 2.5 — On workspace-structure.md revision (three file classes)

**2-of-4 for revision** [Architect 01a Q2, Outsider 01d Q2] — cross-model. **2-of-4 against** [Operationalist 01b Q2, Skeptic 01c Q2] — same-family.

Same cross-model pattern as §2.3 (split). Adopted with same justification. The file-class distinction is engine-definition files / development-provenance files / application-scope files.

### 2.6 — On H4 as novel hypothesis

Outsider [01d Q1] explicitly **rejects both H1 and H2** and proposes a fourth hypothesis:

> "My position is a fourth hypothesis: make the stack explicit as methodology -> engine -> application. Selvedge remains the methodology; the Selvedge engine is the current loadable implementation; each run against self-development or an external problem is an application of that engine."

This is the central cross-model contribution of the deliberation. It threads the needle between H2 (full reframe) and H3 (partial reframe) by keeping both senses of "methodology" alive — but explicitly — rather than collapsing one into the other. It aligns with §2.1 (keep kernel filename), §2.3 (split prompts for load-boundary clarity), §2.4 (Selvedge as layered denotation), and §2.5 (workspace-structure file classes).

**This is the third consecutive session (after Sessions 010, 013/014) where Outsider-originated structural resolution threads a three-way Claude split.** WX-10-5 / WX-11-3 pattern continues.

## 3. Cross-model contributions (Outsider-sourced, per OI-004 criterion 3)

Concrete outcome-shaping contributions from Outsider [01d] that NO Claude perspective produced:

1. **Layered model (methodology → engine → application)** as a fourth hypothesis rejecting H1/H2/H3's either/or framing [01d Q1]. Novel structural insight; neither Architect nor Operationalist proposed separating the methodology-level abstract from the engine-level concrete AND the application-level run as three distinct layers.
2. **"Selvedge engine" as qualified phrase** — preserving unqualified "Selvedge" for the methodology and using the qualified phrase for the implementation [01d Q5]. No Claude perspective produced this qualified-denotation resolution; Architect collapsed to engine, Operationalist conflated both, Skeptic refused the question.
3. **Thin-dispatcher PROMPT.md pattern** [01d Q3] — keeping `PROMPT.md` as a short top-level entry point while moving executable content to `prompts/development.md` and `prompts/application.md`. Architect proposed replacing `PROMPT.md` altogether; Outsider's dispatcher pattern preserves continuity of the entry point.
4. **"External application workspaces inherit the engine, not the engine's autobiography"** [01d Q6] — crisp articulation of the engine-definition-vs-development-provenance distinction at the operational activation level.
5. **Frame-challenge at Q1** — Outsider rejected the H1/H2/H3 framing itself as "entangling two different decisions that should be separated: what Selvedge is, and what must be loaded to run it" [01d Q1]. This methodological critique of the hypothesis frame is a genre of cross-model contribution consistent with WX-11-3 pattern (Outsider-originated resolution that Claude perspectives do not independently produce).

Cumulative OI-004 criterion-3 count: **40 through Session 014 + 5 in Session 017 = 45** across Sessions 005–017.

## 4. Preserved first-class minorities

### 4.1 — Skeptic's H1 "no reframing" position [01c all Q]

Preserved operationally via:
- The Reopening conditions in `identity.md` — specifically condition 1 (external adoption threshold, unmet). Skeptic's argument [01c Q5] is that H2 or H3 or H4 "de facto triggers" the condition without satisfying it. This is preserved as a standing warrant to reopen OI-017 if the Skeptic's predicted failure mode materialises (structural commitment without external-evidence justification).
- The **three-consecutive-session preservation-discipline warrant**: if three consecutive sessions 018+ revise H4's adopted shape without operational pressure (no external adopter; no documented friction blamed on the layered model), Skeptic's position becomes the preferred revision direction for reverting toward H1.

Skeptic's exact warrant language [01c Q7]: *"The observable that would cause me to abandon H1 in favour of H3: a named prospective practitioner (identified by email address, not a hypothetical) reports, in a form recorded in provenance, that they attempted to understand what adopting Selvedge would mean and could not do so because of the methodology/engine/implementation ambiguity."* Inverse: if H4 is adopted and no such report materialises over an extended period, the workspace should revisit whether H4's structural commitment paid for itself.

### 4.2 — Operationalist's H3 "cosmetic-reframing" concern [01b Q7]

Preserved as warrant: if the split `prompts/development.md` and `prompts/application.md` turn out to be "almost the same ... with only small variable substitutions and no meaningful behavioural divergence" [01d Q7, Outsider-convergent with Operationalist], the split is premature and should be merged back. Outsider explicitly agrees this would be evidence to abandon H4 in favour of H3.

### 4.3 — Architect's H2 "truth-surfacing" full-rename position [01a Q2, Q5]

Preserved as warrant: if operational experience with H4 reveals that the layered model's "Selvedge methodology" / "Selvedge engine" distinction is not meaningful in practice (i.e., users collapse them to "Selvedge" in all cases without losing information), Architect's stronger rename-the-kernel position becomes the preferred revision direction. Architect's H2 is explicitly not ruled out by H4; it is deprioritised as over-specifying.

## 5. Check for operator-preference-priming

Operator stated preference at Session 017 open: "Continue with OI-017 as preference (full reframe)." This points at H2.

**Preference-priming check:** did perspectives drift toward H2 due to the stated preference?

- Architect [01a]: advocated H2 (matches preference). Reasoning is role-assigned; cannot independently diagnose priming vs assigned-role execution.
- Operationalist [01b]: advocated H3 (diverges from preference). Did not drift.
- Skeptic [01c]: advocated H1 (diverges strongly from preference). Did not drift.
- Outsider [01d]: advocated H4, explicitly rejecting H2 as "overcorrects" [01d Q1]. Did not drift.

**3-of-4 diverged from operator preference.** The one perspective that matched (Architect) did so as assigned-role. No preference-priming signal detected. Brief-priming-absent streak extends to eight consecutive sessions (Sessions 010–017).

## 6. Synthesis recommendation

Adopt **H4** (Outsider-originated layered model) with the following specific shape:

1. **Three-layer denotation**: methodology → engine → application. `identity.md` v1 → v2 incorporates Outsider's language at [01d Q5].
2. **`PROMPT.md` as thin dispatcher** with executable content moved to `prompts/development.md` (self-development mode; current workspace's entry point) and `prompts/application.md` (external-problem mode; template-shaped, minimally specified pending first external use). Honours 2-of-4 cross-model-supported split; preserves 2-of-4 same-family against-split position as minority warrant.
3. **New `engine-manifest.md` v1** per Outsider's minimal specification [01d Q4]: engine definition, canonical file set, entry points per application kind, exclusion list, minimal initialisation contract. 3-of-4 cross-model convergence; preserves Skeptic's "specification-without-consumer" objection as first-class minority warrant.
4. **`workspace-structure.md` v2 → v3** with explicit file-class distinction (engine-definition / development-provenance / application-scope). 2-of-4 cross-model-supported; preserves 2-of-4 same-family against position as minority.
5. **`methodology-kernel.md` v4 remains v4 by filename**; add one-sentence scope clarification near top of §Purpose per Outsider's language [01d Q2]. 3-of-4 against-rename convergence (cross-model).
6. **Light edits** to `multi-agent-deliberation.md` and `validation-approach.md` stating their rules apply to both self-development and external-application runs. Minor-not-substantive per Session 005 D-034 precedent (elaboration within existing scope).
7. **`reference-validation.md` unchanged** per Outsider's finding [01d Q2] that no concrete inconsistency exists.

Skeptic's H1 position is not adopted but is preserved as first-class minority with specific Reopening-condition warrant. Operationalist's H3 cosmetic-reframing concern is preserved as warrant with merge-back condition. Architect's H2 kernel-rename position is preserved as warrant for stronger-restructure direction.

## 7. Operator-preference reconciliation

The deliberation's conclusion (H4) departs from operator's stated preference (H2) in specific ways:
- H4 does **not** rename `methodology-kernel.md` to `engine-kernel.md` (Architect's H2 detail that Operationalist, Skeptic, and Outsider all rejected).
- H4 keeps "Selvedge" naming the methodology, using "Selvedge engine" as the qualified implementation phrase (rejects Architect's Selvedge-names-engine reading).
- H4 **does** split `PROMPT.md` (matches operator preference direction).
- H4 **does** create `engine-manifest.md` (matches H2/H3 direction).
- H4 **does** add workspace-structure file-class distinction (matches H2 direction).

Net: H4 adopts the reframing direction the operator preferred but rejects the specific H2 rename-and-collapse shape based on 3-of-4 cross-model evidence. The operator's Session 016 framing ("for the engine to determine"; "no stake in the specific shape") explicitly authorises this departure; the Session 017 steering ("as preference") does not elevate H2 to binding. Decision D-074 will adopt H4 per this synthesis; no user ratification halt is required unless the user subsequently overrides.

## 8. Limitations

Required content per `multi-agent-deliberation.md` v3 §Limitations:

- All three Claude-subagent perspectives (Architect, Operationalist, Skeptic) share the Claude Opus 4.7 model family. Their agreement patterns are cross-context-isolated but not cross-training-lineage isolated. The non-Claude Outsider (OpenAI GPT-5.4 via `codex exec`) is the primary cross-model-honesty signal.
- Intra-Claude-family size-mixing was not used in this deliberation (all three Claude perspectives are Opus 4.7). Does not narrow OI-004.
- Parallel context isolation prevents conversational anchoring but not training-distribution anchoring. The three Claude perspectives' convergence patterns (e.g., preserving "Selvedge names the methodology" in §2.4) must be read with the shared-priors caveat.
- Brief-writing has no adversary. The shared brief's framing choices propagated into all four briefs identically. The hypothesis-frame H1/H2/H3 in §1.5 was orchestrator-generated; Outsider explicitly challenged this frame and proposed H4, which is the session's strongest anti-framing-drift signal.
- Synthesis is the highest-risk single-agent re-entry point. The synthesizer (Claude Opus 4.7) may be systematically biased toward patterns that match the Claude perspectives more than the Outsider's. The synthesis mitigates this by explicitly weighting Outsider-originated language (§2.4 identity.md wording; §2.3 dispatcher shape) as the adopted content.
- Non-Claude participation depends on convener fidelity. Outsider's response was captured via `codex exec` and committed verbatim at `01d-perspective-outsider.md`; the raw response file is the primary record. No post-hoc editing.
- A single non-Claude participant narrows OI-004 less than its presence suggests. This is the eleventh session with non-Claude participation and the sixth required-trigger deliberation; sustained-practice tally will advance 5-of-3 → 6-of-3.
