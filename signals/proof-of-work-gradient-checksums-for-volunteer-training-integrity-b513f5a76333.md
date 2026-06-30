# Proof-of-Work Gradient Checksums for Volunteer Training Integrity

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `proof-of-work-gradient-checksums-for-volunteer-training-integrity-b513f5a76333`
Run ID: `proof-of-work-gradient-checksums-for-volunteer-training-integrity-b513f5a76333-20260605T104529880411+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/5be133f499a0

## What looked useful

All fabricated, stale, and copied gradients with valid nonces were accepted at the same 100% rate as honest gradients. A 100% random-gradient run accepted 320/320 fake submissions and did not converge like the honest control. Hash cost benchmarks showed PoW adds cost but not provenance.

## Boundaries and scale limits

Synthetic MLP, 8836 parameters, 40 rounds, 8 volunteers, local GB10 worker. This is not a large-model or real-network validation, but the verifier failure is semantic and does not depend on model scale.

## Claim scope

A pure proof-of-work checksum that hashes submitted gradient bytes with a nonce can rate-limit submissions but does not verify that a volunteer computed the gradient from the assigned model/data; this was directly tested on a synthetic PyTorch volunteer-training harness with honest, random, stale, and copied gradients.

## Why it stopped

Proxy-scale but direct early falsification: the verifier accepts arbitrary gradient bytes once the attacker mines a nonce, so the design proves hash work over submitted bytes rather than gradient provenance.

## Recommended next action

Stop this pure PoW-gradient-checksum design as an integrity mechanism; only revisit with an added secret challenge, recomputation audit, trusted execution, or cryptographic proof that binds the proof to actual training computation.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/proof-of-work-gradient-checksums-for-volunteer-training-integrity-b513f5a76333`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
