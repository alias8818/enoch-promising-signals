# Quantization and thread-affinity sweep for TinyLlama CPU inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantization-and-thread-affinity-sweep-for-tinyllama-cpu-i-010370e1ab`
Run ID: `quantization-and-thread-affinity-sweep-for-tinyllama-cpu-i-010370e1ab-20260609T130052660289+0000`

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

- Parent run decision: Bounded CPU Inference Benchmark for Quantized Small Models: enoch://control-plane/projects/bounded-cpu-inference-benchmark-for-quantized-small-models-145382f5d226/runs/bounded-cpu-inference-benchmark-for-quantized-small-models-145382f5d226-20260609T055413792099+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/25069159f620

## What looked useful

A direct llama.cpp TinyLlama sweep found meaningful thread/affinity sensitivity and mixed quantization behavior: initial bests shifted under five-repetition confirmation, showing that noisy 8-thread generation can mislead and that stable 4-thread settings deserve priority in follow-up CPU inference sweeps.

## Boundaries and scale limits

Single CPU worker, 8 online CPUs, one TinyLlama GGUF source, two quantizations, short prompt/generation sizes, small repetition counts, no power counters, no latency percentiles, no broader CPU or workload robustness.

## Claim scope

On this CPU worker, TinyLlama GGUF CPU inference throughput is materially affected by thread count and Linux CPU affinity; 4-thread generation was more stable than 8-thread generation in confirmation, and Q4_K_M was not a universal throughput winner over Q8_0.

## Why it stopped

Tier 1 direct validation completed and produced useful but mixed local evidence; publication-grade closure would require broader, quieter, instrumented CPU benchmarking rather than more short runs here.

## Recommended next action

Stop this run as no-paper useful signal; next run should repeat the harness on a quieter CPU host with more repetitions, median/p95 latency, memory bandwidth counters, and Q4_K_M/Q5_K_M/Q8_0 over a longer generation workload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stability-instrumented TinyLlama CPU affinity and quantization benchmark
- Success threshold: A single quantization/thread/affinity configuration remains within 5% of best median generation throughput across three independent runs while not degrading prompt-processing throughput by more than 10% versus the prompt-processing best.
- Stop condition: Stop if top configurations change rank by more than 10% across independent runs or if added telemetry shows the effect is host-noise dominated rather than affinity/quantization driven.

## Evidence references

- Artifact root: `<local-path>/projects/quantization-and-thread-affinity-sweep-for-tinyllama-cpu-i-010370e1ab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
