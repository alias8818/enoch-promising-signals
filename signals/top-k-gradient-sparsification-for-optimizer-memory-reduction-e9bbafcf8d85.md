# Top-K Gradient Sparsification for Optimizer Memory Reduction

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `top-k-gradient-sparsification-for-optimizer-memory-reduction-e9bbafcf8d85`
Run ID: `top-k-gradient-sparsification-for-optimizer-memory-reduction-e9bbafcf8d85-20260601T012312955349+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/c71372671f73

## What looked useful

Sparse top-k moment state has a memory-quality trap. At 1% top-k, active coordinates reached 95-97% on the stochastic linear probe and 50-71% on the quadratic control, yielding 1.43-2.45x dense Adam logical optimizer memory. At 0.05% top-k, memory could drop to 0.134x dense Adam without error feedback on the deterministic quadratic, but relative parameter error was 0.8869 versus 0.00000183 for dense Adam. Dense error-feedback residuals consumed enough memory to erase or sharply reduce savings.

## Boundaries and scale limits

This is a bounded local proxy result: no full neural-network training, no production sparse-kernel allocator implementation, and no long-horizon or multi-model validation. Logical sparse memory is best-case payload accounting and excludes hash/table overhead.

## Claim scope

Naive top-k Adam moment sparsification with sparse per-coordinate moment state, optionally with a dense error-feedback residual, did not provide a simultaneous optimizer-memory and quality win on 262,144-parameter CUDA synthetic linear and deterministic quadratic probes.

## Why it stopped

Proxy and deterministic-control evidence falsified the simple memory-reduction claim: settings that saved logical memory failed quality, while settings with broader coordinate coverage or dense error feedback lost the memory advantage.

## Recommended next action

Stop this naive top-k optimizer-memory path as no-paper evidence; only continue with a redesigned sparse optimizer that uses fixed state budgets or eviction and proves actual memory savings on a bounded neural training task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fixed-Budget Sparse Adam State With Eviction
- Success threshold: On the bounded neural task, fixed-budget sparse Adam must reach final validation loss <= 1.25x dense Adam, measured optimizer memory <= 0.5x dense Adam, and runtime <= 1.5x dense Adam.
- Stop condition: Stop if actual measured optimizer memory exceeds 0.5x dense Adam after sparse data-structure overhead, or if final validation loss is > 1.25x dense Adam at the same step budget.

## Evidence references

- Artifact root: `<local-path>/projects/top-k-gradient-sparsification-for-optimizer-memory-reduction-e9bbafcf8d85`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
