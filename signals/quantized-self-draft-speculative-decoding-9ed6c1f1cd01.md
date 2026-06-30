# Quantized Self-Draft Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-self-draft-speculative-decoding-9ed6c1f1cd01`
Run ID: `quantized-self-draft-speculative-decoding-9ed6c1f1cd01-20260601T041600838540+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8016b872fcd7

## What looked useful

Quantized self-draft proposals were correlated with the target: draft window 4 accepted 343/469 proposed tokens and reduced target calls from 384 to 119. Throughput still dropped to 0.64x of target-only after warmup because draft overhead dominated.

## Boundaries and scale limits

Small-model, short-prompt, greedy-only probe. The draft was int8-rounded then dequantized to floating PyTorch weights, so this does not test production int8 kernels, KV-cache optimized serving, stochastic speculative sampling, large models, long context, or batching.

## Claim scope

On GB10 with PyTorch 2.12, greedy decoding for distilgpt2 over 8 prompts x 48 new tokens showed that an int8-rounded same-architecture draft can exactly preserve target greedy output and reduce target forward calls, but a naive two-model implementation is slower than target-only decoding.

## Why it stopped

Useful bounded proxy result: mechanism partially supported, but local throughput is negative; this is not a full validation of production quantized speculative decoding.

## Recommended next action

Stop this no-paper run; the next bounded test should replace the dequantized same-size draft with a genuinely cheaper draft path and require at least 1.10x throughput over a KV-cache target baseline with exact output preservation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cheaper Quantized Self-Draft Path for Exact Greedy Speculation
- Success threshold: At least 1.10x tokens/sec over target-only KV-cache greedy decoding with exact output match and at least 70% acceptance on the best draft window.
- Stop condition: Stop if the cheaper draft path cannot exceed target-only throughput after reducing target calls, or if exact greedy output preservation fails.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-self-draft-speculative-decoding-9ed6c1f1cd01`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
