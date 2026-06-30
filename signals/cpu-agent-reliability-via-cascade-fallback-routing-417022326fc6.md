# CPU Agent Reliability via Cascade Fallback Routing

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-agent-reliability-via-cascade-fallback-routing-417022326fc6`
Run ID: `cpu-agent-reliability-via-cascade-fallback-routing-417022326fc6-20260521T201518454570+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f42e89d1099e

## What looked useful

At 50,000 requests per policy per scenario, signal-only conservative cascade reached 87.736% success under independent failures and 82.568% under correlated failures. That is +16.85 and +18.37 success percentage points over primary-only, but only +1.01 and +1.23 points over retry-primary-on-signal. The cost was 45.74%-55.73% higher mean latency and 42.81%-53.05% higher mean CPU versus primary-only. Oracle cascade over all failures reached 91.948% and 86.732%, showing that detector coverage is the main bottleneck.

## Boundaries and scale limits

Proxy-only simulation: no real LLM/agent calls, no production queueing, no live tool APIs, no measured CPU saturation beyond the harness process, and no real semantic failure detector. The oracle all-failures cascade is an upper bound that assumes silent wrong answers are detectable.

## Claim scope

In a deterministic synthetic CPU-agent routing harness with modeled task stress, detectable error modes, latency, CPU work, and independent/correlated failure regimes, conservative cascade fallback increased request success over primary-only and slightly over same-stack retry/peer fallback, at substantial latency and CPU overhead.

## Why it stopped

Closed as no-paper useful signal because the current result is a synthetic proxy mechanism test, not direct production or real-agent validation.

## Recommended next action

Run a bounded real-trace replay with actual CPU agent tasks and a semantic/error detector, comparing primary-only, retry-primary, same-stack peer, and conservative fallback on success, latency, CPU, and detector coverage.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU-Agent Trace Replay for Cascade Fallback Routing
- Success threshold: Cascade fallback beats retry-primary and same-stack peer by at least 1.0 absolute success percentage point with non-overlapping 95% confidence intervals, while mean CPU overhead versus primary-only remains below 60%.
- Stop condition: Stop if cascade success is not at least 1.0 percentage point above retry-primary/peer, if detector coverage is below 70%, or if CPU overhead exceeds 60% without a larger reliability gain.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-agent-reliability-via-cascade-fallback-routing-417022326fc6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
