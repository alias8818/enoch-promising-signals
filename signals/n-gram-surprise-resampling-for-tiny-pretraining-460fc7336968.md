# N-gram Surprise Resampling for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `n-gram-surprise-resampling-for-tiny-pretraining-460fc7336968`
Run ID: `n-gram-surprise-resampling-for-tiny-pretraining-460fc7336968-20260527T173811627515+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7a7e6dcc5445

## What looked useful

Naive oversampling of high 5-gram-surprise windows was consistently worse than uniform on whole-validation loss (+0.0196 cross entropy mean delta across 3 matched seeds), though it slightly reduced high-surprise validation band loss. The tradeoff suggests pure surprise resampling overweights rare/hard slices at the expense of common validation distribution modeling.

## Boundaries and scale limits

Small character-level dataset, tiny Transformer, 3 seeds, short fixed-token runs, no BPE/subword tokenization, no GPT-2-small-class model, no long-run convergence, no downstream evaluation, and no tuned mixture or curriculum schedule.

## Claim scope

In a Tiny Shakespeare character-level causal Transformer probe with 800 update steps, 6.55M sampled training tokens per run, and 3 matched seeds, pure 5-gram surprise-weighted window sampling did not improve deterministic validation cross entropy over uniform sampling.

## Why it stopped

Bounded direct tiny-LM evidence consistently falsified the simple pure n-gram surprise-resampling hypothesis versus uniform at fixed sequence-item budget; this is an early scoped negative result, not a full-scale validation.

## Recommended next action

Stop this run as a scoped early negative; if continuing, test a predeclared uniform-plus-surprise mixture schedule rather than pure surprise weighting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Uniform-Surprise Mixture Sampling for Tiny Pretraining
- Success threshold: Across at least 3 matched seeds, one predeclared mixture has mean whole-validation cross entropy at least 0.01 lower than uniform and does not worsen high-surprise band loss.
- Stop condition: Stop if all predeclared mixtures are worse than uniform on mean whole-validation cross entropy or if any apparent gain is confined only to high-surprise bands while whole-validation loss regresses.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-surprise-resampling-for-tiny-pretraining-460fc7336968`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
