# Outlier-Aware 4-bit Weight-Only Quant on GPT-2-Small

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `outlier-aware-4-bit-weight-only-quant-on-gpt-2-small-240d984ab9d6`
Run ID: `outlier-aware-4-bit-weight-only-quant-on-gpt-2-small-240d984ab9d6-20260629T220208679674+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6c14b3140ece

## What looked useful

Outlier-aware residual preservation consistently improved W4 GPT-2-small loss across smoke, medium, and near-full validation runs: near-full loss deltas were +0.3934 for standard W4 and +0.1941 for outlier-aware W4 versus fp, with weighted relative reconstruction MSE falling from 0.03413 to 0.01824.

## Boundaries and scale limits

Single model, single validation dataset, one outlier fraction, dequantized-weight evaluation only, no packed int4+sparse-residual kernel, no latency or bandwidth measurement, embeddings/layer norms/tied lm_head excluded.

## Claim scope

On GPT-2-small projection and MLP weights evaluated on 230,400 WikiText-2 validation tokens, preserving the top 0.2% absolute weights per output channel as exact residuals reduced the standard per-channel W4 loss penalty by about 50.7% while retaining an estimated 3.91x fp16 storage compression for targeted weights.

## Why it stopped

The result directly supports the scoped mechanism but is not publication-grade because runtime, packed storage behavior, robustness, and ablations were not tested.

## Recommended next action

Stop this run as no-paper useful evidence; next run should perform a bounded outlier-density and target-tensor sweep plus at least one practical packed-kernel feasibility check before any paper decision.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Outlier-density Pareto sweep and packed-kernel feasibility for GPT-2-small W4 residual quantization
- Success threshold: At least one configuration below 1% residual density recovers at least 45% of the standard W4 loss penalty on full validation, keeps estimated targeted-weight compression at or above 3.7x versus fp16, and shows metadata/decode overhead small enough to plausibly preserve a serving memory benefit.
- Stop condition: Stop if no tested density recovers at least 30% of the W4 loss penalty, or if packed residual metadata/decode overhead eliminates the practical storage or latency advantage.

## Evidence references

- Artifact root: `<local-path>/projects/outlier-aware-4-bit-weight-only-quant-on-gpt-2-small-240d984ab9d6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
