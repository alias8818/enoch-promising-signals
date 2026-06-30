# Speculative decoding with n-gram draft model for home GPUs

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `speculative-decoding-with-n-gram-draft-model-for-home-gpus-2e3b9e3c9b9e`
Run ID: `speculative-decoding-with-n-gram-draft-model-for-home-gpus-2e3b9e3c9b9e-20260605T142745251870+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/0ecc541d5ba8

## What looked useful

A zero-parameter n-gram draft can be viable for repeated or self-repeating generations on a home GPU, but the benefit is sensitive to draft length and prompt structure; gamma 2 slightly hurt the prose prompt while gamma 8 improved all tested prompts.

## Boundaries and scale limits

Greedy-only, GPT-2-small-class target, Python/Hugging Face prototype, four prompts, 96 generated tokens per prompt; not validated on 1B-7B+ home LLMs, sampling, batching, quantization, production inference engines, or broad prompt distributions.

## Claim scope

In a bounded batch-1 greedy decoding benchmark on GB10 using GPT-2 and four short prompts, an exact n-gram draft verifier reduced target forwards per token and improved throughput up to 2.21x for gamma 8 while preserving greedy outputs.

## Why it stopped

No-paper closure: bounded direct GPU evidence supports the mechanism, but the validation is too narrow and prototype-specific for publication-grade claims.

## Recommended next action

Run a bounded deepen follow-up in a production-style local inference engine on a 1B-7B class model with greedy and sampling modes before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: N-gram speculative decoding in a local LLM serving engine
- Success threshold: Median throughput at least 1.2x over no-draft baseline on repeated/code/log prompts, no more than 5% slowdown on low-match prompts with adaptive disablement, and exact greedy output match for all greedy trials.
- Stop condition: Stop if adaptive n-gram drafting fails to exceed 1.1x median speedup on repeated prompts or causes more than 5% median slowdown on low-match prompts after implementation overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-n-gram-draft-model-for-home-gpus-2e3b9e3c9b9e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
