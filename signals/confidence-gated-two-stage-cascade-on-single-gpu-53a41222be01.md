# Confidence-Gated Two-Stage Cascade on Single GPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-gated-two-stage-cascade-on-single-gpu-53a41222be01`
Run ID: `confidence-gated-two-stage-cascade-on-single-gpu-53a41222be01-20260610T112431864097+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/dc32965b9de5

## What looked useful

At batch 1024, cascade t=0.45 reached 0.8664 accuracy versus 0.8555 for always-large while reducing expected MFLOPs/sample from 0.8571 to 0.2862, but latency worsened from 0.1444 to 0.1777 us/sample. At batch 64, cascade t=0.65 reached 0.8557 accuracy versus 0.8333 for always-large and reduced expected MFLOPs/sample to 0.3134, but latency worsened from 0.7922 to 8.2128 us/sample.

## Boundaries and scale limits

Evidence is limited to synthetic data, small MLP classifiers, PyTorch eager execution, batch sizes 64 and 1024, and p50-style throughput timing. It does not cover fused kernels, CUDA graphs, production serving runtimes, transformer workloads, real datasets, or tail latency.

## Claim scope

On a structured synthetic classification benchmark run on one NVIDIA GB10 with an unfused PyTorch confidence-gated cascade, threshold routing reduced expected linear-layer compute and sometimes improved accuracy, but did not reduce measured inference latency versus always running the larger model.

## Why it stopped

Local evidence supports expected-compute savings but early-falsifies the practical naive single-GPU latency claim for this unfused PyTorch implementation and model scale; this is not full validation on real workloads.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should implement fused or static-bucketed routing and require measured latency below always-large at matched or better accuracy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused or Static-Bucketed Single-GPU Cascade Latency Test
- Success threshold: At a threshold with accuracy at least equal to always-large, measured p50 latency must be at least 10% lower than always-large for one nontrivial batch setting without increasing p95 latency.
- Stop condition: Stop as negative if fused/static-bucketed routing remains slower than always-large at matched accuracy across the tested batch settings.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-two-stage-cascade-on-single-gpu-53a41222be01`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
