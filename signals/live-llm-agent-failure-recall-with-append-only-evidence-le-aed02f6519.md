# Live LLM-agent failure recall with append-only evidence ledger

Status: `useful_signal`
Project ID: `live-llm-agent-failure-recall-with-append-only-evidence-le-aed02f6519`
Run ID: `live-llm-agent-failure-recall-with-append-only-evidence-le-aed02f6519-20260514T073506587536+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Live LLM-agent failure recall with append-only evidence ledger: internal_generated:live-llm-agent-failure-recall-with-append-only-evidence-le-aed02f6519

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 2 synthetic online evidence met the internal success threshold, but this is still simulator evidence rather than direct live LLM-agent evidence, so it cannot justify finalize_positive.

## Recommended next action

Stop this run as mechanism-supported but not paper-ready; next, validate the same append-only ledger protocol on real LLM-agent failure traces with verified corrective actions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace validation of append-only failure evidence ledger
- Success threshold: Append-only evidence ledger improves repeat-failure recall by >=15 percentage points over the strongest baseline with 95% CI lower bound >0 and novel-failure false positive rate <=5%.
- Stop condition: Stop if the ledger fails to beat the strongest baseline by 5 percentage points on repeat-failure recall, exceeds 10% novel-failure false positives, or requires hand-labeled schema knowledge unavailable at inference time.

## Evidence references

- Artifact root: `<local-path>/projects/live-llm-agent-failure-recall-with-append-only-evidence-le-aed02f6519`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
