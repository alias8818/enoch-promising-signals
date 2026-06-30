# 8-bit Adam optimizer states for CPU-bound tiny-VRAM training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-adam-optimizer-states-for-cpu-bound-tiny-vram-training-0f01afb87578`
Run ID: `8-bit-adam-optimizer-states-for-cpu-bound-tiny-vram-training-0f01afb87578-20260607T165109123266+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/aa1218c962cc

## What looked useful

The optimizer-state memory mechanism is supported, but CPU quantize/dequantize overhead is material. The idea is practical only if memory pressure is the binding constraint or if realistic training hides the optimizer-step overhead behind other work.

## Boundaries and scale limits

No GPU, tiny-VRAM offload path, PyTorch/bitsandbytes implementation, transformer workload, or long training run was tested. RSS was not a clean optimizer-state metric; explicit state byte accounting was used.

## Claim scope

In a local NumPy CPU proxy, blockwise 8-bit Adam moment states reduce explicit optimizer-state memory to about 25.0% of fp32 Adam state memory at 262k to 4.19M parameters, while raw optimizer updates are about 1.8-2.3x slower and a small synthetic regression probe reaches similar but slightly worse final loss.

## Why it stopped

Bounded CPU proxy supports the memory mechanism but not a paper-ready tiny-VRAM training claim; direct model-training evidence is missing and raw CPU optimizer updates were materially slower.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should integrate a PyTorch-compatible 8-bit CPU Adam state path into a small transformer or LoRA finetune and measure fit/no-fit, wall-clock, and validation loss under a fixed memory cap.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PyTorch small-transformer tiny-memory 8-bit CPU Adam state test
- Success threshold: 8-bit CPU Adam states must reduce optimizer-state memory by at least 3.5x, avoid OOM or increase max feasible batch/model size under the cap, keep end-to-end wall-clock overhead below 35%, and keep validation loss within 3% of fp32 after a bounded run.
- Stop condition: Stop if integration overhead makes end-to-end training more than 50% slower without enabling a larger feasible workload, or if validation loss is more than 10% worse than fp32 across two seeds.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adam-optimizer-states-for-cpu-bound-tiny-vram-training-0f01afb87578`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
