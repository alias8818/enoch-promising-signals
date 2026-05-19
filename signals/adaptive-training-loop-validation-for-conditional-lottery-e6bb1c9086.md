# Adaptive Training-Loop Validation for Conditional Lottery Aggregation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-training-loop-validation-for-conditional-lottery-e6bb1c9086`
Run ID: `adaptive-training-loop-validation-for-conditional-lottery-e6bb1c9086-20260518T082256360223+0000`

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

- Internal Enoch project: Adaptive Training-Loop Validation for Conditional Lottery Aggregation: internal_generated:adaptive-training-loop-validation-for-conditional-lottery-e6bb1c9086

## What looked useful

Sparse ticket pools showed exploitable oracle specialization on heterogeneous tasks, and conditional aggregation improved NLL over lottery aggregation ablations. However, accuracy gains over ablations were small/inconsistent and the method failed to beat the parameter-matched dense baseline.

## Boundaries and scale limits

No GPT-2-small-class, language-model, large-corpus, multi-node, or full adaptive end-to-end training-loop validation was run. The aggregator was trained post-hoc on validation predictions rather than used to change ticket training assignments over time.

## Claim scope

Local fixed-seed synthetic classification validation of post-hoc conditional aggregation over sparse ticket MLPs, compared with dense, uniform, unconditional, random-gate, and single-regime controls.

## Why it stopped

Tier 2 medium validation produced a useful mechanism signal but did not meet the success threshold against a real dense baseline; this is not publication-grade evidence.

## Recommended next action

Stop this run as no-paper evidence; only pursue a deepen follow-up if implementing true adaptive routing of training examples to tickets rather than another post-hoc aggregator.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-End Adaptive Ticket Routing for Conditional Lottery Aggregation
- Success threshold: Across at least 5 fixed seeds, adaptive conditional routing must beat the dense baseline by at least 1.0 percentage point accuracy or reduce NLL by at least 0.03 on a heterogeneous task, while not degrading the single-regime control by more than 0.5 percentage point.
- Stop condition: Stop as negative if adaptive routing does not beat the dense baseline on direct accuracy or NLL, or if gains disappear relative to the post-hoc-only conditional aggregator.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-training-loop-validation-for-conditional-lottery-e6bb1c9086`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
