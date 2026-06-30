# Live Real Agent Task Queue Pressure With Correctness Grading

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-real-agent-task-queue-pressure-with-correctness-gradi-08eeec6658`
Run ID: `live-real-agent-task-queue-pressure-with-correctness-gradi-08eeec6658-20260531T202840930216+0000`

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

- Parent run decision: Replay Real Agent Tasks Under Controlled Queue Pressure: enoch://control-plane/projects/replay-real-agent-tasks-under-controlled-queue-pressure-0a3fd4efcd/runs/replay-real-agent-tasks-under-controlled-queue-pressure-0a3fd4efcd-20260531T111743658129+0000
- Parent run decision: Agent Reliability Degradation Under Queue Pressure: enoch://control-plane/projects/agent-reliability-degradation-under-queue-pressure-d18e6c50e6c8/runs/agent-reliability-degradation-under-queue-pressure-d18e6c50e6c8-20260530T063313402874+0000

## What looked useful

Across 6 fixed seeds, 5 utilization levels, 3 deadline multipliers, and no-wait controls, FIFO deadline correctness dropped from low to high utilization by 7.31 pp at 1.5x, 9.63 pp at 2.0x, and 5.65 pp at 3.0x while high-utilization no-wait-penalty loss stayed within about 0.4 pp of isolated baseline in aggregate.

## Boundaries and scale limits

The worker is not an LLM/Codex agent, tasks are arithmetic search puzzles rather than real user or coding tasks, arrivals are synthetic, and deadlines are derived from estimated median service time. Evidence does not cover production queues, semantic grading, model/tool failures, retries, or human-facing task quality.

## Claim scope

In a bounded live CPU task harness with deterministic anytime search workers, exact-answer grading, fixed seeds, and virtual FIFO queue scheduling, high queue utilization reduces deadline-conditioned correctness because queue wait consumes fixed arrival-to-deadline budget.

## Why it stopped

Tier 2 bounded live-task evidence supports the queue/deadline correctness mechanism, but it remains a simplified proxy and is not sufficient for a paper-level real-agent claim.

## Recommended next action

Deepen with actual LLM/Codex-style tasks that have unit-test or auditable rubric grading under the same fixed-seed queue pressure design.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM Agent Queue Pressure With Unit-Test Correctness Grading
- Success threshold: At least two realistic deadline multipliers show >=2 percentage-point correctness loss from low to high utilization under FIFO deadline pressure, p95 wait increases monotonically or clearly with utilization, and the no-wait-penalty control stays within 2 percentage points of isolated correctness.
- Stop condition: Stop if isolated correctness is too low for meaningful pressure measurement, task execution cannot be made deterministic enough for paired comparison, or the no-wait-penalty control also degrades by more than 2 percentage points, indicating confounding unrelated to queue wait.

## Evidence references

- Artifact root: `<local-path>/projects/live-real-agent-task-queue-pressure-with-correctness-gradi-08eeec6658`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
