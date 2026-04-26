# Session Records — Index

Thin pointer-only index per `specifications/records-contract.md` v1 §2.2. Each row points at a structured source record at `records/sessions/S<NNN>.md`; canonical session-close detail lives at `provenance/<NNN>-session/03-close.md` per the `anchor_close` field.

This file is default-read surface per `specifications/read-contract.md` v6 §1 item 5 (replacing the pre-v6 SESSION-LOG.md). It must remain under the per-file budget in `read-contract.md` §2.

Authority discipline: source record (frontmatter) > index row. Validator check 25 verifies index-row-record consistency; on mismatch, the record wins.

Pre-engine-v10 SESSION-LOG.md preserved verbatim as archive-pack at `provenance/058-session/archive/pre-records-SESSION-LOG/` per `read-contract.md` v6 §4-§7 archive-pack discipline.

| ID | Status | Title | Source record | Witness/path | Anchor session | Last status event |
|----|--------|-------|---------------|--------------|----------------|-------------------|
| [S001](S001.md) | closed | Genesis | S001.md | provenance/001-genesis/03-close.md | 1 | closed S001 |
| [S002](S002.md) | closed | Self-Validation | S002.md | provenance/002-self-validation/03-close.md | 2 | closed S002 |
| [S003](S003.md) | closed | Multi-Agent Deliberation | S003.md | provenance/003-multi-agent-deliberation/03-close.md | 3 | closed S003 |
| [S004](S004.md) | closed | Participation Mechanisms | S004.md | provenance/004-participation-mechanisms/03-close.md | 4 | closed S004 |
| [S005](S005.md) | closed | Schema Enforcement & First Cross-Model | S005.md | provenance/005-schema-enforcement/03-close.md | 5 | closed S005 |
| [S006](S006.md) | closed | Triggers-Met Schema | S006.md | provenance/006-triggers-met-schema/03-close.md | 6 | closed S006 |
| [S007](S007.md) | closed | External Application Prep | S007.md | provenance/007-external-application-examination/03-close.md | 7 | closed S007 |
| [S008](S008.md) | closed | First External Application | S008.md | provenance/008-first-external-application/03-close.md | 8 | closed S008 |
| [S009](S009.md) | closed | External Validate Receipt + W2/W4 | S009.md | provenance/009-external-validate-receipt/03-close.md | 9 | closed S009 |
| [S010](S010.md) | closed | Second External Application | S010.md | provenance/010-household-decision-protocol/03-close.md | 10 | closed S010 |
| [S011](S011.md) | closed | W1 Kernel §1 Read Revision | S011.md | provenance/011-w1-kernel-read-revision/03-close.md | 11 | closed S011 |
| [S012](S012.md) | closed | OI-001 Methodology Naming — Selvedge | S012.md | provenance/012-methodology-naming/03-close.md | 12 | closed S012 |
| [S013](S013.md) | closed | Artefact Revision — House Decision v2 | S013.md | provenance/013-artefact-revision/03-close.md | 13 | closed S013 |
| [S014](S014.md) | closed | OI-016 Resolution — Reference-Validation Mechanism | S014.md | provenance/014-oi016-resolution/03-close.md | 14 | closed S014 |
| [S015](S015.md) | closed | Reference-Validation Agenda Ratified | S015.md | provenance/015-session-assessment/03-close.md | 15 | closed S015 |
| [S016](S016.md) | closed | Operator Reframing Input — OI-017 Opened | S016.md | provenance/016-operator-reframing-assessment/03-close.md | 16 | closed S016 |
| [S017](S017.md) | closed | OI-017 Resolved — H4 Layered Model; engine-manifest.md Created; PROMPT.md Split | S017.md | provenance/017-oi017-reframing-deliberation/03-close.md | 17 | closed S017 |
| [S018](S018.md) | closed | Reference-Validation First-Exercise — D2 Kerth REJECTED at C3 | S018.md | provenance/018-reference-validation-exercise-1/03-close.md | 18 | closed S018 |
| [S019](S019.md) | closed | reference-validation.md v1 → v2 — R1–R6 Adopted | S019.md | provenance/019-reference-validation-revision/03-close.md | 19 | closed S019 |
| [S020](S020.md) | closed | Workspace Scaling — §SESSION-LOG Minor; mempalace R3 | S020.md | provenance/020-workspace-scaling-deliberation/03-close.md | 20 | closed S020 |
| [S021](S021.md) | closed | OI-004 Criterion-4 Articulation; engine-v1 → engine-v2 | S021.md | provenance/021-oi004-criterion4-articulation/03-close.md | 21 | closed S021 |
| [S022](S022.md) | closed | Workspace Scaling Trajectory — Read-Contract Adoption; engine-v2 → engine-v3 | S022.md | provenance/022-workspace-scaling-trajectory/03-close.md | 22 | closed S022 |
| [S023](S023.md) | closed | Read-Contract Budget Recalibration; engine-v3 → engine-v4; §5.4 Cadence Activate... | S023.md | provenance/023-session-assessment/03-close.md | 23 | closed S023 |
| [S024](S024.md) | closed | MAD 6K-Soft-Warn Response — A.4 Carry-the-Warning; engine-v4 Preserved | S024.md | provenance/024-session-assessment/03-close.md | 24 | closed S024 |
| [S025](S025.md) | closed | Path A — Carry-Warning Continues; engine-v4 Preserved | S025.md | provenance/025-session-assessment/03-close.md | 25 | closed S025 |
| [S026](S026.md) | closed | Path A — D-086 R9 Cadence Escalation Window Ages Out | S026.md | provenance/026-session-assessment/03-close.md | 26 | closed S026 |
| [S027](S027.md) | closed | Folder-Naming Discipline; §5.2 Vindicated; §5.3 Aggregate Activated; engine-v4 P... | S027.md | provenance/027-session-assessment/03-close.md | 27 | closed S027 |
| [S028](S028.md) | closed | Path G — §5.3 Converted; read-contract.md v3; Close-Rotation; engine-v4 → engine... | S028.md | provenance/028-session-assessment/03-close.md | 28 | closed S028 |
| [S029](S029.md) | closed | Path A + §6.2 Audit of Session 028 All-Clean; First Post-v5; First Close-Rotatio... | S029.md | provenance/029-session-assessment/03-close.md | 29 | closed S029 |
| [S030](S030.md) | closed | Path J — workspace-structure.md §SESSION-LOG Stale-Literal Cleanup; WX-24-2 Flag... | S030.md | provenance/030-session-assessment/03-close.md | 30 | closed S030 |
| [S031](S031.md) | closed | Path C — S1 Feldenkrais L1b PASS; Sealing Deferred; §5.6 + §5.8 Double Vindicati... | S031.md | provenance/031-session-assessment/03-close.md | 31 | closed S031 |
| [S032](S032.md) | closed | Path C-Fresh — PD-A RoSB L1b REJECT; §9 Trigger 7 FIRES; OI-016 Re-Opens | S032.md | provenance/032-session-assessment/03-close.md | 32 | closed S032 |
| [S033](S033.md) | closed | Path K+L — Kernel §7 Revision; methodology-kernel.md v5→v6 + reference-validatio... | S033.md | provenance/033-session-assessment/03-close.md | 33 | closed S033 |
| [S034](S034.md) | closed | Path A + §6.2 Audit of Session 033 All-Clean; §5.9 + §5.10 Double Vindication; e... | S034.md | provenance/034-session-assessment/03-close.md | 34 | closed S034 |
| [S035](S035.md) | closed | Path A — Second Post-v6; WX-35-1 OI-004.md 13-Session Claimed-But-Unexecuted Gap... | S035.md | provenance/035-session-assessment/03-close.md | 35 | closed S035 |
| [S036](S036.md) | closed | Path PD — MODE.md + engine-feedback/ Adopted; engine-v6 → engine-v7 | S036.md | provenance/036-session-assessment/03-close.md | 36 | closed S036 |
| [S037](S037.md) | closed | Path A + §6.2 Audit of Session 036 All-Clean; First Post-v7 | S037.md | provenance/037-session-assessment/03-close.md | 37 | closed S037 |
| [S038](S038.md) | closed | Path A — Second Post-v7; §10.3 Skeptic-Preserver Minimal-Revision Non-Vindicated... | S038.md | provenance/038-session-assessment/03-close.md | 38 | closed S038 |
| [S039](S039.md) | closed | Path A — Third Post-v7; WX-35-1 Vindicated at Standing Discipline | S039.md | provenance/039-session-assessment/03-close.md | 39 | closed S039 |
| [S040](S040.md) | closed | Path L+A — SESSION-LOG.md Preemptive Restructure; Thin-Index Discipline Restored... | S040.md | provenance/040-session-log-preemptive-restructure/03-close.md | 40 | closed S040 |
| [S041](S041.md) | closed | Path OI-004 — Closure: State 3→4 (Closed); First-Ever OI-004 Closure; §5.2 + §5.... | S041.md | provenance/041-session-assessment/03-close.md | 41 | closed S041 |
| [S042](S042.md) | closed | Path A — First Post-OI-004-Closure; engine-v7 Preservation Window 6 (New Longest... | S042.md | provenance/042-session-assessment/03-close.md | 42 | closed S042 |
| [S043](S043.md) | closed | Path PSD — Path-Selection Discipline Deliberation; First Three-Family Three-Line... | S043.md | provenance/043-session-assessment/03-close.md | 43 | closed S043 |
| [S044](S044.md) | closed | Path OC — Operator-Corrective New Class; Four-Perspective Two-Family (2 Claude +... | S044.md | provenance/044-session-assessment/03-close.md | 44 | closed S044 |
| [S045](S045.md) | closed | Path OS — Operator-Surfaced Four-Perspective Two-Family Cross-Family Deliberatio... | S045.md | provenance/045-session-assessment/03-close.md | 45 | closed S045 |
| [S046](S046.md) | closed | Path OS — First External-Application Bootstrap (selvedge-disaster-response 4–5 S... | S046.md | provenance/046-session/03-close.md | 46 | closed S046 |
| [S047](S047.md) | closed | Path OS — Operator-Directed MAD Design of Arc-Plan for selvedge-disaster-respons... | S047.md | provenance/047-session/03-close.md | 47 | closed S047 |
| [S048](S048.md) | closed | Path T — Default-Agent Triage-Classify of engine-feedback/inbox/ (First Non-Empt... | S048.md | provenance/048-session/03-close.md | 48 | closed S048 |
| [S049](S049.md) | closed | Path AS — Scope Revised Mid-Ratification to Synthesis + Options + Meta-Decision ... | S049.md | provenance/049-session/03-close.md | 49 | closed S049 |
| [S050](S050.md) | closed | Path AS Reified n=2 — 4-Perspective Two-Family MAD on EF-047-Retrieval-Disciplin... | S050.md | provenance/050-session/03-close.md | 50 | closed S050 |
| [S051](S051.md) | closed | Path L+A (Preemptive-Restructure + Watch) Reified n=2 — Forced-Restructure per S... | S051.md | provenance/051-session/03-close.md | 51 | closed S051 |
| [S052](S052.md) | closed | Path T+L (Triage-Classify + Minor Path L Implementation Fix) First-Instance Bund... | S052.md | provenance/052-session/03-close.md | 52 | closed S052 |
| [S053](S053.md) | closed | Path A (Watch) Pure Ratified — Single-Orchestrator Default-Agent Session; Engine... | S053.md | provenance/053-session/03-close.md | 53 | closed S053 |
| [S054](S054.md) | closed | Path T+L (Triage-Classify + Minor Path L Implementation Fix) Reified at n=2 (S05... | S054.md | provenance/054-session/03-close.md | 54 | closed S054 |
| [S055](S055.md) | closed | Path A (Watch) Pure Ratified — Tenth Path A Instance; `forward_references('S055'... | S055.md | provenance/055-session/03-close.md | 55 | closed S055 |
| [S056](S056.md) | closed | Path T (Triage-Classify) Pure Reified n=2 (S048 First-Instance Single-Orchestrat... | S056.md | provenance/056-session/03-close.md | 56 | closed S056 |
| [S057](S057.md) | closed | Path AS Shape-1 (Phase-1 Synthesis/Design-Space Session for EF-055 Dedicated MAD... | S057.md | provenance/057-session/03-close.md | 57 | closed S057 |
| [S058](S058.md) | closed | Path AS-MAD-execution per S057 D-196 pre-ratification; 4-perspective two-family ... | S058.md | provenance/058-session/03-close.md | 58 | closed S058 |
| [S059](S059.md) | closed | Path T+L bundled scope — Triage of 3 EF-058 inbox records (uv-migration resolve... | S059.md | provenance/059-session/03-close.md | 59 | closed S059 |
| [S060](S060.md) | closed | Path L+A reshape mid-ratification; (i)+(b)+(β) records-substrate-authority alig... | S060.md | provenance/060-session/03-close.md | 60 | closed S060 |
| [S061](S061.md) | closed | Path AS Shape-1 (Phase-1 Synthesis/Design-Space Session for EF-058-tier-2-valid... | S061.md | provenance/061-session/03-close.md | 61 | closed S061 |
| [S062](S062.md) | closed | Path AS-MAD-execution per S061 D-218 pre-ratification — 4-perspective two-family MAD on EF-058-tier-2-validation; (δ-γ + α + z5-light + z6-deferred-spec) layer composition adopted | S062.md | provenance/062-session/03-close.md | 62 | closed S062 |
| [S063](S063.md) | closed | Path L (single-orchestrator phase-3 adoption) per S062 D-221 — engine-v10→v11 ratified; layer composition implemented; first triggered (γ) cross-family reviewer fired (Google Gemini; first-of-record provider); WX-62-1 opens; (z5) ledger bootstrapped | S063.md | provenance/063-session/03-close.md | 63 | closed S063 |
| [S064](S064.md) | closed | Path AS-MAD-execution per session-mid operator amendment — engine-v11→v12 ratified (first-of-record depth-0 preservation); v6→v7 substantive (revised §Tier 2.5 + minimum-evidence-packet + §7 Next-session-shape critique + (z11) authoritative-not-witness + tripartite distinction + Layer 6.5 + (z7) template-versioning); 5 new minorities (45→50); second (γ) reviewer fired (codex; bootstrap-limited-confidence) | S064.md | provenance/064-session/03-close.md | 64 | closed S064 |
| [S065](S065.md) | closed | Path A (Watch) ratified — first non-MAD post-engine-v12 session; observation window for revised v7 audit shape; affirmative no-action justification per (z12) 5-condition test; engine-v12 preserved (depth 0→1); WX-62-1 stays at 2-of-3 (third recording at next triggered close); D-129 nineteenth-consecutive + D-138 nineteenth-consecutive clean exercises; WX-28-1 thirty-fifth close-rotation S059 OUT S065 IN; WX-24-1 MAD v4 thirty-eighth-session no-growth streak (23-session run; new record); thirty-seventh-consecutive housekeeping [none]-trigger pattern | S065.md | provenance/065-session/03-close.md | 65 | closed S065 |
