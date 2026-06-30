# Pressure-Gated Cascade Routing for Local Serving

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `pressure-gated-cascade-routing-for-local-serving-f3ca80d30a7e`
Run ID: `pressure-gated-cascade-routing-for-local-serving-f3ca80d30a7e-20260528T112953612209+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b486f625560c

## What looked useful

Pressure gating won 15/15 regimes against both confidence-only and conservative static cascades on regime-mean p95 latency, SLO miss rate, and utility. Compared with conservative static routing, pressure gating averaged -1288.9 ms p95 latency, -0.0755 SLO miss rate, +0.0155 mean quality, and +0.0420 utility while routing 8.71 percentage points more requests to the expensive tier and blocking 29.3% of low-confidence escalations under pressure.

## Boundaries and scale limits

Synthetic queueing and proxy-quality evidence only; no real local LLM runtime, no measured tokens/sec, no calibrated model confidence, no real answer-quality labels or judge scores, and no production timeout/drop behavior.

## Claim scope

In a deterministic synthetic discrete-event simulation of local two-tier cascade serving, pressure-gated escalation improved utility and SLO behavior over confidence-only and conservative static cascade baselines across 15 tested load/burst regimes.

## Why it stopped

Closed as no-paper useful signal because the evidence supports the mechanism in simulation but remains proxy-only rather than direct local-serving validation.

## Recommended next action

Run a bounded real local-serving replay with a cheap and expensive local LLM, calibrated uncertainty, production-like timeouts, and labeled or judged answer quality before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Local-Serving Replay for Pressure-Gated Cascade Routing
- Success threshold: Pressure-gated routing improves utility by at least 0.02 over the best tuned static cascade while reducing SLO miss rate by at least 25% relative and keeping mean quality within 0.02 absolute of the static cascade.
- Stop condition: Stop if pressure gating cannot beat the best tuned static cascade on utility in two independent replay workloads, or if quality drops by more than 0.03 absolute at comparable SLO miss rate.

## Evidence references

- Artifact root: `<local-path>/projects/pressure-gated-cascade-routing-for-local-serving-f3ca80d30a7e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
