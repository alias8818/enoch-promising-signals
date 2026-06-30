# Suffix-Array Speculative Decoding Without Draft Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-speculative-decoding-without-draft-model-e05fbba41f90`
Run ID: `suffix-array-speculative-decoding-without-draft-model-e05fbba41f90-20260530T024011526600+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/36b9f72c1481

## What looked useful

Exact draft-model-free speculative decoding via suffix-array proposals is mechanically viable and sometimes saves target calls, but proposal acceptance is low and brittle; the result is useful for follow-up design, not paper-ready evidence.

## Boundaries and scale limits

The run used synthetic/repeated local memory, prompts drawn from that memory, small GPT-2-family models, full-prefix verification, and short continuations. It did not test real held-out corpora, optimized KV-cache serving, batched latency, sampling, or large-context models.

## Claim scope

On a bounded synthetic repeated-text memory with cached GPT-2 and DistilGPT-2 targets, suffix-array proposals can preserve exact greedy decoding and reduce target forward-call count by roughly 15-19% for 48 prompts x 48 generated tokens.

## Why it stopped

Closed as no-paper useful signal: local evidence supports the mechanism in a favorable synthetic setting, but not a broad or publication-grade validation.

## Recommended next action

Run a bounded deepen test on real held-out text/code/chat traces with an optimized KV-cache verifier and controls against n-gram/hash retrieval before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out corpus suffix-array speculative decoding with KV-cache verification
- Success threshold: Exact-match rate 1.0, mean target-call reduction >= 20%, p10 target-call reduction > 0%, and mean latency improvement >= 10% on at least two real held-out datasets.
- Stop condition: Stop if exactness fails, mean call reduction remains below 10%, or latency does not improve after KV-cache implementation on two datasets.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-decoding-without-draft-model-e05fbba41f90`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
