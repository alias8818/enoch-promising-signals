# CascadeKV: Dynamic KV-Cache Routing for Local Model Cascades

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cascadekv-dynamic-kv-cache-routing-for-local-model-cascades-57ed65ce4515`
Run ID: `cascadekv-dynamic-kv-cache-routing-for-local-model-cascades-57ed65ce4515-20260524T201514174270+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b5ed284b6fb1

## What looked useful

Different-width/depth KV transfer failed by tensor shape. Same-shape different-weight caches ran but had relative L2 cache difference 1.397 versus 0.0 for a same-weights control. In simulation, same-model caching reduced estimated latency 59.57% versus no cache, while dynamic same-model routing at 0.76 router accuracy was 12.26% worse than serial same-model caching; dynamic routing only beat that baseline at 0.98 accuracy by 4.90%.

## Boundaries and scale limits

Direct KV evidence used tiny GPT-2-style random models. Latency and memory results are synthetic cost accounting over 240 sessions x 8 turns, not real local LLM serving throughput or answer-quality measurements.

## Claim scope

Naive cross-model KV-cache routing across local cascade members is not valid for ordinary independent transformer models; same-model/session KV reuse is useful, and dynamic routing must beat a strong same-model-cache serial cascade rather than a no-cache baseline.

## Why it stopped

Proxy/direct early falsification, not full validation: tensor compatibility and cache-tensor tests undermine naive cross-model KV routing, while synthetic routing shows the dynamic policy is fragile versus a strong same-model-cache baseline.

## Recommended next action

Stop this run as a proxy/direct early falsification of naive cross-model KV reuse; next bounded work should benchmark a real same-model-cache cascade with calibrated routing and no cross-model KV reuse unless an explicit adapter is introduced.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Local Cascade Benchmark for Same-Model KV-Aware Routing
- Success threshold: Dynamic same-model KV-aware routing improves p95 latency by at least 10% versus same-model-cache serial cascade at no more than 1% absolute quality loss and no more than 10% additional KV memory.
- Stop condition: Stop if dynamic routing fails to beat same-model-cache serial cascade by 5% p95 latency after router calibration, or if quality loss exceeds 1% absolute.

## Evidence references

- Artifact root: `<local-path>/projects/cascadekv-dynamic-kv-cache-routing-for-local-model-cascades-57ed65ce4515`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
