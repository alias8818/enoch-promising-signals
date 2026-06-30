# Multi-process gossip averaging on a small neural non-IID benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `multi-process-gossip-averaging-on-a-small-neural-non-iid-b-b540399fd7`
Run ID: `multi-process-gossip-averaging-on-a-small-neural-non-iid-b-b540399fd7-20260524T154159548660+0000`

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

- Parent run decision: Gossip-Averaging Toy Distributed Training on Single CPU: enoch://control-plane/projects/gossip-averaging-toy-distributed-training-on-single-cpu-57285a6bac42/runs/gossip-averaging-toy-distributed-training-on-single-cpu-57285a6bac42-20260524T083217083885+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/57c7e86ee078

## What looked useful

Ring gossip averaging can preserve FedAvg-like accuracy in this controlled non-IID toy setting, but the tested benchmark was too easy for independent local models and failed the predeclared +10 percentage point utility threshold.

## Boundaries and scale limits

Single CPU host, simulated orchestration rather than networked peer-to-peer transport, tiny one-hidden-layer MLP, generated Gaussian data, 8 clients, 35 rounds, 8 seeds; not evidence for public datasets, larger neural models, real distributed systems, or publication-grade robustness.

## Claim scope

On a generated small neural non-IID Gaussian classification benchmark with 8 local client processes, decentralized ring gossip averaging matched synchronous FedAvg within 0.2 percentage points over 8 seeds, but improved over independent local training by only about 4.0 percentage points.

## Why it stopped

Direct Tier 1 evidence was mixed: gossip passed the within-5pp-of-FedAvg mechanism threshold but failed the predeclared +10pp-over-local practical utility threshold over both 3-seed and 8-seed runs.

## Recommended next action

Stop this run as no-paper useful signal; if pursued, run a bounded harder direct benchmark with label-exclusive or public small-dataset client shards where local training is demonstrably disadvantaged before considering scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Harder non-IID label-shard test for multi-process gossip averaging
- Success threshold: Across at least 5 seeds, gossip mean global accuracy is within 5 percentage points of FedAvg and at least 10 percentage points higher than independent local training on the same harder non-IID benchmark.
- Stop condition: Stop if local-only accuracy remains within 10 percentage points of gossip after the harder split, or if gossip falls more than 5 percentage points behind FedAvg.

## Evidence references

- Artifact root: `<local-path>/projects/multi-process-gossip-averaging-on-a-small-neural-non-iid-b-b540399fd7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
