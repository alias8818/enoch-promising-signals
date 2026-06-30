# Q-Route: Quantization-Aware Routing in Model Cascades

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `q-route-quantization-aware-routing-in-model-cascades-e2c498ca23dc`
Run ID: `q-route-quantization-aware-routing-in-model-cascades-e2c498ca23dc-20260524T200640351436+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b5ed284b6fb1

## What looked useful

Across 10 held-out runs, Q-route improved over confidence-only by +1.11 percentage points at 5% escalation and +0.92 points at 10% escalation, with no negative seeds at those budgets. Q-route also captured more cheap-model errors than confidence-only at 10% escalation on both datasets.

## Boundaries and scale limits

Synthetic datasets only; small MLP only; symmetric post-training weight quantization only; escalation fraction used as a cost proxy; no real LLM, production quantization backend, latency, energy, or distribution-shift validation.

## Claim scope

In a bounded NumPy probe with two synthetic multiclass datasets, a validation-tuned quantization-fragility routing score improved held-out accuracy over confidence-only routing at tight 5-10% escalation budgets in a 3-bit-quantized-to-float MLP cascade.

## Why it stopped

Closed as no-paper useful signal: bounded synthetic evidence supports the routing mechanism, but it is proxy-level rather than direct publication-grade validation.

## Recommended next action

Run the same validation-tuned Q-route protocol on a real non-synthetic cascade with measured quality-latency tradeoffs and production-relevant quantization before considering a paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Q-Route on Real Quantized Model Cascades with Latency Measurement
- Success threshold: At 5-20% escalation, Q-route must improve area under the quality-latency curve by at least 1% relative to the best tuned non-quantization-aware baseline on held-out test data, without increasing p95 latency at fixed escalation budget.
- Stop condition: Stop if Q-route fails to beat the best tuned confidence/calibration baseline on two independent real-task seeds or if the measured latency overhead of computing fragility exceeds the recovered fallback savings.

## Evidence references

- Artifact root: `<local-path>/projects/q-route-quantization-aware-routing-in-model-cascades-e2c498ca23dc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
