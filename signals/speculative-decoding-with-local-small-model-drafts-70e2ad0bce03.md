# Speculative Decoding with Local Small Model Drafts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `speculative-decoding-with-local-small-model-drafts-70e2ad0bce03`
Run ID: `speculative-decoding-with-local-small-model-drafts-70e2ad0bce03-20260605T212258756566+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/1fd369b1bf6e

## What looked useful

The mechanism is plausible: a nearby small local draft has substantial target agreement and clear cycle-compression potential over random proposals, with self-draft and random controls behaving as expected. The run does not establish end-to-end speedup.

## Boundaries and scale limits

Small local prompt set, Qwen 0.5B-to-1.5B pair only, 32 generated tokens per prompt, greedy decoding only, sequential verifier used for exact acceptance measurement, no optimized batched verifier, no KV-cache sharing, no serving throughput benchmark, no larger 7B+ target validation.

## Claim scope

On 20 fixed short prompts with greedy decoding, a cached local Qwen2.5-0.5B-Instruct draft paired with a cached local Qwen2.5-1.5B-Instruct target accepted 52.5% of proposed tokens at draft length k=4 and emitted 2.69 target-equivalent tokens per theoretical target verification cycle while preserving target-greedy output in the sequential correctness harness.

## Why it stopped

Scoped local evidence supports acceptance/cycle-compression potential but not publication-grade or serving-speed claims.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement an optimized batched verifier with KV-cache-aware timing on the same model pair and require measured latency improvement over target-only decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-aware batched speculative decoding benchmark for Qwen 0.5B draft and 1.5B target
- Success threshold: At least 1.2x median tokens/second improvement over target-only greedy decoding with 100% target-output equivalence and no prompt bucket showing more than 5% regression.
- Stop condition: Stop if optimized speculative decoding is less than 1.05x faster overall or if draft overhead exceeds the saved target verification time in two independent prompt buckets.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-local-small-model-drafts-70e2ad0bce03`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
