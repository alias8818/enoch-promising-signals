# SVD-Residual 2-bit: Principled Top-k Singular Channel Preservation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `svd-residual-2-bit-principled-top-k-singular-channel-preservation-6f21b18e39db`
Run ID: `svd-residual-2-bit-principled-top-k-singular-channel-preservation-6f21b18e39db-20260528T101113418779+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b81ac000324e

## What looked useful

On 8 GPT-2 matrices, k=16 SVD-residual q2 reduced median relative output MSE to 0.517x direct q2 with 1.221x estimated storage, winning 8/8 cases versus q2 and 8/8 versus random rank-k residual. Synthetic spiked/power-law spectra improved strongly, while flat spectra showed little benefit.

## Boundaries and scale limits

No end-to-end perplexity, activation-trace calibration, quantized kernels, latency, memory-bandwidth, or broad model-family validation. Real-model evidence covers only 8 GPT-2 matrices and random Gaussian inputs.

## Claim scope

Bounded matrix-level probe on synthetic spectra and 8 pretrained GPT-2 2D weight matrices: exact top-k SVD preservation plus row-wise 2-bit residual quantization reduces random-output MSE versus direct row-wise q2 and random rank-k residual controls when spectra are structured.

## Why it stopped

Stopped after a successful bounded mechanism probe; evidence is useful but proxy-level and not a full validation of deployable 2-bit LLM quantization.

## Recommended next action

Run a bounded end-to-end GPT-2-small perplexity follow-up with all eligible linear weights quantized, real activation calibration, matched-storage q2/q3/q4 baselines, and the same random-rank control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end GPT-2 SVD-residual 2-bit perplexity validation
- Success threshold: At k <= 16 or a matched-storage rank, SVD-residual q2 must reduce perplexity degradation versus direct q2 by at least 25% and beat random rank-k residual in at least 80% of quantized layers, without exceeding q3 storage.
- Stop condition: Stop if activation-calibrated SVD-residual q2 fails to improve perplexity degradation by at least 10% over direct q2 on GPT-2-small or if SVD storage/latency overhead exceeds the q3 baseline without quality benefit.

## Evidence references

- Artifact root: `<local-path>/projects/svd-residual-2-bit-principled-top-k-singular-channel-preservation-6f21b18e39db`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
