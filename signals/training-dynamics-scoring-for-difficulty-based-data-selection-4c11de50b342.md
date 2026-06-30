# Training-Dynamics Scoring for Difficulty-Based Data Selection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `training-dynamics-scoring-for-difficulty-based-data-selection-4c11de50b342`
Run ID: `training-dynamics-scoring-for-difficulty-based-data-selection-4c11de50b342-20260521T212138960486+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a7551cd5ba5c

## What looked useful

TD hardness correlated with latent difficulty (mean r=0.562) and strongly separated flipped-label examples from clean ones. TD-middle selection improved accuracy over random by +3.53, +2.50, and +2.19 percentage points at 10%, 20%, and 40% budgets; TD-hard selection failed because it concentrated label noise.

## Boundaries and scale limits

Synthetic Gaussian data only; small MLPs only; 6 seeds; no real text/vision dataset, no large model pretraining, no datacenter-scale validation, and no claim that the same score is sufficient for broad data curation.

## Claim scope

In a controlled synthetic noisy multiclass classification benchmark with known latent difficulty, early per-example training-dynamics hardness scores identify useful middle-difficulty subsets and label-noise-heavy hard subsets; selecting TD-middle examples improves clean-test accuracy over same-size random selection for 10%, 20%, and 40% budgets across 6 seeds.

## Why it stopped

No-paper closure: the local result is a useful synthetic mechanism signal, not direct publication-grade evidence on real data or large-model data selection.

## Recommended next action

Run a bounded real-data deepen test on a small vision or text classification dataset with saved training-dynamics traces and the same random/easy/mid/hard controls before considering any paper or scale-out claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Data Training-Dynamics Difficulty Selection Check
- Success threshold: TD-middle beats random and the strongest static baseline by at least 1 percentage point mean clean-test accuracy across at least 5 seeds, with no seed-level catastrophic failures and diagnostics showing lower noise/ambiguity than TD-hard.
- Stop condition: Stop if TD scores do not beat random by at least 0.5 percentage points on average or if improvements disappear after controlling for static final loss/confidence.

## Evidence references

- Artifact root: `<local-path>/projects/training-dynamics-scoring-for-difficulty-based-data-selection-4c11de50b342`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
