# Early-Exit Self-Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `early-exit-self-speculative-decoding-a19b1183bc65`
Run ID: `early-exit-self-speculative-decoding-a19b1183bc65-20260603T153531297558+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2995134c597b

## What looked useful

Early-exit drafting produced high acceptance and reduced verifier calls, especially gamma=8 with 78.59% acceptance and 7.23 tokens per verifier call, but serial layer-token cost proxy and naive no-KV wall-clock were worse than baseline, so practical speedup remains unproven.

## Boundaries and scale limits

Toy character-level dataset, one seed, 4-layer small model, greedy decoding only, no optimized KV-cache serving implementation, and no GPT-2-small-class or larger validation.

## Claim scope

On a 4-layer 826k-parameter character-level Transformer trained for 600 steps on Tiny Shakespeare, an auxiliary layer-2 LM head reached 83.94% validation top-1 agreement with the final head and reduced greedy verifier calls during self-speculative decoding across 16 prompts.

## Why it stopped

Bounded local evidence supports the acceptance/verifier-call mechanism but not a publishable practical speedup claim.

## Recommended next action

Stop this run as no-paper useful signal; next direct test should use a KV-cache-aware GPT-2-small-class implementation and require measured wall-clock speedup against normal decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache GPT-2-small-class early-exit self-speculative decoding
- Success threshold: At least 1.2x wall-clock tokens/s over optimized greedy baseline on 256+ held-out prompts while preserving greedy final-model outputs.
- Stop condition: Stop if acceptance stays below 60% after auxiliary-head training or if optimized self-speculative decoding remains below 1.05x baseline tokens/s at all gamma values.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-self-speculative-decoding-a19b1183bc65`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
