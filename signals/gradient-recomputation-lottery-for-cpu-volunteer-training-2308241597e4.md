# Gradient Recomputation Lottery for CPU Volunteer Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gradient-recomputation-lottery-for-cpu-volunteer-training-2308241597e4`
Run ID: `gradient-recomputation-lottery-for-cpu-volunteer-training-2308241597e4-20260613T175206835541+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e68f043f16b4

## What looked useful

Lottery p=0.5 used 50.8% of store-all activation memory at 1.22x CPU time; lottery p=0.25 used 27.9% activation memory at 1.97x CPU time. All strategies had identical mean final loss in the deterministic proxy.

## Boundaries and scale limits

Local CPU-only proxy: not a transformer, not PyTorch autograd, not distributed volunteer training, no optimizer-state or network-straggler validation, and no long-run convergence study.

## Claim scope

In a bounded CPU NumPy proxy with manual gradients, lottery-style random activation checkpointing preserved the loss trajectory while trading CPU time for lower retained activation bytes.

## Why it stopped

No-paper closure: the local proxy supports the recomputation mechanism but does not provide direct publication-grade evidence for CPU volunteer training.

## Recommended next action

Run a bounded PyTorch transformer/GPT-2-small-class autograd benchmark comparing lottery checkpointing against standard activation checkpointing under memory pressure.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PyTorch Transformer Lottery Checkpointing Under CPU Memory Pressure
- Success threshold: At least 35% lower peak activation memory than store-all with no loss degradation beyond seed noise and CPU time no worse than 1.5x a matched fixed-checkpoint baseline at similar memory.
- Stop condition: Stop if lottery checkpointing is slower than fixed checkpointing by more than 1.5x at matched memory or if loss diverges/mismatches the baseline beyond seed noise.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-recomputation-lottery-for-cpu-volunteer-training-2308241597e4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
