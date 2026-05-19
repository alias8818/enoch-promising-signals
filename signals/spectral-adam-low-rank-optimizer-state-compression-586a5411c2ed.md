# Spectral Adam: Low-Rank Optimizer State Compression

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `spectral-adam-low-rank-optimizer-state-compression-586a5411c2ed`
Run ID: `spectral-adam-low-rank-optimizer-state-compression-586a5411c2ed-20260518T084636091947+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/70f36d7b4575

## What looked useful

Dense-Adam diagnostics show the second moment is spectrally concentrated while the first moment is not: rank-8 energy averaged 0.904 for low-rank-task exp_avg_sq but only 0.493 for exp_avg, and 0.662 versus 0.225 on the full-rank task. This suggests hybrid or second-moment-only compression is more plausible than compressing both moments.

## Boundaries and scale limits

Evidence is limited to synthetic/proxy matrix regression on one GB10 GPU with exact per-step SVD; no GPT-2-small, LLM-scale, distributed, or optimized-kernel validation was run.

## Claim scope

On controlled 192x192 matrix-regression proxy tasks, a direct SpectralAdam design that stores both Adam first and second moments as truncated SVD factors reduces nominal stored optimizer-state memory but does not preserve Adam-like convergence and is much slower than Adam.

## Why it stopped

Proxy/direct implementation evidence showed severe convergence degradation and 30x-50x step-rate slowdown relative to Adam despite nominal state-memory savings; this is an early falsification of the simple design, not a full-scale LLM validation.

## Recommended next action

Stop this simple all-state SpectralAdam line as a no-paper proxy/early falsification; run a bounded follow-up that compresses only the second moment or uses a hybrid dense/quantized first moment.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid Adam with spectral second-moment compression
- Success threshold: At least 1.5x persistent optimizer-state reduction versus Adam, no more than 20% step-time overhead in the optimized prototype, and final metrics within the stated Adam tolerances on all bounded tasks.
- Stop condition: Stop if hybrid compression fails to reach within 2x Adam final loss on either proxy task or if step-time overhead remains above 2x before optimized kernels.

## Evidence references

- Artifact root: `<local-path>/projects/spectral-adam-low-rank-optimizer-state-compression-586a5411c2ed`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
