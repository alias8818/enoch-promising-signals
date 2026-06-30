# INT8 Quantized Gradient Checkpointing for Home Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-quantized-gradient-checkpointing-for-home-training-440639afb62a`
Run ID: `int8-quantized-gradient-checkpointing-for-home-training-440639afb62a-20260608T125012257256+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/715307f7e303

## What looked useful

INT8 saved-tensor hooks compressed saved activation payloads by about 4x. In the medium run, standalone INT8 reduced 149.07 MiB of saved tensors to 37.32 MiB with 0.999873 gradient cosine and 1.85x CPU time; INT8 plus checkpointing reduced 9.01 MiB to 2.26 MiB with 0.999913 gradient cosine and 1.33x CPU time.

## Boundaries and scale limits

No GPU allocator, CUDA kernels, mixed precision, optimizer-state pressure, real dataset, long-run convergence, or GPT-2-small-class training was tested.

## Claim scope

Bounded CPU PyTorch probe of INT8-compressed autograd saved tensors on transformer-like residual MLP stacks, including comparison with recomputation checkpointing.

## Why it stopped

No-paper closure: this CPU-only probe supports the compression mechanism but is not full validation of home-training usefulness.

## Recommended next action

Run a bounded home-GPU or GB10 follow-up on a GPT-2-small-class model comparing standard checkpointing, INT8 saved tensors, and combined mode for peak memory, tokens/s, and validation loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Home-GPU GPT-2-small INT8 saved-tensor checkpointing validation
- Success threshold: Combined INT8 checkpointing reduces peak allocated memory by at least 20% versus standard checkpointing, validation loss remains within 1% of baseline, and throughput overhead is no more than 25%.
- Stop condition: Stop if gradient error causes unstable loss, validation loss exceeds baseline by more than 3%, or throughput overhead exceeds 50% before any meaningful memory reduction.

## Evidence references

- Artifact root: `<local-path>/projects/int8-quantized-gradient-checkpointing-for-home-training-440639afb62a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
