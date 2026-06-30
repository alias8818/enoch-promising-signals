# Real-Agent Trace Validation for Queue-Aware Loop Throttling

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-agent-trace-validation-for-queue-aware-loop-throttlin-1d2e416713`
Run ID: `real-agent-trace-validation-for-queue-aware-loop-throttlin-1d2e416713-20260530T030703410925+0000`

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

- Parent run decision: Queue-Aware Agent Loop Throttling: enoch://control-plane/projects/queue-aware-agent-loop-throttling-25238ef64c51/runs/queue-aware-agent-loop-throttling-25238ef64c51-20260529T231617851222+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ba9392f21335

## What looked useful

Queue-aware throttling beat fixed_8 on useful on-time completions at all tested loads and cut p95 latency by 2.40s to 99.46s in paired comparisons. It met the parent success threshold at the lowest tested load, but lost useful on-time completions to the SLA-adaptive baseline at loads 2.4, 3.2, and 4.0 jobs/s and exceeded the 0.03 mean-quality-drop threshold at higher loads.

## Boundaries and scale limits

Traffic arrivals, partial-quality interpolation, normalized service time, and queueing are controlled replay assumptions. The job catalog and final outcome labels are real local agent traces, but Codex JSONL did not provide timestamped per-event tool durations or direct per-budget quality labels. This is not live production validation or publication-grade evidence.

## Claim scope

On an 80-task local real-agent Enoch/Codex trace corpus replayed under matched bursty arrivals, dispatch-time queue-aware loop throttling improved p95 latency and useful on-time completions versus fixed 8-loop and fixed 12-loop baselines, but it did not consistently beat an SLA-adaptive loop-budget controller.

## Why it stopped

Direct-trace replay failed the stated follow-up threshold: queue-aware throttling did not improve useful on-time completions by at least 5% over the SLA-adaptive baseline across overloaded traces and quality loss exceeded the allowed bound at higher load.

## Recommended next action

Stop paper escalation for this policy as stated; a bounded next test should evaluate a hybrid queue-plus-SLA controller that relaxes the aggressive 3/5-loop modes when useful completion rate falls.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Hybrid Queue and SLA Feedback Loop Throttling on Real Agent Traces
- Success threshold: Hybrid queue-plus-SLA improves useful on-time completions by at least 5% over SLA-adaptive and at least 10% over the best fixed-loop baseline on at least 3 of 4 matched load levels, while mean quality drops by no more than 0.03 versus the best fixed-loop useful baseline.
- Stop condition: Stop if the hybrid controller cannot beat SLA-adaptive useful on-time completions on at least 2 overloaded load levels, or if its mean quality loss exceeds 0.03 even when latency improves.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-trace-validation-for-queue-aware-loop-throttlin-1d2e416713`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
