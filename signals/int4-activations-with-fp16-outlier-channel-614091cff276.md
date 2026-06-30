# INT4 activations with FP16 outlier channel

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int4-activations-with-fp16-outlier-channel-614091cff276`
Run ID: `int4-activations-with-fp16-outlier-channel-614091cff276-20260628T204050048888+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ba6eef76f325

## What looked useful

At 28.8% of FP16 activation storage, keeping 5% of channels in FP16 reduced downstream matmul relative RMSE by 85.5% for fixed sparse channel outliers, but only 3.0% for normal activations, 4.7% for Student-t heavy-tailed activations, and 4.1% for rare element-wise spikes.

## Boundaries and scale limits

Tested CPU-only synthetic activation matrices up to 4096x1024 with 256-output dense projections. No real transformer activation traces, fused kernels, end-task accuracy, serving latency, or GPU/memory-bandwidth measurements were produced.

## Claim scope

Synthetic NumPy activation probes show that INT4 activations with globally selected FP16 outlier channels can substantially reduce reconstruction and downstream dense-matmul error when outliers are persistent by channel, but not when activations are homogeneous, broadly heavy-tailed, or dominated by rare element-wise spikes.

## Why it stopped

Synthetic/proxy evidence is mixed: the mechanism works for stable channel outliers but does not generalize across tested activation regimes, so this is not a full validation or paper-ready result.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should replay the same scheme on GPT-2-small-class layer activation traces and compare against standard per-token/per-channel activation quantization controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Validate FP16 outlier channels on real transformer activation traces
- Success threshold: At least half of measured transformer layers show >=50% downstream output relative-RMSE reduction versus INT4-only while staying <=30% of FP16 activation storage, with selected outlier channels stable between calibration and evaluation samples.
- Stop condition: Stop if fewer than half of layers meet the error-reduction threshold or if selected outlier channels are not stable across calibration and evaluation samples.

## Evidence references

- Artifact root: `<local-path>/projects/int4-activations-with-fp16-outlier-channel-614091cff276`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
