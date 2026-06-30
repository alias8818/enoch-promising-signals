# Binarized Gradient Distribution Audit

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `binarized-gradient-distribution-audit-fe24169c64ce`
Run ID: `binarized-gradient-distribution-audit-fe24169c64ce-20260621T020406097483+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/656162164e51

## What looked useful

Gradient sign binarization produced dense-vs-sign cosine as low as 0.427, absolute-gradient p99/median up to 48.26, and raw sign-update L2 scale up to 1929.9x dense gradient scale. Despite that distortion, sign-scaled and raw-sign updates were within about 0.5 percentage points of dense SGD mean test accuracy across four bounded tasks.

## Boundaries and scale limits

Tested only synthetic/small controlled binary classification tasks with one-hidden-layer MLPs, 3 seeds, 2048 training examples, 1024 test examples, 40 epochs, and CPU-only NumPy. Did not test transformers, public benchmark datasets, Adam/AdamW, momentum, gradient clipping, distributed training, communication compression, or hardware throughput.

## Claim scope

In small NumPy MLP classifiers, sign-binarized gradients substantially distort gradient magnitude distribution and dense-update direction, but can match dense SGD test accuracy when update scale is controlled.

## Why it stopped

No-paper useful signal: bounded local evidence quantifies real distributional distortion but does not validate a broad binarized-gradient training claim or falsify small-task viability.

## Recommended next action

Run a bounded deepen follow-up on a standard public dataset with Adam/AdamW, clipping, momentum, and layerwise diagnostics to test whether the observed distributional distortion becomes a training penalty under realistic optimizer controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimizer-state stress test for binarized gradient distortion
- Success threshold: Sign-binarized optimizer variants lose at least 1.0 percentage point mean held-out accuracy versus matched dense optimizer controls or show repeatable instability across at least 5 seeds, while preserving the observed gradient-distribution distortion diagnostics.
- Stop condition: Stop if sign-binarized variants remain within 0.5 percentage points of dense controls across optimizer settings and no instability appears; record the result as robustness of small-task insensitivity.

## Evidence references

- Artifact root: `<local-path>/projects/binarized-gradient-distribution-audit-fe24169c64ce`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
