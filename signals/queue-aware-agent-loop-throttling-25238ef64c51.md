# Queue-Aware Agent Loop Throttling

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `queue-aware-agent-loop-throttling-25238ef64c51`
Run ID: `queue-aware-agent-loop-throttling-25238ef64c51-20260529T231617851222+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ba9392f21335

## What looked useful

Queue-aware throttling was inactive or mildly beneficial at healthy load and strongly beneficial under overload: at 6.5 jobs/s it increased useful on-time completions from 715.1 for fixed_8 and 124.4 for fixed_12 to 813.5 per trace, and at 8.0 jobs/s from 423.6 and 73.6 to 938.1, while keeping p95 latency near 2.6s. It traded off mean quality at severe overload.

## Boundaries and scale limits

Synthetic/proxy-only evidence; no real LLM agent traces, no measured user quality labels, no production tool latency distribution, and no multi-tenant serving stack. The result supports a mechanism, not a paper-ready production claim.

## Claim scope

In a deterministic synthetic discrete-event queue with bursty arrivals, fixed worker capacity, diminishing returns from loop iterations, and deadline-scored useful completions, dispatch-time queue-aware loop budgets improved useful on-time completions under overload compared with fixed 8-loop and fixed 12-loop baselines.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic matched-trace proxy rather than direct production or real-agent validation.

## Recommended next action

Run a bounded deepen follow-up on real or recorded agent tasks with measured quality labels to test whether useful on-time completion gains persist against tuned fixed-loop and SLA-adaptive baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Trace Validation for Queue-Aware Loop Throttling
- Success threshold: Queue-aware throttling improves useful on-time completions by at least 10% over the best fixed-loop baseline and at least 5% over an SLA-adaptive baseline on overloaded traces, while mean quality drops by no more than 0.03 absolute.
- Stop condition: Stop if queue-aware throttling fails to beat the best fixed-loop baseline on useful on-time completions in a matched overloaded replay, or if quality loss exceeds the threshold even when latency improves.

## Evidence references

- Artifact root: `<local-path>/projects/queue-aware-agent-loop-throttling-25238ef64c51`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
