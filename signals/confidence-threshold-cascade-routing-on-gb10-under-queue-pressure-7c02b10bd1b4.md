# Confidence-Threshold Cascade Routing on GB10 Under Queue Pressure

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `confidence-threshold-cascade-routing-on-gb10-under-queue-pressure-7c02b10bd1b4`
Run ID: `confidence-threshold-cascade-routing-on-gb10-under-queue-pressure-7c02b10bd1b4-20260620T041432072695+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c1d9a11bb32e

## What looked useful

Measured GB10 proxy service times showed a 13.14x slow/fast ratio. In 50k-request queue simulations, pressure-aware routing reduced p95 latency by 67.0% at the near-knee 4936.6 rps scenario versus static_t0.82 with a 0.50 percentage-point expected-accuracy drop, and by 99.5-99.6% once the static high threshold saturated the slow stage with 1.27-4.13 percentage-point expected-accuracy drops. A static low threshold remains a strong latency baseline but pays its accuracy cost at all rates.

## Boundaries and scale limits

Evidence uses fp16 matmul service-time proxies and synthetic confidence/accuracy distributions, not real LLM inference, real confidence calibration, dynamic batching, KV-cache pressure, tokenizer overhead, or production traffic traces.

## Claim scope

In a GB10-calibrated synthetic two-stage cascade queue, pressure-aware confidence threshold lowering prevents catastrophic slow-stage backlog versus a high static threshold near and above the measured verifier-stage saturation knee, with an explicit expected-accuracy cost.

## Why it stopped

Closed as no-paper useful signal because the mechanism is supported only by GB10-calibrated proxy kernels and synthetic queue traces, not direct production/model-serving evidence.

## Recommended next action

Run a bounded real-model GB10 follow-up using an actual small/large LLM cascade, calibrated confidence scores, measured task quality, and the same static-high, static-low, and pressure-aware policies across a load sweep that crosses the slow-stage saturation knee.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Model GB10 Confidence Cascade Under Slow-Stage Saturation
- Success threshold: Across at least one near-knee and one above-knee real-model load point, pressure-aware routing reduces p95 latency by at least 50% versus the high static threshold while losing no more than 2 percentage points of measured task quality, and retains at least 1 percentage point higher measured quality than the low static threshold at comparable p95 latency.
- Stop condition: Stop if real confidence is poorly calibrated enough that thresholding cannot separate easy from hard requests, if GB10 memory pressure prevents running both models without invalidating the queue test, or if pressure-aware routing fails to beat either static baseline on the defined quality-latency threshold.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-threshold-cascade-routing-on-gb10-under-queue-pressure-7c02b10bd1b4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
