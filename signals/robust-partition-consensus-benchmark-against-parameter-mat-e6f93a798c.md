# Robust Partition-Consensus Benchmark Against Parameter-Matched Baselines

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `robust-partition-consensus-benchmark-against-parameter-mat-e6f93a798c`
Run ID: `robust-partition-consensus-benchmark-against-parameter-mat-e6f93a798c-20260602T185343612748+0000`

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

- Parent run decision: Cross-Worker Hidden State Consensus: enoch://control-plane/projects/cross-worker-hidden-state-consensus-f89c619fb723/runs/cross-worker-hidden-state-consensus-f89c619fb723-20260601T062751759535+0000
- Parent run decision: Partitioned Real-Sequence Hidden-State Consensus Benchmark: enoch://control-plane/projects/partitioned-real-sequence-hidden-state-consensus-benchmark-c2dc93af8d/runs/partitioned-real-sequence-hidden-state-consensus-benchmark-c2dc93af8d-20260602T105415314065+0000

## What looked useful

Partition mean consensus reached 0.8743 corrupt-average accuracy versus 0.7522 for a 1.39% larger dense MLP, a paired +0.1221 mean delta across five seeds. The median robust aggregator did not meet the stricter success threshold and underperformed mean consensus.

## Boundaries and scale limits

Synthetic data only; 5 fixed seeds; small 5.7k-parameter classifiers; no real datasets, learned representation partitions, large models, or non-synthetic corruption sources were tested.

## Claim scope

On a synthetic 8-partition multi-class classification benchmark with localized feature-partition corruptions, mean partition consensus improved corrupt-average accuracy over a parameter-matched dense MLP while preserving clean accuracy.

## Why it stopped

Tier 2 synthetic evidence supports a bounded mean-consensus mechanism but not publication readiness; the stricter robust-median threshold failed and real-data validation remains absent.

## Recommended next action

Stop this run as no-paper useful signal; next, test mean partition consensus on real grouped-feature or representation-partition datasets with a parameter-matched dense baseline and a non-partition ensemble control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Data Partition Mean-Consensus Robustness Check
- Success threshold: Mean partition consensus improves corrupt-average accuracy by at least 5 percentage points over both dense and non-partition ensemble controls across datasets without losing more than 3 percentage points clean accuracy.
- Stop condition: Stop if the mean corrupt-average gain is below 2 percentage points on both real datasets or if clean accuracy drops by more than 5 percentage points versus the dense baseline.

## Evidence references

- Artifact root: `<local-path>/projects/robust-partition-consensus-benchmark-against-parameter-mat-e6f93a798c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
