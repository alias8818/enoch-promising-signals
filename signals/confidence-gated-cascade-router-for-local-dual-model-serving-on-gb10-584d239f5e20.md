# Confidence-Gated Cascade Router for Local Dual-Model Serving on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-gated-cascade-router-for-local-dual-model-serving-on-gb10-584d239f5e20`
Run ID: `confidence-gated-cascade-router-for-local-dual-model-serving-on-gb10-584d239f5e20-20260611T121940415266+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c2e658f144b9

## What looked useful

Simple confidence-threshold routing did not meet the predeclared target in any tested scenario. It reduced latency under queue pressure, but either accuracy dropped more than 2 points or the large-model route rate exceeded 65%. Oracle routing showed a large remaining ceiling, indicating confidence calibration/router quality is the likely bottleneck rather than the cascade mechanism itself.

## Boundaries and scale limits

No real LLM serving, token generation, batching, KV-cache, memory pressure, or task-label evaluation was measured; GPU was detected but not used; results cover only deterministic synthetic confidence/quality distributions and short CPU-only runs.

## Claim scope

Bounded synthetic trace/queue simulation of confidence-threshold cascade routing for a fast low-quality model and a slower higher-quality model on a local GB10-assigned worker.

## Why it stopped

Early synthetic proxy falsification: the simple confidence-gated router failed the predeclared quality/latency/route-rate threshold, so the evidence is useful but not publication-grade and not a full real-serving validation.

## Recommended next action

Stop this run as no-paper proxy evidence; run a bounded direct follow-up using actual local small/large model outputs on GB10 with calibrated confidence scores and labeled tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct GB10 Dual-Model Cascade Trace With Calibrated Confidence
- Success threshold: Across at least two task mixes and a sustained local serving load, calibrated or learned routing must keep accuracy within 0.02 of large-only, reduce mean latency by at least 35%, and route no more than 65% of requests to the large model.
- Stop condition: Stop if real confidence scores cannot beat the synthetic threshold trade-off, if route rate must exceed 65% to stay within 2 accuracy points, or if GB10 serving overhead removes the latency benefit.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-cascade-router-for-local-dual-model-serving-on-gb10-584d239f5e20`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
