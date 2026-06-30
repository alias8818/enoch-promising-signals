# 2-bit KV Cache with Channel-Wise Residuals for 32k Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-kv-cache-with-channel-wise-residuals-for-32k-context-354eef9dd976`
Run ID: `2-bit-kv-cache-with-channel-wise-residuals-for-32k-context-354eef9dd976-20260522T144627117639+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bd4403e6afb2

## What looked useful

Mean channel-wise residuals recover only small reconstruction error at 2 bits: across all cases, symmetric 2-bit K/V rel-MSE improved about 1% and affine 2-bit improved about 3-4%, while attention-output error was inconsistent. At 32768 context, residual variants worsened attention-output relative MSE in all six base-vs-residual pairs while reducing compression from 7.11x to 6.74x versus fp16.

## Boundaries and scale limits

This was a synthetic attention-mechanism benchmark, not a trained 32k-context LLM perplexity, generation-quality, or optimized serving benchmark. It used 16 heads, head dimension 128, block size 128, and three controlled KV distributions on one GB10 GPU.

## Claim scope

A concrete 2-bit KV cache scheme with one fp16 mean channel-wise residual per head/block/channel was tested on synthetic K/V tensors up to 32768 context. The residual slightly reduced raw K/V reconstruction error but did not preserve attention-output fidelity and often worsened attention-output relative MSE.

## Why it stopped

The result is not a full 32k LLM validation, but the tested residual mechanism failed the local attention-fidelity success condition: at 32768 context it slightly improved reconstruction MSE while worsening attention-output relative MSE in every tested distribution/family pair.

## Recommended next action

Stop this project as a proxy/direct-attention early falsification of simple mean channel-wise residuals; if continuing locally, run a bounded real-activation follow-up on a small trained decoder with perplexity/logit-divergence controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Activation 2-bit KV Residual Check on a Small Decoder
- Success threshold: Residual 2-bit KV must reduce next-token logit KL or perplexity degradation by at least 25% versus affine 2-bit KV without losing more than 10% of its compression advantage, and must beat a value-only residual control.
- Stop condition: Stop if residual 2-bit fails to improve logit KL/perplexity over affine 2-bit by at least 10% on two prompt sets or remains clearly worse than 4-bit KV at comparable implementation complexity.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-channel-wise-residuals-for-32k-context-354eef9dd976`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
