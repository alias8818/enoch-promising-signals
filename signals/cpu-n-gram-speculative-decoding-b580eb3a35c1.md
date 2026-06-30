# CPU N-Gram Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-decoding-b580eb3a35c1`
Run ID: `cpu-n-gram-speculative-decoding-b580eb3a35c1-20260603T234450973884+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/71331c498ab7

## What looked useful

Prompt n-gram speculative decoding is mechanism-positive for copy-heavy contexts and weak as a general CPU decoding accelerator for non-copy heldout text. Indexed lookup is necessary; naive reverse scanning can erase benefits.

## Boundaries and scale limits

No neural LLM target model, transformer KV-cache verification, batched serving, or production prompt distribution was tested. Results are bounded to a Python CPU prompt-lookup proxy over 107,520 aggregate output tokens per hash configuration.

## Claim scope

A CPU hash-indexed prompt n-gram proposer was tested on public-domain Shakespeare token continuations with exact-match verification. It reduced target verification calls by about 64-86% on copy-heavy continuations, but only about 9% on ordinary heldout continuation exact matching.

## Why it stopped

Closed as no-paper useful signal because the evidence is a proxy benchmark, not direct LLM serving validation.

## Recommended next action

Run a bounded real-model follow-up by integrating the hash prompt-lookup proposer into a CPU LLM decoding stack and enabling it only for prompts with measurable copy likelihood.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU LLM Prompt-Lookup Speculative Decoding With Copy-Likelihood Gating
- Success threshold: At least 25% tokens/s improvement on copy-heavy prompts, less than 5% slowdown on ordinary prompts with gating enabled, and reproducible acceptance diagnostics over at least 100 prompts per class.
- Stop condition: Stop if real-model acceptance on copy-heavy prompts fails to reduce target calls by 30% or if gated ordinary-prompt slowdown exceeds 5%.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-decoding-b580eb3a35c1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
