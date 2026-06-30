# Real prefix-cache latency validation for exact-anchor prompt layouts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-prefix-cache-latency-validation-for-exact-anchor-prom-de31dec2da`
Run ID: `real-prefix-cache-latency-validation-for-exact-anchor-prom-de31dec2da-20260529T213113511802+0000`

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

- Parent run decision: Exact-Anchor Prefix Caching for Multi-Turn Long-Context Reuse: enoch://control-plane/projects/exact-anchor-prefix-caching-for-multi-turn-long-context-reuse-3a8f8e6f89a9/runs/exact-anchor-prefix-caching-for-multi-turn-long-context-reuse-3a8f8e6f89a9-20260529T175231516507+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ece0442c89b7

## What looked useful

A controlled real-serving test showed exact-anchor prompt layouts can trigger large prefix-cache reuse: median cached tokens were 3808 for exact-prefix repeats versus 35 for perturbed-before-anchor controls, with a 28.18x steady-state wall-latency ratio.

## Boundaries and scale limits

Single small quantized model, one serving engine, one host, sequential single-slot requests, one prompt length, synthetic deterministic content, no production provider cache, no concurrency, no cache eviction or multi-tenant testing.

## Claim scope

In a local CUDA llama.cpp server with one SmolLM2-135M GGUF model, one slot, 4096 context, and synthetic prompts of about 3.7k-3.8k tokens, preserving an exact long prefix before an anchor reduced steady-state wall latency from a 319.98 ms median control to 11.36 ms while increasing cached tokens from 35 to 3808.

## Why it stopped

Tier 1 controlled small direct test completed with useful mechanism support, but the evidence is too narrow for publication readiness.

## Recommended next action

Run a medium confirmation on vLLM or a hosted provider with automatic prompt caching across 3-5 prefix lengths, realistic prompt bodies, and sequential plus concurrent modes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium provider/vLLM confirmation of exact-anchor prefix-cache latency
- Success threshold: Exact-anchor arms must show at least 5x median TTFT or prefill-latency improvement over same-length perturbed-before-anchor controls, with cached-token counters or equivalent prefill counters confirming reuse for at least two prefix lengths.
- Stop condition: Stop if cached-token counters do not differ materially from controls or if median TTFT improvement is below 2x for two serving stacks/prefix lengths after warmup.

## Evidence references

- Artifact root: `<local-path>/projects/real-prefix-cache-latency-validation-for-exact-anchor-prom-de31dec2da`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
