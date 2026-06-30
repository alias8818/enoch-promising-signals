# Dynamic Anchor Offloading for Home Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-anchor-offloading-for-home-inference-c877486eab10`
Run ID: `dynamic-anchor-offloading-for-home-inference-c877486eab10-20260525T093341528818+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f262c98f3c9e

## What looked useful

Dynamic anchors are only useful when selected at per-head/layer granularity and when the resident budget leaves enough non-recent anchor slots. At 16.7% resident tokens, dynamic_head retained 0.7296 mean attention mass versus 0.6930 for sink+recent and 0.6922 for static_even; at 25.0%, it retained 0.7764 versus 0.7390 and 0.7314.

## Boundaries and scale limits

This is a trace-level proxy on a small model and short context. It does not measure end-to-end home inference latency, host-device transfer cost, quality/perplexity under approximate attention, real KV allocator behavior, or Llama-class 1B-8B long-context serving.

## Claim scope

On a small CUDA attention-trace experiment with distilgpt2 at sequence length 384, per-layer/per-head dynamic anchors retained more late-query attention mass than static anchors and sink+recent baselines at 12.5%-25% resident-token budgets, but not conclusively at the tightest 8.3% budget.

## Why it stopped

Proxy attention-trace evidence is useful but insufficient for a paper or full validation because no real offload scheduler, transfer path, latency measurement, or quality degradation test was implemented.

## Recommended next action

Build a bounded serving prototype that implements per-head/layer dynamic anchor KV residency and measure latency, memory, and quality against sink+recent and static policies on a 1B-8B local model at 4k-32k contexts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Serving Prototype for Per-Head Dynamic Anchor KV Residency
- Success threshold: At 50% or lower KV residency, dynamic anchors improve retained quality/perplexity versus sink+recent with no more than 10% median latency regression, or achieve at least 20% lower memory residency at equal quality and latency.
- Stop condition: Stop if dynamic anchors fail to beat sink+recent on quality-adjusted latency/memory at two resident budgets or if page-in overhead erases the retained-attention advantage.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-anchor-offloading-for-home-inference-c877486eab10`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
