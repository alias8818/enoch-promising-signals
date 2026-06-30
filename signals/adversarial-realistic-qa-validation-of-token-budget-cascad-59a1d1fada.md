# Adversarial realistic QA validation of token-budget cascade

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `adversarial-realistic-qa-validation-of-token-budget-cascad-59a1d1fada`
Run ID: `adversarial-realistic-qa-validation-of-token-budget-cascad-59a1d1fada-20260609T184134378723+0000`

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

- Parent run decision: Real-model GB10 validation of token-budget cascade for long-context QA: enoch://control-plane/projects/real-model-gb10-validation-of-token-budget-cascade-for-lon-ec1e56e57d/runs/real-model-gb10-validation-of-token-budget-cascade-for-lon-ec1e56e57d-20260609T121913572159+0000
- Parent run decision: Token-Budget Cascade for Long-Context Home Inference on gb10: enoch://control-plane/projects/token-budget-cascade-for-long-context-home-inference-on-gb10-98812a8100aa/runs/token-budget-cascade-for-long-context-home-inference-on-gb10-98812a8100aa-20260609T071555579853+0000

## What looked useful

The guarded cascade reduced mean token exposure by 30.5% versus the 320-token full baseline, but achieved only 77.9% of full-baseline F1 and underperformed the simple fixed 160-token baseline. A stricter threshold recovered some F1 but spent more tokens than full context and still trailed fixed_medium.

## Boundaries and scale limits

Tested one extractive QA model, constructed prepended distractors, 540 medium-run evaluations across three fixed seeds, and token exposure rather than full production serving cost. Not a broad LLM or multi-dataset validation.

## Claim scope

On adversarially perturbed SQuAD validation examples using distilbert-base-cased-distilled-squad, a fixed-threshold 96->160->320 token-budget cascade with a distractor-answer guard failed to preserve full-context extractive QA quality while saving tokens.

## Why it stopped

Medium confirmation with fixed seeds, direct QA metrics, ablations, random control, and real fixed-context baselines failed the predefined non-inferiority threshold.

## Recommended next action

Stop this cascade variant as no-paper evidence; if continuing, test a learned/calibrated early-acceptance policy against the same fixed-medium and full-context baselines before scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated early-acceptance policy for adversarial QA token cascades
- Success threshold: Held-out calibrated cascade F1 >= 95% of fixed_full F1, mean token exposure <= 75% of fixed_full, and F1 > fixed_medium at comparable or lower token exposure.
- Stop condition: Stop if calibration cannot beat fixed_medium F1 while retaining at least 25% token savings on the first held-out medium run.

## Evidence references

- Artifact root: `<local-path>/projects/adversarial-realistic-qa-validation-of-token-budget-cascad-59a1d1fada`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
