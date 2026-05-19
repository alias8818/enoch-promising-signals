# Robust logprob confidence scores for Qwen2.5-Coder cascade routing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `robust-logprob-confidence-scores-for-qwen2-5-coder-cascade-75c3d70e9f`
Run ID: `robust-logprob-confidence-scores-for-qwen2-5-coder-cascade-75c3d70e9f-20260516T224003227335+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Robust logprob confidence scores for Qwen2.5-Coder cascade routing: internal_generated:robust-logprob-confidence-scores-for-qwen2-5-coder-cascade-75c3d70e9f

## What looked useful

Robust logprob features are useful correctness predictors: cross-validated robust-logprob logistic confidence reached AUROC 0.7453 and AUPRC 0.6121 versus length-only AUROC 0.7211 and AUPRC 0.5672. However, held-out routing with a 1 percentage point train drop tolerance either accepted too few small outputs or lost quality on test; sum_logprob accepted 19.8% on average but had -1.56 pp mean held-out quality delta and -6.41 pp 5th percentile delta versus always-large.

## Boundaries and scale limits

Single dataset family, one Qwen2.5-Coder model pair, greedy decoding, MBPP provided assert tests rather than hidden tests, and no production latency/cost traces or 7B-plus fallback model validation.

## Claim scope

On 257 MBPP sanitized executable tasks with greedy Qwen2.5-Coder-0.5B-Instruct small generations and Qwen2.5-Coder-1.5B-Instruct as the fallback model, small-generation logprob features predict pass/fail correctness above random and calibrated multi-feature logprob confidence beats a length-only confidence baseline. Raw robust logprob scores do not provide reliable held-out cascade savings at near-always-large quality.

## Why it stopped

Direct bounded validation found mechanism support but did not meet a practical cascade-routing threshold, and raw robust logprob scores were not clearly superior to a simple length control.

## Recommended next action

Stop this run as no-paper useful-signal evidence; only continue with a bounded follow-up that tests calibrated logprob confidence on a stronger fallback model and hidden-test-style code evaluation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated logprob routing with a stronger Qwen2.5-Coder fallback
- Success threshold: Calibrated robust logprob confidence must beat length-only AUROC by at least 0.03 and route at least 20% of examples to the small model with mean held-out pass-rate delta no worse than -1 percentage point and 5th percentile bootstrap delta no worse than -3 percentage points versus always-large.
- Stop condition: Stop if oracle cascade headroom over always-large is below 5 percentage points, if calibrated robust logprob fails to beat length-only AUROC by 0.03, or if held-out routing loses more than 1 percentage point mean quality at under 20% small-model acceptance.

## Evidence references

- Artifact root: `<local-path>/projects/robust-logprob-confidence-scores-for-qwen2-5-coder-cascade-75c3d70e9f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
