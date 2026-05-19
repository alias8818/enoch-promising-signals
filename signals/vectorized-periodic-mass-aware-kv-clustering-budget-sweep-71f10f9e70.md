# Vectorized periodic mass-aware KV clustering budget sweep on GPT-2-small

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `vectorized-periodic-mass-aware-kv-clustering-budget-sweep-71f10f9e70`
Run ID: `vectorized-periodic-mass-aware-kv-clustering-budget-sweep-71f10f9e70-20260519T082453787075+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Vectorized periodic mass-aware KV clustering budget sweep on GPT-2-small: internal_generated:vectorized-periodic-mass-aware-kv-clustering-budget-sweep-71f10f9e70

## What looked useful

Mass-aware KV pooling reduced the loss gap versus full cache by 63.2%, 73.8%, and 83.4% relative to recent truncation at budgets 32, 64, and 128 respectively; at budget 256 it reached mean NLL 3.692842 versus full-cache 3.646901.

## Boundaries and scale limits

Single model, single dataset, 512-token windows, one fixed seed, fp16 cache, eager attention with output_attentions enabled, and ordered contiguous pooled clusters rather than full arbitrary K-means; no optimized serving kernel, no larger model, no 1024-token context, and no multi-dataset robustness validation.

## Claim scope

On GPT-2-small evaluated autoregressively on 64 Wikitext-2 test windows of 512 tokens, periodic attention-mass-weighted ordered KV pooling preserves next-token loss substantially better than same-budget recent-token truncation and uniform old-token pooling at budgets 32, 64, and 128, and is near full-cache loss at budget 256.

## Why it stopped

No-paper useful signal: direct GPT-2-small metrics support the mass-aware mechanism, but robustness and optimized-serving evidence are insufficient for publication readiness.

## Recommended next action

Run a bounded deepen follow-up on 1024-token contexts across at least two datasets with a numerically stable vectorized compression implementation and a no-attention-collection serving proxy before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robust 1024-token mass-aware KV pooling validation with optimized compression
- Success threshold: Mass-aware pooling reduces the recent-truncation loss gap by at least 50% at budgets 128 and 256 on both datasets, has no non-finite runs, and adds less than 20% compression overhead in the serving proxy.
- Stop condition: Stop if mass-aware pooling fails to beat uniform pooling on either dataset at budget 128, produces any unexplained non-finite sequence after mixed-precision fixes, or requires attention collection overhead that dominates any practical cache-memory benefit.

## Evidence references

- Artifact root: `<local-path>/projects/vectorized-periodic-mass-aware-kv-clustering-budget-sweep-71f10f9e70`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
