# Calibrated gates versus entropy thresholds for local LM cascades

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `calibrated-gates-versus-entropy-thresholds-for-local-lm-ca-3724fdeee7`
Run ID: `calibrated-gates-versus-entropy-thresholds-for-local-lm-ca-3724fdeee7-20260520T173242170783+0000`

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

- Parent run decision: Entropy-gated cascades on a harder local model pair: enoch://control-plane/projects/entropy-gated-cascades-on-a-harder-local-model-pair-85342883f1/runs/entropy-gated-cascades-on-a-harder-local-model-pair-85342883f1-20260520T171729907534+0000
- Parent run decision: Entropy-Gated Local Model Cascades: enoch://control-plane/projects/entropy-gated-local-model-cascades-6a4ea0e74d7a/runs/entropy-gated-local-model-cascades-6a4ea0e74d7a-20260520T161922331865+0000

## What looked useful

Entropy-only calibration preserves the entropy ranking and does not improve cascade accuracy. A richer calibrated gate can improve entropy by about 0.5-0.8 percentage points at some deferral rates, but raw max-probability is a stronger practical baseline and wins all seeds at every tested budget versus entropy.

## Boundaries and scale limits

Only one real multiple-choice dataset, one small local model pair, likelihood-based continuation scoring, 400 calibration and 800 test examples per seed, and no larger 1B/7B or open-ended generation serving validation.

## Claim scope

On 1,400 HellaSwag validation examples scored by a DistilGPT-2 to GPT-2 local cascade, a multifeature calibrated logistic gate gives small, budget-dependent gains over a raw entropy threshold, but it does not robustly beat a simpler raw max-probability threshold.

## Why it stopped

Tier 2 local validation produced a useful no-paper signal: calibrated full gating only showed small and budget-dependent gains versus entropy and did not dominate the real max-probability baseline.

## Recommended next action

Stop paper pursuit for this run; if continuing, run a bounded deepen test where calibrated gates must beat both entropy and raw max-probability across stronger local model pairs and at least two datasets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated cascade gates versus max-probability on stronger local LM pairs
- Success threshold: Calibrated multifeature gate improves mean cascade accuracy by at least 1.5 percentage points over both raw entropy and raw max-probability at two or more deferral budgets, with wins on at least 80% of seed-dataset pairs.
- Stop condition: Stop if calibrated gates fail to beat raw max-probability by at least 0.5 percentage points on average after the first two datasets or if the deferred model is not at least 5 percentage points better than the small model.

## Evidence references

- Artifact root: `<local-path>/projects/calibrated-gates-versus-entropy-thresholds-for-local-lm-ca-3724fdeee7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
