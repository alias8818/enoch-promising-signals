# Residual-Ternary Draft Model for Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-ternary-draft-model-for-speculative-decoding-a7cde9543c25`
Run ID: `residual-ternary-draft-model-for-speculative-decoding-a7cde9543c25-20260527T213413213314+0000`

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

Residual-ternary storage and acceptance are promising in a bounded proxy, but naive execution is too slow for speculative decoding; future value depends on a custom inference kernel or runtime that converts the storage advantage into latency advantage.

## Boundaries and scale limits

The target was a frozen synthetic teacher, not a trained production language model; the ternary path used ordinary PyTorch operations rather than a packed/fused ternary inference kernel; no real serving stack, tokenizer, cache, or 7B+ target model was tested.

## Claim scope

In a self-contained synthetic autoregressive-teacher probe on NVIDIA GB10, a residual-ternary draft matched dense-draft speculative acceptance within about 0.3 percentage points on average and used about 28% of the dense fp16 storage, but the stock PyTorch implementation ran at only about 19% of dense-draft throughput.

## Why it stopped

Proxy/local evidence is mixed: acceptance and storage support the mechanism, but measured stock PyTorch throughput directly falsifies practical speculative-decoding viability for this implementation; this is not a full validation on real language models.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should implement a packed/fused residual-ternary linear kernel and require throughput parity with the dense draft before any real-LM validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed residual-ternary draft kernel throughput gate
- Success threshold: Residual-ternary draft throughput is at least 1.0x dense-draft throughput, acceptance is no more than 1 percentage point below dense draft, and effective storage remains at or below 35% of dense fp16 storage across five seeds.
- Stop condition: Stop if fused residual-ternary throughput remains below 0.8x dense-draft throughput or acceptance drops more than 2 percentage points versus dense draft.

## Evidence references

- Artifact root: `<local-path>/projects/residual-ternary-draft-model-for-speculative-decoding-a7cde9543c25`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
