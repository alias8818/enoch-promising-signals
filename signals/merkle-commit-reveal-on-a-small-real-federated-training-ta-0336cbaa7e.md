# Merkle Commit-Reveal on a Small Real Federated Training Task

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `merkle-commit-reveal-on-a-small-real-federated-training-ta-0336cbaa7e`
Run ID: `merkle-commit-reveal-on-a-small-real-federated-training-ta-0336cbaa7e-20260524T232543528623+0000`

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

- Parent run decision: Merkle Commit-Reveal for Volunteer Training: enoch://control-plane/projects/merkle-commit-reveal-for-volunteer-training-c7f211d63626/runs/merkle-commit-reveal-for-volunteer-training-c7f211d63626-20260524T215634139562+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e971ea2dbc86

## What looked useful

The mechanism is technically viable in a direct small real FL loop: mean final accuracy matched plain FedAvg at 0.9911111111111112, wall-clock overhead was 0.03255094144825623, and tamper detection rate was 1.0 across client tamper trials.

## Boundaries and scale limits

Only 133 train and 45 test samples, 6 clients, small dense update vectors, synchronous full participation, no secure transport, no client dropout, no collusion, and no proof that committed updates were honestly computed from local data.

## Claim scope

On a small real UCI Wine federated classification task with 6 moderately non-IID clients, 30 FedAvg rounds, and multinomial logistic regression, a Merkle commit-reveal wrapper over quantized client updates preserved final accuracy, added 3.26% wall-clock overhead, and detected all tested post-commit update tampering.

## Why it stopped

Tier 1 direct mechanism support was achieved, but the run is too small and narrow for publication readiness.

## Recommended next action

Run a medium bounded confirmation on a larger real FL benchmark with larger model updates and explicit whole-update hash/signature baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Real-Data Merkle Commit-Reveal FL Confirmation
- Success threshold: Accuracy within 0.01 absolute of plain FedAvg, 100% post-commit tamper detection, no false positives on honest reveals, and Merkle overhead no more than 15% above plain FedAvg or justified by partial-audit functionality versus whole-update hash baselines.
- Stop condition: Stop as negative if accuracy drops by more than 0.01, any honest reveal fails verification, any tampered reveal is accepted, or Merkle overhead exceeds 25% without demonstrating partial-audit value over simpler hash commitments.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-commit-reveal-on-a-small-real-federated-training-ta-0336cbaa7e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
