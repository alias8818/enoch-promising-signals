# Selective Gradient Checkpointing via Runtime Importance Scoring

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `selective-gradient-checkpointing-via-runtime-importance-scoring-6091e79f030c`
Run ID: `selective-gradient-checkpointing-via-runtime-importance-scoring-6091e79f030c-20260522T125535786431+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/afd07c8c9072

## What looked useful

Runtime-low-importance checkpointing saved 229.00 MB versus no checkpointing with 5.38% step overhead, while static-memory checkpointing saved 358.76 MB with 7.99% overhead. Runtime importance per MB selected exactly the same layers as the static memory heuristic, indicating that memory/cost dominated the useful placement signal in this workload.

## Boundaries and scale limits

Evidence is limited to a synthetic transformer-like residual MLP stack, three seeds, short 5-step policy timings, one GB10 GPU, and no long-horizon GPT-2-small/full-language-model training. It is a mechanism probe, not a full-scale validation.

## Claim scope

On a 12-layer heterogeneous transformer-like CUDA training benchmark, raw runtime activation-gradient importance was not a useful standalone selector for exact selective gradient checkpoint placement; a static activation-memory heuristic saved substantially more memory at the same number of checkpointed layers, and cost-normalized importance collapsed to the static memory selection.

## Why it stopped

Proxy early falsification rather than full validation: raw runtime importance did not beat cheap static or random controls for selective exact checkpoint placement in the bounded GPU benchmark.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test an explicit memory/recompute/importance objective on a GPT-2-small-class training loop and require improvement over static memory heuristics after score overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cost-Aware Dynamic Checkpoint Placement on GPT-2-Small-Class Training
- Success threshold: At the same peak-memory budget, the dynamic cost-aware policy must improve tokens/sec or step time by at least 5% over the best static heuristic without worse loss trajectory across at least three seeds, including score overhead.
- Stop condition: Stop if dynamic placement is within measurement noise of the best static heuristic, if score overhead erases the benefit, or if loss/gradient correctness diverges from exact checkpoint controls.

## Evidence references

- Artifact root: `<local-path>/projects/selective-gradient-checkpointing-via-runtime-importance-scoring-6091e79f030c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
