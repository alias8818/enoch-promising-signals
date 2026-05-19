# Optimized long-context real-KV anchor router benchmark

Status: `useful_signal`
Project ID: `optimized-long-context-real-kv-anchor-router-benchmark-e4b7adedbe`
Run ID: `optimized-long-context-real-kv-anchor-router-benchmark-e4b7adedbe-20260515T134507201835+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Optimized long-context real-KV anchor router benchmark: internal_generated:optimized-long-context-real-kv-anchor-router-benchmark-e4b7adedbe

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Bounded real-Q/K/V validation supports the anchor-routing mechanism but falsifies the optimized systems claim for the benchmarked implementation: at 16k tokens, anchor routing selected 12.8-26.0% of keys with 0.968-0.971 output cosine but remained slower than dense attention.

## Recommended next action

Stop this run as a no-paper mixed result; only spend the final follow-up depth slot on a fused or batched real-KV router if it can directly test end-to-end latency speedup rather than another Python-level proxy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused real-KV anchor router latency validation
- Success threshold: Across at least three seeds and three layers at 16k or longer context, fused/batched anchor routing must preserve at least 0.95 output cosine and 0.90 dense attention mass while selecting no more than 15% of keys and achieving at least 1.5x lower per-query or decode-step latency than dense attention.
- Stop condition: Stop negative if fused/batched anchor routing is still slower than dense at 16k, or if achieving speedup requires dropping below 0.95 output cosine or 0.90 dense attention mass.

## Evidence references

- Artifact root: `<local-path>/projects/optimized-long-context-real-kv-anchor-router-benchmark-e4b7adedbe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
