# Canary-Commit Gradient Validation for Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `canary-commit-gradient-validation-for-volunteer-training-4dee7196b032`
Run ID: `canary-commit-gradient-validation-for-volunteer-training-4dee7196b032-20260527T174957629778+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/80d69c8860f5

## What looked useful

AUC improved with canary count: omitted-canary detection AUC rose from 0.552 at 1 canary to 0.922 at 16, and flipped-canary AUC rose from 0.605 to 0.978. But at a 1% honest false-rejection budget, 16 canaries detected only 2.25% of omitted-canary commits and 21.75% of flipped-canary commits, so the tested one-shot mixed-gradient projection is too weak as a standalone validator.

## Boundaries and scale limits

Toy synthetic data only; no real volunteer network, no large model, no adaptive adversary, no secure aggregation, no compressed gradients, and no long training-loop quality measurement.

## Claim scope

In a synthetic 610-gradient-dimension two-layer MLP with 64 normal samples per volunteer batch and 400 trials per canary count, projection onto a hidden canary-gradient direction creates a monotonic audit signal but is not a reliable standalone gate at strict honest false-rejection budgets.

## Why it stopped

Proxy/toy early falsification of the simple one-shot mixed-batch projection validator; it shows a signal but fails a practical strict-threshold reliability bar rather than providing full validation.

## Recommended next action

Run a bounded sequential or orthogonal-codebook canary follow-up and require at least 80% omitted-canary detection at no more than 5% honest false rejection before considering larger volunteer-training validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sequential Orthogonal Canary Gradient Validator
- Success threshold: At least 80% omitted-canary detection and 90% flipped-canary detection at no more than 5% honest false rejection, with monotonic improvement over the one-shot baseline across seeds.
- Stop condition: Stop negative if the sequential/codebook validator still detects less than 60% of omitted-canary updates at a 5% honest false-rejection budget or requires a canary fraction larger than 25% of the volunteer batch.

## Evidence references

- Artifact root: `<local-path>/projects/canary-commit-gradient-validation-for-volunteer-training-4dee7196b032`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
