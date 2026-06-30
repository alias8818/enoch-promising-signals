# Heterogeneous Real-Trace Verifier Shard Scheduling

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `heterogeneous-real-trace-verifier-shard-scheduling-6da291fae9`
Run ID: `heterogeneous-real-trace-verifier-shard-scheduling-6da291fae9-20260522T020904507296+0000`

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

- Parent run decision: Distributed Verifier Shards: enoch://control-plane/projects/distributed-verifier-shards-39aa7e742d8d/runs/distributed-verifier-shards-39aa7e742d8d-20260521T223852892600+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2eeb37ddb77e

## What looked useful

Heterogeneity-aware queue/rate scheduling is the dominant baseline: it reduced p95 latency by roughly 70% versus round-robin, while adding explicit cache locality improved p95 by only 0.77% at 8,192 blocks/shard and 2.15% with very large caches, below the 10% Tier 1 threshold.

## Boundaries and scale limits

Single trace sample, simulator-only service model, fixed three-shard heterogeneity, no live verifier kernels, no batching/network/memory-contention model, and no full multi-day trace validation.

## Claim scope

On the first 5,000 requests of the public Qwen Bailian trace, with modeled heterogeneous verifier shard rates and per-shard LRU prefix caches, cache-aware estimated-completion-time scheduling did not materially improve p95 latency over heterogeneity-aware estimated-completion-time scheduling without cache locality.

## Why it stopped

Controlled small direct trace simulation failed the stated 10% p95 improvement threshold; this is not full serving-system validation, but it is a direct early falsification of the cache-aware scheduling advantage under the tested trace and service model.

## Recommended next action

Stop this run as no-paper useful signal; any next bounded test should calibrate verifier service/cache-hit costs on real kernels before re-testing whether cache-aware placement can clear a 10% p95 threshold over heterogeneity-aware ECT.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Verifier Cache-Cost Scheduling Test
- Success threshold: Cache-aware scheduling must reduce p95 latency by at least 10% versus hetero_ect_no_cache in at least two load settings without reducing throughput or increasing any major request-type p95 by more than 5%.
- Stop condition: Stop if calibrated cache-aware scheduling remains below 5% p95 improvement over hetero_ect_no_cache across all tested load and cache settings.

## Evidence references

- Artifact root: `<local-path>/projects/heterogeneous-real-trace-verifier-shard-scheduling-6da291fae9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
