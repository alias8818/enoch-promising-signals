# Merkleized KV Ledger for Local Agent Integrity

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `merkleized-kv-ledger-for-local-agent-integrity-86296c8425e9`
Run ID: `merkleized-kv-ledger-for-local-agent-integrity-86296c8425e9-20260518T001333466821+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bc7881660028

## What looked useful

Mechanism works for local integrity: Merkle ledger detected tampering where plain JSONL did not, and proof checks exceeded 166k/s in the largest probe. However naive recomputation limited Merkle write/verify throughput to 316 ops/s at 10k updates versus roughly 106k write ops/s and 204k verify ops/s for a hash-chain control.

## Boundaries and scale limits

Synthetic single-process workloads only; no real agent traces, concurrent writers, crash recovery, external root anchoring, deletion/truncation adversary coverage, or optimized incremental Merkle tree. Largest run was 10,000 updates / 2,000 keys / 1 repeat.

## Claim scope

A stdlib Python prototype of a Merkleized append-only KV ledger detects direct record tampering and supports fast sampled inclusion-proof verification on synthetic local workloads up to 10,000 updates and 2,000 keys, but uses naive full-tree recomputation.

## Why it stopped

Useful bounded local evidence, but not paper-ready because the evaluation is synthetic and the naive implementation has a measured scaling bottleneck.

## Recommended next action

Implement an incremental Merkle KV index with external root anchoring and evaluate it on real local-agent KV traces; stop this run as no-paper useful evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Incremental Merkle KV Ledger on Real Agent Traces
- Success threshold: Incremental Merkle ledger detects all tested tamper classes, verifies sampled inclusion proofs correctly, and achieves at least 10k write ops/s plus 50k replay verify ops/s with under 3x bytes/op versus hash-chain on the trace workload.
- Stop condition: Stop if incremental Merkle throughput remains below 2k write ops/s or fails any tamper/crash-recovery correctness check after one implementation pass.

## Evidence references

- Artifact root: `<local-path>/projects/merkleized-kv-ledger-for-local-agent-integrity-86296c8425e9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
