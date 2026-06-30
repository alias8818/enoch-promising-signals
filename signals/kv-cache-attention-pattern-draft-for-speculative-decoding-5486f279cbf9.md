# KV-Cache Attention Pattern Draft for Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-attention-pattern-draft-for-speculative-decoding-5486f279cbf9`
Run ID: `kv-cache-attention-pattern-draft-for-speculative-decoding-5486f279cbf9-20260523T041057650158+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e56aeca11e8c

## What looked useful

Draft attention page rankings did not meet the main moderate-coupling budget-8 success threshold over recency (delta 0.0028 target attention mass, 0.3975 win rate). They helped in diffuse/anchor-heavy synthetic regimes (delta 0.0358 to 0.0924) and failed or reversed in strongly local regimes, narrowing the idea to non-local workloads.

## Boundaries and scale limits

No real transformer attention traces, no serving implementation, no GPU prefetch latency measurement, and no end-to-end speculative decoding throughput. Results are bounded to a CPU synthetic simulator with 2,000 main trials plus two 1,000-trial sensitivity regimes.

## Claim scope

Synthetic page-level attention trace simulation for speculative decoding KV-cache page prediction, comparing draft-ranked pages against recency, random, and previous-target controls across coupling and locality regimes.

## Why it stopped

No-paper useful signal: synthetic evidence is mixed and early-falsifies the broad claim, but it is not full validation and does not test real model traces or serving throughput.

## Recommended next action

Run a bounded direct trace study with a real draft/target pair, measuring page-level attention mass overlap and verifier latency for recency-only versus recency-plus-draft predictors.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model draft attention trace test for KV-cache page prediction
- Success threshold: At budget 8 or equivalent memory budget, recency-plus-draft improves target attention-mass coverage by at least 0.05 absolute and verifier latency or miss-rate by at least 5% on non-local prompts without regressing local prompts by more than 1%.
- Stop condition: Stop if real-model traces show less than 0.02 absolute attention-mass improvement over recency in non-local prompts or any latency/miss-rate benefit disappears after adding recency to the predictor.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-attention-pattern-draft-for-speculative-decoding-5486f279cbf9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
