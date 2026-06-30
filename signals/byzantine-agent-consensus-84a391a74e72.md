# Byzantine Agent Consensus

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `byzantine-agent-consensus-84a391a74e72`
Run ID: `byzantine-agent-consensus-84a391a74e72-20260526T113750996392+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b47c4530c038

## What looked useful

Agreement trimming failed to improve over plurality: agreement_trimmed_25 mean delta versus plurality was -0.0060 with 0/120 scenarios above +10 percentage points and 24/120 below -2 percentage points; agreement_trimmed_34 mean delta was -0.0139. Confidence weighting was unsafe under high-confidence collusion. Confidence capping showed a narrow low-fraction positive signal but was not robust broadly.

## Boundaries and scale limits

No real LLM traces, natural-language debate, adaptive multi-round adversaries, network protocol implementation, or production task distribution were tested. Evidence is a local synthetic proxy and should not be treated as broad Byzantine consensus validation.

## Claim scope

Synthetic 9-agent, 4-choice answer aggregation with 0-4 collusive Byzantine agents, honest accuracies 0.58-0.82, honest error correlations 0.0-0.7, and 5000 Monte Carlo trials per scenario.

## Why it stopped

Proxy early falsification: the directly tested synthetic aggregation setting did not support agreement trimming as a Byzantine defense, though full validation or reversal would require real multi-agent LLM answer traces with controlled adversaries.

## Recommended next action

Stop this run as a no-paper useful signal; the agreement-trimming hypothesis is proxy-falsified and should only be revisited with direct LLM trace evidence or a substantially different adversary detector.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Confidence-capped consensus on real multi-agent answer traces
- Success threshold: Confidence capping beats plurality by at least 5 percentage points mean accuracy with no scenario worse than plurality by more than 2 percentage points under f <= floor((n-1)/3).
- Stop condition: Stop if confidence capping loses to plurality by more than 2 percentage points in two or more controlled trace scenarios or fails to beat plurality by at least 5 percentage points on average.

## Evidence references

- Artifact root: `<local-path>/projects/byzantine-agent-consensus-84a391a74e72`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
