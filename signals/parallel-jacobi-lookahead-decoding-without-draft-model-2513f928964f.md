# Parallel Jacobi Lookahead Decoding Without Draft Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `parallel-jacobi-lookahead-decoding-without-draft-model-2513f928964f`
Run ID: `parallel-jacobi-lookahead-decoding-without-draft-model-2513f928964f-20260630T104834345111+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e3b49e3a046a

## What looked useful

Across 16 seeds and four synthetic corpus types, lookahead verification preserved exact greedy output and reduced sequential passes by about 0.63-0.84, but required about 28x-240x more token-position predictions in the proxy.

## Boundaries and scale limits

No real transformer serving kernel, KV-cache packing, CUDA attention path, sampling exactness test, or wall-clock GPU latency benchmark was run. The idea also overlaps directly with public ICML 2024 Lookahead Decoding work.

## Claim scope

A local deterministic variable-context simulator shows that cached Jacobi/lookahead n-gram proposals can preserve exact greedy output and reduce sequential verification passes, but only as an algorithmic proxy.

## Why it stopped

Proxy evidence supports the mechanism but not a publication-grade or novel claim; practical speedup remains unvalidated without a real transformer/GPU implementation.

## Recommended next action

Stop this run as no-paper useful signal; a meaningful next test would implement model-specific packed lookahead verification on a small real causal LM and report exactness, accepted tokens, GPU utilization, and wall-clock latency against greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small real-transformer packed lookahead decoding benchmark
- Success threshold: At least 1.2x median wall-clock speedup over greedy decoding with 100% greedy-output exactness and a reported utilization explanation for the speedup.
- Stop condition: Stop if packed implementation cannot preserve exact greedy output or if median wall-clock speedup is below 1.05x despite reduced sequential pass count.

## Evidence references

- Artifact root: `<local-path>/projects/parallel-jacobi-lookahead-decoding-without-draft-model-2513f928964f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
