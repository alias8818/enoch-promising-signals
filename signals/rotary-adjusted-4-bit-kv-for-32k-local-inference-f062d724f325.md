# Rotary-Adjusted 4-bit KV for 32k Local Inference

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `rotary-adjusted-4-bit-kv-for-32k-local-inference-f062d724f325`
Run ID: `rotary-adjusted-4-bit-kv-for-32k-local-inference-f062d724f325-20260528T011511024659+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9bff071dd906

## What looked useful

In anisotropic rotary-pair synthetic keys, the simple rotary-adjusted placement consistently worsened attention-logit MSE versus quantizing rotated K directly; output MSE was mixed and therefore not reliable as the primary early metric.

## Boundaries and scale limits

No trained LLM KV traces, no perplexity or generation-quality test, no packed int4 kernel throughput measurement, and no end-to-end local inference benchmark.

## Claim scope

Synthetic CUDA attention probe up to 32,768 tokens comparing symmetric int4 quantization of already-rotated K against quantization of unrotated K followed by RoPE after dequantization; V quantization was identical in both paths.

## Why it stopped

Proxy synthetic mechanism test, not full validation, falsified the core KV-fidelity mechanism for the simple pre-RoPE int4 K-cache placement.

## Recommended next action

Stop this simple variant as an early synthetic falsification; only revisit with real RoPE LLM KV traces and identical cache quantizers if the objective is end-to-end model evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV trace test for rotary-adjusted int4 cache placement
- Success threshold: Rotary-adjusted int4 must reduce attention-logit MSE by at least 10% and not degrade perplexity or long-context task accuracy versus rotated-K int4 on real model traces.
- Stop condition: Stop if real-model trace logit MSE is not better than the rotated-K int4 baseline at both 8k and 32k, even if a few output samples improve after softmax/value mixing.

## Evidence references

- Artifact root: `<local-path>/projects/rotary-adjusted-4-bit-kv-for-32k-local-inference-f062d724f325`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
