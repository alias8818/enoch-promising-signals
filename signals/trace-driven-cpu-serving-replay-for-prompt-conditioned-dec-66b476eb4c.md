# Trace-driven CPU serving replay for prompt-conditioned decode-length bucketing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `trace-driven-cpu-serving-replay-for-prompt-conditioned-dec-66b476eb4c`
Run ID: `trace-driven-cpu-serving-replay-for-prompt-conditioned-dec-66b476eb4c-20260604T230631110401+0000`

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

- Parent run decision: Prompt-conditioned CPU batch scheduling for local serving: enoch://control-plane/projects/prompt-conditioned-cpu-batch-scheduling-for-local-serving-71c10c1264f0/runs/prompt-conditioned-cpu-batch-scheduling-for-local-serving-71c10c1264f0-20260604T170321134696+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7e3d08743ebf

## What looked useful

Moderate-load Tier 1 replay missed the threshold: prompt_bucket improved p95 latency by 4.15% and waste by 0.35% versus FIFO, close to random_bucket. Heavy-load sensitivity supported the mechanism: with noisy prompt labels, prompt_bucket improved p95 latency by 85.84%, waste by 21.95%, and throughput by 34.18% versus FIFO, while random_bucket did not reproduce the effect.

## Boundaries and scale limits

Stdlib replay only; no real transformer kernels, no production traces, no multi-tenant admission control, and only five deterministic seeds per condition.

## Claim scope

In a deterministic trace-driven CPU decode replay, prompt-conditioned decode-length bucketing did not meet a 10% improvement threshold at moderate load, but it produced large latency, waste, and throughput gains under overload where FIFO accumulated backlog.

## Why it stopped

The Tier 1 controlled moderate-load replay did not satisfy the stated 10% success threshold; overload sensitivity is a useful mechanism signal but not full validation or paper-positive evidence.

## Recommended next action

Run a bounded direct CPU-kernel utilization sweep using a real small decoder model or captured serving trace to find the break-even load where prompt-conditioned length bucketing becomes beneficial.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU-kernel utilization sweep for prompt-conditioned decode bucketing
- Success threshold: At one or more near-saturation/overload points, prompt_bucket improves p95 latency or completed throughput by at least 10% versus FIFO, regresses the other metric by no more than 5%, and beats random_bucket by at least 5 percentage points on the same primary metric.
- Stop condition: Stop if real-kernel replay shows less than 10% prompt_bucket improvement versus FIFO at all utilization points or if random_bucket matches the prompt_bucket gain within 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/trace-driven-cpu-serving-replay-for-prompt-conditioned-dec-66b476eb4c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
