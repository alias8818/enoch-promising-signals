# Volunteer Distributed Training with Compressed State Sync

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `volunteer-distributed-training-with-compressed-state-sync-5954d60741b3`
Run ID: `volunteer-distributed-training-with-compressed-state-sync-5954d60741b3-20260607T151355496884+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7a69b6f68e37

## What looked useful

At 5% top-k q8 with error feedback, compressed sync used 6.28% of full-sync bytes and had only -0.0010 absolute accuracy delta but +0.0394 loss delta versus full sync. At 10% top-k q8 with error feedback, loss and accuracy were close to full sync (+0.0180 loss, -0.0011 accuracy) but sparse index overhead raised byte ratio to 12.54%.

## Boundaries and scale limits

Synthetic single-process CPU simulation only; no real volunteer network, straggler/churn trace, multi-process transport, optimizer-state sync, neural model, or language-model workload was tested.

## Claim scope

In a 5-seed NumPy synthetic non-IID logistic FedAvg proxy with intermittent client participation, top-k q8 error-feedback compressed model-delta sync preserved accuracy closely at large byte reductions, but no variant met the strict combined threshold of <=10% full-sync bytes, absolute loss difference <=0.02, and accuracy drop <=0.02.

## Why it stopped

The result is a proxy-only mixed signal: compressed sync preserved accuracy but missed the strict <=10% byte plus loss-preservation threshold, so it is not a publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up with a small neural model and packed/block-sparse index coding before considering larger volunteer-scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Block-coded compressed sync on a small neural distributed-training proxy
- Success threshold: A compressed variant achieves <=0.10 byte ratio versus dense sync, absolute loss difference <=0.02, accuracy drop <=0.02, and no unstable residual growth across at least 5 seeds.
- Stop condition: Stop as negative if no compressed variant meets the byte/loss/accuracy threshold or if residual/model norms show persistent divergence relative to dense sync.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-distributed-training-with-compressed-state-sync-5954d60741b3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
