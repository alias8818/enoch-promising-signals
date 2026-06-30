# Canary Gradient Injection for Volunteer Validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `canary-gradient-injection-for-volunteer-validation-74f759fcf901`
Run ID: `canary-gradient-injection-for-volunteer-validation-74f759fcf901-20260528T093231157433+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4bc252eb86c7

## What looked useful

The canary signal is real but too weak for practical single-round single-volunteer validation at modest canary budgets in larger cohorts. With mean aggregation and no noise, r=0.1 gave TPR@1%FPR of 0.534 at 8 clients, 0.130 at 32, 0.042 at 128, and 0.024 at 512. TPR>=0.8 required r=0.3 for 8-32 clients, r=1.0 for 128 clients, and was not reached for 512 clients. Coordinate median weakened detection further.

## Boundaries and scale limits

No real model training, no secure aggregation implementation, no non-IID data, no optimizer dynamics, and no multi-round accumulation. Tested up to 512 clients, dimension 4096, 1000 trials per cell, mean and coordinate median aggregation, aggregate noise L2 scales 0, 0.01, and 0.05.

## Claim scope

Synthetic clipped-gradient aggregation simulation: one volunteer injects one private random canary into one normalized update and validates inclusion from one released aggregate using a dot-product test calibrated to 1% false-positive rate.

## Why it stopped

Proxy simulation gives an early practical falsification of naive single-round canary-gradient volunteer validation at modest canary budgets and realistic cohort sizes; this is not a full production validation.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should evaluate multi-round canary accumulation on real federated model gradients before considering any larger validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-round canary accumulation on real federated gradients
- Success threshold: For n>=128, canary_ratio<=0.1, and at most 50 rounds, reach TPR>=0.8 at 1% FPR with final validation loss or accuracy within 1% relative of the no-canary baseline.
- Stop condition: Stop if TPR remains below 0.5 at 1% FPR after 50 rounds, or if canary injection degrades validation quality by more than 2% relative to baseline.

## Evidence references

- Artifact root: `<local-path>/projects/canary-gradient-injection-for-volunteer-validation-74f759fcf901`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
