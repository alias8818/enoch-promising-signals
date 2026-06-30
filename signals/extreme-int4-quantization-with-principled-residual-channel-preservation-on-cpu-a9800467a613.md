# Extreme INT4 Quantization with Principled Residual Channel Preservation on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `extreme-int4-quantization-with-principled-residual-channel-preservation-on-cpu-a9800467a613`
Run ID: `extreme-int4-quantization-with-principled-residual-channel-preservation-on-cpu-a9800467a613-20260611T000701951757+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/1d429d1ca879

## What looked useful

On five synthetic 768-class transformer linear cases, preserving 1% of channels retained about 7.31x estimated compression versus FP32. Activation-variance selection reduced INT4 relative output MSE by about 37.86% on heavy-tail cases and 40.38% on an activation-only outlier case, while random residual selection was about 0.65% and 0.63% respectively. On Gaussian cases, 1% preservation reduced MSE by only about 1.17%, close to random.

## Boundaries and scale limits

No pretrained model, perplexity, task accuracy, packed INT4 kernel, or end-to-end latency evidence was produced. The benchmark used synthetic activations/weights and dequantized NumPy matmul, so claims are limited to layer-level output-error mechanics and analytical storage estimates.

## Claim scope

Synthetic transformer-shaped linear layers on a CPU worker: preserving 1% of input channels as a full-precision residual after row-wise symmetric INT4 quantization substantially reduces relative output MSE when quantization error is concentrated in high-variance or high-weight outlier channels, but provides only marginal benefit on isotropic Gaussian layers.

## Why it stopped

The local synthetic benchmark supports the residual-channel mechanism in outlier regimes but is not direct full-model evidence and is not paper-ready.

## Recommended next action

Run a bounded real-model follow-up on a small pretrained transformer: calibrate activation variance on held-out text, apply simulated INT4 plus residual channels to linear layers, and compare perplexity, memory, and CPU latency against row-wise INT4, random residuals, and an outlier-preserving baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Small-Transformer Validation of Activation-Variance Residual Channels for INT4 CPU Quantization
- Success threshold: At 1% preserved channels, activation-variance residual INT4 recovers at least 25% of the row-wise INT4 perplexity degradation versus FP32 and beats random residual preservation by at least 10 percentage points at comparable memory.
- Stop condition: Stop if activation-variance residual preservation does not beat random preservation on perplexity recovery at 1% and 2% preserved channels, or if CPU latency overhead exceeds 25% for the residual path without a commensurate perplexity gain.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-int4-quantization-with-principled-residual-channel-preservation-on-cpu-a9800467a613`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
