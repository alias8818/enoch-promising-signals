# Deterministic-Replay Gradient Verification on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `deterministic-replay-gradient-verification-on-cpu-d87145400ce6`
Run ID: `deterministic-replay-gradient-verification-on-cpu-d87145400ce6-20260610T144111964244+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b0deda3113ea

## What looked useful

Deterministic CPU replay plus full-gradient hashing is a cheap exact integrity check for this small NumPy workload, while sampled finite differences add formula-level coverage at selected coordinates. The mechanism is useful but not broad or publication-grade.

## Boundaries and scale limits

No autograd framework, process-restart replay, optimizer-state replay, real dataset, cross-host CPU, GPU, distributed, mixed-precision, or large-model validation was run. Finite-difference detection is sampled and tolerance-limited; replay hashes detect corruption relative to a clean deterministic rerun but do not by themselves prove a deterministic gradient formula is correct.

## Claim scope

On one CPU worker, a NumPy two-layer MLP with recorded seeds, parameters, and synthetic batches replayed analytic gradients bitwise across tiny/small/medium configs; sampled central finite differences agreed within about 4.1e-11 absolute error and detected injected checked-coordinate faults at practical magnitudes.

## Why it stopped

Local bounded mechanism supported, but evidence is synthetic NumPy-only and insufficient for paper-positive closure.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement the same replay/hash/finite-difference protocol in an autograd framework with process restart and realistic RNG/data-loader controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Framework-level deterministic CPU gradient replay with process restarts
- Success threshold: Across at least 20 fresh-process replays per model, gradient hashes are identical under deterministic settings; finite-difference max absolute error stays below 1e-6 for sampled coordinates; injected checked-coordinate gradient faults of 1e-5 are detected.
- Stop condition: Stop if the framework cannot support Python/CPU installation locally, if deterministic replay fails after documented deterministic settings, or if the full follow-up would exceed the local CPU worker budget without producing process-restart metrics.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-replay-gradient-verification-on-cpu-d87145400ce6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
