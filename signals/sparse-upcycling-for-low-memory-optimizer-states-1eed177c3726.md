# Sparse Upcycling for Low-Memory Optimizer States

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sparse-upcycling-for-low-memory-optimizer-states-1eed177c3726`
Run ID: `sparse-upcycling-for-low-memory-optimizer-states-1eed177c3726-20260525T194301024706+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/830068e89f03

## What looked useful

Sparse optimizer-state storage can be useful when the target and useful gradients are sparse, but the specific upcycling policy tested here caused heavy state churn and was worse than cold sparse admission.

## Boundaries and scale limits

Proxy-only CUDA experiment: dim=65536, true sparsity=512, batch=256, 600 steps, five seeds. No transformer, real corpus, GPT-2-small-class baseline, distributed training, long-horizon stability, or optimizer offload comparison was tested.

## Claim scope

On synthetic sparse linear regression with dense gradients, a cold sparse Adam-state baseline stored 16x fewer moment floats than full Adam and improved final loss and sparse support recovery, but the tested upcycling eviction/initialization rule underperformed the cold sparse-state baseline at the same budget.

## Why it stopped

Moderate proxy evidence shows the named upcycling policy is not competitive with a simpler sparse-state control, so this run should close as useful no-paper evidence rather than continue locally.

## Recommended next action

Stop this upcycling variant as no-paper evidence; run a bounded follow-up on cold/adaptive sparse-state Adam in a small transformer or GPT-2-small-class setting before considering scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cold Sparse-State Adam on Small Transformer Training
- Success threshold: Sparse-state Adam achieves within 2% validation loss or perplexity of full Adam while using at least 8x fewer moment entries, and does not exceed the cold sparse-state baseline's churn-adjusted runtime by more than 10%.
- Stop condition: Stop if sparse-state methods trail full Adam by more than 5% validation loss or perplexity at 8x memory reduction across three seeds, or if active-state churn prevents stable support/parameter reuse.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-upcycling-for-low-memory-optimizer-states-1eed177c3726`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
