# Priority Queue with Cascade Fallback for Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `priority-queue-with-cascade-fallback-for-agents-ad11c82e5d82`
Run ID: `priority-queue-with-cascade-fallback-for-agents-ad11c82e5d82-20260528T063008814742+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/3143dc884d0d

## What looked useful

Cascade fallback is mechanically useful for recovering failed tasks, reducing failure rate by about 19.5 percentage points and raising success rate by about 10.2 percentage points on average, but the naive design converts failures into late expensive completions. Priority queueing alone was indistinguishable from FIFO in this setup.

## Boundaries and scale limits

Synthetic local simulation only; no live LLM/tool agents, real provider latency, rate limits, production traces, or dollar billing were measured. The run used 600 tasks per seed/scenario and should not be treated as broad agent-systems validation.

## Claim scope

In a deterministic synthetic discrete-event simulator with 30 seeds across 9 load/deadline regimes, priority+cascade fallback improved deadline-weighted completion over FIFO by 1.4 to 14.3 percentage points, but priority-only dispatch had no measurable effect and cascade increased mean cost and tail lateness.

## Why it stopped

Proxy simulator evidence is mixed: cascade supports the fallback mechanism but falsifies the naive combined priority-queue+cascade design as paper-ready because priority alone added no benefit and cascade raised cost/tail lateness substantially.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should add deadline-aware cascade admission or cancellation and require retained completion gains without the observed tail-lateness explosion.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Deadline-aware cascade admission for agent fallback queues
- Success threshold: Across all 9 scenarios, deadline-weighted completion is at least 5 percentage points above FIFO on average, p95 lateness delta is no more than 5 seconds on average, and mean cost delta is no more than 2.5 simulated cost units.
- Stop condition: Stop as negative if deadline-aware cascade cannot meet both the p95 lateness and cost thresholds while preserving at least a 5 percentage point completion gain.

## Evidence references

- Artifact root: `<local-path>/projects/priority-queue-with-cascade-fallback-for-agents-ad11c82e5d82`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
