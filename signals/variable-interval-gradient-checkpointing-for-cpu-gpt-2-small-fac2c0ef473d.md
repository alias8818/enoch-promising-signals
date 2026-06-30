# Variable-interval gradient checkpointing for CPU GPT-2-small

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `variable-interval-gradient-checkpointing-for-cpu-gpt-2-small-fac2c0ef473d`
Run ID: `variable-interval-gradient-checkpointing-for-cpu-gpt-2-small-fac2c0ef473d-20260628T140332074680+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3118b0c19190

## What looked useful

For equal GPT-2-small block activation costs, the best variable-interval schedule exactly matches the best uniform schedule: 63.000 MiB proxy peak versus 63.000 MiB, 0.000% improvement. Mild 10% heterogeneity also showed 0.000% improvement; a synthetic 2x heterogeneity proxy produced only 0.940% global improvement.

## Boundaries and scale limits

No real PyTorch GPT-2-small backward pass or allocator/RSS trace was run because the host Python 3.14 environment had no installed PyTorch wheel. Evidence is schedule-level, not full training throughput evidence.

## Claim scope

Schedule-level exhaustive search for block-boundary checkpoint intervals on a GPT-2-small-shaped 12-block CPU training proxy.

## Why it stopped

Proxy schedule evidence does not support variable-interval checkpointing as a meaningful improvement for GPT-2-small block-boundary CPU checkpointing; this is not a full validation.

## Recommended next action

Stop this run as an early proxy falsification; only retry if a supported PyTorch CPU environment is available for direct RSS/backward measurements against the best uniform checkpoint cadence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct PyTorch CPU RSS test for GPT-2-small checkpoint schedules
- Success threshold: Confirm variable intervals improve peak RSS by less than 2% versus best uniform at equal or worse step time, or overturn the proxy by showing at least 5% lower peak RSS at no more than 5% additional wall-clock cost.
- Stop condition: Stop after one reproducible GPT-2-small CPU batch/sequence configuration with three repeated steps per schedule if variable intervals remain within 2% of best uniform RSS.

## Evidence references

- Artifact root: `<local-path>/projects/variable-interval-gradient-checkpointing-for-cpu-gpt-2-small-fac2c0ef473d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
