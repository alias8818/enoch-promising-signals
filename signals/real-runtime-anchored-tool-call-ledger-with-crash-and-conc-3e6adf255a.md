# Real-runtime anchored tool-call ledger with crash and concurrency faults

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-runtime-anchored-tool-call-ledger-with-crash-and-conc-3e6adf255a`
Run ID: `real-runtime-anchored-tool-call-ledger-with-crash-and-conc-3e6adf255a-20260526T195531317700+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Runtime-integrated anchored tool-call ledger: enoch://control-plane/projects/runtime-integrated-anchored-tool-call-ledger-6e04a98f51/runs/runtime-integrated-anchored-tool-call-ledger-6e04a98f51-20260526T130857146414+0000
- Parent run decision: Append-Only Ledger for Tool Call Verification: enoch://control-plane/projects/append-only-ledger-for-tool-call-verification-67c714c7c256/runs/append-only-ledger-for-tool-call-verification-67c714c7c256-20260526T043111662260+0000

## What looked useful

Main run: anchored ledger lost 0/4051 acknowledged events; anchored_no_anchor lost 0/3151; SQLite WAL lost 0/3114; naive JSONL lost 17/3118 and failed in all 5 partial-fault trials. No-partial ablation lost 0 acknowledged events for all variants, showing the unsafe baseline fails specifically under torn-write faults. Anchors were not necessary for local recovery in this harness; framing, fsync, locking, and tail repair were the supported mechanism.

## Boundaries and scale limits

Evidence is limited to local filesystem semantics, Python subprocess writers, synthetic tool-call records, 5 fixed seeds for the partial-write run, and 3 fixed seeds for the no-partial ablation. It does not cover actual LangGraph/OpenAI runtime integration, power loss, kernel panic, network filesystems, multi-host concurrency, long soak tests, or optimized production performance.

## Claim scope

In a local Python real-runtime filesystem/process harness, a framed tool-call ledger using flock serialization, fsync, CRC/hash-chain validation, and pre-append torn-tail repair preserved all acknowledged event ids across fixed-seed concurrent SIGKILL and partial-write fault trials, matching SQLite WAL on acknowledged-event durability and outperforming unsafe JSONL on reliability.

## Why it stopped

Tier 2 local evidence supports the mechanism but is not paper-positive because it uses synthetic tool-call records and a local harness rather than a production agent runtime integration or broad filesystem/power-loss validation.

## Recommended next action

Run a bounded real LangGraph/tool-middleware integration follow-up that emits actual tool-call lifecycle events and injects crashes around tool execution, ledger append, ack emission, and replay.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LangGraph-integrated crash/replay validation for anchored tool-call ledgers
- Success threshold: Zero lost acknowledged tool-call events and no non-idempotent duplicate side effects for anchored across at least 10 fixed-seed integrated runtime trials, with recovery behavior within 2x SQLite WAL latency and explicit handling of unacknowledged recovered events.
- Stop condition: Stop if anchored loses any acknowledged event, produces an unrecoverable hash/checksum/anchor mismatch after repair, or cannot provide an idempotent replay policy for unacknowledged recovered events in the real runtime.

## Evidence references

- Artifact root: `<local-path>/projects/real-runtime-anchored-tool-call-ledger-with-crash-and-conc-3e6adf255a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
