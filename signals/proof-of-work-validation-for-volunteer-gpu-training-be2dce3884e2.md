# Proof-of-Work Validation for Volunteer GPU Training

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `proof-of-work-validation-for-volunteer-gpu-training-be2dce3884e2`
Run ID: `proof-of-work-validation-for-volunteer-gpu-training-be2dce3884e2-20260609T215457121271+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/057a62b6fedd

## What looked useful

PoW can throttle update submissions with sub-microsecond verification cost, but a fabricated non-training update with a valid proof was accepted at both tested difficulties. PoW-only validation should not be treated as proof of useful volunteer GPU training.

## Boundaries and scale limits

Single-host synthetic toy model only; no multi-volunteer network, no large-model convergence test, no remote attestation, no hidden-batch recomputation, and no economic test against specialized hashpower.

## Claim scope

Bounded local hashcash-style PoW probe on a GB10 toy training workload. The tested PoW-only verifier cheaply verifies proofs and binds them to submitted update digests, but it does not validate that the digest came from honest GPU training.

## Why it stopped

Early direct falsification of the PoW-only validation claim: a worker that did no training solved PoW for a fabricated update digest and was accepted by the PoW-only verifier. This is not a full volunteer-scale validation.

## Recommended next action

Stop this PoW-only validation line as no-paper; run a bounded follow-up that combines PoW admission with hidden canary gradient spot checks against honest, random, replay, and fabricated-update workers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PoW plus hidden canary gradient spot checks for volunteer training validation
- Success threshold: PoW-plus-canary rejects at least 95% of fabricated/replay/random updates in a seeded adversarial suite while accepting at least 95% of honest updates and keeping verifier overhead below 10 ms per update on the local host.
- Stop condition: Stop if fabricated or replayed updates still pass above 5%, or if verifier overhead exceeds 10 ms per update before reaching the rejection threshold.

## Evidence references

- Artifact root: `<local-path>/projects/proof-of-work-validation-for-volunteer-gpu-training-be2dce3884e2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
