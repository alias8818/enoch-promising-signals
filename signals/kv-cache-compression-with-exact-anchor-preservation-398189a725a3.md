# KV-cache compression with exact anchor preservation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `kv-cache-compression-with-exact-anchor-preservation-398189a725a3`
Run ID: `kv-cache-compression-with-exact-anchor-preservation-398189a725a3-20260628T021602248606+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2a6832ec220d

## What looked useful

At 32x compression on anchor-retrieval traces, exact-anchor compression achieved 0.0824 mean anchor-target relative L2 error versus 0.9994 for the best baseline, with exact anchor copy error 0.0. The mostly non-anchor workload showed a tradeoff: unconditional anchor reservation can worsen total error when non-anchor tokens dominate queries.

## Boundaries and scale limits

No real transformer checkpoint, tokenizer, real prompt anchor detector, multi-layer decode, throughput, latency, or memory-bandwidth validation was run. The experiment assumes anchors are known and uses synthetic K/V traces with one attention computation.

## Claim scope

In a deterministic synthetic scaled-dot-product attention probe with known query-relevant anchors, exact anchor K/V preservation plus segment-mean compression substantially reduced anchor-target attention-output error versus same-budget segment-mean, uniform-keep, and random-keep baselines at 4x-32x compression.

## Why it stopped

Closed as no-paper useful signal: the synthetic proxy supports the mechanism but does not provide direct model-serving evidence, and it exposed a non-anchor workload tradeoff.

## Recommended next action

Run a bounded real-model follow-up on GPT-2-small-class or a small open LLM using real long-context anchor retrieval tasks, same-budget KV compression controls, anchor-selection ablations, and latency/memory metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model validation of exact anchor KV preservation under equal-budget compression
- Success threshold: At 8x or greater KV compression, exact-anchor preservation improves anchor-task accuracy or target logit preservation by at least 20% relative to the best same-budget compression baseline while keeping non-anchor control degradation within 5% absolute and showing measured KV memory reduction.
- Stop condition: Stop if exact-anchor preservation fails to beat the best same-budget baseline on anchor tasks, or if non-anchor degradation exceeds 5% absolute at the smallest compression ratio that gives meaningful memory savings.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-compression-with-exact-anchor-preservation-398189a725a3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
