# Ternary-Weight Transformer with FP8 Residual Outlier Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-weight-transformer-with-fp8-residual-outlier-channels-8abf63e3e7aa`
Run ID: `ternary-weight-transformer-with-fp8-residual-outlier-channels-8abf63e3e7aa-20260629T005739344625+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/640fda8882d3

## What looked useful

At 12.5% FP8 residual-row budget, validation loss improved from 2.8554 for ternary-only to 2.7294, but dense was 1.9725. Even 50% residual rows left validation loss at 2.4038 while reducing estimated compression to 5.15x. The residual mechanism helps monotonically but is too weak as a naive post-training scheme.

## Boundaries and scale limits

No GPT-2-small-class or larger run, no quantization-aware training, no fused ternary/FP8 kernel, no activation quantization, and no downstream benchmarks. Throughput numbers are dequantized PyTorch evaluation proxies, not hardware-realized ternary/FP8 speed.

## Claim scope

Small-scale post-training probe on a 4-layer, 128-dimension character-level Transformer trained on Tiny Shakespeare: ternary weights plus FP8 residual outlier output rows improve over ternary-only weights but remain far worse than dense at practical residual budgets.

## Why it stopped

Early direct small-model falsification of the naive post-training form, not a full validation of all ternary/FP8 training variants.

## Recommended next action

Stop this run as a no-paper useful signal; only pursue a bounded follow-up if it changes the method to quantization-aware training or a stronger residual selection/control baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantization-aware ternary plus FP8 residual rows on the same small Transformer probe
- Success threshold: At 12.5% or lower FP8 residual-row budget, ternary+FP8 QAT reaches within +0.10 validation loss of dense and beats ternary-only QAT by at least 50% of the dense-gap reduction while preserving at least 8x estimated weight-storage compression.
- Stop condition: Stop if QAT ternary+FP8 remains more than +0.25 validation loss worse than dense at 12.5% residual rows or does not beat ternary-only QAT by at least +0.05 validation loss.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-weight-transformer-with-fp8-residual-outlier-channels-8abf63e3e7aa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
