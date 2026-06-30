# CPU-efficient paged attention for extended context with 3GB VRAM budget

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cpu-efficient-paged-attention-for-extended-context-with-3gb-vram-budget-cf7d947c74d4`
Run ID: `cpu-efficient-paged-attention-for-extended-context-with-3gb-vram-budget-cf7d947c74d4-20260610T101228475316+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f080886e20ca

## What looked useful

The limiting factor is old-KV bytes scanned, not page-table correctness. A 3GiB KV budget fits about 6,144 tokens for a Llama-7B-shaped fp16 KV cache; scanning old KV beyond that is estimated at 196.8 ms/token for 8k context, 984.2 ms/token for 16k, and 5.7 s/token for 64k before model/GPU compute.

## Boundaries and scale limits

Synthetic CPU-only benchmark; no real model, GPU, PCIe/UMA overlap, fused kernels, multi-request scheduler, or quality evaluation. Extrapolation assumes the measured 5.45 GB/s effective old-KV scan rate at the largest synthetic context.

## Claim scope

On this CPU worker, a NumPy streaming paged-attention kernel for one-token decode was numerically correct and reduced temporary score storage, but full old-KV CPU scans extrapolated to a 32-layer 7B-class fp16 KV cache exceed practical per-token latency under a 3GiB hot KV budget.

## Why it stopped

Proxy early falsification of naive/full CPU old-KV scans: the measured CPU paged scan rate makes the extrapolated 7B-class old-KV contribution exceed interactive decode budgets even at 8k context.

## Recommended next action

Stop this full-scan paged-attention direction as no-paper; run a bounded follow-up that avoids scanning most old KV bytes via selective page retrieval or compression.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Selective old-page retrieval for 3GiB-budget extended context
- Success threshold: Scan at least 10x fewer old-KV bytes than full paging while keeping attention output error below a task-appropriate bound and estimated CPU old-KV latency below 100 ms/token at 8k context.
- Stop condition: Terminate if selective retrieval cannot cut old-KV bytes by at least 10x on replay traces or if output error is too high at that reduction.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-efficient-paged-attention-for-extended-context-with-3gb-vram-budget-cf7d947c74d4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
