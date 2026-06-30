# Tiered KV-Cache: Hot FP8 Cold INT4 Residuals

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `tiered-kv-cache-hot-fp8-cold-int4-residuals-39a0d00f9b5d`
Run ID: `tiered-kv-cache-hot-fp8-cold-int4-residuals-39a0d00f9b5d-20260531T140217050347+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a7e78c6c302c

## What looked useful

All-FP8 KV gave 0.026-0.044 relative attention-output RMSE at 2.0x compression. Tiered hot-FP8/cold-INT4 with 6.25% sparse residual channels gave 0.117-0.158 RMSE at 2.57-2.81x compression. Increasing residuals to 25% improved RMSE to 0.098-0.108 at T=4096, but compression dropped to 1.60x, worse than all-FP8.

## Boundaries and scale limits

This run used controlled synthetic KV distributions and dequantized PyTorch attention on one GB10. It did not evaluate real transformer KV traces, model perplexity, paged/fused serving kernels, multi-batch decode, or production latency under memory-bandwidth pressure.

## Claim scope

On synthetic decode-attention KV tensors up to 8192 tokens, batch 1, 8 heads, head dimension 128, a hot-FP8/cold-INT4 cache with sparse FP8-like residual correction does not approach all-FP8 output fidelity before residual metadata removes its memory advantage.

## Why it stopped

Early/proxy falsification: the mechanism was directly tested for attention-output fidelity and storage accounting, but not for full model quality or production serving.

## Recommended next action

Stop this fixed tiered sparse-residual design as no-paper proxy evidence; only revisit if real model KV traces show a different residual distribution that can beat all-FP8 on both quality and metadata-inclusive compression.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/tiered-kv-cache-hot-fp8-cold-int4-residuals-39a0d00f9b5d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
