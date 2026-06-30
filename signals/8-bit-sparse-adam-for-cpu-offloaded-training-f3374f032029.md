# 8-bit Sparse Adam for CPU-Offloaded Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-sparse-adam-for-cpu-offloaded-training-f3374f032029`
Run ID: `8-bit-sparse-adam-for-cpu-offloaded-training-f3374f032029-20260525T045022377965+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/fbfbc972dd11

## What looked useful

Naive 8-bit sparse Adam second-moment quantization is unstable because positive variance can round to zero. A guarded uint8 second-moment encoding that floors positive bins to 1 preserved convergence in two sparse embedding regression proxies and achieved 3.765x optimizer-state compression in the large sparse update benchmark, with update time ranging from 0.955x to 1.266x FP32 depending on sparse batch size.

## Boundaries and scale limits

Proxy-only CPU tests; no PyTorch optimizer integration, no real GPU CPU-offload path, no transfer-overlap measurement, no distributed sharding, and no GPT-2-small-class or larger training validation.

## Claim scope

In NumPy CPU proxy tests for embedding-like sparse row updates, row-wise 8-bit Adam moment state with a positive-bin floor for the second moment matched FP32 sparse Adam convergence while reducing optimizer-state memory from 128 MiB to 34 MiB on a 262,144 x 64 benchmark. Naive second-moment quantization without the floor diverged.

## Why it stopped

Proxy mechanism evidence is useful but not sufficient for a paper or full CPU-offloaded training claim.

## Recommended next action

Run a bounded deepen follow-up implementing the guarded 8-bit sparse Adam state in a real PyTorch CPU-offload optimizer path and compare memory, throughput, and validation loss against FP32 sparse Adam on a small sparse language-model or recommender-style workload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PyTorch CPU-Offload Validation of Guarded 8-bit Sparse Adam
- Success threshold: At least 3x optimizer-state memory reduction, final validation loss within 1% of FP32 sparse Adam, no divergence, and optimizer-step throughput no worse than 20% below FP32 on the bounded workload.
- Stop condition: Stop if guarded 8-bit sparse Adam diverges, exceeds FP32 validation loss by more than 1% after matched training, or is more than 20% slower in optimizer-step throughput without a compensating memory-capacity benefit.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-sparse-adam-for-cpu-offloaded-training-f3374f032029`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
