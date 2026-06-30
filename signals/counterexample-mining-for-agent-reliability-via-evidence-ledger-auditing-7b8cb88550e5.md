# Counterexample Mining for Agent Reliability via Evidence Ledger Auditing

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `counterexample-mining-for-agent-reliability-via-evidence-ledger-auditing-7b8cb88550e5`
Run ID: `counterexample-mining-for-agent-reliability-via-evidence-ledger-auditing-7b8cb88550e5-20260525T095401192632+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/74ba39470e6c

## What looked useful

Evidence ledgers are useful as an audit substrate in this bounded probe: they expose unsupported claims, stale evidence, contradictions, wrong citations, and ignored tool errors that transcript-only and final-answer-only checks miss. The included harness and minimized examples provide a reproducible starting point for real-trace evaluation.

## Boundaries and scale limits

Synthetic-only traces; hand-specified failure taxonomy; rule-based auditor matched to the ledger schema; no real LLM agent traces, no human labels, no ambiguous evidence, no adversarial transcript manipulation, and no deployment-scale validation.

## Claim scope

In a deterministic synthetic benchmark of tool-using agent traces with explicit evidence ledgers and five seeded reliability failure types, rule-based evidence-ledger auditing detected all seeded failures and mined compact claim-level counterexamples while simple transcript-keyword and final-answer/world-state baselines missed most chronology/evidence failures.

## Why it stopped

No-paper closure: the evidence is a synthetic mechanism probe with useful signal, not a direct real-agent validation or publication-grade result.

## Recommended next action

Run a bounded deepen follow-up on real or replayed LLM agent traces with gold/human labels, using the same ledger schema and comparing against transcript heuristics, final-answer checks, and an LLM judge.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger auditing on labeled real agent traces
- Success threshold: At least 20 percentage points higher recall than the strongest non-ledger baseline on labeled evidence-related failures, with false-positive rate no more than 5 percentage points worse and at least 30 useful minimized counterexamples judged actionable.
- Stop condition: Stop if real-trace false-positive rate exceeds 20% at useful recall, if ledger fields are too inconsistently available to audit, or if an LLM judge matches ledger recall and precision without structured ledger access.

## Evidence references

- Artifact root: `<local-path>/projects/counterexample-mining-for-agent-reliability-via-evidence-ledger-auditing-7b8cb88550e5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
