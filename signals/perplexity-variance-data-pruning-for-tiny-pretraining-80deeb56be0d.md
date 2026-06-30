# Perplexity-Variance Data Pruning for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `perplexity-variance-data-pruning-for-tiny-pretraining-80deeb56be0d`
Run ID: `perplexity-variance-data-pruning-for-tiny-pretraining-80deeb56be0d-20260526T091531005044+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/026a37900b96

## What looked useful

Across seeds 7, 11, 13, 17, and 19, low-variance pruning was the best pruned policy in 5/5 runs. Mean held-out clean perplexity was 52.55 for low-variance pruning versus 72.79 for random pruning and 85.40 for high-variance pruning.

## Boundaries and scale limits

Synthetic generated corpus, small GRU LM, one clean validation distribution, no GPT-2-small-class transformer, no real web/text corpus, no downstream transfer, and all-data training used more tokens than pruned subsets.

## Claim scope

Synthetic tiny-language-model pruning test: a pilot GRU's per-document token-NLL variance was useful for selecting a 50% training subset, and low-variance pruning beat random same-size pruning on held-out clean-domain perplexity across five seeds.

## Why it stopped

Closed as a no-paper useful signal because the evidence is reproducible but proxy-only and synthetic rather than direct real-corpus transformer pretraining evidence.

## Recommended next action

Run one bounded deepen follow-up on a real small text corpus with a parameter-matched transformer and token-budget-matched baselines; do not write a paper from this synthetic tiny-GRU result alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Corpus Transformer Check for Perplexity-Variance Pruning
- Success threshold: Low-variance or combined mean/variance pruning reduces held-out perplexity by at least 5% versus random same-size pruning in at least 3/3 seeds without losing to a simple low-mean baseline.
- Stop condition: Stop if variance-aware pruning fails to beat random same-size pruning by 5% in two seeds or if the effect is fully explained by a simpler boilerplate/noise filter.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-variance-data-pruning-for-tiny-pretraining-80deeb56be0d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
