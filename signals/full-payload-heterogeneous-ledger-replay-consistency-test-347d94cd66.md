# Full-Payload Heterogeneous Ledger Replay Consistency Test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `full-payload-heterogeneous-ledger-replay-consistency-test-347d94cd66`
Run ID: `full-payload-heterogeneous-ledger-replay-consistency-test-347d94cd66-20260522T194142705711+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Deterministic Replay Adapter for a Real Agent Ledger: enoch://control-plane/projects/deterministic-replay-adapter-for-a-real-agent-ledger-afde7186f2/runs/deterministic-replay-adapter-for-a-real-agent-ledger-afde7186f2-20260522T092004428790+0000
- Parent run decision: Heterogeneous Real-Ledger Deterministic Replay Corpus Test: enoch://control-plane/projects/heterogeneous-real-ledger-deterministic-replay-corpus-test-1b7b3fccfe/runs/heterogeneous-real-ledger-deterministic-replay-corpus-test-1b7b3fccfe-20260522T101304328718+0000

## What looked useful

Full-payload ledger records gave 64/64 deterministic replay consistency across three local backends. Pointer mutation/loss controls showed 0/64 consistency after one external payload was changed or removed: unverified mutation silently diverged, verified mutation failed, and payload loss failed. The mechanism is supported, but the result is not paper-positive.

## Boundaries and scale limits

Synthetic local workload only; heterogeneous paths are storage/serialization backends, not independent production ledger systems; no production traces, multi-language engines, distributed consensus logs, schema evolution, or long-retention object-store failures were tested.

## Claim scope

On a synthetic fixed-seed account ledger with 64 seeds, 20,000 transactions per seed, 1,000 accounts, and 512-byte payload memos, canonical full-payload append records replayed to identical final-state hashes across JSONL, gzip JSONL, and SQLite backends; a hash+URI pointer baseline only replayed consistently while external payload blobs remained clean.

## Why it stopped

Bounded synthetic validation supports the mechanism but does not establish a broad or novel publication-grade claim.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded deepen test should replay a real public ledger or audit-log corpus through at least two independently implemented readers and repeat the pointer mutation/loss controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Corpus Full-Payload Ledger Replay Consistency
- Success threshold: Across the fixed real corpus, full-payload replay must show 100% final-state hash agreement across independent readers, while pointer mutation/loss controls must show either detected unreplayability or measurable silent divergence in at least 95% of injected trials.
- Stop condition: Stop if full-payload replay diverges across independent readers without a correctable canonicalization bug, or if no suitable real corpus with durable full payloads can be used without private/human access.

## Evidence references

- Artifact root: `<local-path>/projects/full-payload-heterogeneous-ledger-replay-consistency-test-347d94cd66`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
