# Calibrated Verifier Cache-Cost Scheduling Test

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `calibrated-verifier-cache-cost-scheduling-test-f3743cc2fb`
Run ID: `calibrated-verifier-cache-cost-scheduling-test-f3743cc2fb-20260522T065625951455+0000`

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

- Parent run decision: Heterogeneous Real-Trace Verifier Shard Scheduling: enoch://control-plane/projects/heterogeneous-real-trace-verifier-shard-scheduling-6da291fae9/runs/heterogeneous-real-trace-verifier-shard-scheduling-6da291fae9-20260522T020904507296+0000
- Parent run decision: Distributed Verifier Shards: enoch://control-plane/projects/distributed-verifier-shards-39aa7e742d8d/runs/distributed-verifier-shards-39aa7e742d8d-20260521T223852892600+0000

## What looked useful

The scheduler is a useful mechanism candidate but its apparent gains are small once strong SPT/cache-only and probability-only baselines are included. Future work should keep those baselines and require real measured cache costs before claiming novelty.

## Boundaries and scale limits

Synthetic workload only; no real verifier traces, no measured LLM KV/cache costs, no live serving latency, and no end-to-end model quality evaluation. CPU-only local run completed in 22.94 seconds, so this is Tier 2 mechanism evidence rather than full-scale validation.

## Claim scope

In a reproducible 20-seed online simulator with 6,000 verifier tasks per seed, calibrated expected-utility over cache-aware marginal cost beats FIFO and slightly beats SPT/cache-only in the calibrated-cache setting, but it does not robustly separate from probability-only or no-cache ablations.

## Why it stopped

Tier 2 evidence is mixed and not paper-positive: the mechanism beats FIFO and slightly beats SPT/cache-only, but gains over probability-only and no-cache ablations are too small or uncertain in key scenarios.

## Recommended next action

Run a bounded real-trace replay or small LLM verifier workload with measured cache warm/cold costs; stop if calibrated cache-cost scheduling fails to beat both probability-only and SPT/cache-only by at least 5% expected utility and 2 percentage points wrong-answer recall.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace Calibrated Verifier Cache-Cost Replay
- Success threshold: Primary policy beats both probability-only and SPT/cache-only by >=5% expected utility and >=2 percentage points wrong-answer recall with paired 95% confidence intervals excluding zero in the main real-trace scenario.
- Stop condition: Stop as no-paper if gains over either strong baseline are below threshold or confidence intervals include zero after the fixed replay budget.

## Evidence references

- Artifact root: `<local-path>/projects/calibrated-verifier-cache-cost-scheduling-test-f3743cc2fb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
