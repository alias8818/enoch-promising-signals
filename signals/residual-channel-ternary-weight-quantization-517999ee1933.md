# Residual-Channel Ternary Weight Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-ternary-weight-quantization-517999ee1933`
Run ID: `residual-channel-ternary-weight-quantization-517999ee1933-20260527T212131876374+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4b794cb3bc8e

## What looked useful

Raw weight-error residual-channel selection reduced weight MSE but did not materially beat random residual channels on accuracy and worsened cross-entropy. Activation-weighted channel selection gave small paired accuracy gains over ternary and random controls, suggesting any channel method likely needs data-aware importance.

## Boundaries and scale limits

No natural benchmark, transformer, GPT-2-small-class model, quantization-aware training, post-quantization fine-tuning, custom kernels, latency, or energy measurements. Results should not be generalized to large models or hardware deployment.

## Claim scope

Bounded local mechanism probe on five small MLP seeds trained on a deterministic teacher-generated 10-class classification task; post-training ternary quantization of linear weights with dense residual input-channel preservation.

## Why it stopped

Early bounded falsification of raw weight-error residual-channel selection as a standalone post-training ternary rule; activation-aware variant is promising but not paper-ready.

## Recommended next action

Stop this run as a no-paper useful signal; run one bounded deepen test on a real small benchmark with activation-aware channel residuals, random controls, and optional post-quantization fine-tuning.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-Aware Residual Channels for Ternary Quantization on a Real Small Benchmark
- Success threshold: Activation-weighted residual channels beat random residual channels by at least +1.0 percentage point mean accuracy or at least 5% relative loss reduction at one or more matched bit budgets, while preserving at least 5x weight compression.
- Stop condition: Stop if activation-weighted residual channels do not beat random-channel controls on the selected real benchmark at matched budgets, or if the result only improves weight MSE without improving task metrics.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-ternary-weight-quantization-517999ee1933`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
