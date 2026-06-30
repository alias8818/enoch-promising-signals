# CPU-Offloaded 8-bit Sparse Optimizer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-offloaded-8-bit-sparse-optimizer-dd723904bc70`
Run ID: `cpu-offloaded-8-bit-sparse-optimizer-dd723904bc70-20260601T103110945164+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1969124219c8

## What looked useful

8-bit blockwise moment state reduced parameter-plus-state memory to 0.503x dense FP32. Step-time viability depended on quantization-block locality: random 1% sparsity touched 92.5% of blocks and was 25.6x slower than dense FP32, while clustered 0.1% and 1% sparsity were 15.0x and 2.6x faster than dense, respectively.

## Boundaries and scale limits

No real model training, no GPU-to-CPU transfer/overlap measurement, no production C++/SIMD kernel, and sparse inactive-coordinate Adam semantics are simplified. Absolute sparse-8-bit latency includes Python per-block loop overhead.

## Claim scope

CPU-only synthetic benchmark of blockwise 8-bit Adam-style optimizer state for sparse gradients over 8,000,000 parameters; compares random unstructured sparsity against perfectly block-clustered sparsity.

## Why it stopped

Proxy evidence shows memory savings but rejects general step-time viability for random unstructured sparsity because blockwise quantization makes sparse updates touch most blocks at 1% density; this is not a full end-to-end training validation.

## Recommended next action

Stop this run as a proxy early falsification of the broad claim; a bounded follow-up should use real sparse-gradient traces and an optimized CPU blockwise 8-bit kernel to test whether block locality persists outside synthetic clustered cases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-driven block-locality test for CPU-offloaded 8-bit sparse optimizer
- Success threshold: For a real workload at <=1% gradient density, median touched-block fraction is <=10%, optimized sparse 8-bit CPU step is at least 1.5x faster than dense FP32 CPU step, memory is <=0.55x dense state, and validation loss remains within 1% of baseline after a bounded run.
- Stop condition: Stop if real traces touch more than 50% of quantization blocks at <=1% density or if the optimized kernel remains slower than dense FP32 by more than 20% after basic vectorization.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-8-bit-sparse-optimizer-dd723904bc70`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
