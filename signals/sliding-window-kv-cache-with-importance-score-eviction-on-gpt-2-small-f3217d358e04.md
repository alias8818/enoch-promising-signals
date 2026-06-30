# Sliding-Window KV Cache with Importance-Score Eviction on GPT-2-Small

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `sliding-window-kv-cache-with-importance-score-eviction-on-gpt-2-small-f3217d358e04`
Run ID: `sliding-window-kv-cache-with-importance-score-eviction-on-gpt-2-small-f3217d358e04-20260611T171002283023+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6f9a06c67866

## What looked useful

At budget 32/recent 16, importance eviction had +0.0425 mean NLL delta versus full cache and 0.9602 top-1 agreement, while sliding-only had +1.1382 NLL delta and 0.7323 agreement. At budget 16/recent 8, importance eviction had +0.2921 NLL delta and 0.8665 agreement, while sliding-only had +3.0930 and 0.3943.

## Boundaries and scale limits

Not evaluated on standard corpora, 1024-token contexts, optimized serving kernels, stochastic prompt sets, or larger models. Runtime measurements include attention-output overhead and are not production latency evidence.

## Claim scope

In a bounded GPT-2-small incremental inference test on eight handcrafted long-range-recall snippets, retaining a recent window plus older tokens with high accumulated attention mass preserved next-token behavior much better than a pure sliding-window cache at the same retained-cache length.

## Why it stopped

No-paper closure: this run produced direct but narrow GPT-2-small evidence on handcrafted snippets, enough for a useful signal but not enough for a publication-grade or broad serving claim.

## Recommended next action

Run a bounded deepen test on a real corpus such as WikiText-103 or PG19 excerpts with 512-1024 token contexts, budgets 64/128/256, and a latency-aware implementation that separates scoring overhead from serving cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corpus-scale GPT-2-small KV importance eviction benchmark
- Success threshold: Across at least 100 held-out real-corpus sequences, importance eviction should recover at least 50% of sliding-only's NLL gap to full cache at two or more budgets, with top-1 agreement improved by at least 10 percentage points and overhead below 20% versus sliding-only in a non-diagnostic implementation.
- Stop condition: Stop if importance eviction recovers less than 25% of the sliding-only NLL gap at all tested budgets or requires attention-scoring overhead that eliminates any plausible cache-efficiency benefit.

## Evidence references

- Artifact root: `<local-path>/projects/sliding-window-kv-cache-with-importance-score-eviction-on-gpt-2-small-f3217d358e04`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
