# 4-bit weight-only quantization with learned residual channels for GPT-2-small

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `4-bit-weight-only-quantization-with-learned-residual-channels-for-gpt-2-small-80f9ae9d287c`
Run ID: `4-bit-weight-only-quantization-with-learned-residual-channels-for-gpt-2-small-80f9ae9d287c-20260605T144805305132+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/eafddd5fee48

## What looked useful

Naive learned residual channels improved weight reconstruction but did not materially repair language-model loss. 4-bit groupwise quantization added +0.1636 loss versus FP32; 16 residual channels worsened loss by 0.0026 versus int4, and 64 residual channels recovered only 0.00145 loss while raising estimated storage to 5.03 bits per quantized parameter.

## Boundaries and scale limits

Fixed text rather than a standard validation corpus; embeddings and LM head were not quantized; residual channels were selected from weight error rather than activation/task loss; no integer kernel or runtime benefit was measured; single seed and small token count.

## Claim scope

Bounded GPT-2-small CPU probe on 2048 fixed-text tokens: symmetric 4-bit groupwise quantization of transformer projection/MLP weights, with residual channels selected by per-channel quantization-error energy and evaluated folded into dense weights.

## Why it stopped

Early bounded direct GPT-2-small probe found that weight-error-selected residual channels fail to recover the 4-bit task-loss regression; this is not a full validation of all residual-channel methods.

## Recommended next action

Stop this run as a no-paper useful negative signal; the next bounded test should use activation-aware residual-channel training on WikiText-2 and require storage-normalized loss recovery.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware residual-channel selection for GPT-2-small 4-bit quantization
- Success threshold: Recover at least 25% of the int4 loss delta versus FP32 on a standard validation split while staying at or below 5.1 effective bits per quantized parameter.
- Stop condition: Stop if activation-aware residual channels recover less than 10% of the int4 loss penalty at 5.1 effective bits or if they underperform a simple storage-matched baseline.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-weight-only-quantization-with-learned-residual-channels-for-gpt-2-small-80f9ae9d287c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
