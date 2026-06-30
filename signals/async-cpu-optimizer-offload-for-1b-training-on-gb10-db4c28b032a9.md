# Async CPU-Optimizer Offload for 1B Training on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `async-cpu-optimizer-offload-for-1b-training-on-gb10-db4c28b032a9`
Run ID: `async-cpu-optimizer-offload-for-1b-training-on-gb10-db4c28b032a9-20260611T070331811163+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f3e4b47678f8

## What looked useful

1B FP32 CPU AdamW took 0.803 s versus 0.343 s for CUDA AdamW; warmed BF16 round-trip transfer for 1B elements took 0.067 s; CPU-offloaded optimizer state reduces CUDA-resident 1B optimizer memory from about 16 GB to about 4 GB excluding activations but keeps about 12 GB in CPU/UMA memory.

## Boundaries and scale limits

This run did not train a 1B Transformer end to end. It directly measured 1B flattened optimizer vectors, tensor copies, and BF16 matmul throughput; activation memory, real model scheduling, gradient accumulation, and convergence under delayed async updates remain untested.

## Claim scope

On GB10, warmed 1B-vector measurements show CPU AdamW optimizer offload saves CUDA-resident optimizer memory but leaves about 0.80 seconds of CPU optimizer work per 1B update on the critical path unless stale-update semantics are accepted.

## Why it stopped

Early mechanism falsification for the async hiding claim: direct 1B-vector optimizer evidence shows CPU AdamW is slower than the CUDA optimizer baseline and would be exposed unless a real training loop proves overlap without stale weights.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next bounded test should be an end-to-end 1B-class GB10 training step comparison of GPU-resident AdamW versus CPU-offloaded AdamW at identical token/batch settings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end GB10 1B training-step comparison for CPU optimizer offload
- Success threshold: CPU-offloaded AdamW must enable a larger feasible token batch or sequence length and deliver at least 90% of the GPU-resident AdamW tokens/sec at the same model scale, or show a memory-feasible configuration that GPU-resident AdamW cannot run.
- Stop condition: Stop if CPU-offloaded AdamW remains more than 10% slower end to end at the largest configuration both methods can run, or if it only wins by using stale/delayed update semantics without an explicit convergence validation.

## Evidence references

- Artifact root: `<local-path>/projects/async-cpu-optimizer-offload-for-1b-training-on-gb10-db4c28b032a9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
