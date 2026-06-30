# Real local CPU workload validation for confidence-threshold cascades

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-local-cpu-workload-validation-for-confidence-threshol-09ec363a16`
Run ID: `real-local-cpu-workload-validation-for-confidence-threshol-09ec363a16-20260529T150253451354+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Confidence-threshold model cascade for local CPU serving: enoch://control-plane/projects/confidence-threshold-model-cascade-for-local-cpu-serving-ba2f82d244b1/runs/confidence-threshold-model-cascade-for-local-cpu-serving-ba2f82d244b1-20260529T103341055423+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/630e55275c8c

## What looked useful

Across four 8k/2k AG News CPU runs, all runs met the preregistered threshold. Best qualifying cascades used thresholds 0.97 or 0.99, averaged 0.8725 accuracy versus 0.87575 expensive-only accuracy, had worst qualifying accuracy loss 0.0045, avoided 47.05% to 57.00% of expensive calls, and estimated 1.63x mean inference speedup versus expensive-only.

## Boundaries and scale limits

Evidence is limited to one public text dataset, two simple CPU Naive Bayes model variants, 8,000 training examples, 2,000 held-out examples per run, and four random seeds. It does not cover transformer/LLM classifiers, production serving concurrency, distribution shift, calibrated neural confidence, or tail latency.

## Claim scope

On a bounded AG News local CPU text-classification workload using hashed Naive Bayes models, a high cheap-model confidence threshold can preserve expensive-model accuracy within 1 absolute percentage point while avoiding at least 30% of expensive-model inference calls.

## Why it stopped

Tier 1 direct validation produced a useful mechanism signal but only for one small local CPU workload; strict paper gate remains closed.

## Recommended next action

Run a deepen follow-up on multiple real CPU classification tasks with calibrated confidence and concurrent latency measurement before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated multi-workload CPU validation for confidence-threshold cascades
- Success threshold: At least 3/3 workloads meet accuracy loss <= 1 absolute percentage point and expensive-call avoidance >= 30%, with measured p95 latency improvement versus expensive-only inference.
- Stop condition: Stop as negative if fewer than 2/3 workloads meet the accuracy/call-avoidance threshold or if calibration removes the apparent benefit.

## Evidence references

- Artifact root: `<local-path>/projects/real-local-cpu-workload-validation-for-confidence-threshol-09ec363a16`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
