# Queue-Pressure Adaptive Cascade Routing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `queue-pressure-adaptive-cascade-routing-591e29985932`
Run ID: `queue-pressure-adaptive-cascade-routing-591e29985932-20260528T062400113953+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/3143dc884d0d

## What looked useful

Queue-pressure adaptive escalation reduced SLO violations and improved utility only when the large-model stage was severely saturated; in easy, steady, and moderate-burst cases, static confidence routing had higher utility because adaptive routing sacrificed too much answer quality.

## Boundaries and scale limits

No real model inference, no calibrated production confidence scores, no public or private production trace replay, no GPU serving stack, and no datacenter-scale validation. Results cover only the simulator assumptions and 40 deterministic seeds per scenario.

## Claim scope

Synthetic discrete-event serving simulation of two-stage small/large model cascades under steady, easy, bursty, and severe-burst arrival patterns.

## Why it stopped

Synthetic evidence is mixed: adaptive queue pressure is useful as overload protection in severe saturation, but it is not generally better than static confidence routing and the run does not include direct model-serving evidence.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should replay measured small/large model latencies and calibrated confidence-quality curves on a public request trace before considering a paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-driven queue-pressure cascade replay with measured model latencies
- Success threshold: Adaptive routing must improve mean utility by at least 5% in overload intervals and lose no more than 1% mean utility in steady/easy intervals versus the best tuned static threshold.
- Stop condition: Stop if adaptive routing fails to beat tuned static routing in overload intervals or requires more than 3% steady-load quality loss to meet the SLO.

## Evidence references

- Artifact root: `<local-path>/projects/queue-pressure-adaptive-cascade-routing-591e29985932`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
