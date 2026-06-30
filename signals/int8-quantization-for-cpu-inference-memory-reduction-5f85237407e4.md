# INT8 quantization for CPU inference memory reduction

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `83`
Project ID: `int8-quantization-for-cpu-inference-memory-reduction-5f85237407e4`
Run ID: `int8-quantization-for-cpu-inference-memory-reduction-5f85237407e4-20260607T142745645617+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/bf55314bb4ea

## What looked useful

INT8 weight quantization can materially reduce persistent CPU inference memory, but naive dequantize-per-layer execution may forfeit peak-memory gains and slow inference; deployments should validate peak RSS with the actual INT8 runtime rather than infer memory solely from stored weight size.

## Boundaries and scale limits

Single-process NumPy CPU benchmark, synthetic random weights/inputs, batch 8, one host, three measured iterations, no real model checkpoint, no task accuracy, no fused INT8 GEMM runtime. Peak inference RSS rose because layer weights were dequantized to FP32 temporaries.

## Claim scope

On a synthetic four-layer 4096-wide CPU MLP, symmetric per-output-channel INT8 weight storage reduced persistent model bytes and steady process RSS by about 75% relative to FP32; the claim is limited to resident model memory mechanics, not real-model accuracy or production fused-kernel performance.

## Why it stopped

Bounded synthetic evidence supports the memory mechanism but is insufficient and not novel enough for publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; validate the same memory, peak RSS, throughput, and accuracy metrics in a production CPU INT8 runtime before considering a stronger claim.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/int8-quantization-for-cpu-inference-memory-reduction-5f85237407e4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
