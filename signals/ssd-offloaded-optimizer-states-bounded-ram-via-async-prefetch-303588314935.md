# SSD-Offloaded Optimizer States: Bounded RAM via Async Prefetch

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ssd-offloaded-optimizer-states-bounded-ram-via-async-prefetch-303588314935`
Run ID: `ssd-offloaded-optimizer-states-bounded-ram-via-async-prefetch-303588314935-20260630T025922002551+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/19487e3ddef6

## What looked useful

For 488.3 MiB of offloaded Adam-like moment state, direct file offload reduced peak RSS from about 797 MiB in-RAM to 324-347 MiB. Async prefetch sped up offload by 1.109x normally and 1.435x with cold-cache hints, but remained 2.10-2.35x slower than in-RAM. Naive np.memmap did not bound RSS on this host.

## Boundaries and scale limits

No real model training, convergence, GPU overlap, multi-node behavior, memory-pressure GB10 behavior, checkpoint/restart path, or dedicated NVMe validation was tested. The local filesystem is worker storage and may not match a training SSD.

## Claim scope

A bounded CPU microbenchmark over 64M float32 parameters shows that direct chunk file I/O can keep Adam-like first/second moment state mostly outside process RSS, and one-thread async prefetch can recover throughput versus synchronous chunk paging.

## Why it stopped

Local evidence is a useful mechanism signal but remains a microbenchmark/proxy result, so this run should not proceed to paper writing.

## Recommended next action

Run one bounded deepen test: integrate direct chunk I/O async prefetch into a small real training loop and require matching loss trajectory plus lower peak RSS before considering any paper path.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-model training validation for direct-I/O offloaded Adam states
- Success threshold: Offloaded run matches final loss within 1% of in-RAM Adam, reduces peak process memory by at least 40%, and keeps median step-time slowdown at or below 2.5x on the same host.
- Stop condition: Stop as negative if loss diverges, checkpoint/restart is incorrect, memory reduction is below 25%, or median step-time slowdown exceeds 4x after chunk-size tuning.

## Evidence references

- Artifact root: `<local-path>/projects/ssd-offloaded-optimizer-states-bounded-ram-via-async-prefetch-303588314935`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
