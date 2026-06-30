# Queue-Pressure Adaptive Model Cascade Routing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `queue-pressure-adaptive-model-cascade-routing-d8f5d5d21cf4`
Run ID: `queue-pressure-adaptive-model-cascade-routing-d8f5d5d21cf4-20260601T015340731072+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/02a91e825c70

## What looked useful

Queue pressure is useful as a safety valve for aggressive quality-seeking cascades, but the tested adaptive policy traded higher cost and worse p99/SLO miss rates for higher quality and small utility gains versus the best static threshold.

## Boundaries and scale limits

Synthetic arrivals, synthetic confidence/quality calibration, exponential service times, six random seeds, and no real LLM serving traces or measured model latencies. Results do not establish production superiority or paper-grade generality.

## Claim scope

In a synthetic two-model cascade simulation with bursty and stationary arrivals, queue-pressure-aware escalation improved scalar utility over the best fixed confidence threshold by 0.0049 to 0.0152 while preventing collapse relative to aggressive fixed thresholds.

## Why it stopped

Synthetic medium evidence is useful but mixed; it supports the pressure-safety mechanism while showing that the policy does not dominate best fixed thresholds on latency or cost.

## Recommended next action

Run a bounded trace-replay follow-up using measured small/large model latency distributions and calibrated confidence-quality curves, with a constrained objective that requires utility gain without worse p99 latency than the best static threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-replay constrained queue-pressure cascade routing
- Success threshold: Adaptive routing improves mean utility by at least 1% over the best static threshold while p99 latency is no worse than 5% above best static in at least 8 of 10 seeds or trace windows.
- Stop condition: Stop if adaptive routing cannot meet the p99 constraint in two calibrated traces or if utility gains disappear after matching escalation rate.

## Evidence references

- Artifact root: `<local-path>/projects/queue-pressure-adaptive-model-cascade-routing-d8f5d5d21cf4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
