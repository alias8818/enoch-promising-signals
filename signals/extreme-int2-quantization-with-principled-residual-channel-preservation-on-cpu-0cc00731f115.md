# Extreme INT2 Quantization with Principled Residual Channel Preservation on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `extreme-int2-quantization-with-principled-residual-channel-preservation-on-cpu-0cc00731f115`
Run ID: `extreme-int2-quantization-with-principled-residual-channel-preservation-on-cpu-0cc00731f115-20260613T223039853441+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/74ea33d242ca

## What looked useful

A quantization-error-based residual-channel score nearly matched an oracle row-error selector and outperformed random selection across normal, outlier-row, and low-rank spiky synthetic matrices. At 5% preserved channels, relative output-MSE reductions versus pure INT2 were 0.0748 normal, 0.6389 outlier_rows, and 0.0746 low_rank_spiky.

## Boundaries and scale limits

Evidence is synthetic and reconstruction-only. It does not test real transformer weights, real calibration activations, packed INT2 CPU kernels, perplexity, memory bandwidth, or end-to-end inference latency.

## Claim scope

On synthetic 768 x 768 CPU linear reconstruction probes, preserving 1-10% of output channels selected by activation-weighted INT2 quantization error consistently reduces output MSE versus pure INT2 and beats random residual-channel selection.

## Why it stopped

The run produced useful synthetic reconstruction evidence, but it is proxy-only and not sufficient for a paper or a full CPU INT2 inference claim.

## Recommended next action

Run a bounded direct follow-up on real transformer linear layers with calibration activations, packed INT2 plus residual FP16/FP32 channels, and paired perplexity/error plus CPU throughput metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-layer INT2 residual-channel preservation with packed CPU kernels
- Success threshold: At 2-5% preserved channels, activation MSE or perplexity degradation improves by at least 25% versus random residual selection at equal preserved-byte budget, while packed CPU throughput remains meaningfully better than full FP16/FP32.
- Stop condition: Stop if targeted residual selection fails to beat random by 10% on real-layer metrics at equal byte budget, or if packed residual handling removes the CPU throughput advantage.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-int2-quantization-with-principled-residual-channel-preservation-on-cpu-0cc00731f115`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
