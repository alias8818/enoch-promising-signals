# Real-trace model-in-the-loop anchor handoff replay

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-trace-model-in-the-loop-anchor-handoff-replay-beddfe01f4`
Run ID: `real-trace-model-in-the-loop-anchor-handoff-replay-beddfe01f4-20260612T070124970741+0000`

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

- Parent run decision: Long-Context Anchor Memory for Agent Task Handoffs: enoch://control-plane/projects/long-context-anchor-memory-for-agent-task-handoffs-2a2ffe6cdf1b/runs/long-context-anchor-memory-for-agent-task-handoffs-2a2ffe6cdf1b-20260612T021728068048+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f0e02bdbdc90

## What looked useful

Anchor handoff summaries showed a directional recovery benefit in a corrected no-leakage control, improving 3/6 to 4/6 on both Qwen/Qwen2.5-0.5B-Instruct and Qwen/Qwen3-0.6B, but failed the predeclared +2/6 success threshold.

## Boundaries and scale limits

One project trace, hand-authored multiple-choice probes, two small local models, deterministic short generations, no frontier model, no live downstream task execution, and no broad trace diversity.

## Claim scope

In one local real Codex/Enoch worker trace replay with six redacted handoff probes, explicit anchor summaries produced a reproducible but sub-threshold +1/6 accuracy gain across two small cached instruction models.

## Why it stopped

Tier 1 controlled direct replay produced only a sub-threshold directional signal, not a validated or paper-positive result.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up on at least 30 independent real traces with automatic anchors and blinded held-out next-state probes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-trace automatic-anchor handoff replay benchmark
- Success threshold: With-anchor accuracy exceeds no-anchor accuracy by at least 10 percentage points overall and improves at least 60 percent of individual traces without increasing invalid responses.
- Stop condition: Stop if the first 30 traces show less than a 5 percentage point aggregate gain or if anchor-generated contexts cause more invalid/contradictory answers than the no-anchor control.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-model-in-the-loop-anchor-handoff-replay-beddfe01f4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
