# Structured Evidence Ledger Reduces Hallucinated Tool Calls in Small Agents

Status: `useful_signal`
Project ID: `structured-evidence-ledger-reduces-hallucinated-tool-calls-in-small-agents-417a2250bb0c`
Run ID: `structured-evidence-ledger-reduces-hallucinated-tool-calls-in-small-agents-417a2250bb0c-20260518T141638368101+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f96907f28b2e

## What looked useful

Composite hallucinated tool-call rate fell from 36.7% to 28.3% over two Qwen-0.5B runs, and unsupported tool calls fell from 30.6% to 20.6%. The ledger also increased missed required calls from 15.6% to 23.9% and invalid/unlisted calls from 4.4% to 8.3%, so the mechanism is mixed and appears partly driven by conservatism.

## Boundaries and scale limits

Only 180 paired tasks per condition on one small local model family; tasks were synthetic; tools were not executed; outputs were normalized from free-form text rather than native function calling; one attempted cross-model run was stopped for runtime.

## Claim scope

In a synthetic single-step tool-use benchmark using Qwen/Qwen2.5-0.5B-Instruct, a structured evidence ledger reduced composite hallucinated tool calls versus a prose baseline across two sampling seeds, mainly by reducing unsupported tool calls.

## Why it stopped

This run produced a bounded synthetic useful signal but not direct publication-grade evidence; the result is mixed because the ledger reduced unsupported calls while increasing missed required calls and some unlisted-tool errors.

## Recommended next action

Run a bounded deepen study in a real agent harness with executable tools, native structured outputs, at least two small models, and metrics that jointly penalize hallucinated calls and missed necessary calls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Executable-agent validation of evidence ledgers under calibrated abstention
- Success threshold: Ledger reduces composite hallucinated tool calls by at least 20% relative while keeping missed required tool calls within 2 percentage points of baseline and not lowering task success.
- Stop condition: Stop if the ledger's reduction disappears under executable tools/native structured outputs, or if gains are explained solely by reduced tool-call rate with materially higher missed required calls.

## Evidence references

- Artifact root: `<local-path>/projects/structured-evidence-ledger-reduces-hallucinated-tool-calls-in-small-agents-417a2250bb0c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
