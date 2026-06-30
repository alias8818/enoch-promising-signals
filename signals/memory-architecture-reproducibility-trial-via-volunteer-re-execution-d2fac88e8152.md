# Memory Architecture Reproducibility Trial via Volunteer Re-Execution

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `memory-architecture-reproducibility-trial-via-volunteer-re-execution-d2fac88e8152`
Run ID: `memory-architecture-reproducibility-trial-via-volunteer-re-execution-d2fac88e8152-20260611T145659636436+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e509d1003508

## What looked useful

Sequential bandwidth was reproducible across tested sizes and large-vs-small pointer-chase latency contrast was 76.61x, but pointer-chase CV exceeded 15% at 4 MiB and 16 MiB, including a same-seed control.

## Boundaries and scale limits

Single machine only; no cross-volunteer cohort, no privileged hardware counters, no CPU isolation/frequency controls, no page-size controls, and no full memory-architecture validation.

## Claim scope

On one CPU worker, a portable volunteer-reexecution memory benchmark recovered a strong coarse cache-to-DRAM latency contrast, but failed the predeclared all-size reproducibility threshold because transition-size pointer-chase latency was unstable.

## Why it stopped

Proxy/local volunteer re-execution recovered coarse regime contrast but failed the predeclared reproducibility threshold, so this is an early bounded falsification rather than a full validation.

## Recommended next action

Stop this run as no-paper useful signal; deepen with a controlled pointer-chase diagnostic using perf counters, CPU isolation/frequency controls, and THP/page-size reporting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Controlled pointer-chase reproducibility diagnostics for transition-size working sets
- Success threshold: Transition-size pointer-chase CV below 0.15 at both 4 MiB and 16 MiB, or a counter-backed explanation showing that the instability is a reproducible platform effect.
- Stop condition: Stop if controlled runs still exceed 0.15 CV without a consistent counter-level explanation, or if perf/CPU isolation is unavailable on the worker.

## Evidence references

- Artifact root: `<local-path>/projects/memory-architecture-reproducibility-trial-via-volunteer-re-execution-d2fac88e8152`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
