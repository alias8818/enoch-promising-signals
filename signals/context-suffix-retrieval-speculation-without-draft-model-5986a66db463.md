# Context-Suffix Retrieval Speculation Without Draft Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `context-suffix-retrieval-speculation-without-draft-model-5986a66db463`
Run ID: `context-suffix-retrieval-speculation-without-draft-model-5986a66db463-20260523T053344525511+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/56c9da98cb9d

## What looked useful

Best natural-prose estimated speedup upper bound was 1.0275x and real-prose median was 1.0003x across 36 rows; synthetic repeated blocks reached 1.9748x best and 1.3314x median across 12 rows, indicating the mechanism is workload-specialized rather than generally strong.

## Boundaries and scale limits

Proxy-only run with simple word/punctuation tokenization, no target model verifier, no LLM tokenizer, no KV-cache serving integration, three natural prose texts, one synthetic repeated workload, and fixed token-equivalent verifier overhead rather than wall-clock model measurements.

## Claim scope

Token-level simulator over three Gutenberg prose texts plus one synthetic repeated-block stream: context-suffix retrieval without a draft model yields useful speculative continuations in repeated/copy-heavy streams, but provides negligible broad acceleration on ordinary prose under exact-match acceptance.

## Why it stopped

Proxy simulator produced a mixed useful signal but not direct publication-grade evidence: mechanism works on repeated synthetic streams and is negligible on ordinary prose.

## Recommended next action

Run a bounded direct-model follow-up on copy-heavy real traces with an actual small target-model verifier and LLM tokenizer; do not write a paper from this proxy result alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct verifier test of context-suffix speculation on copy-heavy traces
- Success threshold: At least 1.15x measured wall-clock speedup on two copy-heavy trace families with identical generated token sequences to the baseline and no more than 3 percent slowdown on the low-copy control.
- Stop condition: Stop if accepted-token rate is below 0.05 on copy-heavy traces or measured retrieval plus verification overhead eliminates speedup in the first calibrated small-model run.

## Evidence references

- Artifact root: `<local-path>/projects/context-suffix-retrieval-speculation-without-draft-model-5986a66db463`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
