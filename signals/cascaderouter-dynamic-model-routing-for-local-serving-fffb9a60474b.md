# CascadeRouter: Dynamic Model Routing for Local Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cascaderouter-dynamic-model-routing-for-local-serving-fffb9a60474b`
Run ID: `cascaderouter-dynamic-model-routing-for-local-serving-fffb9a60474b-20260527T120741034910+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/526badc83053

## What looked useful

Latency-aware cascade routing can keep simulated p95 latency near 1-1.5 seconds through 8 QPS while reducing mean compute cost about 34-48% versus all-large, but quality drops from -4.8 percentage points at 2 QPS to -8.7 points at 8 QPS. Static cascades preserve quality better but can still overload the large-model queue at high load.

## Boundaries and scale limits

No real LLM inference, real quality labels, GPU batching, KV cache behavior, UMA memory pressure, tokenizer effects, or production traffic traces were tested. Results should be treated as a mechanism probe only.

## Claim scope

Synthetic discrete-event local-serving simulation with small/medium/large model classes, confidence cascades, Poisson arrivals, hard-tailed prompt difficulty, and queue-aware escalation thresholds.

## Why it stopped

Proxy-only useful signal: the queueing mechanism is supported, but synthetic model accuracy and latency are not direct evidence for real local LLM serving.

## Recommended next action

Run a bounded real-model serving follow-up with calibrated confidence thresholds, labeled tasks, and measured GPU/UMA latency/cost before considering any paper or deployment claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CascadeRouter serving probe
- Success threshold: At 4-8 QPS equivalent load, latency-aware routing achieves at least 3x lower p95 latency than all-large or static cascade, stays within 5 percentage points of all-large quality, and reduces compute cost by at least 20%.
- Stop condition: Stop as negative if calibrated latency-aware routing cannot stay within 5 quality points of all-large at any load where it also reduces p95 latency by at least 3x and compute by at least 20%.

## Evidence references

- Artifact root: `<local-path>/projects/cascaderouter-dynamic-model-routing-for-local-serving-fffb9a60474b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
