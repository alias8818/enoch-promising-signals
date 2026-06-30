# Real-trace bounded queue pressure validation for memory consolidation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-bounded-queue-pressure-validation-for-memory-co-504d79a26e`
Run ID: `real-trace-bounded-queue-pressure-validation-for-memory-co-504d79a26e-20260620T074600855499+0000`

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

- Parent run decision: Bounded Queue Feed Pressure for Memory Consolidation: enoch://control-plane/projects/bounded-queue-feed-pressure-for-memory-consolidation-f2fa7cdf26e3/runs/bounded-queue-feed-pressure-for-memory-consolidation-f2fa7cdf26e3-20260620T071722509259+0000
- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/8326b63f3b9a

## What looked useful

Across 63 policy runs, bounded_consolidate_oldest had 27/27 zero-drop bounded-consolidate runs, no invariant failures, and max queue length equal to the tested cap, while bounded_drop_new reached a 0.74875 drop rate and unbounded replay reached 2400 queued items.

## Boundaries and scale limits

One local trace, 64 base events at run time, metadata-only payload sizes, no wall-clock arrival timestamps, no retrieval-quality scoring, no live multi-session memory agent, and pressure partly amplified by trace repetition.

## Claim scope

A small ordered local Codex worker event-trace replay supports the mechanism that bounded oldest-item consolidation can hold a memory-consolidation queue cap without dropping work under controlled pressure.

## Why it stopped

Tier 1 controlled direct replay completed and produced useful mechanism evidence, but the evidence is too narrow and partly pressure-amplified for publication readiness.

## Recommended next action

Run a deepen follow-up on several real timestamped multi-session memory traces with retrieval-quality scoring and live queue telemetry; do not write a paper from this Tier 1 metadata replay alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Timestamped multi-session bounded consolidation queue validation
- Success threshold: For every trace and tested pressure level, bounded_consolidate_oldest has zero drops, no queue-cap violations, at least 10x lower peak queued bytes than unbounded under pressure, and retrieval quality no worse than 5 percent below unbounded.
- Stop condition: Stop as unsupported if bounded consolidation drops any event, violates the configured cap, or reduces retrieval quality by more than 5 percent versus unbounded on two or more traces.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-bounded-queue-pressure-validation-for-memory-co-504d79a26e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
