# Suffix-Array N-gram Draft for Speculative Decoding from Generation History

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-n-gram-draft-for-speculative-decoding-from-generation-history-99916e0cf394`
Run ID: `suffix-array-n-gram-draft-for-speculative-decoding-from-generation-history-99916e0cf394-20260529T135641960655+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5213de7fb002

## What looked useful

History exact-match drafting produced 0.482 accepted tokens per position on a CPython tokenize.py trace with min_context=4 and 0.756 with min_context=2, but only 0.007 on Tiny Shakespeare and 0.064 on Alice under min_context=4. A synthetic repeat control reached 7.57 accepted tokens per position. The Python suffix-array query path was about 9-12x slower than a hash n-gram table while returning equivalent drafts.

## Boundaries and scale limits

Tokenization used regex word/punctuation tokens rather than a model tokenizer; traces were at most 16000 tokens except the shorter CPython source file; no GPU verifier, KV-cache integration, online dynamic suffix-array maintenance, or serving wall-clock speedup was measured.

## Claim scope

Offline trace probe of exact-match generation-history drafting on small regex-tokenized public prose/code-like traces and a synthetic repeat control. The mechanism works on repetitive histories and one code-like trace, but is weak on ordinary prose and not validated end-to-end with a target model.

## Why it stopped

Bounded offline evidence supports the mechanism only for repetitive/code-like histories and does not support a paper-ready suffix-array-specific serving claim.

## Recommended next action

Stop this run as no-paper useful signal; next, run a bounded real-model speculative decoding follow-up comparing no draft, hash n-gram history draft, and optimized suffix-array history draft on model-tokenized prose/code/session traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model history-draft speculative decoding comparison
- Success threshold: At least 1.15x end-to-end tokens/s over no-draft on code or repetitive/session traces with no material regression on prose, and suffix-array memory/update tradeoffs competitive with hash n-gram lookup.
- Stop condition: Stop if accepted tokens per position stays below 0.2 on model-tokenized code/session traces or if index overhead eliminates measured wall-clock speedup.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-n-gram-draft-for-speculative-decoding-from-generation-history-99916e0cf394`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
