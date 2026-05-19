# Ledger-Constrained Decoding for Tool Truthfulness in 1B Agents

Status: `compute_scale_blocked`
Project ID: `ledger-constrained-decoding-for-tool-truthfulness-in-1b-agents-bdf902b9d85e`
Run ID: `ledger-constrained-decoding-for-tool-truthfulness-in-1b-agents-bdf902b9d85e-20260514T200847208167+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/75713d80857c

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Synthetic proxy evidence supports the mechanism for Qwen2.5-1.5B but is not full validation of real 1B tool-agent truthfulness, and Qwen2.5-0.5B showed wrong-in-ledger failures.

## Recommended next action

Stop this run as no-paper proxy evidence; next run should validate integrated ledger-constrained decoding on realistic multi-step tool traces with a 1B-class model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Based Ledger-Constrained Decoding for 1B Tool Agents
- Success threshold: At least +8 percentage points exact truthfulness and -50% unsupported/misleading answer rate versus baseline, with no more than +3 percentage points wrong-in-ledger errors on realistic traces.
- Stop condition: Stop if constraints fail to improve exact truthfulness by at least 3 percentage points on a 100-trace pilot or if wrong-in-ledger errors increase by more than the unsupported-answer reduction.

## Evidence references

- Artifact root: `<local-path>/projects/ledger-constrained-decoding-for-tool-truthfulness-in-1b-agents-bdf902b9d85e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
