# Tiered Exact-Anchor KV Cache with Cross-Layer Compression

Status: `compute_scale_blocked`
Project ID: `tiered-exact-anchor-kv-cache-with-cross-layer-compression-7411950a6bc9`
Run ID: `tiered-exact-anchor-kv-cache-with-cross-layer-compression-7411950a6bc9-20260514T182254433950+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b94336eb2cb6

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Proxy/early falsification rather than full validation: direct small-model KV-cache replay tests showed no cross-layer benefit over same-layer anchor interpolation and unacceptable KL/logit drift at useful compression ratios.

## Recommended next action

Stop this run as a proxy/early falsification: the tested exact-anchor cross-layer schemes are not paper-ready because fidelity only holds below 2x compression and degrades at useful ratios.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive exact anchors with learned cross-layer KV residual prediction
- Success threshold: At least 2.5x effective KV-cache compression with mean KL <= 0.03, top1_match_rate >= 0.95, top5_overlap >= 0.95, and <= 5% decode-throughput overhead versus full KV replay.
- Stop condition: Stop if the learned/adaptive method cannot beat same-layer periodic anchors by at least 25% relative KL reduction at matched compression, or if throughput overhead exceeds 10%.

## Evidence references

- Artifact root: `<local-path>/projects/tiered-exact-anchor-kv-cache-with-cross-layer-compression-7411950a6bc9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
