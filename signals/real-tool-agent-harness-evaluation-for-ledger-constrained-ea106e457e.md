# Real Tool-Agent Harness Evaluation for Ledger-Constrained Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `real-tool-agent-harness-evaluation-for-ledger-constrained-ea106e457e`
Run ID: `real-tool-agent-harness-evaluation-for-ledger-constrained-ea106e457e-20260514T203901774283+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Real Tool-Agent Harness Evaluation for Ledger-Constrained Decoding: internal_generated:real-tool-agent-harness-evaluation-for-ledger-constrained-ea106e457e

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Bounded executable harness supports the safety mechanism versus unconstrained and syntax-only baselines, but a simple post-hoc repair baseline dominated ledger-constrained decoding on exact task success while preserving invalid-free execution; this is not paper-positive direct evidence.

## Recommended next action

Stop as paper-negative for this run; only pursue one depth-4 direct LLM follow-up if the controller wants to test token-level constrained decoding against post-hoc repair on realistic tool-agent tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-Level Ledger-Constrained Decoding vs Post-Hoc Repair on Real LLM Tool-Agent Tasks
- Success threshold: Ledger-constrained decoding must achieve invalid-free execution and improve exact task success by at least 5 absolute percentage points or reduce end-to-end cost/latency by at least 10% versus post-hoc repair, with paired 95% confidence intervals excluding zero.
- Stop condition: Stop if post-hoc repair matches invalid-free safety and remains within 5 absolute success points and 10% cost/latency of ledger-constrained decoding across the main benchmark conditions.

## Evidence references

- Artifact root: `<local-path>/projects/real-tool-agent-harness-evaluation-for-ledger-constrained-ea106e457e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
