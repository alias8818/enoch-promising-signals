# Gradient hash commitment with spot-check recomputation for volunteer training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-hash-commitment-with-spot-check-recomputation-for-volunteer-training-aaac2bfba11f`
Run ID: `gradient-hash-commitment-with-spot-check-recomputation-for-volunteer-training-aaac2bfba11f-20260619T153033598477+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8d7f05af6eeb

## What looked useful

The mechanism behaves like straightforward random sampling: broad cheating is caught reliably at moderate spot rates, sparse cheating is often missed, and exact float hashing is brittle to tiny numeric drift despite near-identical gradient direction.

## Boundaries and scale limits

Tested only on a synthetic MLP with 128 batches and local CPU recomputation; no distributed volunteers, no real network, no cross-hardware reproducibility, no large model, and no production adversary model were validated.

## Claim scope

In a deterministic CPU PyTorch toy volunteer/verifier setup, per-batch gradient hash commitments plus random spot-check recomputation detect checked corrupted gradients and have low hash overhead, but detection probability is limited by sampling rate and corruption sparsity.

## Why it stopped

Bounded local probe supports the sampling mechanism but also exposes sparse-cheating and exact-hash brittleness limits; this is proxy/local evidence, not full volunteer-training validation.

## Recommended next action

Stop this run as no-paper useful signal; next, test cross-hardware deterministic recomputation and tolerant/canonical gradient commitments against explicit false-accept and false-reject thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cross-hardware tolerant gradient commitment validation
- Success threshold: A bounded follow-up succeeds if benign cross-hardware false rejection is below 1%, tampering that changes update cosine similarity below 0.999 is detected above 95% when 10% of batches are corrupted and 20% are checked, and verifier overhead remains under 25% of full recomputation.
- Stop condition: Stop if exact or tolerant commitments cannot distinguish benign numeric drift from adversarial perturbation at the stated thresholds, or if required verifier overhead approaches full redundant training.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-hash-commitment-with-spot-check-recomputation-for-volunteer-training-aaac2bfba11f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
