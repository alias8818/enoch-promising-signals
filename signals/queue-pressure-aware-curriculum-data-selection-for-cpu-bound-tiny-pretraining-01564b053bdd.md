# Queue-pressure-aware curriculum data selection for CPU-bound tiny pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `queue-pressure-aware-curriculum-data-selection-for-cpu-bound-tiny-pretraining-01564b053bdd`
Run ID: `queue-pressure-aware-curriculum-data-selection-for-cpu-bound-tiny-pretraining-01564b053bdd-20260609T204736771643+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/a4f8d59705a3

## What looked useful

Queue pressure alone was an unsafe curriculum signal: it kept the trainer fed by over-selecting cheap/core samples and nearly eliminating rare/high-value samples, losing to uniform validation loss in all tested loader-capacity regimes.

## Boundaries and scale limits

Synthetic data, simulated queue timing, bigram model, 3-5 seeds per regime, and simulated budgets of 120-180 seconds. This is not transformer-scale or real-corpus evidence.

## Claim scope

In a bounded synthetic tiny-pretraining proxy with a NumPy bigram language model, heterogeneous preprocessing costs, and a simulated producer/consumer loader queue, the tested pressure-only threshold curriculum improved throughput but produced substantially worse validation loss than uniform sampling.

## Why it stopped

Proxy early falsification: the tested queue-pressure policy improved throughput but failed the target metric, with final eval loss 3.1394 vs uniform 1.8070 at 25 loader units/s and similar gaps at 45 and 70 units/s.

## Recommended next action

Stop this pressure-only policy as no-paper early negative evidence; the next bounded test should add an explicit utility or coverage constraint to the pressure controller.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Utility-constrained queue-pressure curriculum for CPU-bound tiny pretraining
- Success threshold: Mean final eval loss within 5% of uniform while improving tokens/s by at least 50% and maintaining nonzero rare-data coverage across all loader-capacity regimes.
- Stop condition: Stop if the constrained policy still exceeds uniform final eval loss by more than 15% in two or more loader-capacity regimes, or if throughput gain falls below 20%.

## Evidence references

- Artifact root: `<local-path>/projects/queue-pressure-aware-curriculum-data-selection-for-cpu-bound-tiny-pretraining-01564b053bdd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
