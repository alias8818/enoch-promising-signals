# Adaptive Batching for Home GPU Bounded Work

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-batching-for-home-gpu-bounded-work-de67dcd9057d`
Run ID: `adaptive-batching-for-home-gpu-bounded-work-de67dcd9057d-20260605T225109388204+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f9f83ddb00d4

## What looked useful

At 2200 offered rps, immediate dispatch saturated at 1544 rps with 100% SLA misses and p95 latency near 2.9 seconds. Fixed8/fixed16 served about 2185 rps with zero SLA misses and p95 under 4.8 ms. Adaptive served 2191 rps with zero SLA misses and p95 1.97 ms, but used 0.215 GPU ms/request versus fixed16 at 0.070.

## Boundaries and scale limits

Short 8-second measurement windows per condition; synthetic fixed-shape GPU workload only; no production LLM server, tokenizer, KV-cache, variable sequence lengths, streaming decode, multi-client interference, or long-duration robustness.

## Claim scope

On one GB10 host with synthetic Poisson arrivals and a real CUDA matmul/GELU proxy workload, batching prevents immediate-dispatch queue collapse under overload; adaptive batching preserves lower tail latency than fixed batching but is less GPU-efficient.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic CUDA proxy that supports the scheduling mechanism but does not directly validate production LLM serving.

## Recommended next action

Run a bounded real-model serving benchmark on GB10 with a small local LLM and realistic prompt/output length distributions before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive batching on real small-LLM serving workloads
- Success threshold: Adaptive batching achieves within 5% of the best fixed policy throughput while reducing p95 latency by at least 25% versus fixed batching and avoiding SLA misses at the highest sustainable load.
- Stop condition: Stop if adaptive batching either misses the SLA in any load regime where fixed batching succeeds or loses more than 10% throughput versus the best fixed policy without at least a 25% p95 latency gain.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-batching-for-home-gpu-bounded-work-de67dcd9057d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
