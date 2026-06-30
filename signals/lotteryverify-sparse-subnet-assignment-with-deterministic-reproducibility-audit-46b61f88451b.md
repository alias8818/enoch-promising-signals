# LotteryVerify: Sparse Subnet Assignment with Deterministic Reproducibility Audit

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `lotteryverify-sparse-subnet-assignment-with-deterministic-reproducibility-audit-46b61f88451b`
Run ID: `lotteryverify-sparse-subnet-assignment-with-deterministic-reproducibility-audit-46b61f88451b-20260610T020724973684+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b7d69054757c

## What looked useful

LotteryVerify produced exact 21708-position masks for all 12 tested subnets, matched all assignment and audit digests across an independent repeat process, had no order-invariance failures, and had mean pairwise Jaccard 0.0256257442 versus expected 0.0256410256. Seeded RNG baselines failed traversal-order invariance, and Bernoulli RNG also missed the exact density target.

## Boundaries and scale limits

No real model training, pruning recovery, cross-language implementation, GPU tensor-order audit, or large-model deployment was tested. Results are limited to mask assignment and audit reproducibility, not sparse-subnet training quality.

## Claim scope

A local standard-library prototype showed that canonical BLAKE2b score based, layerwise exact sparse subnet assignment is deterministic, traversal-order independent, density-exact, and digest-auditable on a synthetic transformer-shaped manifest of 434176 parameter positions, 12 subnets, and 5% density.

## Why it stopped

Bounded local audit succeeded, but evidence is limited to deterministic mask assignment on a synthetic manifest and is not full validation of training behavior or model-scale reproducibility.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded action is to integrate the deterministic masks into a small real training workload and audit mask, checkpoint, and metric reproducibility across repeated runs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LotteryVerify Small Training Reproducibility Audit
- Success threshold: All deterministic-mask repeats match mask digests and selected coordinates exactly, checkpoint hashes match when deterministic kernels permit it, final metrics vary less than 0.1% across repeats, and RNG traversal baselines show at least one reproducibility failure.
- Stop condition: Stop if deterministic masks fail exact digest reproducibility under fixed canonical tensor naming, or if the only remaining failures are unrelated nondeterministic training kernels rather than sparse assignment.

## Evidence references

- Artifact root: `<local-path>/projects/lotteryverify-sparse-subnet-assignment-with-deterministic-reproducibility-audit-46b61f88451b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
