# PagedOptimizer for GPT-2 small pretraining on 4GB VRAM

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `pagedoptimizer-for-gpt-2-small-pretraining-on-4gb-vram-faa2059e11b8`
Run ID: `pagedoptimizer-for-gpt-2-small-pretraining-on-4gb-vram-faa2059e11b8-20260601T010251311673+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/c71372671f73

## What looked useful

GPU AdamW already fit GPT-2-small sequence length 1024 at batches 1-2 under 4 GiB. At batch 3, GPU AdamW and CPU-paged AdamW both peaked at 4.643 GiB allocated and 5.191 GiB reserved, so paging did not rescue the failing case. Gradient checkpointing made batch 3 fit with standard GPU AdamW.

## Boundaries and scale limits

Synthetic data only, short 1-3 step probes, custom CPU-state paged AdamW rather than production bitsandbytes, and GB10 UMA rather than a discrete hard-limited 4 GB GPU.

## Claim scope

On this GB10 CUDA setup with synthetic GPT-2-small training steps at sequence length 1024, CPU-state paged AdamW reduces persistent CUDA optimizer state but does not by itself enable the first non-fitting 4 GiB-target batch size; activation memory is the limiting peak.

## Why it stopped

Proxy early falsification, not full validation: the tested paged optimizer moved Adam moments off CUDA but activation memory dominated the non-fitting configuration, and standard GPU AdamW already fit meaningful GPT-2-small cases under the 4 GiB target.

## Recommended next action

Stop this run as a proxy early falsification; only retry if a discrete hard 4 GB GPU or allocator cap plus a production paged optimizer is available.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hard 4 GB GPT-2-small paged-optimizer validation
- Success threshold: Find at least one matched GPT-2-small configuration where GPU AdamW OOMs during optimizer-state allocation or step under 4 GiB, paged AdamW completes at least 100 steps with peak reserved memory below 4 GiB, and throughput remains at least 25% of the GPU AdamW nearest-fitting baseline.
- Stop condition: Stop if the first non-fitting configurations are all activation-memory limited, if standard gradient checkpointing resolves the memory issue without paging, or if paged AdamW cannot keep reserved CUDA memory below 4 GiB.

## Evidence references

- Artifact root: `<local-path>/projects/pagedoptimizer-for-gpt-2-small-pretraining-on-4gb-vram-faa2059e11b8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
