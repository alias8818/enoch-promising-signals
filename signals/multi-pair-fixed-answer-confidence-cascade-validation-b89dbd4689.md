# Multi-pair fixed-answer confidence cascade validation

Status: `useful_signal`
Project ID: `multi-pair-fixed-answer-confidence-cascade-validation-b89dbd4689`
Run ID: `multi-pair-fixed-answer-confidence-cascade-validation-b89dbd4689-20260516T194803386788+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Multi-pair fixed-answer confidence cascade validation: internal_generated:multi-pair-fixed-answer-confidence-cascade-validation-b89dbd4689

## What looked useful

Multi-pair context can shift fixed-answer margins, but the observed effect is dominated by context/example formatting rather than a positive high-confidence cascade. High-confidence labels did not improve final-answer margins and sometimes harmed them.

## Boundaries and scale limits

Local validation only: two small open-weight instruction models, synthetic fixed-answer A/B comparison tasks, next-token answer margins. It does not cover frontier models, natural factual QA, multi-turn dialogue, or generated self-reported confidence calibration.

## Claim scope

On two cached small Qwen instruction models (0.5B and 1.5B), fixed-seed multi-pair A/B number-comparison and arithmetic-sum tasks did not show a beneficial high-confidence cascade; on the competent number-comparison task, high-confidence prior solved pairs were no better than low-confidence controls and were worse than neutral correct examples for Qwen 1.5B.

## Why it stopped

Tier 2 fixed-seed direct metrics with a real final-alone baseline and ablations failed to support the beneficial high-confidence cascade hypothesis.

## Recommended next action

Stop this confidence-cascade paper line for synthetic fixed-answer A/B tasks; only revisit with a reframed natural-language factual-QA protocol on stronger models.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/multi-pair-fixed-answer-confidence-cascade-validation-b89dbd4689`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
