# Dynamic 2-Bit Quantized Draft for Speculative Decoding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `dynamic-2-bit-quantized-draft-for-speculative-decoding-13c60b0590ec`
Run ID: `dynamic-2-bit-quantized-draft-for-speculative-decoding-13c60b0590ec-20260526T023921574044+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2d456810f23e

## What looked useful

The tested 2-bit draft collapses the next-token distribution and predicts sub-1x speculative speedup even under an optimistic 10% draft-cost assumption, while an 8-bit control in the same harness reaches 0.9837 acceptance. This is useful no-paper evidence against naive per-output affine 2-bit drafts.

## Boundaries and scale limits

Single pretrained distilgpt2 model; 64 contexts; simulated quantize-dequantize weights, not packed 2-bit kernels; no quantization-aware training, learned codebooks, activation-aware calibration, larger target models, or production serving measurements.

## Claim scope

On distilgpt2 with 64 Wikitext validation contexts, simulated per-output affine 2-bit quantization of GPT-2 Conv1D/Linear draft weights does not preserve enough next-token distribution fidelity for speculative decoding; sampled acceptance was 0.0213 when quantizing all such weights and 0.0166 when leaving the tied lm_head/embedding full precision.

## Why it stopped

Proxy-limited but direct early falsification of simple simulated 2-bit affine draft quantization, not a full validation against all possible 2-bit draft methods.

## Recommended next action

Stop this run; if continuing the line, run a bounded deepen test with quantization-aware or activation-aware 2-bit draft calibration and require acceptance high enough to predict >1x speedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware or QAT 2-bit draft recovery test
- Success threshold: Sampled acceptance >= 0.50 and predicted speculative speedup > 1.0x at draft cost ratio 0.25, with KL reduced by at least 5x versus naive 2-bit affine quantization.
- Stop condition: Stop if acceptance remains below 0.25 after activation-aware calibration or QAT on the bounded model, because verifier rejection will dominate any plausible 2-bit kernel gain.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-2-bit-quantized-draft-for-speculative-decoding-13c60b0590ec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
