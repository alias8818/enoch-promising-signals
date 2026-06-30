# Bounded Work Queue with Exact Anchor Anchoring

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-work-queue-with-exact-anchor-anchoring-71bd01f19327`
Run ID: `bounded-work-queue-with-exact-anchor-anchoring-71bd01f19327-20260611T024921829887+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/aa8425bcdf2b

## What looked useful

Exact anchoring was the correctness-critical mechanism; fuzzy repeated-section anchoring produced 949 wrong-location edits and left 15,872 of 16,384 intended targets unchanged. Bounded queueing independently reduced peak RSS from 89,852 KB to 21,456 KB for exact anchoring.

## Boundaries and scale limits

Synthetic Python benchmark only; no production traces, no stronger contextual fuzzy baseline, no multi-process serving, no file I/O or network pressure, and no large-scale editor integration.

## Claim scope

On a synthetic 16,384-edit text workload with repeated fuzzy section labels and 4 KB queued payloads, exact unique anchors eliminated wrong-location edits, and a bounded queue reduced peak RSS by 76.1% versus an unbounded materialized queue with a 4.9% throughput cost.

## Why it stopped

No-paper closure: the local synthetic result supports the mechanism but is not direct production or publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up that replays real or trace-derived edit streams against exact anchors and stronger contextual anchoring baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace replay for exact anchor anchoring under bounded queues
- Success threshold: Exact anchors achieve at least 99.9% correct-target edits with zero wrong-target edits, bounded queue peak RSS is at least 50% lower than unbounded, and throughput loss is no more than 10% on the replay workload.
- Stop condition: Stop if exact anchoring shows any reproducible wrong-target edit, if bounded queue memory savings fall below 25%, or if throughput loss exceeds 20% after basic queue-size tuning.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-work-queue-with-exact-anchor-anchoring-71bd01f19327`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
