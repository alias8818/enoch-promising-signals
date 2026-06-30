# Holdout Overfit Proof-of-Work

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `holdout-overfit-proof-of-work-b6c723101237`
Run ID: `holdout-overfit-proof-of-work-b6c723101237-20260608T194713038652+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/32e06eb072fe

## What looked useful

Proof-of-work reduces adaptive holdout overfit only by reducing effective submission count; at equal submission counts it is statistically equivalent to a direct submission cap in this simulation.

## Boundaries and scale limits

Does not cover real leaderboard traces, trained model families with correlated errors, multi-account attackers, specialized PoW hardware, economic incentives, or deployed anti-Sybil systems.

## Claim scope

Synthetic adaptive public-holdout simulation with random 50%-private-accuracy classifiers and measured local SHA-256 Hashcash-style proof-of-work costs.

## Why it stopped

Medium synthetic/proxy evidence supports PoW as a throttle but not as a distinct holdout-overfit solution beyond submission caps.

## Recommended next action

Stop as no-paper useful signal unless a bounded follow-up directly tests PoW against equal effective submission caps on trained real-data model families.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: PoW versus equal submission caps on trained real-data leaderboard attacks
- Success threshold: If PoW reduces mean public-private overfit gap by at least 20% versus an equal effective submission cap without reducing private accuracy, treat the mechanism as worth further study; otherwise close as throttling-only.
- Stop condition: Stop if two datasets show PoW and equal caps differ by less than 5% relative overfit gap or if the adaptive attack fails to create at least a 2 percentage point public-private gap under the uncapped condition.

## Evidence references

- Artifact root: `<local-path>/projects/holdout-overfit-proof-of-work-b6c723101237`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
