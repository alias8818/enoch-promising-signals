# Structured Evidence Ledger Constrains Tool Misuse in Small Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `structured-evidence-ledger-constrains-tool-misuse-in-small-agents-df13049acc87`
Run ID: `structured-evidence-ledger-constrains-tool-misuse-in-small-agents-df13049acc87-20260607T161634563882+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/94ace52d2eee

## What looked useful

Structured source/action/nonce evidence gates sharply separated from a freeform checklist: checklist misuse was 0.1661, full ledger misuse was 0.0000, no-source-filter ablation misuse was 0.1622 on poisoned ledger hints, and no-nonce ablation misuse was 0.1678 on replay attacks.

## Boundaries and scale limits

The experiment used generated episodes and hand-coded stochastic policies, not real LLM agents, real tool APIs, production prompt-injection corpora, or human task distributions. It is mechanism evidence only and is not publication-grade evidence for deployed agents.

## Claim scope

In a synthetic randomized small-agent tool-use benchmark, a structured evidence ledger requiring trusted source, exact tool/target/amount matching, non-revoked approval, and nonce binding reduced unsafe privileged tool misuse to 0 / 42836 unsafe episodes while preserving 0.9845 allowed-task completion.

## Why it stopped

Synthetic proxy evidence supports the mechanism but is insufficient for a paper or broad validation of real agents.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same ledger/checklist/baseline interface on actual small LLM agents in a sandbox.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evaluate structured evidence ledgers on sandboxed small LLM tool agents
- Success threshold: Ledger unsafe privileged tool misuse is at least 50% lower than checklist misuse with allowed-task completion at or above 85% across at least 300 held-out real-agent episodes.
- Stop condition: Stop if ledger misuse is not lower than checklist misuse, if allowed-task completion falls below 70%, or if real-agent tool-call parsing prevents a valid paired comparison.

## Evidence references

- Artifact root: `<local-path>/projects/structured-evidence-ledger-constrains-tool-misuse-in-small-agents-df13049acc87`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
