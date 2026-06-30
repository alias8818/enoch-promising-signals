# Extreme Quantization with Principled Residual Channels: Small Model Proof

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `extreme-quantization-with-principled-residual-channels-small-model-proof-6023fd048445`
Run ID: `extreme-quantization-with-principled-residual-channels-small-model-proof-6023fd048445-20260611T114321223495+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/749fa37361d0

## What looked useful

Principled residual channels produced consistent paired wins for 1-bit quantization across all 9 seed/fraction comparisons, with mean random-minus-principled validation loss improvements of 0.0128, 0.0210, and 0.0312 at 1%, 2%, and 5% residual budgets. The best 2-bit condition was 5% principled residual channels with mean validation loss 2.3957 versus 2.4293 for 2-bit no-residual, but all quantized variants remained materially worse than dense FP32 mean validation loss 2.0521.

## Boundaries and scale limits

This is a small proxy experiment, not GPT-2-small-class or pretrained LLM evidence. It does not validate subword tokenization, large-corpus training, quantization-aware recovery, inference kernels, memory bandwidth savings, or large-model perplexity retention.

## Claim scope

In a 431k-parameter character-level Tiny Shakespeare transformer trained for 1000 steps across three seeds, activation-error selected full-precision residual input channels improved post-training 1-bit linear-weight quantization over equal-budget random residual channels at 1%, 2%, and 5% channel budgets, and improved 2-bit quantization most clearly at a 5% residual budget.

## Why it stopped

Closed as no-paper useful signal because the run supports the residual-channel selection mechanism only on a small proxy model and does not provide direct publication-grade evidence for extreme quantization of practical language models.

## Recommended next action

Run a bounded GPT-2-small-class or pretrained-small-LM perplexity follow-up with matched effective-bit controls and random-channel baselines before considering paper framing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class residual-channel quantization confirmation
- Success threshold: At matched effective-bit budget, principled residual channels reduce perplexity degradation by at least 10% relative to random residual channels for both 1-bit and 2-bit quantization, while retaining a meaningful compression ratio and without material inference slowdown.
- Stop condition: Stop if principled residual channels fail to beat random residual channels on GPT-2-small-class perplexity in at least two independent seeds or if the residual implementation removes the practical compression/latency benefit.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-quantization-with-principled-residual-channels-small-model-proof-6023fd048445`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
