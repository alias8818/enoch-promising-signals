# Residual Channel Recovery for Sub-4-bit Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-recovery-for-sub-4-bit-quantization-995e3bfb396d`
Run ID: `residual-channel-recovery-for-sub-4-bit-quantization-995e3bfb396d-20260526T002721026467+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2f775d23480f

## What looked useful

Residual channel recovery removes most baseline output MSE when quantization error is channel-concentrated: for 2-bit base plus 6.25% residual channels, targeted recovery reduced MSE by 79.4% on heavy-tail and 84.9% on mixed-outlier regimes versus 5.8-6.1% for random channels. The same setting reduced only 10.7% on homogeneous channels. However, at matched approximate storage budget, 2-bit plus fp16 residual channels was worse than uniform 3-bit/4-bit quantization in most same-budget comparisons, and row-norm selection matched calibrated error selection, weakening the novelty/practicality claim.

## Boundaries and scale limits

No real transformer checkpoints, language-model perplexity, task accuracy, hardware kernels, activation quantization, or end-to-end serving throughput were tested. Residual storage was modeled as fp16 dense rows, so actual packing and runtime overhead remain unvalidated.

## Claim scope

Vectorized NumPy synthetic linear-layer PTQ proxy with 512x512 layers, Gaussian/correlated activations, 12 seeds, and homogeneous/heavy-tail/mixed-outlier channel scale regimes. Tested 2-bit and 3-bit per-row symmetric base quantization plus fp16 residual recovery for 1.56%, 3.12%, 6.25%, and 12.5% output channels.

## Why it stopped

Synthetic proxy supports the error-concentration mechanism but early-falsifies the stronger practical claim under fp16 residual-row accounting because uniform higher-bit quantization and simple row-norm channel selection are strong controls.

## Recommended next action

Stop as no-paper useful signal: do not claim RCR is a storage-competitive sub-4-bit method until a real small-transformer PTQ follow-up shows perplexity/accuracy gains over uniform and mixed-precision baselines at matched model size and runtime overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer PTQ residual-channel recovery with matched storage controls
- Success threshold: Activation-error-selected residual recovery beats both uniform same-budget quantization and row-norm mixed precision by at least 3% relative perplexity/loss degradation reduction on held-out data while keeping packed model size within 2% of the matched budget.
- Stop condition: Stop if calibrated RCR fails to beat uniform same-budget quantization or row-norm mixed precision on the first real small-transformer checkpoint, or if residual packing/runtime overhead removes the storage advantage.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-recovery-for-sub-4-bit-quantization-995e3bfb396d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
