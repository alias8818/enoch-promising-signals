# Exact-Anchor KV Compression for Long-Context CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-kv-compression-for-long-context-cpu-inference-7f4e18bd801e`
Run ID: `exact-anchor-kv-compression-for-long-context-cpu-inference-7f4e18bd801e-20260605T063244256207+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/57315345ba57

## What looked useful

Exact anchors preserved planted anchor retrieval with 0.0058-0.0130 mean relative L2 output error while reducing KV memory to 2.37%-14.08% of full cache and speeding weighted single-query attention by 11.46x-20.96x. Fixed anchors failed planted off-anchor retrieval with about 0.997 mean relative L2 error, so the broad compression claim is not supported without adaptive/salience-aware anchor selection.

## Boundaries and scale limits

No real LLM integration, no tokenizer or real long-context dataset, no multi-layer cache, no autoregressive serving loop, no perplexity or task-quality evaluation, and no production CPU inference runtime.

## Claim scope

Synthetic single-query CPU attention mechanism probe for fixed-stride exact-anchor KV compression with weighted mean-pooled non-anchor blocks, D=64, sequence lengths 4096-65536, and planted anchor, planted non-anchor, and diffuse random cases.

## Why it stopped

Bounded synthetic CPU mechanism test produced a mixed result: anchored needles are preserved, but fixed exact anchors plus pooled non-anchors fail off-anchor needles, so the broad idea is not paper-ready.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded follow-up on adaptive or salience-promoted anchors only if the controller wants to test recovery of off-anchor retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Anchor Promotion for Off-Anchor KV Retrieval
- Success threshold: At 65536 tokens, nonanchor_needle mean relative L2 error below 0.10 while KV memory ratio remains below 0.06 and weighted decode remains at least 8x faster than full single-query attention.
- Stop condition: Stop if nonanchor_needle relative L2 error remains above 0.50 at 65536 tokens or if the adaptive policy needs more than 0.10 KV memory ratio to recover the target.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-for-long-context-cpu-inference-7f4e18bd801e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
