# KV-Cache N-Gram Speculation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-n-gram-speculation-35b649e72eec`
Run ID: `kv-cache-n-gram-speculation-35b649e72eec-20260525T182141591991+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/04773911dabc

## What looked useful

Prompt-lookup n-gram speculation works on repeated text but is too sparse on ordinary WikiText-2 prose for a broad acceleration claim: n=2 reduced simulated target calls by 2.51%, n=3 by 1.27%, and n>=4 by less than 0.7%.

## Boundaries and scale limits

No real target-model verification latency, GPU serving benchmark, KV-cache kernel measurement, or model-generated continuation benchmark was run. WikiText evidence covers about 50k evaluated decode tokens from 538 eligible docs in the first 1000 nonempty WikiText-2 test rows.

## Claim scope

Offline GPT-2-tokenized prompt-lookup n-gram speculative decoding simulation on WikiText-2 prose plus a repeated-text positive control. The run measured exact draft acceptance and simulated target-call reduction with lookback 2048 and max draft length 16.

## Why it stopped

Proxy evidence supports the mechanism only in repeated contexts and early-falsifies a broad general-prose acceleration claim; it is not a full validation of model-serving speed.

## Recommended next action

Stop this run as a bounded offline proxy result; a worthwhile next test is a real target-model latency benchmark on code/log/template/RAG workloads where repetition is expected.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model prompt-lookup latency on repetition-heavy workloads
- Success threshold: At least 10% end-to-end latency reduction on a repetition-heavy workload with no quality regression and at least 5x the WikiText-2 accepted-token fraction.
- Stop condition: Stop if real-model latency improves by less than 5% or acceptance remains below 10% of generated tokens on the repetition-heavy workload.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-n-gram-speculation-35b649e72eec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
