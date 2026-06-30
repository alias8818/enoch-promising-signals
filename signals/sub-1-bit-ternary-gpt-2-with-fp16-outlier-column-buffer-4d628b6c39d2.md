# Sub-1-bit ternary GPT-2 with FP16 outlier column buffer

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `sub-1-bit-ternary-gpt-2-with-fp16-outlier-column-buffer-4d628b6c39d2`
Run ID: `sub-1-bit-ternary-gpt-2-with-fp16-outlier-column-buffer-4d628b6c39d2-20260630T102702999481+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b208dfad9bd4

## What looked useful

The mechanism has a real but small directional effect: increasing FP16 outlier columns reduced validation loss and reconstruction error at every tested threshold. However, the best under-1-bit aggressive setting tested was 0.936 effective bits/weight with validation loss 4.3412 versus dense 0.7234, so the sub-1-bit post-training variant is an early negative.

## Boundaries and scale limits

This run used a toy synthetic corpus, a 4-layer 128-hidden transformer, post-training quantization only, and dense embeddings/layer norms/biases/lm head. It did not test GPT-2-small/full-corpus training, quantization-aware training, custom kernels, inference throughput, or full-model compression.

## Claim scope

On a tiny GPT-2-style causal transformer trained on a deterministic synthetic byte language, post-training quantization of internal Linear weights to sub-1-bit sparse ternary symbols plus FP16 high-energy input-column buffers did not preserve validation loss. FP16 outlier columns monotonically helped, but not enough to make the sub-1-bit setting viable.

## Why it stopped

Proxy/local early falsification: direct toy GPT-style post-training sub-1-bit quantization failed to preserve loss even with FP16 outlier columns; this is not a full GPT-2-scale validation.

## Recommended next action

Stop this run as a no-paper useful negative; the one bounded next test is quantization-aware fine-tuning on the same harness to see whether the outlier-buffer mechanism can recover to within +0.30 validation loss at under 1 effective bit/weight.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantization-aware fine-tuning for sub-1-bit ternary GPT Linear layers with FP16 outlier columns
- Success threshold: Validation loss within +0.30 of dense at under 1.0 effective bits/weight for internal Linear weights, with ternary-plus-outlier beating ternary-only by at least 0.10 validation loss.
- Stop condition: Stop if quantization-aware fine-tuning remains more than +0.75 validation loss worse than dense after the bounded run, or if all under-1-bit variants fail to beat ternary-only by 0.10 validation loss.

## Evidence references

- Artifact root: `<local-path>/projects/sub-1-bit-ternary-gpt-2-with-fp16-outlier-column-buffer-4d628b6c39d2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
