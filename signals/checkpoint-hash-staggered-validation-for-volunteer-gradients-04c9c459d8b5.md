# Checkpoint-Hash Staggered Validation for Volunteer Gradients

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `checkpoint-hash-staggered-validation-for-volunteer-gradients-04c9c459d8b5`
Run ID: `checkpoint-hash-staggered-validation-for-volunteer-gradients-04c9c459d8b5-20260525T215511105429+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e67dcf88cc54

## What looked useful

Checkpoint-hash metadata is useful as a low-cost freshness filter for honest stale submissions, rejecting about 404-406 stale submissions per 2,000-step run at 20% stale workers. It is not a provenance proof: when stale workers falsely claimed the current hash, hash rejection dropped to zero and only recomputation caught them. At 40% malicious plus 20% stale workers, checkpoint-hash staggered validation reduced noise-attack loss ratio from 1.095 to 1.036 and sign-flip loss ratio from 1.067 to 1.024 versus no validation, but accepted bad-gradient rates remained around 0.32-0.34 and immediate random validation was similar or slightly better.

## Boundaries and scale limits

Evidence is from CPU-only synthetic linear-regression simulations: 1,080 full-sweep runs plus 120 adversarial-stale runs. It does not include real distributed volunteer infrastructure, large neural models, adaptive adversaries, bandwidth constraints, cryptographic worker identity, or proof that a claimed checkpoint hash was actually used to compute a gradient.

## Claim scope

In a deterministic synthetic volunteer-SGD simulator, checkpoint hashes cheaply reject truthfully reported stale-checkpoint gradients, and 5% recomputation validation reduces accepted malicious-gradient damage, but staggered validation is not consistently better than immediate random validation at the same budget.

## Why it stopped

Bounded simulation produced a mixed result: useful freshness-filter evidence, but no support for checkpoint hashes as gradient provenance validation or for staggered validation superiority over random validation.

## Recommended next action

Stop this run as no-paper useful signal; a follow-up should test whether adaptive validation-budget scheduling can beat immediate random validation while keeping accepted invalid gradients below 10% in the same simulator.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Validation Budgeting for Checkpoint-Hashed Volunteer Gradients
- Success threshold: Accepted invalid-gradient rate below 10% and final loss ratio no worse than 1.02 under 20% malicious plus 20% stale workers, at recomputation cost per step no higher than 0.08, with improvement over immediate random validation in at least two of three attack types.
- Stop condition: Stop negative if adaptive validation cannot beat immediate random validation at matched cost or requires more than 8% recomputation to keep invalid accepted gradients below 10%.

## Evidence references

- Artifact root: `<local-path>/projects/checkpoint-hash-staggered-validation-for-volunteer-gradients-04c9c459d8b5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
