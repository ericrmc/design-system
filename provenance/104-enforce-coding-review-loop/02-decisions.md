---
session: 104
title: enforce-coding-review-loop — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Adopt sessions.kind as the close-time anchor for coding review loop enforcement; default coding, immutable post-open.

**Kind:** substantive.  **Outcome:** adopt process_rule `sessions.kind classification at open`.

**Why.**

- (deliberation) P-1 and P-2 converge on need for structural close-gate; declaration is the anchor available without working-tree visibility (OI-083-001).
- (constraint) Substrate has no file-tracking surface; passive detection of code-touch is impossible without a separate artifact-tracking mechanism out of scope here.
- (spec_clause) Methodology already names the predicate: a coding session that closes without a clean reviewer pass or halted-state record is invalid.

**Effects.**

- modifies sessions table gains kind column; session-open accepts optional kind field.
- creates Trigger pattern mirroring T-23 enforces immutability of sessions.kind post-open.

**Rejected alternatives.**

- **R-1.1.** Anchor enforcement on recorded change facts via session_artifact_changes plus manifest-hash sealing per P-2.
  - (too_large_for_session) Requires substrate-side file-tracking surface that does not exist; multiplies scope beyond what OI-083-001 frames as MEDIUM and post-release-gate.
- **R-1.2.** Make every session a coding session by default with no override mechanism.
  - (inferior_tradeoff) Forces the loop on pure-spec or meta sessions where it is fatigue-inducing ceremony with no behavioral surface to review.

## D-2. Add review_passes table as terminal-pass artefact distinct from review_findings; submit via review-pass with head_sha staleness assertion.

**Kind:** substantive.  **Outcome:** adopt process_rule `review_passes terminal-pass artefact`.

**Why.**

- (deliberation) Both perspectives agree review_passes must be distinct from review_findings; findings are per-iteration line items, a pass is the terminal outcome.
- (deliberation) P-2 staleness-protection insight: review-pass row carries an operator-asserted head_sha so clean review plus late mutation is detectable on audit.
- (prior_decision) Methodology coding review loop requires clean reviewer pass or halted record at close; the substrate now has a typed row to refuse close against.

**Effects.**

- creates review_passes table with iteration, outcome, head_sha, summary fields.
- creates submit review-pass handler producing RP-S<wno>-<iter> alias.

**Rejected alternatives.**

- **R-2.1.** Reuse review_findings table with a new severity value clean-pass for terminal attestation.
  - (breaks_invariant) Conflates per-iteration findings with terminal pass; queries on findings.severity would no longer mean what they currently mean.
- **R-2.2.** Require manifest_hash not head_sha; substrate computes the manifest from recorded artifact changes.
  - (too_large_for_session) Manifest computation requires a session_artifact_changes table the substrate does not yet have; head_sha is thinner and adoptable now.

## D-3. Admit halted as a sessions.status value; widen T-11, T-18, T-19, T-20 to admit halted as a distinct close-path with its own gating semantics.

**Kind:** substantive.  **Outcome:** adopt process_rule `sessions.status halted`.

**Why.**

- (deliberation) P-2 caveat: T-20 currently makes halt impossible without faking adjudication on unresolved findings; halted must be a distinct close-path.
- (spec_clause) Methodology says a halted session is not a normal close and the next session reopens the work; status must be observable on the session row.

**Effects.**

- modifies sessions.status CHECK widened to admit halted in addition to open and closed.
- modifies T-11, T-18, T-19, T-20 admit halted close-path with distinct gates.
- creates Halt requires review_pass with outcome nonconverged plus a referenced halt-issue.

**Rejected alternatives.**

- **R-3.1.** Encode halt as a flag on review_pass with sessions.status remaining closed.
  - (inferior_tradeoff) Buries halt state in a child table; a session-row read alone cannot tell whether close was normal or halted, defeating the methodology's reopen-the-work signal.

## D-4. Add T-XX (next free slot) refusing close on coding session without terminal review_pass; admit halted close path on review_pass nonconverged plus halt-issue.

**Kind:** substantive.  **Outcome:** adopt process_rule `T-XX coding session close gate`.

**Why.**

- (prior_decision) DV-S104-1 declares classification anchor; DV-S104-2 ships review_passes; this trigger is what makes the close-gate structural rather than advisory.
- (spec_clause) Methodology states: coding session that closes without a clean reviewer pass or halted-state record is invalid; this trigger is the structural enforcement.

**Effects.**

- creates T-XX refuses close on kind=coding without review_pass outcome=clean.
- modifies T-20 narrowed to fire only on closed path; halted path is governed by T-XX.

**Rejected alternatives.**

- **R-4.1.** Keep T-20 fully blocking and require all findings adjudicated even in halt path.
  - (breaks_invariant) Forces implementer to fake adjudication on findings the loop never resolved; defeats the methodology's halted-state honesty.

## D-5. Open follow-up issue tracking P-2 manifest-hash sealing alternative as forward direction if declaration-based enforcement proves operator-policed in practice.

**Kind:** procedural.  **Outcome:** defer open_question `manifest-hash sealing forward direction`.

**Why.**

- (deliberation) P-2 minority position preserved (synthesis M-1): recorded-change-fact anchor is structurally stronger than declaration; defer until empirical signal warrants escalation.

**Effects.**

- opens_issue OI-S104-manifest-hash-sealing as forward direction.

## D-6. Open follow-up issue: decision_effects.effect_kind admits creates and modifies but not deletes, despite methodology saying delete-executable triggers the loop.

**Kind:** procedural.  **Outcome:** defer open_question `decision_effects deletes effect_kind gap`.

**Why.**

- (deliberation) P-2 surfaced this gap as probably-missed; out of scope for OI-083-001 enforcement work but worth tracking.

**Effects.**

- opens_issue OI-S104-deletes-effect-kind gap in decision_effects enum.

## D-7. Encode halted state via review_passes.outcome=nonconverged rather than admitting halted as sessions.status value; defer status-value admission to a future session.

**Kind:** calibration.  **Outcome:** supersede process_rule `DV-S104-3 halted status encoding`.

**Why.**

- (engine_feedback) Producing the change revealed the cost: SQLite column-level CHECK cannot be widened in-place; rebuilding sessions risks orphaning the eight triggers and many FK referrers.
- (constraint) Migration 016 explicitly noted table-rebuild on heavily-FKd tables is the trap calibrated table-rebuild fell into; sessions is the most heavily-FKd table in the schema.
- (prior_decision) OI-083-001 is MEDIUM and post-release-gate; the lighter encoding satisfies the issue title (substrate refuses close-without-evidence) without paying rebuild cost.

**Effects.**

- supersedes DV-S104-3 halted-as-status admission deferred.
- modifies Halt encoded as review_pass row with outcome=nonconverged plus halt_issue_id.
- opens_issue OI-S104-3 to track halted-as-status-value rebuild when warranted.

**Rejected alternatives.**

- **R-7.1.** Pay the table-rebuild cost now and admit halted as sessions.status value.
  - (too_large_for_session) Sessions table has eight triggers and dozens of FK referrers; rebuild is its own session-sized work and unjustified for a MEDIUM post-release-gate issue.
- **R-7.2.** Add sessions.is_halted boolean column alongside status.
  - (inferior_tradeoff) Two columns expressing one enum; queries become awkward (status=closed AND is_halted=1) without gaining the single-column read property the rebuild would have.
