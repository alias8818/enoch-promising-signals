# Principled Mixed-Precision Quantization: Residual INT4 + Attention INT8 vs Uniform Baselines

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `principled-mixed-precision-quantization-residual-int4-attention-int8-vs-uniform-baselines-4bb4758225de`
Run ID: `principled-mixed-precision-quantization-residual-int4-attention-int8-vs-uniform-baselines-4bb4758225de-20260614T000335003790+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/55c904e84fe4

## What looked useful

Across two architectures, attention-output INT4 caused modest degradation while residual-boundary INT4 caused large degradation. Proposed residual INT4 + attention INT8 beat uniform INT4 but remained 14x to 77x worse in perplexity ratio than FP, while the inverted residual INT8 + attention INT4 stayed near 1.2x to 1.5x.

## Boundaries and scale limits

Post-training fake quantization only; 32,640 WikiText-2 next-token positions per model; two small pretrained causal LMs; no packed integer kernels, latency validation, outlier-aware calibration, learned rotations, QAT, KV-cache study, or large-model validation.

## Claim scope

On GPT-2 and Pythia-70M WikiText-2 fake-quantized inference, naive per-token residual-boundary INT4 plus attention-output INT8 is not competitive with uniform INT8 or the inverted residual INT8 plus attention INT4 assignment; residual-boundary INT4 is the dominant source of perplexity collapse.

## Why it stopped

Early proxy falsification rather than full validation: direct small-model perplexity evidence shows residual INT4 is the harmful component under the tested quantizer, so the proposed residual INT4 + attention INT8 principle is unsupported.

## Recommended next action

Stop this assignment as a paper candidate; run a bounded follow-up that protects residuals at INT8 and tests whether attention outputs can be pushed to INT4 with calibration against same-budget baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-preserving mixed precision: residual INT8 with attention INT4
- Success threshold: Residual INT8 + attention INT4 stays within 10% perplexity of uniform INT8 on every tested model/dataset and beats residual INT4 + attention INT8 by at least 25% relative perplexity on every tested model/dataset.
- Stop condition: Stop if residual INT8 + attention INT4 exceeds 1.25x uniform INT8 perplexity on two models or fails to beat residual INT4 + attention INT8 after calibration.

## Evidence references

- Artifact root: `<local-path>/projects/principled-mixed-precision-quantization-residual-int4-attention-int8-vs-uniform-baselines-4bb475`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
