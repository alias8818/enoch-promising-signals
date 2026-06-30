# Bounded Queue Backpressure for CPU Worker Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-queue-backpressure-for-cpu-worker-reliability-3be8504e0f2c`
Run ID: `bounded-queue-backpressure-for-cpu-worker-reliability-3be8504e0f2c-20260621T062202040799+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/7933f37160e7

## What looked useful

Unbounded admission accepted 3599 tasks but completed only 2609 after a 4 second drain, abandoned 990, reached depth 1793, max RSS 114.652 MiB, and p95 latency 5.982521 s. Bounded blocking completed all 1666 accepted tasks with depth 128, max RSS 26.602 MiB, and p95 latency 0.691867 s. Bounded dropping completed all 1929 accepted tasks, dropped 1671 explicitly, held depth 128, max RSS 26.680 MiB, and p95 latency 0.607265 s.

## Boundaries and scale limits

Synthetic in-process harness only; not validated in the production Enoch CPU worker, process pools, real task payloads, retry/cancellation semantics, or sustained long-duration overload.

## Claim scope

In a deterministic local Python CPU-worker overload harness, bounded queue admission capped queue depth and reduced RSS/tail latency versus unbounded admission while preserving completion for accepted tasks through blocking or explicit dropping.

## Why it stopped

Synthetic local evidence supports the mechanism but is not direct production-worker validation or publication-grade evidence.

## Recommended next action

Stop this run as no-paper useful evidence; next implement the same bounded admission policies in the actual CPU worker and replay representative jobs with process-level memory, latency, retry, and cancellation telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded admission replay in the actual CPU worker runtime
- Success threshold: Bounded modes keep max queue depth at the configured cap, reduce peak RSS by at least 2x versus unbounded, reduce p95 accepted-task latency by at least 2x, and complete all accepted non-cancelled tasks during recovery.
- Stop condition: Stop if bounded modes do not improve both peak RSS and p95 latency by at least 2x versus unbounded, or if retry/cancellation semantics make task loss ambiguous.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-queue-backpressure-for-cpu-worker-reliability-3be8504e0f2c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
