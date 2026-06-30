# Gradient Checkpointing Schedule Optimization for Tiny-VRAM

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `gradient-checkpointing-schedule-optimization-for-tiny-vram-602a84546407`
Run ID: `gradient-checkpointing-schedule-optimization-for-tiny-vram-602a84546407-20260605T194808301109+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7a7f94acbc26

## What looked useful

The optimizer used available modeled memory to avoid over-checkpointing. Across four budgets it reduced modeled recompute 23.6-60.1% versus uniform full checkpointing and improved median CUDA step time 9.5-25.5%; it also beat greedy by 3.3-15.8% median step time.

## Boundaries and scale limits

Toy heterogeneous MLP only; budgets are modeled rather than enforced by OOM; CUDA allocator peak did not distinguish schedules; no GPT-2-small-class transformer trace, real optimizer-state pressure, long training run, or framework integration was validated.

## Claim scope

On a 12-block heterogeneous CUDA toy network with simulated activation-memory budgets, an exact activation/cost-aware checkpoint scheduler reduced recompute proxy and median backward-step time versus uniform full checkpointing and greedy segment selection.

## Why it stopped

Closed as no-paper useful signal because the evidence is a toy/proxy validation, not direct tiny-VRAM transformer training evidence.

## Recommended next action

Run a bounded transformer-trace follow-up with measured per-layer activations and enforced allocator caps before making any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer Trace Checkpoint Schedule Validation Under Enforced Memory Caps
- Success threshold: At two or more enforced memory budgets, the optimized schedule must remain within the cap and improve median step time by at least 8% versus the strongest feasible baseline over repeated CUDA training steps.
- Stop condition: Stop if optimized schedules fail to meet enforced caps, do not beat the strongest baseline by 8% median step time, or only win under modeled memory while failing direct allocator/OOM validation.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-checkpointing-schedule-optimization-for-tiny-vram-602a84546407`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
