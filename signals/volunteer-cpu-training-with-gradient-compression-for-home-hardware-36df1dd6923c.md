# Volunteer CPU Training with Gradient Compression for Home Hardware

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `volunteer-cpu-training-with-gradient-compression-for-home-hardware-36df1dd6923c`
Run ID: `volunteer-cpu-training-with-gradient-compression-for-home-hardware-36df1dd6923c-20260609T153632797187+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/11df40c64e18

## What looked useful

Across 3 seeds, top-k 1% with error feedback reduced payload by 98.0% with mean final accuracy 0.5806 versus dense 0.5861, and top-k 5% reduced payload by 90.0% with mean final accuracy 0.5874. At a modeled 20 Mbps uplink, top-k 1% reduced estimated end-to-end time from 142.42s dense to 6.73s. Random-k 1% matched the payload reduction but lost 9.46 accuracy points, showing the compression choice matters.

## Boundaries and scale limits

Synthetic data only; workers simulated in one Python process; network time estimated from payload bytes at fixed Mbps; no real volunteer hosts, WAN latency, churn, stragglers, privacy constraints, public dataset, or large model.

## Claim scope

Local CPU synthetic 8-worker synchronous training proxy with a 136,714-parameter MLP: top-k gradient sparsification with error feedback and 8-bit quantization reduced measured payload while preserving final accuracy near dense training.

## Why it stopped

No-paper useful signal only: this run directly tested CPU compression/training but proxied networking and did not validate a real volunteer deployment.

## Recommended next action

Run a bounded direct multi-host follow-up on two or more real home/VM nodes with measured latency, bandwidth, straggler behavior, and a public dataset before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real multi-host volunteer CPU gradient-compression benchmark
- Success threshold: Top-k with error feedback reaches final validation accuracy within 1 percentage point of dense and reduces measured communication wall time by at least 5x at the constrained uplink setting.
- Stop condition: Stop if top-k loses more than 3 accuracy points versus dense in two seeds or if measured CPU compression overhead eliminates at least 80% of the communication-time savings.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-cpu-training-with-gradient-compression-for-home-hardware-36df1dd6923c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
