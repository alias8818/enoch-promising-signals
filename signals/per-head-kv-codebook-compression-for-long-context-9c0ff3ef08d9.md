# Per-Head KV Codebook Compression for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-head-kv-codebook-compression-for-long-context-9c0ff3ef08d9`
Run ID: `per-head-kv-codebook-compression-for-long-context-9c0ff3ef08d9-20260607T204343763827+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b929845421d7

## What looked useful

Per-head KV codebooks are a worthwhile baseline for long-context cache compression, but the naive shared-K baseline is too weak; an equal-total-center global codebook removes much of the advantage. Real-trace mid-rate results show a small per-head advantage with slightly better compression ratio, while other settings are tied or favor global equal-center codebooks.

## Boundaries and scale limits

No full autoregressive compressed-cache decoding, no perplexity/task evaluation, no multi-layer quality metric, no optimized serving kernel, one small real model trace limited to 1024 tokens, and synthetic data is only a mechanism proxy.

## Claim scope

Bounded post-training KV-cache vector quantization probe on a synthetic head-diverse trace and one distilgpt2 layer-3 cache trace. Per-head codebooks strongly beat a same-K shared codebook and are marginally better than an equal-total-center shared codebook at mid compression on the real trace, but not consistently across synthetic data or all center counts.

## Why it stopped

No-paper useful signal: the local proxy and one real trace are mixed, so this is not publication-grade validation of per-head KV codebook compression for long context.

## Recommended next action

Run a bounded deepen experiment with compressed KV cache in the autoregressive loop on a GPT-2-small-class model, reporting next-token KL or perplexity deltas across all layers and comparing per-head against equal-total-center global codebooks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Autoregressive quality test for per-head KV codebook cache compression
- Success threshold: At least 20% lower next-token KL or perplexity degradation than equal-total-center global codebooks at one mid-rate compression point, without a worse compression ratio, across a minimum of three prompt batches.
- Stop condition: Stop if per-head fails to beat equal-total-center global codebooks on mean next-token KL/perplexity degradation or if compressed-cache decoding cannot be implemented locally within a bounded small-model run.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-kv-codebook-compression-for-long-context-9c0ff3ef08d9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
