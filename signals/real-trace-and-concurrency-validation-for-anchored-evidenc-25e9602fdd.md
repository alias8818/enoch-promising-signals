# Real Trace and Concurrency Validation for Anchored Evidence Ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-and-concurrency-validation-for-anchored-evidenc-25e9602fdd`
Run ID: `real-trace-and-concurrency-validation-for-anchored-evidenc-25e9602fdd-20260610T055341936141+0000`

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

- Parent run decision: Append-Only Evidence Ledger with Anchored Quotes for CPU Agents: enoch://control-plane/projects/append-only-evidence-ledger-with-anchored-quotes-for-cpu-agents-1ddaecc2803b/runs/append-only-evidence-ledger-with-anchored-quotes-for-cpu-agents-1ddaecc2803b-20260610T003542330990+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/eb42f9c0ae34

## What looked useful

The mechanism passed a controlled direct concurrency replay: 1,600 trace-derived events, 8 writers, 8 streams, 25 anchors, zero verification failures, stable replay digest, and deliberate payload tampering detected.

## Boundaries and scale limits

Trace corpus was small and local to this worker run; replay rounds amplified concurrency pressure but not trace diversity. The test used one SQLite database and thread-level concurrency only. It did not test multi-process, multi-host, crash/recovery, remote anchoring, Byzantine writers, long sustained load, or production trace volumes.

## Claim scope

In a controlled local Tier 1 replay of real Enoch/Codex JSONL trace records, a SQLite-backed anchored evidence ledger with transactional appends preserved exactly-once capture, per-stream hash-chain integrity, complete range anchors, deterministic replay verification, and post-commit tamper detection under 8 concurrent writer threads.

## Why it stopped

Tier 1 controlled direct test produced useful mechanism support but not publication-grade breadth or robustness.

## Recommended next action

Run a bounded deepen follow-up with an independent larger trace corpus, multi-process writers, and crash/recovery fault injection before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-process crash/recovery validation for anchored evidence ledgers
- Success threshold: After crash/restart, verification has zero missing or duplicate expected committed events, zero stream-chain failures, zero anchor failures, stable replay digest across two verification passes, deliberate tampering is detected, and throughput is within 3x of a simple append-only baseline for the same corpus.
- Stop condition: Stop as unsupported if any committed event is missing or duplicated, any stream hash chain or anchor verification fails without detected external tampering, recovery cannot complete after injected crashes, or throughput is worse than 3x the append-only baseline on the bounded corpus.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-and-concurrency-validation-for-anchored-evidenc-25e9602fdd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
