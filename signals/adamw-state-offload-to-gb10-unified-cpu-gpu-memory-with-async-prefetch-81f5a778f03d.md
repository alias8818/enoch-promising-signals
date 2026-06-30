# AdamW state offload to gb10 unified CPU/GPU memory with async prefetch

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adamw-state-offload-to-gb10-unified-cpu-gpu-memory-with-async-prefetch-81f5a778f03d`
Run ID: `adamw-state-offload-to-gb10-unified-cpu-gpu-memory-with-async-prefetch-81f5a778f03d-20260629T055201971532+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4178ad38520c

## What looked useful

Managed AdamW state on GB10 relieved PyTorch CUDA allocator pressure by 8 MB, 80 MB, 400 MB, and 800 MB at 1M, 10M, 50M, and 100M parameters respectively. Runtime without explicit prefetch was roughly baseline at 50M-100M; immediate prefetch was slower than no-prefetch at every size and 1.9% slower than GPU-resident baseline at 100M.

## Boundaries and scale limits

Synthetic single-tensor optimizer update only; no real model, backward pass, bucket scheduler, separate-stream overlap, checkpoint/resume integration, convergence test, or memory-pressure run near GB10 capacity.

## Claim scope

On a GB10 host with CUDA 13 and PyTorch 2.12, fp32 AdamW m/v state can be allocated with cudaMallocManaged outside PyTorch's CUDA caching allocator and used in synthetic vectorized AdamW updates from 1M to 100M parameters. This saves 8 bytes per parameter from PyTorch CUDA allocation with matching checksums; immediate same-stream per-step prefetch is not a runtime win.

## Why it stopped

Bounded mechanism probe succeeded for allocator offload but early-falsified immediate per-step async prefetch as a performance improvement; no full training or overlap evidence was produced.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next action is a bounded bucketed optimizer prototype that overlaps managed-state prefetch for bucket N+1 on a separate stream while updating bucket N in a real training loop.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bucketed managed-memory AdamW state with overlapped prefetch during real training
- Success threshold: At least 7 bytes per trainable parameter reduction in PyTorch CUDA allocator pressure for AdamW state with no more than 5% step-time or tokens/sec regression versus standard AdamW, and no loss/convergence regression over the bounded training window.
- Stop condition: Stop if separate-stream overlapped prefetch remains more than 10% slower than standard AdamW after bucket-size tuning, if checkpoint/resume is unreliable, or if managed-state memory pressure triggers unsafe MemAvailable decline on GB10.

## Evidence references

- Artifact root: `<local-path>/projects/adamw-state-offload-to-gb10-unified-cpu-gpu-memory-with-async-prefetch-81f5a778f03d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
