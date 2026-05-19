# Natural Tool-Trace Ledger ReAct With Independent Semantic Verification

Status: `useful_signal`
Project ID: `natural-tool-trace-ledger-react-with-independent-semantic-609daf2f66`
Run ID: `natural-tool-trace-ledger-react-with-independent-semantic-609daf2f66-20260514T075526550338+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Natural Tool-Trace Ledger ReAct With Independent Semantic Verification: internal_generated:natural-tool-trace-ledger-react-with-independent-semantic-609daf2f66

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Bounded synthetic validation supports semantic replay for constrained parseable ledgers but directly falsifies robust unconstrained natural-ledger verification via zero accepted coverage on free-form traces; no real LLM evidence was produced, so this is not paper-ready.

## Recommended next action

Stop this run as a synthetic mixed result; if continuing the line, run a real LLM tool-use benchmark comparing plain ReAct, structured-ledger ReAct, syntax-only validation, and semantic verification on held-out tasks with adversarial trace perturbations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real LLM Tool-Trace Ledger Verification Under Constrained vs Free-Form Ledgers
- Success threshold: Semantic verification must improve accepted bad-trace rate by at least 20 percentage points over syntax-only validation while preserving at least 70% coverage on non-adversarial natural/paraphrased traces and at least 50% coverage under adversarial perturbations.
- Stop condition: Stop if free-form or paraphrased natural ledgers remain below 70% coverage, if accepted bad-trace reduction is under 20 percentage points, or if gains vanish against structured syntax-only controls.

## Evidence references

- Artifact root: `<local-path>/projects/natural-tool-trace-ledger-react-with-independent-semantic-609daf2f66`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
