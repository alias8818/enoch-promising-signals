# Paged AdamW: CPU-offloaded states with async prefetch

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `paged-adamw-cpu-offloaded-states-with-async-prefetch-43fb13248b59`
Run ID: `paged-adamw-cpu-offloaded-states-with-async-prefetch-43fb13248b59-20260628T141342009160+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/dc6d1b4c93e6

## What looked useful

CPU-offloaded paged AdamW with async next-page prefetch is correct in the tested harness and partially hides paging overhead, but the throughput penalty versus full GPU-state AdamW remains large. The result is useful as a bounded implementation/performance signal, not a paper-ready validation.

## Boundaries and scale limits

Synthetic optimizer-only benchmark; no real transformer training loop, no autograd integration, no mixed precision, no distributed sharding, no convergence data, and no comparison to production fused/offload optimizers. Async offload remained 1.65x-2.48x slower than GPU-resident AdamW moments in the tested 64M-parameter sweep.

## Claim scope

On GB10 with PyTorch 2.12/CUDA 13, synthetic flat fp32 AdamW tensors up to 64M parameters can keep first/second moments in pinned CPU memory and use double-buffered async page prefetch with exact agreement to a GPU-state AdamW baseline. Async prefetch improved synchronous CPU-state offload by 1.04x-1.18x while reducing GPU-resident moment storage by 2x-32x depending on page size.

## Why it stopped

Synthetic proxy evidence supports the mechanism but is not a full validation and remains slower than GPU-state AdamW; close this run as a useful no-paper signal.

## Recommended next action

Run a bounded direct training-loop follow-up on a GPT-2-small-class or smaller transformer to test whether the memory saving enables a larger batch/model with acceptable tokens-per-second and unchanged loss curves.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Paged AdamW async prefetch in a real transformer training loop
- Success threshold: Async CPU-state paging must match loss curves within run noise, reduce peak GPU optimizer-state memory enough to enable at least a 1.5x larger batch or otherwise infeasible configuration, and keep end-to-end training throughput at least 60% of the GPU-state feasible baseline.
- Stop condition: Stop if async offload fails correctness/convergence, cannot enable a larger feasible configuration, or end-to-end throughput falls below 60% of the GPU-state baseline in the bounded training loop.

## Evidence references

- Artifact root: `<local-path>/projects/paged-adamw-cpu-offloaded-states-with-async-prefetch-43fb13248b59`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
