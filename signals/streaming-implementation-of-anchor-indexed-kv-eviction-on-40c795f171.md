# Streaming implementation of anchor-indexed KV eviction on exact-match retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `streaming-implementation-of-anchor-indexed-kv-eviction-on-40c795f171`
Run ID: `streaming-implementation-of-anchor-indexed-kv-eviction-on-40c795f171-20260530T041141384492+0000`

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

- Parent run decision: Anchor-Indexed KV Compression with Exact Recall Probes: enoch://control-plane/projects/anchor-indexed-kv-compression-with-exact-recall-probes-e60184c4c634/runs/anchor-indexed-kv-compression-with-exact-recall-probes-e60184c4c634-20260529T174221008055+0000
- Parent run decision: Anchor-indexed KV eviction in a small transformer exact-match retrieval task: enoch://control-plane/projects/anchor-indexed-kv-eviction-in-a-small-transformer-exact-ma-a397e05222/runs/anchor-indexed-kv-eviction-in-a-small-transformer-exact-ma-a397e05222-20260529T211017566277+0000

## What looked useful

Across 5 seeds, 60,000 records, 15,000 queries per seed/budget, and capacities 256-2048, anchor-indexed latest retention beat sliding-window exact-match accuracy at every budget. Medium-locality gains ranged from +1.70 to +18.47 percentage points, while scan-only retention matched accuracy but needed 231-880 mean lookup steps versus 1 for the direct index. No-refresh and hash-bucket ablations exposed stale-value and collision risks.

## Boundaries and scale limits

No trained transformer, real attention logits, tokenizer effects, multi-layer KV coupling, GPU memory bandwidth, or end-to-end generation quality were tested. Absolute accuracy depends on key locality and budget/keyspace ratio; weak locality reduces low-budget gains.

## Claim scope

In a synthetic streaming exact-match retrieval benchmark with key/value anchor records, fixed seeds, bounded KV budgets, and hot/cold query locality, retaining the latest anchor per key with a direct key index improves exact-match accuracy over sliding-window and random eviction while reducing lookup work relative to scan-only retained anchors.

## Why it stopped

No-paper closure: this run provides useful synthetic mechanism evidence, not publication-grade model-level validation.

## Recommended next action

Run a bounded transformer-level follow-up using real KV tensors on an exact-match retrieval task, with full-cache, sliding-window, no-refresh, scan-only, and collision ablations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer-level anchor-indexed KV eviction for exact-match retrieval
- Success threshold: At two or more KV budgets, anchor-indexed latest retention improves exact-match accuracy by at least 5 percentage points over sliding-window with no more than 10% throughput regression versus sliding-window, while no-refresh and collision ablations explain failure modes.
- Stop condition: Stop if real-KV implementation fails to beat sliding-window by 5 percentage points at every tested budget, or if index overhead causes more than 10% throughput regression without a compensating accuracy gain.

## Evidence references

- Artifact root: `<local-path>/projects/streaming-implementation-of-anchor-indexed-kv-eviction-on-40c795f171`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
