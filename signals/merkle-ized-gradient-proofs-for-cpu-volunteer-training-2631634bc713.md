# Merkle-ized Gradient Proofs for CPU Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `merkle-ized-gradient-proofs-for-cpu-volunteer-training-2631634bc713`
Run ID: `merkle-ized-gradient-proofs-for-cpu-volunteer-training-2631634bc713-20260529T052413291678+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e8a03bd370e8

## What looked useful

Verifier spot checks were millisecond-scale and detected 10% corrupted leaves with about 0.79-0.84 probability for 16 checks, matching theory. However, a worker that commits honest leaves and submits an unrelated aggregate update passes all Merkle inclusion checks, so Merkle proofs alone are insufficient for CPU volunteer training correctness.

## Boundaries and scale limits

No real volunteer network, neural model, real dataset, multi-round training, incentive mechanism, or production cryptographic implementation was tested. The largest direct case was batch 512 by dimension 8192 with 16 spot checks.

## Claim scope

Synthetic logistic-regression batches on one CPU worker show that Merkle per-sample gradient spot checks can cheaply detect corrupted committed leaves with expected sampling probability, but the simple Merkle-only protocol does not bind the accepted aggregate update to the committed leaves.

## Why it stopped

Proxy/local evidence found a protocol-level gap: Merkle inclusion spot checks do not prove the reported aggregate gradient equals the committed leaves, so the simple idea is an early falsification rather than a full validation.

## Recommended next action

Stop this Merkle-only line as a standalone proof; next test should add and benchmark an aggregate-binding mechanism before any larger training validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Aggregate-binding audit for Merkle committed gradients
- Success threshold: Detect 100% of decoupled aggregate attacks in the harness, keep verifier time under 10% of full gradient recomputation for batch sizes at least 512, and preserve honest verification pass rate under deterministic quantized arithmetic.
- Stop condition: Stop if aggregate binding requires verifier work comparable to recomputing the full batch or if honest deterministic verification cannot be made reliable.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-ized-gradient-proofs-for-cpu-volunteer-training-2631634bc713`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
