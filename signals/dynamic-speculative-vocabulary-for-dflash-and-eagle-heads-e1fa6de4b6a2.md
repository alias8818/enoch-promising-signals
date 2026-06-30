# Dynamic Speculative Vocabulary for DFlash and EAGLE Heads

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `dynamic-speculative-vocabulary-for-dflash-and-eagle-heads-e1fa6de4b6a2`
Run ID: `dynamic-speculative-vocabulary-for-dflash-and-eagle-heads-e1fa6de4b6a2-20260519T234516956601+0000`

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

- ChatGPT Pro speculative decoding research map 2026-05-19: file://new-chatgpt-pro-ideas-05-19.md
- Spec-Decoding Oracle Trace Ranker: Instrumented DFlash Trace Analysis to Rank 12 Branch Proposals: file://new-chatgpt-pro-ideas-05-19.md

## What looked useful

Dynamic shortlists consistently improved sampled-token hit rate over static global shortlists by 6.3 to 10.8 absolute percentage points across four runs and produced 6.6x to 19.7x CPU projection speedups, but they underperformed static shortlists immediately after topic switches.

## Boundaries and scale limits

No real DFlash or EAGLE implementation, no trained model logits, no GPU kernel integration, no accepted-tokens-per-second measurement, and no end-to-end latency measurement.

## Claim scope

NumPy proxy simulation of dynamic speculative vocabulary selection on synthetic topic-persistent next-token distributions with CPU output-projection row-count benchmarking.

## Why it stopped

Useful proxy signal only: it supports the mechanism under persistent local vocabulary structure but lacks direct DFlash/EAGLE acceptance and latency evidence.

## Recommended next action

Stop this run as no-paper proxy evidence; next run should implement a small real-model EAGLE-like draft-head trace with static, dynamic, and full-vocab controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model dynamic vocabulary trace for EAGLE-like speculative heads
- Success threshold: At one or more shortlist sizes, dynamic vocabulary reaches at least 95% full-vocab draft-token recall, beats static shortlist accepted-token recall by at least 5 absolute percentage points, and does not lose end-to-end latency after shortlist overhead.
- Stop condition: Stop if dynamic shortlist recall is below static at matched size on real-model traces, or if shortlist overhead eliminates projection savings in end-to-end timing.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-speculative-vocabulary-for-dflash-and-eagle-heads-e1fa6de4b6a2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
