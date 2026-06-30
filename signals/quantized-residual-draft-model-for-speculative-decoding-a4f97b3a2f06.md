# Quantized Residual Draft Model for Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quantized-residual-draft-model-for-speculative-decoding-a4f97b3a2f06`
Run ID: `quantized-residual-draft-model-for-speculative-decoding-a4f97b3a2f06-20260522T150454526248+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bd4403e6afb2

## What looked useful

Across smoke, main, and stronger-residual synthetic runs, 4-bit and 8-bit top-k residual corrections increased exact speculative acceptance over the base draft. Main run improved from 0.9577 baseline to 0.9677 with top-k 8 4-bit residuals at 16 bytes/context and 0.9710 with top-k 32 8-bit residuals at 74 bytes/context. Strong-residual sensitivity improved from 0.9234 baseline to 0.9668 with top-k 8 4-bit and 0.9720 with top-k 32 8-bit. Two-bit residuals were visibly quantization-limited.

## Boundaries and scale limits

No real Transformer training, no learned residual generalization, no real tokenizer/corpus, no multi-token serving benchmark, and no parameter-matched dense neural draft baseline.

## Claim scope

Synthetic contextual-LM probe only: sparse quantized residual-logit corrections to a base draft increase exact one-token speculative acceptance probability and match Monte Carlo draft/verify acceptance checks.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only even though the mechanism is supported.

## Recommended next action

Run a bounded real-LM follow-up: train or distill a residual draft for a GPT-2-small-class target and compare accepted tokens per target forward pass plus latency against a parameter-matched dense draft.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LM Quantized Residual Draft for GPT-2-Small Speculative Decoding
- Success threshold: At least 5% relative improvement in accepted tokens per target forward pass over the uncorrected draft, with end-to-end latency not worse than the matched dense draft at comparable memory.
- Stop condition: Stop if learned residual corrections fail to improve accepted tokens per target forward pass over the uncorrected draft or if residual lookup/dequantization overhead erases latency gains.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-residual-draft-model-for-speculative-decoding-a4f97b3a2f06`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
