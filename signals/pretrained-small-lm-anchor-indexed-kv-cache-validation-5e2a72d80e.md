# Pretrained Small-LM Anchor-Indexed KV Cache Validation

Status: `useful_signal`
Project ID: `pretrained-small-lm-anchor-indexed-kv-cache-validation-5e2a72d80e`
Run ID: `pretrained-small-lm-anchor-indexed-kv-cache-validation-5e2a72d80e-20260518T062412892619+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Pretrained Small-LM Anchor-Indexed KV Cache Validation: internal_generated:pretrained-small-lm-anchor-indexed-kv-cache-validation-5e2a72d80e

## What looked useful

Exact anchor-to-prefix KV cache reuse is a valid loss-preserving mechanism for a pretrained small LM, while wrong-anchor and truncated-cache controls degrade NLL substantially; the result is useful engineering evidence but not a novel paper-ready claim.

## Boundaries and scale limits

This run did not test approximate anchors, end-to-end serving lookup/eviction overhead, cache build amortization over multi-hit workloads, batched decoding, memory pressure, other model families, larger GPT-2-small-class or 7B models, or production inference engines.

## Claim scope

On distilgpt2 FP32 continuation scoring over 96 Wikitext-derived examples with fixed seeds, exact anchor-indexed prefix KV cache hits preserve NLL relative to full-context recomputation within p95 absolute NLL delta 1.23e-5 and reduce synchronized local cache-hit continuation time by 1.53x in aggregate.

## Why it stopped

Tier 2 direct metrics support exact-anchor KV reuse, but exact prefix caching alone is not paper-positive novelty and the run omits realistic serving/index overheads.

## Recommended next action

Stop this run as no-paper useful signal; if deepening, run an end-to-end multi-hit serving-style benchmark that includes anchor lookup, cache construction amortization, cache memory footprint, and hit-rate sensitivity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-End Anchor KV Cache Hit-Rate and Amortization Benchmark
- Success threshold: Across at least three fixed seeds, exact anchors have p95 absolute NLL delta <= 1e-4, wrong/truncated controls are measurably worse by >= 0.1 mean NLL, and end-to-end throughput including cache build amortization and lookup overhead improves by >= 1.5x at realistic cache hit rates.
- Stop condition: Stop as negative if exact-anchor NLL is not equivalent, if controls do not separate from exact anchors, or if end-to-end speedup including overhead is below 1.2x.

## Evidence references

- Artifact root: `<local-path>/projects/pretrained-small-lm-anchor-indexed-kv-cache-validation-5e2a72d80e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
