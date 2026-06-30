# Redis eviction receipt robustness under subscriber backpressure and disconnects

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `48`
Project ID: `redis-eviction-receipt-robustness-under-subscriber-backpre-7d28274c9a`
Run ID: `redis-eviction-receipt-robustness-under-subscriber-backpre-7d28274c9a-20260522T033105182212+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `48`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Native Redis Eviction Receipts Under Concurrent Clients: enoch://control-plane/projects/native-redis-eviction-receipts-under-concurrent-clients-54d9c42b07/runs/native-redis-eviction-receipts-under-concurrent-clients-54d9c42b07-20260522T015852927877+0000
- Parent run decision: Persistent Anchored Eviction Receipts In A Real Cache: enoch://control-plane/projects/persistent-anchored-eviction-receipts-in-a-real-cache-27bca397c9/runs/persistent-anchored-eviction-receipts-in-a-real-cache-27bca397c9-20260522T015359853338+0000

## What looked useful

Against Redis INFO stats.evicted_keys, fast subscribers received 306858/306858 eviction events across three repeats, but slow_5ms subscribers received only 1397/263854 with two OOM write failures, slow_1ms_lowbuf received 12845/357629, and 50% disconnect subscribers received 53107/334054. Plain Pub/Sub keyevent notifications therefore fail robust receipt semantics under the tested stressors.

## Boundaries and scale limits

Single host, loopback Redis, Redis 7.0.15 only, 8 MB maxmemory, synthetic 1 KiB values, three fixed seeds per scenario, and bounded CPU-only runtime under the GB10 resource limit. Not a multi-version, multi-node, production-network, or 24-hour datacenter validation.

## Claim scope

Local Redis 7.0.15 keyevent Pub/Sub eviction notifications are not robust application-level eviction receipts under slow subscriber processing, low pubsub output-buffer pressure, or subscriber disconnects; fast subscribers can match evicted_keys exactly in this harness.

## Why it stopped

Direct bounded local validation falsified the robustness hypothesis for plain Redis keyevent Pub/Sub under subscriber backpressure and disconnects; this is useful no-paper evidence rather than paper-positive positive evidence.

## Recommended next action

Stop treating Redis keyevent Pub/Sub as a robust eviction receipt channel; if durable receipts are needed, test a Redis Streams or external ledger design against the same evicted_keys ground truth matrix.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Durable Redis eviction receipt ledger under subscriber backpressure
- Success threshold: Across at least three seeds per scenario, durable receipt coverage is >= 0.999 against evicted_keys, no Redis write OOM occurs, and reconnecting subscribers can recover missed receipts from the ledger.
- Stop condition: Stop if the durable mechanism loses more than 0.1% of receipts in any stressed scenario, triggers Redis OOM/write refusal, or requires throughput collapse so severe that it is not a practical receipt design.

## Evidence references

- Artifact root: `<local-path>/projects/redis-eviction-receipt-robustness-under-subscriber-backpre-7d28274c9a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
