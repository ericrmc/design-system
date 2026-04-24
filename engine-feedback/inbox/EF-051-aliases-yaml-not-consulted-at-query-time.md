---
feedback_id: EF-051-aliases-yaml-not-consulted-at-query-time
source_workspace_id: selvedge-self-development
source_session: 051
created_at: 2026-04-25T00:00:00Z
reported_by: application-agent
target: engine-adjacent
target_files:
  - tools/build_retrieval_index.py
  - tools/retrieval_server.py
  - specifications/retrieval-contract.md
  - specifications/aliases.yaml
severity: friction
status: inbox
---

## Observation

S051 smoke-tested the S050-built retrieval substrate per S050 close §8 honest-limit ("S051 open should exercise the substrate as its first substantive read operation and record any defects as engine-feedback"). The primary paths work:

- `search("retrieval contract", k=3)` returns `specifications/retrieval-contract.md` as one of the top results.
- `resolve_id("§10.4-M5")` returns canonical `§10.4-M5` at `specifications/retrieval-contract.md` line 40.
- `resolve_id("D-172")` returns canonical `D-172` at `specifications/engine-manifest.md` line 23.
- `resolve_id("NONEXISTENT-999")` returns `None` (no raise), per §2.2 "Never raises on unknown alias".

One defect surfaced: **`resolve_id("M5")` returns `None`** despite `specifications/aliases.yaml` carrying a seed entry (schema_version 1) declaring `canonical: "§10.4-M5"` with `aliases: ["M5", "Reviser OI-tag-only", "§10.4-minority-5"]`.

## Why It Matters

Per `specifications/retrieval-contract.md` v1 §2.2 (adopted S050 D-170 + D-172 as engine-v9 contract):

> - If `alias` matches an `aliases[]` entry in `specifications/aliases.yaml`, resolves to the corresponding canonical.

The current engine-adjacent implementation does NOT fulfill this clause for any seed alias. Two implementation layers fail this contract:

**Layer 1 — `tools/build_retrieval_index.py` `load_aliases()` (lines 128–240).** The function loads `aliases.yaml` entries then applies them via:

```python
cur.execute(
    "UPDATE identifiers SET canonical = ? WHERE id_text = ?",
    (canonical, alias),
)
```

This only remaps identifiers whose `id_text` literally matched one of the `ID_PATTERNS` regexes at extraction time. An alias like `"M5"` by itself never matches any ID_PATTERNS regex (not `D-NNN`, not `OI-NNN`, not `§N(.N)*(-MN)?`, not `WX-N-N`, not `S\d{3}`, not `engine-vN`, not `EF-NNN-...`, not `d01N_N`). Therefore no `identifiers` row ever has `id_text = 'M5'` to be remapped. The alias is effectively inert at index-build time.

**Layer 2 — `tools/retrieval_server.py` `resolve_id()` (lines 169–229).** None of the three resolution strategies consults `aliases.yaml`:
- Strategy 1: direct canonical lookup in `identifiers` table.
- Strategy 2: `id_text` lookup in `identifiers` table.
- Strategy 3: `ID_LIKE_RE` pattern-matched LIKE prefix lookup.

At query time the aliases file is never read.

**Cumulative consequence**: of the 8 seed entries in `specifications/aliases.yaml` (schema_version 1), **0 resolve to their canonicals** via `resolve_id()`. Every declared non-ID-pattern alias (`"M5"`, `"Reviser OI-tag-only"`, `"Skeptic-preserver premature-feedback-pathway"`, `"Decision 157"`, `"the S049 scope-revision decision"`, `"operator scope revision S049"`, `"Decision 163"`, `"S050 Halt-1 ratifications"`, `"Decision 172"`, `"retrieval-contract v1 adoption"`, `"engine-v9 bump"`, `"OI 19"`, `"Path-selection work-channel and warrant-surface diversity"`, `"retrieval-substrate-use recording"`, `"phase-2 gate"`, `"WX 50-1"`, `"EF-047 retrieval"`, `"retrieval-discipline-and-text-system-scaling-ceiling"`) is dead-letter.

## Suggested Change

Two independent repair directions; either or both may be adopted:

### Direction A — Index-time reverse-remap (modify `build_retrieval_index.py`)

Instead of (or in addition to) remapping existing identifier rows, **insert synthetic identifier rows** for each alias pointing to the canonical's declared location. Concretely: for each `(alias, canonical, kind)` tuple from `aliases.yaml`, after main indexing, look up the canonical's first occurrence row in `identifiers`, then INSERT a new row with `id_text = alias` and `canonical = <resolved canonical>` pointing to the same `source_path + line`. This preserves the existing read-model and makes Strategy 2 (`id_text` lookup) succeed at query time.

### Direction B — Query-time aliases consultation (modify `retrieval_server.py`)

Load `specifications/aliases.yaml` once at server startup into a dict `{alias: canonical}`. In `resolve_id()`, add a Strategy 1.5 between Strategy 1 (canonical direct lookup) and Strategy 2 (id_text lookup): if `alias` is a key in the aliases dict, recursively look up the resolved `canonical` via Strategy 1. This makes the aliases.yaml file authoritative at query time without requiring a reindex when aliases.yaml changes.

Either direction fulfills §2.2. Direction A is more consistent with the existing "index is the read model" framing; Direction B is more consistent with "aliases.yaml is the authoritative alias vocabulary, independent of index build".

## Evidence

Smoke-test transcript at `provenance/051-session/03-close.md` §6 (WX-50-1 retrieval substrate use) records the test invocations and results. Key evidence:

- `resolve_id("§10.4-M5")`: match at `specifications/retrieval-contract.md:40` ✓
- `resolve_id("D-172")`: match at `specifications/engine-manifest.md:23` ✓
- `resolve_id("M5")`: None ✗
- Direct SQL `SELECT * FROM identifiers WHERE id_text = 'M5'`: 0 rows (confirms the indexer never inserted the alias as a row).

The implementation files involved (from the S050 commits):
- `tools/build_retrieval_index.py` lines 128–147 (`load_aliases`), 235–240 (alias application loop).
- `tools/retrieval_server.py` lines 169–229 (`resolve_id`).
- `specifications/retrieval-contract.md` v1 §2.2 (contract clause).
- `specifications/aliases.yaml` (seed entries).

## Application-Scope Disposition

N/A — self-dev-originated feedback. Placed directly in inbox per S048 precedent (self-dev-originated records are placed directly in inbox with `source_workspace_id: selvedge-self-development` rather than fabricating an external-workspace outbox routing).

The defect is engine-adjacent (implementation-level), not engine-definition (contract-level) — the contract `specifications/retrieval-contract.md` v1 §2.2 is correct; the implementation does not fulfill it. Triage should consider whether this is a pure implementation fix (Direction A and/or B above) or whether §2.2 should be narrowed to describe the current implementation's actual semantics.

## Triage disposition recommendation

- **Classification**: implementation-level, engine-adjacent.
- **Severity**: friction (substrate partially unfulfilled; primary ID resolution works).
- **Proposed session**: S052 or later — single-orchestrator minor-amendment Path L. Not MAD-required (no kernel amendment; no spec revision beyond a possible §Honest-limit clarification in `retrieval-contract.md` if the contract is narrowed instead of the implementation fixed).
- **Engine-v impact**: minor per OI-002 if implementation fix only; no engine-v bump. If §2.2 is substantively narrowed, engine-v bump candidate.
- **Bundled-candidate status**: may be bundled with next substrate work (e.g., substrate first real use from S051+ onwards exposes further defects); or addressed standalone.
