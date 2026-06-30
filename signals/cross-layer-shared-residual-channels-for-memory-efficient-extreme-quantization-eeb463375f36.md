# Cross-Layer Shared Residual Channels for Memory-Efficient Extreme Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cross-layer-shared-residual-channels-for-memory-efficient-extreme-quantization-eeb463375f36`
Run ID: `cross-layer-shared-residual-channels-for-memory-efficient-extreme-quantization-eeb463375f36-20260529T044625462342+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/bab3238b6373

## What looked useful

Shared residual channels appear to offer a real memory/error tradeoff for repeated Transformer weight shapes, but the decorrelated synthetic control also performed well and one rank-16 real-weight group missed the 10% parity threshold, so the mechanism is useful but not yet a paper-ready end-to-end quantization result.

## Boundaries and scale limits

Evidence is limited to post-training weight reconstruction and random Gaussian linear-output probes on DistilGPT-2 plus synthetic controls. It does not include perplexity, task accuracy, calibration activations, fused kernels, larger models, or comparisons with production quantization methods.

## Claim scope

For same-shaped DistilGPT-2 layer weight groups under INT2 per-row quantization, a shared rank-r residual basis plus per-layer coefficients reduced correction-parameter count by 43.1% on average while keeping reconstruction and random-linear activation error about 5% above independent per-layer residual bases across ranks 4, 8, and 16; 8 of 9 group/rank probes were within a 10% error-parity threshold.

## Why it stopped

Stopped with a proxy-level useful signal: local evidence supports the memory/error mechanism, but full validation requires real activation or perplexity evidence rather than only weight and random-linear reconstruction.

## Recommended next action

Run a bounded deepen test that injects shared residual corrections into DistilGPT-2 inference and measures perplexity against INT2-only and independent residual correction at matched memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Perplexity validation for shared residual channels in INT2 DistilGPT-2
- Success threshold: Shared residual correction must be within 1% relative perplexity of independent residual correction at the same or lower correction memory and must improve over INT2-only by at least 5% relative perplexity.
- Stop condition: Stop if shared correction is worse than independent residual correction by more than 3% relative perplexity at matched memory or fails to improve over INT2-only by at least 2%.

## Evidence references

- Artifact root: `<local-path>/projects/cross-layer-shared-residual-channels-for-memory-efficient-extreme-quantization-eeb463375f36`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
