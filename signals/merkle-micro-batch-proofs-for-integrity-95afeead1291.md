# Merkle Micro-Batch Proofs for Integrity

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `merkle-micro-batch-proofs-for-integrity-95afeead1291`
Run ID: `merkle-micro-batch-proofs-for-integrity-95afeead1291-20260602T215000979966+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e0a7186ea72f

## What looked useful

Merkle micro-batches accepted valid proofs and rejected 891/891 tampered sampled records. Proofs verified in 6.44 to 36.60 microseconds and grew to 416 bytes at batch size 8192. Expected metadata beats one 32-byte digest per record only for sparse audits; at 100% per-record verification, Merkle proof metadata is much larger than per-record digests.

## Boundaries and scale limits

No signatures, key management, storage-engine integration, network transport, real workload traces, concurrent append behavior, recovery semantics, or adaptive adversary model were tested. This is not production-scale or publication-grade validation.

## Claim scope

Local CPU SHA-256 benchmark of Merkle micro-batches from 1 to 8192 records and 128 to 4096 bytes per record, measuring build throughput, proof size, verification latency, tamper rejection, and expected metadata under sparse audit rates.

## Why it stopped

Bounded local evidence supports the sparse-audit mechanism but falsifies the broader interpretation that Merkle micro-batch proofs are generally metadata-efficient for every-record integrity verification.

## Recommended next action

Stop as no-paper useful signal; next bounded test should integrate signed batch roots into an append-only log and compare sparse-audit detection against per-record HMAC/signature baselines on realistic traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Signed Merkle Micro-Batch Audit Prototype on Append-Only Trace
- Success threshold: At 1% to 5% audit rates, retain at least 3x less metadata per record than the per-record baseline, reject all invalid sampled proofs, and keep p95 proof verification under 1 ms on the same CPU class.
- Stop condition: Stop if signed-root/proof overhead exceeds per-record baseline metadata at sparse audit rates, if any tampered sampled record verifies successfully, or if p95 verification exceeds 1 ms for batch sizes up to 8192.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-micro-batch-proofs-for-integrity-95afeead1291`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
