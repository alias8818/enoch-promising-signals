# Gossip-Averaging Toy Distributed Training on Single CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gossip-averaging-toy-distributed-training-on-single-cpu-57285a6bac42`
Run ID: `gossip-averaging-toy-distributed-training-on-single-cpu-57285a6bac42-20260524T083217083885+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/57c7e86ee078

## What looked useful

Random-pair gossip at lr 0.003 and heterogeneity 2.0 improved mean validation MSE over local-only training (0.422974 vs 0.589382) but lagged all-reduce (0.400707). At lr 0.03 under the same heterogeneity, distributed local/gossip/allreduce variants diverged while centralized stayed finite, showing gossip is not a drop-in stability fix.

## Boundaries and scale limits

Synthetic convex linear regression only; no real network, asynchronous workers, optimizer-state exchange, GPU training, large neural model, or multi-node throughput evidence.

## Claim scope

Single-process CPU simulation of 8-worker non-IID linear regression: periodic gossip averaging can reduce worker disagreement and, in a stable high-heterogeneity setting, improve validation MSE versus local-only training, but it remains below full all-reduce and is sensitive to learning-rate/heterogeneity.

## Why it stopped

The result is a synthetic single-process proxy with a useful mechanism signal and an early stability caveat, not direct/full validation of distributed training.

## Recommended next action

Stop this run as no-paper toy evidence; run a bounded multi-process neural follow-up only if the next controller budget supports direct systems and non-convex training measurements.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-process gossip averaging on a small neural non-IID benchmark
- Success threshold: Random-pair gossip achieves at least 80% of all-reduce's validation metric gain over local-only, does not diverge across at least 5 seeds, and reports communication/runtime overhead clearly.
- Stop condition: Stop if gossip fails to beat local-only in validation metric at any stable calibrated setting, or if it requires communication as frequent/costly as all-reduce to remain stable.

## Evidence references

- Artifact root: `<local-path>/projects/gossip-averaging-toy-distributed-training-on-single-cpu-57285a6bac42`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
