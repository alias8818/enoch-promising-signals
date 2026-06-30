# Compressed Context Suffix-Array Draft Generation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `compressed-context-suffix-array-draft-generation-f3d971de734a`
Run ID: `compressed-context-suffix-array-draft-generation-f3d971de734a-20260601T035541819033+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8016b872fcd7

## What looked useful

The suffix-array drafter built and queried quickly, but accepted only 0.0646 tokens per 8-token draft on the largest natural-text run and had 0.0552 first-token accuracy, below the unigram baseline's 0.0752 first-token accuracy and slightly below the n-gram context baseline.

## Boundaries and scale limits

Single public natural-text corpus, word/punctuation tokenizer rather than a model tokenizer, no neural verifier model, no end-to-end speculative decoding wall-clock measurement, and no tests on highly repetitive code/log domains.

## Claim scope

Bounded CPU probe of exact-token draft generation from a suffix-array context copier on Tiny Shakespeare word/punctuation tokens, compared with memorized n-gram and unigram baselines.

## Why it stopped

Early natural-text proxy falsification: exact held-out draft acceptance was too low and did not beat simple baselines, so a larger run of the same suffix-array copier is not justified.

## Recommended next action

Stop this mechanism as a paper candidate; only revisit with a changed mechanism that includes model-scored candidates or a different target domain, then require verifier-in-the-loop accepted-token and wall-clock speedup evidence.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/compressed-context-suffix-array-draft-generation-f3d971de734a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
