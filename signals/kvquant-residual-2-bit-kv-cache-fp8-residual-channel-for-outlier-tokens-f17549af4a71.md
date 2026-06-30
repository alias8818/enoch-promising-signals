# KVQuant+Residual: 2-bit KV cache + FP8 residual channel for outlier tokens

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kvquant-residual-2-bit-kv-cache-fp8-residual-channel-for-outlier-tokens-f17549af4a71`
Run ID: `kvquant-residual-2-bit-kv-cache-fp8-residual-channel-for-outlier-tokens-f17549af4a71-20260619T233022224296+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c33550975a42

## What looked useful

The residual-token mechanism is strong when quantization error is concentrated in outlier tokens, but the no-outlier control shows it is not a general substitute for 3-bit KV quantization. It is worth one bounded real-KV follow-up, not paper writing.

## Boundaries and scale limits

Synthetic tensor-only probe on GB10; no real transformer KV traces, no perplexity or task accuracy, no pre-RoPE/per-channel KVQuant reproduction, no packed-cache kernel latency, and only three seeds at sequence length 2048.

## Claim scope

On synthetic heavy-tailed KV tensors with token-local outliers, selecting the highest-error 2% of KV tokens and storing FP8 residual vectors can reduce attention-output error far below plain 2-bit and plain 3-bit quantization at about 2.29 effective bits per element.

## Why it stopped

Stopped after a calibrated synthetic proxy and control produced useful but non-paper evidence; the result does not validate real model accuracy or serving performance.

## Recommended next action

Run a bounded real-KV trace follow-up on a small pretrained transformer, comparing plain Q2/Q3, Q2 plus FP8 token residuals, and a simple sparse element residual under identical perplexity or attention-output metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-transformer KV trace test for Q2 plus FP8 token residuals
- Success threshold: At 1-2% residual tokens, Q2 plus FP8 token residuals must beat plain Q3 attention-output error or perplexity degradation while using at least 15% fewer effective bits per KV element.
- Stop condition: Stop if real KV quantization error is not token-concentrated or if Q2 plus FP8 token residuals fails to beat plain Q3 at an equal or lower effective bit budget.

## Evidence references

- Artifact root: `<local-path>/projects/kvquant-residual-2-bit-kv-cache-fp8-residual-channel-for-outlier-tokens-f17549af4a71`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
