# Adversarial Persistence Test for Incremental Merkle KV Agent Trace Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adversarial-persistence-test-for-incremental-merkle-kv-age-e2048a7490`
Run ID: `adversarial-persistence-test-for-incremental-merkle-kv-age-e2048a7490-20260518T002853431333+0000`

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

- Internal Enoch project: Adversarial Persistence Test for Incremental Merkle KV Agent Trace Ledger: internal_generated:adversarial-persistence-test-for-incremental-merkle-kv-age-e2048a7490

## What looked useful

Mechanism support: immutable per-revision Merkle root anchors preserve adversarial persistence for mutable KV trace state under targeted value-edit, deletion, rollback, replay, and forged-root attacks, while providing much cheaper historical point verification than hash-chain replay. The no-history-anchor ablation failed clean historical verification, confirming that historical anchors are necessary for the target ledger behavior.

## Boundaries and scale limits

Synthetic single-process workload only; no real agent traces, crash/restart validation, concurrent writers, external transparency service, signatures, or optimized persistent tree. The simulator stores full revision snapshots and recomputes roots on writes, making write throughput about 9.4x slower than the hash-chain baseline and preventing a systems-performance claim.

## Claim scope

In a deterministic local Python simulator with 8 fixed seeds, 2000 writes per seed, 800-key workload, and 300 targeted adversarial persistence attacks per scheme per seed, a per-revision anchored Merkle KV trace ledger detected all targeted tampering tested and reduced median historical point verification hash work from 1334.75 operations for a hash-chain baseline to 12.0 operations.

## Why it stopped

Medium local evidence supports the persistence mechanism but not publication readiness because the workload is synthetic, the implementation is an unoptimized simulator, the 5000-write attempt exposed harness scalability limits, and no crash/restart or real trace validation was performed.

## Recommended next action

Stop this run as no-paper useful evidence; next, implement an optimized persistent sparse Merkle tree or Merkle-B-tree ledger and rerun the same adversarial suite at >=10000 writes, >=16 fixed seeds, and with crash/restart persistence checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized Persistent Merkle KV Ledger With Crash-Restart Adversarial Persistence
- Success threshold: Across >=16 seeds and >=10000 writes per seed, optimized Merkle KV detects 100% of targeted adversarial persistence attacks, clean historical queries pass, median historical point verification remains <=2% of hash-chain replay hash work, and write throughput is at least 50% of the hash-chain baseline.
- Stop condition: Stop negative if any targeted attack is undetected, clean historical verification fails, crash/restart corruption is not detected, median point verification exceeds 10% of hash-chain replay, or write throughput remains below 25% of hash-chain after one optimized implementation pass.

## Evidence references

- Artifact root: `<local-path>/projects/adversarial-persistence-test-for-incremental-merkle-kv-age-e2048a7490`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
