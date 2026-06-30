# Integer-Quantized KV Cache with Anchor Paging for CPU LLM Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `integer-quantized-kv-cache-with-anchor-paging-for-cpu-llm-inference-6e07ebded11a`
Run ID: `integer-quantized-kv-cache-with-anchor-paging-for-cpu-llm-inference-6e07ebded11a-20260629T100552075953+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/084f73bed7c6

## What looked useful

Integer paged KV storage is the useful mechanism in this bounded test. At 32768 tokens, all-int8 paging used 8.002 MiB vs 32.000 MiB fp32 and ran at 14.693 ms/token vs 21.015 ms/token fp32 contiguous with mean relative L2 error 0.0132. Anchor+recent fp32 pages used 8.283 MiB, ran at 15.629 ms/token, and only improved mean relative L2 to 0.0131.

## Boundaries and scale limits

Not a full LLM serving result: single-head/single-layer proxy, random tensors, NumPy page loops, no perplexity or generation-quality measurement, no optimized kernel, and no multi-model robustness.

## Claim scope

Synthetic CPU decode-attention benchmark over random K/V/Q tensors shows int8 paged KV storage reduces modeled KV memory by about 75% and can beat fp32 contiguous latency at 32768-token context, while anchor/recent fp32 pages provide only marginal numerical-error improvement.

## Why it stopped

Synthetic proxy supports memory savings and large-context latency potential but does not validate the anchor-paging claim strongly enough for a paper.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next bounded action is to test the same KV policies inside a real small CPU LLM decode loop with perplexity/generation quality and tokens/sec.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU LLM Decode Test for Int8 Paged KV Cache
- Success threshold: At long context, int8 paged KV achieves at least 60% KV memory reduction, no worse than 5% tokens/sec regression versus fp32, and quality/logprob degradation within a predeclared tolerance; anchor pages must improve quality enough to justify their extra memory.
- Stop condition: Stop if real-model quality degrades beyond tolerance, if int8 paging remains slower than fp32 at long context after basic implementation tuning, or if anchor pages again provide only marginal quality improvement.

## Evidence references

- Artifact root: `<local-path>/projects/integer-quantized-kv-cache-with-anchor-paging-for-cpu-llm-inference-6e07ebded11a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
