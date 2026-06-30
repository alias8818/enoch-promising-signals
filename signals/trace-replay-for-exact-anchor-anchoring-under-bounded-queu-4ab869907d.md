# Trace replay for exact anchor anchoring under bounded queues

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-replay-for-exact-anchor-anchoring-under-bounded-queu-4ab869907d`
Run ID: `trace-replay-for-exact-anchor-anchoring-under-bounded-queu-4ab869907d-20260611T031057967189+0000`

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

- Parent run decision: Bounded Work Queue with Exact Anchor Anchoring: enoch://control-plane/projects/bounded-work-queue-with-exact-anchor-anchoring-71bd01f19327/runs/bounded-work-queue-with-exact-anchor-anchoring-71bd01f19327-20260611T024921829887+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/aa8425bcdf2b

## What looked useful

The capacity threshold is crisp in the controlled model: 0 mismatches across 631 cases. Capacity below the event gap causes eviction and failure; non-unique keys cause ambiguity independent of capacity.

## Boundaries and scale limits

Small synthetic direct traces only: 631 cases, max trace length 65, no production trace corpus, no concurrency, no distributed queues, no persistence failure, and no real application integration.

## Claim scope

In deterministic controlled traces with unique anchor occurrence ids, bounded FIFO replay recovers exact anchors exactly when queue capacity is at least the anchor-to-resolve event gap; duplicate live keys remain ambiguous even with sufficient capacity.

## Why it stopped

Tier 1 controlled small direct test completed with mechanism support, but evidence is synthetic and not publication-grade.

## Recommended next action

Run a bounded deepen follow-up on a real or richer generated trace corpus with known ground-truth anchor occurrences, including concurrent/reordered events and queue capacity sweeps.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Ground-truth trace corpus replay for exact anchor recovery under queue bounds
- Success threshold: At least 99.9% exact recovery with occurrence ids at capacity >= p99.9 gap, zero unexplained misses in audited failures, and clear failure of key-only baseline on duplicate-key controls.
- Stop condition: Stop if occurrence-id replay misses anchors despite sufficient capacity on audited traces, or if the corpus lacks ground-truth occurrence ids needed to judge exactness.

## Evidence references

- Artifact root: `<local-path>/projects/trace-replay-for-exact-anchor-anchoring-under-bounded-queu-4ab869907d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
