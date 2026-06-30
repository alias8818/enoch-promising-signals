# Adaptive-rank LoRA on 4-bit base for home GPUs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-rank-lora-on-4-bit-base-for-home-gpus-9610a4c89cdc`
Run ID: `adaptive-rank-lora-on-4-bit-base-for-home-gpus-9610a4c89cdc-20260602T165009551009+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/3398ca971db3

## What looked useful

Adaptive rank allocation produced a consistent 17.4% lower mean validation MSE than same-budget fixed rank in the corrected proxy run, while remaining worse than a much larger fixed high-rank reference.

## Boundaries and scale limits

Tested only synthetic linear residuals with three 192x192 modules, five seeds, deterministic int4 dequantization, and short runs on a GB10. Not tested on transformer fine-tuning, real datasets, NF4/bitsandbytes kernels, or LLM-scale memory and throughput.

## Claim scope

In a self-contained synthetic CUDA proxy with frozen symmetric groupwise int4 base weights and uneven per-module residual ranks [2, 8, 14], adaptive LoRA rank allocation reached ranks [2, 8, 8] and reduced validation MSE versus uniform fixed rank [6, 6, 6] at the same trainable parameter count.

## Why it stopped

This run produced only proxy evidence; it supports a mechanism but does not provide direct LLM fine-tuning evidence or paper-ready validation.

## Recommended next action

Run a bounded GPT-2-small-class 4-bit QLoRA fine-tune with matched trainable-parameter fixed-rank controls and record validation loss, memory, and throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class adaptive-rank QLoRA confirmation
- Success threshold: Adaptive rank achieves at least 5% lower validation loss than matched fixed-rank LoRA or matches loss with at least 20% fewer trainable parameters, without exceeding fixed-rank peak memory.
- Stop condition: Stop if adaptive rank fails to beat matched fixed-rank validation loss in two independent small-model runs or if allocator overhead removes home-GPU feasibility.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-rank-lora-on-4-bit-base-for-home-gpus-9610a4c89cdc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
