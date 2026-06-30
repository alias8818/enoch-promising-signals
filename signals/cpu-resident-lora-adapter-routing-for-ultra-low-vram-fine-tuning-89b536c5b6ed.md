# CPU-Resident LoRA Adapter Routing for Ultra-Low VRAM Fine-Tuning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-resident-lora-adapter-routing-for-ultra-low-vram-fine-tuning-89b536c5b6ed`
Run ID: `cpu-resident-lora-adapter-routing-for-ultra-low-vram-fine-tuning-89b536c5b6ed-20260621T110353612671+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/eacd2fdc9cc6

## What looked useful

Adapter device-memory estimate dropped from 50,331,648 bytes resident-all to 196,608 bytes with cache size 1, 786,432 bytes with cache size 4, and 3,145,728 bytes with cache size 16. Locality routing achieved 94.2%-95.4% cache hit rate, while random and round-robin routing collapsed to 0.0%-3.75% and 0.0% respectively.

## Boundaries and scale limits

No CUDA, measured VRAM, PCIe/NVLink/UMA transfer latency, transformer integration, optimizer-state migration, or real downstream quality measurement. Tested 256 adapters, dimension 512, rank 16, batch 16, and 240 synthetic update steps per route pattern.

## Claim scope

CPU-only NumPy proxy shows that CPU-resident routed LoRA adapter caching can reduce estimated adapter device memory in proportion to cache_size/adapter_count, while routing locality determines cache hit rate.

## Why it stopped

Closed as no-paper useful signal because this run is a CPU-only proxy and cannot validate actual ultra-low-VRAM GPU fine-tuning viability.

## Recommended next action

Run one bounded GPU follow-up implementing the same routed-adapter cache in PyTorch on a low-VRAM model, measuring peak VRAM, transfer latency, step time, and loss against resident-all and single-adapter LoRA controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPU VRAM and Transfer Validation for CPU-Resident Routed LoRA Cache
- Success threshold: For a high-locality or router-batched schedule, cache size <=16 adapters uses <=10% of resident-all adapter VRAM, reaches >=80% of resident-all step throughput, and matches resident-all loss within 5% after the bounded run.
- Stop condition: Stop if measured transfer overhead pushes throughput below 50% of resident-all at cache size 16, or if peak VRAM is not reduced by at least 5x versus resident-all multi-adapter LoRA.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-resident-lora-adapter-routing-for-ultra-low-vram-fine-tuning-89b536c5b6ed`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
