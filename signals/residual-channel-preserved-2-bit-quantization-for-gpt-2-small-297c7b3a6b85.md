# Residual-Channel-Preserved 2-bit Quantization for GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-preserved-2-bit-quantization-for-gpt-2-small-297c7b3a6b85`
Run ID: `residual-channel-preserved-2-bit-quantization-for-gpt-2-small-297c7b3a6b85-20260524T191711961947+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5c558e37ba4a

## What looked useful

Naive high-activation residual-channel preservation is an early negative in this setup despite lower weight MSE. Residual-channel preservation selected by quantization-error concentration gave a concrete positive mechanism signal at 5% preserved weight fraction, reducing loss from 35.6891 to 22.8783 versus all-2bit, but still with unusably high perplexity and insufficient benchmark coverage.

## Boundaries and scale limits

Tiny local validation corpus; no WikiText/LAMBADA or downstream benchmarks; no packed 2-bit kernel; no multi-seed random-control sweep; no quantization-aware fine-tuning; no deployment throughput or compression measurement.

## Claim scope

Bounded GPT-2-small proxy: per-output affine 2-bit quantization of transformer linear/Conv1D weights with residual-channel preservation evaluated on a 378-token local validation set. Activation-selected residual channels worsened loss at 1%, 2%, and 5% budgets; quantization-error-selected residual channels improved over all-2bit at 5% but remained far from FP32.

## Why it stopped

No-paper closure: this was a short direct/proxy GPT-2-small experiment, sufficient to falsify the activation heuristic locally and identify a promising selector, but not sufficient for a publication or deployment claim.

## Recommended next action

Run a bounded WikiText-2 or WikiText-103 follow-up comparing all-2bit, activation-top, weight-error-top, and 5 random-preserve seeds at matched 1%, 2%, 5%, and 10% preservation budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Benchmark weight-error residual-channel preservation for GPT-2-small 2-bit quantization
- Success threshold: Weight-error residual-channel preservation recovers at least 20% of the FP32-to-all-2bit loss gap and beats the mean random-preserve control by at least one random-control standard deviation at the same storage budget.
- Stop condition: Stop if weight-error residual preservation fails to beat all-2bit and random-preserve controls at 5% and 10% budgets on the public validation set.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-preserved-2-bit-quantization-for-gpt-2-small-297c7b3a6b85`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
