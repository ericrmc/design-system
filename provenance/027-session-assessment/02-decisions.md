---
session: 027
title: Decisions — Folder-naming discipline
date: 2026-04-23
status: complete
---

# Decisions — Session 027

Two decisions recorded.

## D-094: Folder-naming discipline — default is permanent; no rename at close; no retroactive rename

**Triggers met:** [d016_2, d016_3, d016_4]

**Triggers rationale:** d016_2 — this decision produces a minor revision to `workspace-structure.md` §provenance (the revision formalises existing operational behavior and does not introduce new constraint or structural change, judged minor per OI-002 heuristic; minor revisions still trigger d016 because multi-agent-deliberation.md v4 d016_2 text is "creates or substantively revises any specification in `specifications/`" and the triggering event is the deliberation itself, regardless of the revision's minor/substantive outcome — conservative reading). d016_3 — the folder-naming question had at least four namable positions before deliberation (leave as-is; rename forward; rename retroactively; drop the practice entirely). d016_4 — the operator surfaced the observation as a pattern of engine self-observability failure; the load-bearing methodology-level question (Q6 in the deliberation) is whether this class of cross-sectional drift is governable by single-session self-audits, which was answered 3-of-3 by the deliberation.

**Non-Claude participation:** skipped. Reason: d023_* does not fire for this decision (no kernel revision per d023_1; no multi-agent-deliberation.md revision per d023_2; no validation-approach.md Tier 2 revision per d023_3; no OI-004 state change per d023_4). Session 015/016/018/025/026 precedent for single-perspective-or-Claude-only deliberation sessions on narrow-scope questions. The operator's external observation at Session 027 open functioned as the external-pattern-detection input that a non-Claude Outsider would otherwise have provided — the operator is an external pattern-detector with workspace-wide visibility, which was the detection mechanism the deliberation's Q6 converged on. `retry_in_session:` n/a (not a required-trigger decision).

**Decision:**

Session 027 adopts the following folder-naming discipline for `provenance/NNN-title/` directories:

1. **Opening default**: at session open, the provenance folder is created as `NNN-session-assessment` per current engine practice.

2. **Folder name is permanent**: the folder name is not revised at close and is not revised by subsequent sessions. The `NNN-session-assessment` opening default is the permanent folder name for every session created under this discipline.

3. **Discoverability is carried by SESSION-LOG.md**, not by folder names. The SESSION-LOG thin-index entry contains the session's descriptive title; a reader locating session content by topic consults SESSION-LOG, not the folder listing.

4. **No retroactive rename** of Sessions 023/024/025/026. The four folders retain their current `NNN-session-assessment` names as historical witnesses to the period before this discipline was specified. D-017 holds unbroken.

5. **No new close-step obligation.** No new validator check. No new Open Issue opened on this topic.

**Artefact produced**: minor revision to `workspace-structure.md` v4 §provenance (no v-bump — minor per OI-002 heuristic; the revision formalises operational behavior already in practice across Sessions 023-026 and does not introduce structural change). Engine-v4 preserved (amendment is minor; does not meet engine-manifest.md §5 substantive-revision criteria).

**Methodology-level finding recorded**: Session 027's deliberation produced 3-of-3 convergence on the Q6 question — single-session self-audits cannot catch cross-sectional drift in surfaces the audit does not name; the detection mechanism that worked (operator external observation of the workspace as a whole) is load-bearing for this class of drift. This finding is preserved in §Honest notes of `03-close.md` and carried forward as a methodology observation; no specification change encodes it because the Q6 convergence explicitly recommends against adding a new audit mechanism at this scale.

**Minorities preserved (per `multi-agent-deliberation.md` v4 §Synthesis — preserve dissent; activation triggers documented per §Open Extensions precedent)**:

- **§A Discoverer [01b-perspective-discoverer.md, Q1-Q5]**: close-step rename-when-substantive rule in `workspace-structure.md` §provenance, cross-referenced from `prompts/development.md`; scoped retroactive dispensation with closed enumerations of permitted/forbidden edits for Sessions 023/024 (+ 025/026 for symmetry); substantive per OI-002 → engine-v5 bump. **Activation warrant**: if a future workspace reorganisation requires path-string updates inside closed-session folders, the Discoverer closed-enumeration dispensation shape is the preferred template. Separately: if three or more future sessions produce substantive output while retaining the `NNN-session-assessment` folder name (evidence the permanent-default discipline produces the same discoverability regression the operator flagged), the Discoverer close-step rename proposal becomes the preferred revision direction.

- **§B Minimalist [01c-perspective-minimalist.md, Q4]**: change opening default from `NNN-session-assessment` to `NNN-session` (semantically empty) or `NNN-session-NNN` (redundant-stable). **Activation warrant**: if a future session observes confusion caused by the `session-assessment` default name (a future Claude or operator misinterpreting the folder name as a claim about session content beyond "this session performed the Assess activity"), the Minimalist default-change is the preferred revision direction. The revision would be minor per OI-002.

- **§C Archivist [01a-perspective-archivist.md, Q5]**: if any rule is adopted beyond D-094, it belongs only in `prompts/development.md` as advisory guidance, not in `workspace-structure.md` as normative specification. **Activation warrant**: if the D-094 §provenance amendment produces spec-prompt divergence (prompts/development.md guidance diverging from workspace-structure.md specification), the Archivist advisory-placement reframing is the preferred alternative — move the rule out of the spec and into the prompt.

**Rationale for decision (Decide-level summary)**:

The deliberation produced 2-of-3 majorities on both Q1 (do not formalise a new rule) and Q3 (do not retroactively rename). The 3-of-3 Q6 convergence — operator external observation is the detection mechanism; single-session self-audits cannot catch this class of drift — is the deliberation's load-bearing methodology finding. D-094 honours the majority by minimising new surface: the amendment records what the engine already does operationally and specifies that SESSION-LOG carries the discoverability function. Retroactive rename is declined because (i) 2-of-3 perspectives argued against it, (ii) D-017 immutability holds without exception, (iii) the four placeholder-named folders function as legible historical witnesses to the pre-discipline period (Minimalist [01c, Q3]: "historical witnesses to the drift. That is not a cost — that is a feature"). Three minority positions are preserved with activation warrants so the minority proposals remain available for future sessions to adopt if the activation conditions arise.

**Operator pre-session framing honoured**: the operator authorised "produce a minor amendment to `workspace-structure.md` or `prompts/development.md`, and optionally authorise a retroactive rename" at pre-session. D-094 produces the minor amendment (to workspace-structure.md) and declines the optional retroactive rename, consistent with the deliberation's majority direction. The "optionally" framing permits this reading.

**Engine-v consequences**: none. Engine-v4 preserved across Sessions 024/025/026/**027** (five consecutive non-bump sessions since engine-v4 adoption at Session 023). §5.4 Session 022 engine-version-cadence minority continues at activated-not-escalated; R9 automatic escalation trigger aged out at Session 026 close per D-092; §5.4 re-examination at Session 028+ remains on content grounds alone.

**Rejected alternatives** (preserved in full detail as §A/§B/§C minority positions above; summarised here for decision-record discipline):

- **Shape α — Archivist advisory-only** (rejected as full adoption; partially honoured via no-retroactive-rename): add only a single advisory sentence to `prompts/development.md`; no `workspace-structure.md` amendment at all. Rejected because the deliberation's 3-of-3 Q6 convergence warrants recording the engine's disposition on this question somewhere normative, and because the Minimalist structural claim (SESSION-LOG is the authoritative thin-index) is sharper in `workspace-structure.md` than in a prompt. The Archivist concern about spec-prompt divergence is addressed by the amendment's restraint — it specifies what already happens operationally and does not introduce a new obligation.

- **Shape β — Discoverer close-step rename plus retroactive dispensation** (rejected as full adoption; preserved verbatim as Minority §A): adopt a close-step folder-rename rule under substantive revision to `workspace-structure.md` (engine-v5 bump); issue a scoped retroactive dispensation authorising path-string updates inside Sessions 023-026 with closed enumerations. Rejected because 2-of-3 perspectives argued against retroactive action, both citing D-017 as unconditional and the "path-string only" boundary as lexical-not-semantic (Archivist [01a, Q3]) or as a dispensation-precedent (Minimalist [01c, Q3]) that would be invoked for future reorganisations. The closed-enumeration dispensation shape is preserved as Minority §A with an activation warrant for any future session where workspace reorganisation demands path-string updates inside closed-session folders.

- **Minimalist default-name change** `NNN-session-assessment` → `NNN-session` (rejected at this session; preserved as Minority §B): change the opening default to the semantically-empty form. Rejected at Session 027 because (i) the Archivist position that `session-assessment` is semantically grounded in activity 2 of the nine-activity kernel is a positive reason to keep the current default; (ii) changing the default would force Session 015's historical folder into an anomalous state (a retained pre-discipline default that would require an explanatory note); (iii) the operator's observation was about the *permanence* of the drift pattern, not about the default name's semantics — the core issue is resolved by the permanence clause alone. Preserved with activation warrant: if a future session observes confusion caused by the `session-assessment` default, the Minimalist change becomes preferred revision direction.

- **Retroactive rename of Sessions 023/024/025/026** (rejected; preserved under Minority §A activation warrant above): the four folders are retained as legible historical witnesses to the pre-discipline period (Minimalist [01c, Q3]: "historical witnesses to the drift. That is not a cost — that is a feature"). D-017 holds unbroken. Git history points into old paths and commit messages reference them; a retroactive rename would either leave the workspace internally inconsistent (if citations left stale) or require editing closed-session content (which the "path-string only" framing does not cleanly contain per Archivist [01a, Q3]).

- **Opening an OI on folder-naming** (rejected): the Q6 3-of-3 convergence recommends against adding spec surface for this class of concern; OI-007 scaling pressure is cited by all three perspectives. The methodology-level finding is recorded in §Honest notes of `03-close.md` as forward observation rather than as a new tracked OI.

- **New validator check for folder-name-reflects-content** (rejected): all three perspectives explicitly reject this (Archivist [01a, Q5]: the check is aesthetic and cannot be mechanised without false positives/negatives; Discoverer [01b, Q5]: does not propose a validator addition; Minimalist [01c, Q5] + Q6 analysis: the check would either over-block or duplicate the informal convention).

**Remaining open**: whether a future session will adopt an "index audit" altitude (Discoverer [01b, Q6]) or a "periodic open-ended attention" discipline (Archivist [01a, Q6]) for catching cross-sectional drift is deferred. No activation trigger is specified at Session 027; the load-bearing next step is continued operator observation of drift patterns, which does not require new engine infrastructure.

## D-095: OI housekeeping and methodology-finding recognition

**Triggers met:** [none]

**Triggers rationale:** OI state maintenance; no new normative content; no spec revision; no OI-004 state change; no new OI opened; no watchpoint opened. d016_3 does not fire because there is no genuine disagreement on housekeeping state (the OI counts are determined facts at session close).

**Non-Claude participation:** skipped. Reason: d023_* does not fire (no kernel revision, no MAD revision, no validation-approach.md Tier 2 revision, no OI-004 state change). `retry_in_session:` n/a.

**Decision**:

- **OI-002** (substantive vs minor heuristic): new data point. Session 027 classifies its `workspace-structure.md` §provenance amendment as **minor** under OI-002. The amendment adds a clause stating the folder name is permanent (does not introduce structural change; does not change file classes; does not alter top-level directory layout; does not modify the `NNN-title/` naming pattern specified at §Validation item 3). This is the 12th data point in the OI-002 heuristic history. No OI-002 state change.

- **OI-004** (criterion-4 independence): tally unchanged at 8-of-3 required. Session 027 is Claude-only (participants_family: `claude-only`); no non-Claude participation; no voluntary contribution. voluntary:required ratio unchanged at **9:8**. criterion-3 cumulative unchanged at **67**. State 3 (Articulated; awaiting closure-retrospective) unchanged.

- **OI-007** (scaling pressure): active count unchanged at **13**. D-094 honours OI-007 by declining to open any new surface — no new OI, no new validator check, no new close-step obligation, no new spec file. The operator observation that surfaced this work was **external** to the engine's current audit mechanisms, which the deliberation's 3-of-3 Q6 convergence identifies as the load-bearing detection layer for this class of drift. Recording this as forward methodology observation, not as a new OI.

- **OI-015** (laundering-gap enforcement in domain reading): session count unchanged at **6** (Session 024 positive exercise remains last data point). Session 027's operator input was a single observation about folder-naming drift, which is workspace-meta-level, not domain input; OI-015 laundering surface is not exercised this session. No positive or negative exercise count change.

- **OI-018** (revisit engine-manifest.md §5 bump-trigger criteria): unchanged. Open — deferred. R9 automatic escalation trigger aged out at Session 026 close. Session 027 preserved engine-v4 (no bump); §5.4 activated-not-escalated state preserved. Remaining activation triggers: "external-application portability confusion" (unexercised) or operator-directed prospective engagement. Neither fires this session.

- **Methodology-level finding from Session 027 Q6 convergence**: recorded in §Honest notes of `03-close.md` as a forward observation, not as a new OI. The finding is that single-session self-audits (Session N+1 auditing Session N) are structurally unable to surface cross-sectional drift in surfaces the audit prompt does not name, and the operator's external-attention layer is the detection mechanism that caught the folder-name drift. This observation is carried forward for consideration at a future session; if an index-audit session-type (Discoverer [01b, Q6]) or periodic open-ended-attention discipline (Archivist [01a, Q6]) is to be formalised, a subsequent session's deliberation would do that work. Session 027 does not open an OI on this because no activation trigger has been specified for when such a formalisation becomes appropriate — the load-bearing next step is continued operator observation of drift patterns, which does not require spec infrastructure.

- **Minorities from Session 023, Session 024, and Session 027**: all preserved unchanged.
  - §5.1 Splitter A.2 (Session 024): counter at zero.
  - §5.2 Skeptic vindication (Session 023): runway 5-of-5 at Session 027 close **if conditions hold** — see §Validation/§Honest notes in `03-close.md`.
  - §5.3 Pacer aggregate-hard-budget (Session 023): activation conditional on Session 027 close aggregate crossing 100K or >10% single-session growth without compensating restructure — see Validation.
  - §5.4 Session 022 engine-v-cadence: activated-not-escalated; R9 window closed; content-grounds-only at Session 028+.
  - §5.5 tokeniser-drift watch (Session 023): no activation (no single-Read failure).
  - Session 024 A.4 minorities (Splitter, Archivist, Skeptic, Outsider carry-warning): all preserved unchanged.
  - Session 027 new first-class minorities §A (Discoverer close-step), §B (Minimalist default-change), §C (Archivist advisory-placement): all preserved per D-094 with activation warrants.

**Total first-class minorities after Session 027 close**: 12 preserved positions across Sessions 023/024/027 (four from Session 023 §5.1-§5.5 excluding §5.4 which is activated not-minority; five from Session 024; three from Session 027).

**Watchpoints active**:
- WX-22-1 witness-dumping pattern (Session 022): no new data.
- WX-24-1 MAD growth (Session 024): 6,386 at open; held unchanged across five consecutive session opens. Thresholds: 7,000 reconsider A.1; 7,500 R2 conversion condition (i) fires; 8,000 hard-fail.
- WX-24-2 budget-literal drift forward discipline (Session 024): no session 027 edits to exercise.
- WX-24-3 Outsider pre-response workspace exploration pattern (Session 024): stable at n=4; Session 027 non-test (no Outsider convened); pattern held at n=4.

No new watchpoints opened.
