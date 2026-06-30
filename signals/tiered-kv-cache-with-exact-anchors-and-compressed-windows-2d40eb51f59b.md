# Tiered KV Cache with Exact Anchors and Compressed Windows

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiered-kv-cache-with-exact-anchors-and-compressed-windows-2d40eb51f59b`
Run ID: `tiered-kv-cache-with-exact-anchors-and-compressed-windows-2d40eb51f59b-20260602T224741471386+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/93566c73e35a

## What looked useful

The tiered cache consistently beat recent-only at the same retained-token budget across random, anchor-retrieval, local-recent, and diffuse-old synthetic patterns. Base tiered relative L2 errors were 0.228 on anchor retrieval and 0.216 on local-recent versus 1.492 and 1.350 for recent-only, at 0.164 retained-token ratio. However, random and diffuse-old errors remained high and the naive implementation was about 50x slower than full attention.

## Boundaries and scale limits

No end-to-end transformer perplexity, retrieval benchmark, multi-layer error accumulation, incremental cache update, fused kernel, or production serving latency was tested. Timing applies only to a naive rebuild-per-query PyTorch prototype and is not representative of an optimized serving implementation.

## Claim scope

Synthetic single-head causal attention probe at sequence length 4096 shows that exact recent tokens plus periodic anchors and cardinality-weighted compressed old windows can reduce retained KV tokens to about 16.4% while producing substantially lower attention-output error than a same-budget recent-only cache.

## Why it stopped

No-paper closure: this is a bounded synthetic attention useful signal, not direct publication-grade model or serving evidence; the naive rebuild-per-query implementation is also timing-negative.

## Recommended next action

Run a bounded transformer decode follow-up with incremental summaries on a small pretrained model, measuring perplexity/retrieval quality and decode latency against full KV and recent-only baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Incremental Tiered KV Cache in Small Transformer Decode
- Success threshold: At retained-token ratio <= 0.35, tiered KV has at least 30% lower quality degradation than same-budget recent-only and decode throughput no worse than 20% below full KV in an incremental implementation.
- Stop condition: Stop if tiered KV fails to improve quality degradation over recent-only by at least 10% at any tested memory ratio, or if incremental maintenance remains more than 2x slower than full KV after straightforward vectorization.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-kv-cache-with-exact-anchors-and-compressed-windows-2d40eb51f59b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
