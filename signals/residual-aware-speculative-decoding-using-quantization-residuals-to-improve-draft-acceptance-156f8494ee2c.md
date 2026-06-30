# Residual-Aware Speculative Decoding: Using Quantization Residuals to Improve Draft Acceptance

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `residual-aware-speculative-decoding-using-quantization-residuals-to-improve-draft-acceptance-156f8494ee2c`
Run ID: `residual-aware-speculative-decoding-using-quantization-residuals-to-improve-draft-acceptance-156f8494ee2c-20260524T031345599389+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/156899663d7c

## What looked useful

Top-k residual-row correction consistently improved acceptance while matched random residual-row correction had near-zero effect. For int4 output-head quantization, top-64 residual rows raised mean acceptance from 0.7903 to 0.9374 and reduced rejection by 70.15%; for int3, top-64 raised acceptance from 0.4741 to 0.7675.

## Boundaries and scale limits

This is an output-head-only proxy using shared target hidden states and exact residual rows. It does not validate a fully quantized draft transformer, autoregressive multi-token speculative decoding, throughput, kernel overhead, residual storage bandwidth, or robustness across datasets/models.

## Claim scope

On 168 Qwen/Qwen2.5-0.5B hidden positions, when the draft differs from the target only by row-wise symmetric output-head quantization, applying exact quantization residual dot products to draft top-k vocabulary rows substantially improves the theoretical speculative per-token acceptance probability sum_v min(p_target(v), q_draft(v)).

## Why it stopped

Closed as no-paper useful signal because the mechanism is supported only in an output-head proxy; full draft-model decoding and throughput evidence are still required.

## Recommended next action

Run a direct end-to-end speculative decoding follow-up with an independently quantized draft model, residual-aware proposal correction, accepted tokens per verifier call, and wall-clock tokens/sec.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-End Residual-Aware Speculative Decoding with a Quantized Draft Model
- Success threshold: Residual-aware correction improves accepted tokens per verifier call by at least 10% over the uncorrected quantized draft and does not reduce end-to-end tokens/sec by more than 5%; stronger success requires a net throughput improvement.
- Stop condition: Stop if acceptance gains are below 3% on two quantization settings or if residual correction overhead causes more than 10% lower tokens/sec than the uncorrected quantized draft.

## Evidence references

- Artifact root: `<local-path>/projects/residual-aware-speculative-decoding-using-quantization-residuals-to-improve-draft-acceptance-156`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
