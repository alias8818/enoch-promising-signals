# Low-Rank Shared Optimizer Moments Across Layers

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `low-rank-shared-optimizer-moments-across-layers-5bbe4af8674a`
Run ID: `low-rank-shared-optimizer-moments-across-layers-5bbe4af8674a-20260522T130514496441+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/afd07c8c9072

## What looked useful

Baseline AdamW moments were only moderately low-rank across layers (mean rank-2 energy 0.814, minimum 0.517), while forced rank-2 shared moments worsened mean final validation loss by +0.304 versus AdamW. A rank-2 coordinate permutation control was essentially tied with aligned rank-2 compression, weakening the coordinate-aligned sharing premise. Naive linear compression of second moments also required positivity handling to avoid invalid Adam updates.

## Boundaries and scale limits

Not tested on real language data, GPT-2-small-class scale, long training, distributed optimizer systems, or a true memory-saving factorized implementation. The experiment materialized full moments for projection, so it tests optimization behavior and moment structure, not actual memory savings.

## Claim scope

Bounded local test on a 6-layer tiny transformer trained on a synthetic autoregressive sequence task; rank-1 and rank-2 shared low-rank AdamW moment compression across matched layers after every step, with clamped second moments, was compared to full AdamW across 3 seeds.

## Why it stopped

Moderate local evidence shows the tested low-rank shared optimizer moments materially degrade training and do not beat a permutation control; this is an early bounded falsification, not a full-scale validation.

## Recommended next action

Stop this no-paper line for rank-1/rank-2 reconstruct-and-clamp shared moments; if continuing, test a positivity-preserving factorized second-moment optimizer with rank >=4 and an aligned-vs-shuffled control on a real language dataset.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Positivity-Preserving Shared Second-Moment Factorization
- Success threshold: At equal training tokens, rank-4 or rank-8 positivity-preserving shared moments are within 2% validation loss or perplexity of AdamW, show measured optimizer-state memory reduction, and outperform the shuffled/permuted control.
- Stop condition: Stop if aligned shared factors remain more than 5% worse than AdamW or fail to outperform the shuffled/permuted control at the same memory budget.

## Evidence references

- Artifact root: `<local-path>/projects/low-rank-shared-optimizer-moments-across-layers-5bbe4af8674a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
