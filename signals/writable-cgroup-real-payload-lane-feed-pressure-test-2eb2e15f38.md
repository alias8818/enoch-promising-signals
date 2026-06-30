# Writable-cgroup real-payload lane feed pressure test

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `33`
Project ID: `writable-cgroup-real-payload-lane-feed-pressure-test-2eb2e15f38`
Run ID: `writable-cgroup-real-payload-lane-feed-pressure-test-2eb2e15f38-20260523T140932798755+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `33`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -5, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Process-isolated memory-aware lane feed benchmark with fairness controls: enoch://control-plane/projects/process-isolated-memory-aware-lane-feed-benchmark-with-fai-ad70e1cefe/runs/process-isolated-memory-aware-lane-feed-benchmark-with-fai-ad70e1cefe-20260523T104533259574+0000
- Parent run decision: Cgroup-limited real-payload lane feed validation: enoch://control-plane/projects/cgroup-limited-real-payload-lane-feed-validation-b5a88184db/runs/cgroup-limited-real-payload-lane-feed-validation-b5a88184db-20260523T105542815665+0000

## What looked useful

The writable-cgroup lane-feed mechanism is not viable in the current deployment because the necessary writable control surface is absent. Real-payload baseline and adaptive runs both completed 2519 tasks; adaptive p95 latency was 0.90% worse and memory PSI deltas were zero, so the adaptive mechanism had no pressure signal to act on.

## Boundaries and scale limits

Tested one local CPU worker service cgroup, 8 available CPUs, two 90-second medium cases, 1 MiB compression/hash payloads, 4 GiB touched memory stress, and no delegated cgroup control. This is not a multi-host or datacenter-scale scheduling result.

## Claim scope

On this CPU worker's actual cgroup v2 service slice, unprivileged worker code cannot create child cgroups, cannot set memory.high, cannot enable subtree controls, and did not obtain usable memory PSI trigger behavior; a bounded real-payload PSI-read adaptive feeder produced no improvement over fixed feed under 4 GiB memory stress.

## Why it stopped

Direct permission and real-payload tests falsified the required local mechanism rather than merely failing to scale it.

## Recommended next action

Stop this branch for the current worker deployment; only retry if the service is explicitly delegated a writable child cgroup with memory/cpu controllers and a validated PSI trigger registration path.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/writable-cgroup-real-payload-lane-feed-pressure-test-2eb2e15f38`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
