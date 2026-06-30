# Suffix-Array Speculative Decoding for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-speculative-decoding-for-cpu-inference-98621c88617f`
Run ID: `suffix-array-speculative-decoding-for-cpu-inference-98621c88617f-20260526T032001032043+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a28d37830bd4

## What looked useful

Suffix-array lookup overhead was microsecond-scale and acceptance was high on repetitive local documentation, but acceptance collapsed on Python stdlib code; mechanism appears workload-specific rather than generally viable for CPU speculative decoding.

## Boundaries and scale limits

Not an end-to-end CPU LLM serving benchmark; no BPE tokenizer, no target-model logits, no comparison to a learned draft model, fixed training-prefix suffix table only, local corpora only.

## Claim scope

Trace-level exact-token acceptance for a truncated suffix-array draft proposer on 80k-token local documentation and Python stdlib corpora, measured on a CPU worker with regex tokenization and no real LLM verifier.

## Why it stopped

Proxy trace evidence is useful but insufficient for paper writing; the broad CPU inference claim needs direct model-serving validation and the code-corpus result is weak.

## Recommended next action

Run one bounded real-verifier follow-up with llama.cpp or equivalent CPU inference on repeated-document/RAG prompts, comparing greedy decoding, suffix-array drafting, and a standard draft-model baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU LLM Verification for Suffix-Array Drafting on Repetitive RAG Prompts
- Success threshold: At least 1.25x end-to-end tokens/sec over greedy CPU decoding on repetitive document/RAG prompts with no regression beyond 5% on the negative-control workload.
- Stop condition: Stop if real-verifier first-token acceptance is below 20% or end-to-end speedup is below 1.10x on repetitive prompts after implementation overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-decoding-for-cpu-inference-98621c88617f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
