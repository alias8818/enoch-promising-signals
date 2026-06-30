# Per-head KV quantization with downstream perplexity and decode latency

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-head-kv-quantization-with-downstream-perplexity-and-de-90af47cdc3`
Run ID: `per-head-kv-quantization-with-downstream-perplexity-and-de-90af47cdc3-20260604T211251058834+0000`

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

- Parent run decision: Per-head KV cache quantization for long local context: enoch://control-plane/projects/per-head-kv-cache-quantization-for-long-local-context-d59e147960fd/runs/per-head-kv-cache-quantization-for-long-local-context-d59e147960fd-20260604T162252048619+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/787b7ccf8e16

## What looked useful

int8 per-head KV preserved downstream perplexity closely (+0.072%) and reduced estimated cache footprint by about 75%, but naive quantize/dequantize cache handling made decode about 25% slower. int4 reduced estimated cache bytes further but more than doubled perplexity.

## Boundaries and scale limits

Single model, short context, one dataset slice, one GB10 host, and a Python/Hugging Face boundary simulation that estimates compressed cache bytes but does not provide a fused packed-cache attention kernel.

## Claim scope

Tier 1 controlled direct test on GPT-2 small using Wikitext-2 validation text: sequential cached perplexity over 512 tokens and greedy decode latency over 128 generated tokens with FP, int8 per-head, and int4 per-head KV cache variants.

## Why it stopped

Tier 1 direct evidence is useful but mixed: quality supports int8 per-head KV as a mechanism, while the tested implementation is latency-negative and int4 is quality-negative.

## Recommended next action

Stop paper escalation here; run one bounded deepen follow-up implementing an optimized packed int8 KV cache path and test whether longer-context decode recovers latency while keeping perplexity delta under 0.5%.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized packed int8 per-head KV cache latency at longer context
- Success threshold: At prompt length at least 512 and decode length at least 256, int8 per-head KV has perplexity delta <= 0.5% versus FP and decode throughput >= FP baseline while reducing estimated KV cache footprint by at least 60%.
- Stop condition: Stop if optimized int8 still loses more than 10% decode throughput at long context or if perplexity delta exceeds 0.5% on the same real-text evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-kv-quantization-with-downstream-perplexity-and-de-90af47cdc3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
