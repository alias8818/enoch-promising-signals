# Evidence Ledger for Agent Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-agent-reliability-b1c8740df42c`
Run ID: `evidence-ledger-for-agent-reliability-b1c8740df42c-20260613T091954999176+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f0a4cc9efb5b

## What looked useful

The ledger verifier achieved 1.000 precision, 1.000 recall, and 0 false positives on the primary 320-task run; answer-only checking achieved 1.000 precision but only 0.3958 recall, missing 116 provenance/tamper faults. Across 10 replicated seeds, ledger recall stayed 1.000 while answer-only recall averaged 0.4076.

## Boundaries and scale limits

Tested only on synthetic documents and deterministic verifier logic: 320-task primary run plus 10 replicated 320-task runs. No live LLM agent, no human grading, no adversarial semantic paraphrase cases, and no comparison against production observability systems.

## Claim scope

In a deterministic synthetic provenance benchmark, an append-only evidence ledger with source revision ids, quoted spans, span hashes, previous-record hashes, and record hashes made provenance faults and tampering machine-detectable compared with answer-only logs.

## Why it stopped

The result is a bounded synthetic mechanism validation, not direct publication-grade evidence for broad agent reliability.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should run a real retrieval-augmented agent over evolving documents and compare undetected failure rates with and without the ledger.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence ledger in a live retrieval-augmented agent workflow
- Success threshold: Ledger-enabled runs reduce undetected provenance/stale-source/tamper failures by at least 50% versus answer-only or unverified-citation logs without reducing answer accuracy by more than 5 percentage points.
- Stop condition: Stop if ledger verification fails to reduce undetected failures by at least 25% on a 100-task live-agent pilot or if overhead exceeds 2x wall-clock for the same task set.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-agent-reliability-b1c8740df42c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
