# Real local-model tiered verification cascade on deterministic tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-local-model-tiered-verification-cascade-on-determinis-c4ed5f6fe6`
Run ID: `real-local-model-tiered-verification-cascade-on-determinis-c4ed5f6fe6-20260605T222009359746+0000`

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

- Parent run decision: Tiered Verification Cascade for Local Agent Reliability: enoch://control-plane/projects/tiered-verification-cascade-for-local-agent-reliability-f680fcc16f76/runs/tiered-verification-cascade-for-local-agent-reliability-f680fcc16f76-20260605T214316012868+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/1fd369b1bf6e

## What looked useful

Exact verification made the cascade safe and the stronger local tier rescued 18 of 44 cheap-model failures, but exact fallback was still required for 43.3% of tasks, so these tiers are not reliable enough for the stated deterministic-task threshold.

## Boundaries and scale limits

Small synthetic task family, one seed for the controlled run, two small local model tiers, no production workload, no larger local models, no adversarial prompt variation, and no comparison against exact-solver-first latency/cost.

## Claim scope

On a seeded 60-task deterministic arithmetic/linear-equation set, a two-tier local Qwen 0.5B to 1.5B verified cascade produced zero false accepts and improved model-verified accuracy from 26.7% to 56.7%, but did not meet the practical reliability threshold.

## Why it stopped

Controlled direct Tier 1 test missed the pre-registered threshold: best model-verified accuracy was 56.7% versus 90% required, and exact-solver fallback was 43.3% versus 10% allowed; this is a useful no-paper signal rather than full validation.

## Recommended next action

Run a bounded deepen test with a stronger local model tier on the same generator plus a second seed, and stop unless it reaches at least 90% model-verified accuracy, at most 10% exact fallback, and zero false accepts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stronger local-model tier for verified deterministic arithmetic cascade
- Success threshold: Across both seeds, model-verified accuracy >= 90%, exact solver fallback <= 10%, false accepts = 0, and at least 15 percentage points improvement over the cheap-only tier.
- Stop condition: Stop if the stronger local tier remains below 80% model-verified accuracy or above 20% exact fallback on the first seed, because it would still be far from the deterministic-task reliability target.

## Evidence references

- Artifact root: `<local-path>/projects/real-local-model-tiered-verification-cascade-on-determinis-c4ed5f6fe6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
