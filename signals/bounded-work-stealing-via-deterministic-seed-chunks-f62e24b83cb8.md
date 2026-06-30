# Bounded Work Stealing via Deterministic Seed Chunks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-work-stealing-via-deterministic-seed-chunks-f62e24b83cb8`
Run ID: `bounded-work-stealing-via-deterministic-seed-chunks-f62e24b83cb8-20260601T061741524768+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7c1ce4c99f51

## What looked useful

At the first budget recovering at least 80% of dynamic gain, bounded stealing improved median makespan by 16.4% to 29.6% versus static assignment while moving 183.5 to 376 of 4096 chunks per trial.

## Boundaries and scale limits

Simulation only; no real multiprocessing, distributed runtime, GPU workload, scheduler contention, cache effects, failure recovery, or production trace validation was tested.

## Claim scope

Deterministic simulation over 16 workers, 4096 fixed seed chunks, 24 seeds, and four synthetic runtime distributions shows bounded deterministic stealing can recover at least 80% of centralized dynamic scheduling's median speedup over static assignment with bounded steal traffic.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy simulation, not direct scheduler/runtime validation.

## Recommended next action

Run a bounded real-runtime follow-up using multiprocessing or a small distributed executor with fixed seed chunks, assignment-log replay checks, and scheduler-overhead measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-runtime validation of deterministic bounded seed-chunk stealing
- Success threshold: Across at least three workloads, bounded stealing recovers >=75% of dynamic scheduling's makespan gain over static assignment, steals <=10% of chunks, and has replay-identical assignment digests.
- Stop condition: Stop if bounded stealing recovers <50% of dynamic scheduling's gain on two workloads or if scheduler overhead exceeds the saved runtime.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-work-stealing-via-deterministic-seed-chunks-f62e24b83cb8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
