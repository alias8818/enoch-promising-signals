# CPU offload of AdamW state with pipelined micro-batch prefetch

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-offload-of-adamw-state-with-pipelined-micro-batch-prefetch-3579560358c6`
Run ID: `cpu-offload-of-adamw-state-with-pipelined-micro-batch-prefetch-3579560358c6-20260620T013658401406+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/daad613fd6bb

## What looked useful

CPU-offloaded AdamW state saved 36-43% peak GPU allocation in this benchmark, but at 268M parameters the optimizer step was still 1.67x slower than all-GPU state with prefetch. Prefetch improved over synchronous CPU staging by about 6% at medium sizes, not enough to support a paper-ready practical speed claim.

## Boundaries and scale limits

Synthetic optimizer-step-only benchmark; no end-to-end transformer training, gradient-accumulation overlap, distributed sharding, convergence validation, or datacenter-scale run. Largest tested case was 268,435,456 float32 parameters and 5 measured optimizer steps per mode.

## Claim scope

On a GB10 with PyTorch 2.12/CUDA 13.0, synthetic CUDA AdamW optimizer-step benchmarks from 8.4M to 268.4M float32 parameters show that CPU-offloading first/second moment state to pinned host memory is correct and saves GPU memory, but a two-slot bucket prefetch pipeline recovers only a small fraction of the synchronous staging overhead.

## Why it stopped

Bounded direct optimizer-step benchmark supports memory savings and correctness but early-falsifies the stronger claim that bucket prefetch alone hides enough AdamW state traffic to preserve practical all-GPU-step performance.

## Recommended next action

Stop this optimizer-step-only variant as no-paper useful signal; the next bounded test should measure H2D state prefetch launched during the final microbatch backward pass in a small real transformer training loop.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end last-microbatch AdamW state prefetch in a small transformer training loop
- Success threshold: Last-microbatch prefetch reaches at least 90% of all-GPU AdamW end-to-end tokens/sec while saving at least 25% peak GPU optimizer-state memory, or enables a strictly larger batch/model that all-GPU AdamW cannot fit with no more than 15% tokens/sec loss versus the largest fitting baseline.
- Stop condition: Stop if H2D prefetch cannot be overlapped with backward in PyTorch without race/synchronization hazards, or if end-to-end throughput remains more than 20% slower than all-GPU AdamW on two parameter scales despite memory savings.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offload-of-adamw-state-with-pipelined-micro-batch-prefetch-3579560358c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
