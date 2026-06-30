# Online predictor for attention-aware KV anchors on GPT-2 traces

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `48`
Project ID: `online-predictor-for-attention-aware-kv-anchors-on-gpt-2-t-a38d38fef3`
Run ID: `online-predictor-for-attention-aware-kv-anchors-on-gpt-2-t-a38d38fef3-20260520T045346624375+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `48`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Direct KV-retention quality test for attention-aware anchors on small GPT traces: enoch://control-plane/projects/direct-kv-retention-quality-test-for-attention-aware-ancho-6d517c0256/runs/direct-kv-retention-quality-test-for-attention-aware-ancho-6d517c0256-20260520T044306708618+0000
- Parent run decision: Attention-aware exact anchor partitioning on real small-model KV traces: enoch://control-plane/projects/attention-aware-exact-anchor-partitioning-on-real-small-mo-7f8e4eda74/runs/attention-aware-exact-anchor-partitioning-on-real-small-mo-7f8e4eda74-20260520T043736710025+0000

## What looked useful

The learned predictor beats random, recency, cumulative-attention, and usually recent-window baselines, but consistently trails the trivial last-query-attention baseline by 0.85 to 1.36 percentage points in mean future attention-mass recall across the large validation settings. The no-recent ablation drops sharply, suggesting the learned predictor mostly reuses short-term attention dynamics rather than discovering a stronger anchor rule.

## Boundaries and scale limits

Evidence is trace-level rather than actual KV-cache eviction; it uses GPT-2-small, Wikitext-2, one fixed seed, sequence length 256, averaged layers/heads, and a linear SGD predictor. It does not cover larger models, longer contexts, serving latency, perplexity impact, or non-linear predictors.

## Claim scope

On GPT-2-small attention traces from Wikitext-2 blocks of length 256, a lightweight linear online predictor using age, cumulative attention, recent attention, last-query attention, token id, and position features does not outperform the simple last-query-attention anchor baseline for future attention-mass recall at 10% or 25% anchor budgets over 16-token and 64-token horizons.

## Why it stopped

Bounded direct GPT-2 trace validation repeatedly failed the practical threshold of beating the strongest simple baseline, so this is a no-paper useful negative rather than a full positive validation.

## Recommended next action

Stop pursuing this linear online predictor as a paper result; run a bounded adjacent KV-eviction/perplexity experiment for the stronger observed last-query-attention anchor heuristic.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Last-query attention anchors for real GPT-2 KV-cache eviction
- Success threshold: Last-query attention eviction beats recency and cumulative-attention eviction by at least 2% relative perplexity or at least 2 percentage points future attention-mass recall at the same KV budget, without more than 5% runtime overhead versus the compared heuristic.
- Stop condition: Stop if last-query attention does not beat recency/cumulative-attention on either perplexity delta or attention-mass recall in the first bounded GPT-2 validation, or if implementation overhead dominates the cache-saving benefit.

## Evidence references

- Artifact root: `<local-path>/projects/online-predictor-for-attention-aware-kv-anchors-on-gpt-2-t-a38d38fef3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
