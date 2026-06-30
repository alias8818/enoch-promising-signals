# 4-bit Quantized Training with LoRA on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `4-bit-quantized-training-with-lora-on-gb10-8cf1e30d1921`
Run ID: `4-bit-quantized-training-with-lora-on-gb10-8cf1e30d1921-20260605T105530274318+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/ffc50c4ab94f

## What looked useful

The mechanism works on GB10 and produces a reproducible storage reduction, but generic PyTorch dequantization made int4 about 13.7% slower than bf16 in the matched run and did not reduce peak CUDA allocation at toy scale.

## Boundaries and scale limits

Synthetic data, randomly initialized frozen base, small transformer sizes only; no pretrained model, no real validation set, no optimized NF4/int4 kernels, no paged optimizer, and no long-run convergence or downstream quality evidence.

## Claim scope

On this GB10 host with PyTorch 2.12/CUDA 13, a toy causal LM using frozen symmetric int4-packed linear weights and trainable LoRA adapters can train on GPU, reduce frozen buffer storage by about 4x versus bf16 frozen buffers, and maintain short-run synthetic loss improvement comparable to a bf16 frozen-base LoRA control.

## Why it stopped

The result is a bounded proxy/mechanism validation rather than full validation of 4-bit quantized LoRA training quality.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded direct test should use a GPT-2-small-class pretrained model, real validation data, and production quantized kernels on GB10.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class QLoRA validation on GB10 with real data
- Success threshold: 4-bit LoRA validation loss within 5% of bf16 LoRA control, frozen-weight storage at least 3.5x smaller, and throughput no worse than 25% below bf16 on the same GB10 run.
- Stop condition: Stop if production 4-bit kernels are unavailable on GB10/aarch64, if validation loss diverges or remains more than 10% worse than bf16 after the calibrated budget, or if throughput is more than 50% below bf16 without a compensating memory result.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-quantized-training-with-lora-on-gb10-8cf1e30d1921`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
