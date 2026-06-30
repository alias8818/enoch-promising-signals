# Real-token GPT-2-small suffix-cache speculation with KV-aware verification

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `real-token-gpt-2-small-suffix-cache-speculation-with-kv-aw-f196b33e67`
Run ID: `real-token-gpt-2-small-suffix-cache-speculation-with-kv-aw-f196b33e67-20260519T201453135968+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: KV-Cache Suffix-Array Speculation: enoch://control-plane/projects/kv-cache-suffix-array-speculation-2fdda793fba3/runs/kv-cache-suffix-array-speculation-2fdda793fba3-20260519T200127097182+0000
- Parent run decision: Tokenizer-level suffix-cache speculation in a small transformer loop: enoch://control-plane/projects/tokenizer-level-suffix-cache-speculation-in-a-small-transf-ba3deb2ae6/runs/tokenizer-level-suffix-cache-speculation-in-a-small-transf-ba3deb2ae6-20260519T200650252657+0000

## What looked useful

Suffix-conditioned real-token continuations were accepted more often than random real-token proposals, but acceptance was still only 4.78% accepted/proposed for suffix length 2 and 3.33% for suffix length 1. Exact suffix speculation was slower than greedy: 0.662x wall speed for suffix length 2 and 0.538x for suffix length 1.

## Boundaries and scale limits

Validated locally on NVIDIA GB10 with GPT-2-small, Wikitext-2 train-built caches, validation prompts, seeds 0/1/2, 36 prompts per configuration, 64-token prompts, and 96 generated tokens. Does not cover larger LMs, production batching, learned draft models, or custom KV-cache kernels.

## Claim scope

Naive real-token suffix-cache speculative decoding for GPT-2-small on Wikitext-2 held-out prompts, using exact greedy float32 target verification with TF32 disabled, did not accelerate decoding versus a real greedy baseline.

## Why it stopped

Tier 2 direct GPT-2-small validation with fixed seeds, real baseline, random control, and suffix-length ablation found exact but slower decoding due to near-universal proposal rejection.

## Recommended next action

Stop this naive suffix-cache path; future work should require a different proposal mechanism that first demonstrates much higher full-draft acceptance under exact greedy verification.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-token-gpt-2-small-suffix-cache-speculation-with-kv-aw-f196b33e67`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
