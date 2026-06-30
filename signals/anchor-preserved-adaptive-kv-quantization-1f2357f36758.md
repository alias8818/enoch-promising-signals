# Anchor-Preserved Adaptive KV Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-preserved-adaptive-kv-quantization-1f2357f36758`
Run ID: `anchor-preserved-adaptive-kv-quantization-1f2357f36758-20260525T092103549578+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f262c98f3c9e

## What looked useful

Anchor-preserved KV quantization is not automatically beneficial under a fixed memory budget. It improves synthetic attention-output error only when anchor attention is sufficiently concentrated; otherwise reallocating bits away from non-anchor tokens causes higher error than uniform quantization.

## Boundaries and scale limits

No real model perplexity or generation evaluation, no packed KV kernels, no end-to-end latency measurement, no learned/runtime anchor selector, and no production serving workload. The result is a mechanism probe, not a full model validation.

## Claim scope

Synthetic CUDA attention probe with 3.125% anchor tokens, sequence length 2048, 8 heads, head dimension 64, and per-token symmetric KV quantize/dequantize. Budget-matched anchor preservation beats uniform int4 only when anchors receive high attention mass, about 13% to 20% in the sweep; it loses when anchor mass is about 3% to 8%.

## Why it stopped

No-paper useful signal: this was a synthetic mechanism probe, and the fixed-budget result is mixed rather than broadly supportive. It is an early conditional finding, not full validation.

## Recommended next action

Run a bounded real-model trace experiment on a small autoregressive LM comparing uniform KV quantization against budget-matched anchor-preserved quantization, and stop unless real traces show stable high anchor attention mass plus lower perplexity or generation loss at equal memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model trace test for budget-matched anchor-preserved KV quantization
- Success threshold: At equal effective KV bits, anchor-preserved adaptive quantization reduces next-token KL or perplexity degradation by at least 10% versus uniform quantization on layers/heads with stable anchor mass above the synthetic threshold, without worse aggregate model quality.
- Stop condition: Stop if real traces rarely show small anchor sets capturing at least 10% to 13% attention mass, or if matched-budget anchor preservation fails to beat uniform quantization on next-token KL/perplexity.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-preserved-adaptive-kv-quantization-1f2357f36758`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
