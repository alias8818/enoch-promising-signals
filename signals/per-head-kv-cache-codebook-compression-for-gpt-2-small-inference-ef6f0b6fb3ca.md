# Per-head KV cache codebook compression for GPT-2-small inference

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `per-head-kv-cache-codebook-compression-for-gpt-2-small-inference-ef6f0b6fb3ca`
Run ID: `per-head-kv-cache-codebook-compression-for-gpt-2-small-inference-ef6f0b6fb3ca-20260601T081914039421+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/14a984222a59

## What looked useful

Simple per-vector int8 reconstruction was essentially loss-neutral on the bounded probe, while per-head k-means codebooks with k=16, k=64, and k=256 increased NLL by about +1.83, +1.05, and +0.96 respectively. k=256 also exceeded fp16 storage for a single 128-token request when codebook bytes were counted.

## Boundaries and scale limits

This run tested a bounded GPT-2-small setting only: 64 held-out continuation tokens, prefix length 128, small calibration data, no optimized cache kernels, no long-context serving, no larger models, and no alternative residual/product/attention-aware codebook variants.

## Claim scope

On GPT-2-small with 128-token WikiText-2 prefixes, 8 calibration sequences, and 4 held-out evaluation sequences, naive per-layer/per-head static vector k-means codebooks for KV-cache reconstruction caused large next-token NLL and KL drift despite high amortized compression ratios.

## Why it stopped

Early direct falsification, not full validation: real GPT-2-small KV-cache injection showed large behavior degradation for naive per-head vector codebooks on held-out continuations.

## Recommended next action

Stop this naive codebook path as no-paper evidence; only revisit with a bounded residual/product-quantized or normalized variant that first beats the int8 baseline on GPT-2-small NLL/KL at a useful byte ratio.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual or product-quantized per-head KV cache codebooks for GPT-2-small
- Success threshold: At least 4x storage reduction versus fp16 with delta NLL <= 0.05 and KL <= 0.02 on held-out GPT-2-small continuations, while matching or beating the int8 baseline after metadata accounting.
- Stop condition: Stop if the best bounded variant has delta NLL > 0.10 or KL > 0.05 at 4x storage reduction, or if metadata/codebook overhead eliminates storage benefit at 512-token prefixes.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-kv-cache-codebook-compression-for-gpt-2-small-inference-ef6f0b6fb3ca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
