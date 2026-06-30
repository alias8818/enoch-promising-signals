# Queue-Aware Early Exit Routing for Local Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `queue-aware-early-exit-routing-for-local-serving-0bc692d4cb71`
Run ID: `queue-aware-early-exit-routing-for-local-serving-0bc692d4cb71-20260529T153413271449+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1e8d7bf3cbbd

## What looked useful

Queue pressure is a plausible control signal for early-exit routing: it reduced synthetic p95/p99 latency in all tested burst regimes and improved heavy-burst deadline hit rate by 4.4 percentage points versus static aggressive routing at about 0.010 expected-accuracy loss. The mechanism failed to restore SLA performance near saturation and crossed the 0.02 quality-loss target there.

## Boundaries and scale limits

No real model was served; confidence, accuracy, and layer service times were synthetic. The result does not validate transformer accuracy, calibration, GPU kernel behavior, batching, multi-worker queues, token streaming, or production traffic traces.

## Claim scope

Synthetic single-server bursty local-serving simulation with calibrated early-exit confidence at layers 4, 8, and 12. Queue-aware thresholds reduced p95 and p99 latency versus the strongest static deadline-hit comparator across three replicated scenarios, with scenario-dependent deadline-hit and expected-accuracy tradeoffs.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only and mixed across SLA and quality metrics, not because the idea is fully falsified.

## Recommended next action

Run a bounded direct-serving follow-up using a real early-exit model, replayed burst traces, calibrated confidence, true task accuracy, and the same queue-aware threshold policy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct local-serving test of queue-aware early-exit thresholds
- Success threshold: At least 15% lower p95 latency than the best static threshold in moderate and heavy burst traces, no more than 0.02 absolute accuracy loss, and no worse deadline-hit rate in the same traces.
- Stop condition: Stop if real confidence is poorly calibrated enough that queue-aware threshold changes exceed 0.02 accuracy loss before achieving 15% p95 latency reduction, or if batching/serving overhead erases the simulated latency benefit.

## Evidence references

- Artifact root: `<local-path>/projects/queue-aware-early-exit-routing-for-local-serving-0bc692d4cb71`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
