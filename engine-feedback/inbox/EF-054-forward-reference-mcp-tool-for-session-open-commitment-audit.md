---
feedback_id: EF-054-forward-reference-mcp-tool-for-session-open-commitment-audit
source_workspace_id: selvedge-self-development
source_session: 053
created_at: 2026-04-25
reported_by: operator
target: engine-adjacent
target_files:
  - tools/retrieval_server.py
  - specifications/retrieval-contract.md
  - prompts/development.md
severity: friction
status: inbox
---

# EF-054 — Forward-reference MCP tool for session-open commitment audit

## Observation

Forward-commitments landing at a session — preserved-minority activation warrants, watchpoint windows, "evaluate at S{NNN}" decisions, scheduled-MAD adoption sessions, criterion-firing checkpoints, "carry-forward to S{NNN}" notes — are recorded across prior sessions' provenance and must be re-discovered at every session open. The current discipline is "read prior `03-close.md` §7 next-session-recommendation sections," which relays forward only what the closing session's Case Steward chose to surface — selection-bias prone.

Empirical demonstration at S053 close (post-session audit): the workspace substrate contains a line-precise record of every `S053`-keyed forward-reference via the `identifiers` table:

```
SELECT source_path, line, context_snippet
FROM identifiers
WHERE id_text = 'S053'
ORDER BY source_path, line;
```

Returns **19 records, all from `provenance/050-session/`** — the WX-50-1 phase-2 gate setup. Of those 19, **S053 only addressed ~17 in close**: two P1-raw-perspective commitments (Criterion 3 rebuild-latency p95 ≤ 500ms across 10 rebuilds; Criterion 6 adoption-sunset condition on two-consecutive-session check-24-failure) were not relayed forward through S050 close §7 → S051 close §7 → S052 close §7, and consequently S053 did not evaluate them. Substrate has the data; agents miss it because the workflow shape doesn't include a substrate query at session open.

`search()` (BM25) is a weaker tool for this purpose — it ranks documents not lines, returns small result counts, and a query like `search("S053")` at S053 open returned ~1 high-ranked result vs. the 19 line-precise hits the `identifiers` table contains. The data is structured and line-keyed; structured retrieval is the right mechanism, not full-text search.

## Why It Matters

1. **Forward-commitments are load-bearing methodology mechanism.** The engine relies on preserved-minority activation warrants firing at the right session; on watchpoint windows being evaluated cleanly; on scheduled MADs running at their scheduled session; on carry-forwards being acted upon. Selection-bias in relay (Case Steward chooses what to forward; later Case Stewards inherit only the relayed subset) silently erodes commitment-fidelity over multi-session windows.

2. **Substrate phase-1 data is sufficient for the audit; the MCP surface is not.** The `identifiers` table is line-keyed and indexed at every session open per `retrieval-contract.md` v1 §4. The contract's `resolve_id` tool returns only the *first* occurrence per §2.2; the contract's `search` tool returns BM25-ranked documents per §2.1. Neither tool returns *all* occurrences of an identifier as a structured list — which is exactly what session-open forward-commitment audit requires.

3. **WX-50-1 phase-2 gate organic-use case missed.** This need would have advanced phase-2 gate Condition 2 (structured-filter or graph-traversal fallback) during the S050–S053 observation window if the gap had been recognised earlier. Recording it now as forward observation does not retroactively fire the gate, but does inform phase-2 deliberation when it next happens.

4. **Read-discipline shape question.** `prompts/development.md` §How to operate currently directs agents to read every prior `03-close.md` in the retention window — but it does not direct agents to *query the substrate for what was addressed to the current session*. The substrate's value at phase-1 is partly diagnostic (what does the index contain about *this* session?) and that diagnostic is not currently invoked.

## Suggested Change

Three candidate MCP feature additions (non-exclusive). Each is additive to the existing tool surface; none require contract revision per `retrieval-contract.md` v1 §2 (the contract names `search` + `resolve_id` as required minimum at phase-1; additional tools are permitted).

### Direction A — `forward_references` MCP tool (phase-1-compatible; minor)

Add a new MCP tool to `tools/retrieval_server.py`:

```
forward_references(target: str) -> list[{path: str, line: int, context: str, kind: str}]
```

**Semantics**:
- Returns *all* occurrences of `target` in the `identifiers` table (NOT just the first per `resolve_id` semantics; NOT BM25-ranked per `search` semantics).
- Sorted by `source_path` then `line` for deterministic output.
- `kind` propagated from the existing `identifiers.id_kind` column (decision / minority / watchpoint / session / engine-version / feedback / trigger / other).
- For target `S053`: returns the 19 records demonstrated above, line-precise.
- For target `WX-50-1`: returns every line-precise reference to the watchpoint across the corpus.
- For target `D-172`: returns every line-precise citation of the engine-v9 decision.
- Returns empty list (not error) if target is unindexed.

**Implementation cost**: minor extension to `tools/retrieval_server.py` (new `@app.tool()` decorator + ~15 LOC). No schema change. No index-build change. No contract amendment (additive).

**Classification at adoption**: minor per OI-002 per the 7-precedent bug-fix-style + extension chain (S022/S030/S033/S040/S046/S051/S052/S053 EF-053-direction-A-candidate). No engine-v bump.

### Direction B — `commitments_landing_at(session)` MCP tool (phase-1.5; minor-substantive)

Add a semantic-aware variant:

```
commitments_landing_at(session: int) -> list[{path: str, line: int, context: str, kind: str, commitment_type: str}]
```

**Semantics**: same as Direction A's `forward_references(f'S{session:03d}')`, plus an additional `commitment_type` field derived by lightweight pattern matching on the `context_snippet`:
- `scheduled_mad` if context contains "scheduled" + "MAD" / "deliberation"
- `evaluation_window` if context contains "evaluate at" / "evaluation continues"
- `criterion_firing` if context contains "Criterion" + numeric
- `carry_forward` if context contains "carry-forward" / "deferred to"
- `watchpoint_window` if context contains "WX-" + window
- `other` otherwise

**Implementation cost**: Direction A + ~30 LOC of regex-based classification at MCP-call time (or pre-computed at index-build time and stored as a new `identifiers.commitment_type` column — modest schema addition gated on operator preference).

**Classification at adoption**: minor if pure server-side classification; substantive if schema column added (new identifiers field is contract-relevant).

### Direction C — `forward_commitments:` frontmatter + `list_commitments_at(session)` (phase-2; substantive)

Adopt a structured-frontmatter convention on `03-close.md` files:

```yaml
---
session: 053
title: ...
date: 2026-04-25
status: complete
forward_commitments:
  - target_session: 054
    topic: "EF-053 triage"
    location: "§7"
    type: carry_forward
  - target_session: 054
    topic: "EF-054 triage"
    location: "§7"
    type: carry_forward
  - target_window: [055, 060]
    topic: "engine-v9 preservation depth observation"
    location: "§3"
    type: observation_window
---
```

The substrate's `frontmatter_kv` table (deferred to phase-2 per S050 D-171) indexes these structured fields; MCP tool `list_commitments_at(session)` returns deterministic records.

**Implementation cost**: substantial. Requires `frontmatter_kv` table (phase-2 candidate); requires write-discipline convention adoption (close-file authors must populate `forward_commitments:` correctly); requires backfill question for past closes (skip / document-only / partial).

**Classification at adoption**: substantive. Adds a frontmatter field to engine-definition close-file shape; touches `prompts/development.md` §Close obligation; possible engine-v bump.

### Most likely path

**Direction A first** as a minor engine-adjacent extension. Concrete, narrow, additive, no contract revision. Demonstrates the tool's value via S054+ session-open audit. If Direction A is in routine use after several sessions and forward-commitment-fidelity demonstrably improves, Direction B becomes a natural upgrade. Direction C is the long-horizon target if the substrate eventually moves toward structured-artefact framings (cf. §10.4-M10 Substrate-N2 minority).

`prompts/development.md` §How to operate amendment paired with Direction A (minor documentary): add a sentence directing agents to call `forward_references(f'S{current_session:03d}')` at session open as part of the Read activity. This makes the tool's existence operationally visible without forcing it (agents using Read alone still satisfy the minimum read-contract).

## Evidence

- S053 close §6: documented `tool_calls_by_type: {search: 4, resolve_id: 8}` due-diligence queries; note that none of these used `identifiers` table directly because there is no MCP surface to do so — they used `resolve_id` (first-occurrence) and `search` (document-ranked) as the contract permits.
- S053 post-session operator question demonstrating the gap: "Can you execute a search for something like 'S054' and see all the decisions or watchpoints tied to it? Should that be something done at the start of a session?"
- Empirical demonstration at S053 post-session: `SELECT * FROM identifiers WHERE id_text='S053'` returned 19 line-precise hits all in `provenance/050-session/`; `search('S054')` returned 1 BM25-ranked hit. Direct SQL is operationally adequate; MCP surface is not.
- Two S053-relayed commitments missed by the close-narrative-only relay chain (S050 → S051 → S052 → S053): P1 §452 Criterion 2 (validator check 24 first-firing-session); P1 §454 Criterion 3 (rebuild latency p95 ≤ 500 ms across 10 rebuilds by S053 close); P1 §460 Criterion 6 (adoption-sunset two-consecutive-session check-24-failure). S053 did not measure rebuild latency, did not test check 24 (it's deferred to phase-2 anyway per D-171), and did not evaluate adoption-sunset. Whether these would have changed S053's substantive outcome is a separate question; the gap is in the *surfacing* mechanism not the outcomes.

## Application-Scope Disposition

Recorded as inbox intake at S053 close. No triage at S053 (Path A Watch session; intake is permitted but resolution requires deliberation or implementation work that Path A does not include).

Triage scheduled S054+. Most likely shape: Direction A is implemented as a minor engine-adjacent extension, paired with a minor documentary update to `prompts/development.md` §How to operate naming the new tool in the Read-activity step. Path T+L bundled label (S052 first-instance) reifies at n=2 if S054 adopts this pattern.

If S054 also triages EF-053 in the same session, it would bundle EF-053 + EF-054 in a Path T++ or Path T+L+L shape — first instance of multi-intake same-session resolution. Operator discretion at triage.

Engine-v impact at triage: minor if Direction A only (no engine-v bump); substantive if Direction C is adopted alone (engine-v bump candidate). Direction B is borderline (depends on schema decision).
