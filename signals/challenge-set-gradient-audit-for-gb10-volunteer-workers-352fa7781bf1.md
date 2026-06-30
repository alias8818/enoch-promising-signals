# Challenge-set gradient audit for gb10 volunteer workers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `challenge-set-gradient-audit-for-gb10-volunteer-workers-352fa7781bf1`
Run ID: `challenge-set-gradient-audit-for-gb10-volunteer-workers-352fa7781bf1-20260613T105309266356+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/10a2893af618

## What looked useful

The bounded audit passed 16/20 checks and found deterministic tolerance misses concentrated in BF16 plus one near-threshold float32 matmul/GELU case and one FP16 matmul/GELU case; repeat drift was 0.0 for all checks.

## Boundaries and scale limits

Single GB10 host, one fixed seed, five synthetic functions, dimensions up to 256, no real training loop, no multi-host comparison, and no broad fused-kernel or optimizer coverage.

## Claim scope

A compact PyTorch challenge set can run on a local NVIDIA GB10 worker and produce deterministic gradient-error signals across exact-reference and CPU-float64-reference functions for float64, float32, bfloat16, and float16.

## Why it stopped

Proxy-scale gradient audit produced useful deterministic evidence but not full validation or a paper-ready result.

## Recommended next action

Stop this run as no-paper useful signal; next run should deepen the audit with multiple seeds, shape sweeps, finite-difference spot checks, and real model-layer cases on the same GB10 path.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-seed GB10 gradient audit with model-layer cases
- Success threshold: Reproduce the same dtype/case failure pattern in at least 8 of 10 seeds and show float32 L2-relative error below 1e-6 for all tested model-layer cases.
- Stop condition: Stop if failures are not reproducible across seeds or if CPU double and finite-difference references disagree enough to invalidate the comparison.

## Evidence references

- Artifact root: `<local-path>/projects/challenge-set-gradient-audit-for-gb10-volunteer-workers-352fa7781bf1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
