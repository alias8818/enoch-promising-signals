# Evidence-ledger rollback for tool-use agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-rollback-for-tool-use-agents-56aa37d3ad03`
Run ID: `evidence-ledger-rollback-for-tool-use-agents-56aa37d3ad03-20260604T173351093607+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c880fb01dc46

## What looked useful

Across 50,000 trials per policy, rollback reduced stale-evidence use to 0.0 in all contaminated scenarios. At failed-branch probabilities 0.10, 0.20, 0.35, and 0.50, baseline accuracy was 0.98844, 0.92196, 0.70406, and 0.42118 while rollback accuracy was 1.0. No-effect controls with no failures or no spurious failed-branch evidence showed zero delta.

## Boundaries and scale limits

Proxy-only local CPU simulation; no real LLM planner, real tool APIs, long-horizon memory, latency-overhead measurement, or production trace validation.

## Claim scope

In a deterministic synthetic tool-use benchmark where failed speculative branches emit plausible invalid answer evidence, evidence-ledger rollback prevents retained failed-branch evidence from contaminating final plurality answers.

## Why it stopped

Closed as no-paper useful signal because the evidence supports the mechanism only in a synthetic proxy benchmark, not in real agent traces.

## Recommended next action

Run a bounded real LLM tool-use trace harness comparing retained-evidence baseline versus rollback on tasks with injected timeout/retry and malformed-output failures.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real tool-use trace validation of evidence-ledger rollback
- Success threshold: Rollback reduces stale evidence/citation use by at least 50% relative to baseline and improves or preserves answer accuracy with less than 10% median latency overhead.
- Stop condition: Stop if rollback fails to reduce stale evidence/citation use by 20% on the first 100 paired tasks or causes more than 20% median latency overhead without accuracy gain.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-rollback-for-tool-use-agents-56aa37d3ad03`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
