# CPU gradient checkpointing for tiny-VRAM training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-gradient-checkpointing-for-tiny-vram-training-a3e90f548f8e`
Run ID: `cpu-gradient-checkpointing-for-tiny-vram-training-a3e90f548f8e-20260605T054321023351+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7718771a5fd1

## What looked useful

The mechanism is plausible and tunable: CPU-offloaded checkpoint boundaries lowered estimated device activation peaks to 19.4-58.3% of save-all across segment sizes 2-16 while preserving identical loss in a real forward/backward proxy. This is useful for designing a direct small-VRAM experiment but not paper-ready.

## Boundaries and scale limits

No CUDA/GB10/PyTorch direct measurement was available. Results do not measure actual tiny-VRAM OOM thresholds, device allocator peaks, PCIe/NVLink/UMA transfer overhead, optimizer state memory, transformer attention activations, or GPT-2-small-class training behavior.

## Claim scope

CPU-only NumPy proxy for a 32-layer MLP shows that offloading checkpoint boundary activations can reduce estimated device activation peak from 18.0 MiB save-all to 4.5 MiB at segment 4, with matching backward losses and about 1.16x mean wall time in the main run.

## Why it stopped

Closed as no-paper useful signal because this CPU worker can only provide proxy memory accounting and CPU runtime, not direct tiny-VRAM accelerator evidence.

## Recommended next action

Run a bounded direct PyTorch/JAX implementation on a real tiny-VRAM CUDA or UMA device and compare save-all, standard checkpointing, and CPU-offloaded boundary checkpointing using max allocated memory, OOM threshold, step time, and transfer counters.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct tiny-VRAM CUDA validation of CPU-offloaded checkpoint boundaries
- Success threshold: CPU-offloaded checkpointing must reduce actual max device memory by at least 40% versus standard checkpointing or permit at least one larger batch/sequence setting that standard checkpointing OOMs, while keeping median step-time overhead at or below 1.5x.
- Stop condition: Stop if CPU-offloaded checkpointing fails to improve actual OOM threshold or max allocated memory versus standard checkpointing, or if step-time overhead exceeds 2x in the smallest viable direct run.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-gradient-checkpointing-for-tiny-vram-training-a3e90f548f8e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
