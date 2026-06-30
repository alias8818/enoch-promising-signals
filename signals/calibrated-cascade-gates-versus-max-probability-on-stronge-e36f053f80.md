# Calibrated cascade gates versus max-probability on stronger local LM pairs

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `48`
Project ID: `calibrated-cascade-gates-versus-max-probability-on-stronge-e36f053f80`
Run ID: `calibrated-cascade-gates-versus-max-probability-on-stronge-e36f053f80-20260520T174832603520+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `48`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Entropy-gated cascades on a harder local model pair: enoch://control-plane/projects/entropy-gated-cascades-on-a-harder-local-model-pair-85342883f1/runs/entropy-gated-cascades-on-a-harder-local-model-pair-85342883f1-20260520T171729907534+0000
- Parent run decision: Calibrated gates versus entropy thresholds for local LM cascades: enoch://control-plane/projects/calibrated-gates-versus-entropy-thresholds-for-local-lm-ca-3724fdeee7/runs/calibrated-gates-versus-entropy-thresholds-for-local-lm-ca-3724fdeee7-20260520T173242170783+0000

## What looked useful

Calibration helped probability calibration but not cascade routing. Raw max probability remained equal or better at matched route-to-large fractions on the main stronger pair, and the second pair showed only tiny calibrated gains at one budget with bootstrap intervals crossing zero.

## Boundaries and scale limits

Evidence is limited to HellaSwag multiple-choice scoring with GPT-2-family local models (`distilgpt2` -> `gpt2`, `gpt2` -> `gpt2-medium`), one fixed sample seed, and gates trained to predict small-model correctness rather than direct large-model routing benefit. It does not test modern 7B+ instruction-tuned pairs or cross-dataset robustness.

## Claim scope

On two local GPT-2-family cascade pairs evaluated on 8,000 sampled HellaSwag validation examples each, with 4,000 examples held out for exact-budget cascade metrics, calibrating the small model's confidence substantially improved ECE but did not improve cascade accuracy over raw max-probability routing at matched route-to-large budgets.

## Why it stopped

Direct bounded validation falsified the target threshold for calibrated gates: despite lower ECE, isotonic and logistic calibrated gates did not beat raw max-probability routing under exact matched cascade budgets on the tested local LM pairs.

## Recommended next action

Stop this calibrated-correctness-gate branch as no-paper evidence; if continuing within the lineage, test a direct value-of-routing gate that predicts large-minus-small correctness rather than calibrated small-model correctness.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Direct value-of-routing gates for local LM cascades
- Success threshold: At least +1.0 percentage point held-out cascade accuracy over raw max-probability routing at two or more nontrivial matched route budgets, with 95% bootstrap intervals excluding zero on at least one budget.
- Stop condition: Stop negative if the value-of-routing gate fails to beat raw max probability by at least +0.5 percentage points at every nontrivial budget or if gains vanish under bootstrap uncertainty.

## Evidence references

- Artifact root: `<local-path>/projects/calibrated-cascade-gates-versus-max-probability-on-stronge-e36f053f80`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
