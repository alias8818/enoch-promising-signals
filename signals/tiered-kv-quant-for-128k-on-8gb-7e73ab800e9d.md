# Tiered KV-Quant for 128k on 8GB

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiered-kv-quant-for-128k-on-8gb-7e73ab800e9d`
Run ID: `tiered-kv-quant-for-128k-on-8gb-7e73ab800e9d-20260527T234026304515+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c5dcc7df3333

## What looked useful

For 32-KV-head MHA, even uniform int2 with conservative token scales is 8.5 GiB, so the tested tiered schemes do not fit an 8 GiB KV budget. For 8-KV-head GQA, uniform int4 already fits at 4.125 GiB with scales; aggressive 2-bit far tiering has high synthetic attention error, while 3-bit far tiering improves over uniform int3 but remains worse than uniform int4.

## Boundaries and scale limits

No full transformer inference, no real-model K/V distributions, no perplexity or long-context benchmark, no packed KV kernel implementation, and no direct 128k serving run.

## Claim scope

Closed-form 128k KV-cache memory accounting for representative MHA/GQA/MQA shapes plus synthetic single-query attention-error probes up to 65,536 tokens on GB10/CUDA.

## Why it stopped

Proxy evidence does not support the broad 128k-on-8GB tiered KV-quant claim: MHA does not fit, GQA already fits with uniform int4, and 2-bit far tiering harms synthetic attention.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should use a real small GQA model with pseudo-quantized KV and compare tier 3/4/8 against uniform int3 and int4 on long-context retrieval or perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model GQA KV tiering versus uniform int3/int4
- Success threshold: Tier 3/4/8 must reduce KV memory by at least 15% versus uniform int4 while matching at least 95% of uniform-int4 task accuracy or perplexity delta, and must outperform uniform int3 by at least 20% relative error reduction.
- Stop condition: Stop if tier 3/4/8 is not clearly better than uniform int3 on real-model quality, or if uniform int4 memory is already sufficient for the target local model and tiering adds quality loss without enabling a new context/model configuration.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-kv-quant-for-128k-on-8gb-7e73ab800e9d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
