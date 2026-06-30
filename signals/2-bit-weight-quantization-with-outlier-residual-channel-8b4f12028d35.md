# 2-bit Weight Quantization with Outlier Residual Channel

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-weight-quantization-with-outlier-residual-channel-8b4f12028d35`
Run ID: `2-bit-weight-quantization-with-outlier-residual-channel-8b4f12028d35-20260620T115049793864+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/40b7dd73fddc

## What looked useful

Outlier residual channels are a real mechanism in this probe: at 4% restored channels, loss improved from 35.95 to 23.52 while random restoration stayed at 37.12; at 16%, outlier loss was 20.52 versus random 34.48. However, full precision loss was 3.89, so the simple method remains far from viable.

## Boundaries and scale limits

Single pretrained GPT-2-small model, post-training weight-only quantization, 128 validation batches at sequence length 128, no activation-aware calibration, no custom kernels, no larger-model or downstream-task validation.

## Claim scope

On pretrained GPT-2-small, restoring high-residual input channels after naive per-output-channel 2-bit affine quantization of attention/MLP weights improves reconstruction error and bounded WikiText-2 proxy loss more than random channel restoration at the same effective-bit overhead, but does not recover usable language-model quality.

## Why it stopped

Bounded proxy evidence supports the outlier-channel mechanism but early-falsifies the practical viability of naive 2-bit affine quantization plus sparse residual channels at the tested overheads; this is not full-scale validation.

## Recommended next action

Stop this simple naive-2-bit path as no-paper evidence; the only worthwhile next bounded action is a calibrated activation-aware/GPTQ-style 2-bit plus outlier-residual comparison against a 4-bit baseline on GPT-2-small or OPT-125M.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware 2-bit quantization with outlier residual channels
- Success threshold: At an effective storage budget below the matched 4-bit baseline, activation-aware 2-bit plus outlier residual should reduce perplexity to within 15% of the 4-bit baseline and outperform random residual restoration by at least 10% relative loss reduction.
- Stop condition: Stop if activation-aware 2-bit plus outlier residual remains more than 50% worse in perplexity than the 4-bit baseline at any storage budget below or equal to 4 effective bits, or if random residual restoration matches the outlier strategy.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-weight-quantization-with-outlier-residual-channel-8b4f12028d35`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
