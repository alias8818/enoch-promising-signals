# Adaptive Cascade Router for Local Multi-Model Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-cascade-router-for-local-multi-model-serving-1b6f4e4aa034`
Run ID: `adaptive-cascade-router-for-local-multi-model-serving-1b6f4e4aa034-20260527T220013319491+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/3731a45b2210

## What looked useful

Adaptive queue-aware routing reduced static-cascade queue collapse and improved utility versus best fixed cascade variants, but high overload favored explicit quality shedding to the small model.

## Boundaries and scale limits

Synthetic workload only; no real LLM serving, GPU batching, KV-cache memory pressure, tokenizer length distribution, or production traffic was measured. Full claims require direct local serving benchmarks with real models and calibrated confidence signals.

## Claim scope

In a bounded synthetic discrete-event proxy for local three-model serving, a queue-aware adaptive cascade improved utility over a fixed-threshold static cascade family across low, balanced, high, and bursty load scenarios, but did not dominate the cheap-model-only baseline under high overload.

## Why it stopped

Proxy simulation produced useful mixed evidence, but the claim is not direct or publication-grade; finalize as no-paper useful signal.

## Recommended next action

Run a bounded direct local-serving benchmark with real small/medium/large local models and an overload-shedding adaptive router before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct local-model benchmark for adaptive cascade routing with overload shedding
- Success threshold: Adaptive-with-shedding improves SLO-adjusted utility by at least 0.03 over the best tuned static cascade and matches or beats always-small utility outside the highest overload scenario, with less than 1 percentage point accuracy loss versus a latency-feasible cascade baseline.
- Stop condition: Stop if measured model confidence is too poorly calibrated to route better than tuned static thresholds, or if overload shedding collapses to always-small across balanced and bursty loads.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-cascade-router-for-local-multi-model-serving-1b6f4e4aa034`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
