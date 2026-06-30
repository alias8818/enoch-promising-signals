# Sparse-Local KV Cache with Gumbel-Top-K Refresh

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `sparse-local-kv-cache-with-gumbel-top-k-refresh-b75a1eddef49`
Run ID: `sparse-local-kv-cache-with-gumbel-top-k-refresh-b75a1eddef49-20260629T230542449766+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/73e1919ed312

## What looked useful

Gumbel-top-k refresh is not broadly superior in purely local traffic, but in synthetic persistent and mixed long-range regimes it reduced relative MSE by about 1-4% versus deterministic top-k/random global-slot baselines and by about 56% versus local-only.

## Boundaries and scale limits

No trained transformer, no language-model perplexity or generation metrics, no real KV-cache serving benchmark, no GPU throughput measurement, and no layer-wise or batching effects. The evidence is local CPU simulation only.

## Claim scope

Synthetic streaming causal-attention proxy with sequence length 1024, local window 64, global slots 64, 12 seeds, and three hand-designed regimes. Gumbel-top-k refresh improved attention-output approximation over local-only and gave small gains over random or deterministic top-k in long-range recurrent regimes.

## Why it stopped

Current evidence is a synthetic proxy useful signal, not full validation; direct model-quality and serving-cost evidence is required before a paper claim.

## Recommended next action

Run a bounded direct transformer test with matched KV budgets on a small trained model, measuring perplexity or task accuracy plus cache-update overhead against local-only, random refresh, deterministic top-k, and attention-sink baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-Transformer Gumbel KV Refresh Validation
- Success threshold: At matched KV budget, Gumbel refresh improves perplexity or task accuracy by at least 2% relative to deterministic top-k or random refresh on long-context cases without more than 10% serving-time overhead.
- Stop condition: Stop if Gumbel refresh fails to beat deterministic top-k or random refresh on model-quality metrics across at least two long-context settings, or if refresh overhead erases the memory-budget benefit.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-local-kv-cache-with-gumbel-top-k-refresh-b75a1eddef49`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
