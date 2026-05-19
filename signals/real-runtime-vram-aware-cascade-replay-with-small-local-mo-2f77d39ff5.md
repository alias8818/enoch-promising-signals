# Real-runtime VRAM-aware cascade replay with small local models

Status: `useful_signal`
Project ID: `real-runtime-vram-aware-cascade-replay-with-small-local-mo-2f77d39ff5`
Run ID: `real-runtime-vram-aware-cascade-replay-with-small-local-mo-2f77d39ff5-20260519T191108433551+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Parent run decision: Dynamic VRAM Router for Model Cascades: enoch://control-plane/projects/dynamic-vram-router-for-model-cascades-1ce88212c855/runs/dynamic-vram-router-for-model-cascades-1ce88212c855-20260519T190616995559+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b5bc4b826607

## What looked useful

Static replay calibrated for 6,144 MiB headroom used batch 81 and required 5,184 MiB scratch. After a 3,072 MiB resident CUDA allocation reduced measured headroom to 3,020 MiB, static replay failed admission; adaptive replay recomputed batch 40 from live headroom, completed in 2 batches, and matched the successful cascade accuracy of 0.929688.

## Boundaries and scale limits

Tier 1 controlled small direct test only: synthetic CUDA classifiers, modeled replay scratch rather than real transformer KV cache, controlled reserved-headroom window, single machine, short runs, no production LLM serving stack or language-task quality metrics.

## Claim scope

On a GB10 CUDA runtime with unified-memory telemetry, a small synthetic two-stage local-model cascade using live cudaMemGetInfo headroom reduced replay batch size under resident memory pressure and completed replay where a pre-calibrated static batch failed admission, while preserving the same synthetic cascade accuracy.

## Why it stopped

No-paper closure: this is useful Tier 1 mechanism evidence, but it is synthetic and not sufficient for publication-grade claims about real LLM cascade serving.

## Recommended next action

Run a bounded direct follow-up with a real small local transformer or llama.cpp/GGUF cascade, applying the same live-memory admission controller to real prompt replay/KV-cache memory under repeatable pressure.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-memory replay admission for real small local transformer cascades
- Success threshold: Under pressure levels where static replay has at least one OOM/admission failure, adaptive replay completes at least 95% of replay requests without quality degradation beyond 1% relative and with no more than 25% p95 latency overhead.
- Stop condition: Stop if real-model adaptive replay still fails admission/OOM at the same pressure points as static replay, or if it avoids failures only by causing more than 1% quality loss or more than 25% p95 latency overhead.

## Evidence references

- Artifact root: `<local-path>/projects/real-runtime-vram-aware-cascade-replay-with-small-local-mo-2f77d39ff5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
