# Cryptographic Spot-Check Validation for Volunteer CPU Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cryptographic-spot-check-validation-for-volunteer-cpu-training-29096bbcdffa`
Run ID: `cryptographic-spot-check-validation-for-volunteer-cpu-training-29096bbcdffa-20260630T035924677305+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9c1f2304a1b1

## What looked useful

Cryptographic commit-then-HMAC spot checks detect corrupted volunteer gradient shards at the expected hypergeometric rate. Detection is strong for moderate/blatant corruption but sparse 1% corruption remains poorly detected even at 50% verifier recomputation overhead.

## Boundaries and scale limits

Local CPU-only simulation: logistic-regression gradients, 128 examples/shard, 16 dimensions, non-adaptive random row corruption, no real distributed trainer, no adaptive/colluding adversaries, no privacy-preserving verification.

## Claim scope

Toy logistic-regression gradient shards with SHA-256 Merkle commitments and post-commit HMAC spot-check challenges under non-adaptive random row corruption.

## Why it stopped

Bounded simulation supports the mechanism but also shows sparse-corruption weakness; evidence is not a full validation of volunteer CPU training security.

## Recommended next action

Stop this run as no-paper useful signal; next bounded step is a real multi-process volunteer-training prototype with adversarial workers and end-to-end model-quality impact.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end adversarial volunteer CPU training spot-check prototype
- Success threshold: At <=25% verifier recomputation overhead, reduce final model-quality degradation from >=10% corrupted shard attacks by at least 80% versus no validation while keeping false rejections below 1%.
- Stop condition: Stop if <=25% overhead fails to detect enough moderate corruption to improve final model quality over no-validation controls, or if sparse adaptive attacks dominate without a bounded mitigation.

## Evidence references

- Artifact root: `<local-path>/projects/cryptographic-spot-check-validation-for-volunteer-cpu-training-29096bbcdffa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
