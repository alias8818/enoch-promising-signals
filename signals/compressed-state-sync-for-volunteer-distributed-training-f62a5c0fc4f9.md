# Compressed state sync for volunteer distributed training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-state-sync-for-volunteer-distributed-training-f62a5c0fc4f9`
Run ID: `compressed-state-sync-for-volunteer-distributed-training-f62a5c0fc4f9-20260607T141740129022+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/bf55314bb4ea

## What looked useful

Dense int8 cached-state delta sync is a viable next candidate for volunteer distributed training experiments; sparse top-k state sync needs calibration/loss safeguards before scale-up.

## Boundaries and scale limits

Synthetic data, small convex softmax model, single-machine simulation, no real WAN, no secure transport overhead, no optimizer-state sync, no large neural model, no adversarial or privacy-sensitive volunteer behavior.

## Claim scope

In a local NumPy simulation of intermittent non-IID volunteer workers with cached model state, dense int8 bidirectional model-delta synchronization reduced measured downlink plus uplink bytes by 4.75x versus zlib-compressed fp32 deltas without hurting final softmax-classifier accuracy over three seeds. Aggressive sparse top-k sync achieved larger byte reductions but had worse loss/calibration and one failure at 1% density.

## Why it stopped

Local proxy produced a useful mechanism signal but not direct publication-grade validation of volunteer distributed training at scale.

## Recommended next action

Run a bounded multi-process network-shaped emulator with optimizer-state deltas and a small neural model to test whether the dense-int8 byte reduction survives protocol overhead and harder convergence dynamics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Network-shaped optimizer-state delta sync emulator
- Success threshold: At least 3x total byte reduction versus full-state sync, final validation accuracy within 1 percentage point, no material wall-clock regression under the same shaped network budget.
- Stop condition: Stop if dense int8 loses more than 1 percentage point of validation accuracy in two independent seeds or if protocol overhead reduces total byte savings below 2x.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-state-sync-for-volunteer-distributed-training-f62a5c0fc4f9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
