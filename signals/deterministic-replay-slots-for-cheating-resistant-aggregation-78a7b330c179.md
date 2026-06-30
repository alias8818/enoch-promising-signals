# Deterministic Replay Slots for Cheating-Resistant Aggregation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `deterministic-replay-slots-for-cheating-resistant-aggregation-78a7b330c179`
Run ID: `deterministic-replay-slots-for-cheating-resistant-aggregation-78a7b330c179-20260608T170635344194+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/fc88751159c5

## What looked useful

Commit-then-seed replay matched analytic detection closely (mean absolute Monte Carlo vs analytic delta 0.00559), while adaptive-known-seed cheating had 0.0 detection across all tested rows. Low-overhead audits can be useful for broad tampering but are weak for very sparse tampering.

## Boundaries and scale limits

150 synthetic scenarios, 1000 Monte Carlo trials per scenario, no real federated learning system, no cryptographic commitment implementation, no network/straggler/adversarial-collusion benchmark, and aggregate error proxied by tampered slot fraction.

## Claim scope

Synthetic slot-level aggregation audit model: deterministic replay slots detect tampering according to hypergeometric sampling probability when aggregate/contribution commitments are fixed before replay seed selection; they fail against an adaptive cheater that knows the replay slots before tampering.

## Why it stopped

No-paper useful signal: this run is synthetic/proxy evidence and also exposes a decisive known-seed adaptive failure mode; it is not a full validation of a deployed cheating-resistant aggregation protocol.

## Recommended next action

Build a toy committed aggregation prototype with Merkle commitments and post-commit replay seed derivation, then measure detection, proof bandwidth, verifier time, and end-to-end aggregation overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Committed Replay Slots in a Toy Federated Aggregator
- Success threshold: Detection within 5 percentage points of analytic prediction for commit-before-seed tampering, 0% or near-0% detection for the known-seed negative control, and measured verifier overhead below 5% at 1% to 5% audit coverage.
- Stop condition: Stop if commitment/proof overhead exceeds 20% in the smallest workload or if commit-before-seed detection deviates from analytic prediction by more than 10 percentage points after implementation bugs are ruled out.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-replay-slots-for-cheating-resistant-aggregation-78a7b330c179`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
