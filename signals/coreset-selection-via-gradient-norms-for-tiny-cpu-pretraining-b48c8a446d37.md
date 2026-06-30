# Coreset selection via gradient norms for tiny CPU pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `coreset-selection-via-gradient-norms-for-tiny-cpu-pretraining-b48c8a446d37`
Run ID: `coreset-selection-via-gradient-norms-for-tiny-cpu-pretraining-b48c8a446d37-20260528T175214045959+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0c44e0cde6a7

## What looked useful

Naive static high-gradient coreset selection was consistently worse than random by +0.5535 validation cross-entropy on average (+16.3%) and won 0/5 paired repeats; selection diagnostics show reduced target diversity and near-zero gradient-norm/loss correlation at initialization.

## Boundaries and scale limits

Tiny character LM proxy only: average embedding context model, Tiny Shakespeare windows, 4096 candidate windows, 2048 validation windows, 500 SGD steps, no Transformer, no large corpus, no dynamic rescoring, and no datacenter-scale training.

## Claim scope

In a NumPy character-level next-token pretraining proxy with a fixed 15% subset, static top initial per-example gradient-norm selection under equal SGD update budget underperformed random subset selection across five paired repeats.

## Why it stopped

Early CPU proxy falsification, not full validation: the directly tested naive static gradient-norm coreset failed against random under equal budget, while larger Transformer/corpus evidence would be required to reject all gradient-informed coreset variants.

## Recommended next action

Stop scaling naive static top-gradient selection; if continuing locally, test diversity-constrained or stratified gradient-norm selection before any larger model run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Diversity-constrained gradient-norm coreset for tiny language-model pretraining
- Success threshold: Diversity-constrained gradient selection beats random mean validation loss by at least 2% and wins at least 4/5 paired repeats while preserving target entropy within 5% of random.
- Stop condition: Stop if the diversity-constrained method fails to beat random in at least 3/5 paired repeats or still reduces target entropy by more than 10% versus random.

## Evidence references

- Artifact root: `<local-path>/projects/coreset-selection-via-gradient-norms-for-tiny-cpu-pretraining-b48c8a446d37`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
