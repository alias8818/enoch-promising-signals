# Asynchronous Federated Learning with Staleness-Aware Aggregation for Volunteer Networks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `asynchronous-federated-learning-with-staleness-aware-aggregation-for-volunteer-networks-de6ca0f28dee`
Run ID: `asynchronous-federated-learning-with-staleness-aware-aggregation-for-volunteer-networks-de6ca0f28dee-20260620T103422021914+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/35b446046754

## What looked useful

Staleness-aware attenuation was not an unconditional improvement: it hurt conservative fixed async FL, was marginal at moderate alpha, and helped clearly only as a high-alpha stability control. The best policy was gentle sqrt-inverse attenuation under server_alpha=1.5, improving final loss by 0.0270 and area loss by 0.0526 versus fixed across 12/12 paired seeds.

## Boundaries and scale limits

No real FL benchmark, real volunteer availability traces, deep model, privacy mechanism, network failure model, or large-scale deployment was tested. Results are local synthetic evidence only.

## Claim scope

Synthetic non-IID logistic-regression asynchronous FL with 50 clients, heavy-tailed volunteer-style delays, 1200 server update events per seed, and paired comparisons across 12 seeds and three server-alpha regimes.

## Why it stopped

Closed as no-paper useful synthetic signal: evidence is conditional and proxied, not direct publication-grade validation of volunteer-network asynchronous FL.

## Recommended next action

Run a bounded deepen test on a standard FL benchmark with trace-derived or benchmarked client availability and equal validation-budget tuning for fixed versus sqrt-inverse staleness-aware aggregation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Benchmark sqrt-inverse staleness control on real FL workload traces
- Success threshold: sqrt-inverse staleness-aware aggregation improves convergence-area loss or task error by at least 5% versus best tuned fixed FedAsync in the aggressive-delay/high-alpha regime without losing more than 1% in the conservative tuned regime.
- Stop condition: Stop if equal-budget tuning shows fixed FedAsync matches or beats staleness-aware aggregation on both final performance and convergence area across the benchmark workload.

## Evidence references

- Artifact root: `<local-path>/projects/asynchronous-federated-learning-with-staleness-aware-aggregation-for-volunteer-networks-de6ca0f2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
