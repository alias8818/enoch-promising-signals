# Residual-channel int2 quantization for GPT-2-small with calibrated deltas

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-int2-quantization-for-gpt-2-small-with-calibrated-deltas-9aaeaa3a1640`
Run ID: `residual-channel-int2-quantization-for-gpt-2-small-with-calibrated-deltas-9aaeaa3a1640-20260621T163745713724+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/408262a02f5a

## What looked useful

Best tested residual-channel variant, int2 plus int8 deltas on 10% of channels, reduced weighted NMSE from 0.695969 to 0.425798 but remained 16.45x worse than per-channel int4 NMSE 0.025880. Mean cosine improved from 0.803213 to 0.855331, versus int4 at 0.987777.

## Boundaries and scale limits

Weight reconstruction only over 48 GPT-2-small projection matrices; no embeddings in the main claim, no activation calibration, no forward passes, no perplexity, no generation quality, and no optimized inference kernel.

## Claim scope

On real GPT-2-small projection weights, per-channel int2 quantization with calibrated scalar or sparse int8 residual-channel deltas improves weight reconstruction monotonically, but the tested residual budgets do not approach a simple per-channel int4 reconstruction baseline.

## Why it stopped

Early direct weight-reconstruction test produced a useful mechanism signal but not paper-ready evidence; the result is a proxy for model quality rather than a full validation.

## Recommended next action

Run a bounded activation-aware GPT-2-small perplexity/logit-KL follow-up comparing residual-channel int2 against int4 and fp16 on a small calibration/evaluation corpus; stop if 10% residual channels remain far worse than int4.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware GPT-2-small perplexity check for residual-channel int2 deltas
- Success threshold: At 10% residual-channel budget, int2 residual-channel perplexity degradation and logit KL should be no more than 25% worse than the int4 baseline degradation while retaining at least 5x estimated compression versus fp16.
- Stop condition: Stop as non-viable if activation-aware 10% residual-channel int2 remains more than 2x worse than int4 by perplexity degradation or logit KL on the bounded corpus.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-int2-quantization-for-gpt-2-small-with-calibrated-deltas-9aaeaa3a1640`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
