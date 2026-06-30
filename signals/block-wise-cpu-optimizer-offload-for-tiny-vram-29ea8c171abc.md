# Block-wise CPU Optimizer Offload for Tiny-VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `block-wise-cpu-optimizer-offload-for-tiny-vram-29ea8c171abc`
Run ID: `block-wise-cpu-optimizer-offload-for-tiny-vram-29ea8c171abc-20260628T051606246122+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/3ae7c4efc8f7

## What looked useful

Block-wise moment streaming reduced analytical device-memory residency by 1.88x to 1.98x across the sweep, with CPU proxy step-time overhead from 1.09x to 2.99x and median overhead 1.65x. The mechanism is plausible but not paper-ready without direct tiny-VRAM GPU validation.

## Boundaries and scale limits

No CUDA device was available, so the run did not directly measure VRAM, host-device transfer, CUDA allocator behavior, real model training, or convergence. The largest sweep point used 128 blocks of 262144 fp32 elements per block and 5 optimizer steps.

## Claim scope

CPU proxy timing plus analytical device-memory accounting for block-wise Adam optimizer moment offload on synthetic tensors.

## Why it stopped

Closed as no-paper useful signal because this worker could only produce CPU proxy timing and analytical memory accounting, not direct tiny-VRAM GPU evidence.

## Recommended next action

Run the same harness on a CUDA host with an enforced tiny-VRAM budget and record torch.cuda.max_memory_allocated, OOM/pass behavior, real transfer overhead, and loss parity on a small model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CUDA tiny-VRAM validation for block-wise Adam offload
- Success threshold: Block-wise mode completes a workload that full-state Adam cannot fit under the selected tiny-VRAM budget, keeps measured peak VRAM within 10% of analytical prediction, has mean step-time overhead below 2x, and matches baseline loss within 2% over the short run.
- Stop condition: Stop if block-wise mode exceeds the predicted VRAM budget by more than 25%, cannot complete due to allocator/transfer behavior, has step-time overhead above 3x, or diverges materially from baseline loss in the short run.

## Evidence references

- Artifact root: `<local-path>/projects/block-wise-cpu-optimizer-offload-for-tiny-vram-29ea8c171abc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
