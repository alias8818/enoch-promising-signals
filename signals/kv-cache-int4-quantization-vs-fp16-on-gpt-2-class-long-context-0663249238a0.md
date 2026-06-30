# KV-cache int4 Quantization vs FP16 on GPT-2-class Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-int4-quantization-vs-fp16-on-gpt-2-class-long-context-0663249238a0`
Run ID: `kv-cache-int4-quantization-vs-fp16-on-gpt-2-class-long-context-0663249238a0-20260620T132642237555+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/330adaeef2cf

## What looked useful

Int4 KV-cache compression works as a storage representation and per-vector scaling is much less damaging than per-tensor scaling, but naive dequantize/requantize around stock GPT-2 attention loses the expected serving advantage. Future work should focus on direct int4-KV attention or amortized dequantization rather than only changing cache storage.

## Boundaries and scale limits

No natural-language corpus quality evaluation, no fused int4 attention kernel, no batch-size sweep, no contexts beyond GPT-2-small's 1024 native positions, and only 16 decode steps per context length. The evidence is a bounded GPU mechanism benchmark, not a production-serving validation.

## Claim scope

On GPT-2-small with random-token prompts, batch size 1, native 1024-position limit, and 16 decode steps, packed symmetric int4 KV-cache storage reduces KV memory by 3.765x to 4.00x versus FP16, but a stock Transformers implementation that dequantizes KV before each forward pass is 2.2x to 3.2x slower per generated token than FP16. Per-vector scales reduce logit drift substantially versus per-tensor scales but do not eliminate output changes.

## Why it stopped

Proxy/direct bounded evidence: direct GPT-2-small GPU cache measurements show memory compression but slower decode for the naive int4 path, so this does not support a paper-ready positive claim.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded action is an optimized int4-KV attention/dequantization experiment on real text, not a larger version of the same naive dequantize-before-forward loop.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized int4 KV attention path for GPT-2-small on real text
- Success threshold: At least 3.5x KV-cache memory reduction, no more than 20% end-to-end decode latency overhead versus FP16, top-1 agreement above 90% or perplexity degradation below 5% on the fixed text slice.
- Stop condition: Stop if optimized int4-KV decode remains more than 50% slower than FP16 or if text perplexity degradation exceeds 10% after per-vector scaling.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-int4-quantization-vs-fp16-on-gpt-2-class-long-context-0663249238a0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
