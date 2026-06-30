# Evidence Ledger for Small Local Agent Consistency

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-small-local-agent-consistency-5d82869aecc5`
Run ID: `evidence-ledger-for-small-local-agent-consistency-5d82869aecc5-20260604T194315274376+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ae645af88749

## What looked useful

The ledger achieved 0.886953 mean accuracy versus 0.340656 for recency memory and 0.291922 for rolling summary; on full streams it reached 1.0 canonical, shuffled, and duplicate-heavy accuracy with 0.0 order sensitivity.

## Boundaries and scale limits

The run used 500 synthetic cases and deterministic memory policies, not a real local LLM, natural-language extraction, tool traces, or long-horizon deployed agent workflows.

## Claim scope

In a deterministic synthetic benchmark of generated structured evidence streams, an append-only evidence ledger with retraction handling and reliability-based conflict resolution produced substantially higher consistency than recency-only and rolling-summary memory baselines.

## Why it stopped

Closed as no-paper useful signal because the positive result is synthetic and deterministic rather than direct evidence from a real small local agent.

## Recommended next action

Run a bounded deepen follow-up with a real local small model extracting claims from natural-language observations, using this harness and the same ledger/control metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language local-agent evidence ledger consistency test
- Success threshold: Ledger condition improves mean held-out query accuracy by at least 0.15 absolute and reduces order sensitivity by at least 50% versus the best control without increasing missing rate by more than 0.05.
- Stop condition: Stop if the ledger improvement is below 0.05 absolute accuracy, if extraction errors dominate more than 50% of ledger failures, or if the setup cannot run locally under the 15 minute CPU-only ceiling.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-small-local-agent-consistency-5d82869aecc5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
