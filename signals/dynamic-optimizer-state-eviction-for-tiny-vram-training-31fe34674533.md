# Dynamic Optimizer State Eviction for Tiny-VRAM Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `dynamic-optimizer-state-eviction-for-tiny-vram-training-31fe34674533`
Run ID: `dynamic-optimizer-state-eviction-for-tiny-vram-training-31fe34674533-20260602T211743804112+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/13108353904e

## What looked useful

Dynamic optimizer-state eviction works mechanically in this bounded CUDA test: AdamW moment tensors can live on CPU between updates, preserving numerics while reducing peak GPU allocation. The naive implementation is slow, running at about 0.39x standard AdamW throughput with pageable CPU state and about 0.47x with pinned CPU state.

## Boundaries and scale limits

Evidence is synthetic and short-run only: no real transformer/data task, no enforced tiny-VRAM cap or baseline OOM boundary, no multi-hour convergence, no distributed optimizer comparison, and no async prefetch/overlap optimization.

## Claim scope

On a GB10 CUDA worker, a naive CPU-evicted AdamW implementation for a deterministic 100.7M-parameter synthetic residual MLP removed persistent optimizer moments from GPU state, reduced peak CUDA allocation by about 704 MiB versus standard AdamW, and preserved the loss trajectory to numerical precision over 20 steps.

## Why it stopped

Bounded synthetic evidence supports the mechanism but is not direct or broad enough for a paper-ready claim.

## Recommended next action

Stop this run as no-paper useful-signal evidence; deepen with a real small transformer under an enforced CUDA memory budget and compare OOM boundary, convergence, and throughput against AdamW plus a standard memory-saving baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer Memory-Cap Test for CPU-Evicted AdamW
- Success threshold: Evicted AdamW fits at least one transformer configuration or batch size that standard AdamW cannot fit under the same memory cap, final validation loss is within 2% of the unconstrained baseline at matched tokens, and throughput remains at least 0.35x standard AdamW.
- Stop condition: Stop if the evicted optimizer cannot produce a real memory-cap fit advantage, diverges beyond the 2% validation-loss tolerance, or sustained throughput falls below 0.35x after pinned-memory and simple prefetch tuning.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-optimizer-state-eviction-for-tiny-vram-training-31fe34674533`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
