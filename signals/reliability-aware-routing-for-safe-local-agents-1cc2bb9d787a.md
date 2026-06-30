# Reliability-Aware Routing for Safe Local Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `reliability-aware-routing-for-safe-local-agents-1cc2bb9d787a`
Run ID: `reliability-aware-routing-for-safe-local-agents-1cc2bb9d787a-20260527T121313316910+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/526badc83053

## What looked useful

Conservative reliability-aware routing reduced unsafe rate versus a static safe baseline at the strict threshold but cost 48.35% more. A near-cost threshold improved success but had slightly higher unsafe rate. Cold-start routing was unsafe without offline calibration.

## Boundaries and scale limits

Proxy-only simulation; no real local-agent traces, no model/tool execution, no human safety labels, and no production latency or cost measurements. Final evidence used 40 seeds x 10,000 synthetic deployment tasks per threshold.

## Claim scope

Synthetic contextual local-agent routing with four agent choices, four domains, three risk bins, offline calibration, and a single drift event. Reliability-aware Wilson-bound routing exposes a controllable safety/cost frontier but does not dominate a static safe baseline.

## Why it stopped

No paper-ready direct evidence: synthetic results show a useful safety/cost tradeoff but not a clear Pareto improvement over a static safe baseline.

## Recommended next action

Stop paper path for this proxy result; next bounded action is to replay the router on a real local-agent task suite with offline calibration and unsafe-action labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay reliability-aware routing on labeled local-agent traces
- Success threshold: At matched or lower mean cost than static safe routing, reduce unsafe-action rate by at least 25% with no more than a 2 percentage point success-rate loss across a held-out real-task split.
- Stop condition: Stop if calibrated reliability bounds cannot beat static risk routing on unsafe rate at matched cost, or if label coverage is insufficient to measure unsafe actions by context.

## Evidence references

- Artifact root: `<local-path>/projects/reliability-aware-routing-for-safe-local-agents-1cc2bb9d787a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
