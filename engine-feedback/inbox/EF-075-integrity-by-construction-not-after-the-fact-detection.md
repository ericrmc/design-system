---
id: EF-075-integrity-by-construction-not-after-the-fact-detection
source_workspace_id: selvedge-self-development
source_session: 075
target: methodology
severity: friction
status: new
reported_by: operator
filed_at: 2026-04-26
---

# Integrity-by-construction, not after-the-fact detection

## Operator note (S075 post-close intake)

> "I don't want to lead architecture decisions. I want the system to be aware of its flaws and correct them itself.
>
> In fact, there could be extra validation checks to help surface integrity or quality issues with references. The validation agent, that is now separate from the orchestrator agent, has been consistently raising quality issues about things the lead agent has claimed. In my view these errors shouldn't be allowed to happen at all. The system should not allow for integrity issues, bad references, counting as ceremony, etc."

## Empirical pattern: the (γ) reviewer keeps catching the same failure classes

The operator-direct reframe is empirically supported. Three of the five findings at the S075 (γ) reviewer audit are the same failure classes already caught at S074:

| Class | S074 finding | S075 finding |
|---|---|---|
| **Decisions declare d016_* triggers without `Single-agent reason:` annotation** | F1 (D-288/D-289/D-291) | **F0 (D-293/D-294/D-295/D-296)** |
| **Stale spec text after supersession (line-level)** | F2 (v8 lines 33 + 162) | **F3 (v9 lines 19 + 35 + 342 + digest_emitter.py docstring)** |
| **Stale forward-reference text after supersession (section-level)** | F3 (v8 §(z6) phase-3.1-at-S074 stale text) | **F2 (engine-manifest v15 entry D-NNN placeholders + Path-L/Path-AS drift)** |
| Validator-spec mechanism gap | F4 (check 27 narrower than spec audit shape; deferred S075+) | (CLOSED at S075 D-295) |
| Close overstates substrate evidence | (none) | **F4 (close §10 sub-section 14 claims substrate_calls records that don't exist)** |
| State surfaces lag narrative | (none) | **F1 (validation-debt + engine-feedback INDEX disposition extensions claimed but not committed pre-audit)** |

The audit-correct-recur loop is alive: orchestrator makes the same class of mistake, reviewer catches it, orchestrator point-fixes at close commit, structural mechanism doesn't change, **next session the same class recurs**. The (γ) reviewer is doing its job. The structural feedback loop into prevention is missing.

## Diagnosis

Every recurring finding class is **mechanically preventable at write-time** with the substrate the workspace already exposes:

| Failure class | Mechanical prevention |
|---|---|
| D-NNN / S-NNN / v-N placeholders surviving to commit | Pre-commit grep for placeholder patterns; FAIL. |
| `Single-agent reason:` missing on d016_* trigger declarations | Already in check 14 schema; promote to pre-commit gate, not post-commit check. |
| Stale wording about a mechanism (e.g., "PreToolUse + PostToolUse" when config is PostToolUse-only) | Cross-file consistency check between `.claude/settings.json` and prose claims about it. |
| References to superseded decisions | `resolve_id` verification at write-time; if decision is superseded and not flagged, FAIL. |
| §10.4-M* / §(zN) cross-spec references | Substrate-resolved at write-time. |
| §1e file-edit claims vs actual git diff | If the close §1e claims file X was edited this session, git's modification list must include X. |
| Smoke-test substrate evidence claims vs actual digest content | If the close claims the digest contains substrate_calls records, the digest must contain them; substrate counts; if claim != count, FAIL. |
| State surfaces (validation-debt, engine-feedback INDEX) lag narrative | If the close narrates that file X was updated, file X's `updated-by-session:` frontmatter must equal current session. |

These are not judgment-class errors. They are mechanical-drift errors that the substrate is fully capable of catching at write-time but currently catches only at audit-time, where the cost of correction is higher and the recurrence is unprevented.

## Counting-as-ceremony

The operator's "counting as ceremony" critique points at a related but distinct class. Examples in S075's close narrative:

- `forty-seventh-consecutive housekeeping [none]-trigger pattern`
- `D-129 + D-138 twenty-ninth-consecutive clean exercises`
- `WX-28-1 forty-fifth close-rotation S069 OUT S075 IN`
- `WX-24-1 MAD v4 forty-eighth-session no-growth streak preserved (33-session run from S042 reset)`
- `periphrastic-form discipline at n=8 (S068+S069+S070+S071+S072+S073+S074+S075)`
- `§5.6 GPT-family-concentration window-ii advances ten-consecutive → eleven-consecutive`

Each had a substantive purpose at origin (pattern detection, drift observation). At n=2-5 they were informative. At n=20+ they are ritual. The forty-seventh-consecutive [none] housekeeping pattern carries no information — it just means nothing has changed. **The act of tracking it manually at every close is what makes it ceremonial.**

If these counters were substrate-derived rather than orchestrator-claimed:

- They could not be miscounted (no F0/F2-class ceremonial-counter-error possible).
- They would only require attention when they CHANGE (the streak breaks).
- They would stop displacing substantive close-narrative content.
- They would stop being ceremony.

## Architectural direction

The operator was explicit about not wanting to lead architecture decisions. Recording candidate directions for future-session triage; not pre-ratifying:

**Direction 1: Pre-commit validation gates**. validate.sh today runs as post-hoc inspection. It should also run at pre-commit with a stricter FAIL bar for the mechanical-drift classes the (γ) reviewer has empirically demonstrated the orchestrator cannot prevent on its own. Gates are operator-discretionary at workspace level (`.git/hooks/pre-commit` invoking validate.sh strict mode); engine-definition specifies the strict-mode check set.

**Direction 2: Auto-computed substrate-derived state-tracking**. Instead of orchestrator-claimed counters in close narrative, the close template carries `{{counter:housekeeping_none}}-th-consecutive`-style placeholders that substrate fills at commit time. Counters that are derived cannot be wrong; counters surface only when they change.

**Direction 3: Recurring-finding-class auto-promotion**. When the (γ) reviewer catches a finding class N times across M sessions (e.g., n=2 across 2 consecutive sessions), the engine promotes that class into a structural check at the next engine-v bump. F0+F2+F3 in S075 (which are S074-recurrences) should become checks 30+31+32 automatically. The audit-correct loop tightens itself; the reviewer's bandwidth shifts toward judgment-class findings rather than mechanical-drift findings.

**Direction 4: Reference auto-completion**. Instead of writing `D-NNN` placeholders and hoping to fill them in later, the orchestrator declares "this is decision N+1 in this session" and the system assigns the number at commit-time. Similar for v-N spec versions, S-NNN session references.

**Direction 5: Cross-file consistency checks**. Pre-commit checks that verify spec text matches actual configuration (e.g., "PreToolUse + PostToolUse" wording in spec must match `.claude/settings.json` hooks), and that file-edit claims in close §1e match `git diff --name-only` for the close commit.

These directions are interrelated; some imply others. Path-AS Shape-1 phase-1 design-space scope at future session is the natural shape for working through cross-product implementation candidates + per-direction dispositions per §10.4-M35 staging-must-be-per-direction discipline.

## Cross-linkage

- **§10.4-M23 P3 substrate-led reviewer-judged frame** (S064; substantively adopted as v7 audit-shape direction) — this record is a direct exercise of M23's reopen warrant (a) reviewer-judges-without-substrate-input, applied at the orchestrator side rather than the reviewer side.
- **EF-075-reviewer-side-substrate-use** (sibling intake; same operator-conversation) — orthogonal but related: that record is about reviewer-side substrate use; this record is about orchestrator-side write-time-prevention. Together they cover both halves of the substrate's underuse.
- **EF-075-reviewer-cost-not-optimization-target** (sibling intake; same operator-conversation) — supports this record's directions: cost is not a blocker for adding pre-commit gates or substrate-querying overhead.
- **EF-068-read-write-rebalance** (S068 triaged; standing operator-discretionary surface) — Direction 4 (reduce forced-write rate; housekeeping → records-substrate frontmatter; trigger-based housekeeping) overlaps with this record's Direction 2 (auto-computed counters); future Path-AS scope might bundle.
- **EF-058-tier-2-validation-discipline-by-distinct-agent** (S058 resolved at S062 D-221; engine-v11 ratified) — the (γ) reviewer mechanism that produces the findings this record observes recurring; the present record is essentially "EF-058 resolution gave us detection; we now need the prevention complement."
- **§10.4-M22 P1 two-session-arc minority** — every (γ) reviewer audit finding represents a candidate for two-session-arc substantive engagement; the current pattern (point-fix at close commit, no structural feedback) is the engine equivalent of "synthesizer-framing absorption" at the methodology-self-improvement level.

## Triage notes

Operator-surfaced post-session intake at S075 close. **Tenth-of-record operator-surfaced intake** (after EF-054 + EF-055 + EF-058×3 + EF-067 + EF-068×2 + EF-073 + EF-075-reviewer-side-substrate-use + EF-075-reviewer-cost-not-optimization-target). Friction-class severity (operator framed as substantive concern about engine's self-correction discipline; not blocker but not pure observation either). **Operator-direct meta-level reframe**: the operator is not directing what the engine should do; the operator is observing that the engine should already be doing this, and noting that future-session triage of this record is itself the test of whether the engine has the self-correction capacity the methodology claims.

The natural triage scope at S076+ is Path-AS Shape-1 phase-1 design-space (per S057 + S061 + S070 + S072 precedent). However, **the meta-irony is acute**: deferring this record to "future Path-AS phase-1 → phase-2 MAD → phase-3 implementation" is itself the recurring pattern the operator is critiquing. If the engine's response to "you are not preventing your own recurring failures" is "we will deliberate at length about this in 3-4 future sessions", the operator's diagnosis is empirically vindicated. A more honest near-term shape would be: pick 1-2 high-leverage pre-commit gates (D-NNN placeholder ban + §1e-claim-vs-git-diff check are both small) and implement at S076 alongside the planned phase-3.2 + VD-003 review work, treating this record as activated-not-deferred.

Disposition selection at future-session triage; not pre-ratifying at intake. The selection itself is observable evidence about the engine's self-correction discipline.
