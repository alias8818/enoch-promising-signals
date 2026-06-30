# Memory-Aware Lane Feed Pressure for Bounded CPU Work Generation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `memory-aware-lane-feed-pressure-for-bounded-cpu-work-generation-bc0018350164`
Run ID: `memory-aware-lane-feed-pressure-for-bounded-cpu-work-generation-bc0018350164-20260523T102009162590+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8e30b7823e28

## What looked useful

Across 20 seeds and memory caps of 512, 768, 1024, and 1536 MiB, memory-aware admission had zero simulated memory breaches and peak/cap about 0.987 while count-only baselines exceeded the cap by 8.25x to 24.75x. Worker utilization stayed about 0.999, but Jain lane fairness dropped to 0.814-0.906 versus 0.997 for naive_count, showing a real fairness/task-mix tradeoff.

## Boundaries and scale limits

Evidence is synthetic plus a small RSS smoke. It does not cover real OOM/earlyoom behavior, measured MemAvailable feedback, cgroup enforcement, production scheduler overhead, long steady-state operation, or realistic application work quality.

## Claim scope

In a bounded event simulation of 8 CPU work lanes and 8 workers, memory-aware lane admission kept queued-plus-running simulated resident memory below fixed caps while preserving worker utilization; the result is a mechanism signal, not a production or paper-grade validation.

## Why it stopped

Closed as no-paper useful signal because the primary support is a bounded simulator and the small RSS smoke is only a proxy, not direct full-system validation.

## Recommended next action

Run a process-isolated real producer/consumer benchmark with cgroup or MemAvailable-driven admission and fairness-controlled useful-work metrics before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Process-isolated memory-aware lane feed benchmark with fairness controls
- Success threshold: Memory-aware policy has zero memory-budget breaches, at least 90% worker utilization, at least 85% weighted useful-work throughput versus the best feasible baseline, and Jain lane fairness at least 0.95 across at least 5 seeds and 3 memory caps.
- Stop condition: Stop as negative if memory-aware admission breaches budget in any repeated run, drops weighted useful-work throughput below 85% of baseline, or cannot reach Jain fairness 0.95 without losing the memory bound.

## Evidence references

- Artifact root: `<local-path>/projects/memory-aware-lane-feed-pressure-for-bounded-cpu-work-generation-bc0018350164`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
