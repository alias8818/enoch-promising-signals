# Empirical-Confidence Gating for Non-Reversible Agent Actions

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `empirical-confidence-gating-for-non-reversible-agent-actions-cd40a83e5928`
Run ID: `empirical-confidence-gating-for-non-reversible-agent-actions-cd40a83e5928-20260628T223543394685+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/edbe5c5bae6d

## What looked useful

Raw confidence thresholds remained unsafe in overconfidence and distribution-shift scenarios. Empirical lower-bound gating served as a conservative safety brake; it improved harm control in the harm-cost-5 sensitivity run but collapsed to full review for the primary harm-cost-20 setting.

## Boundaries and scale limits

No real LLM agents, real operator labels, production tool traces, or real irreversible-loss model were evaluated; the evidence is limited to stochastic simulation with 30 seeds per scenario.

## Claim scope

In a deterministic synthetic simulation of non-reversible agent actions, empirical Wilson lower-bound confidence gating reduces harmful executions versus raw confidence thresholds, but under high irreversible-harm cost it abstains from all autonomous execution.

## Why it stopped

Synthetic evidence is useful but mixed: the mechanism prevents harmful raw-confidence overexecution, yet the primary high-harm configuration enables no autonomous execution and is not a full validation.

## Recommended next action

Stop this run as no-paper useful signal; next, evaluate the same empirical lower-bound gate on labeled real-agent irreversible-action proposals with a predeclared harm/review utility model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent trace validation of empirical gates for irreversible tool actions
- Success threshold: Empirical lower-bound gating has lower harmful-execution rate than raw threshold gating, positive execution rate above 1% in at least one action class, and equal or better utility under the predeclared risk model.
- Stop condition: Stop if empirical gating either abstains on all real-agent action classes or has harmful-execution rate not lower than raw confidence threshold gating.

## Evidence references

- Artifact root: `<local-path>/projects/empirical-confidence-gating-for-non-reversible-agent-actions-cd40a83e5928`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
