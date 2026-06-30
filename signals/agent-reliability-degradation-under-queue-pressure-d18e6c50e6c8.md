# Agent Reliability Degradation Under Queue Pressure

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-reliability-degradation-under-queue-pressure-d18e6c50e6c8`
Run ID: `agent-reliability-degradation-under-queue-pressure-d18e6c50e6c8-20260530T063313402874+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d04a9c2427be

## What looked useful

The no-deadline control stayed flat within 0.108 percentage points across utilization, while deadline-conditioned pressure loss rose monotonically. At 45s deadline, pressure loss rose from 0.27 pp at 0.35 utilization to 3.80 pp at 0.97. At 30s deadline, pressure loss rose from 1.77 pp to 7.23 pp, with the >=5 pp loss threshold reached at 0.92 utilization.

## Boundaries and scale limits

No real LLM agents, production traces, tool calls, retries, admission control, adaptive scheduling, or human correctness rubric were tested. Results cover 4 synthetic workers, 8 replicates, 10000 measured tasks per utilization per deadline condition, and deadlines of 30s and 45s.

## Claim scope

Bounded synthetic discrete-event agent-harness proxy: fixed intrinsic task correctness, Poisson arrivals, fixed worker pool, and deadline-conditioned task success. Queue pressure degrades measured reliability when queue wait consumes the remaining deadline budget.

## Why it stopped

No-paper useful signal: the local synthetic proxy supports the queue/deadline mechanism but is not direct production-agent evidence.

## Recommended next action

Run a bounded replay experiment with a real local or logged agent workload under controlled arrival rates, fixed model/tooling, per-task correctness labels, queue wait, timeout, and retry telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay Real Agent Tasks Under Controlled Queue Pressure
- Success threshold: At least a 5 percentage point monotonic increase in deadline-conditioned reliability loss between low utilization and high utilization, with no-deadline correctness varying by less than 2 percentage points and timeout/wait telemetry explaining most of the loss.
- Stop condition: Stop as negative if deadline-conditioned loss is below 2 percentage points at high utilization or if no-deadline correctness shifts by more than the pressure effect, making queue pressure non-identifiable.

## Evidence references

- Artifact root: `<local-path>/projects/agent-reliability-degradation-under-queue-pressure-d18e6c50e6c8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
