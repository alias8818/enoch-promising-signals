# Lottery-Ticket Sparse Peer Validation for Volunteer Swarms

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `lottery-ticket-sparse-peer-validation-for-volunteer-swarms-b4817527ea83`
Run ID: `lottery-ticket-sparse-peer-validation-for-volunteer-swarms-b4817527ea83-20260608T111301452029+0000`

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

Plain sparse lottery assignment works in low-noise simulated swarms at k=3 with 20% of dense validation overhead, but degrades under adversarial validators. With oracle reputation, moderate Byzantine k=7 reached 0.0088 undetected bad rate and 0.0020 false reject rate at 46.7% of dense overhead; without reputation the same setting was 0.0271 and 0.0107. The core dependency is trustworthy validator scoring, not ticketing alone.

## Boundaries and scale limits

No live volunteer swarm, no cryptographic ticket implementation, no real workload correctness checks, no adaptive adversary, and best positive results depend on oracle-assisted reputation updates. High Byzantine sparse validation did not meet the 1% undetected-bad target.

## Claim scope

CPU Monte Carlo simulation of sparse lottery-ticket peer validation over 400 validators, 5,000 tasks per replicate, 10 replicates per condition, with low, moderate, and high Byzantine scenarios. Supports only a conditional mechanism claim: sparse validation is cost-effective in low-noise swarms and can be useful in moderate Byzantine swarms only when paired with reliable validator scoring.

## Why it stopped

Simulation provides proxy evidence and early falsification of the strong standalone sparse-lottery claim; strongest positive result depends on oracle reputation rather than a deployable protocol.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should replace oracle reputation with a deployable adjudication mechanism and require the moderate-Byzantine k=7 condition to keep undetected bad rate below 1.5% and false reject rate below 1%.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sparse Lottery Validation with Non-Oracle Reputation
- Success threshold: At k=7 and threshold=4, undetected bad rate below 0.015, false reject rate below 0.01, and validation overhead at or below 50% of dense k=15, without oracle reputation.
- Stop condition: Stop if non-oracle reputation cannot reduce malicious validator selection by at least 40% versus no-reputation lottery or if undetected bad rate remains above 0.03 in the moderate-Byzantine condition.

## Evidence references

- Artifact root: `<local-path>/projects/lottery-ticket-sparse-peer-validation-for-volunteer-swarms-b4817527ea83`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
