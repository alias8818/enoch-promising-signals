# Queue admission policy under near-capacity gb10 lane

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `queue-admission-policy-under-near-capacity-gb10-lane-527f13858bd1`
Run ID: `queue-admission-policy-under-near-capacity-gb10-lane-527f13858bd1-20260613T105911856467+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/10a2893af618

## What looked useful

Measured GB10 service samples fed a near-capacity replay. At rho 0.95, p90 deadline admission raised deadline goodput from 539.79/s for admit-all to 1165.89/s, cut p95 wait from 25.84 ms to 4.09 ms, and reduced wasted GPU service from 50.3% to about 0.004%. At rho 1.05, admit-all collapsed to 10.70 deadline completions/s while the guard sustained 1170.07/s by rejecting about 29.1% of arrivals.

## Boundaries and scale limits

Not a live serving test; workloads were synthetic GEMMs, arrivals were Poisson, deadlines were synthetic, and admission used class-level service estimates with exact simulated backlog. No multi-client CUDA dispatch, real model inference, burst traces, or estimator-overhead study was performed.

## Claim scope

For a single GB10 lane replay driven by measured fp16 GEMM service times and synthetic Poisson arrivals, a p90 deadline-aware admission guard improved deadline-satisfied goodput and reduced wasted late-completion GPU time versus admit-all and a simple queue-depth cap under rho 0.85, 0.95, and 1.05.

## Why it stopped

Closed as no-paper useful signal because the queueing layer was replayed from measured GB10 service samples rather than validated as a live serving system.

## Recommended next action

Run a live single-GB10 concurrent request harness with online service-time estimates and real CUDA dispatch to verify the replay mechanism under actual queueing overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live GB10 deadline-aware admission under concurrent CUDA request dispatch
- Success threshold: At rho 0.95, deadline-aware admission improves deadline-satisfied goodput by at least 1.5x over admit-all and at least 1.2x over queue-cap while keeping late admitted GPU time below 5%.
- Stop condition: Stop if live dispatch overhead or estimator error reduces the deadline-goodput advantage below 1.2x over queue-cap in two independent runs.

## Evidence references

- Artifact root: `<local-path>/projects/queue-admission-policy-under-near-capacity-gb10-lane-527f13858bd1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
