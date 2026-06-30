# Early-exit cascade router for CPU serving

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `early-exit-cascade-router-for-cpu-serving-545c67795e74`
Run ID: `early-exit-cascade-router-for-cpu-serving-545c67795e74-20260523T110636121032+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/29f7362601bb

## What looked useful

Across five 50,000-request seeds, threshold 0.65 was consistently the best cascade under 1 percentage point accuracy loss: 94.25% mean accuracy, 0.59 percentage-point mean loss versus always-large, 15.29% escalation, and 75.93% mean-latency reduction versus always-large.

## Boundaries and scale limits

Synthetic binary classification only; CPU cost is emulated with deterministic math loops; no real inference engine, production trace, concurrency, batching, or tail-latency measurement. Absolute latency values are not transferable.

## Claim scope

In a deterministic synthetic CPU-serving benchmark with a cheap misspecified classifier, a heavier nonlinear classifier, and confidence-threshold routing, an early-exit cascade reduced mean latency substantially while keeping accuracy within 1 percentage point of the always-heavy baseline.

## Why it stopped

Closed as no-paper useful signal: synthetic evidence supports the routing mechanism, but production CPU-serving claims require direct model-serving evidence.

## Recommended next action

Run a bounded direct-evidence follow-up on a real CPU inference stack with a small/large model pair and report quality plus p50/p95/p99 latency under concurrent serving.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU inference validation for confidence-threshold early-exit cascades
- Success threshold: At least 40% p50 or mean latency reduction versus always-large, no more than 1 percentage point quality loss or task-equivalent tolerance, and no p99 regression large enough to erase serving value.
- Stop condition: Stop if the cascade cannot achieve at least 20% mean latency reduction before exceeding the quality-loss tolerance, or if router overhead and tail latency erase the measured benefit.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-cascade-router-for-cpu-serving-545c67795e74`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
