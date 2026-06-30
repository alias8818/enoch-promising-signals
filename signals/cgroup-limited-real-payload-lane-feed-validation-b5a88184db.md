# Cgroup-limited real-payload lane feed validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cgroup-limited-real-payload-lane-feed-validation-b5a88184db`
Run ID: `cgroup-limited-real-payload-lane-feed-validation-b5a88184db-20260523T105542815665+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Process-isolated memory-aware lane feed benchmark with fairness controls: enoch://control-plane/projects/process-isolated-memory-aware-lane-feed-benchmark-with-fai-ad70e1cefe/runs/process-isolated-memory-aware-lane-feed-benchmark-with-fai-ad70e1cefe-20260523T104533259574+0000
- Parent run decision: Memory-Aware Lane Feed Pressure for Bounded CPU Work Generation: enoch://control-plane/projects/memory-aware-lane-feed-pressure-for-bounded-cpu-work-generation-bc0018350164/runs/memory-aware-lane-feed-pressure-for-bounded-cpu-work-generation-bc0018350164-20260523T102009162590+0000

## What looked useful

Tier-2-shaped local confirmation with fixed seed 20260523, three repeats, real payload corpus, equal-depth baseline, byte-cap FIFO control, memory-throughput ablation, and direct RSS/cgroup telemetry. mem_fair achieved 123.83 items/s, fairness 0.5462, and 1115.78 MiB peak RSS versus naive_depth at 112.07 items/s, fairness 0.5510, and 1405.69 MiB peak RSS; mem_throughput starved the xlarge lane.

## Boundaries and scale limits

The worker could read service cgroup v2 telemetry but could not create a child cgroup or set MemoryMax; the parent service cgroup had memory.max=max and memory.high=max. Results do not validate enforced cgroup pressure, OOM behavior, production dataloaders, GPU/model consumers, or multi-node runtime.

## Claim scope

In a CPU-only process-isolated benchmark using real local Enoch artifact payload bytes, a memory-aware fair lane feeder reduced peak summed lane RSS by 20.62% versus an equal-depth baseline while preserving nearly identical completion fairness and avoiding the large-lane starvation of memory-only controls.

## Why it stopped

Moderate real-payload evidence supports the feeder mechanism, but the requested cgroup-limited validation was only telemetered, not enforced, because unprivileged cgroup limit creation was denied.

## Recommended next action

Stop this branch as no-paper useful signal; rerun the same benchmark on a runner with delegated cgroup v2 child creation or systemd transient MemoryMax permission before making any cgroup-limited claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Writable-cgroup real-payload lane feed pressure test
- Success threshold: mem_fair has zero cgroup OOM kills/high-limit breaches, at least 15% lower peak memory.current or summed lane RSS than naive_depth, at least 80% of naive_depth throughput, fairness delta no worse than -0.03, and nonzero xlarge completions in every repeat.
- Stop condition: Stop as unsupported if cgroup limits cannot be enforced, if mem_fair triggers any cgroup OOM kill/high breach under the configured limit, if its peak memory reduction is below 15%, or if it starves the xlarge lane in any repeat.

## Evidence references

- Artifact root: `<local-path>/projects/cgroup-limited-real-payload-lane-feed-validation-b5a88184db`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
