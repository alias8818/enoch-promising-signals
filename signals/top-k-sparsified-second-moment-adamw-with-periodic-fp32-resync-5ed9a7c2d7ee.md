# Top-k sparsified second-moment AdamW with periodic FP32 resync

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `top-k-sparsified-second-moment-adamw-with-periodic-fp32-resync-5ed9a7c2d7ee`
Run ID: `top-k-sparsified-second-moment-adamw-with-periodic-fp32-resync-5ed9a7c2d7ee-20260621T153953648877+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/abe0ec9a3419

## What looked useful

Sparse second-moment state can reduce estimated persistent optimizer-state memory to about 0.51x-0.60x and can work on stable-curvature quadratic proxies, but the naive top-k plus scalar tail floor fails the stochastic regression control by 12.3x-13.7x final-loss ratio for resync-25 variants and 4.37e3x for top5 resync-100.

## Boundaries and scale limits

No GPU kernel, no PyTorch model training, no language-model workload, no production resync implementation without a dense oracle; 700-step CPU probes only.

## Claim scope

CPU NumPy proxy comparing dense AdamW to naive sparse second-moment AdamW with oracle periodic FP32 resync on two ill-conditioned quadratic objectives and one stochastic minibatch linear regression objective.

## Why it stopped

Proxy and direct small-control evidence show unacceptable degradation on stochastic minibatch regression despite stable-quadratic successes; this is an early falsification of the naive mechanism, not full-scale validation.

## Recommended next action

Stop this naive variant as no-paper early negative; next bounded test should add explicit tail correction or randomized refresh and require minibatch regression loss ratio <=1.2 at <=0.60x estimated optimizer-state memory before any model-scale run.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Tail-corrected sparse second-moment AdamW with randomized refresh
- Success threshold: Across 3 seeds, loss ratio <=1.2 on stochastic minibatch regression and no catastrophic quadratic instability while estimated persistent optimizer-state memory remains <=0.60x dense AdamW.
- Stop condition: Stop if any required small-control task exceeds 2x dense AdamW final loss at <=0.60x memory or needs dense second-moment persistence to remain stable.

## Evidence references

- Artifact root: `<local-path>/projects/top-k-sparsified-second-moment-adamw-with-periodic-fp32-resync-5ed9a7c2d7ee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
