# CPU-based Gradient Checkpointing with Async Offload

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-based-gradient-checkpointing-with-async-offload-060da8064c5d`
Run ID: `cpu-based-gradient-checkpointing-with-async-offload-060da8064c5d-20260609T105100771695+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/befa06f93b7e

## What looked useful

Checkpointing reduced median peak RSS delta to 0.73x baseline with 1.05x wall time. Hook-based offload packed about 284 MB of saved tensors per step. Async packing reduced immediate pack time but increased median peak RSS delta to 1.65x baseline and wall time to 1.13x baseline because pending CPU clones retained memory.

## Boundaries and scale limits

No CUDA/GB10 device was available on this worker, so HBM relief, pinned-memory DMA, PCIe/NVLink transfer overlap, CUDA stream behavior, and real memory-limited training were not tested. The model is toy-scale: hidden 768, depth 8, 512 tokens, one optimizer step per trial.

## Claim scope

CPU-only PyTorch proxy for activation checkpointing and saved-tensor hook offload on a toy transformer-like MLP stack; direct evidence covers wall time, process RSS, saved tensor volume, async pending copies, and CPU copy bandwidth.

## Why it stopped

No-paper useful signal: this is a CPU proxy, not direct accelerator validation, and the async offload variant exposed a memory-retention risk rather than a closed positive result.

## Recommended next action

Stop this CPU-worker run; run a bounded CUDA follow-up with pinned CPU buffers, CUDA streams/events, and GPU memory accounting to test whether async offload reduces HBM by at least 25% with no more than 15% step-time regression.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CUDA pinned-memory validation of async saved-activation offload
- Success threshold: Async offload achieves at least 25% lower peak GPU memory than baseline and no more than 15% median step-time regression, while outperforming plain checkpointing on the memory/time Pareto curve.
- Stop condition: Stop as negative if async offload fails to reduce peak GPU memory by 25%, causes more than 15% step-time regression, or pending copies keep source tensors live long enough to erase most memory relief.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-based-gradient-checkpointing-with-async-offload-060da8064c5d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
