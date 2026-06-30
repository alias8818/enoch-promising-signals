# Contrastive Data Pairing for Noise Robustness

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `contrastive-data-pairing-for-noise-robustness-3a01fe37a709`
Run ID: `contrastive-data-pairing-for-noise-robustness-3a01fe37a709-20260608T120927110936+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ddd8ca4fc941

## What looked useful

Augmentation produced the dominant robustness gain. Adding paired contrastive loss improved severe-corruption accuracy by about 0.8 percentage points over augmented CE at 0% label noise and about 0.7 percentage points at 20% label noise, but label-noise effects were not statistically clear and embedding cosine diagnostics moved opposite the simple stability mechanism.

## Boundaries and scale limits

Five seeds on 1,797 8x8 digit images; synthetic Gaussian, dropout, salt/pepper, combined input corruptions; 0% and 20% synthetic label noise; no natural-image dataset, convolutional encoder, large model, or real noise distribution.

## Claim scope

On sklearn digits with a small MLP, paired corrupted-view contrastive training gives a small severe-corruption accuracy gain over an equally augmented cross-entropy baseline, but not a broad or paper-ready robustness result.

## Why it stopped

The run produced direct small-scale evidence, but the effect over a fair augmented baseline is below 1 percentage point and mechanistically mixed, so it is not publication-grade validation.

## Recommended next action

Stop this run as no-paper useful evidence; a bounded follow-up should test whether the small paired-contrastive gain persists on a natural-image dataset with a convolutional encoder and stronger mechanism diagnostics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-image confirmation of paired contrastive robustness
- Success threshold: Paired contrastive beats augmented CE by at least 2 percentage points on severe corruptions at matched clean accuracy within 1 point, with consistent positive deltas across seeds and mechanism diagnostics that do not contradict the stated invariance mechanism.
- Stop condition: Stop as negative if the severe-corruption gain over augmented CE is below 1 percentage point or if clean accuracy drops by more than 2 points.

## Evidence references

- Artifact root: `<local-path>/projects/contrastive-data-pairing-for-noise-robustness-3a01fe37a709`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
