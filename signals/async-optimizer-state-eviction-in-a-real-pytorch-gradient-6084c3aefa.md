# Async optimizer-state eviction in a real PyTorch gradient-accumulation loop

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `async-optimizer-state-eviction-in-a-real-pytorch-gradient-6084c3aefa`
Run ID: `async-optimizer-state-eviction-in-a-real-pytorch-gradient-6084c3aefa-20260525T093341052052+0000`

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

- Parent run decision: Gradient accumulation with optimizer state eviction between steps: enoch://control-plane/projects/gradient-accumulation-with-optimizer-state-eviction-between-steps-0c7d9d25a649/runs/gradient-accumulation-with-optimizer-state-eviction-between-steps-0c7d9d25a649-20260525T090311107900+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/de2d5cca39c6

## What looked useful

The mechanism is control-flow-correct in a real PyTorch gradient-accumulation loop: 20-step controlled run had max_abs_param_diff 0.0 with +0.47% wall-time overhead while evicting 26,509,608 bytes of AdamW state; larger 12-step run with accumulation 16 had max_abs_param_diff 2.05e-6 and 103,350,568 bytes represented by eviction. This is useful engineering evidence but not publication-grade memory evidence.

## Boundaries and scale limits

No CUDA device was available, so this run does not directly validate GPU memory reduction, CUDA stream overlap, pinned-memory transfer behavior, allocator fragmentation, or large-model training throughput. CPU RSS increased because CPU was both the training device and eviction target.

## Claim scope

On a CPU-only PyTorch 2.12 worker, an async optimizer-state eviction wrapper around torch.optim.AdamW can run inside a real gradient-accumulation loop, install placeholders during accumulation, restore state before optimizer.step(), and preserve final parameters exactly or within small floating-point tolerance while handling 26 MB to 103 MB of AdamW state.

## Why it stopped

Closed as no-paper useful signal: Tier 1 direct PyTorch loop correctness was validated, but the available CPU-only host cannot prove the core GPU memory-saving claim.

## Recommended next action

Run the same script on a single CUDA GPU with optimizer state resident on GPU and require torch.cuda.max_memory_allocated/reserved to fall by at least 70% of AdamW state bytes during accumulation with no more than 10% throughput loss and max_abs_param_diff <= 1e-5.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Single-GPU CUDA validation of async AdamW state eviction during gradient accumulation
- Success threshold: CUDA allocated or reserved memory during accumulation drops by at least 70% of measured AdamW state bytes versus baseline, final max_abs_param_diff <= 1e-5, and throughput overhead <= 10%.
- Stop condition: Stop if the CUDA run cannot reduce memory by at least 30% of AdamW state bytes, if parameter divergence exceeds 1e-5 under deterministic settings, or if eviction/restore overhead exceeds 25% after basic pinned-memory/nonblocking-copy tuning.

## Evidence references

- Artifact root: `<local-path>/projects/async-optimizer-state-eviction-in-a-real-pytorch-gradient-6084c3aefa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
