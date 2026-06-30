# Contextual N-gram KV-Cache Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `contextual-n-gram-kv-cache-drafting-3b9f3806a616`
Run ID: `contextual-n-gram-kv-cache-drafting-3b9f3806a616-20260525T130651239405+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/40dd4190e197

## What looked useful

The mechanism succeeds on repeated synthetic text, but real-text acceptance is weak: best generous proxy speedup was 1.080x on WikiText-2 and 1.124x on TinyStories, driven by ambiguous 2-token contexts with median accepted length 0 when covered. For n>=4, proxy speedup fell to 1.031x and 1.074x respectively.

## Boundaries and scale limits

No neural target model forward passes, no actual KV-cache reuse, no wall-clock serving latency, no batching, and no sampling-quality evaluation. The speedup metric is a generous target-call upper-bound proxy.

## Claim scope

Causal GPT-2-tokenized trace evaluation of naive contextual n-gram continuation drafting on 120k-token WikiText-2 test and TinyStories validation slices, plus a repeated-text synthetic sanity control.

## Why it stopped

Moderate proxy evidence shows weak real-text acceptance under a generous upper-bound speedup model, so the naive contextual n-gram KV-cache drafting idea is not paper-ready and likely not practically useful as a standalone method.

## Recommended next action

Stop paper pursuit for the naive trace-only form; only continue with a bounded end-to-end small-LM speculative decoder if adding a confidence filter or retrieval refinement can beat 1.15x measured wall-clock speedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end confidence-filtered contextual n-gram drafting on a small causal LM
- Success threshold: At least 1.15x measured wall-clock tokens/sec over no-draft greedy decoding on both corpora, with identical greedy outputs and no more than 10% additional peak memory.
- Stop condition: Stop if measured speedup is below 1.05x on either corpus or if verification/KV overhead erases more than half of the target-call proxy gain.

## Evidence references

- Artifact root: `<local-path>/projects/contextual-n-gram-kv-cache-drafting-3b9f3806a616`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
