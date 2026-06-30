# Quantized Evidence Ledger with Exact Anchor Embeddings

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-evidence-ledger-with-exact-anchor-embeddings-98e3a7bc2045`
Run ID: `quantized-evidence-ledger-with-exact-anchor-embeddings-98e3a7bc2045-20260602T143154437256+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6178637ba9c2

## What looked useful

The simple exact-anchor residual ledger gave only a small inconsistent int8 recall@1 gain at 256 anchors and failed under 4-bit quantization pressure, where direct quantization retained higher recall@1 and recall@10 with better compression.

## Boundaries and scale limits

Synthetic embeddings only; no real model embeddings, production retrieval traces, product quantization baseline, learned anchor selection, asymmetric distance computation, latency engineering, or large-scale corpus validation.

## Claim scope

On synthetic clustered unit embeddings with 20,000 corpus vectors, 256 queries, 384 dimensions, and 3 seeds, exact-anchor residual scalar quantization was not robustly better than direct per-vector symmetric quantization at comparable byte budgets.

## Why it stopped

Proxy/medium synthetic evidence does not support the tested mechanism as paper-ready or practically superior; this is an early falsification, not a full validation of all anchor-aware quantization methods.

## Recommended next action

Stop this simple exact-anchor residual scalar-quantization design as an early synthetic falsification; a bounded follow-up should test anchor-aware residual product quantization on real embedding data against PQ/OPQ baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchor-aware residual product quantization on real retrieval embeddings
- Success threshold: Anchor-aware residual PQ improves recall@10 by at least 2 percentage points over the best byte-matched non-anchor baseline without worse query latency by more than 10%.
- Stop condition: Stop if anchor-aware residual PQ fails to beat the best byte-matched PQ/OPQ baseline on recall@10 in two independent real-embedding datasets.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-evidence-ledger-with-exact-anchor-embeddings-98e3a7bc2045`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
