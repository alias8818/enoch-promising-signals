# Context-Suffix Matching Speculative Decoding for Structured Text

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `context-suffix-matching-speculative-decoding-for-structured-text-c0e4c0ba9a39`
Run ID: `context-suffix-matching-speculative-decoding-for-structured-text-c0e4c0ba9a39-20260523T171226663359+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7d1a8c055254

## What looked useful

On 1,200-record synthetic structured corpora, suffix-copy achieved mean 4.714x upper-bound target-call speedup versus 1.192x on shuffled controls and 1.012x on unstructured random tokens. Repeat-rate sensitivity increased mean structured speedup from 3.858x at repeat probability 0.15 to 4.913x at 0.75.

## Boundaries and scale limits

No real language model, tokenizer, GPU serving stack, model-cache integration, batching, quality evaluation, or real structured-text corpus was tested. Reported speedups are upper bounds on target-call reduction, not end-to-end latency.

## Claim scope

Synthetic proxy traces for JSON, CSV, logfmt, and Markdown-table structured text show that context-suffix copying can reduce target verification calls in a speculative-decoding simulator, with controls showing the effect depends on ordered structure.

## Why it stopped

This run produced only synthetic proxy evidence: useful mechanism signal, but not direct model-serving evidence or publication-grade validation.

## Recommended next action

Run a bounded direct-evidence follow-up on real small-model structured-text continuations, measuring end-to-end speculative decoding overhead and accepted tokens against n-gram/trie baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model trace validation for context-suffix speculative decoding on structured text
- Success threshold: At least 1.5x target-call reduction and positive estimated latency after proposer overhead on two or more real structured formats, with no degradation in exact greedy output.
- Stop condition: Stop if real-model continuations show less than 1.2x target-call reduction after overhead on all tested formats or if proposer overhead exceeds saved verifier cost.

## Evidence references

- Artifact root: `<local-path>/projects/context-suffix-matching-speculative-decoding-for-structured-text-c0e4c0ba9a39`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
