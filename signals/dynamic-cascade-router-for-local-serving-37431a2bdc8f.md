# Dynamic Cascade Router for Local Serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-cascade-router-for-local-serving-37431a2bdc8f`
Run ID: `dynamic-cascade-router-for-local-serving-37431a2bdc8f-20260528T230813530213+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4b7f37f21ef6

## What looked useful

Selective escalation can preserve SLO-goodput under load with about 2.7% large-model use, but dynamic deadline gating added only 0.0003-0.0007 absolute SLO-goodput over a static cascade across 180-420 rps.

## Boundaries and scale limits

Synthetic binary classification only; no real LLM generation, batching, prompt-length variability, KV-cache pressure, multi-worker scheduling, or real request trace. Service times use local CUDA measurements plus conservative per-request serving floors.

## Claim scope

In a five-seed synthetic local-serving proxy with CUDA-measured small/large model latency and single-server queue replay, selective confidence cascading improved SLO-goodput over always-large and slightly over small-only, but the deadline-aware dynamic policy did not materially outperform a tuned static confidence cascade.

## Why it stopped

Proxy/early falsification of the dynamic-router novelty: the cascade mechanism worked, but dynamic deadline-aware routing was effectively tied with static confidence routing in the bounded experiment.

## Recommended next action

Stop this run as no-paper useful signal; deepen with real local-model serving traces before investing in a dynamic-router paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Local-Model Trace Test for Dynamic Cascade Routing
- Success threshold: Dynamic router improves held-out SLO-goodput by >=0.02 absolute over tuned static cascade at no more than 0.005 absolute accuracy loss and no higher p95 latency.
- Stop condition: Stop if dynamic routing improves SLO-goodput by <0.005 absolute over static cascade on two real traces or if quality loss exceeds 0.01 absolute at the best latency point.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-cascade-router-for-local-serving-37431a2bdc8f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
