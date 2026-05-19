# Direct confidence-quality cascade test with real local models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-confidence-quality-cascade-test-with-real-local-mod-520703164e`
Run ID: `direct-confidence-quality-cascade-test-with-real-local-mod-520703164e-20260516T193724242466+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/9734c9277505

## What looked useful

Qwen2.5 small-model confidence had eval AUC 0.802 for correctness; the cascade improved held-out exact match from 0.6818 to 0.8182, but stayed below always-large 0.8939 and only reached the upper end of the same-rate random-escalation control interval.

## Boundaries and scale limits

Single primary model pair, small fixed-answer benchmark, one threshold-selection split, exact-match scoring only, no human-rated open-ended tasks, no production latency/cost study, and no multi-family robustness validation.

## Claim scope

On a 66-item held-out fixed-answer QA/math eval using local Qwen2.5-0.5B-Instruct to Qwen2.5-1.5B-Instruct, small-model generated-token log probability predicted small-model correctness and a dev-selected confidence cascade improved exact-match accuracy over small-only while escalating 43.9% of examples.

## Why it stopped

No-paper closure: direct Tier 1 evidence supports the confidence-quality mechanism but not a robust cascade claim because the selected cascade did not clearly beat the random same-rate escalation control and remained below always-large quality.

## Recommended next action

Run a bounded deepen test with at least 200 held-out fixed-answer items and at least three local small/large model pairs, pre-registering a requirement to beat same-rate random escalation by at least 5 percentage points.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-pair fixed-answer confidence cascade validation
- Success threshold: Across at least two of three model pairs, the confidence cascade improves exact-match accuracy over small-only by at least 10 percentage points, beats same-rate random escalation by at least 5 percentage points with p < 0.05, and captures at least half of the always-large accuracy gain while escalating no more than 50% of examples.
- Stop condition: Stop if fewer than two model pairs beat same-rate random escalation by 5 percentage points or if confidence AUC for small-model correctness is below 0.65 on two or more held-out eval splits.

## Evidence references

- Artifact root: `<local-path>/projects/direct-confidence-quality-cascade-test-with-real-local-mod-520703164e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
