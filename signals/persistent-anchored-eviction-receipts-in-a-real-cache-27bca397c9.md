# Persistent Anchored Eviction Receipts In A Real Cache

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `persistent-anchored-eviction-receipts-in-a-real-cache-27bca397c9`
Run ID: `persistent-anchored-eviction-receipts-in-a-real-cache-27bca397c9-20260522T015359853338+0000`

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

- Parent run decision: Eviction Cryptographic Receipts: enoch://control-plane/projects/eviction-cryptographic-receipts-a4bac4165d4c/runs/eviction-cryptographic-receipts-a4bac4165d4c-20260521T225414196665+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2eeb37ddb77e

## What looked useful

Mechanism support is positive: 890 observed DiskCache evictions produced exactly 890 receipts and 36 anchors, no-eviction control produced zero receipts, and tampering with receipt line 446 was detected. Practicality is limited by high overhead: mean set latency was 10.44x baseline and p95 latency was 68.15x baseline.

## Boundaries and scale limits

Small deterministic workload only: 900 set operations, 2048-byte values, 98,304-byte cache size limit, single process, no concurrency, no crash-window testing, no Redis/Memcached/native cache hook, and eviction reason inferred by comparing live keys before and after each set.

## Claim scope

In a controlled single-process Tier-1 test using diskcache.Cache 5.6.3 as a real SQLite-backed cache, an external wrapper converted all observed capacity evictions into fsynced JSONL receipts, chained them with SHA-256, wrote periodic anchors, verified the chain after the run, avoided false positives in a no-eviction control, and detected receipt tampering.

## Why it stopped

Tier-1 direct evidence supports the mechanism but remains no-paper evidence because the implementation is an external DiskCache wrapper with high latency overhead and no concurrency, crash, or native engine validation.

## Recommended next action

Run a bounded native-event follow-up in Redis or Memcached with concurrent clients and crash-window checks before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Native Redis Eviction Receipts Under Concurrent Clients
- Success threshold: At least 10000 capacity evictions with receipt_count exactly matching independently observed evictions, zero receipts in a no-eviction control, tamper detection succeeds, post-restart verification succeeds, and p95 set latency overhead is below 2x baseline.
- Stop condition: Stop as unsupported if any confirmed eviction lacks a receipt, any no-eviction control emits receipts, chain or anchor verification fails after restart, or p95 overhead is at least 2x baseline after one straightforward batching or fsync-cadence optimization.

## Evidence references

- Artifact root: `<local-path>/projects/persistent-anchored-eviction-receipts-in-a-real-cache-27bca397c9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
