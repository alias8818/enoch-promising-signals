# CPU-Offloaded Factored Optimizer for Tiny-VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-offloaded-factored-optimizer-for-tiny-vram-6d210eddf93c`
Run ID: `cpu-offloaded-factored-optimizer-for-tiny-vram-6d210eddf93c-20260527T090413278378+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/40fceb570eb0

## What looked useful

Factored offloaded optimizer state has the expected O(n+m) memory advantage and did not introduce a CPU update-time penalty in a 13.34 second local proxy benchmark. A toy quadratic check showed the factored update reduced loss from 0.500155 to 0.047683 over 200 steps, so the measured code path is not just static memory accounting.

## Boundaries and scale limits

No GPU was available in this deployment. The run did not test end-to-end tiny-VRAM training, PCIe/NVLink transfer overlap, transformer loss curves, mixed precision, or production framework integration.

## Claim scope

Bounded CPU proxy evidence: for large 2D float32 tensors, an Adafactor-style factored CPU-offloaded optimizer state reduces optimizer-state memory by 1024x to 5461x versus full Adam state, avoids 8 MiB to 256 MiB of GPU-resident Adam state for the tested tensors, and has comparable NumPy CPU update time on this host.

## Why it stopped

Closed as no-paper useful signal because the evidence is a CPU proxy plus synthetic convergence sanity check, not a full direct validation of tiny-VRAM GPU training.

## Recommended next action

Run a bounded direct tiny-VRAM GPU follow-up: train a small transformer with the offloaded factored optimizer and compare memory, throughput, transfer traces, and validation loss against AdamW.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-VRAM GPU Training Validation for CPU-Offloaded Factored Optimizer
- Success threshold: Compared with AdamW under a fixed tiny-VRAM budget, the factored offload run should fit without out-of-memory, reach within 5% of baseline validation loss at the same token budget, and incur no more than 25% wall-clock slowdown while reducing peak GPU optimizer-state memory by at least 80%.
- Stop condition: Stop if the implementation cannot fit a transformer that AdamW cannot fit, if transfer stalls cause more than 50% wall-clock slowdown after basic overlap/batching fixes, or if validation loss remains more than 10% worse than baseline across two learning-rate settings.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-factored-optimizer-for-tiny-vram-6d210eddf93c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
