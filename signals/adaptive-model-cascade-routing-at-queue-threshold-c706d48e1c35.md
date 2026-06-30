# Adaptive Model Cascade Routing at Queue Threshold

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adaptive-model-cascade-routing-at-queue-threshold-c706d48e1c35`
Run ID: `adaptive-model-cascade-routing-at-queue-threshold-c706d48e1c35-20260613T153903685247+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/a4135adbcc7b

## What looked useful

At 16-36 req/s with utility accuracy - 0.20*p95_latency_seconds, adaptive threshold 2 beat static cascade and small-only: at 20 req/s utility was 0.7450 vs static 0.5584 and small-only 0.7113; at 36 req/s utility was 0.7267 vs static -77.4362 and small-only 0.7114. The mechanism is a controlled quality/latency tradeoff: escalation rate fell as overload rose while accuracy stayed above small-only.

## Boundaries and scale limits

No real model inference, GPU serving, batching, prompt-length distribution, production traces, or calibrated task confidence were tested. Evidence is limited to 25,000 synthetic requests per seed, 8 seeds, 8 arrival rates, and fixed service/quality distributions.

## Claim scope

Synthetic discrete-event queueing proxy shows that adaptive suppression of large-model escalation at queue thresholds can improve a latency-weighted accuracy utility under overload, compared with static cascade, large-only, and small-only baselines.

## Why it stopped

Stopped after a reproducible proxy-only useful signal; evidence is not direct or publication-grade, so this run should not proceed to paper writing.

## Recommended next action

Run a bounded trace-driven real-serving follow-up with small and large model endpoints, batching enabled, and the same baselines to test whether the queue-threshold mechanism survives real confidence calibration and GPU serving effects.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Driven Real-Serving Validation of Queue-Threshold Cascade Routing
- Success threshold: Adaptive threshold cascade improves latency-weighted task utility by at least 3% over static cascade and small-only in overload regimes while keeping accuracy within 5 percentage points of static cascade.
- Stop condition: Stop if adaptive threshold fails to beat both static cascade and small-only utility in two independent overload traces, or if confidence calibration causes more than a 5 percentage point accuracy loss without a compensating p95/p99 latency gain.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-model-cascade-routing-at-queue-threshold-c706d48e1c35`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
