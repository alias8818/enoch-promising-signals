# Exact-Anchor KV Saliency Gating with Clustered Non-Anchor Compression

Status: `useful_signal`
Project ID: `exact-anchor-kv-saliency-gating-with-clustered-non-anchor-compression-d2462d72c7d3`
Run ID: `exact-anchor-kv-saliency-gating-with-clustered-non-anchor-compression-d2462d72c7d3-20260519T071844997165+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0df6739cebff

## What looked useful

The mechanism is promising in diffuse-attention cases and sensitive to anchor allocation. A 50% anchor allocation beat top-prune on mean reconstruction error and narrow paired win rate, while 25% anchors was mixed or worse at lower budgets. This justifies a bounded direct decoding follow-up but not a paper.

## Boundaries and scale limits

No end-to-end generation, perplexity, task accuracy, decode-latency, memory-bandwidth, long-context, larger-model, production-kernel, or non-oracle saliency-predictor validation. Saliency anchors were selected from exact full attention for the current query, so the result is an upper-bound mechanism proxy.

## Claim scope

Frozen GPT-2-small mechanism test of single-query attention-context reconstruction on 16 natural-language synthetic contexts up to 128 tokens, across 12 layers, 4 heads per layer, positions 32/64/96, and cache budgets of 12.5%, 25%, and 50%. With 50% of the compressed budget allocated to exact saliency anchors, clustered non-anchor compression reduced mean relative L2 versus exact top-saliency pruning by 26.8% to 57.6%, and strongly beat random-anchor clustering.

## Why it stopped

No-paper useful signal: corrected GPT-2-small proxy evidence supports the mechanism in a scoped setting, but it is not direct end-to-end evidence and uses oracle per-query saliency.

## Recommended next action

Run a bounded GPT-2-small compressed-cache generation/perplexity benchmark with dense cache and exact top-prune controls; stop if the attention reconstruction gain does not survive iterative decoding under matched cache budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end GPT-2 compressed-cache decoding validation for exact-anchor clustered KV compression
- Success threshold: At matched cache budget on GPT-2-small or distilgpt2, exact-anchor clustered compression reduces next-token KL or perplexity degradation versus top-prune by at least 20% while adding no more than 25% decode latency overhead relative to the compressed top-prune baseline.
- Stop condition: Stop if compressed-cache decoding shows no improvement over top-prune in next-token KL/perplexity at two or more tested budgets, or if clustering overhead dominates latency beyond the 25% threshold.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-saliency-gating-with-clustered-non-anchor-compression-d2462d72c7d3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
