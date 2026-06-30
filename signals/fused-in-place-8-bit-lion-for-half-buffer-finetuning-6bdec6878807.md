# Fused In-Place 8-bit Lion for Half-Buffer Finetuning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `fused-in-place-8-bit-lion-for-half-buffer-finetuning-6bdec6878807`
Run ID: `fused-in-place-8-bit-lion-for-half-buffer-finetuning-6bdec6878807-20260525T135742286365+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7cb06f40219f

## What looked useful

Fusion is required for the 8-bit state idea to be useful: eager quantization regressed latency, while compiled block-int8 saved roughly 4x state memory and was faster on larger buffers. Quantization drift is small under random-gradient update replay but can hurt convergence; block 64 reduced the toy final-MSE gap from 2.10x to 1.44x versus FP32 at modest memory/speed cost.

## Boundaries and scale limits

No real model finetune, validation loss, LoRA/adapter task, checkpoint-resume test, multi-GPU run, or production CUDA/Triton kernel was tested. Evidence is optimizer-step and toy-convergence only.

## Claim scope

On GB10 with PyTorch 2.12/CUDA 13, synthetic half-precision trainable buffers of 4M-16M elements showed that a torch.compile-fused block-int8 Lion momentum state used about 25-27% of FP32-state memory and improved optimizer-step median latency by 1.35-1.64x versus a compiled FP32-state Lion control; eager int8 was slower, and a toy convex convergence proxy lagged FP32.

## Why it stopped

Closed as no-paper useful signal: local proxy evidence supports a memory/speed mechanism but the convergence proxy is degraded, so the original finetuning viability claim is not directly supported.

## Recommended next action

Run a bounded real small-model finetune comparing compiled FP32-state Lion against block-int8 Lion at block sizes 64/128/256, and stop unless validation loss stays within 1% while preserving a meaningful memory or step-time win.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-finetune validation for fused block-int8 Lion state
- Success threshold: Validation loss within 1% of FP32-state Lion at matched steps, optimizer-state memory at least 3x smaller, and optimizer-step median latency no worse than 1.10x FP32-state Lion on the chosen trainable-buffer size.
- Stop condition: Stop if all tested block sizes exceed 1% validation-loss degradation or if the fastest quality-preserving int8 configuration is slower than 1.10x the compiled FP32-state control.

## Evidence references

- Artifact root: `<local-path>/projects/fused-in-place-8-bit-lion-for-half-buffer-finetuning-6bdec6878807`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
