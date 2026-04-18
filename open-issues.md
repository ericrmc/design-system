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
**Status:** Open — narrowed-pending-sustained-practice after Session 005 (phrased as tally, not endorsement); tally advanced from 1 of 3 to 2 of 3 in Session 006 per D-043; tally **unchanged at 2 of 3** after Session 007 per D-049 (non-Claude participation included but no D-023 trigger fired)
When a single AI agent plays all perspectives, disagreement is simulated. Session 003 built parallel context-isolated Claude subagents as the first real mechanism, closing the single-context simulation gap but leaving the Claude-monoculture gap. Session 004 specified a non-Claude participation mechanism (in `multi-agent-deliberation.md` v2, see D-021/D-023/D-024) but explicitly chose **not** to claim any narrowing of OI-004 (D-025), because no non-Claude participant was in Session 004's deliberation. Narrowing requires operational use.

**Session 006 tally (per D-043):** Two sessions of non-Claude participation had occurred (Sessions 005 and 006, both Outsider perspective via `codex exec` to OpenAI GPT-5; both D-023 required-trigger deliberations).

**Session 007 tally (per D-049):** Session 007 included non-Claude participation (Outsider = OpenAI GPT-5 via `codex exec`, continuing the Sessions 005/006 pattern) with a full D-024 manifest, **but none of Session 007's decisions (D-044 through D-049) triggered any D-023 clause** — no kernel modification, no spec revision, no OI-004 state change. Per the strict v3 spec closure-criterion-2 reading ("at least three required-trigger deliberations"), Session 007's deliberation was not a required-trigger deliberation; the sustained-practice tally does **not** advance. Tally remains at 2 of 3. This is the methodology's **first non-Claude session without a D-023 trigger** and is a novel data pattern. Criterion 3 (recorded impact) gains three new data points from Session 007 (Skeptic+Outsider convergence against pre-use spec changes shaping D-047; Outsider-unique methodology-claim downgrade proposal shaping D-048.4; Outsider's ratification-as-third-path framing informing D-045 Branch B), bringing cumulative criterion-3 data points to nine across three sessions. Criterion 4 (articulation of "substantively different training provenance") remains unmet.

A future session may consider whether criterion 2 should expand to count voluntary non-Claude inclusion (i.e., sessions where non-Claude participation occurs without being D-023-required); Session 007 explicitly considered and rejected opening an OI for this question per the "wait for a concrete pattern" principle (Session 006 D-043 Archivist precedent). If Sessions 008+ accumulate multiple voluntary-inclusion-no-tally-advance instances that feel perverse, the question can be re-opened.

Closure criteria are specified in `multi-agent-deliberation.md` v3's Closure Criteria section (unchanged from v2): (1) participant independence; (2) sustained practice across ≥3 required-trigger deliberations; (3) recorded impact on outcomes; (4) articulated definition of "substantively different training provenance." "Closable" and "closed" remain distinct states; closure requires explicit deliberation by a future session.

### OI-005: Sub-activities and work-type variants
**Surfaced:** Session 001
**Status:** Open
The nine core activities may need sub-activities, and different types of work (research, design decisions, validation, implementation) may warrant different subsets or emphases. To be explored as the methodology is applied to different kinds of work — premature to address until the methodology has been applied to a non-self problem.

### OI-006: Cross-references between specifications
**Surfaced:** Session 001
**Status:** Open
The current specification format does not mandate cross-references between related specifications or links to the provenance that produced them. As the number of specifications grows, navigability may require explicit linking. Deferred until the need arises.

### OI-007: Scaling the open issues format
**Surfaced:** Session 001
**Status:** Open
Open issues are currently a single file. After Session 007 the count remains 9 open issues (no new OIs opened this session; Session 007 considered and rejected opening OI-012 for voluntary-non-Claude-inclusion-tally-handling and OI-013 for the same-voice-on-both-sides structural concern, both per the "wait for a concrete pattern" principle inherited from Session 006 D-043). The file remains readable. Consider migrating to a directory of individual issue files, or developing a categorization system, when the need arises.

### OI-008: Persisting validation reports
**Surfaced:** Session 002
**Status:** Open
Should the output of `tools/validate.sh` be saved as part of session provenance? Currently the output is ephemeral — run during Read, consumed, not saved. If validation history proves useful for tracking methodology health over time, a future session should design a persistence mechanism. See D-010 for context.

### OI-009: Monitor for drift-to-ritual in multi-agent deliberation
**Surfaced:** Session 003
**Status:** **Active warning (conditional)** — escalated in Session 007 per D-048. Continues as monitor if Session 008 executes first external application; activates hard with methodology-claim-downgrade provision if Session 008 does not execute.
Session 003's Skeptic argued that multi-agent deliberation will drift to ritual within five sessions. Session 004's audit of Session 003's pattern application found the Skeptic's demands materially shaped the specification, dissent was preserved, and the pattern was applied to maximally load-bearing work — no drift signal. Sessions 004, 005, 006 audits each found no drift; Sessions 005 and 006 surfaced small brief-priming findings (phrase propagation from briefs quoting prior decisions).

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

---

## Resolved Issues

| Issue | Resolved | Session | Notes |
|-------|----------|---------|-------|
| OI-003: Automated validation | 2026-04-17 | 002 | Built two-tier validation: `tools/validate.sh` + guided questions. See `specifications/validation-approach.md` and decisions D-010 through D-014. |
| OI-010: Cross-model or human participation mechanism | 2026-04-18 | 005 | Session 004 specified the mechanism (D-021/D-023/D-024). Session 005 performed the first operational use: Outsider perspective (OpenAI GPT-5 via `codex exec`, Shape A per D-021) with full D-024 per-participant manifest. Per D-027, closure trigger was "first session that performs the first use." Session 005 is that session. See D-032. Narrowing of OI-004 begins (but does not complete) per D-033. |
