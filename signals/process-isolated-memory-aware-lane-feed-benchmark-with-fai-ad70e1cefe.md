# Process-isolated memory-aware lane feed benchmark with fairness controls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `process-isolated-memory-aware-lane-feed-benchmark-with-fai-ad70e1cefe`
Run ID: `process-isolated-memory-aware-lane-feed-benchmark-with-fai-ad70e1cefe-20260523T104533259574+0000`

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

- Parent run decision: Memory-Aware Lane Feed Pressure for Bounded CPU Work Generation: enoch://control-plane/projects/memory-aware-lane-feed-pressure-for-bounded-cpu-work-generation-bc0018350164/runs/memory-aware-lane-feed-pressure-for-bounded-cpu-work-generation-bc0018350164-20260523T102009162590+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8e30b7823e28

## What looked useful

The mechanism is supported as a bounded local scheduling result: adding fairness control to memory-aware feeding avoids high-memory lane starvation while still cutting peak process-local RSS substantially. It is not paper-positive because the evidence is synthetic and small-scale.

## Boundaries and scale limits

Synthetic 4-lane CPU-only benchmark, 3 repeats per policy, 10 seconds per policy-repeat, no cgroup memory limit, no real dataloader, no GPU/model consumer, no long-running service or multi-node validation.

## Claim scope

On a controlled local CPU benchmark with four process-isolated lane workers and synthetic per-lane payload allocations, memory-aware fair feeding reduced peak summed lane RSS by 55.52% versus equal-depth feeding while preserving normalized Jain fairness within 0.001 and avoiding the largest-lane starvation seen in memory-only throughput scheduling.

## Why it stopped

Tier 1 controlled small direct test completed with useful mechanism support, but evidence remains synthetic/local and below paper-readiness.

## Recommended next action

Run a bounded deepen test under cgroup memory pressure with a real file-backed or dataloader-like workload, using the same three-policy comparison and explicit starvation threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cgroup-limited real-payload lane feed validation
- Success threshold: mem_fair reduces peak worker RSS by >=35% versus naive_depth, Jain fairness is no worse than 0.03 below naive_depth, no lane has zero completions, and throughput loss versus naive_depth is <=15%.
- Stop condition: Stop as unsupported if mem_fair fails the RSS reduction threshold, causes any zero-completion lane, or loses more than 15% throughput versus naive_depth in two or more repeats.

## Evidence references

- Artifact root: `<local-path>/projects/process-isolated-memory-aware-lane-feed-benchmark-with-fai-ad70e1cefe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
