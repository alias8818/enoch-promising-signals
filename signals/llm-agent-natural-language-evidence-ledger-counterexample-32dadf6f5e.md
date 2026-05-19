# LLM-Agent Natural-Language Evidence Ledger Counterexample Benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `llm-agent-natural-language-evidence-ledger-counterexample-32dadf6f5e`
Run ID: `llm-agent-natural-language-evidence-ledger-counterexample-32dadf6f5e-20260517T134649788997+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: LLM-Agent Natural-Language Evidence Ledger Counterexample Benchmark: internal_generated:llm-agent-natural-language-evidence-ledger-counterexample-32dadf6f5e

## What looked useful

Natural-language evidence ledgers showed +5.45 percentage-point raw lift on SmolLM2-135M and +2.55 percentage-point raw lift on Qwen2.5-0.5B versus no ledger, but paired exact tests were not significant versus no-ledger (p=0.072 and p=0.311). The terse-ledger control was inconsistent: worse than natural language on SmolLM2-135M but slightly better on Qwen2.5-0.5B.

## Boundaries and scale limits

Only two small local models completed full validation: SmolLM2-135M-Instruct and Qwen2.5-0.5B-Instruct. Qwen2.5-1.5B-Instruct completed a smoke run but the full run was interrupted after no trial progress. Tasks were template-generated finite-domain integer claims, not a broad human-authored agent benchmark.

## Claim scope

On a generated finite-domain integer counterexample benchmark with 55 false natural-language universal claims, fixed seeds, oracle validation, and two small cached local instruct models, natural-language evidence ledgers produced small raw success-rate lifts over a no-ledger baseline but did not significantly beat the no-ledger baseline in paired tests and did not consistently beat a terse-ledger control.

## Why it stopped

Bounded local validation found mixed, non-publication-grade evidence: small positive raw lifts for natural-language ledgers over no-ledger, but no statistically reliable paired win over the real baseline and inconsistent behavior against the terse control.

## Recommended next action

Stop this run as no-paper useful signal; if the controller allows one depth-4 deepen follow-up, run a timeout-safe batched larger-model sweep and require paired p<0.05 plus at least 5 percentage-point natural-language ledger lift over both no-ledger and terse-ledger controls on at least two model classes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Batched Larger-Model Evidence Ledger Counterexample Sweep
- Success threshold: Natural-language ledger improves success by at least 5 percentage points over both no-ledger and terse-ledger controls with paired p<0.05 on at least two model classes, without increasing invalid outputs or repeats enough to erase attempts-to-success gains.
- Stop condition: Stop as negative if natural-language ledger fails to beat no-ledger or terse-ledger by at least 5 percentage points on two completed model classes, or if larger models remain operationally unstable after adding batching, flushed progress, and per-call generation timeouts.

## Evidence references

- Artifact root: `<local-path>/projects/llm-agent-natural-language-evidence-ledger-counterexample-32dadf6f5e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
