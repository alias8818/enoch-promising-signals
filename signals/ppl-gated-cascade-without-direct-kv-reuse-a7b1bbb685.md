# PPL-gated cascade without direct KV reuse

Status: `compute_scale_blocked`
Project ID: `ppl-gated-cascade-without-direct-kv-reuse-a7b1bbb685`
Run ID: `ppl-gated-cascade-without-direct-kv-reuse-a7b1bbb685-20260515T072246821122+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/74ae32019ff3

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 1 controlled direct test supports retrospective PPL/NLL gating, but the evidence is limited to 2048 WikiText-2 tokens and routed-token compute proxy; this is not full validation or publication-grade evidence.

## Recommended next action

Run a bounded medium confirmation with deployable gates, validation-selected thresholds, matched random controls, and actual no-KV-reuse latency/throughput measurement; stop this run as Tier 1 mechanism support but not paper-ready evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium validation of deployable PPL/uncertainty gates for no-KV-reuse LM cascades
- Success threshold: Held-out gated cascade recovers >=75% of large-only NLL improvement over small-only at <=50% large-model calls and shows a measured serving throughput or latency improvement over large-only without direct KV reuse.
- Stop condition: Stop if deployable gates fail to beat matched random routing by at least 10% relative NLL-gain recovery or if measured no-KV-reuse serving is not faster than large-only at the selected operating point.

## Evidence references

- Artifact root: `<local-path>/projects/ppl-gated-cascade-without-direct-kv-reuse-a7b1bbb685`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
