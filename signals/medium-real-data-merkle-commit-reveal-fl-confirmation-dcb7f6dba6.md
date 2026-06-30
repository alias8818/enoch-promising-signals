# Medium Real-Data Merkle Commit-Reveal FL Confirmation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `medium-real-data-merkle-commit-reveal-fl-confirmation-dcb7f6dba6`
Run ID: `medium-real-data-merkle-commit-reveal-fl-confirmation-dcb7f6dba6-20260527T100753321664+0000`

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

- Parent run decision: Merkle Commit-Reveal on a Small Real Federated Training Task: enoch://control-plane/projects/merkle-commit-reveal-on-a-small-real-federated-training-ta-0336cbaa7e/runs/merkle-commit-reveal-on-a-small-real-federated-training-ta-0336cbaa7e-20260524T232543528623+0000
- Parent run decision: Merkle Commit-Reveal for Volunteer Training: enoch://control-plane/projects/merkle-commit-reveal-for-volunteer-training-c7f211d63626/runs/merkle-commit-reveal-for-volunteer-training-c7f211d63626-20260524T215634139562+0000

## What looked useful

Across three fixed seeds, FedAvg and honest Merkle both reached 0.8693 mean final accuracy with zero delta; verified tamper reached 0.8436 accuracy with 100% tamper detection and one rejected client per round; no-verification tamper fell to 0.2369 accuracy. Honest Merkle aggregation overhead averaged 3.61 ms/round versus 0.49 ms/round for FedAvg.

## Boundaries and scale limits

Evidence is limited to MNIST, a 7,850-parameter softmax model, 10 synchronous clients, one tampered client per round, local CPU simulation, and no production networking, secure aggregation, privacy, dropout, collusion, key management, or large-model/client-scale stress.

## Claim scope

On a local real-MNIST federated softmax-regression simulation with 10 non-IID clients, 15 rounds, and fixed seeds 11/22/33, Merkle commit-reveal verification exactly preserves honest FedAvg accuracy/loss, detects post-commit tampered reveals in every tested round, rejects the tampered client update, and prevents the large accuracy collapse seen in the no-verification ablation.

## Why it stopped

Tier 2 mechanism evidence is positive, but publication readiness is not met because validation is limited to local MNIST softmax simulation and a narrow adversary pattern.

## Recommended next action

Stop this run as no-paper useful signal; a bounded next test should evaluate the same commit-reveal mechanism on a CNN-scale real-data FL task with dropout and multi-attacker ablations before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CNN-scale Merkle Commit-Reveal FL With Dropout and Multi-Attacker Ablations
- Success threshold: Across at least three fixed seeds, honest Merkle final accuracy is within 1 percentage point of FedAvg with zero false rejects; tampered reveal detection is 100%; verified tamper accuracy is at least 20 percentage points above the no-verification tamper ablation; overhead is below 5% of total round time.
- Stop condition: Stop if honest Merkle diverges from FedAvg by more than 1 percentage point without tampering, false rejects occur under honest clients, tamper detection falls below 100%, or overhead exceeds 5% of round time after straightforward implementation optimization.

## Evidence references

- Artifact root: `<local-path>/projects/medium-real-data-merkle-commit-reveal-fl-confirmation-dcb7f6dba6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
