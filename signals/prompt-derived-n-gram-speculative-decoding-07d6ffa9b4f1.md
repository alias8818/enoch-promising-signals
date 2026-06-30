# Prompt-Derived N-Gram Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `prompt-derived-n-gram-speculative-decoding-07d6ffa9b4f1`
Run ID: `prompt-derived-n-gram-speculative-decoding-07d6ffa9b4f1-20260528T120627116702+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2f9ce934f070

## What looked useful

True-prompt extractive copies reached 12.13x mean verification-call speedup proxy and 98.0% drafted-token fraction with max_n=8,draft_len=16, while shuffled-prompt extractive control stayed at 1.0003x and non-extractive continuation stayed near 1.023x.

## Boundaries and scale limits

Proxy simulation only; simple regex tokenizer; four books; 160 extractive and 160 non-extractive tasks; no real LLM target traces, no serving latency, no KV-cache or batching measurements.

## Claim scope

In a token-level simulation over public-domain prose, prompt-derived n-gram drafts substantially reduce target verification calls for extractive copied-span outputs after a short target-emitted prefix, but provide negligible benefit for non-extractive continuation.

## Why it stopped

Closed as no-paper useful signal because the mechanism is supported only by a proxy simulation, not by real model decoding or serving measurements.

## Recommended next action

Run a bounded deepen test using a real tokenizer and a small local LLM on extractive QA or quote-copy prompts, measuring exact draft acceptance and wall-clock decode latency versus no-draft and prompt-shuffled controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model acceptance test for prompt-derived n-gram drafts on extractive QA
- Success threshold: At least 2x mean wall-clock decode speedup with unchanged generated text on extractive prompts and less than 1.1x speedup on shuffled-prompt controls.
- Stop condition: Stop if true-prompt wall-clock speedup is below 1.3x, if output text changes materially, or if draft construction overhead dominates target verification savings.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-derived-n-gram-speculative-decoding-07d6ffa9b4f1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
