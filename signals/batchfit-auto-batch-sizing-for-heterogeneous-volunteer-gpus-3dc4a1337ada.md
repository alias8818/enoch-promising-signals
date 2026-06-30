# BatchFit: Auto-Batch Sizing for Heterogeneous Volunteer GPUs

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `batchfit-auto-batch-sizing-for-heterogeneous-volunteer-gpus-3dc4a1337ada`
Run ID: `batchfit-auto-batch-sizing-for-heterogeneous-volunteer-gpus-3dc4a1337ada-20260621T174443604967+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8e1c1f27a7fb

## What looked useful

Across 24 trials x 250 steps in mild, severe, and churn scenarios, BatchFit achieved 2.242x, 3.919x, and 3.533x throughput vs equal-min and 1.200x, 1.134x, and 1.634x vs memory-proportional sizing, with zero simulated OOMs.

## Boundaries and scale limits

Simulator-only evidence: no real CUDA allocator behavior, NCCL/internet communication, physical heterogeneous GPUs, model validation loss, or end-to-end training quality was measured.

## Claim scope

In a deterministic local simulator of synchronized heterogeneous volunteer GPU training, an online per-worker batch-fitting controller improved throughput over equal-min and memory-proportional static batch policies while avoiding simulated OOM retry churn.

## Why it stopped

Proxy-only useful signal; the result supports the mechanism in simulation but does not directly validate BatchFit on real volunteer GPUs.

## Recommended next action

Stop this run as a no-paper simulator result; next run should implement BatchFit in a direct 4-plus heterogeneous GPU training prototype and compare tokens/s, OOM retries, communication overhead, and validation loss against equal-min, memory-proportional, and tuned static baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct heterogeneous GPU BatchFit prototype
- Success threshold: BatchFit improves tokens/s by at least 20% over memory-proportional static sizing with no increase in OOM retry rate and validation loss within 1% relative at matched tokens.
- Stop condition: Stop as negative if BatchFit improves tokens/s by less than 10%, causes more OOM/retry events than the best static baseline, or loses more than 1% relative validation quality at matched tokens.

## Evidence references

- Artifact root: `<local-path>/projects/batchfit-auto-batch-sizing-for-heterogeneous-volunteer-gpus-3dc4a1337ada`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
