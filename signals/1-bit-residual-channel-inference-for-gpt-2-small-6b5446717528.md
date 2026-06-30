# 1-bit Residual-Channel Inference for GPT-2-Small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-bit-residual-channel-inference-for-gpt-2-small-6b5446717528`
Run ID: `1-bit-residual-channel-inference-for-gpt-2-small-6b5446717528-20260607T220345135708+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/291a0c948d7c

## What looked useful

Final residual sign quantization achieved PPL 84.9 vs dense 41.6 and random-sign 220k, with 59.8% dense top-1 agreement. Blockwise residual sign quantization collapsed to PPL 3,156 and 4.3% top-1 accuracy, though still above random-sign PPL 11,020, indicating information remains but is insufficient for drop-in GPT-2-small inference.

## Boundaries and scale limits

Evaluated pretrained GPT-2-small only, 8,192 calibration tokens and 32,768 evaluation targets from WikiText-2 validation, no quantization-aware training, no learned thresholds, no large-domain robustness, no hardware-native 1-bit kernel measurement.

## Claim scope

Bounded GPT-2-small inference probe: final normalized residual-channel signs retain substantial next-token signal, but forcing every post-block residual stream to 1-bit calibrated signs without retraining is not a viable drop-in inference method on WikiText-2 validation tokens.

## Why it stopped

Moderate direct inference evidence gives an early falsification of fixed-scale blockwise 1-bit residual-channel inference as a drop-in GPT-2-small method; this is not a full validation of trained 1-bit residual architectures.

## Recommended next action

Stop this run as a bounded no-paper result; only pursue a follow-up if it tests learned or quantization-aware 1-bit residual calibration rather than repeating fixed-scale sign replacement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned calibration for blockwise 1-bit GPT-2-small residual streams
- Success threshold: Learned-calibrated blockwise 1-bit residual inference reaches perplexity under 2x dense GPT-2-small on the same validation setup and dense top-1 agreement at or above 50%, while remaining clearly above random controls.
- Stop condition: Stop if learned calibration remains above 4x dense perplexity or below 25% dense top-1 agreement after a bounded calibration run, because fixed signs would still be too destructive for practical GPT-2-small inference.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-residual-channel-inference-for-gpt-2-small-6b5446717528`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
