# Real LLM Tool-Trace Ledger Verification Under Constrained vs Free-Form Ledgers

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `real-llm-tool-trace-ledger-verification-under-constrained-3b450fcc17`
Run ID: `real-llm-tool-trace-ledger-verification-under-constrained-3b450fcc17-20260514T084637540216+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Real LLM Tool-Trace Ledger Verification Under Constrained vs Free-Form Ledgers: internal_generated:real-llm-tool-trace-ledger-verification-under-constrained-3b450fcc17

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Bounded direct validation, not full real-world deployment evidence, falsified paper-readiness for this campaign: constrained ledgers did not robustly beat free-form across two Qwen-family LLMs, the no-schema ablation outperformed full constrained JSON for Qwen 1.5B, and LLM accuracy remained far below the always-unfaithful baseline on the fault-rich target set.

## Recommended next action

Stop this depth-4 follow-up as no-paper: bounded direct LLM validation produced mixed format effects and failed the usefulness gate against a trivial class-prior baseline; the controller follow-up cap prevents recommending another deepen/retry.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-llm-tool-trace-ledger-verification-under-constrained-3b450fcc17`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
