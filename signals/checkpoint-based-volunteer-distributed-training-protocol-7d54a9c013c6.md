# Checkpoint-Based Volunteer Distributed Training Protocol

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `checkpoint-based-volunteer-distributed-training-protocol-7d54a9c013c6`
Run ID: `checkpoint-based-volunteer-distributed-training-protocol-7d54a9c013c6-20260607T120318511301+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/240bf78d3f82

## What looked useful

Validation gating was the main useful mechanism: it accepted zero validation-worsening deltas and improved noisy-volunteer accuracy by 0.116 versus ungated checkpointing. The cost was high rejection: gated acceptance averaged 34.5% benign, 26.1% churn/non-IID, 24.0% noisy-volunteer, and 19.8% tight-staleness, with worse loss than centralized SGD in every scenario.

## Boundaries and scale limits

Synthetic binary classification only; no real volunteer network, large model, optimizer-state checkpointing, secure aggregation, bandwidth contention, process-level workers, or FedAvg/asynchronous-SGD implementation on actual distributed hardware. Sweep used 12 seeds, 4 scenarios, 360 attempted volunteer updates per checkpoint protocol per seed.

## Claim scope

In a deterministic synthetic logistic-regression simulator with asynchronous checkpoint/delta volunteer updates, staleness rejection, non-IID shards, churn-shaped service times, and noisy volunteers, validation-gated checkpointing prevents harmful accepted deltas and preserves accuracy under noisy volunteers, but does not outperform centralized SGD and loses efficiency through high rejection rates.

## Why it stopped

Proxy simulator produced mixed evidence: robustness under noisy volunteers but insufficient efficiency and no centralized-SGD win; this is not a full validation of volunteer distributed training.

## Recommended next action

Stop this run as a no-paper useful signal; next run should implement a bounded process-level worker test with real checkpoint files, optimizer state, FedAvg/asynchronous-SGD baselines, and network-shaped delays on a small neural model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Process-Level Checkpoint Volunteer Training on a Small Neural Model
- Success threshold: Gated checkpoint protocol matches the best baseline within 0.02 test accuracy in clean scenarios, improves noisy-volunteer accuracy by at least 0.05 over ungated checkpointing, and keeps harmful accepted deltas below 5% of accepted updates.
- Stop condition: Stop if clean-scenario accuracy trails the best baseline by more than 0.05 after matched compute/bandwidth or if accepted-update fraction remains below 20% without a compensating noisy-volunteer robustness gain.

## Evidence references

- Artifact root: `<local-path>/projects/checkpoint-based-volunteer-distributed-training-protocol-7d54a9c013c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
