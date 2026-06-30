# CPU Cascade Router for Latency-Quality Tradeoff

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-cascade-router-for-latency-quality-tradeoff-07bfb5e4fcd1`
Run ID: `cpu-cascade-router-for-latency-quality-tradeoff-07bfb5e4fcd1-20260523T233503370717+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/12311a2acc01

## What looked useful

Threshold 0.85 matched the KNN expert's 0.9825 accuracy while reducing mean latency from 8.679 ms to 1.132 ms and p95 latency from 48.996 ms to 1.993 ms, routing 10.2% of requests to the expert. Threshold 0.92 reached 0.9857 accuracy with 1.330 ms mean latency and 16.9% expert routing.

## Boundaries and scale limits

Only 629 unique test examples from a classical ML digits dataset were used, with repeated per-example timing on one virtualized CPU worker. No LLM serving, batching, concurrency, queueing, real user traffic, semantic quality labels, or calibration drift was tested.

## Claim scope

On a small local CPU benchmark using sklearn digits, a confidence-threshold cascade from logistic regression to a slower KNN expert can match or exceed the KNN expert's accuracy while substantially reducing per-request mean and p95 latency.

## Why it stopped

No-paper useful signal: the mechanism worked in a small local benchmark, but this is not direct production or LLM evidence and is insufficient for publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on a real CPU text/model-serving workload with calibrated cheap-model confidence, matched-quality constraints, and p95 latency success thresholds before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU cascade router on real text serving workload
- Success threshold: At matched or better quality versus the heavy expert within 0.2 absolute percentage points, the cascade must reduce p95 latency by at least 3x and route no more than 50% of requests to the heavy expert.
- Stop condition: Stop as negative if the cascade cannot match heavy-expert quality within 0.2 percentage points, or if p95 latency speedup is below 2x after threshold tuning on validation data.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-cascade-router-for-latency-quality-tradeoff-07bfb5e4fcd1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
