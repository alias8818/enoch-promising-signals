# CPU-Bound Speculative Decoding with Extreme Quantization Baselines

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cpu-bound-speculative-decoding-with-extreme-quantization-baselines-14a90fdaea6c`
Run ID: `cpu-bound-speculative-decoding-with-extreme-quantization-baselines-14a90fdaea6c-20260608T215912796429+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/aed08e2299b1

## What looked useful

The break-even bound is concrete: in the calibrated medium run, int8 at gamma 8-16 would need draft-token cost below about 0.24-0.38x of target greedy cost, but observed dequantized int8 cost was 1.012x and NumPy int32-dot int8 cost was 20.56x. Int4 acceptance was only about 0.57 and had no modeled break-even path in the tested windows.

## Boundaries and scale limits

This is not a full transformer serving result. It does not test KV-cache behavior, real text/token distributions, optimized ggml/llama.cpp low-bit kernels, or separately trained smaller draft models.

## Claim scope

On a controlled NumPy/OpenBLAS CPU proxy with a 4096-vocab, 512-dim neural bigram target, naive int8/int4 quantized draft baselines do not produce speculative-decoding speedup: int8 preserves top-1 acceptance but is not cheaper than fp32 target tokens, while int4 loses too much acceptance and integer-dot baselines are much slower.

## Why it stopped

Proxy early falsification, not full validation: naive dequantized and NumPy integer-dot quantized drafts failed the observed CPU cost/acceptance break-even requirements for speculative speedup.

## Recommended next action

Stop this run as a proxy early falsification of naive extreme-quantized CPU drafts; the next bounded test should use optimized ggml/llama.cpp low-bit kernels on a real tiny transformer and require measured draft cost below the recorded break-even bound.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU Transformer Speculative Decoding with Optimized Low-Bit Draft Kernels
- Success threshold: At least one optimized low-bit draft configuration achieves end-to-end speculative decoding speedup greater than 1.2x versus target-only greedy decoding on CPU, with measured draft-token cost below the relevant break-even threshold and no correctness failure in target verification.
- Stop condition: Stop if optimized low-bit draft-token cost remains above 0.5x target greedy cost or if measured acceptance below 0.8 prevents any modeled gamma 8-16 speedup.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-bound-speculative-decoding-with-extreme-quantization-baselines-14a90fdaea6c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
