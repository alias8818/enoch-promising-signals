# Real CPU-Agent Trace Replay for Cascade Fallback Routing

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `real-cpu-agent-trace-replay-for-cascade-fallback-routing-0bbdf7eb93`
Run ID: `real-cpu-agent-trace-replay-for-cascade-fallback-routing-0bbdf7eb93-20260522T032502792841+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: CPU Agent Reliability via Cascade Fallback Routing: enoch://control-plane/projects/cpu-agent-reliability-via-cascade-fallback-routing-417022326fc6/runs/cpu-agent-reliability-via-cascade-fallback-routing-417022326fc6-20260521T201518454570+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f42e89d1099e

## What looked useful

Real trace replay is feasible and reproducible, but the simple trace-feature router failed operationally: cost-calibrated routing escalated 7.1% of prefix examples and caught 0 of 44 fallback-needed prefix examples, while safety-first calibration caught 97.7% only by escalating 99.8% of examples.

## Boundaries and scale limits

Single worker trace corpus; fallback-needed labels are derived from Enoch decision metadata rather than human incident labels; only 11 of 117 projects were positive labels; no learned semantic model, private controller telemetry, or real fallback intervention outcomes were tested.

## Claim scope

On 117 real local Enoch/Codex CPU-agent project traces with final decision-derived fallback labels, a deterministic trace-prefix cascade router using command failures, nonzero exits, and error/recovery keywords did not achieve useful fallback routing under leave-one-project-out calibration.

## Why it stopped

Controlled small direct trace replay produced a negative/useful result: the simple router either missed all fallback-needed labels when cost-calibrated or degenerated to almost-always fallback when safety-calibrated.

## Recommended next action

Stop this simple trace-feature cascade path; only revisit fallback routing with stronger labeled incidents and semantic/artifact-validation features rather than command-status replay alone.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-cpu-agent-trace-replay-for-cascade-fallback-routing-0bbdf7eb93`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
