# N-gram Speculative Draft for Local Inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-speculative-draft-for-local-inference-fdf423905c1f`
Run ID: `n-gram-speculative-draft-for-local-inference-fdf423905c1f-20260526T013821480154+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6fe9efb9df68

## What looked useful

Best confirmed setting, n-gram order 2 with draft length 4, averaged 54.69 target forwards for 64 generated tokens, 1.1939x target-call reduction, 0 exact mismatches, and 1.2149x naive wall speedup; 2 of 32 prompts accepted zero draft tokens.

## Boundaries and scale limits

Small model, small public text dataset, 32 prompts, greedy decoding only, simple Python verifier, no optimized KV-cache serving engine, no 7B+ model, no domain-specific local workload corpus.

## Claim scope

A Python/Transformers greedy speculative-decoding proxy using DistilGPT-2 on WikiText-2 showed that an n-gram table can preserve exact target output while reducing target forward calls by about 1.19x on 32 prompts.

## Why it stopped

Useful local proxy evidence supports the mechanism, but acceptance is low and the run is not direct production-grade validation or broad enough for a paper.

## Recommended next action

Run a bounded deepen follow-up in an optimized local inference engine with KV-cache-aware verification on at least 100 realistic local prompts, stopping if exact-output wall speedup is below 1.1x.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-aware n-gram speculative decoding for realistic local inference prompts
- Success threshold: Mean wall-clock speedup at least 1.1x with exact output parity and no more than 10% of prompts slower than baseline.
- Stop condition: Stop as negative if exact-output wall-clock speedup is below 1.1x or if more than 25% of prompts accept zero draft tokens after implementing KV-cache-aware verification.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-local-inference-fdf423905c1f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
