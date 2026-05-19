# Ternary Weights Plus Per-Layer Residual Codebook Recovery

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `83`
Project ID: `ternary-weights-plus-per-layer-residual-codebook-recovery-71052a960214`
Run ID: `ternary-weights-plus-per-layer-residual-codebook-recovery-71052a960214-20260513T205938482301+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/42a66111ca4c

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Proxy/direct small-model evidence only: ternary plus a K=16 residual codebook reduced GPT-2 WikiText-2 loss damage from +9.17685 to +1.69712 nats over 262144 tokens, but this is not full validation or publication-grade evidence.

## Recommended next action

Stop this run as no-paper: the GPT-2 proxy supports residual-codebook recovery but lacks strong PTQ baselines, encoded inference validation, and robustness evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Matched-bit GPT-2 residual-codebook quantization against strong PTQ baselines
- Success threshold: At matched effective <=6 bits/weight, residual-codebook quantization is within 10% relative perplexity of the best strong PTQ baseline and has an encoded inference prototype with lower memory footprint than dense FP16 without >25% latency regression on GB10.
- Stop condition: Stop if strong PTQ baselines beat residual-codebook quantization by more than 10% relative perplexity at matched bits or if the encoded inference path loses the expected memory/latency advantage.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-weights-plus-per-layer-residual-codebook-recovery-71052a960214`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
