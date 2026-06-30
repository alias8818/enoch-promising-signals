# Dynamic gradient pruning for CPU-based tiny model memory reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-gradient-pruning-for-cpu-based-tiny-model-memory-reduction-81c25d38cbaf`
Run ID: `dynamic-gradient-pruning-for-cpu-based-tiny-model-memory-reduction-81c25d38cbaf-20260607T170535323779+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/aa1218c962cc

## What looked useful

At a 12.6M-parameter float32 MLP scale, streamed top-k pruning reduced peak RSS by about 79 MB, roughly 42% versus dense full-gradient SGD, across 5%, 10%, and 20% keep fractions. The tradeoff was 3.5x-4.7x slower runtime and weaker short-run loss movement, with 20% keep recovering about 70% of the dense loss decrease.

## Boundaries and scale limits

Synthetic MLP only; 3 SGD steps; no autograd framework, transformer, real dataset, Adam/AdamW optimizer-state accounting, long-run convergence, or validation accuracy.

## Claim scope

A NumPy CPU two-layer MLP synthetic regression probe showed that dynamic top-k gradient pruning can reduce peak process memory when gradients are pruned through a row-streamed update path before full dense gradient matrices are materialized.

## Why it stopped

Bounded synthetic evidence supports the memory mechanism but is not publication-grade and exposes substantial speed and optimization tradeoffs.

## Recommended next action

Stop this run as no-paper useful signal; next, implement a block/vectorized streamed top-k or error-feedback kernel and test on a tiny transformer with optimizer-state memory included.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Block-streamed gradient pruning with error feedback for tiny transformer CPU training
- Success threshold: At least 25% peak RSS reduction versus dense training, at least 90% of dense validation-loss improvement over the measured window, and no more than 2x wall-clock slowdown.
- Stop condition: Stop if optimizer-state memory eliminates the practical peak RSS reduction below 15%, or if validation-loss improvement remains below 75% of dense after tuning keep fraction/error feedback.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-gradient-pruning-for-cpu-based-tiny-model-memory-reduction-81c25d38cbaf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
