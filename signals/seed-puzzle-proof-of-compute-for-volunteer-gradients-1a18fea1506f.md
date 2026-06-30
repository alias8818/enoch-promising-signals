# Seed-Puzzle Proof-of-Compute for Volunteer Gradients

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `seed-puzzle-proof-of-compute-for-volunteer-gradients-1a18fea1506f`
Run ID: `seed-puzzle-proof-of-compute-for-volunteer-gradients-1a18fea1506f-20260529T001157666963+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2f06b4594a63

## What looked useful

Fabricated and stale gradients solved the same puzzle and were accepted at 100%, matching honest acceptance, while their accepted updates worsened held-out loss. The puzzle proves nonce grinding over chosen bytes, not useful gradient computation.

## Boundaries and scale limits

Evidence is from a synthetic logistic-regression task with 5 seeds, 80 rounds per strategy, 64-dimensional gradients, and 12-bit puzzles. It does not evaluate large models, distributed systems, adaptive multi-worker attacks, or stronger verifier-held spot-check protocols.

## Claim scope

For a minimal seed/hash puzzle that binds SHA256(round_seed || submitted_gradient_bytes || nonce) to a volunteer gradient submission, verifier acceptance does not establish that useful minibatch gradient computation occurred.

## Why it stopped

Early bounded falsification: the tested puzzle verifier accepted arbitrary gradient bytes with valid nonces, so this proxy/direct semantic test fails before any large-scale volunteer-training validation is warranted.

## Recommended next action

Stop treating a gradient-bound seed puzzle alone as proof-of-compute; a bounded next test should add verifier-checkable hidden canary gradients or replicated spot checks and measure rejection of fabricated/stale submissions.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Verifier-held canary spot checks for volunteer gradient proof-of-usefulness
- Success threshold: Reject at least 95% of fabricated/stale submissions while accepting at least 95% of honest submissions, with less than 10% verifier-side compute overhead on the tested small tasks.
- Stop condition: Stop if adaptive fabricated or stale submissions pass above 20% acceptance at useful update magnitudes, or if verifier overhead exceeds recomputing the checked gradient.

## Evidence references

- Artifact root: `<local-path>/projects/seed-puzzle-proof-of-compute-for-volunteer-gradients-1a18fea1506f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
