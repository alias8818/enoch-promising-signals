# Bounded Retry Memory Architecture

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-retry-memory-architecture-ad3d3be769c0`
Run ID: `bounded-retry-memory-architecture-ad3d3be769c0-20260610T054001434180+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/313a4d193b87

## What looked useful

Bounded retry is a useful latency-bounded improvement over single-shot memory retrieval, with k5 mean success 0.886 versus single-shot 0.500 and max p95 attempts 5. However, capped-unbounded retry achieved higher mean success 0.940 and won utility in 246/270 main-seed conditions, so the broad architecture claim is not supported.

## Boundaries and scale limits

Synthetic-only evidence over 270 parameter conditions and two random seeds; no learned memory model, no real agent benchmark, no learned verifier calibration, and no real wall-clock serving latency measurement.

## Claim scope

In a synthetic retrieval/verifier model with independent retry attempts, bounded retry budgets k=2..5 reliably improve success and accepted-wrong rates over single-shot lookup, but k=5 rarely maximizes utility against a capped-unbounded retry policy under the tested cost model.

## Why it stopped

Synthetic mechanism evidence supports bounded retry over single-shot but not a broad paper-ready architecture claim; this is proxy evidence, not full validation.

## Recommended next action

Stop this run as a no-paper synthetic useful signal; the concrete next test is a bounded real memory-agent benchmark comparing single-shot, k5, and larger retry budgets under equal wall-clock latency accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded Retry in a Real Memory-Agent Benchmark
- Success threshold: Bounded k5 must achieve at least 95% of the larger-budget accuracy while reducing p95 latency or p95 attempts by at least 20%, and must beat single-shot utility by at least 10%.
- Stop condition: Stop if bounded k5 fails to beat single-shot by 10% utility or fails to reach 95% of larger-budget accuracy on the first complete benchmark shard.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-retry-memory-architecture-ad3d3be769c0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
