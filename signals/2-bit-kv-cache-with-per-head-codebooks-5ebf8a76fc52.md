# 2-Bit KV Cache with Per-Head Codebooks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `2-bit-kv-cache-with-per-head-codebooks-5ebf8a76fc52`
Run ID: `2-bit-kv-cache-with-per-head-codebooks-5ebf8a76fc52-20260604T184633036860+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/3c542971de2e

## What looked useful

Per-head k-means was best on heterogeneous synthetic heads (attention-output rel MSE 0.1316 vs 0.2216 global k-means) and on distilgpt2 real caches (0.1940 vs 0.2170 global k-means, winning 5 of 6 layers). Uniform int2 baselines were substantially worse. Homogeneous synthetic heads showed almost no per-head advantage over global k-means.

## Boundaries and scale limits

No packed runtime implementation, no end-to-end perplexity/generation evaluation, no decode throughput measurement, one small model (distilgpt2), short prompts, and query-like probes rather than full autoregressive cache reuse.

## Claim scope

Bounded tensor-level and attention-output evidence shows 2-bit per-head scalar k-means codebooks reduce KV-cache reconstruction and probed attention-output error versus global or uniform 2-bit baselines on synthetic heterogeneous caches and distilgpt2 real KV caches.

## Why it stopped

Closed as no-paper useful signal: local evidence supports the mechanism but remains a tensor/cache-output probe rather than full model-quality or serving validation.

## Recommended next action

Run a bounded deepen experiment that integrates a 2-bit per-head k-means KV cache into small-LM autoregressive decoding and measures perplexity plus decode latency against fp16, per-head uniform, global k-means, and per-head k-means baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM Decode Validation for 2-Bit Per-Head KV Codebooks
- Success threshold: Per-head k-means has lower NLL/perplexity degradation than global k-means and per-head uniform at comparable compression, with decode latency overhead small enough that memory savings remain practically plausible.
- Stop condition: Stop if per-head k-means does not improve full-model NLL/perplexity over global k-means or if dequantization overhead makes decode latency materially worse than fp16 for the tested small model.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-per-head-codebooks-5ebf8a76fc52`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
