# LLM Agent Queue Pressure With Unit-Test Correctness Grading

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `llm-agent-queue-pressure-with-unit-test-correctness-gradin-38e18ac1da`
Run ID: `llm-agent-queue-pressure-with-unit-test-correctness-gradin-38e18ac1da-20260601T033520929302+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Replay Real Agent Tasks Under Controlled Queue Pressure: enoch://control-plane/projects/replay-real-agent-tasks-under-controlled-queue-pressure-0a3fd4efcd/runs/replay-real-agent-tasks-under-controlled-queue-pressure-0a3fd4efcd-20260531T111743658129+0000
- Parent run decision: Live Real Agent Task Queue Pressure With Correctness Grading: enoch://control-plane/projects/live-real-agent-task-queue-pressure-with-correctness-gradi-08eeec6658/runs/live-real-agent-task-queue-pressure-with-correctness-gradi-08eeec6658-20260531T202840930216+0000

## What looked useful

Across three fixed seeds and 720 total grading jobs, isolated grading had 0/483 correct-submission false negatives, while 32-way FIFO pressure had 477/483 false negatives. Capping concurrency at 8 reduced this to 2/483, and a generous 32-way timeout reduced it to 0/483. No condition produced false positives.

## Boundaries and scale limits

Synthetic candidate programs and unittest workloads only; no real LLM-generated patches, real repository test suites, production queue traces, distributed services, or multi-host validation. Evidence supports the local timeout-pressure mechanism, not a broad paper-ready claim about all LLM-agent graders.

## Claim scope

On an 8-core local host with deterministic synthetic Python unit-test grading jobs, 32-way FIFO grader queue pressure with a timeout calibrated from isolated baseline runtime caused timeout-driven false negative grades for known-correct submissions; concurrency capping and generous timeout controls largely or completely removed the distortion.

## Why it stopped

The local bounded validation supports the mechanism but remains synthetic and therefore is not publication-grade direct evidence for production LLM-agent correctness grading.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded deepen test should replay real LLM-agent submissions or real repository unit-test suites under the same queue-pressure/control design.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-submission queue-pressure grading replay
- Success threshold: On at least 300 known-correct real submissions or patch-test pairs, high-pressure FIFO increases false negative rate by at least 5 percentage points over isolated grading, while a bounded mitigation reduces at least 80% of the excess false negatives with no statistically meaningful false-positive increase.
- Stop condition: Stop if isolated grading is not stable enough to establish ground truth, if high-pressure FIFO changes false negative rate by less than 2 percentage points, or if errors are dominated by flaky tests rather than queue-induced timeout/runtime pressure.

## Evidence references

- Artifact root: `<local-path>/projects/llm-agent-queue-pressure-with-unit-test-correctness-gradin-38e18ac1da`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
