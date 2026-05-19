# Real-Trace Evidence Ledger Evaluation for Tool-Use Agents

Status: `useful_signal`
Project ID: `real-trace-evidence-ledger-evaluation-for-tool-use-agents-a583987517`
Run ID: `real-trace-evidence-ledger-evaluation-for-tool-use-agents-a583987517-20260517T171504079914+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2e8dc4035b73

## What looked useful

Ledger-backed verification over real command-output evidence reached 100% accuracy and 0% false-support rate on 15 controlled claims; a naive accept-all baseline had 66.7% accuracy and 100% false-support rate.

## Boundaries and scale limits

Single short trace, controlled claims, narrow structured fact extraction, no open-domain entailment, no multi-agent or multi-task benchmark.

## Claim scope

On one real Codex tool-use trace, a deterministic evidence ledger over command outputs correctly classified 15 controlled cited claims, including rejecting all 5 deliberately unsupported tampered claims.

## Why it stopped

Useful Tier 1 direct mechanism signal, but single-trace controlled-claim evidence is not publication-grade validation.

## Recommended next action

Run a bounded deepen test on at least 20 real tool-use traces with manually labeled final-answer claims before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-Trace Evidence Ledger Verification on Real Agent Final Claims
- Success threshold: False-support rate <= 5%, support recall >= 80%, and improvement over no-ledger baseline on the same labeled claims.
- Stop condition: Stop as negative if false-support rate exceeds 10% or support recall falls below 70% on the labeled multi-trace set.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-evidence-ledger-evaluation-for-tool-use-agents-a583987517`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
