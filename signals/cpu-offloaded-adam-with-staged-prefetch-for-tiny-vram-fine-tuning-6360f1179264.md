# CPU-Offloaded Adam with Staged Prefetch for Tiny-VRAM Fine-Tuning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-offloaded-adam-with-staged-prefetch-for-tiny-vram-fine-tuning-6360f1179264`
Run ID: `cpu-offloaded-adam-with-staged-prefetch-for-tiny-vram-fine-tuning-6360f1179264-20260528T084553466522+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b36e65c0bc48

## What looked useful

At 64M elements, pageable CPU offload reduced peak CUDA allocation from 980.38 MB for GPU Adam to 488.28 MB sequential and 503.54 MB staged, but staged remained 2.84x slower than GPU Adam. With pinned CPU state, staged remained 2.79x slower than GPU Adam and only 4% faster than sequential CPU offload.

## Boundaries and scale limits

No end-to-end transformer fine-tuning, no real constrained-VRAM OOM boundary, no backward/optimizer overlap, no convergence or model-quality measurement. Largest synthetic case was 64M fp32 elements with 5 measured optimizer steps.

## Claim scope

Bounded optimizer-step proxy on NVIDIA GB10: CPU-resident Adam state reduces PyTorch CUDA peak allocation for large synthetic fp32 parameter vectors, and staged shard GPU update can be faster than sequential CPU update, but both offload paths remain substantially slower than GPU-resident Adam.

## Why it stopped

Optimizer-step proxy supports the memory-saving mechanism but not a paper-ready staged-prefetch performance claim; direct full-training evidence would be required to overturn this no-paper decision.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement true overlap with backward on a small transformer fine-tune under an enforced CUDA memory cap.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end tiny-memory transformer fine-tune with overlapped CPU-offload Adam
- Success threshold: Under the enforced memory cap, staged/overlapped CPU-offload must be the fastest fitting offload method, keep peak CUDA allocation at least 35% below GPU Adam when GPU Adam fits, and achieve at least 50% of GPU Adam tokens/s or at least 1.25x sequential CPU-offload tokens/s.
- Stop condition: Stop if staged/overlapped CPU-offload is still more than 2x slower than GPU Adam when GPU Adam fits, fails to beat sequential CPU offload by 25%, or cannot produce a stable loss curve under the memory cap.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-adam-with-staged-prefetch-for-tiny-vram-fine-tuning-6360f1179264`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
