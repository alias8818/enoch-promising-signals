# Block-parallel corpus verifier for n-gram speculative decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `block-parallel-corpus-verifier-for-n-gram-speculative-deco-aa39626f96`
Run ID: `block-parallel-corpus-verifier-for-n-gram-speculative-deco-aa39626f96-20260523T102354696676+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Corpus-backed cached verifier ablation for n-gram speculative decoding: enoch://control-plane/projects/corpus-backed-cached-verifier-ablation-for-n-gram-speculat-661ab1f77b/runs/corpus-backed-cached-verifier-ablation-for-n-gram-speculat-661ab1f77b-20260523T094635668479+0000
- Parent run decision: Cached verifier benchmark for n-gram speculative decoding on public GPT-2-small prompts: enoch://control-plane/projects/cached-verifier-benchmark-for-n-gram-speculative-decoding-3fe4a4dcd7/runs/cached-verifier-benchmark-for-n-gram-speculative-decoding-3fe4a4dcd7-20260523T063804491715+0000

## What looked useful

The verifier mechanism works and is fast in isolation: 30 non-smoke configurations had exact CPU/GPU agreement, with median 260.8x speedup and 2.51B to 3.85B candidate-token comparisons/s. Validation also found and fixed a required tail-position validity guard for GPU gathers.

## Boundaries and scale limits

Component-only verifier benchmark; no target language model, no end-to-end speculative decoding latency, no BPE-tokenized model corpus, no optimized C++/CUDA retrieval baseline, and no datacenter-scale serving workload.

## Claim scope

On GB10, for byte-tokenized real local text corpora up to 64 MB and fixed retrieved n-gram candidate positions, a CUDA block-parallel verifier exactly matched a Python CPU verifier while checking speculative continuation blocks 138x to 779x faster across the completed benchmark grid.

## Why it stopped

Useful mechanism evidence, but not paper-ready because it does not measure end-to-end speculative decoding or compare against optimized production-grade baselines.

## Recommended next action

Run one bounded end-to-end n-gram speculative decoding experiment with a small real language model, BPE tokens, optimized retrieval/verifier baselines, and report accepted tokens per target pass plus wall-clock latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end block-parallel n-gram speculative decoding with a small real LM
- Success threshold: At least 1.2x end-to-end tokens/s improvement over the conventional verifier baseline on a fixed prompt set, with identical sampled outputs under deterministic decoding and no more than 1% regression in accepted draft tokens per target-model call.
- Stop condition: Stop if verifier acceleration does not translate to at least 1.05x end-to-end tokens/s on a 100-prompt pilot, or if retrieval/model overhead dominates more than 90% of wall-clock time after basic batching.

## Evidence references

- Artifact root: `<local-path>/projects/block-parallel-corpus-verifier-for-n-gram-speculative-deco-aa39626f96`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
