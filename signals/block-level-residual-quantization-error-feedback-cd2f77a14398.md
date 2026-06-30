# Block-Level Residual Quantization Error Feedback

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `block-level-residual-quantization-error-feedback-cd2f77a14398`
Run ID: `block-level-residual-quantization-error-feedback-cd2f77a14398-20260526T071331045647+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/c5410934474a

## What looked useful

Residual feedback appears to exploit adjacent-block error cancellation when downstream weights preserve coherent block signs. A sign-alternating control removed the large gains, indicating the mechanism is conditional rather than a general block quantization improvement.

## Boundaries and scale limits

Tested only synthetic activation distributions and synthetic projection matrices at dimension 1024 with 8 seeds; no real transformer activations, trained weights, perplexity, task accuracy, latency, or quantized kernel implementation was evaluated.

## Claim scope

In a synthetic NumPy int4 blockwise activation-quantization benchmark, uncompensated residual feedback across contiguous blocks greatly reduced downstream matmul relative MSE for block-sum and block-smooth projections, but did not improve random projections and increased activation reconstruction error.

## Why it stopped

Closed as no-paper useful signal: the local evidence supports a narrow synthetic mechanism but is insufficient for a publication-grade claim.

## Recommended next action

Run a bounded transformer-layer replay using saved activations and weights from a small pretrained model, and compare layer output error plus perplexity against ordinary blockwise quantization.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer-Layer Replay for Residual Block Quantization Feedback
- Success threshold: Feedback must improve layer output relative MSE by at least 5% versus standard blockwise quantization on a majority of tested layers and not worsen validation perplexity by more than the standard quantization baseline.
- Stop condition: Stop if feedback fails to beat standard quantization on most replayed layers, if gains disappear under real trained weights, or if perplexity worsens beyond the standard baseline.

## Evidence references

- Artifact root: `<local-path>/projects/block-level-residual-quantization-error-feedback-cd2f77a14398`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
