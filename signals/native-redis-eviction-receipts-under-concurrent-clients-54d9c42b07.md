# Native Redis Eviction Receipts Under Concurrent Clients

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `native-redis-eviction-receipts-under-concurrent-clients-54d9c42b07`
Run ID: `native-redis-eviction-receipts-under-concurrent-clients-54d9c42b07-20260522T015852927877+0000`

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

- Parent run decision: Persistent Anchored Eviction Receipts In A Real Cache: enoch://control-plane/projects/persistent-anchored-eviction-receipts-in-a-real-cache-27bca397c9/runs/persistent-anchored-eviction-receipts-in-a-real-cache-27bca397c9-20260522T015359853338+0000
- Parent run decision: Eviction Cryptographic Receipts: enoch://control-plane/projects/eviction-cryptographic-receipts-a4bac4165d4c/runs/eviction-cryptographic-receipts-a4bac4165d4c-20260521T225414196665+0000

## What looked useful

A deterministic Tier 2 local harness found that native Redis keyevent eviction notifications can act as high-coverage eviction receipts under 8 concurrent local clients, with a sequential baseline and notification-off ablation confirming the signal. The result is useful mechanism evidence but not paper-ready durability or distributed-systems evidence.

## Boundaries and scale limits

Single Redis process on one host; no cluster, replication, failover, networked subscriber, subscriber disconnect, slow-consumer Pub/Sub pressure, output-buffer-limit stress, or multi-hour runtime. The Redis evicted_keys counter exceeded final missing-key census by a small amount near the memory cap, so exact receipt/counter parity is not established.

## Claim scope

On local Redis 7.0.15 with allkeys-lru, notify-keyspace-events=Ee, one fast local Pub/Sub subscriber, 12 MB maxmemory, 4 KiB values, and 8 concurrent local writer clients, native Redis eviction keyevent notifications covered 100% of finally absent successfully written keys over 23,442 observed concurrent evictions across three fixed seeds; unique receipts covered 99.936% of Redis evicted_keys counter deltas.

## Why it stopped

Tier 2 local evidence supports the mechanism, but paper-grade robustness is missing; closing as no-paper useful signal rather than overclaiming.

## Recommended next action

Run a bounded deepen follow-up that keeps the same direct metrics but adds slow-subscriber/backpressure and disconnect/reconnect controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Redis eviction receipt robustness under subscriber backpressure and disconnects
- Success threshold: Fast subscriber retains at least 99% receipt coverage while slow or disconnected subscriber conditions quantify the first failure threshold in terms of delay, buffer pressure, or reconnect gap.
- Stop condition: Stop if the fast subscriber falls below 99% coverage under the same local conditions or if slow/disconnect conditions show deterministic receipt loss that makes native receipts unsuitable without an external durable log.

## Evidence references

- Artifact root: `<local-path>/projects/native-redis-eviction-receipts-under-concurrent-clients-54d9c42b07`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
