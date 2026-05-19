# Evidence Ledger for Small Agent Tool Calls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-small-agent-tool-calls-8a46fc204841`
Run ID: `evidence-ledger-for-small-agent-tool-calls-8a46fc204841-20260514T221233182536+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/13c56c7c9b90

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Proxy early validation only: synthetic one-claim tool-call cases support the structured-ledger mechanism but do not provide direct/full evidence from real agent traces.

## Recommended next action

Run a bounded direct-trace benchmark on real small-agent tool workflows; stop treating this run as paper-ready because it is proxy/synthetic evidence only.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Trace Audit Benchmark for Structured Evidence Ledgers
- Success threshold: Structured ledger improves unsupported-claim recall by at least 20 absolute percentage points over the strongest non-ledger baseline with false-positive rate no worse than 5 percentage points higher and median ledger overhead under 1.5 KB or 300 tokens per workflow.
- Stop condition: Stop if structured ledgers fail to beat raw transcript or raw tool-log baselines by 10 absolute recall points, exceed the overhead threshold, or require task-specific verifier rules that do not generalize across tool types.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-small-agent-tool-calls-8a46fc204841`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
