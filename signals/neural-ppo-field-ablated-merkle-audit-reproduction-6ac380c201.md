# Neural PPO Field-Ablated Merkle Audit Reproduction

Status: `useful_signal`
Project ID: `neural-ppo-field-ablated-merkle-audit-reproduction-6ac380c201`
Run ID: `neural-ppo-field-ablated-merkle-audit-reproduction-6ac380c201-20260516T092702956621+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Neural PPO Field-Ablated Merkle Audit Reproduction: internal_generated:neural-ppo-field-ablated-merkle-audit-reproduction-6ac380c201

## What looked useful

PPO matched the symbolic verifier at 1.000 mean held-out accuracy over five seeds; removing random noise preserved 1.000 accuracy, while removing root_match or index_consistent collapsed accuracy to the class base rate near 0.498. Root-only retained 0.902 accuracy but failed bad-index cases, supporting the field-ablation mechanism diagnosis.

## Boundaries and scale limits

The PPO policy was not tested as an end-to-end verifier over raw cryptographic proof bytes, production traces, adversarial distributions, deeper-tree shifts, or large-scale workloads. The positive result depends on verifier-derived summary fields and is not a replacement for the exact symbolic verifier.

## Claim scope

In synthetic depth-5 SHA-256 Merkle audit records with engineered audit-summary features, a small PPO actor-critic reproduced the symbolic verifier's accept/reject decision across five fixed seeds, and semantic field ablations identified dependence on root-match and index-consistency fields.

## Why it stopped

The Tier 2 result supports a local mechanism but is not publication-grade because the neural policy consumes engineered verifier-summary fields rather than learning Merkle verification from raw proofs.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next bounded test should remove verifier-derived equality fields and compare PPO against supervised and symbolic baselines on raw or minimally processed proof observations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Raw-Observation PPO Merkle Audit With Supervised and Symbolic Baselines
- Success threshold: Mean held-out accuracy and F1 at least 0.98 across five seeds on in-depth tests and at least 0.95 on a held-out depth, while label-shuffle/random controls remain near chance and symbolic verifier remains exact.
- Stop condition: Stop negative if raw/minimal-observation PPO stays below 0.80 mean accuracy or fails to beat a simple supervised baseline after a calibrated medium run with the same data budget.

## Evidence references

- Artifact root: `<local-path>/projects/neural-ppo-field-ablated-merkle-audit-reproduction-6ac380c201`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
