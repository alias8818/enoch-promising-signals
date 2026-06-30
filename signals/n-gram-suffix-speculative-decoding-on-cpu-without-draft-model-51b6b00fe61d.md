# N-gram Suffix Speculative Decoding on CPU Without Draft Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-speculative-decoding-on-cpu-without-draft-model-51b6b00fe61d`
Run ID: `n-gram-suffix-speculative-decoding-on-cpu-without-draft-model-51b6b00fe61d-20260621T124014353250+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/800ffea83752

## What looked useful

Best idealized target-call reduction was 80.16% on local project text and 93.63% on synthetic repeated templates, but only 6.84% on synthetic low-repeat records. The mechanism is workload-dependent and should target copy/repetition-heavy contexts.

## Boundaries and scale limits

Single-process CPU Python evaluator; regex word/punctuation tokens rather than model BPE; local project text plus synthetic repeated and low-repeat corpora; no real transformer verifier or production decoding loop.

## Claim scope

N-gram suffix lookup can substantially reduce idealized target-model calls in repetition-heavy token streams, but it provides little benefit on low-repeat streams. This run supports the proposal mechanism only, not real CPU LLM latency.

## Why it stopped

Bounded proxy experiment completed; result is useful but not publication-grade because it measures proposal acceptance and idealized call reduction rather than real model-tokenizer latency.

## Recommended next action

Stop this run as a no-paper useful signal; next direct evidence should integrate the suffix proposer into a real CPU LLM verifier and measure latency against greedy decoding on repeated-prompt, code-editing, RAG, and ordinary prose workloads.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU LLM verifier benchmark for n-gram suffix speculative decoding
- Success threshold: At least 20% median latency reduction on repetition-heavy workloads with no generated-token mismatch and no more than 5% regression on ordinary prose.
- Stop condition: Stop if integrated verifier speedup is below 10% on repetition-heavy workloads or if tokenizer/model verification overhead erases the target-call reduction.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-speculative-decoding-on-cpu-without-draft-model-51b6b00fe61d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
