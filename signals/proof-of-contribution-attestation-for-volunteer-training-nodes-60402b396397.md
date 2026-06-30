# Proof-of-Contribution Attestation for Volunteer Training Nodes

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `proof-of-contribution-attestation-for-volunteer-training-nodes-60402b396397`
Run ID: `proof-of-contribution-attestation-for-volunteer-training-nodes-60402b396397-20260611T080431812812+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/6237e930df94

## What looked useful

Spot-check proof-of-contribution is a plausible lightweight filter for coarse freeloading, but high-effort partial freeloaders retain meaningful pass probability unless challenge size, repeated checks, and penalties are tuned.

## Boundaries and scale limits

Toy synthetic data, logistic-regression gradients, one local process, deterministic NumPy recomputation, no real volunteer nodes, no network/identity layer, no GPU nondeterminism, no mixed precision, no large model optimizer state, no privacy-preserving proof system, and no end-to-end adversarial training quality measurement.

## Claim scope

In a local deterministic logistic-gradient simulation, challenge-after-commit per-example gradient spot checks detected naive zero/random freeloading in 100% of trials, stale/replay freeloading in at least 99.95% of trials, and 50%-compute partial freeloading in 99.7% of trials when the verifier recomputed 8 of 128 batch examples.

## Why it stopped

No-paper useful signal: this was a bounded synthetic mechanism test, not a full validation of volunteer training-node attestation.

## Recommended next action

Run a bounded local multi-process PyTorch follow-up with repeated rounds, mixed precision tolerances, adaptive adversaries, and a reward/slashing cost model before considering any paper or production claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Repeated-Round PyTorch Attestation With Adaptive Partial Freeloaders
- Success threshold: Across at least 100 repeated local rounds, honest false rejects stay below 1%, 50%-compute freeloading is detected or made negative-EV in at least 99% of runs, and 90%-compute freeloading is either detected above 95% cumulatively or shown to require verifier overhead above the useful threshold.
- Stop condition: Stop if honest false rejects exceed 1% after tolerance calibration, if nondeterministic recomputation prevents reliable verification, or if 90%-compute freeloading remains positive-EV under verifier recomputation of 10% or less.

## Evidence references

- Artifact root: `<local-path>/projects/proof-of-contribution-attestation-for-volunteer-training-nodes-60402b396397`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
