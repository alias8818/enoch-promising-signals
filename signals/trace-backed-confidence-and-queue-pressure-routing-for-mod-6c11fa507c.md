# Trace-backed confidence and queue-pressure routing for model cascades

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-backed-confidence-and-queue-pressure-routing-for-mod-6c11fa507c`
Run ID: `trace-backed-confidence-and-queue-pressure-routing-for-mod-6c11fa507c-20260630T013826494659+0000`

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

- Parent run decision: Confidence-Routed Model Cascade for Queue Pressure: enoch://control-plane/projects/confidence-routed-model-cascade-for-queue-pressure-ebab2b729b05/runs/confidence-routed-model-cascade-for-queue-pressure-ebab2b729b05-20260630T011759180078+0000
- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/3ca416d3c523

## What looked useful

Across five 20k-request bursty replays, trace-backed risk beat confidence-only risk on validation ROC AUC (mean 0.9256 vs 0.7662). Queue-pressure trace routing improved over confidence-static by mean +0.0208 accuracy, -4.3741 s p95 latency, -0.2434 SLA miss rate, and +0.6841 utility. Against trace-static it preserved accuracy (+0.00055 mean delta) while reducing p95 latency by 0.3645 s and SLA misses by 0.0658.

## Boundaries and scale limits

Evidence is local and proxy-only: small vision classification dataset, engineered classifier trace features, synthetic utility weights, and simulated queue/service times. It does not validate production LLM cascades, real token/tool/retrieval traces, real serving systems, or user-facing correctness/cost tradeoffs.

## Claim scope

In a reproducible local sklearn-digits cascade with a cheap classifier, stronger classifier, learned cheap-error trace risk, and simulated bursty expensive-model queue, trace-backed queue-pressure routing improves utility and latency/SLA metrics over confidence-static and trace-static routing while preserving nearly the same accuracy as trace-static routing.

## Why it stopped

Closed as no-paper useful signal: the bounded proxy supports the mechanism, but direct LLM cascade evidence is required before a paper-positive decision.

## Recommended next action

Run a bounded direct-evidence replay on a real small/large LLM cascade trace with logged correctness, LLM-native trace features, and measured service times; stop treating this proxy as publishable until that replay confirms the latency/SLA gain without accuracy loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace replay for queue-pressure LLM cascade routing
- Success threshold: Trace-queue-pressure routing must reduce p95 latency by at least 25% and SLA misses by at least 20% versus trace-static routing, with accuracy delta no worse than -0.005 and utility positive versus all static baselines.
- Stop condition: Stop as unsupported if trace-backed risk does not beat max-probability confidence by at least 0.05 ROC AUC on cheap-error prediction, or if queue-pressure routing fails to improve p95 latency/SLA misses without more than 0.5 percentage-point accuracy loss.

## Evidence references

- Artifact root: `<local-path>/projects/trace-backed-confidence-and-queue-pressure-routing-for-mod-6c11fa507c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
