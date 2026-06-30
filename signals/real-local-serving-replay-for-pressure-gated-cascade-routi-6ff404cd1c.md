# Real Local-Serving Replay for Pressure-Gated Cascade Routing

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-local-serving-replay-for-pressure-gated-cascade-routi-6ff404cd1c`
Run ID: `real-local-serving-replay-for-pressure-gated-cascade-routi-6ff404cd1c-20260528T151223810789+0000`

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

- Parent run decision: Pressure-Gated Cascade Routing for Local Serving: enoch://control-plane/projects/pressure-gated-cascade-routing-for-local-serving-f3ca80d30a7e/runs/pressure-gated-cascade-routing-for-local-serving-f3ca80d30a7e-20260528T112953612209+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b486f625560c

## What looked useful

Pressure gating did reduce slow-tier queue pressure and p95 latency under bursty local replay. Aggressive gates reduced p95 by about 72-80% but lost too much utility; a looser gate reduced p95 by 47.3% while staying within the predeclared 0.03 utility-loss bound.

## Boundaries and scale limits

The run used simulated service times and a deterministic utility model rather than real LLM inference, real prompt quality, tokenizer/KV-cache behavior, GPU scheduling, or production traffic. It is a Tier 1 local mechanism test, not a full serving validation.

## Claim scope

In a controlled localhost HTTP serving replay with queued fast/slow worker pools, pressure-gated cascade routing at pressure gate 8.0 reduced mean p95 latency by 47.3% versus static confidence cascade while limiting deterministic utility loss to 0.0226 absolute across three 96-request burst traces.

## Why it stopped

No-paper useful signal: the mechanism passed a controlled local replay threshold after gate tuning, but model quality and inference behavior were proxied rather than directly measured on real LLM serving.

## Recommended next action

Run the same replay harness against a real local fast/slow LLM pair on a labeled or judgeable prompt set, preserving the p95 latency >=25% reduction and quality loss <=3 percentage point threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Model Local Cascade Replay With Pressure-Gated Escalation
- Success threshold: Pressure-gated routing reduces mean p95 latency by >=25% versus static cascade with real-task quality loss <=3 percentage points and no increase in error rate/timeouts.
- Stop condition: Stop as unsupported if no tested gate meets both the latency and real-task quality thresholds, or if real model serving overhead removes the p95 latency advantage.

## Evidence references

- Artifact root: `<local-path>/projects/real-local-serving-replay-for-pressure-gated-cascade-routi-6ff404cd1c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
