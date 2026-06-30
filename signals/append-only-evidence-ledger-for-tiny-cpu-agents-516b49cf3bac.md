# Append-Only Evidence Ledger for Tiny CPU Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `append-only-evidence-ledger-for-tiny-cpu-agents-516b49cf3bac`
Run ID: `append-only-evidence-ledger-for-tiny-cpu-agents-516b49cf3bac-20260525T124631360659+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ee1b9b06ebf8

## What looked useful

Append-only hash-chain evidence ledgers appear practical for tiny CPU agents when durability is batched and head hashes are externally anchored; per-record fsync and unanchored tail truncation are the main observed failure modes.

## Boundaries and scale limits

Synthetic events only; single writer; local filesystem only; no production agent traces; no crash-consistency or power-loss testing; no adversarial kernel/storage threat model; no comparison to SQLite/WAL or transparency-log implementations; per-record fsync fell to 848 records/s on this worker.

## Claim scope

In a bounded single-process CPU-worker benchmark with 5,000 deterministic 2 KiB synthetic tiny-agent events, a canonical JSONL SHA-256 hash-chain ledger sustained 23.4k records/s without fsync and 10.9k records/s with fsync batched every 100 records, detected payload modification, middle deletion, and adjacent reordering from the file contents, and detected tail truncation only when checked against an external head-hash anchor.

## Why it stopped

Synthetic single-process local evidence supports the mechanism but is not direct enough for a paper; the decision is a bounded useful signal, not full validation.

## Recommended next action

Stop this run as no-paper useful evidence; a bounded deepen follow-up should test the same ledger against crash recovery and SQLite/WAL baselines using real or replayed tiny-agent traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash and Baseline Evaluation for Tiny-Agent Evidence Ledgers
- Success threshold: Batched-fsync hash ledger remains within 2x plain JSONL append latency, loses no more than the configured batch interval after crash, detects all non-tail mutation/reorder/delete faults, detects tail truncation when anchored, and matches or beats SQLite/WAL throughput for replayed tiny-agent traces.
- Stop condition: Stop if crash recovery loses more than the configured batch interval, any non-tail tamper is undetected, anchored tail truncation is undetected, or the hash ledger is slower than SQLite/WAL by more than 2x under the same durability policy.

## Evidence references

- Artifact root: `<local-path>/projects/append-only-evidence-ledger-for-tiny-cpu-agents-516b49cf3bac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
