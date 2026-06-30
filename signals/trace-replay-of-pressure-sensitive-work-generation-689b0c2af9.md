# Trace Replay of Pressure-Sensitive Work Generation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `trace-replay-of-pressure-sensitive-work-generation-689b0c2af9`
Run ID: `trace-replay-of-pressure-sensitive-work-generation-689b0c2af9-20260607T231110593791+0000`

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

- Parent run decision: Bounded Work Generation for Queue Pressure Relief: enoch://control-plane/projects/bounded-work-generation-for-queue-pressure-relief-e8e03a8bf5b2/runs/bounded-work-generation-for-queue-pressure-relief-e8e03a8bf5b2-20260607T183809909574+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/4965522b9dfe

## What looked useful

Pressure-sensitive work generation is effective for queue-pressure relief in real-duration replay, cutting p95 wait by 82.85% versus a static cap and 88.21% versus unbounded generation. However, at a 4x-median deadline it only improved deadline-success utility by 3.68% versus admission-only and passed the paired joint threshold in 42.5% of replicates, while remaining 42.24% worse than the static cap on deadline utility.

## Boundaries and scale limits

CPU-only event-driven replay, not live LLM/Codex execution; synthetic arrivals and child-task utility; no production trace, cancellation cost, priority scheduling, dependency graph, retries, or semantic task grading.

## Claim scope

Controlled Tier 1 replay over 834 real local Enoch/Codex agent-run service durations with synthetic bursty exogenous arrivals and recursive child-work generation. Pressure-sensitive generation reduced p95 wait and improved eventual completed utility, but did not satisfy the deadline-utility threshold against static-cap and admission-only controls.

## Why it stopped

Controlled direct trace replay produced mixed evidence and failed the stated Tier 1 success threshold; this is not a full validation or paper-ready positive result.

## Recommended next action

Stop this follow-up as no-paper useful evidence; future scheduler work should optimize explicit deadline-aware utility, not only queue pressure or eventual completed utility.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Deadline-Aware Pressure-Sensitive Work Generation Replay
- Success threshold: Deadline-slack-aware pressure generation must reduce p95 wait by at least 20% versus static_cap and improve deadline-success utility by at least 5% versus static_cap in at least 80% of paired replicates at both 4x and 8x median-service deadlines.
- Stop condition: Stop if the slack-aware policy fails to beat static_cap deadline-success utility by 5% at either deadline multiplier or if its p95 wait is not at least 20% lower than static_cap.

## Evidence references

- Artifact root: `<local-path>/projects/trace-replay-of-pressure-sensitive-work-generation-689b0c2af9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
