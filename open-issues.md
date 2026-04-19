# Open Issues

Issues identified during sessions that remain unresolved. Each entry records the issue, the session that surfaced it, and its current status.

---

### OI-001: Naming the methodology
**Surfaced:** Session 001
**Status:** Open
The methodology does not yet have a name. A name should emerge when the methodology has developed enough identity to be named meaningfully. See deliberation in `provenance/001-genesis/01-deliberation.md`, Question 6.

### OI-002: Threshold for substantive revision vs. minor correction
**Surfaced:** Session 001
**Status:** Open (data points added Sessions 002, 003, 004, 005, 006)
Decision D-004 established that substantive revisions trigger file-level version preservation while minor corrections do not. No formal criteria for distinguishing the two have been defined. Session 002 (D-014): adding `tools/` to workspace-structure was minor — change *anticipated by* the specification's own language. Session 003 (D-020): adding a pointer to `multi-agent-deliberation.md` in methodology-kernel.md was minor — kernel's Convene/Deliberate language was already mechanism-neutral. Session 004 (D-026): revising `multi-agent-deliberation.md` v1 → v2 was **substantive** — adds new normative content (new trigger rules, new required fields, new mechanism shapes) not anticipated structurally in v1. Session 005 (D-034): a pair of simultaneous revisions resolved differently — revising `validation-approach.md` v1 → v2 was **substantive** (added three new Tier 1 checks with gating, severity, sequencing, and a new Tier 2 question; new normative content); annotating each Open Extensions entry in `multi-agent-deliberation.md` v2 with an activation precondition was **minor** (elaboration within the section's explicit purpose of naming future candidates; no rules, required fields, triggers, or required artefacts changed). Session 006 (D-041): first session where **both** active revisions were substantive — `multi-agent-deliberation.md` v2 → v3 (adds `triggers_met:` required schema, new Trigger-Coverage Annotation Schema section, updates Validation section operationalisation status) and `validation-approach.md` v2 → v3 (adds two new Tier 1 checks with gating/severity/sequencing/honest-limits and a new Tier 2 question). D-042's revision of an Open Extensions activation precondition was minor per the Session 005 pattern (bundled into v3, not separately preserved). The five-point heuristic holds stable: **minor** if the change makes explicit what the specification's existing language already contains or explicitly anticipates as a category of extension, OR annotates existing candidate entries with descriptive metadata within the section's stated purpose; **substantive** if the change adds new normative content (rules, required fields, severity decisions, gating rules, triggers, required artefacts) beyond what the existing language contains.

### OI-004: Incorporating genuinely independent perspectives
**Surfaced:** Session 001
**Status:** **Closable pending criterion-4 articulation** after Session 009 per D-056 (sustained-practice tally advanced from 2 of 3 to **3 of 3**; closure criteria 1, 2, and 3 satisfied; criterion 4 unmet). Previous states: Open; narrowed-pending-sustained-practice after Session 005 (tally 1 of 3); tally advanced to 2 of 3 in Session 006 per D-043; tally unchanged at 2 of 3 after Session 007 per D-049 and Session 008 per D-052 (non-Claude participation included without D-023 trigger in both cases); tally advanced to **3 of 3** after Session 009 per D-056 (D-053 modifies methodology-kernel.md → d023_1 fires; D-056 asserts OI-004 state change → d023_4 fires; non-Claude participation present; required-trigger deliberation status confirmed)
When a single AI agent plays all perspectives, disagreement is simulated. Session 003 built parallel context-isolated Claude subagents as the first real mechanism, closing the single-context simulation gap but leaving the Claude-monoculture gap. Session 004 specified a non-Claude participation mechanism (in `multi-agent-deliberation.md` v2, see D-021/D-023/D-024) but explicitly chose **not** to claim any narrowing of OI-004 (D-025), because no non-Claude participant was in Session 004's deliberation. Narrowing requires operational use.

**Session 006 tally (per D-043):** Two sessions of non-Claude participation had occurred (Sessions 005 and 006, both Outsider perspective via `codex exec` to OpenAI GPT-5; both D-023 required-trigger deliberations).

**Session 007 tally (per D-049):** Session 007 included non-Claude participation (Outsider = OpenAI GPT-5 via `codex exec`, continuing the Sessions 005/006 pattern) with a full D-024 manifest, **but none of Session 007's decisions (D-044 through D-049) triggered any D-023 clause** — no kernel modification, no spec revision, no OI-004 state change. Per the strict v3 spec closure-criterion-2 reading ("at least three required-trigger deliberations"), Session 007's deliberation was not a required-trigger deliberation; the sustained-practice tally does **not** advance. Tally remains at 2 of 3. This was the methodology's **first non-Claude session without a D-023 trigger** and was recorded as a novel data pattern. Criterion 3 (recorded impact) gained three data points from Session 007 (Skeptic+Outsider convergence against pre-use spec changes shaping D-047; Outsider-unique methodology-claim downgrade proposal shaping D-048.4; Outsider's ratification-as-third-path framing informing D-045 Branch B).

**Session 008 tally (per D-052):** Session 008 included non-Claude participation (Outsider = OpenAI GPT-5 via `codex exec`, continuing the Sessions 005/006/007 pattern) with a full D-024 manifest, **but none of Session 008's decisions (D-050, D-051, D-052) triggered any D-023 clause** — target-selection and artefact-production did not modify the kernel or specs, and no OI-004 state change was asserted. Per the strict v3 spec closure-criterion-2 reading, Session 008's deliberation was not a required-trigger deliberation; the sustained-practice tally does **not** advance. Tally remains at 2 of 3. This is the **second consecutive non-advancing non-Claude session**. Criterion 3 gains three more data points from Session 008 (four-way Q5 convergence on "representability / document-shape / artefact-shape / medium bias" crossing the model-family axis — the Outsider's independent arrival at the same structural finding is the strongest single cross-model signal across all four heterogeneous sessions; Outsider's independent meal-rotation recommendation as Candidate 1 supporting synthesizer's shortlist composition; Outsider-unique "preference instability" failure-mode framing). Cumulative criterion-3 data points across Sessions 005–008: twelve. Criterion 4 (articulation of "substantively different training provenance") remains unmet.

**Session 009 tally (per D-056):** Session 009 is the third required-trigger deliberation with non-Claude participation. D-053 modifies `methodology-kernel.md` §7 (d023_1 fires); D-056 itself asserts the OI-004 state change (d023_4 fires). The Outsider (OpenAI GPT-5 via `codex exec`) was present in the deliberation and its positions materially shaped two adopted decisions (D-053's domain-actor phrasing; D-054's copy-plus-reference regularization mechanism) with two further positions preserved as load-bearing dissent (D-055 tool-fix preservation; kernel framing influence). Tally advances from 2 of 3 to **3 of 3**. Criterion 2 is newly satisfied.

**Closure criterion status (per `multi-agent-deliberation.md` v3 §Closure Criteria):**

- **Criterion 1 (participant independence):** satisfied. Outsider carries `training_lineage_overlap_with_claude: independent-claim` in every qualifying session (Sessions 005, 006, 009 required-trigger; Sessions 007, 008 voluntary).
- **Criterion 2 (sustained practice ≥3 required-trigger deliberations):** **newly satisfied after Session 009.**
- **Criterion 3 (recorded impact on outcomes):** satisfied. Cumulative data points: fifteen across Sessions 005-009 (twelve through Session 008; three added in Session 009 — Outsider's copy-plus-reference shaping D-054, Outsider's domain-actor phrasing shaping D-053, Outsider's Meta-note on tool-validate-drift shaping D-053 framing). Criterion 3 has been satisfied since Session 005; Session 009 extends the evidence base.
- **Criterion 4 (articulated definition of "substantively different training provenance" and enumerated acceptable participant kinds):** **unmet.** No session has yet deliberated this articulation.

**Closure status:** **Closable**, not closed. Criteria 1, 2, and 3 are satisfied. Criterion 4 requires a future session's explicit closure deliberation (which would itself be D-023-triggering and require non-Claude participation). Session 009 does not attempt closure because its ratified scope (W2 + W4) does not include criterion-4 articulation.

The prior question of whether criterion 2 should expand to count voluntary non-Claude inclusion (raised implicitly by Sessions 007 and 008's voluntary-inclusion-no-D-023-trigger pattern) is now moot with respect to Session 009's tally advance but remains a relevant heuristic question for a future closure deliberation if it reviews criterion 2's robustness.

Closure criteria are specified in `multi-agent-deliberation.md` v3's Closure Criteria section (unchanged from v2): (1) participant independence; (2) sustained practice across ≥3 required-trigger deliberations; (3) recorded impact on outcomes; (4) articulated definition of "substantively different training provenance." "Closable" and "closed" remain distinct states; closure requires explicit deliberation by a future session.

### OI-005: Sub-activities and work-type variants
**Surfaced:** Session 001
**Status:** Open — **W4 partially addressed by Session 009** (D-053 added Workspace / Domain sub-senses under §7 Validate, which resolves the W4 sub-activity observation for the Validate activity specifically). W1 (Read activity) remains deferred. Broader sub-activity question for Read, Assess, Convene, Deliberate, Decide, Produce, Record, Close remains deferred to a **second** external application (to avoid proposing sub-activity variants from one data point).
The nine core activities may need sub-activities, and different types of work (research, design decisions, validation, implementation) may warrant different subsets or emphases. Session 008's Produce activity surfaced four watchpoint findings (W1–W4 per D-051). Session 009 addressed W4 via D-053's §7 Validate revision (two named senses: Workspace validation, Domain validation). W1 (Read activity for external domains has two senses — workspace-reading vs. domain-knowledge absorption) remains open; the broader question of sub-activities across the remaining seven activities awaits a second external application before being productively deliberated.

### OI-006: Cross-references between specifications
**Surfaced:** Session 001
**Status:** Open
The current specification format does not mandate cross-references between related specifications or links to the provenance that produced them. As the number of specifications grows, navigability may require explicit linking. Deferred until the need arises.

### OI-007: Scaling the open issues format
**Surfaced:** Session 001
**Status:** Open — count rose from 9 to **12** in Session 009 (three new: OI-012 validate.sh hard-coded path; OI-013 non-file external artefacts; OI-014 domain-actor receipt shape variance)
Open issues are currently a single file. After Session 009 the count is 12 open issues. The file remains readable but is approaching the threshold at which a directory-per-issue or category-based layout may warrant consideration. No action this session; monitor. Consider migrating to a directory of individual issue files, or developing a categorization system, when the need arises.

### OI-008: Persisting validation reports
**Surfaced:** Session 002
**Status:** Open
Should the output of `tools/validate.sh` be saved as part of session provenance? Currently the output is ephemeral — run during Read, consumed, not saved. If validation history proves useful for tracking methodology health over time, a future session should design a persistence mechanism. See D-010 for context.

### OI-009: Monitor for drift-to-ritual in multi-agent deliberation
**Surfaced:** Session 003
**Status:** **Monitor — first external artefact validated positively in Session 009.** Conditional escalation from Session 007 D-048 resolved per Session 008 D-052. Session 009's self-work (W2 + W4 spec revisions) passes the G/O/K/S criterion-package on majority reading per Session 009 D-053/D-054/D-055/D-056 Q5 evaluation; three-of-four perspectives graded the core proposals as load-bearing (Skeptic's minority "drop Q1 entirely" position preserved). Continued monitoring via the G/O/K/S criterion-package adopted in Session 007 D-048.2.
Session 003's Skeptic argued that multi-agent deliberation will drift to ritual within five sessions. Session 004's audit of Session 003's pattern application found the Skeptic's demands materially shaped the specification, dissent was preserved, and the pattern was applied to maximally load-bearing work — no drift signal. Sessions 004, 005, 006 audits each found no drift; Sessions 005 and 006 surfaced small brief-priming findings (phrase propagation from briefs quoting prior decisions).

**Session 008 status change (per D-052):**

Session 008 executed the first external application as constrained by D-048.3. D-048.1's conditional state resolves: OI-009 returns to **Monitor** status. D-048.4's methodology-claim-downgrade provision does not activate (was a commitment mechanism for the failure case; not invoked). The Skeptic's Session 007 "OI-009 activated regardless" dissent is preserved but superseded by Session 008's execution. The G/O/K/S criterion-package adopted in Session 007 D-048.2 remains the operational OI-009 criterion for future self-work assessments.

**Session 007 status changes (per D-048):**

- The four-perspective deliberation produced the following criterion-package (disjunctive) for OI-009 assessment going forward. Self-work in any future session is load-bearing iff it satisfies at least one of:
  - **(G)** *Translation-to-external-frame* — the need for the increment can be stated in terms that refer to the methodology's asserted external use, not only in terms of the methodology's self-description [Generalist, Session 007 Q6].
  - **(O)** *Narrows-external-action-decision-space* — the increment removes a concrete blocker to a named next external action [Outsider, Session 007 Q6].
  - **(K)** *External-reader visibility* — the weakness the increment addresses would be visible to a reader outside the workspace reading the specs for the first time [Skeptic, Session 007 Q6].
  - **(S)** *Specific-obstacle resolution* — the increment resolves a specific articulable obstacle that blocks a named next step, where the obstacle was identified in provenance and the next step is concrete, OR closes an open issue whose closure changes what later sessions can do [Steward, Session 007 Q6].
  - Self-work satisfying none of these is ritual-tracking and activates OI-009.

- **Supersession of Session 006's count-based criterion.** Session 006's close introduced "three consecutive self-sessions" as an OI-009 activation signal. Session 007's Skeptic audit (Q1) flagged this as a redefinition without deliberation. Session 007's four-perspective deliberation produced the content-based criterion-package above, which supersedes the count-based criterion. Counts may be a secondary heuristic but are not load-bearing.

- **Session 007's own classification.** Session 007's work is **external-application preparation** (D-044), not self-infrastructure. It satisfies criteria (G), (O), and (S) of the package: the increment's need terminates in the methodology's external use (G); it removes concrete blockers to Session 008's first external application (O); it resolves the selection-mechanism obstacle Session 006 named (S). Session 007 does not activate OI-009 on its own work.

- **Session 008 binding constraint** (per D-048.3): Session 008 is constrained to target ratification and first external application per D-045's Branches A/B/C. Unrelated self-work in Session 008 activates OI-009 hard unless a newly-surfaced, specifically-named blocker is deliberated.

- **Methodology-claim downgrade provision** (per D-048.4, Outsider-unique): if Session 008 does not execute first external application AND does not surface a blocker meeting D-048.3's standard, PROMPT.md's "domain-general" claim is to be downgraded to "promising but unvalidated self-hosting methodology" in Session 009 (the downgrade itself requires deliberation; this is a commitment mechanism, not a preemptive authorisation).

Drift would continue to appear as originally characterised: multi-agent applied to typos, renames, reordering, or decisions with no genuinely articulable alternative positions. The criterion-package above extends this content-based characterisation to include "self-work that satisfies none of (G)/(O)/(K)/(S)."

### OI-010: Cross-model or human participation mechanism
**Surfaced:** Session 003
**Status:** CLOSED in Session 005 (per D-032) — see Resolved Issues table below.
Session 004 produced a concrete specification (in `multi-agent-deliberation.md` v2): two participation shapes (perspective and reviewer), a three-layer recording schema, explicit trigger rules, and closure criteria. Session 005 performed the first operational use: Outsider perspective delivered via `codex exec` to OpenAI GPT-5, recorded per the v2 schema with full D-024 manifest. D-027 set the closure trigger to "first session that performs the first use." Session 005 is that session. OI-010 closed. Narrowing of OI-004 begins (but does not complete) per D-033 — see OI-004 above.

### OI-011: Intra-family model mixing as a deliberation-quality lever
**Surfaced:** Session 004
**Status:** Open
Per D-022, mixing Anthropic models (Opus + Sonnet + Haiku) does **not** constitute cross-model participation for OI-004. But all three Session 004 perspectives noted that intra-family mixing has residual utility — capability stratification (Haiku surfaces what a weak reasoner catches; Opus explores longer tails), cost-scaled deliberation, and validation-band variance. This is a separate concern that should not be conflated with OI-004 progress in future sessions. A future session may deliberate whether to specify guidance for *when* intra-family mixing is worth doing and *how* to record it honestly (`participants_family: mixed-anthropic`) without inadvertently claiming OI-004 movement.

### OI-012: `validate.sh` hard-coded `02-decisions.md` path
**Surfaced:** Session 009 (per D-055; the underlying tooling sub-finding was recorded in Session 008 W2 per D-051)
**Status:** Open — defer; Session 009 explicitly declined a tool fix
`tools/validate.sh` checks 14 and 15 hard-code the path `02-decisions.md` as each session's decisions file. Session 008 surfaced that this creates a silent-bypass hazard if a session numbers other files (e.g., artefacts) into positions that shift the decisions file to `03-` or later. Session 008 worked around this by using a non-numbered filename for the external artefact; Session 009 removed the collision source by moving external artefacts to `applications/` (D-054). The hard-coded path therefore no longer has an active collision pressure. The defect remains available to bite under different future patterns (e.g., a future session wanting variable decisions-file numbering; or a session generating multiple deliberation artefacts that force renumbering). **Re-visit trigger:** a future session needing variable decisions-file numbering, or a second independent concrete collision with the hard-coded path, whichever comes first. The preferred starting point for the future deliberation is the Reviser/Outsider pattern-match proposal (match `[0-9][0-9]-decisions.md` within each session directory; fail if zero or multiple matches) preserved in D-055 Rejected Alternatives.

### OI-013: Non-file external artefacts
**Surfaced:** Session 009 (per D-056 §3; sourced from Skeptic [01c, Q4] and Outsider [01d, Q4])
**Status:** Open — monitor; no pre-specification
The `applications/` directory introduced in Session 009 presumes file-shaped external artefacts (Markdown text, structured files). Future external artefacts that are software implementations, physical objects, running services, or other non-file shapes will strain the current `workspace-structure.md` §applications text. Session 009 records this as a watchpoint rather than pre-specifying placement rules for artefact shapes the methodology has not yet produced. **Activation trigger:** the first external application that produces a non-file-shaped artefact (or a file-plus-non-file hybrid). That session should deliberate extensions to `workspace-structure.md` or a new category of external artefact accordingly; such a deliberation would be D-016_2-triggering (revises workspace-structure.md) but not inherently D-023 unless it also touches the kernel.

### OI-014: Domain-actor receipt shape variance
**Surfaced:** Session 009 (per D-056 §3; sourced from Minimalist [01b, Q4] and Outsider [01d, Meta-note])
**Status:** Open — monitor; kernel §7 Domain validation text (per D-053) uses deliberately broad domain-actor phrasing
The kernel §7 Domain validation text (D-053) uses "domain-actor" phrasing — "the domain-actor who holds the problem the artefact addresses — the user of a sequence, the reader of a specification, the participant in a process, or an equivalent" — deliberately broad enough to cover user, expert, panel, or observational data. Session 008's Validate receipt fit a specific shape: single user, self-reported, timely, timely-relative-to-Session-009-open. Future external artefacts may produce receipts that do not fit a specific-actor-with-specific-problem-timely-report loop (e.g., a document read by many readers over time; a template adopted by a team; a process that cannot be retrospectively evaluated). The kernel text accommodates these shapes abstractly but does not pre-specify how such receipts are procedurally handled (how to record them, how to weight them, what counts as "enough" evidence). **Activation trigger:** the first external application whose domain-validation receipt shape materially differs from Session 008's single-user-self-report pattern. That session should deliberate whether kernel §7 Domain validation needs elaboration (substantive v-bump likely) or whether the broad phrasing already accommodates the new case adequately.

---

## Resolved Issues

| Issue | Resolved | Session | Notes |
|-------|----------|---------|-------|
| OI-003: Automated validation | 2026-04-17 | 002 | Built two-tier validation: `tools/validate.sh` + guided questions. See `specifications/validation-approach.md` and decisions D-010 through D-014. |
| OI-010: Cross-model or human participation mechanism | 2026-04-18 | 005 | Session 004 specified the mechanism (D-021/D-023/D-024). Session 005 performed the first operational use: Outsider perspective (OpenAI GPT-5 via `codex exec`, Shape A per D-021) with full D-024 per-participant manifest. Per D-027, closure trigger was "first session that performs the first use." Session 005 is that session. See D-032. Narrowing of OI-004 begins (but does not complete) per D-033. |
