# Bounded KV-Cache Pressure for Memory-Constrained GPU Workers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-kv-cache-pressure-for-memory-constrained-gpu-workers-fb2cbe81ca54`
Run ID: `bounded-kv-cache-pressure-for-memory-constrained-gpu-workers-fb2cbe81ca54-20260610T184427769184+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f040bdbdf971

## What looked useful

Fixed-window KV residency produced a direct, reproducible memory-pressure reduction on the target CUDA path: 4.0 GiB resident cache at a 4096-token window versus 64.0 GiB unbounded at 65,536 logical tokens, with one-layer decode median latency at 32,768 logical tokens dropping from 2.372 ms unbounded to 0.292 ms bounded.

## Boundaries and scale limits

Synthetic cache and one-layer attention probes only; no real LLM quality evaluation, no end-to-end serving benchmark, no concurrent request scheduler, no paged-attention fragmentation test, and no deliberate near-OOM run on the swapless UMA host.

## Claim scope

On a GB10 CUDA worker using a synthetic Llama-like BF16 KV-cache shape of 64 layers, 32 KV heads, and head dimension 128, a 4096-token bounded resident KV window caps cache memory at 4.0 GiB while unbounded full-history KV grows linearly at 1.0 MiB/token; the tested largest logical context of 65,536 tokens avoided 60.0 GiB of resident KV cache, and decode-like single-layer attention latency flattened at the window size.

## Why it stopped

This run produced direct synthetic memory/latency mechanism evidence but not end-to-end model-serving or quality evidence, so it is useful no-paper signal rather than publication-grade validation.

## Recommended next action

Run a bounded real-model serving follow-up with fixed-window KV versus full-history or paged KV, measuring throughput, memory residency, and task quality at 8k-64k logical contexts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model fixed-window KV serving under GB10 memory pressure
- Success threshold: At 32k or higher logical context, fixed-window KV uses at least 50% less resident KV memory and improves or maintains p95 decode latency while losing no more than 5% absolute on the selected task-quality metric.
- Stop condition: Stop if quality degradation exceeds 10% absolute at the smallest tested long-context setting or if real serving overhead removes the measured memory advantage.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-kv-cache-pressure-for-memory-constrained-gpu-workers-fb2cbe81ca54`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
