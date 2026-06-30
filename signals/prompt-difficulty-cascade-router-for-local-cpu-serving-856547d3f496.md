# Prompt-difficulty cascade router for local CPU serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-difficulty-cascade-router-for-local-cpu-serving-856547d3f496`
Run ID: `prompt-difficulty-cascade-router-for-local-cpu-serving-856547d3f496-20260620T045512353445+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ae97c47b70d8

## What looked useful

High recall for hard prompts can erase most cascade-serving savings on CPU when the workload has many hard prompts and the quality tolerance is tight. The router beat length-only and random controls, but the practical cost saving was small.

## Boundaries and scale limits

Synthetic prompt/quality labels; matrix-multiplication latency proxy instead of real local LLM inference; 12,000 prompts with 4,800 held out; no real answer judging, no llama.cpp/vLLM CPU serving, and no multi-distribution robustness testing.

## Claim scope

On a deterministic synthetic prompt-difficulty workload with local CPU latency proxy calibration, a feature-based cascade router can identify hard prompts better than length-only or random controls, but preserving near-always-large quality requires routing about 90% of prompts to the expensive tier and saves only 4.17% cost.

## Why it stopped

Proxy early falsification: bounded synthetic evidence found only 4.17% cost saving at near-always-large quality, so the large CPU-serving efficiency claim is not supported without direct real-model evidence.

## Recommended next action

Stop paper path for this proxy result; only revisit if a cheap direct follow-up measures the same protocol on real local CPU model tiers and real prompt quality labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real local CPU two-tier cascade router validation
- Success threshold: At least 15% mean latency or cost saving versus always-large while keeping mean quality within 0.01 and low-quality failure-rate increase at or below 1 percentage point.
- Stop condition: Stop if the best quality-preserving operating point saves less than 10% latency/cost or requires routing more than 85% of prompts to the large tier.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-difficulty-cascade-router-for-local-cpu-serving-856547d3f496`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
