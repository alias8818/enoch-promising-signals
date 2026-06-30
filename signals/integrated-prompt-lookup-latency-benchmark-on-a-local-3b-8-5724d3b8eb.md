# Integrated prompt-lookup latency benchmark on a local 3B-8B serving model

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `integrated-prompt-lookup-latency-benchmark-on-a-local-3b-8-5724d3b8eb`
Run ID: `integrated-prompt-lookup-latency-benchmark-on-a-local-3b-8-5724d3b8eb-20260523T072915198369+0000`

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

- Parent run decision: N-Gram/Prompt-Lookup Speculative Decoding for Home Inference: enoch://control-plane/projects/n-gram-prompt-lookup-speculative-decoding-for-home-inference-dd02225429a6/runs/n-gram-prompt-lookup-speculative-decoding-for-home-inference-dd02225429a6-20260523T052814500746+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e926d567412a

## What looked useful

Repeated prompt/output case: median baseline 44.04 tok/s vs lookup 373.949 tok/s, 8.491x speedup, 100.000% draft acceptance. Control case: median baseline 44.85 tok/s vs lookup 47.117 tok/s, 1.051x speedup, 5.365% acceptance. Mechanism is supported but workload-sensitive.

## Boundaries and scale limits

Single GB10 host, one 7B Q4_K_M model, llama.cpp lookup implementation, greedy decoding, two handcrafted prompt families, three repetitions each, no concurrent serving endpoint p50/p95/p99 measurement, and no broad workload or quality study.

## Claim scope

On one local CUDA-offloaded Qwen2.5-7B-Instruct GGUF model, llama.cpp prompt-lookup decoding produced a large decode-throughput gain on a handcrafted repetitive prompt/output continuation and little gain on a low-overlap control continuation.

## Why it stopped

Tier-1 direct evidence supports the mechanism, but the evidence is too narrow and handcrafted for a paper; finalize as no-paper useful signal.

## Recommended next action

Run a bounded serving-endpoint follow-up on 2-3 local 3B-8B models with natural repeated-context workloads, p50/p95/p99 latency, quality checks, and concurrency 1/4 before considering paper development.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Serving endpoint prompt-lookup latency distribution on natural repeated-context workloads
- Success threshold: Median p50 and p95 decode-latency improvement >=25% on repeated-context workloads with no quality regression and no positive claim on controls below 15% improvement.
- Stop condition: Stop if repeated-context p95 improvement is below 15% on two models or if quality/output validation fails for accepted lookup generations.

## Evidence references

- Artifact root: `<local-path>/projects/integrated-prompt-lookup-latency-benchmark-on-a-local-3b-8-5724d3b8eb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
