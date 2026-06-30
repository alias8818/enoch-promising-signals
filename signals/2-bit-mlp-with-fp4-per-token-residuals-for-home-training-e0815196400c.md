# 2-bit MLP with FP4 per-token residuals for home training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-mlp-with-fp4-per-token-residuals-for-home-training-e0815196400c`
Run ID: `2-bit-mlp-with-fp4-per-token-residuals-for-home-training-e0815196400c-20260522T111005049152+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4286aa1c5b71

## What looked useful

The numeric repair channel is strong: medium probe relative MSE improved from 1.3143 for 2-bit-only MLP to 0.01574 with oracle FP4 per-token residuals, and cosine improved from 0.7092 to 0.99225. The same residual stream is not free: at 512 tokens it was 25.2% of compressed MLP weight bytes for the probe shape, and projections show it can exceed compressed MLP weight bytes at larger token counts.

## Boundaries and scale limits

No packed 2-bit kernels, end-to-end language model training, optimizer-state compression, or non-oracle residual generation were tested. Scaling projections cover memory formulas for GPT-2-small-class and small-1B-class MLP shapes rather than full training.

## Claim scope

Fake-quantized random MLP probes on GB10 show that oracle per-token FP4 output residuals can recover most dense-output error from 2-bit MLP weights, but only when the exact dense residual is available.

## Why it stopped

Proxy evidence supports FP4 residual numeric capacity but early-falsifies the idea as stated for home training because the tested residual requires dense-output access and creates a sizable per-token memory stream; this is not full validation.

## Recommended next action

Stop this run as a proxy useful signal; next test should replace the oracle dense residual with a cheap trainable residual predictor on a tiny LM and compare against dense and 2-bit-only controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trainable non-oracle FP4 residual path for 2-bit MLP toy language modeling
- Success threshold: 2-bit plus non-oracle FP4 residual recovers at least 50% of the validation-loss gap between 2-bit-only and dense while adding less than 25% memory overhead versus the compressed MLP path at the tested token budget.
- Stop condition: Stop if the non-oracle residual recovers less than 25% of the 2-bit loss gap after a calibrated short run, or if memory/throughput overhead exceeds the dense baseline at the target toy scale.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-mlp-with-fp4-per-token-residuals-for-home-training-e0815196400c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
