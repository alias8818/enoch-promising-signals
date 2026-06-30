# Sparse Gradient Compression for Low-VRAM CPU Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sparse-gradient-compression-for-low-vram-cpu-training-aa3944490c65`
Run ID: `sparse-gradient-compression-for-low-vram-cpu-training-aa3944490c65-20260605T214315365289+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/65dfebca2186

## What looked useful

Sparse gradient compression is not sufficient by itself for low-memory CPU training. Moderate 10% top-k Adam retained useful optimization signal, but dense Adam state dominated gradient memory and dense-gradient materialization prevented measured RSS savings.

## Boundaries and scale limits

Proxy-only small MLP evidence; no GPT-2-small-class model, real dataset, long run, production autograd streaming implementation, or sparse optimizer-state implementation was tested.

## Claim scope

On a synthetic CPU NumPy 2-layer MLP with 541,712 parameters and 120 training steps, top-k sparse gradients at 10% preserved most dense Adam loss improvement but sparse SGD and 1% sparsity degraded substantially; sparse gradients alone did not reduce measured peak RSS because dense gradients and dense Adam state remained resident.

## Why it stopped

Bounded proxy evidence is mixed and insufficient for a paper: top-k Adam at 10% was promising on a toy workload, but sparse gradients alone did not produce actual memory savings and dense optimizer state remained.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should implement layerwise streaming top-k plus sparse or row-local optimizer state on a small transformer and compare validation loss, throughput, and peak RSS against dense Adam.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layerwise sparse-gradient and sparse-state optimizer for small CPU transformer training
- Success threshold: Peak RSS at least 25% lower than dense Adam and validation loss no more than 10% worse after the bounded run, with throughput no more than 2x slower.
- Stop condition: Stop if sparse-state implementation cannot reduce measured peak RSS, if validation loss is more than 10% worse, or if CPU-only runtime would exceed the controller budget without checkpointable partial metrics.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-gradient-compression-for-low-vram-cpu-training-aa3944490c65`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
