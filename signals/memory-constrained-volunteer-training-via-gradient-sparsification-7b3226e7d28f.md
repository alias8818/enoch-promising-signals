# Memory-Constrained Volunteer Training via Gradient Sparsification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `memory-constrained-volunteer-training-via-gradient-sparsification-7b3226e7d28f`
Run ID: `memory-constrained-volunteer-training-via-gradient-sparsification-7b3226e7d28f-20260607T035900880722+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/6a20286ef314

## What looked useful

Top-k sparsification reduced transmitted gradient payload by 50x at 1% density and 500x at 0.1% density while maintaining similar top-1 accuracy on the proxy task, but error-feedback variants retained a dense per-worker residual and therefore did not reduce estimated volunteer-side gradient/residual memory versus dense gradients. The memory-constrained premise only held for no-error-feedback sparsification, which showed a small loss penalty.

## Boundaries and scale limits

Not tested on real volunteer devices, real networks, transformer language modeling, GPT-2-small-class baselines, long-horizon training, optimizer-state pressure, privacy, failures, or 7B-scale models.

## Claim scope

Synthetic MLP volunteer-training proxy with 8 simulated workers, 3 seeds, and dense versus top-k sparse gradient aggregation on NVIDIA GB10.

## Why it stopped

Closed as a proxy-scale useful signal, not a full validation: the tested mechanism helps bandwidth but straightforward error feedback does not solve worker memory pressure.

## Recommended next action

Run a bounded GPT-2-small-class follow-up that tests sparse-residual or residual-offload variants against dense training under explicit worker memory caps and injected volunteer churn.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded Transformer Test of Memory-Bounded Sparse Residuals
- Success threshold: Sparse residual/offload variant reaches within 5% of dense held-out loss or perplexity while using at most 25% of dense-gradient volunteer gradient/residual memory and at least 20x fewer transmitted bytes.
- Stop condition: Stop if no variant can stay under the 25% memory budget without more than 10% held-out loss/perplexity regression after the planned bounded run.

## Evidence references

- Artifact root: `<local-path>/projects/memory-constrained-volunteer-training-via-gradient-sparsification-7b3226e7d28f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
