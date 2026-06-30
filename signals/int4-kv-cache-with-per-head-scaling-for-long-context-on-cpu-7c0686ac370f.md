# Int4 KV-Cache with Per-Head Scaling for Long Context on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int4-kv-cache-with-per-head-scaling-for-long-context-on-cpu-7c0686ac370f`
Run ID: `int4-kv-cache-with-per-head-scaling-for-long-context-on-cpu-7c0686ac370f-20260604T075404784733+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0efddd0f401e

## What looked useful

Bandwidth reduction is useful for long-context CPU decode, but per-head-only int4 scaling is too coarse in this probe; future work should test finer scale granularity and real model traces before claiming viability.

## Boundaries and scale limits

CPU-only synthetic benchmark on an 8-online-vCPU Intel Xeon Silver 4114 VM; no real model KV traces, no perplexity/logit metrics, no fp16/bf16 baseline, no production SIMD int4 kernel, no batching or full inference-stack validation.

## Claim scope

On synthetic Gaussian KV tensors, packed signed int4 KV cache with one scale per head reduces CPU KV storage by about 8x and can speed one-token long-context float32 attention decode at 32k context, but incurs about 20-22% relative L2 attention-output error.

## Why it stopped

Synthetic bounded evidence is mixed: memory and long-context latency improve, but quantization error is high and direct model-quality evidence is absent.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should compare per-head, per-block, and per-token int4 scaling on real transformer KV traces with logit or perplexity drift thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Granularity sweep for int4 KV cache scaling on real transformer traces
- Success threshold: At 8k-32k context on a small open model, achieve at least 4x KV memory reduction, at least parity decode latency versus fp16 or bf16 KV, and less than 1% relative perplexity degradation or a predeclared small logit-drift bound.
- Stop condition: Stop if all int4 granularities with at least 4x memory reduction exceed the quality drift threshold or are slower than the fp16/bf16 baseline at 32k context.

## Evidence references

- Artifact root: `<local-path>/projects/int4-kv-cache-with-per-head-scaling-for-long-context-on-cpu-7c0686ac370f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
