# Adam state offload via gb10 unified CPU-GPU memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adam-state-offload-via-gb10-unified-cpu-gpu-memory-f2bbc782795e`
Run ID: `adam-state-offload-via-gb10-unified-cpu-gpu-memory-f2bbc782795e-20260628T095235537044+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5be180975655

## What looked useful

GB10 UMA supports the optimizer-state placement mechanism, but naive CPU-side Adam state offload is a capacity tradeoff rather than a throughput win: it saved 0.954 GiB CUDA allocator peak at 128M FP32 parameters while increasing step time from 45.1 ms to 132.2 ms.

## Boundaries and scale limits

Synthetic optimizer-step benchmark only; no full model convergence, mixed precision training, ZeRO/FSDP integration, fused/chunked overlap, multi-GPU, or datacenter-scale validation.

## Claim scope

On a single GB10 host with PyTorch 2.12.0+cu130, a direct synthetic FP32 Adam benchmark showed that moving Adam first/second moments to CPU tensors saves CUDA allocator memory approximately equal to the offloaded state size, but the naive CPU-offload path is 2.3x-2.9x slower than GPU-resident Adam at 16M-128M parameters.

## Why it stopped

Proxy/direct optimizer-step evidence supports memory savings but early-falsifies the naive practicality claim; this is not a full training validation.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded test should implement chunked/overlapped pinned CPU Adam offload and require slowdown below 1.25x on a GPT-2-small-class local training loop before considering larger validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Chunked overlapped Adam state offload on GB10 UMA
- Success threshold: At least 35% CUDA allocator peak reduction from offloaded Adam state with no more than 1.25x step-time slowdown versus GPU Adam, stable MemAvailable, and matched short-run loss behavior.
- Stop condition: Stop if chunked/overlapped offload remains above 1.5x slowdown at GPT-2-small-class scale or causes unsafe MemAvailable/earlyoom pressure.

## Evidence references

- Artifact root: `<local-path>/projects/adam-state-offload-via-gb10-unified-cpu-gpu-memory-f2bbc782795e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
