# Safe Tool-Use Ledger for 3B Agent

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `safe-tool-use-ledger-for-3b-agent-3facbe29863f`
Run ID: `safe-tool-use-ledger-for-3b-agent-3facbe29863f-20260529T144731044873+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f20cb0e4924a

## What looked useful

On 10,000 synthetic episodes, the ledger-aware checker reached F1 1.000 versus stateless F1 0.377, with bootstrap ledger-minus-stateless F1 delta p05/p50/p95 of 0.609/0.622/0.636. Hash-chain verification detected 200/200 tampered histories.

## Boundaries and scale limits

No real 3B model was run. The traces are synthetic, the oracle policy is hand-specified, and the result does not validate natural-language agent behavior, task success impact, runtime overhead in a live agent loop, or robustness to adversarial model behavior.

## Claim scope

A synthetic, executable tool-use benchmark shows that an append-only ledger carrying policy context, approvals, purpose, budget, and hash-chain history can detect cross-step unsafe tool-use violations that a stateless per-call checker misses.

## Why it stopped

Proxy-only useful signal; the mechanism is supported in synthetic traces but the 3B-agent claim needs direct agent evidence before paper writing.

## Recommended next action

Run the same ledger scaffold in a real local 3B-class tool-using agent environment with no-ledger, audit-only-ledger, and agent-visible-ledger conditions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real 3B Agent Ledger Intervention Evaluation
- Success threshold: Ledger-aware checking reduces unsafe tool calls by at least 50% relative to stateless checking while preserving at least 90% of baseline safe-task completion and keeping p95 audit overhead below 100 ms per tool call.
- Stop condition: Stop if the real 3B agent cannot complete at least 70% of safe baseline tool tasks, or if ledger checks add more than 250 ms p95 per tool call before showing a safety improvement.

## Evidence references

- Artifact root: `<local-path>/projects/safe-tool-use-ledger-for-3b-agent-3facbe29863f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
