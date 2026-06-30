# Real-text bounded validation for gradient-free influence data selection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-text-bounded-validation-for-gradient-free-influence-d-3624229522`
Run ID: `real-text-bounded-validation-for-gradient-free-influence-d-3624229522-20260528T221543354724+0000`

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

- Parent run decision: Gradient-Free Influence Data Selection for Tiny Pretraining: enoch://control-plane/projects/gradient-free-influence-data-selection-for-tiny-pretraining-6e123d5276ad/runs/gradient-free-influence-data-selection-for-tiny-pretraining-6e123d5276ad-20260528T180252005053+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/10efd384d24c

## What looked useful

Centroid-margin selection is not a viable standalone selector here: 0 of 3 budgets met the threshold and it underperformed random at 50 and 100 examples/class. Diversified validation coverage gave +8.2 and +3.6 accuracy points over random at 20 and 50 examples/class, but remained 1.4 to 2.5 points below the length control.

## Boundaries and scale limits

Single real-text dataset, six classes, one train/validation split, linear downstream classifier, TF-IDF representation, five random seeds only for the random baseline, no language-model pretraining or multi-dataset robustness.

## Claim scope

On one six-class 20 Newsgroups split with TF-IDF + LinearSVC, naive centroid-margin gradient-free influence selection failed the predeclared top-vs-random threshold, while a gradient-free validation-coverage variant improved over random in scarce-data budgets but not over a length-based control.

## Why it stopped

Tier 1 direct real-text test completed; the predeclared centroid-margin threshold failed, and the coverage signal is useful but not paper-ready because it did not beat the length control.

## Recommended next action

Run a length-controlled multi-dataset deepen test of gradient-free validation coverage before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Length-controlled multi-dataset validation coverage for gradient-free text selection
- Success threshold: Coverage selection beats both class-balanced random and length-matched controls by at least 2 accuracy points on at least two datasets and two scarce-data budgets, with macro-F1 moving in the same direction.
- Stop condition: Stop if coverage fails to beat length-matched controls on at least two datasets or if gains disappear under multiple split seeds.

## Evidence references

- Artifact root: `<local-path>/projects/real-text-bounded-validation-for-gradient-free-influence-d-3624229522`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
