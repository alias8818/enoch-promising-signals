# Byzantine-Robust Aggregation Toy Test on CPU Volunteer Pool

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `byzantine-robust-aggregation-toy-test-on-cpu-volunteer-pool-a1cb745d115a`
Run ID: `byzantine-robust-aggregation-toy-test-on-cpu-volunteer-pool-a1cb745d115a-20260628T231224656638+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4b5657fb2df5

## What looked useful

Robust aggregation is worth carrying into a direct federated/distributed training harness: full-run mean relative error was 2.079 for plain mean versus 0.109 coordinate median, 0.122 trimmed mean, 0.091 geometric median, and 0.181 Krum; at 30-40 percent Byzantine workers plain mean had 0.000 relative-error success while robust methods were approximately 0.999-1.000.

## Boundaries and scale limits

Synthetic gradients only; no real volunteer network, real model training, real datasets, secure identity, straggler/dropout behavior, colluding adaptive attackers, or unknown Byzantine-count estimation. Trimmed mean and Krum received the true Byzantine count.

## Claim scope

In a bounded synthetic 31-volunteer, 80-dimensional CPU gradient aggregation simulation, coordinate median, trimmed mean, geometric median, and Krum preserved useful gradient estimates under up to 40 percent Byzantine sign-flip, Gaussian, and targeted attacks, while plain averaging failed at high Byzantine fractions.

## Why it stopped

Proxy-only synthetic toy validation supports the mechanism but is not full validation of a real CPU volunteer pool or distributed training system.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is a direct small federated-training harness with real model gradients, unknown Byzantine-count estimation, and repeated seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Federated Training Check for Byzantine-Robust Aggregation
- Success threshold: At 20-30 percent Byzantine clients, at least one robust aggregator must improve final loss or accuracy by at least 20 percent relative to plain mean in four of five seeds without using the true Byzantine count.
- Stop condition: Stop if robust aggregators fail to beat plain mean in at least three of five seeds at 20 percent Byzantine clients, or if the direct training harness exceeds the local CPU budget without checkpointable metrics.

## Evidence references

- Artifact root: `<local-path>/projects/byzantine-robust-aggregation-toy-test-on-cpu-volunteer-pool-a1cb745d115a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
