# Residual-KV Extreme Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-kv-extreme-quantization-5b21568a3e19`
Run ID: `residual-kv-extreme-quantization-5b21568a3e19-20260604T191831003922+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a91f0529d9f4

## What looked useful

WikiText-2 confirmation: int4_r0 delta NLL +0.032 at 0.266 estimated cache ratio; raw int2_r0 delta NLL +2.371 and raw int1_r0 +2.133 were damaging; adding a 64-token fp16 residual window improved int2 to +0.356 at 0.356 cache ratio and int1 to +0.222 at 0.309 cache ratio.

## Boundaries and scale limits

Small GPT-2 model only; 256-token contexts; 2,040 scored tokens per confirmation run; no packed low-bit attention kernels; no real serving memory allocator measurement; no larger-model, long-context, downstream generation, or production-kernel validation.

## Claim scope

On GPT-2 small at 256-token contexts, a recent fp16 residual KV window materially reduces quality loss from extreme 1-bit/2-bit old-cache quantization; 4-bit old-cache quantization is near fp16 baseline in this quantize-dequantize harness.

## Why it stopped

The result is a bounded small-model quality simulation that supports the residual-window mechanism but is not full validation of extreme KV quantization for production or long-context LLMs.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is a deeper validation on a larger open model with 1k-4k contexts and the same fp16/int4/raw-extreme/residual-extreme NLL controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Longer-context residual extreme KV quantization on a larger open LM
- Success threshold: Residual extreme KV variants should keep perplexity ratio <= 1.25 versus fp16 while estimated cache footprint is <= 0.40 of fp16 on at least 20k scored benchmark tokens.
- Stop condition: Stop as negative if residual int1/int2 variants exceed 1.5 perplexity ratio versus fp16 or fail to outperform int4 on memory-quality tradeoff at 1k+ context.

## Evidence references

- Artifact root: `<local-path>/projects/residual-kv-extreme-quantization-5b21568a3e19`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
