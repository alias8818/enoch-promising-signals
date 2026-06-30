# QA-Training 124M on 6GB via 2-bit Weights and FP16 Residual Gradients

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `qa-training-124m-on-6gb-via-2-bit-weights-and-fp16-residual-gradients-a63a088d3af2`
Run ID: `qa-training-124m-on-6gb-via-2-bit-weights-and-fp16-residual-gradients-a63a088d3af2-20260602T134020554690+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/42f8898fb57d

## What looked useful

The 2-bit packed base representation reduced persistent base-weight storage to about 29.5 MiB for the 123.85M-parameter shape, but the full FP16 residual tensors and gradients each still used about 236.2 MiB. The quantized-residual path peaked higher than the dense FP16 SGD control at the same shape, 810.10 MiB vs 708.23 MiB, likely because dequantized weights were materialized transiently.

## Boundaries and scale limits

No real QA dataset, pretrained initialization, validation metric, long-run convergence, AdamW optimizer-state pressure, activation checkpointing, or fused low-bit kernel was tested. The result is allocator-feasibility evidence, not QA training quality evidence.

## Claim scope

A synthetic GPT-2-small-class train-step harness with 123.85M logical parameters, sequence length 256, batch size 1, FP16 residual trainable tensors, and SGD completed forward/loss/backward/update on NVIDIA GB10 with 810.10 MiB max CUDA allocated, under a 6 GiB allocator budget.

## Why it stopped

Mixed bounded result: synthetic 124M-class train steps fit under 6 GiB, but the tested 2-bit-base plus full FP16 residual mechanism did not improve CUDA peak memory versus dense FP16 SGD and did not test QA accuracy or convergence.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should use a real QA batch and optimizer-state controls before any larger training claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real QA optimizer-state comparison for 124M low-bit residual training
- Success threshold: Low-bit residual training must complete the same QA fine-tuning workload under 6 GiB, reduce peak CUDA allocation by at least 25% versus the strongest dense optimizer-state control, and show non-divergent held-out loss over a bounded run.
- Stop condition: Stop if dense controls fit under 6 GiB with equal or lower peak memory, if low-bit residual loss diverges, or if transient dequantization remains the dominant peak-memory cost.

## Evidence references

- Artifact root: `<local-path>/projects/qa-training-124m-on-6gb-via-2-bit-weights-and-fp16-residual-gradients-a63a088d3af2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
