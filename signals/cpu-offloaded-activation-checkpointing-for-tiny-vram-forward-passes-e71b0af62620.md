# CPU-Offloaded Activation Checkpointing for Tiny-VRAM Forward Passes

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-offloaded-activation-checkpointing-for-tiny-vram-forward-passes-e71b0af62620`
Run ID: `cpu-offloaded-activation-checkpointing-for-tiny-vram-forward-passes-e71b0af62620-20260621T105652607762+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/eacd2fdc9cc6

## What looked useful

CPU offload reduced the minimum tested viable logical device budget from 160 MiB for baseline retention to 24 MiB, with 70 spills and 70 reloads and 0.295 s median runtime at 24 MiB; recompute also fit at 24 MiB but took 0.528 s median with 600 recomputed layer steps.

## Boundaries and scale limits

No real GPU, CUDA allocator, PCIe/NVLink/UMA transfer, overlap, PyTorch activation hooks, transformer architecture, or production inference workload was tested.

## Claim scope

In a CPU-local synthetic forward graph with long-lived 2 MiB activations and logical tiny-device memory accounting, CPU spill/reload completed at a 24 MiB logical device budget where retain-on-device baseline failed through 96 MiB.

## Why it stopped

Proxy evidence is useful but not direct enough for paper writing; the current run closes as no-paper useful signal rather than full validation.

## Recommended next action

Run a bounded direct PyTorch/CUDA validation on a small GPU or capped-memory GPU using a transformer-like forward workload, measuring peak allocated VRAM, transfer bytes, wall time, and output correctness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CUDA validation of CPU-offloaded forward activations under capped VRAM
- Success threshold: At a capped budget where retain-on-device fails, CPU offload completes the transformer-like forward pass with matching outputs and at least 20% lower median latency than recompute over three repeats.
- Stop condition: Stop if CPU offload cannot run below the baseline viable VRAM budget, produces mismatched outputs, or is slower than recompute by more than 20% at every capped budget tested.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-activation-checkpointing-for-tiny-vram-forward-passes-e71b0af62620`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
