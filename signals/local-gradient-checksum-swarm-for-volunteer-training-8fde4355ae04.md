# Local Gradient-Checksum Swarm for Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-gradient-checksum-swarm-for-volunteer-training-8fde4355ae04`
Run ID: `local-gradient-checksum-swarm-for-volunteer-training-8fde4355ae04-20260528T004926817116+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f4b8f1f31559

## What looked useful

Dense parity checks detected bad gradients but dropped many honest gradients; sparse checks reduced collateral drops and turned the 25% noisy adversary case from negative to slightly positive while strongly rescuing 25% sign-flip corruption.

## Boundaries and scale limits

No real volunteer network, no asynchronous execution, no malicious checksum workers, no collusion, no privacy constraints, no larger neural model, and no full distributed training stack were tested.

## Claim scope

In a synthetic synchronous logistic-regression proxy with 16 simulated workers, random additive parity checksum tasks can detect corrupted per-shard gradients and improve robustness for sign-flip and some noisy corruption cases, especially with sparse checksum membership.

## Why it stopped

No-paper useful signal from a synthetic proxy; evidence is mixed and not direct/full validation of volunteer training.

## Recommended next action

Run a bounded deepen follow-up using sparse group-testing parity codes on a small neural network with colluding adversaries and measured audit compute overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sparse group-testing gradient checksums for small neural volunteer training
- Success threshold: At 12.5% to 25% corrupted workers, sparse checksum training improves validation accuracy by at least 1 percentage point over naive averaging without dropping more than 25% of honest gradients per step and with audit compute overhead under 75%.
- Stop condition: Stop if sparse checks fail to improve validation accuracy in at least three of four adversary conditions or require dropping more than 25% of honest gradients per step.

## Evidence references

- Artifact root: `<local-path>/projects/local-gradient-checksum-swarm-for-volunteer-training-8fde4355ae04`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
