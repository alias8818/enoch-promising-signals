# KV-Res: 2-bit KV cache with per-head FP8 residual scale

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-res-2-bit-kv-cache-with-per-head-fp8-residual-scale-8e926c38b672`
Run ID: `kv-res-2-bit-kv-cache-with-per-head-fp8-residual-scale-8e926c38b672-20260610T120511913530+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ff79ed4c30e8

## What looked useful

A single per-head residual magnitude is too coarse under outlier-heavy KV. Residual signs make a strong Gaussian reconstruction mechanism, but realistic outlier robustness likely needs finer residual-scale granularity.

## Boundaries and scale limits

No real model KV traces, perplexity, task accuracy, packed-kernel throughput, or long-context serving validation. CPU-only NumPy proxy with synthetic distributions and two group sizes.

## Claim scope

Synthetic attention proxy at seq=512, heads=8, dim=64: q2 plus per-head FP8 residual magnitude and residual sign bits improves Gaussian KV attention-output error versus q3, but fails on mixed-tail, token-outlier, and channel-outlier KV; per-head residual scale without residual signs is worse than plain q2.

## Why it stopped

Closed as no-paper useful signal: the local proxy partially supports the residual-sign mechanism but early-falsifies the per-head-only residual scale as robust replacement for q3/q4 under outlier-heavy KV.

## Recommended next action

Run a bounded follow-up with per-head-per-channel or per-head-per-block residual magnitudes, requiring outlier distributions to beat q3 attention-output error while staying below 3.25 effective bits/value.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Finer residual-scale granularity for low-bit KV cache outlier robustness
- Success threshold: At effective bits/value below 3.25, the finer-granularity residual method must beat q3 mean attention-output relative MSE on all tested outlier distributions and improve q2 by at least 2x.
- Stop condition: Stop if any outlier distribution remains more than 25% worse than q3 attention-output relative MSE or if effective cost reaches 3.25 bits/value without closing the gap.

## Evidence references

- Artifact root: `<local-path>/projects/kv-res-2-bit-kv-cache-with-per-head-fp8-residual-scale-8e926c38b672`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
