# Residual-Channel Extreme Quantization: 1.58-bit weights with learned error-carrying channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-extreme-quantization-1-58-bit-weights-with-learned-error-carrying-channels-6e9954723282`
Run ID: `residual-channel-extreme-quantization-1-58-bit-weights-with-learned-error-carrying-channels-6e9954723282-20260523T032304362113+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/04a78b00adbd

## What looked useful

Ranked residual channels improved monotonically over ternary-only in both reconstruction error and synthetic classification accuracy. Best rank-8 residual model reached 94.3% train and 56.7% test accuracy versus ternary-only 82.4% train and 52.7% test at about 4.565 effective bits per dense weight, but dense FP16 still led with 100% train and 60.1% test.

## Boundaries and scale limits

Only synthetic Gaussian teacher-student classification and analytic 128 x 128 matrix reconstruction were tested. No real language model, transformer block, tokenizer dataset, fused kernel, latency, or large-scale training evidence was produced.

## Claim scope

Bounded synthetic evidence: low-rank learned residual channels can carry some quantization error for 1.58-bit ternary linear layers and improve small teacher-student MLP capacity over ternary-only weights.

## Why it stopped

No-paper closure: this run produced useful bounded synthetic support for the mechanism, but it is not direct language-model evidence and does not close the dense-performance gap.

## Recommended next action

Run a bounded real small-language-model follow-up comparing dense, ternary-only, and residual-channel quantized transformer blocks under matched bit budgets before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-channel ternary quantization on a small transformer language model
- Success threshold: Residual-channel model improves validation perplexity by at least 5% relative to ternary-only at no more than one third of dense FP16 effective weight bits, with consistent direction across repeated runs.
- Stop condition: Stop if residual-channel variants fail to beat ternary-only validation perplexity by 2% at matched bit budget, or if the required residual rank exceeds one third of dense FP16 effective weight bits.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-extreme-quantization-1-58-bit-weights-with-learned-error-carrying-channels-6e99`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
