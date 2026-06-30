# CPU Suffix-Array Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-suffix-array-speculative-decoding-b639b85b308d`
Run ID: `cpu-suffix-array-speculative-decoding-b639b85b308d-20260522T084540825817+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/97c0e59c9136

## What looked useful

Mechanism works in repeated-span workloads: suffix-array accepted 5.9975 tokens/step on synthetic copy data. Natural held-out text was weak: 0.1266 accepted tokens/step and 1.69% proposed-token acceptance. Fixed n-gram controls beat suffix-array on the copy-heavy positive control.

## Boundaries and scale limits

Proxy-only exact-trace replay with 60k train tokens, 12k held-out tokens, 8k positions, simple word/punctuation tokenization, Python implementation, no target language model, no KV-cache or serving integration, and no large corpus.

## Claim scope

Bounded offline trace benchmark: a Python CPU prefix suffix-array drafter can retrieve long exact continuations on copy-heavy synthetic traces, but on a natural Tiny Shakespeare held-out split it accepts only about 0.1266 tokens per replay step.

## Why it stopped

Proxy early falsification for broad natural-text CPU suffix-array drafting: exact held-out acceptance was too low to support a general speculative decoding claim, although copy-heavy traces remain promising.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should integrate the drafter with a small open target LM and compare end-to-end tokens/second against no-draft and n-gram baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM End-to-End Retrieval Drafting Check
- Success threshold: Suffix-array drafting must improve end-to-end tokens/second by at least 10% over no-draft and be within 5% of or better than the n-gram baseline on a copy-heavy workload, without degrading ordinary-text throughput.
- Stop condition: Stop if suffix-array end-to-end throughput is not better than no-draft or is clearly worse than n-gram retrieval on the copy-heavy workload.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-suffix-array-speculative-decoding-b639b85b308d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
