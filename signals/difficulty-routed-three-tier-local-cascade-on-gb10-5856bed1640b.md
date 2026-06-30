# Difficulty-Routed Three-Tier Local Cascade on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `difficulty-routed-three-tier-local-cascade-on-gb10-5856bed1640b`
Run ID: `difficulty-routed-three-tier-local-cascade-on-gb10-5856bed1640b-20260628T075457829943+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1e1b24b469b9

## What looked useful

Across five seeds and 7500 problem evaluations per strategy, the difficulty router matched always-tier2 accuracy at 1.0000 while averaging 0.4982x the measured GPU kernel cost; a weak cheap router fell to 0.6667 accuracy and sequential fallback averaged 0.7379x tier2 cost.

## Boundaries and scale limits

Proxy-only evidence: no actual LLM tiers, tokenizer overhead, KV-cache residency, batching, quantization, model loading, natural-language benchmark distribution, or judged answer quality. Runs were short local GB10 tests, not full-scale validation.

## Claim scope

On a generated arithmetic workload with deterministic tier-capability proxies and measured GB10 CUDA tier-call kernels, a difficulty router preserved correctness while reducing measured GPU kernel cost versus always using the largest tier.

## Why it stopped

Proxy evidence supports the routing mechanism but does not directly validate a real local LLM cascade, so this is no-paper useful signal rather than publication-grade evidence.

## Recommended next action

Run a bounded deepen follow-up with three actual local model tiers on a held-out QA/math benchmark, measuring end-to-end latency, memory residency, and exact-match or judged correctness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Actual local model three-tier cascade with difficulty routing
- Success threshold: Difficulty-routed cascade reaches at least 99% of always-largest-model accuracy while reducing median end-to-end latency or GPU active time by at least 25% versus always largest, and beats sequential cascade on cost at matched quality.
- Stop condition: Stop if router quality falls more than 1 percentage point below always-largest accuracy, if model residency exceeds available GB10 memory posture, or if measured latency savings are below 10% after calibration.

## Evidence references

- Artifact root: `<local-path>/projects/difficulty-routed-three-tier-local-cascade-on-gb10-5856bed1640b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
