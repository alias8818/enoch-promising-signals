# Counterexample Ledger Self-Critique: Bounded Verification Pass for Agent Outputs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `counterexample-ledger-self-critique-bounded-verification-pass-for-agent-outputs-1293240c855a`
Run ID: `counterexample-ledger-self-critique-bounded-verification-pass-for-agent-outputs-1293240c855a-20260620T102412020457+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c84521348d45

## What looked useful

Additional bounded verification checks substantially improved error recall, but the counterexample-ledger targeting mechanism was not reliably better than spending the same extra budget randomly. Equal-budget controls are required for future ledger self-critique claims.

## Boundaries and scale limits

Synthetic records and deterministic predicate checks only; no live LLM outputs, natural-language claim extraction, production traces, or model-call cost measurements. CPU-only runs completed in seconds and do not validate deployment-scale behavior.

## Claim scope

In a deterministic synthetic benchmark of 1200 checkable agent-style outputs per seed, a naive counterexample-ledger second pass improved recall over a 5-check single-pass baseline but did not robustly outperform an equal-budget random second pass.

## Why it stopped

Bounded synthetic evidence did not support a robust ledger-specific advantage over equal-budget random verification; this is a proxy negative/useful-signal result, not a full live-agent validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded work should test a per-output or learned ledger policy against equal-budget systematic and random controls on real LLM agent outputs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-output equal-budget test of per-output counterexample ledgers
- Success threshold: Ledger-guided verification improves error recall by at least 5 percentage points over both equal-budget controls without reducing precision by more than 2 percentage points, with bootstrap 95% interval excluding zero.
- Stop condition: Stop if ledger recall is within 2 percentage points of equal-budget controls or loses to either control on most domains/seeds.

## Evidence references

- Artifact root: `<local-path>/projects/counterexample-ledger-self-critique-bounded-verification-pass-for-agent-outputs-1293240c855a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
