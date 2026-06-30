# Transformer-level anchor-indexed KV eviction for exact-match retrieval

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `33`
Project ID: `transformer-level-anchor-indexed-kv-eviction-for-exact-mat-22a09a09c6`
Run ID: `transformer-level-anchor-indexed-kv-eviction-for-exact-mat-22a09a09c6-20260530T080943579035+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `33`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Streaming implementation of anchor-indexed KV eviction on exact-match retrieval: enoch://control-plane/projects/streaming-implementation-of-anchor-indexed-kv-eviction-on-40c795f171/runs/streaming-implementation-of-anchor-indexed-kv-eviction-on-40c795f171-20260530T041141384492+0000
- Parent run decision: Anchor-indexed KV eviction in a small transformer exact-match retrieval task: enoch://control-plane/projects/anchor-indexed-kv-eviction-in-a-small-transformer-exact-ma-a397e05222/runs/anchor-indexed-kv-eviction-in-a-small-transformer-exact-ma-a397e05222-20260529T211017566277+0000

## What looked useful

Anchor-indexed KV retention was near chance at tight budgets and averaged 18.98% at budget 72, versus 18.77% for recency, 22.55% for random retention, and 22.90% for full cache. The random control is the critical negative result: anchor-indexing did not preserve the model's retrieval information as well as nonsemantic random retention.

## Boundaries and scale limits

Small from-scratch transformer, synthetic key-value prompts, modest full-cache accuracy around 23%, two fixed seeds, and mask-based KV-retention emulation rather than a production incremental cache implementation. No 7B-class pretrained model or serving-system validation was run.

## Claim scope

In a bounded synthetic exact-match retrieval test with a small 4-layer transformer, 32 key-value pairs, early queries, fixed seeds, and attention masks emulating retained KV budgets, anchor-indexed retention did not outperform a random-retention control and only marginally matched recency at the largest budget.

## Why it stopped

Bounded direct validation found that anchor-indexed KV eviction failed the practical success threshold of beating both recency and random retention at matched cache budgets; this is not a full large-model validation, but it is a reproducible local falsification of the tested mechanism.

## Recommended next action

Stop this branch as a no-paper useful negative signal; only revisit if a high-accuracy full-cache retriever and real incremental KV-cache implementation are available for the same recency/random/control comparison.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/transformer-level-anchor-indexed-kv-eviction-for-exact-mat-22a09a09c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
