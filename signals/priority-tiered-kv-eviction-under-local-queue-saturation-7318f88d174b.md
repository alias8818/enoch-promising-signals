# Priority-Tiered KV Eviction Under Local Queue Saturation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `priority-tiered-kv-eviction-under-local-queue-saturation-7318f88d174b`
Run ID: `priority-tiered-kv-eviction-under-local-queue-saturation-7318f88d174b-20260621T034503700965+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/60b7c27a2283

## What looked useful

Eviction-only priority protection can backfire under local queue saturation because low-priority recompute work increases shared queue backlog, offsetting high-priority KV residency gains.

## Boundaries and scale limits

Proxy-only CPU simulation; no real transformer execution, block-level PagedAttention, CUDA kernels, production continuous batching, or real serving traces were tested.

## Claim scope

In a deterministic whole-request KV-cache simulation with FIFO local decode scheduling, priority-tiered eviction under saturated queues reduced high-priority KV evictions and recompute but worsened high-priority p95 latency and completions versus LRU.

## Why it stopped

Proxy medium sweep found the core eviction-only mechanism did not improve high-priority latency under saturated FIFO local queues, so this is useful no-paper evidence rather than full validation.

## Recommended next action

Stop this eviction-only run as a proxy early falsification; next bounded test should couple priority-tiered eviction with priority-aware scheduling or recompute throttling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Coupled Priority-Tiered Eviction With Recompute-Aware Scheduling
- Success threshold: High-priority p95 latency improves by at least 20% versus LRU/FIFO while total completions decrease by no more than 10% and low-priority starvation does not increase unboundedly.
- Stop condition: Stop if coupled scheduling still worsens high-priority p95 latency in every load/capacity cell or requires sacrificing more than 10% total completions to achieve priority gains.

## Evidence references

- Artifact root: `<local-path>/projects/priority-tiered-kv-eviction-under-local-queue-saturation-7318f88d174b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
