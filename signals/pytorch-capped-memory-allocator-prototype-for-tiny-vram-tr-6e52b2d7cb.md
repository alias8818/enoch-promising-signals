# PyTorch capped-memory allocator prototype for tiny-VRAM training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `pytorch-capped-memory-allocator-prototype-for-tiny-vram-tr-6e52b2d7cb`
Run ID: `pytorch-capped-memory-allocator-prototype-for-tiny-vram-tr-6e52b2d7cb-20260614T111431985340+0000`

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

- Parent run decision: Dynamic Memory Allocator for tiny-VRAM Training: enoch://control-plane/projects/dynamic-memory-allocator-for-tiny-vram-training-5595d915338f/runs/dynamic-memory-allocator-for-tiny-vram-training-5595d915338f-20260614T105139548116+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/49180dbfc469

## What looked useful

The cap-aware prototype respected hard PyTorch allocator caps and recovered from a real 768 MiB-cap OOM by reducing microbatch 8 to 4 while preserving effective batch through accumulation. Baseline failed at 768, 1024, and 1536 MiB caps.

## Boundaries and scale limits

Small direct test only: synthetic random token data, one seed, fp32 SGD, three optimizer steps, one GPU, no convergence claim, no long-run fragmentation study, no GPT-2-small-class baseline, and no allocator-internal C++/CUDA implementation.

## Claim scope

Under artificial 768-1536 MiB PyTorch CUDA per-process memory caps on a GB10, a training-loop prototype using activation checkpointing plus OOM-triggered microbatch reduction completed three optimizer steps for a 49.2M-parameter Transformer-like workload at effective batch 8, while the full-microbatch baseline failed before step 1.

## Why it stopped

Tier 1 direct evidence supports the mechanism but remains no-paper because the prototype is training-loop-level, small, synthetic, and short-run rather than allocator-internal or publication-grade.

## Recommended next action

Run a bounded deepen test with checkpoint-only, microbatch-only, and combined cap-aware controls over a longer AdamW language-model training run before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Controlled ablation of cap-aware checkpointing and microbatch scheduling
- Success threshold: Combined cap-aware policy completes at least 500 optimizer steps under the lowest cap where at least one control fails, with peak reserved memory below the configured cap and final/median loss within 5% of the best completing control.
- Stop condition: Stop if all controls complete with similar memory and throughput, or if the combined policy cannot complete after retrying down to microbatch 1 under a cap above fixed model-state memory.

## Evidence references

- Artifact root: `<local-path>/projects/pytorch-capped-memory-allocator-prototype-for-tiny-vram-tr-6e52b2d7cb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
