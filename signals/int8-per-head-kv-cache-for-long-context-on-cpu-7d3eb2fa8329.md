# INT8 Per-Head KV Cache for Long Context on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `int8-per-head-kv-cache-for-long-context-on-cpu-7d3eb2fa8329`
Run ID: `int8-per-head-kv-cache-for-long-context-on-cpu-7d3eb2fa8329-20260602T130350590915+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/565b2420e74b

## What looked useful

INT8 per-head KV cache produced a 1.035x to 3.404x decode speedup, 1.932x median speedup, and roughly 1.1% relative L2 output error while cutting KV memory to one quarter of FP32 in a bounded CPU long-context attention proxy.

## Boundaries and scale limits

Synthetic Q/K/V only; no real LLM, tokenizer, perplexity, retrieval/task metric, prefill/update path, BF16 baseline, batching study, NUMA tuning, or production fused attention kernel was tested.

## Claim scope

On this CPU-only synthetic decode benchmark, symmetric per-head INT8 K/V cache for 8-head attention at sequence lengths 4096 to 32768 and head dimensions 64 to 128 reduced KV cache footprint to 25% of FP32 and improved decode latency in every tested configuration.

## Why it stopped

Bounded synthetic benchmark supports the mechanism but is proxy-only and not sufficient for a real long-context CPU inference claim.

## Recommended next action

Stop this worker run as no-paper useful signal; next run should integrate per-head INT8 KV into a small real CPU LLM inference path and measure end-to-end latency, RSS, and quality against FP32/BF16 KV baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU LLM validation of per-head INT8 KV cache
- Success threshold: At least 20% end-to-end decode throughput improvement and at least 3x KV memory reduction with no more than 1% relative perplexity degradation or a predeclared equivalent task-quality loss.
- Stop condition: Stop if real-model quality degradation exceeds the threshold, if end-to-end decode is not faster than baseline at 16k or 32k context, or if integration overhead eliminates the memory-footprint advantage.

## Evidence references

- Artifact root: `<local-path>/projects/int8-per-head-kv-cache-for-long-context-on-cpu-7d3eb2fa8329`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
