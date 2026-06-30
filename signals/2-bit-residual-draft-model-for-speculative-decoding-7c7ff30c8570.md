# 2-bit+Residual Draft Model for Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-residual-draft-model-for-speculative-decoding-7c7ff30c8570`
Run ID: `2-bit-residual-draft-model-for-speculative-decoding-7c7ff30c8570-20260528T042653604211+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4a9b5300cb31

## What looked useful

Across five seeds, dense draft expected acceptance averaged 0.9542, plain 2-bit averaged 0.8761, and 2-bit plus residual averaged 0.9210. The residual recovered 57.4% +/- 1.2% of the plain 2-bit acceptance loss and 68.9% +/- 1.2% of the KL increase while estimated storage was 16.1% of dense versus 10.6% for plain 2-bit.

## Boundaries and scale limits

Evidence is limited to a small synthetic teacher, MLP drafts, one-token expected acceptance, and storage accounting estimates. It does not validate real LLM distributions, multi-token speculative decoding, natural-language corpora, quantized CUDA kernels, or end-to-end decode throughput.

## Claim scope

On a synthetic autoregressive teacher/draft distillation probe, frozen 2-bit draft weights plus trainable low-rank residual adapters consistently recover a majority of the one-token speculative acceptance and KL loss caused by plain 2-bit post-training quantization.

## Why it stopped

Closed as no-paper useful signal because this run is synthetic/proxy-only: it supports the mechanism but does not provide direct real-LM or end-to-end speculative decoding evidence.

## Recommended next action

Run a bounded GPT-2-small-class real-text follow-up comparing dense draft, plain 2-bit draft, and 2-bit plus residual draft on multi-token speculative acceptance and measured decode throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text GPT-2-small 2-bit residual draft speculative decoding probe
- Success threshold: 2-bit plus residual recovers at least 50% of the acceptance-rate loss from plain 2-bit versus dense and preserves at least 1.2x measured throughput advantage over teacher-only decoding in the bounded setup.
- Stop condition: Stop if residual recovery is below 25% of the plain 2-bit acceptance loss or if measured residual draft throughput is not faster than the dense draft/control path.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-residual-draft-model-for-speculative-decoding-7c7ff30c8570`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
