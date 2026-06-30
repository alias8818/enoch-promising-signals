# Retrieval-Augmented Speculative Decoding (RASD)

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `retrieval-augmented-speculative-decoding-rasd-3ae7ac57c5fc`
Run ID: `retrieval-augmented-speculative-decoding-rasd-3ae7ac57c5fc-20260522T163324908254+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a993b80fdf91

## What looked useful

RASD verification is mechanically sound when retrieved continuations are model-consistent, but raw text retrieval is too weak in this setup to justify a paper claim; future work should focus on trace/cache-aligned retrieval rather than arbitrary corpus copying.

## Boundaries and scale limits

Small embedded corpus, toy/local prompts, distilgpt2 only, exact suffix retrieval only, greedy decoding only, no production batching, no semantic ANN retriever, no 7B+ model or full serving stack.

## Claim scope

On a local distilgpt2 greedy-decoding benchmark with exact token-suffix retrieval, arbitrary raw-corpus continuation retrieval only reduced target calls by 1.04-2.60%, while a target-generated trace cache reduced target calls by 48.70-87.50% as a positive control.

## Why it stopped

Proxy/local early result: raw-corpus retrieval was weak, and the positive-control trace-cache result is useful mechanism evidence but not full validation.

## Recommended next action

Run a bounded deepen follow-up using held-out repeated prompts and a target-generation trace cache, comparing exact suffix retrieval against semantic/hybrid retrieval with a success threshold of at least 25% target-call reduction on held-out traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out trace-cache retrieval for RASD
- Success threshold: At least 25% target-call reduction and at least 1.2x wall-time speedup versus greedy baseline on held-out trace-cache prompts.
- Stop condition: Stop if held-out trace-cache retrieval gives less than 10% target-call reduction or less than 1.05x wall-time speedup after the planned prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/retrieval-augmented-speculative-decoding-rasd-3ae7ac57c5fc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
