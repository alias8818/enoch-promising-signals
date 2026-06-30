# Prompt-conditioned CPU batch scheduling for local serving

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `prompt-conditioned-cpu-batch-scheduling-for-local-serving-71c10c1264f0`
Run ID: `prompt-conditioned-cpu-batch-scheduling-for-local-serving-71c10c1264f0-20260604T170321134696+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7e3d08743ebf

## What looked useful

Predicted-decode bucketing averaged 82.4% p95 improvement vs FIFO on correlated workloads and 78.7% on weakly correlated workloads, while the uncorrelated control regressed by 34.8%; sensitivity runs with batch size 4 and 200 ms batching windows preserved the same sign pattern.

## Boundaries and scale limits

Simulation-only evidence with synthetic prompt classes, synthetic prediction noise, and an explicit CPU proxy cost model; no real model-serving runtime, tokenizer, KV-cache behavior, continuous batching, or production trace replay was tested.

## Claim scope

In a reproducible static-batch CPU local-serving simulator, grouping ready requests by prompt-conditioned predicted decode length reduces p95/p99 latency versus FIFO when predicted output length is informative, and harms tail latency when predictions are uninformative.

## Why it stopped

Proxy/simulation evidence supports the mechanism but is not direct enough for a paper or production claim.

## Recommended next action

Stop this run as no-paper useful simulator evidence; next run should replay real CPU serving traces with measured service times before making any production-serving claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-driven CPU serving replay for prompt-conditioned decode-length bucketing
- Success threshold: Predicted-decode bucketing improves p95 latency by >=10% vs FIFO on calibrated trace replay, p99 does not regress, and long-request p95 regresses by <=5%.
- Stop condition: Stop if prediction calibration is weak or if predicted-decode bucketing fails the p95 threshold at two or more load levels.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-conditioned-cpu-batch-scheduling-for-local-serving-71c10c1264f0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
