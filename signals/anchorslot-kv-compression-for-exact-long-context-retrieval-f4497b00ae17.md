# AnchorSlot KV Compression for Exact Long-Context Retrieval

Status: `useful_signal`
Project ID: `anchorslot-kv-compression-for-exact-long-context-retrieval-f4497b00ae17`
Run ID: `anchorslot-kv-compression-for-exact-long-context-retrieval-f4497b00ae17-20260518T034023814428+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/27b55e4499f7

## What looked useful

AnchorSlot exact accuracy tracked target kept rate almost exactly: 0.8665 accuracy and 0.8662 kept rate in the main sweep at 38.58x mean compression, but only 0.2689 accuracy and 0.2689 kept rate when the anchor detector was noisy. Pooling alone and stride retention were poor exact-retrieval baselines.

## Boundaries and scale limits

Proxy-only synthetic evaluation; no trained transformer, real long-context benchmark, learned anchor detector, multi-layer KV cache, or production inference implementation was evaluated.

## Claim scope

Synthetic one-layer attention retrieval over generated KV memories up to 16,384 tokens shows that segment summaries plus exact AnchorSlot entries can preserve exact needle retrieval only when the anchor selector keeps the queried token.

## Why it stopped

No-paper closure because the result is synthetic/proxy evidence that isolates a mechanism and failure mode, not direct validation of exact long-context retrieval in a trained model.

## Recommended next action

Stop this run as a proxy useful signal; next run should implement AnchorSlot in a small transformer inference stack and test real NIAH/RULER-style retrieval against full KV and token-budget-matched baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct AnchorSlot KV Cache Test in a Small Transformer
- Success threshold: At 8x or greater KV compression, AnchorSlot achieves at least 95 percent of full-KV exact retrieval accuracy and improves by at least 20 absolute percentage points over the best non-full baseline on two context lengths.
- Stop condition: Stop if anchor recall below 0.9 causes retrieval accuracy to track kept-token rate without beating the best token-budget-matched baseline by at least 10 absolute percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/anchorslot-kv-compression-for-exact-long-context-retrieval-f4497b00ae17`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
