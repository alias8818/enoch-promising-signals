# Memory-Mapped Optimizer Paging with Async Prefetch for Tiny-VRAM Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `memory-mapped-optimizer-paging-with-async-prefetch-for-tiny-vram-training-cecd87bcf2ae`
Run ID: `memory-mapped-optimizer-paging-with-async-prefetch-for-tiny-vram-training-cecd87bcf2ae-20260529T001240997861+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b40ae817e9c8

## What looked useful

Async prefetch is mechanically effective for hiding mmap read wait, reducing visible load wait by about 95.5% and chunk-timed work by about 12.0%, but writeback/flush and CUDA update costs dominated end-to-end time and made the practical speedup small and noisy.

## Boundaries and scale limits

Synthetic optimizer loop only; no real transformer training, no final-loss equivalence check, no checkpoint/dataloader interaction, no discrete tiny-VRAM OOM comparison, and state size was 0.75 GiB rather than multi-GB optimizer state from a full model.

## Claim scope

On a GB10 local synthetic chunked Adam benchmark with 0.75 GiB of memmap-backed optimizer state, one-thread async prefetch hid most measured memmap load wait but produced only about 1.2% mean end-to-end throughput gain versus synchronous mmap loading.

## Why it stopped

No-paper closure: bounded proxy evidence supports the prefetch mechanism but does not support a publication-grade or practically meaningful training-system claim.

## Recommended next action

Run a bounded real-training follow-up on a GPT-2-small-class or smaller transformer with an intentionally constrained optimizer-state budget, comparing standard optimizer placement, synchronous mmap paging, and mmap paging with async prefetch while checking loss equivalence and including writeback/checkpoint costs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real transformer training validation for mmap optimizer paging with async prefetch
- Success threshold: Async-prefetched mmap paging must match baseline loss within tolerance and improve end-to-end throughput by at least 10% over synchronous mmap paging, or enable a model/batch configuration that the standard optimizer-state placement cannot run locally.
- Stop condition: Stop if loss diverges, memory pressure triggers early termination, or async prefetch improves end-to-end throughput by less than 5% after a calibrated short training window.

## Evidence references

- Artifact root: `<local-path>/projects/memory-mapped-optimizer-paging-with-async-prefetch-for-tiny-vram-training-cecd87bcf2ae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
