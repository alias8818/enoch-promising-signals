# Unified-memory optimizer offload strategies on GB10

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `unified-memory-optimizer-offload-strategies-on-gb10-35d030d256c0`
Run ID: `unified-memory-optimizer-offload-strategies-on-gb10-35d030d256c0-20260613T091259715895+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/90ea5e0df42f

## What looked useful

Naive CPU optimizer offload over CUDA managed memory on GB10 increased step time by 1.38x to 3.62x versus GPU-side Adam updates across 0.016 GiB to 16 GiB managed allocations; explicit prefetch did not produce a throughput win.

## Boundaries and scale limits

Synthetic optimizer microbenchmark only; no real PyTorch/DeepSpeed/FSDP training loop, no convergence measurement, no activation-pressure study, and no capacity-threshold case where GPU-only optimizer state fails.

## Claim scope

On a GB10 host, a synthetic CUDA managed-memory Adam-style optimizer microbenchmark with up to 16 GiB total managed allocation found GPU-side optimizer updates faster than CPU updates over managed memory, with or without explicit prefetch.

## Why it stopped

Closed as no-paper useful signal: direct managed-memory microbenchmark evidence argues against naive CPU optimizer offload as a throughput optimization, but full training evidence would be required for a paper or broader claim.

## Recommended next action

Run a bounded real PyTorch training comparison on GB10 using GPU AdamW versus FSDP or ZeRO-style CPU optimizer offload, including throughput and capacity-threshold measurements.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real PyTorch GB10 optimizer offload throughput and capacity threshold
- Success threshold: CPU optimizer offload either improves end-to-end throughput by at least 5% at equal model/batch or enables at least 25% larger batch/parameter count with no more than 20% throughput loss.
- Stop condition: Stop if CPU offload is at least 20% slower at equal scale and does not enable a materially larger safe batch or model size under GB10 MemAvailable telemetry.

## Evidence references

- Artifact root: `<local-path>/projects/unified-memory-optimizer-offload-strategies-on-gb10-35d030d256c0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
