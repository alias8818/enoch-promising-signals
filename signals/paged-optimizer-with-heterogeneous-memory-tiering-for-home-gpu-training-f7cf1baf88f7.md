# Paged optimizer with heterogeneous memory tiering for home GPU training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `paged-optimizer-with-heterogeneous-memory-tiering-for-home-gpu-training-f7cf1baf88f7`
Run ID: `paged-optimizer-with-heterogeneous-memory-tiering-for-home-gpu-training-f7cf1baf88f7-20260610T172516650564+0000`

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

At 32M parameters with 244.141 MiB logical Adam state and a 32 MiB page cache, clustered access used 0.138x the baseline RSS increment at 1.368x mean step time, random sparse access used 0.869x RSS at 4.237x step time, and dense access used 1.137x RSS at 2.178x step time. Paging is only promising when optimizer-state locality is strong.

## Boundaries and scale limits

No GPU training, no model forward/backward pass, no PCIe/UMA transfer overlap, no real transformer optimizer trace, and no comparison to production paged optimizer implementations. The result is a mechanism probe, not a home-GPU training validation.

## Claim scope

CPU-only synthetic Adam-state benchmark: page-backed optimizer state reduced resident memory under stable clustered page locality but was slower, and it became unattractive under random sparse or dense access.

## Why it stopped

No-paper useful signal: this CPU-only synthetic probe supports the locality-dependent mechanism but early-falsifies the broad dense-training claim; full validation requires real GPU training evidence.

## Recommended next action

Run a bounded PyTorch prototype on a commodity 8-12 GB GPU or unified-memory home GPU using a real sparse/locality-heavy workload, and stop unless it keeps throughput loss below 20% while increasing feasible model size or batch size versus full Adam.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Commodity-GPU PyTorch validation of locality-aware paged Adam
- Success threshold: Paged optimizer enables at least 25% larger batch size or parameter count than full Adam with no more than 20% throughput loss and no loss divergence over a bounded training run.
- Stop condition: Stop if page churn causes more than 20% throughput loss at the same feasible workload, if no larger batch/model fits, or if measured real workloads look dense/random rather than locality-heavy.

## Evidence references

- Artifact root: `<local-path>/projects/paged-optimizer-with-heterogeneous-memory-tiering-for-home-gpu-training-f7cf1baf88f7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
