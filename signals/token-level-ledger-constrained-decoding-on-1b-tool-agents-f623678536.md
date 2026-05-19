# Token-Level Ledger-Constrained Decoding on 1B Tool Agents

Status: `useful_signal`
Project ID: `token-level-ledger-constrained-decoding-on-1b-tool-agents-f623678536`
Run ID: `token-level-ledger-constrained-decoding-on-1b-tool-agents-f623678536-20260514T203024849702+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Token-Level Ledger-Constrained Decoding on 1B Tool Agents: internal_generated:token-level-ledger-constrained-decoding-on-1b-tool-agents-f623678536

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Mechanism support only; this Tier 2 run used a synthetic constrained tool-planning benchmark and one 1B-class model, so it is insufficient for publication-grade claims about deployed 1B tool agents.

## Recommended next action

Stop this run as no-paper: the fixed-seed synthetic 1B-model evidence supports the ledger mechanism, but publication requires a full token-mask implementation in a real tool-agent harness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Tool-Agent Harness Evaluation for Ledger-Constrained Decoding
- Success threshold: Ledger-constrained decoding reduces budget/tool violations by at least 50% relative to the strongest baseline, preserves at least 95% of baseline task success, and keeps median decoding latency overhead below 25% on a fixed benchmark split.
- Stop condition: Stop if ledger constraints fail to beat retry/repair on violation rate, reduce task success below 95% of the best baseline, or add at least 25% median latency overhead after implementation tuning.

## Evidence references

- Artifact root: `<local-path>/projects/token-level-ledger-constrained-decoding-on-1b-tool-agents-f623678536`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
