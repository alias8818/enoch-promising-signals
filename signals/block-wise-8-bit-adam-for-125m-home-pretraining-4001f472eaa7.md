# Block-Wise 8-Bit Adam for 125M Home Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `block-wise-8-bit-adam-for-125m-home-pretraining-4001f472eaa7`
Run ID: `block-wise-8-bit-adam-for-125m-home-pretraining-4001f472eaa7-20260524T170703300453+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/43764c537a02

## What looked useful

At 125M parameters, block size 2048 reduced persistent Adam moment state from 995,518,464 bytes to 249,365,712 bytes, but after 2 steps relative parameter L2 error vs fp32 Adam was 18.68 and max absolute error was 106.86. Block size 256 still had relative L2 error 13.57. The failure mechanism is second-moment entries quantizing to exact zero under default eps=1e-8, causing denominator underflow and update spikes.

## Boundaries and scale limits

Directly tested optimizer-state memory and synthetic-gradient update fidelity at 124,439,808 parameters on GB10. Did not test real language-model data, transformer activations, full pretraining loss, or mature 8-bit optimizer variants such as logarithmic, percentile-clipped, floor-preserving, or bitsandbytes-style encodings.

## Claim scope

A simple linear block-wise 8-bit Adam moment-state implementation is not a viable drop-in default-Adam optimizer for 125M-class home pretraining: it saves about 4x persistent optimizer-state memory but produces immediate update spikes against fp32 Adam on a 125M-parameter CUDA optimizer proxy.

## Why it stopped

Proxy/early falsification, not full pretraining validation: the direct 125M optimizer-state test fails update fidelity immediately at default Adam epsilon despite achieving the intended memory reduction.

## Recommended next action

Stop this implementation as a paper path; run a bounded follow-up that changes only the second-moment 8-bit encoding and requires low update drift before any real 125M pretraining attempt.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Floor-Preserving 8-Bit Second Moment for 125M Adam
- Success threshold: At default Adam eps=1e-8, final relative parameter L2 drift below 0.01 and no max absolute update spike above 10x fp32 Adam over 100 synthetic-gradient steps, with at least 3.5x persistent optimizer-state memory reduction.
- Stop condition: Stop negative if any revised v encoding still exceeds 1% relative parameter L2 drift or shows update spikes above 10x fp32 Adam before 100 steps.

## Evidence references

- Artifact root: `<local-path>/projects/block-wise-8-bit-adam-for-125m-home-pretraining-4001f472eaa7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
