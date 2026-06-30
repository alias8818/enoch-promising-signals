# CPU-Offloaded Paged Optimizer for Tiny-VRAM Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-offloaded-paged-optimizer-for-tiny-vram-training-1c6ae160326c`
Run ID: `cpu-offloaded-paged-optimizer-for-tiny-vram-training-1c6ae160326c-20260527T050103281744+0000`

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

Paged CPU optimizer state is mechanically useful when updates touch a small fraction of pages, but dense full-model training gets only GPU memory offload, not paged transfer reduction. Page size trades CPU throughput against sparse-touch amplification.

## Boundaries and scale limits

No CUDA/PyTorch training, no constrained-VRAM GPU, no real model convergence, no PCIe/NVLink transfer, and no asynchronous prefetch/overlap were tested. Results are not publication-grade evidence for tiny-VRAM full fine-tuning.

## Claim scope

CPU-only mechanism probe of page-granular Adam state updates over 16,777,216 float32 parameters. Paging reduced touched optimizer-state traffic only for sparse page-touch regimes; dense updates touched all pages and had no transfer-byte reduction.

## Why it stopped

Proxy mechanism evidence is useful but insufficient for a paper; dense tiny-VRAM benefit was early-falsified at the page-traffic level, while sparse regimes remain promising.

## Recommended next action

Run a bounded CUDA/PyTorch constrained-VRAM test comparing standard CPU-offloaded Adam against paged CPU-offloaded Adam on dense full fine-tuning and adapter/sparse-update regimes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Constrained-VRAM GPU validation of paged CPU-offloaded Adam
- Success threshold: For sparse or adapter regimes, at least 20% lower wall-clock step time or feasible training under a VRAM cap where the baseline fails, with no worse loss trend over a bounded run; for dense full fine-tuning, evidence of full-state transfer overlap sufficient to avoid slowdown versus standard CPU offload.
- Stop condition: Stop if dense and sparse workloads are both slower than standard CPU offload by more than 10% with no lower peak GPU memory, or if page movement cannot be overlapped enough to make sparse updates faster.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-paged-optimizer-for-tiny-vram-training-1c6ae160326c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
