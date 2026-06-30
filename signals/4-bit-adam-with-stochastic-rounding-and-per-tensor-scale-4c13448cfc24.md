# 4-bit Adam with Stochastic Rounding and Per-Tensor Scale

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `4-bit-adam-with-stochastic-rounding-and-per-tensor-scale-4c13448cfc24`
Run ID: `4-bit-adam-with-stochastic-rounding-and-per-tensor-scale-4c13448cfc24-20260629T212426734400+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6f5c6116a70f

## What looked useful

FP32 AdamW completed all seeds at lr 6e-4, 3e-4, and 1e-4. Both 4-bit nearest and 4-bit stochastic variants ended with non-finite weights in every seed at all three learning rates. The 4-bit variants used about 0.125x the estimated persistent optimizer-state memory, but second-moment zero-code rates were very high in the primary run: about 0.934 for nearest and 0.898 for stochastic. This supports the mechanism that per-tensor 4-bit scaling under-resolves v, making Adam denominators too small and causing divergence.

## Boundaries and scale limits

Synthetic task only; 2-layer 128-wide transformer; 260 training steps; three seeds; no real corpus, LLM-scale model, fused optimizer kernel, distributed training, or long-run validation. This is a bounded early falsification of the plain per-tensor scheme, not a full low-bit optimizer survey.

## Claim scope

On a tiny CUDA-trained causal transformer arithmetic-sequence benchmark, a plain AdamW variant that stores m and v as packed 4-bit values with one scale per parameter tensor did not remain stable under matched hyperparameters. Stochastic rounding reduced unchanged-state rates versus nearest rounding but did not prevent divergence.

## Why it stopped

Bounded proxy/early falsification: the direct local training test found repeatable divergence of the plain per-tensor 4-bit optimizer across three learning rates while FP32 AdamW controls completed.

## Recommended next action

Stop pursuing the plain per-tensor-scale 4-bit AdamW scheme as a paper candidate; the next bounded test should replace per-tensor v scaling with block-wise or logarithmic v quantization and require all seeds to complete without non-finite weights.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Block-wise or logarithmic second-moment scaling for 4-bit AdamW
- Success threshold: Modified 4-bit variant completes all 3 seeds for 260 steps with finite weights, mean final validation loss within 0.3 of FP32 AdamW at the same learning rate, and mean v zero-code rate below 0.5 while retaining at least 4x estimated optimizer-state memory reduction.
- Stop condition: Stop if the modified variant diverges in any seed at both lr 6e-4 and 3e-4, or if v zero-code rate remains above 0.8 after the scaling change.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-adam-with-stochastic-rounding-and-per-tensor-scale-4c13448cfc24`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
