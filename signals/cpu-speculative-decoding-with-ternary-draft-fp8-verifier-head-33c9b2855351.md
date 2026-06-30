# CPU speculative decoding with ternary draft + FP8 verifier head

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cpu-speculative-decoding-with-ternary-draft-fp8-verifier-head-33c9b2855351`
Run ID: `cpu-speculative-decoding-with-ternary-draft-fp8-verifier-head-33c9b2855351-20260619T171432065427+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/38572eb15e20

## What looked useful

FP8 quantization preserved top-1 in the proxy, but the ternary draft accepted only 0.93% to 12.16% of positions and the combined speculative path reached at best 0.0628x FP32 baseline accepted-token throughput.

## Boundaries and scale limits

Synthetic hidden states only; no trained draft model; no native FP8 CPU GEMM; no bitpacked ternary kernel; no end-to-end real transformer serving.

## Claim scope

Bounded synthetic CPU LM-head proxy with direct ternarization of a verifier head and cached software-dequantized approximate E4M3 FP8 weights does not produce speculative decoding speedup.

## Why it stopped

Proxy early falsification: bounded synthetic tests showed acceptance far below break-even and no robust FP8 CPU head speedup, so larger local CPU-only runs are not justified.

## Recommended next action

Stop this naive CPU-only dense-matmul path; only revisit with a trained ternary draft and native bitpacked ternary/FP8 CPU kernels measured against FP32 end-to-end decode.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained ternary draft plus native low-bit CPU kernels for speculative decoding
- Success threshold: At least 1.2x end-to-end accepted-token throughput versus FP32 baseline with verifier-equivalent outputs on a real small LM and acceptance above the measured break-even threshold.
- Stop condition: Stop if trained-draft acceptance remains below break-even or native low-bit kernels fail to deliver at least 1.5x head-level speedup over FP32 matmul.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-speculative-decoding-with-ternary-draft-fp8-verifier-head-33c9b2855351`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
