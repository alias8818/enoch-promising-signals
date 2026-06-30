# Speculative decoding with n-gram suffix draft and adaptive acceptance threshold

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `speculative-decoding-with-n-gram-suffix-draft-and-adaptive-acceptance-threshold-4da705f19ce2`
Run ID: `speculative-decoding-with-n-gram-suffix-draft-and-adaptive-acceptance-threshold-4da705f19ce2-20260628T032712042189+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a959f9b7cbe6

## What looked useful

Suffix n-gram drafting can reduce verifier calls on highly repetitive streams, but natural-text acceptance was near zero and adaptive thresholding never beat the best fixed gate across tested overheads and suffix lengths.

## Boundaries and scale limits

Proxy replay only: no real LLM logits, no full speculative correction, no optimized GPU verifier, no KV-cache serving benchmark, and no production repeated-prompt traces.

## Claim scope

Bounded replay benchmarks over Tiny Shakespeare and repeated synthetic token streams do not support adaptive suffix-confidence thresholds as an improvement over tuned fixed thresholds for n-gram suffix drafting.

## Why it stopped

Proxy replay evidence rejects the adaptive threshold as a paper-worthy improvement over fixed gates; this is not a full LLM-serving validation.

## Recommended next action

Stop this adaptive-threshold variant unless a real nonstationary repeated-trace workload and GPU verifier benchmark are available; prefer a tuned fixed suffix-confidence gate for further local experiments.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-n-gram-suffix-draft-and-adaptive-acceptance-threshold-4da705f19ce2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
