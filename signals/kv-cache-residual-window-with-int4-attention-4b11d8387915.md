# KV-Cache Residual Window with INT4 Attention

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-residual-window-with-int4-attention-4b11d8387915`
Run ID: `kv-cache-residual-window-with-int4-attention-4b11d8387915-20260604T225621477011+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/56ed13c59bd9

## What looked useful

A small FP16 residual window can preserve attention outputs when the salient attention mass is in the recent tail: at S=8192,W=128, recent-needle relative L2 fell from 0.1211 with whole-cache INT4 to 0.00733 while cache memory remained 29.25% of FP16. The same window did not protect old salient tokens: old-needle relative L2 stayed about 0.1038. The unfused implementation was slower than FP16, about 4x to 5x at S=8192.

## Boundaries and scale limits

No real language model perplexity or generation-quality evaluation; no fused INT4 attention kernel; timing reflects dequantize-then-attend PyTorch code, not production serving throughput; tested sequence length capped at 8192 and synthetic query/K/V distributions.

## Claim scope

Synthetic single-step GPU decode attention with 8 heads, head dimension 64, sequence lengths up to 8192, comparing full FP16 KV-cache attention to older-token INT4 KV-cache plus a recent FP16 residual window.

## Why it stopped

Proxy/local evidence is useful but not paper-ready: it supports the recent-token residual mechanism, exposes an old-token failure mode, and shows the current unfused path is slower than FP16.

## Recommended next action

Run a bounded real-model decode/perplexity follow-up with GPT-2-small-class weights, whole-cache INT4 and residual-window INT4 baselines, and retrieval-style old-token probes before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model residual-window INT4 KV-cache decode evaluation
- Success threshold: At a cache memory ratio below 0.40 of FP16 for contexts of at least 4096 tokens, residual-window INT4 keeps perplexity within 2% of FP16 and improves old-cache INT4 output error by at least 5x on recent-token probes, while documenting retrieval-task regressions if old-token salience is not retained.
- Stop condition: Stop if residual-window INT4 exceeds 2% perplexity degradation versus FP16 at all memory ratios below 0.50, or if recent-token probes do not improve output error by at least 3x over whole-cache INT4.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-residual-window-with-int4-attention-4b11d8387915`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
