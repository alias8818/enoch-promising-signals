# Falsifiable Evidence Ledger for Tiny Tool-Use Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `falsifiable-evidence-ledger-for-tiny-tool-use-agents-6b2e0fda5fbc`
Run ID: `falsifiable-evidence-ledger-for-tiny-tool-use-agents-6b2e0fda5fbc-20260608T235111466501+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/aa358701de54

## What looked useful

A falsifiable evidence ledger strongly improved accuracy over stale-search baselines when a verifier existed, but it underperformed an equal-budget always-verify control at nonzero TTLs. Without a verifier, the ledger did not robustly improve correctness. The mechanism is an accuracy/tool-call tradeoff controlled by evidence reuse TTL.

## Boundaries and scale limits

No real LLM agents, real web/API tools, adversarial documents, natural-language parsing, or production memory systems were tested. Main evidence is 6400 synthetic answers per agent per verifier condition plus shorter TTL sensitivity runs.

## Claim scope

Synthetic dynamic-fact simulation for tiny tool-use agents with stale search, noisy rumor, and optional live verifier tools.

## Why it stopped

No paper-positive result: this was proxy/synthetic evidence showing a useful mechanism and a negative boundary, not direct validation on real tool-use agents.

## Recommended next action

Run a bounded deepen follow-up with actual tiny LLM agents on replayed web/API current-fact tasks, comparing ledger TTL policies against an equal-budget always-verify baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay-Based Evidence Ledger Test for Tiny LLM Tool Agents
- Success threshold: Ledger TTL policy achieves at least 95% of always-verify accuracy while reducing verifier/tool calls by at least 10%, and beats stale-search accuracy by at least 15 percentage points with bootstrap 95% CI excluding zero.
- Stop condition: Stop if ledger accuracy is more than 5 percentage points below always-verify at less than 10% call savings, or if gains over stale-search disappear under equal tool budgets.

## Evidence references

- Artifact root: `<local-path>/projects/falsifiable-evidence-ledger-for-tiny-tool-use-agents-6b2e0fda5fbc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
