# Volunteer Training Attestation via Proof-of-Work

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `volunteer-training-attestation-via-proof-of-work-ffc9f432a2f1`
Run ID: `volunteer-training-attestation-via-proof-of-work-ffc9f432a2f1-20260605T060114156259+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e8e619eb5e79

## What looked useful

Measured 717688 SHA-256 hashes/second locally and solved an 18-bit quiz-bound PoW in 1.00 seconds. For 10 four-choice questions with 22-bit PoW, secret answers multiply untrained expected work by 1048576x, but shared/leaked answers reduce the multiplier to exactly 1x, so the mechanism no longer distinguishes trained from untrained claimants.

## Boundaries and scale limits

No human volunteers, real courseware, identity binding, device diversity, outsourced solver market, or deployment-scale abuse study was run. The result is a bounded cryptographic/cost-model probe, not a full production validation.

## Claim scope

Mechanism-level local evaluation of proof-of-work for volunteer training attestation. Pure PoW proves compute only; quiz-answer-bound PoW increases blind guessing cost only while answers remain secret and collapses to compute-only PoW when answers are shared.

## Why it stopped

Early mechanism-level falsification: the local probe directly shows PoW attests compute, and answer-bound PoW loses its training-specific advantage when answers are transferable. This is not a full deployment validation.

## Recommended next action

Stop treating proof-of-work as a training attestation primitive; if used at all, scope it as quiz guessing rate limiting and pair it with a separate non-transferable identity or proctoring mechanism.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-training-attestation-via-proof-of-work-ffc9f432a2f1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
