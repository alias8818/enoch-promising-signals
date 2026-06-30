# Multi-process CPU ZeRO-1 rank-local RSS validation for tiny GPT training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `multi-process-cpu-zero-1-rank-local-rss-validation-for-tin-0c006214cc`
Run ID: `multi-process-cpu-zero-1-rank-local-rss-validation-for-tin-0c006214cc-20260620T063642138413+0000`

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

- Parent run decision: Bounded CPU-only ZeRO-style optimizer state sharding for tiny GPT-2-class training: enoch://control-plane/projects/bounded-cpu-only-zero-style-optimizer-state-sharding-for-tiny-gpt-2-class-training-e53a60ef20d3/runs/bounded-cpu-only-zero-style-optimizer-state-sharding-for-tiny-gpt-2-class-training-e53a60ef20d3-20260620T061622238735+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a4517dea9a45

## What looked useful

The Tier 1 direct test supports the local RSS mechanism: optimizer-state sharding produced the expected 4-way state reduction and a measurable rank-local RSS reduction without changing final loss in the controlled setup.

## Boundaries and scale limits

Short 4-step synthetic run on a tiny GPT model; no real corpus, no GPT-2-small-class scale, no production ZeRO implementation, no checkpoint/resume, no long-run convergence, and no rank-distinct batches with gradient all-reduce.

## Claim scope

In a controlled four-process CPU tiny-GPT synthetic training run, a ZeRO-1-style rank-local Adam state shard reduced per-rank optimizer state by 75.00% and mean peak RSS by 20.41% versus replicated Adam while preserving the isolated loss trajectory.

## Why it stopped

Closed as no-paper useful Tier 1 evidence: the result directly validates the small controlled RSS mechanism, but the scale and training realism are insufficient for publication readiness.

## Recommended next action

Run a bounded deepen follow-up using rank-distinct batches with explicit gradient all-reduce or PyTorch ZeroRedundancyOptimizer, and require the RSS reduction to persist without loss drift.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Rank-distinct CPU ZeRO-1 tiny GPT RSS and convergence validation
- Success threshold: At least 15% lower mean peak rank-local RSS for ZeRO-1 than replicated Adam, expected near-4x optimizer-state reduction, and final loss within 1% of baseline over at least 32 bounded CPU training steps.
- Stop condition: Stop if the RSS reduction is below 10%, optimizer state is not actually sharded, synchronized training diverges beyond 2% final-loss drift, or the run projects beyond the local CPU budget.

## Evidence references

- Artifact root: `<local-path>/projects/multi-process-cpu-zero-1-rank-local-rss-validation-for-tin-0c006214cc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
