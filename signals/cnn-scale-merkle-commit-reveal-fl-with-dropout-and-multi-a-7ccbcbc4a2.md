# CNN-scale Merkle Commit-Reveal FL With Dropout and Multi-Attacker Ablations

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `cnn-scale-merkle-commit-reveal-fl-with-dropout-and-multi-a-7ccbcbc4a2`
Run ID: `cnn-scale-merkle-commit-reveal-fl-with-dropout-and-multi-a-7ccbcbc4a2-20260527T163625970166+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Medium Real-Data Merkle Commit-Reveal FL Confirmation: enoch://control-plane/projects/medium-real-data-merkle-commit-reveal-fl-confirmation-dcb7f6dba6/runs/medium-real-data-merkle-commit-reveal-fl-confirmation-dcb7f6dba6-20260527T100753321664+0000
- Parent run decision: Merkle Commit-Reveal on a Small Real Federated Training Task: enoch://control-plane/projects/merkle-commit-reveal-on-a-small-real-federated-training-ta-0336cbaa7e/runs/merkle-commit-reveal-on-a-small-real-federated-training-ta-0336cbaa7e-20260524T232543528623+0000

## What looked useful

Merkle roots over CNN update chunks detected 1,447/1,447 adaptive equivocation attempts with about 0.17 ms verification per update, but committed malicious updates reduced mean final accuracy by 30.5-32.3 percentage points with 4 attackers and about 94 percentage points with 8 attackers.

## Boundaries and scale limits

Synthetic 8x8 image classification with a 5,210-parameter CNN; no real CIFAR/ImageNet-scale data, no production FL networking, no secure aggregation, no robust aggregation, and CPU-only local validation.

## Claim scope

In a bounded NumPy CNN federated-learning simulator with 24 non-IID clients, benign dropout, 5 fixed seeds, 30 rounds, and 1/4/8 malicious clients, Merkle commit/reveal reliably rejected post-commit equivocation at low verification overhead, but did not prevent committed multi-attacker poisoning from degrading or collapsing training.

## Why it stopped

Bounded direct CNN FL validation found a mixed mechanism result: equivocation prevention works, but the main dropout and multi-attacker robustness claim fails against committed malicious updates.

## Recommended next action

Stop this branch as no-paper evidence; the bounded result supports Merkle commit/reveal only as an equivocation-prevention component, not as a standalone FL robustness defense.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Commit-Reveal Plus Robust Aggregation for Committed Multi-Attacker CNN FL
- Success threshold: For 4 attackers, final accuracy within 10 percentage points of honest and at least 20 percentage points better than commit/reveal only; for 8 attackers, final accuracy at least 50 percentage points better than commit/reveal only while retaining 100% equivocation detection.
- Stop condition: Stop if robust aggregation plus commit/reveal still loses more than 30 percentage points vs honest for 4 attackers or fails to beat commit/reveal only by at least 10 percentage points for 8 attackers.

## Evidence references

- Artifact root: `<local-path>/projects/cnn-scale-merkle-commit-reveal-fl-with-dropout-and-multi-a-7ccbcbc4a2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
