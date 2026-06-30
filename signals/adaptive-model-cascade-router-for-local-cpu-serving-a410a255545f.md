# Adaptive Model Cascade Router for Local CPU Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-model-cascade-router-for-local-cpu-serving-a410a255545f`
Run ID: `adaptive-model-cascade-router-for-local-cpu-serving-a410a255545f-20260628T212307642886+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2731a9e81bfb

## What looked useful

Adaptive routing can find a useful latency-quality tradeoff when easy and hard requests are separable by cheap signals, but the current router leaves hard-slice quality on the table and needs direct LLM-serving validation before any paper or deployment claim.

## Boundaries and scale limits

Proxy-only evidence: softmax classifiers and synthetic task modes, not real local LLMs, token workloads, answer-quality metrics, or production traffic. Hard/full-context examples still showed under-escalation failures.

## Claim scope

On a deterministic synthetic CPU-serving proxy, an adaptive small/medium/large cascade router using cheap confidence and request-feature signals reduced measured per-request CPU cost by 65.39% versus all-large and 16.82% versus a static confidence small/large cascade, with a 0.0152 absolute held-out accuracy loss versus all-large.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only, despite supporting the routing mechanism.

## Recommended next action

Run a bounded direct CPU LLM-serving follow-up with quantized small/medium/large local models, real prompt features, and task-quality scoring against all-large and static-cascade baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct quantized local LLM adaptive cascade benchmark
- Success threshold: Mean latency at least 40% lower than all-large, quality no more than 2 absolute points below all-large, and adaptive router at least 10% faster than static confidence cascade at matched quality.
- Stop condition: Stop if the router cannot stay within 2 absolute quality points of all-large without routing more than 70% of requests to the large tier, or if local CPU inference cannot complete the bounded prompt suite within the allocated worker budget.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-model-cascade-router-for-local-cpu-serving-a410a255545f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
