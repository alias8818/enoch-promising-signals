# Block-wise 4-bit Optimizer State Compression with Shared Exponents

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `block-wise-4-bit-optimizer-state-compression-with-shared-exponents-345a6e5f2c02`
Run ID: `block-wise-4-bit-optimizer-state-compression-with-shared-exponents-345a6e5f2c02-20260601T093012690651+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e1263501b224

## What looked useful

The attractive 8.06-9.0 bits/parameter state footprint is outweighed by second-moment underflow: v zeros reach 26.7% at only 1 decade of dynamic range for block 16, and all quantized training variants remain near random accuracy while FP32 Adam learns.

## Boundaries and scale limits

CPU-only synthetic stress test and toy logistic regression; no transformer, real LM gradients, GPU fused optimizer, checkpoint persistence, or large-scale training was tested.

## Claim scope

Naive block-wise 4-bit Adam moment compression with one shared power-of-two exponent per block for signed m and unsigned v fails on synthetic Adam update stress tests and a small ill-conditioned logistic-regression training probe.

## Why it stopped

Proxy and toy direct tests provide an early falsification of the naive shared-exponent 4-bit Adam-state scheme, not a full validation or universal impossibility result.

## Recommended next action

Stop this naive encoding as a paper path; only continue with a bounded follow-up that changes the v representation to avoid underflow, then reruns the same stress and toy-training gates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Nonzero/log-domain second-moment encoding for 4-bit Adam state compression
- Success threshold: Mean validation loss within 0.05 absolute of FP32 on the toy probe, update cosine above 0.95 for at least 2 decades of within-block dynamic range, and no more than 1% zero/underflowed effective v entries.
- Stop condition: Stop if the modified encoding still has more than 5% effective v underflow at 2 decades or toy validation loss remains more than 0.25 worse than FP32 across three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/block-wise-4-bit-optimizer-state-compression-with-shared-exponents-345a6e5f2c02`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
