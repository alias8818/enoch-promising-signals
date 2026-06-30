# Constant-Memory KV Cache with LSH for Long Context on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `constant-memory-kv-cache-with-lsh-for-long-context-on-cpu-265d1ee1f149`
Run ID: `constant-memory-kv-cache-with-lsh-for-long-context-on-cpu-265d1ee1f149-20260525T125641045478+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ee1b9b06ebf8

## What looked useful

Fixed LSH with 4,096 logical slots used about 43.5 candidates and 1.36 ms/query at 32k tokens in the medium run, versus exact full attention at 32,768 candidates and 322.10 ms/query. However, LSH top-1 recall at 32k was only 0.198 in the medium run, and same-capacity reservoir/window baselines often had higher output cosine while scanning many more candidates.

## Boundaries and scale limits

No real transformer, tokenizer, multi-head/multi-layer decode loop, optimized implementation, perplexity, or downstream long-context task accuracy was tested. Process RSS includes full exact-reference keys/values retained for evaluation and is not the logical cache footprint.

## Claim scope

On a dependency-free synthetic clustered-vector CPU benchmark up to 32,768 tokens, fixed-memory random-hyperplane LSH KV caching kept logical cache capacity and candidate count bounded while reducing per-query latency versus exact full attention, but quality/recall was mixed.

## Why it stopped

Synthetic proxy evidence supports candidate-pruning efficiency but not a full validation of constant-memory LSH KV cache quality for real long-context LLM inference.

## Recommended next action

Stop this run as no-paper useful signal; next concrete action is a bounded small-transformer integration measuring perplexity/retrieval accuracy and decode latency against exact, window, reservoir, and LSH caches.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer evaluation of fixed-memory LSH KV cache
- Success threshold: At an equal fixed KV capacity, LSH must improve decode latency by at least 3x over exact attention and match or beat both window and reservoir baselines on the chosen quality metric within a predeclared tolerance.
- Stop condition: Stop if LSH quality falls below both same-capacity baselines or cannot achieve at least a 3x latency gain at matched quality on the bounded small-transformer task.

## Evidence references

- Artifact root: `<local-path>/projects/constant-memory-kv-cache-with-lsh-for-long-context-on-cpu-265d1ee1f149`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
