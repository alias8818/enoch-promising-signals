# CPU-Offloaded Dynamic Sparse 8-bit Optimizer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-offloaded-dynamic-sparse-8-bit-optimizer-f3035350a459`
Run ID: `cpu-offloaded-dynamic-sparse-8-bit-optimizer-f3035350a459-20260522T093044403740+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/97c0e59c9136

## What looked useful

Int8 moment storage reduced optimizer-state memory to about 25% of dense FP32 Adam and dynamic sparsity reduced estimated offload traffic to 1.5-30% of dense traffic, but naive linear int8 second-moment quantization caused large parameter error and dynamic sparse updates were faster than dense vectorized Adam only at 1% density.

## Boundaries and scale limits

No GPU offload, no PCIe/NVLink measurement, no real model training, no convergence or validation-loss evidence, and no LLM-scale workload. Offload traffic is estimated from bytes per active update.

## Claim scope

Synthetic CPU-only microbenchmark of dense FP32 Adam, blockwise linear int8 Adam state, and dynamic top-k sparse int8 Adam on 1M-parameter generated gradient traces for 10 steps.

## Why it stopped

Early proxy falsification: the scoped synthetic optimizer test showed unacceptable relative L2 parameter error of 0.57-0.70 for dynamic sparse int8 Adam after only 10 steps, despite memory and estimated traffic savings.

## Recommended next action

Stop this implementation path as no-paper evidence; the next bounded test should replace linear int8 second-moment storage with a stability-focused representation before any model-scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stabilized sparse 8-bit Adam state with real small-model convergence check
- Success threshold: Relative update/parameter error below 0.05 on synthetic traces and validation loss within 2% of dense Adam while preserving at least 2x optimizer-state memory reduction.
- Stop condition: Stop if stabilized state still exceeds 0.1 relative error on synthetic traces or if sparse update overhead remains slower than dense Adam above 1% active density.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-dynamic-sparse-8-bit-optimizer-f3035350a459`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
