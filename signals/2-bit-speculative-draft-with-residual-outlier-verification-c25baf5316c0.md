# 2-Bit Speculative Draft with Residual Outlier Verification

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `2-bit-speculative-draft-with-residual-outlier-verification-c25baf5316c0`
Run ID: `2-bit-speculative-draft-with-residual-outlier-verification-c25baf5316c0-20260601T065821063867+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8740107b585d

## What looked useful

The 2-bit residual-outlier mechanism failed the bounded acceptance probe, while the same harness produced strong 4-bit controls: 4-bit top-128 reached 0.9494 mean single-token acceptance and 0.8126 approximate four-token all-accept probability.

## Boundaries and scale limits

Proxy-only distribution-fidelity test; no separately trained draft model, no kernel implementation, no end-to-end speculative decoding latency measurement, fixed prompt suite rather than a standard corpus, and independent gamma=4 acceptance approximation rather than measured multi-token draft chains.

## Claim scope

On 256 distilgpt2 next-token contexts, uniform affine 2-bit quantization of non-outlier logits with exact top-k residual logits is too lossy for high speculative acceptance: top-128 residuals reached 0.6129 mean single-token acceptance and top-512 reached 0.7544.

## Why it stopped

Early proxy falsification rather than full validation: the tested 2-bit residual distribution did not reach plausible acceptance levels, and stronger evidence would require an actual low-cost draft implementation with measured end-to-end speedup.

## Recommended next action

Stop the 2-bit uniform-quantized variant as an early proxy falsification; run a bounded end-to-end 4-bit residual speculative decoding branch if continuing this line.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: 4-bit residual speculative draft end-to-end probe
- Success threshold: Mean single-token acceptance >= 0.90, measured four-token draft all-accept probability >= 0.70, and end-to-end tokens/sec at least 1.2x over the non-speculative target baseline on the same hardware.
- Stop condition: Stop if the implemented 4-bit path cannot exceed 0.85 mean acceptance or fails to produce any end-to-end throughput gain after accounting for residual verification overhead.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-speculative-draft-with-residual-outlier-verification-c25baf5316c0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
