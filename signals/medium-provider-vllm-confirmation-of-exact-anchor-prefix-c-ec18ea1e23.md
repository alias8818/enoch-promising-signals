# Medium provider/vLLM confirmation of exact-anchor prefix-cache latency

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `medium-provider-vllm-confirmation-of-exact-anchor-prefix-c-ec18ea1e23`
Run ID: `medium-provider-vllm-confirmation-of-exact-anchor-prefix-c-ec18ea1e23-20260530T014313377073+0000`

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
- Parent run decision: Real prefix-cache latency validation for exact-anchor prompt layouts: enoch://control-plane/projects/real-prefix-cache-latency-validation-for-exact-anchor-prom-de31dec2da/runs/real-prefix-cache-latency-validation-for-exact-anchor-prom-de31dec2da-20260529T213113511802+0000

## What looked useful

Real vLLM serving metrics support the mechanism: enabled runs showed 26,496 local cached prompt tokens and exact-prefix median TTFT of 8.41 ms across 48 requests, versus 11.67 ms for perturbed prefixes; the disabled baseline had near-identical exact and perturbed medians around 11.05 ms and zero prefix-cache hits.

## Boundaries and scale limits

Single small model, single local client, synthetic prompts, max_model_len=1536, no provider endpoint, no 7B+ model, no concurrency stress, no eviction-pressure study, and no realistic production trace.

## Claim scope

On a local GB10 vLLM 0.22 OpenAI-compatible server running facebook/opt-125m with 850-word synthetic anchors, exact shared prefixes reduced streaming TTFT by about 28% versus perturbed prefixes when prefix caching was enabled; disabling prefix caching removed the exact-prefix advantage.

## Why it stopped

The Tier 2 local vLLM mechanism is supported, but the evidence is too narrow for publication-grade or provider-wide claims.

## Recommended next action

Run a bounded deepen follow-up on a 1B-7B class model with realistic multi-client traces, concurrency levels, and eviction pressure before considering any paper or provider-wide claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Larger-model concurrent vLLM exact-prefix cache latency under realistic traces
- Success threshold: Across repeated runs, enabled exact-prefix median TTFT is at least 15% lower than both enabled perturbed-prefix and disabled exact-prefix baselines, with nonzero local prefix-cache hit counters and no comparable advantage in the disabled baseline.
- Stop condition: Stop if larger-model vLLM cannot run locally after ordinary install/configuration retries, or if enabled exact-prefix TTFT improvement is below 10% in two fixed-seed repetitions while prefix-cache hit counters remain low or absent.

## Evidence references

- Artifact root: `<local-path>/projects/medium-provider-vllm-confirmation-of-exact-anchor-prefix-c-ec18ea1e23`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
