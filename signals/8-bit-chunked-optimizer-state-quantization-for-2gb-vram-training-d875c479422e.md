# 8-bit chunked optimizer state quantization for <2GB VRAM training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-chunked-optimizer-state-quantization-for-2gb-vram-training-d875c479422e`
Run ID: `8-bit-chunked-optimizer-state-quantization-for-2gb-vram-training-d875c479422e-20260611T095821914217+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/49eaaab87def

## What looked useful

Chunked 8-bit optimizer states can be viable in a toy Adam training loop if affine/range-aware per-chunk quantization is used, but naive symmetric int8 chunking destabilized training despite similar memory compression.

## Boundaries and scale limits

No CUDA, GPU VRAM allocator, transformer model, activation memory, checkpointing, or real <2GB VRAM training run was tested. Results are limited to a synthetic CPU training loop and memory arithmetic.

## Claim scope

CPU NumPy toy softmax-regression proxy: affine per-chunk 8-bit Adam state storage preserved validation loss within 0.0044 absolute loss of fp32 Adam while reducing optimizer-state bytes from 8.0 to about 2.0-2.25 bytes per parameter; symmetric per-chunk int8 state storage failed badly.

## Why it stopped

Proxy evidence only: the CPU toy result supports the affine mechanism and falsifies naive symmetric chunking, but it is not a direct VRAM training validation.

## Recommended next action

Stop this worker run as no-paper useful signal; next bounded evidence should be a direct PyTorch/CUDA <2GB memory-cap experiment using affine chunked optimizer states.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct 2GB VRAM affine chunked Adam validation
- Success threshold: Validation loss within 1% of fp32 Adam after at least 1000 steps, optimizer-state memory compression >=3.5x, and successful run completion under a 2 GiB GPU memory cap.
- Stop condition: Stop if affine chunked states exceed fp32 Adam validation loss by more than 5% after warmup, fail to reduce optimizer-state memory by 3.5x, or cannot complete a representative run under the 2 GiB cap.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-chunked-optimizer-state-quantization-for-2gb-vram-training-d875c479422e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
