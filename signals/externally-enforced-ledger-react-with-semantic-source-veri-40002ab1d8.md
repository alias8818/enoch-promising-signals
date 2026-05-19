# Externally Enforced Ledger ReAct With Semantic Source Verification

Status: `useful_signal`
Project ID: `externally-enforced-ledger-react-with-semantic-source-veri-40002ab1d8`
Run ID: `externally-enforced-ledger-react-with-semantic-source-veri-40002ab1d8-20260514T071446771919+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Externally Enforced Ledger ReAct With Semantic Source Verification: internal_generated:externally-enforced-ledger-react-with-semantic-source-veri-40002ab1d8

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 2 controlled fixed-seed evidence supports the mechanism but is not publication-grade because the benchmark is synthetic, single-model, and uses a template-based semantic verifier.

## Recommended next action

Stop this run as no-paper but mechanism-supported; run one bounded deepen follow-up on natural/tool-trace QA with an independent semantic verifier before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural Tool-Trace Ledger ReAct With Independent Semantic Verification
- Success threshold: External semantic enforcement improves task success by >=0.15 over both ReAct baseline and prompt-only ledger control, reduces unsupported answers by >=50% versus lexical verification, and has no more than 0.05 answerable-accuracy loss versus the best real baseline.
- Stop condition: Stop negative if the independent verifier fails to beat lexical verification by >=0.10 task success or causes >0.05 answerable-accuracy loss on the natural/tool-trace benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/externally-enforced-ledger-react-with-semantic-source-veri-40002ab1d8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
