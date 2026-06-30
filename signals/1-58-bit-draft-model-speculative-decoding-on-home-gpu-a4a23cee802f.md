# 1.58-Bit Draft Model Speculative Decoding on Home GPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `1-58-bit-draft-model-speculative-decoding-on-home-gpu-a4a23cee802f`
Run ID: `1-58-bit-draft-model-speculative-decoding-on-home-gpu-a4a23cee802f-20260527T172244235785+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fe6b5049c075

## What looked useful

The cheap route of post-training ternarizing a draft copy produced finite logits but too little next-token agreement to reduce target verification work. Future work should not assume a ternarized copy is an adequate speculative draft without training or distillation for target agreement.

## Boundaries and scale limits

Small local proxy only: 8 prompts, 32 new tokens per prompt, distilgpt2 target, greedy decoding, no trained BitNet draft, no optimized ternary CUDA kernels, no larger target model, and no production scheduler.

## Claim scope

On GB10 with distilgpt2, a post-training ternarized copy of the target model's transformer matrix weights is not a useful 1.58-bit draft for greedy speculative decoding: acceptance remained at or below 3.42% across three ternary thresholds and measured throughput was about 3.7-3.8% of batched target-only decoding.

## Why it stopped

Proxy/early falsification rather than full validation: the tested post-training ternary draft had near-zero acceptance and large overhead, so it cannot support a paper-positive claim.

## Recommended next action

Stop this run as an early proxy falsification of post-training ternarized drafts; a separate bounded follow-up should test a distilled ternary draft only if training for target-token agreement is in scope.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Distilled Ternary Draft Acceptance for Small Speculative Decoding
- Success threshold: At least 50% accepted proposed tokens and at least 1.15x end-to-end tokens/second over batched target-only decoding for the scoped prompt set.
- Stop condition: Stop if held-out greedy acceptance remains below 30% after a bounded distillation run or if draft overhead prevents any target-call reduction from improving end-to-end throughput.

## Evidence references

- Artifact root: `<local-path>/projects/1-58-bit-draft-model-speculative-decoding-on-home-gpu-a4a23cee802f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
