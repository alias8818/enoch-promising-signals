# Evidence-Ledger Gating for Tool-Using Home Agent

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-gating-for-tool-using-home-agent-c29c48f495f4`
Run ID: `evidence-ledger-gating-for-tool-using-home-agent-c29c48f495f4-20260528T050851117042+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b47b93fd62bd

## What looked useful

Strict evidence gating prevented all unsafe executions in two 20,000-episode synthetic runs, including a high-instrumentation condition, while a lenient stale-evidence ablation leaked 239 unsafe executions. The mechanism is useful but conservative: default trusted sensor coverage caused a 32.37 percentage point success-rate loss, reduced to 7.28 points with higher coverage.

## Boundaries and scale limits

Synthetic policy and environment only; no real LLM traces, smart-home integrations, human interaction data, or multiday state drift. Runs were CPU-only and bounded to 20,000 simulated episodes per condition.

## Claim scope

In a synthetic home-agent simulator with explicit side-effectful action preconditions, a trusted-and-fresh evidence-ledger gate reduced unsafe tool executions versus an ungated policy, but completion depended strongly on trusted sensor coverage.

## Why it stopped

Closed as no-paper useful signal: synthetic evidence supports the safety mechanism but also shows completion-cost risk, so the result is not publication-grade direct validation.

## Recommended next action

Run a bounded direct-evidence follow-up with an active verification/recovery loop on real or LLM-generated home-agent traces; do not write a paper from this synthetic-only result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Active Verification Recovery for Evidence-Ledger Home-Agent Gating
- Success threshold: Unsafe execution rate at least 80% lower than ungated baseline, false block rate below 10% among safe proposals, and task success loss below 5 percentage points versus ungated baseline on the trace benchmark.
- Stop condition: Stop if active verification cannot reduce false blocks below 20% without allowing more than half of baseline unsafe executions, or if trace labels show action preconditions are too ambiguous for reproducible gating.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-gating-for-tool-using-home-agent-c29c48f495f4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
