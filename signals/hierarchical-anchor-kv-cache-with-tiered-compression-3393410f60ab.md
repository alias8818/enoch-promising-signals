# Hierarchical Anchor KV Cache with Tiered Compression

Status: `useful_signal`
Project ID: `hierarchical-anchor-kv-cache-with-tiered-compression-3393410f60ab`
Run ID: `hierarchical-anchor-kv-cache-with-tiered-compression-3393410f60ab-20260515T222944061710+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/908298541335

## What looked useful

On seq_len=8192 with 5 seeds and 5120 total queries, HAKV achieved 0.987 mean cosine on far-anchor recall at 0.059 memory ratio; memory-matched random anchors achieved 0.103. HAKV failed on far non-anchor recall with 0.089 cosine, showing the method depends on correct anchor coverage.

## Boundaries and scale limits

No pretrained language model, perplexity, downstream task accuracy, production decoding throughput, or kernel-level cache-update overhead was tested. The result is a mechanism probe, not full transformer validation.

## Claim scope

Synthetic causal-attention traces with planted periodic far-anchor motifs: exact anchor retention plus tiered quantized centroids preserves full-cache attention outputs for anchored far recalls at roughly 6% KV memory, compared with memory-matched random-anchor and segment-compression baselines.

## Why it stopped

No-paper closure: this is a synthetic attention-fidelity mechanism result with a clear failure mode, not publication-grade evidence for real transformer inference.

## Recommended next action

Run a bounded real-model inference follow-up in a small pretrained transformer, measuring perplexity/retrieval accuracy, KV memory, and decode latency against memory-matched random-anchor and segment-compression controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model HAKV inference fidelity on small pretrained transformers
- Success threshold: At a KV memory ratio of 10% or less, HAKV should improve long-range retrieval accuracy by at least 20 absolute percentage points over both random-anchor and segment-only baselines while keeping perplexity degradation within 10% relative to full KV on the tested small model.
- Stop condition: Stop if HAKV does not beat both memory-matched controls on retrieval accuracy, or if perplexity degradation exceeds 25% relative to full KV at all tested memory budgets.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-anchor-kv-cache-with-tiered-compression-3393410f60ab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
