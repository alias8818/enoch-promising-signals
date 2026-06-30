# Sybil-Resistant Tiered Reputation for GB10 Volunteer Pools

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sybil-resistant-tiered-reputation-for-gb10-volunteer-pools-79975f6e7a61`
Run ID: `sybil-resistant-tiered-reputation-for-gb10-volunteer-pools-79975f6e7a61-20260612T235941945882+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3474a9ab489f

## What looked useful

Tiered probation and promotion cut accepted bad results by 78.6% versus flat reputation in fresh-Sybil churn, but increased accepted bad results by 522.9% to 881.8% under sleeper Sybils because burn-in audits certified attackers into higher scheduling tiers.

## Boundaries and scale limits

No real GB10 volunteer trace, no real identity-cost model, no collusion graph, no measured task verification cost, and no live deployment. Main evidence is 20-replicate CPU simulation over 4.8 million synthetic task assignments.

## Claim scope

Synthetic local simulation of GB10-style volunteer task scheduling with honest workers, fresh Sybil churn, and sleeper Sybils. Tiered reputation reduced fresh-Sybil accepted bad results but failed the broader Sybil-resistance claim under sleeper attackers.

## Why it stopped

Synthetic evidence is an early falsification of the unqualified Sybil-resistant tiered reputation claim, not a full validation or real deployment result.

## Recommended next action

Stop this run as a no-paper useful signal; test a bounded follow-up with persistent random audits, tier-demotion hysteresis, and cross-identity burst caps against the same sleeper attack.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sleeper-resistant tiered reputation with persistent audits and anomaly caps
- Success threshold: Sleeper accepted-bad-result rate no higher than the flat baseline plus 10% relative, fresh-Sybil accepted-bad-result reduction at least 40% versus flat, and audit overhead no more than 2.5x flat.
- Stop condition: Stop as negative if any ablated tiered variant still exceeds the flat sleeper accepted-bad-result rate by more than 10% relative or requires more than 2.5x audit overhead.

## Evidence references

- Artifact root: `<local-path>/projects/sybil-resistant-tiered-reputation-for-gb10-volunteer-pools-79975f6e7a61`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
