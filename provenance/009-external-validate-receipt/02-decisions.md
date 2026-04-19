---
session: 009
title: Decisions — Kernel Validate & Workspace-Structure Revisions
date: 2026-04-19
status: complete
---

# Decisions — Session 009

Decisions recorded in this session: **D-053 through D-056** (four decisions). Each declares `triggers_met:` and `triggers_rationale:` per the schema introduced in Session 006 (D-037, D-038).

---

## D-053: Revise methodology-kernel.md §7 to name two senses of Validate (W4)

**Triggers met:** [d016_1, d016_2, d016_3, d023_1]

**Triggers rationale:** The decision modifies `methodology-kernel.md` (d016_1) and substantively revises a specification in `specifications/` (d016_2). Reasonable practitioners genuinely disagreed: three-of-four perspectives favoured some form of revision while the Skeptic argued for drop-entirely on n=1 grounds (d016_3). Kernel modification mandates non-Claude participation (d023_1); the Outsider perspective is present and its positions materially shaped the adopted text.

**Decision.** Replace the current `methodology-kernel.md` §7 with the following text:

> #### 7. Validate
>
> Validate the session's output at each level on which it makes claims. Two senses apply.
>
> **Workspace validation** applies to every session. Check that:
>
> - New specifications don't contradict existing ones
> - Specifications describe the workspace as it actually is
> - Provenance records are complete and well-formed
> - Open issues reflect the actual state of uncertainty
>
> **Domain validation** applies when a session produces or revises an artefact intended for use outside the workspace. Obtain evidence from the domain-actor who holds the problem the artefact addresses — the user of a sequence, the reader of a specification, the participant in a process, or an equivalent — that the artefact functioned for its intended use. Record who performed the validation, what was tried, what happened, and whether modifications were requested. Domain validation may complete out-of-session; when it does, the receiving session records the report and decides whether it triggers revision.
>
> If either validation reveals problems, they are either fixed in this session (return to Produce) or recorded as open issues for subsequent sessions.

`methodology-kernel.md` is revised v1 → v2. v1 is preserved as `methodology-kernel-v1.md` per workspace-structure.md §specifications. The new v2 is set `last-updated: 2026-04-19`, `updated-by-session: 009`, `supersedes: methodology-kernel-v1.md`.

**Substantive-versus-minor classification per OI-002 heuristic.** Substantive. The revision adds new normative content (a second named sense of Validate; a record-format for domain validation evidence; an explicit recognition that Validate may complete across sessions). This is beyond what the v1 language contains or anticipates.

**Key arguments carried (convergent).**

1. The two senses are already in active use — Workspace validation by `tools/validate.sh` and other internal checks, Domain validation by the user's Session 009 Validate report on the Session 008 artefact. A kernel that names only one creates downstream divergence.
2. Preserving the nine-activity count (all four perspectives agreed) avoids cascading reference edits in `multi-agent-deliberation.md` and `validation-approach.md` that refer to "the nine activities."
3. Domain-actor phrasing (rather than user-only) incorporates the Outsider's Q4 observation [01d, Q4] that receipt shapes will vary.
4. Cross-session completion is explicitly allowed, matching Session 008→009 actual practice.

**Rejected alternatives (preserved as dissent).**

- **Skeptic: drop Q1 entirely.** [01c, Q1]: "Session 008 is n=1… Better to stay silent now and let the shape emerge." The Skeptic argued that the richer revisions cascade into validation-approach edits and lengthen the kernel on one data point. Rejected because three-of-four perspectives (including the Outsider) independently argued that the ambiguity is in the kernel itself and will re-surface every external-artefact session. The Skeptic's minimum-form (one appended scoping sentence) was considered and rejected as preserving ambiguity about whether the user's out-of-session test was kernel-Validate or something else.

- **Reviser: named 7a/7b sub-activity labels.** [01a, Q1]: more structural than the adopted form. The Outsider's bolded category labels ("Workspace validation" / "Domain validation") read more cleanly and carry the same distinction without implying numeric ordering within §7.

- **Minimalist: one appended bullet only.** [01b, Q1]: preserves the smallest possible surface but, per the Reviser's objection, hides the fact that Domain validation is a categorically different check from the first four bullets. Rejected because the adopted form's explicit category structure makes the categorical distinction visible to a first-time reader without adding new vocabulary beyond "Domain validation" itself.

- **Add a tenth kernel activity.** [01a, 01b, 01c, 01d all reject]: all four perspectives rejected this. No further consideration.

**Non-Claude participation:** included (Outsider = OpenAI GPT-5 via `codex exec`). No skip annotation. The Outsider's Q1 text is the primary source for the adopted wording, with Q4 integration finding 4 (domain-actor phrasing) also Outsider-sourced.

---

## D-054: Create applications/ top-level directory; regularize Session 008 artefact by copy-plus-reference (W2)

**Triggers met:** [d016_2, d016_3]

**Triggers rationale:** Substantively revises `workspace-structure.md` (d016_2) by adding a new top-level directory and a new normative category of workspace content. Reasonable practitioners genuinely disagreed (d016_3) — a 2-2 split on whether to create `applications/` at all, resolved by synthesizer judgment with dissent preserved. d023_* not triggered: `workspace-structure.md` is not in the D-023 category list (D-023 covers kernel, multi-agent-deliberation, validation-approach, and OI-004 state changes). Non-Claude participation was included as part of the session's deliberation on the kernel revision (D-053) and materially influenced the Q2 outcome via the Outsider's copy-plus-reference mechanism, even though Q2 itself does not independently require non-Claude participation.

**Decision.**

1. Create new top-level directory `applications/` as the canonical home for **external artefacts** — work-products the methodology has produced for use outside the workspace.

2. Revise `workspace-structure.md` v1 → v2 to add a new §applications section, amend §Additional directories to note applications/ is now defined rather than hypothetical, and preserve v1 as `workspace-structure-v1.md`. Proposed §applications text:

   > ### applications/
   >
   > Contains external artefacts — work-products the methodology has produced for use outside the workspace (specifications, sequences, templates, design fragments, and the like). Organized by the session that originally produced the artefact:
   >
   > ```
   > /applications/
   >   /NNN-[slug]/
   >     [artefact-files]
   > ```
   >
   > `NNN` is the producing session's number; `[slug]` is a short descriptive name. Filenames within the directory are descriptive (not numbered for reading order) — the numbered-reading-order convention applies to provenance records only.
   >
   > External artefacts are **mutable**: they may be revised by later sessions in response to domain validation (methodology-kernel.md §7 Domain validation) or other feedback. Revisions update the artefact in place; the revising session's provenance records what changed and why. When an artefact is revised, the corresponding provenance copies in the originating session and any prior revising sessions remain untouched (per the provenance immutability rule) and serve as historical witnesses to earlier versions.
   >
   > **Regularization of pre-existing external artefacts.** When an external artefact was placed in a producing session's provenance directory before `applications/` existed, the artefact is regularized into `applications/` by **copy-plus-reference**: a copy is made to `applications/NNN-[slug]/[filename]` with frontmatter fields `originating_session` and `regularized_in_session`; the provenance copy is not moved, modified, or deleted. The regularizing session's decision record is the authoritative cross-reference.

3. Regularize Session 008's artefact via copy-plus-reference. Specifically:

   - **Copy** `provenance/008-first-external-application/artefact-morning-unfurl.md` to `applications/008-morning-unfurl/morning-unfurl.md`.
   - Add to the copy's frontmatter: `originating_session: 008`, `regularized_in_session: 009`, `provenance_witness_path: provenance/008-first-external-application/artefact-morning-unfurl.md`.
   - Do **not** modify `provenance/008-first-external-application/artefact-morning-unfurl.md` or its directory (preserves immutability of closed provenance).
   - Do **not** create a forward-pointer file in Session 008's provenance (would require modifying closed provenance; forbidden).

4. Future sessions producing external artefacts should place them directly in `applications/NNN-[slug]/` from the start. No regularization is needed for sessions that adopt the canonical path at creation.

**Substantive-versus-minor classification per OI-002 heuristic.** Substantive. New top-level directory; new normative category (mutable external artefacts distinct from immutable provenance); new regularization procedure. Well beyond v1's language.

**Key arguments carried.**

1. Provenance is immutable; external artefacts are mutable — Session 008's artefact was validated positively ("no modifications requested") but could have been validated negatively and would then have required revision. Embedding mutable artefacts in immutable directories is a structural contradiction. [Reviser 01a, Q2; Outsider 01d, Q2].
2. External readers seeking what the methodology has produced should not need to navigate provenance archaeology to find deliverables. [Outsider 01d, Q2; Reviser 01a, Q2].
3. The Outsider's copy-plus-reference mechanism [01d, Q2] resolves the immutability concern that Minimalist and Skeptic raised: the provenance copy stays as a frozen historical witness; the applications/ copy is the live, mutable canonical.

**Rejected alternatives (preserved as dissent).**

- **Minimalist + Skeptic: do not create applications/.** [Minimalist 01b, Q2]: "One artefact is one data point. Creating `applications/` from one case makes a pattern claim the evidence does not support." [Skeptic 01c, Q2]: "This is n=1 architecture." Both proposed a one-sentence addition to `workspace-structure.md` canonicalizing Session 008's embedded pattern. **Rejected on mutability grounds**: the current embedded pattern works only until an artefact needs revision, at which point it violates provenance immutability. A specification that works only until its first exercise of a foreseeable case is a specification with a known failure mode. The synthesizer judges the structural integrity argument stronger than the pattern-from-n=1 objection, while preserving the minority dissent as first-class in this record. Applications/ can be deprecated by a future session if it does not earn its place; reversibility mitigates the pattern-commitment concern. **This is the most contested decision of Session 009.**

- **Reviser: move the Session 008 artefact rather than copy.** [01a, Q2]: "Move… to `applications/008-morning-unfurl/artefact.md`. Leave a forward-pointer file `provenance/008-first-external-application/external-artefact.md`." **Rejected** on three-of-four immutability convergence: moving files out of a closed session's provenance directory, or adding new files to a closed directory, contradicts the "immutable once the session closes" property in workspace-structure.md v1 §provenance. The Reviser's proposed forward-pointer file would itself be a new file in a closed directory; not allowed.

- **Hybrid: artefact in provenance, stub in applications/.** [Reviser implicit, Minimalist 01b rejects, Skeptic 01c rejects]: "The only thing it adds is a second address for each artefact to fall out of sync with" [Skeptic, 01c, Q2]. Rejected.

**Non-Claude participation:** included. The Outsider's copy-plus-reference mechanism is the Outsider-original contribution that unlocked this decision; the Claude 2-2 split (Reviser move vs Minimalist/Skeptic leave-in-place) did not produce a path that honoured both mutability and immutability until the Outsider proposed the third way.

---

## D-055: Defer `tools/validate.sh` path-flexibility update; record as new open issue

**Triggers met:** [d016_3, d016_4]

**Triggers rationale:** Reasonable practitioners disagreed genuinely (d016_3) — a 2-2 split on whether to update the tool now or defer. Operator-marked load-bearing (d016_4) because Session 008 specifically flagged this as a brittleness requiring a Session 009 resolution one way or the other; this decision is the resolution, and its disposition (defer) is as much a substantive choice as a fix-now would have been. d023_* not triggered (the decision does not modify any spec in the D-023 category list; it declines to modify a tool).

**Decision.**

1. Leave `tools/validate.sh` as it currently is (15 Tier-1 checks, 7 Tier-2 questions, hard-coded `02-decisions.md` path in checks 14 and 15).

2. Open new open issue **OI-012: `validate.sh` hard-coded `02-decisions.md` path**. Wording to record in `open-issues.md`:

   > `tools/validate.sh` checks 14 and 15 hard-code the path `02-decisions.md` as each session's decisions file. Session 008 surfaced that this creates a silent-bypass hazard if a session numbers other files (e.g., artefacts) into positions that shift the decisions file to `03-` or later. Session 008 worked around this by using a non-numbered filename for the external artefact; Session 009 removed the collision source by moving external artefacts to `applications/` (D-054). The hard-coded path therefore no longer has an active collision pressure. The defect remains available to bite under different future patterns (e.g., a future session wanting variable decisions-file numbering; or a session generating multiple deliberation artefacts that force renumbering). Revisit when such a pressure arises, or when a second concrete collision occurs, whichever comes first.

3. D-054's adoption of `applications/` removes the immediate hazard. External artefacts leave the provenance directory; the numbered-reading-order files in provenance remain stable; the `02-decisions.md` assumption is no longer at risk from external-artefact numbering.

**Substantive-versus-minor classification per OI-002 heuristic.** Not applicable — no specification is being revised. The tool remains unchanged.

**Key arguments carried.**

1. [Skeptic 01c, Q3]: "Touching a validator in a session that isn't going to stress-test the change is how validators acquire bugs."
2. [Skeptic 01c, Q3] (on pattern-matching specifically): "Pattern-matching makes the tool more permissive, which sounds like robustness. But validate.sh's value is that it catches deviations from the expected shape… Before relaxing the assertion, we should know what variance the tool is supposed to tolerate — and we don't, from one data point."
3. [Minimalist 01b, Q3]: parameterising or pattern-matching "Adds configuration surface for a problem that is already solved by convention."
4. [synth]: D-054's applications/ decision removes the immediate collision pressure. The tool's strictness is a feature, not a bug, when there is no evidence of current or imminent variance to tolerate.

**Rejected alternatives (preserved as dissent).**

- **Reviser + Outsider: pair the tool update with the workspace-structure revision.** [Reviser 01a, Q3]: "A specification whose tool requires an unwritten filename convention to function is a specification with a hidden dependency." [Outsider 01d, Q3]: "The hard-coded `02-decisions.md` path is not just inelegant; it creates a silent failure mode." Both proposed pattern-match to `[0-9][0-9]-decisions.md` (Reviser) or `NN-decisions.md` (Outsider), with fail-if-zero-matches and fail-if-multiple-matches. **Rejected on the grounds that the applications/ decision (D-054) removes the current pressure; pattern-matching reduces the tool's strictness without corresponding stress-test evidence.** This dissent is load-bearing: if OI-012's re-visit trigger fires, the Reviser+Outsider pattern-match proposal is the preferred starting point for the Session-that-triggers deliberation. Preserved in full.

**Non-Claude participation:** Outsider present. Outsider position (fix-now) was not adopted; minority Outsider position is preserved explicitly in OI-012's wording.

---

## D-056: OI-004 sustained-practice tally advances 2 → 3 of 3; session housekeeping (watchpoints, validation-approach.md minor correction)

**Triggers met:** [d016_1, d016_4, d023_4]

**Triggers rationale:** Asserts a change in the state of OI-004 (d023_4 and d016_1 by extension of the kernel-modification-implies-OI-004-triggering reading — and also asserts OI-004 criterion-2 satisfaction). Operator-marked load-bearing (d016_4) because this is the decision that formally registers Session 009 as a sustained-practice deliberation, adopts the Q4 integration resolutions, and houses the watchpoint records.

**Decision.**

**(1) OI-004 sustained-practice tally.** Session 009 is the third required-trigger deliberation with non-Claude participation (Sessions 005, 006 preceded; Sessions 007 and 008 included non-Claude participation voluntarily but did not fire any D-023 trigger). D-053 fires d023_1 (kernel modification) and this decision D-056 itself fires d023_4 (OI-004 state change). Both required-trigger criteria are active; non-Claude participation was present.

- **Sustained-practice tally (criterion 2):** advances from **2 of 3** (status after Session 008) to **3 of 3**.
- **OI-004 closure not automatic.** Per `multi-agent-deliberation.md` v3 §Closure Criteria, closure requires all four of: (1) participant independence [satisfied — Outsider is `training_lineage_overlap_with_claude: independent-claim`]; (2) sustained practice ≥ 3 required-trigger deliberations [**newly satisfied in Session 009**]; (3) recorded impact [satisfied — Outsider's copy-plus-reference shaped D-054, Outsider's domain-actor phrasing shaped D-053's adopted text, Outsider's tool-fix position shaped D-055's dissent preservation; cumulative across Sessions 005–009]; (4) articulated definition of "substantively different training provenance" and enumerated acceptable participant kinds [**remains unmet**]. OI-004 is therefore **closable but not closed**. Closure requires a future session's explicit deliberation on criterion 4.
- OI-004 status transitions from `narrowed-pending-sustained-practice` (2 of 3) to `closable-pending-criterion-4-articulation`.

**(2) Minor correction to `validation-approach.md`.** Add a one-sentence scope note to §Purpose stating the specification covers methodology-kernel.md §7 Workspace validation; Domain validation (kernel §7) is performed by domain-actors and is outside this specification's Tier 1 / Tier 2 scope. This is a minor correction per the OI-002 heuristic (descriptive annotation within the section's stated purpose; no new normative content, no new rules, no new required fields, no severity decisions, no gating rules, no triggers, no required artefacts). No version bump; `validation-approach.md` remains v3. Precedent: D-014 (Session 002) and D-020 (Session 003) for minor corrections bundled without file-level versioning.

**(3) New open issues.**

- **OI-012** (per D-055): `validate.sh` hard-coded `02-decisions.md` path. Wording in D-055.
- **OI-013**: **Non-file external artefacts.** Applications/ presumes file-shaped deliverables (Markdown, structured text, YAML). Future external artefacts that are software implementations, physical objects, running services, or other non-file shapes will strain the current workspace-structure §applications text. Deferred until the first such case surfaces; no pre-specification. Sourced from [Skeptic 01c, Q4] and [Outsider 01d, Q4].
- **OI-014**: **Domain-actor receipt shape variance.** The kernel §7 Domain validation text (D-053) uses "domain-actor" phrasing deliberately broad enough to cover user, expert, panel, or observational data. Session 008 exercised one shape only (single user, self-reported, timely). Future external artefacts may produce receipts that do not fit a specific-actor-with-specific-problem-timely-report loop; the kernel text does not pre-specify how such receipts are handled. Monitor. Sourced from [Minimalist 01b, Q4] and [Outsider 01d, Meta-note].

**(4) Additional OI updates.**

- **OI-005** (sub-activities and work-type variants): Session 008 deferred this to a second external application. D-053's adoption of two named senses under §7 Validate partially addresses the W4 work-type-variant observation. OI-005 status updated to note that W4 has been resolved via D-053; the broader sub-activity question remains open and still deferred to a second external application.
- **OI-009** (drift-to-ritual): Monitor status maintained. Session 009's self-work passes G/O/K/S on the majority reading (three-of-four perspectives' Q5 grades place Q1 and Q2 as load-bearing, with the Skeptic's minority position that Q1 does not satisfy O preserved). Session 009 was ratified by the user as the direction after Session 008's positive external Validate; the G/O/K/S criterion-package adopted in Session 007 D-048.2 remains operational.

**(5) OI housekeeping on OI-007 (scaling open issues format).** Session 009 opens three new OIs (OI-012, OI-013, OI-014). Open-issue count rises from 9 to 12. The single-file format remains readable but is approaching the threshold at which a directory-per-issue or category-based layout may warrant consideration. No action this session; monitor.

**Substantive-versus-minor classification per OI-002 heuristic.** Decision D-056 does not revise any specification; it asserts OI state changes and authorises the validation-approach.md minor correction per D-014 precedent. Not applicable to the OI-002 heuristic per se. The validation-approach.md minor correction is explicitly classified as minor per the reasoning in §(2) above.

**Key arguments carried.**

1. The OI-004 tally advancement is mechanical per the v3 spec's closure criteria — Session 009 has a required-trigger deliberation (D-053 modifies kernel; D-023.1 fires) with non-Claude participation present.
2. OI-004 is "closable" not "closed" because criterion 4 (articulation of substantively different training provenance) has not been deliberated. A closure deliberation is a future session's work and is itself D-023-triggering.
3. Watchpoint-not-revision discipline (per D-047.3 precedent in Session 008) for OI-013 and OI-014: record the empirical concerns; do not pre-specify their resolution.

**Rejected alternatives (preserved as dissent).**

- **Deliberate OI-004 closure in Session 009.** Considered and rejected: closure requires criterion 4 to be articulated, which is not within Session 009's ratified scope (W2 + W4 only). A closure deliberation is itself D-023-triggering and warrants its own session focus.
- **Version-bump `validation-approach.md` to v4 for the scope note.** Considered and rejected: the scope note is descriptive annotation of what the existing specification already covers. Per the OI-002 heuristic, this is minor. D-014 and D-020 precedents for bundled minor corrections apply. A v4 bump would inflate the supersession chain without corresponding normative change. Reviser + Outsider's "coordinated change" argument is honoured by the minor correction; Skeptic's "no bundling" concern is honoured by the no-v-bump form.
- **Open an OI for validation-approach.md Domain-validation-section gap.** Considered and rejected: the minor correction above addresses the immediate divergence risk. A future session producing a second external artefact with a different receipt shape may warrant a richer validation-approach.md revision, but that is OI-014 territory (monitor) rather than a pre-emptive OI.

**Non-Claude participation:** included. The OI-004 tally advancement is the mechanical result of Session 009's required-trigger deliberation with Outsider present; the state change assertion is what activates d023_4 here.

---

## Summary

| Decision | Triggers met | Non-Claude | Nature |
|---|---|---|---|
| D-053 | d016_1, d016_2, d016_3, d023_1 | present | Substantive spec revision — methodology-kernel.md v1 → v2 |
| D-054 | d016_2, d016_3 | present (not required) | Substantive spec revision — workspace-structure.md v1 → v2; applications/ directory created |
| D-055 | d016_3, d016_4 | present (not required) | Defer tool change; OI-012 opened |
| D-056 | d016_1, d016_4, d023_4 | present | OI-004 state change (tally 2→3); watchpoints OI-013, OI-014; validation-approach.md minor correction |

Session 009 is the third required-trigger deliberation with non-Claude participation. OI-004 sustained-practice criterion 2 is satisfied; OI-004 is now **closable pending criterion 4 articulation**, not closed.
