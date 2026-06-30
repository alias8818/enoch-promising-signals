# Outlier-routed residual KV cache for long context on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `outlier-routed-residual-kv-cache-for-long-context-on-cpu-4ff16a5c2315`
Run ID: `outlier-routed-residual-kv-cache-for-long-context-on-cpu-4ff16a5c2315-20260629T082421956541+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.7-code: enoch://research-facility/provider/moonshotai/kimi-k2.7-code/2449eeb394cd

## What looked useful

At 1% routed entries, int4 outlier routing reduced mean relative L2 attention-output error by 72.58% versus int4 and improved top1 attention match from 0.7882 to 0.9271 while using an estimated 29.56% of dense fp16 KV memory. Int8 remained much more accurate at 51.56% of dense fp16 memory.

## Boundaries and scale limits

No real transformer KV traces, no multi-layer accumulation, no perplexity or generation-quality measurement, no tokenizer/corpus variation, and no production decode-loop cache kernel benchmark. This is not direct LLM-serving evidence.

## Claim scope

Synthetic attention-level CPU proxy with long K/V contexts up to 32768 tokens, dimension 64, 32 queries, three seeds, and injected sparse outliers. Magnitude-based outlier routing on top of int4 KV quantization improved attention-output fidelity versus plain int4 at modest extra memory.

## Why it stopped

No-paper closure: the mechanism is supported only by a synthetic attention-level proxy, not by direct end-to-end model evidence.

## Recommended next action

Run a bounded direct-evidence follow-up on real KV traces from a small open transformer, measuring perplexity or next-token KL plus decode latency against fp16, int8, int4, and int4 outlier-routed caches.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-transformer KV trace validation for outlier-routed int4 cache
- Success threshold: At 1-2% routed entries, recover at least 50% of the int4-to-fp16 quality gap while using less than 70% of int8 KV memory and adding less than 25% CPU decode-step latency over int4.
- Stop condition: Stop if routed int4 fails to recover at least 25% of the int4-to-fp16 quality gap on two representative long-context samples or if latency overhead exceeds 50% before quality approaches int8.

## Evidence references

- Artifact root: `<local-path>/projects/outlier-routed-residual-kv-cache-for-long-context-on-cpu-4ff16a5c2315`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
