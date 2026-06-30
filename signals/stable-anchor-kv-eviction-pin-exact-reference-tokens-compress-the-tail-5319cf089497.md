# Stable-Anchor KV Eviction: Pin Exact-Reference Tokens, Compress the Tail

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `stable-anchor-kv-eviction-pin-exact-reference-tokens-compress-the-tail-5319cf089497`
Run ID: `stable-anchor-kv-eviction-pin-exact-reference-tokens-compress-the-tail-5319cf089497-20260629T232609164757+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/889938e71ba1

## What looked useful

At 5% cache budget, anchor_pin_compress_tail reached 0.998 long-range exact accuracy and 1.000 aggregate-within-2 accuracy versus sliding at 0.000 and 0.057. At 10%, the combined policy reached 1.000 on both metrics. At 2%, summaries traded off exact retention, lowering exact accuracy from anchor_pin 0.839 to combined 0.679 while restoring aggregate accuracy to 1.000.

## Boundaries and scale limits

No production transformer KV cache was patched; no natural-language anchor detection, perplexity, decoding latency, or downstream QA was measured. Tail compression used exact synthetic topic-count summaries.

## Claim scope

Synthetic 4096-token streaming KV-cache proxy with exact anchor tokens and oracle aggregate tail summaries: anchor pinning preserves long-range exact references better than sliding/random eviction, and tail summaries recover aggregate prefix information when cache budget is at least about 5% in this setup.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy-only, despite supporting the mechanism under the tested cache-policy simulator.

## Recommended next action

Run a bounded real-transformer follow-up that patches a small causal LM KV cache and evaluates matched-memory needle/reference QA, perplexity, decode throughput, and ablations for anchors only, summaries only, and anchors plus summaries.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Transformer KV Cache Test for Stable Anchor Pinning plus Tail Summaries
- Success threshold: At a fixed KV budget of 5% to 10% of full context, anchors plus summaries should improve long-range exact-reference QA by at least 3x over sliding-window eviction while keeping perplexity degradation under 5% and decode throughput loss under 20% versus the matched-budget baseline.
- Stop condition: Stop if a small real-transformer patch cannot beat sliding-window exact-reference QA by at least 2x at matched memory, or if quality/throughput regressions dominate the accuracy gain.

## Evidence references

- Artifact root: `<local-path>/projects/stable-anchor-kv-eviction-pin-exact-reference-tokens-compress-the-tail-5319cf089497`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
