# Adaptive Backpressure Governor for GPU Work Queue with Anchor-Pinned Compressed Snapshots

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-backpressure-governor-for-gpu-work-queue-with-anchor-pinned-compressed-snapshots-df42b78b7f69`
Run ID: `adaptive-backpressure-governor-for-gpu-work-queue-with-anchor-pinned-compressed-snapshots-df42b78b7f69-20260613T233306275802+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d4d69433c599

## What looked useful

Three replay-verified replicated runs showed adaptive anchor-compressed snapshots cut peak queued snapshot memory by 71.2% versus no-backpressure raw snapshots and 36.5% versus a 1 MiB static raw cap, while p95 latency was 7.2% worse than the static cap and wall time was 1403.6% higher due to CPU compression plus replay verification. The adaptive runs reconstructed 1,044 compressed snapshots with zero mismatches.

## Boundaries and scale limits

Single-process synthetic workload, one GB10, short replicated runs across three seeds, Python/zlib compression, no production request traces, no multi-stream scheduler, no real training/inference checkpoint replay, and no datacenter-scale memory pressure.

## Claim scope

On a local GB10 synthetic GPU work-queue benchmark with bursty arrivals, 64 KiB recoverable snapshots, pinned host anchors, and 2048x2048 FP16 CUDA work, anchor-compressed queued snapshots reduced peak queued snapshot memory versus raw snapshots, but the adaptive governor did not improve tail latency over a static raw memory cap and incurred large CPU compression overhead.

## Why it stopped

The local mechanism signal is useful, but the combined adaptive governor is not supported as a performance improvement: it lowers snapshot memory but does not beat a static cap on tail latency and adds large CPU overhead in the tested implementation.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen test with asynchronous/vectorized compression and a latency-aware controller before considering any larger validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Latency-aware adaptive governor with asynchronous compressed snapshots
- Success threshold: At least 50% lower peak queued snapshot memory than static raw cap while p95 latency is no worse than static raw cap by more than 2% and wall-clock overhead is below 20% across five seeds.
- Stop condition: Stop if asynchronous/vectorized compression still adds more than 20% wall-clock overhead or p95 latency remains worse than static raw cap by more than 2% in two consecutive calibrated runs.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-backpressure-governor-for-gpu-work-queue-with-anchor-pinned-compressed-snapshots-df42b7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
