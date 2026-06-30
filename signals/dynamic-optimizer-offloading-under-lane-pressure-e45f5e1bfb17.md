# Dynamic Optimizer Offloading Under Lane Pressure

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `dynamic-optimizer-offloading-under-lane-pressure-e45f5e1bfb17`
Run ID: `dynamic-optimizer-offloading-under-lane-pressure-e45f5e1bfb17-20260531T110703551386+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/95f52623c2d6

## What looked useful

Tight-budget dynamic placement retained 3-10 of 16 optimizer-state shards on CUDA, used 0.775 GiB peak CUDA allocation versus 0.954 GiB for all-GPU state, and ran at 15.178 ms mean step versus 29.866 ms for always-offloaded CPU state and 7.916 ms for all-GPU state. This supports a bounded memory-throughput tradeoff mechanism but is not paper-ready.

## Boundaries and scale limits

Synthetic tensor updates only; no real transformer backward pass, scheduler, multi-lane production contention, datacenter-scale model, or convergence measurement. Lane pressure was an artificial budget, not live external jobs.

## Claim scope

On a GB10 CUDA/UMA synthetic Adam-state benchmark with 16 shards, dynamic hot-shard optimizer-state retention under an artificial lane budget occupied less peak CUDA memory than all-GPU state while remaining faster than always-offloaded CPU state.

## Why it stopped

Closed as no-paper useful signal because current evidence is a synthetic mechanism probe with artificial pressure, not direct full training validation.

## Recommended next action

Run a bounded real-training follow-up: integrate the dynamic placement policy into a small transformer/GPT-2-class training loop with concurrent lane memory pressure and compare throughput, peak CUDA allocation, and loss parity against static all-GPU and full-offload baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-training validation of dynamic Adam-state placement under concurrent lane pressure
- Success threshold: Dynamic placement achieves at least 15% lower peak CUDA allocation than all-GPU optimizer state, at least 1.5x throughput over full CPU offload, and final short-run loss within 1% of the all-GPU baseline.
- Stop condition: Stop if dynamic placement is slower than full CPU offload, fails to reduce peak CUDA allocation by 10%, or introduces loss divergence greater than 1% in the bounded training run.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-optimizer-offloading-under-lane-pressure-e45f5e1bfb17`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
