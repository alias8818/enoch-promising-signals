# Real-LM Quantized Residual Draft for GPT-2-Small Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-lm-quantized-residual-draft-for-gpt-2-small-speculati-c0c6b4ea13`
Run ID: `real-lm-quantized-residual-draft-for-gpt-2-small-speculati-c0c6b4ea13-20260522T162324128802+0000`

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

- Parent run decision: Quantized Residual Draft Model for Speculative Decoding: enoch://control-plane/projects/quantized-residual-draft-model-for-speculative-decoding-a4f97b3a2f06/runs/quantized-residual-draft-model-for-speculative-decoding-a4f97b3a2f06-20260522T150454526248+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bd4403e6afb2

## What looked useful

An 8-bit GPT-2-small-derived draft preserved enough next-token choices to reduce target forwards/token from 1.0 to 0.551 at gamma 2 and 0.336 at gamma 4 with exact float32 greedy output preservation, but it was slower wall-clock than target-only decoding because the draft was same-size and unoptimized. A 4-bit draft was directly negative, accepting only 4 tokens out of 498-965 proposals and providing essentially no target-pass reduction.

## Boundaries and scale limits

Small prompt set, greedy decoding only, local GB10 GPU, no optimized integer kernels, no smaller residual draft architecture, and no sampling-mode speculative decoding validation. Latency is representative of this naive same-size torch implementation only.

## Claim scope

Tier 1 controlled small direct GPT-2-small greedy speculative decoding test on 8 prompts and 256 generated tokens total, comparing target-only greedy decoding against same-architecture quantized/dequantized GPT-2-small drafts at 8-bit and 4-bit uniform weight quantization.

## Why it stopped

Tier 1 direct evidence supports the 8-bit acceptance mechanism but falsifies a practical speedup claim for the naive same-size implementation; 4-bit uniform quantization is directly non-viable under this setup.

## Recommended next action

Stop this run as no-paper useful signal; run one bounded deepen follow-up with a genuinely cheaper 8-bit residual draft or optimized quantized draft kernel and require actual wall-clock speedup while preserving exact target outputs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized Cheap 8-bit GPT-2 Draft for Exact Speculative Speedup
- Success threshold: At least 1.15x wall-clock tokens/s over target-only GPT-2-small greedy decoding, exact target-output match, at least 60% proposal acceptance, and target forwards/token at or below 0.55 on the bounded prompt set.
- Stop condition: Stop negative if the cheap draft cannot exceed 60% acceptance, cannot reduce target forwards/token below 0.55, introduces exactness mismatches, or remains slower than target-only decoding after one optimized bounded implementation.

## Evidence references

- Artifact root: `<local-path>/projects/real-lm-quantized-residual-draft-for-gpt-2-small-speculati-c0c6b4ea13`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
