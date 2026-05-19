# Self-correcting ledger for sub-3B agent reasoning

Status: `useful_signal`
Project ID: `self-correcting-ledger-for-sub-3b-agent-reasoning-9768cc0647f2`
Run ID: `self-correcting-ledger-for-sub-3b-agent-reasoning-9768cc0647f2-20260518T170523575469+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3a12a50e16d3

## What looked useful

Explicit ledger externalization can materially improve a capable 1.5B model on multi-step state arithmetic, while verifier repair produced a smaller paired gain of 3/40 over ledger prompting. The mechanism failed completely at 0.5B and is not paper-ready.

## Boundaries and scale limits

Synthetic arithmetic ledger tasks only; two cached Qwen sub-3B instruct models; 40-example main set per model; greedy decoding; no naturalistic agent traces, no standard reasoning benchmark, no training-time self-correction, and no long-horizon tool-use validation.

## Claim scope

Bounded synthetic state-tracking evaluation: on 40 deterministic ledger-arithmetic tasks with 6-10 transactions, Qwen2.5-1.5B-Instruct improved from 0% direct accuracy to 42.5% with ledger prompting and 50.0% with two verifier repair rounds; Qwen2.5-0.5B-Instruct remained at 0% in all modes.

## Why it stopped

No-paper useful signal: local synthetic evidence supports ledger externalization at 1.5B but only weakly supports verifier self-correction beyond ledger prompting, and the 0.5B tier fails entirely.

## Recommended next action

Run a bounded deepen follow-up on 1.5B and 3B-class models with 200+ examples, prompt ablations, stricter repair-format prompting, and one naturalistic state-tracking dataset; stop if self-correction adds less than 10 percentage points over ledger prompting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded ablation of verifier-repaired ledgers on small-model state tracking
- Success threshold: Self-correcting ledger accuracy is at least 10 percentage points above ledger prompting alone on 1.5B and 3B-class models without more than 2.5x latency versus ledger prompting.
- Stop condition: Stop if self-correction improves less than 5 percentage points over ledger prompting on the first 100 paired examples or if repair rounds commonly degrade previously valid ledgers.

## Evidence references

- Artifact root: `<local-path>/projects/self-correcting-ledger-for-sub-3b-agent-reasoning-9768cc0647f2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
